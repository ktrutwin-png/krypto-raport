# -*- coding: utf-8 -*-
"""
Agent „Kraken Pro" – boty na sucho (paper trading), margin do 10x jak na Kraken Pro.
Nie składa ŻADNYCH zleceń. Używa tylko publicznych cen Krakena (bez kluczy API).

Każdy bot ma własne wirtualne 500 EUR, gra LONG i SHORT na XRP/EUR, BTC/EUR, ETH/EUR.
Wejście (reguła szefa nr 1 z MT5): 3 ostatnie zamknięte świece M15 w tym samym kolorze
= kierunek, potwierdzony trendem H1 (EMA20 vs EMA50).
Wyjście: KRÓTKI TP + przesuwany SL (od 15.11 na życzenie szefa): start 1,5 x odległość do TP,
gdy cena przejdzie połowę drogi do TP -> SL na zero (pokrywa opłaty), potem SL idzie za ceną
w odległości 0,5 x dystans TP (im bliżej celu, tym ciaśniej). Pozycje otwarte przed 15.11 grają po staremu (bez SL).
Dodatkowa ochrona = likwidacja jak na Krakenie
(cross margin: poziom depozytu < 40% całego konta bota → zamknięcie wszystkiego).
Koszty jak na Kraken Pro (najniższy próg): wejście rynkowe 0.40%, TP limitem 0.25%,
otwarcie marginu 0.02%, rollover 0.02% co 4 h.
"""
import json, os, sys, time, csv, urllib.request, urllib.parse
from datetime import datetime, timezone

KAT = os.path.dirname(os.path.abspath(__file__))
PARY = {"XRP/EUR": "XRPEUR", "BTC/EUR": "XBTEUR", "ETH/EUR": "ETHEUR"}
KAPITAL = 500.0
DZWIGNIA = 10
DEPOZYT_NA_POZYCJE = 50.0          # 50 EUR własne x10 = 500 EUR pozycji
MAX_POZYCJI = 3
FEE_TAKER, FEE_MAKER = 0.0040, 0.0025
FEE_MARGIN_OPEN, FEE_ROLLOVER = 0.0002, 0.0002
LIKWIDACJA = 0.40
SL_START = 1.5      # SL startowy = 1,5 x odległość wejście->TP
SL_PROG_BE = 0.5    # po przejściu 50% drogi do TP SL idzie na zero (z opłatami)
SL_TRAIL = 0.5      # potem SL ciągnie się za najlepszą ceną w odległości 0,5 x dystans TP
KOSZT_RT = FEE_TAKER + FEE_MAKER + FEE_MARGIN_OPEN   # koszty wejścia+wyjścia (do progu „na zero")

# Krótkie TP – nasze liczby. TP szefa na złocie (+0.3%) nie pokryje opłat Krakena
# (ok. 0.65-0.8% w obie strony), więc najkrótsze sensowne TP to ok. 0.8%.
BOTY = {
    "KP_krotki_0.8": {"tp": 0.008},
    "KP_sredni_1.2": {"tp": 0.012},
    "KP_ATR":        {"tp": "atr"},   # max(0.8%, 1x ATR(14) z H1)
}


def teraz():
    return datetime.now(timezone.utc)


def log(msg):
    linia = f"{teraz():%Y-%m-%d %H:%M:%S} {msg}"
    print(linia, flush=True)
    with open(os.path.join(KAT, "agent.log"), "a", encoding="utf-8") as f:
        f.write(linia + "\n")


def api(sciezka, **par):
    url = "https://api.kraken.com/0/public/" + sciezka + "?" + urllib.parse.urlencode(par)
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "hexa-paper"}), timeout=20) as r:
        d = json.load(r)
    if d.get("error"):
        raise RuntimeError(d["error"])
    return d["result"]


def swiece(para, interwal):
    res = api("OHLC", pair=para, interval=interwal)
    klucz = [k for k in res if k != "last"][0]
    # [time, open, high, low, close, vwap, volume, count]; ostatnia = jeszcze otwarta
    return [(int(s[0]), float(s[1]), float(s[2]), float(s[3]), float(s[4])) for s in res[klucz]][:-1]


def cena(para):
    res = api("Ticker", pair=para)
    t = list(res.values())[0]
    return float(t["b"][0]), float(t["a"][0]), float(t["c"][0])   # bid, ask, last


def ema(v, n):
    k, e = 2 / (n + 1), v[0]
    for x in v[1:]:
        e = x * k + e * (1 - k)
    return e


def atr_pct(s, n=14):
    tr = [max(s[i][2] - s[i][3], abs(s[i][2] - s[i - 1][4]), abs(s[i][3] - s[i - 1][4])) for i in range(1, len(s))]
    return (sum(tr[-n:]) / n) / s[-1][4]


def sygnal(m15, h1):
    o = m15[-3:]
    zielone = all(x[4] > x[1] for x in o)
    czerwone = all(x[4] < x[1] for x in o)
    zam = [x[4] for x in h1[-120:]]
    trend_w_gore = ema(zam, 20) > ema(zam, 50)
    if zielone and trend_w_gore:
        return "LONG"
    if czerwone and not trend_w_gore:
        return "SHORT"
    return None


def wczytaj(nazwa):
    p = os.path.join(KAT, f"stan_{nazwa}.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {"gotowka": KAPITAL, "pozycje": [], "ostatnia_swieca": {}, "likwidacje": 0,
            "start": teraz().isoformat()}


def zapisz(nazwa, st):
    p = os.path.join(KAT, f"stan_{nazwa}.json")
    with open(p + ".tmp", "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=1)
    os.replace(p + ".tmp", p)


def zapisz_transakcje(wiersz):
    p = os.path.join(KAT, "transakcje.csv")
    nowy = not os.path.exists(p)
    with open(p, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nowy:
            w.writerow(["czas_zamkniecia", "bot", "para", "kierunek", "wejscie", "wyjscie", "ilosc",
                        "wynik_eur", "oplaty_eur", "powod", "czas_otwarcia"])
        w.writerow(wiersz)


def pnl(poz, c):
    r = (c - poz["wejscie"]) if poz["kierunek"] == "LONG" else (poz["wejscie"] - c)
    return r * poz["ilosc"]


def zamknij(nazwa, st, poz, c, powod, fee):
    oplata = c * poz["ilosc"] * fee
    wynik = pnl(poz, c) - oplata
    st["gotowka"] += wynik
    poz["oplaty"] += oplata
    st["pozycje"].remove(poz)
    netto = pnl(poz, c) - poz["oplaty"]          # po wszystkich opłatach (otwarcie, rollover, zamknięcie)
    zapisz_transakcje([teraz().isoformat(timespec="seconds"), nazwa, poz["para"], poz["kierunek"],
                       poz["wejscie"], c, round(poz["ilosc"], 6), round(netto, 4),
                       round(poz["oplaty"], 4), powod, poz["otwarta"]])
    log(f"[{nazwa}] ZAMKNIĘTA {poz['kierunek']} {poz['para']} {poz['wejscie']} -> {c} | {netto:+.2f} EUR netto ({powod})")


def obieg():
    ceny, dane = {}, {}
    for nazwa_pary, kod in PARY.items():
        try:
            ceny[nazwa_pary] = cena(kod)
            dane[nazwa_pary] = (swiece(kod, 15), swiece(kod, 60))
        except Exception as e:
            log(f"BŁĄD danych {nazwa_pary}: {e}")
    for nazwa, cfg in BOTY.items():
        st = wczytaj(nazwa)
        t = teraz()
        # rollover co 4 h
        for poz in st["pozycje"]:
            ost = datetime.fromisoformat(poz["rollover"])
            while (t - ost).total_seconds() >= 4 * 3600:
                koszt = poz["wejscie"] * poz["ilosc"] * FEE_ROLLOVER
                st["gotowka"] -= koszt
                poz["oplaty"] += koszt
                ost = ost.fromtimestamp(ost.timestamp() + 4 * 3600, timezone.utc)
            poz["rollover"] = ost.isoformat()
        # przesuwany SL (tylko pozycje z polem "sl")
        for poz in list(st["pozycje"]):
            if "sl" not in poz or poz["para"] not in ceny:
                continue
            bid, ask, _ = ceny[poz["para"]]
            dyst = abs(poz["tp"] - poz["wejscie"])
            if poz["kierunek"] == "LONG":
                poz["best"] = max(poz["best"], bid)
                postep = (poz["best"] - poz["wejscie"]) / dyst
                if postep >= SL_PROG_BE:
                    nowy = max(poz["wejscie"] * (1 + KOSZT_RT), poz["best"] - SL_TRAIL * dyst)
                    poz["sl"] = max(poz["sl"], nowy)
                if bid <= poz["sl"]:
                    zamknij(nazwa, st, poz, poz["sl"], "SL" if poz["sl"] < poz["wejscie"] else "SL_TRAIL", FEE_TAKER)
            else:
                poz["best"] = min(poz["best"], ask)
                postep = (poz["wejscie"] - poz["best"]) / dyst
                if postep >= SL_PROG_BE:
                    nowy = min(poz["wejscie"] * (1 - KOSZT_RT), poz["best"] + SL_TRAIL * dyst)
                    poz["sl"] = min(poz["sl"], nowy)
                if ask >= poz["sl"]:
                    zamknij(nazwa, st, poz, poz["sl"], "SL" if poz["sl"] > poz["wejscie"] else "SL_TRAIL", FEE_TAKER)
        # TP (zlecenie limit = maker)
        for poz in list(st["pozycje"]):
            if poz["para"] not in ceny:
                continue
            bid, ask, _ = ceny[poz["para"]]
            if poz["kierunek"] == "LONG" and bid >= poz["tp"]:
                zamknij(nazwa, st, poz, poz["tp"], "TP", FEE_MAKER)
            elif poz["kierunek"] == "SHORT" and ask <= poz["tp"]:
                zamknij(nazwa, st, poz, poz["tp"], "TP", FEE_MAKER)
        # likwidacja (cross margin całego konta bota)
        if st["pozycje"]:
            uzyty = sum(p["wejscie"] * p["ilosc"] / DZWIGNIA for p in st["pozycje"])
            kapital = st["gotowka"] + sum(pnl(p, ceny[p["para"]][2]) for p in st["pozycje"] if p["para"] in ceny)
            if uzyty > 0 and kapital / uzyty < LIKWIDACJA:
                log(f"[{nazwa}] ⚠️ LIKWIDACJA: poziom depozytu {kapital / uzyty:.0%}")
                st["likwidacje"] += 1
                for p in list(st["pozycje"]):
                    if p["para"] in ceny:
                        bid, ask, _ = ceny[p["para"]]
                        zamknij(nazwa, st, p, bid if p["kierunek"] == "LONG" else ask, "LIKWIDACJA", FEE_TAKER)
        # nowe wejścia – raz na zamkniętą świecę M15
        for para, (m15, h1) in dane.items():
            if len(m15) < 3 or len(h1) < 60:
                continue
            ost_sw = m15[-1][0]
            if st["ostatnia_swieca"].get(para) == ost_sw:
                continue
            st["ostatnia_swieca"][para] = ost_sw
            if len(st["pozycje"]) >= MAX_POZYCJI or any(p["para"] == para for p in st["pozycje"]):
                continue
            kier = sygnal(m15, h1)
            if not kier:
                continue
            uzyty = sum(p["wejscie"] * p["ilosc"] / DZWIGNIA for p in st["pozycje"])
            if st["gotowka"] - uzyty < DEPOZYT_NA_POZYCJE:
                continue
            bid, ask, _ = ceny[para]
            wej = ask if kier == "LONG" else bid
            tp_pct = cfg["tp"] if cfg["tp"] != "atr" else max(0.008, atr_pct(h1))
            ilosc = DEPOZYT_NA_POZYCJE * DZWIGNIA / wej
            oplata = wej * ilosc * (FEE_TAKER + FEE_MARGIN_OPEN)
            st["gotowka"] -= oplata
            tp = wej * (1 + tp_pct) if kier == "LONG" else wej * (1 - tp_pct)
            sl = wej * (1 - SL_START * tp_pct) if kier == "LONG" else wej * (1 + SL_START * tp_pct)
            st["pozycje"].append({"para": para, "kierunek": kier, "wejscie": wej, "ilosc": ilosc, "tp": tp,
                                  "sl": sl, "best": wej,
                                  "otwarta": t.isoformat(timespec="seconds"), "rollover": t.isoformat(),
                                  "oplaty": oplata})
            log(f"[{nazwa}] OTWARTA {kier} {para} @ {wej} TP {tp:.5f} ({tp_pct:.2%}) SL {sl:.5f} (przesuwany) | 50 EUR x10")
        # podsumowanie
        kapital = st["gotowka"] + sum(pnl(p, ceny[p["para"]][2]) for p in st["pozycje"] if p["para"] in ceny)
        st["kapital"] = round(kapital, 2)
        st["aktualizacja"] = t.isoformat(timespec="seconds")
        zapisz(nazwa, st)


def main():
    log("=== Agent Kraken Pro (na sucho) START === boty: " + ", ".join(BOTY))
    while True:
        try:
            obieg()
        except Exception as e:
            log(f"BŁĄD obiegu: {e}")
        if "--raz" in sys.argv:
            break
        time.sleep(60)


if __name__ == "__main__":
    main()
