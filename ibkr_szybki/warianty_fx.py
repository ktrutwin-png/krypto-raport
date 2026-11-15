# -*- coding: utf-8 -*-
"""
Tester wariantów TP na forexie IBKR – symulacja „na sucho" na prawdziwych cenach bid/ask z IB Gateway.
Nie składa zleceń (konto paper netuje pozycje, więc kilka wariantów na tej samej parze musi być wirtualnych).

Każdy wariant: ta sama reguła wejścia co bot (3 świece w tym samym kolorze + trend H1 EMA20/50),
inny interwał i inny TP. Wielkość 100 000 jednostek. Koszt jak na IBKR: spread (wejście po ask/bid)
+ prowizja 0.2 bp wartości, min. 2 USD za stronę. Bez SL, wyjście czasowe jak w bocie.
Wynik w USD i pipsach -> warianty_transakcje.csv, stan w warianty_stan.json.
"""
import csv, json, os, sys, time
from datetime import datetime, timezone, timedelta
from ib_async import IB, Forex, util

KAT = os.path.dirname(os.path.abspath(__file__))
PARY = ["EURUSD", "GBPUSD", "USDJPY"]
ILOSC = 100000
CLIENT_ID = 12
WARIANTY = {
    "M5_TP3":   {"tf": "5 mins",  "okres": "2 D", "tp": 3,     "czas": 90},
    "M5_TP6":   {"tf": "5 mins",  "okres": "2 D", "tp": 6,     "czas": 90},
    "M15_TP4":  {"tf": "15 mins", "okres": "5 D", "tp": 4,     "czas": 180},
    "M15_ATR":  {"tf": "15 mins", "okres": "5 D", "tp": "atr", "czas": 180},
}


def teraz():
    return datetime.now(timezone.utc)


def log(msg):
    linia = f"{teraz():%Y-%m-%d %H:%M:%S} {msg}"
    print(linia, flush=True)
    with open(os.path.join(KAT, "warianty.log"), "a", encoding="utf-8") as f:
        f.write(linia + "\n")


def pip(para):
    return 0.01 if para.endswith("JPY") else 0.0001


def ema(v, n):
    k, e = 2 / (n + 1), v[0]
    for x in v[1:]:
        e = x * k + e * (1 - k)
    return e


def atr(b, n=14):
    tr = [max(b[i].high - b[i].low, abs(b[i].high - b[i - 1].close), abs(b[i].low - b[i - 1].close))
          for i in range(1, len(b))]
    return sum(tr[-n:]) / n


def prowizja_usd(para, cena):
    wartosc_usd = ILOSC * cena if para.startswith(("EUR", "GBP")) else ILOSC   # USDJPY: baza to USD
    return max(2.0, wartosc_usd * 0.00002)


def wynik_usd(para, kier, wej, wyj):
    ruch = (wyj - wej) if kier == "LONG" else (wej - wyj)
    if para.endswith("JPY"):
        return ruch * ILOSC / wyj          # zysk w JPY przeliczony na USD
    return ruch * ILOSC                     # EURUSD/GBPUSD: zysk w USD


def wczytaj():
    p = os.path.join(KAT, "warianty_stan.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {w: {"pozycje": {}, "ostatnia_swieca": {}, "wynik_usd": 0.0, "transakcje": 0} for w in WARIANTY}


def zapisz(st):
    p = os.path.join(KAT, "warianty_stan.json")
    with open(p + ".tmp", "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=1)
    os.replace(p + ".tmp", p)


def zapisz_csv(w):
    p = os.path.join(KAT, "warianty_transakcje.csv")
    nowy = not os.path.exists(p)
    with open(p, "a", newline="", encoding="utf-8") as f:
        c = csv.writer(f)
        if nowy:
            c.writerow(["czas_zamkniecia", "wariant", "para", "kierunek", "wejscie", "wyjscie",
                        "pips", "wynik_usd_netto", "powod", "czas_otwarcia"])
        c.writerow(w)


class Tester:
    def __init__(self):
        self.ib = IB()
        self.st = wczytaj()
        self.k = {p: Forex(p) for p in PARY}

    def polacz(self):
        self.ib.connect("127.0.0.1", 4002, clientId=CLIENT_ID, timeout=20, readonly=True)
        self.ib.qualifyContracts(*self.k.values())
        log("Tester wariantów połączony: " + ", ".join(WARIANTY))

    def swiece(self, para, tf, okres):
        return list(self.ib.reqHistoricalData(self.k[para], "", okres, tf, "MIDPOINT", False, 2, timeout=30) or [])

    def ceny(self):
        t = self.ib.reqTickers(*self.k.values())
        out = {}
        for tk in t:
            para = tk.contract.symbol + tk.contract.currency
            if tk.bid and tk.ask and tk.bid > 0 and tk.ask > 0:
                out[para] = (tk.bid, tk.ask)
        return out

    def zamknij(self, w, para, p, wyj, powod):
        s = self.st[w]
        brutto = wynik_usd(para, p["kierunek"], p["wejscie"], wyj)
        netto = brutto - p["prowizja"] - prowizja_usd(para, wyj)
        pipsy = ((wyj - p["wejscie"]) if p["kierunek"] == "LONG" else (p["wejscie"] - wyj)) / pip(para)
        s["wynik_usd"] = round(s["wynik_usd"] + netto, 2)
        s["transakcje"] += 1
        zapisz_csv([teraz().isoformat(timespec="seconds"), w, para, p["kierunek"], p["wejscie"], wyj,
                    round(pipsy, 1), round(netto, 2), powod, p["otwarta"]])
        log(f"[{w}] ZAMKNIĘTA {p['kierunek']} {para} {pipsy:+.1f} pips = {netto:+.2f} USD ({powod})")
        del s["pozycje"][para]

    def obieg(self):
        c = self.ceny()
        # wyjścia
        for w, cfg in WARIANTY.items():
            for para, p in list(self.st[w]["pozycje"].items()):
                if para not in c:
                    continue
                bid, ask = c[para]
                if p["kierunek"] == "LONG" and bid >= p["tp"]:
                    self.zamknij(w, para, p, p["tp"], "TP")
                elif p["kierunek"] == "SHORT" and ask <= p["tp"]:
                    self.zamknij(w, para, p, p["tp"], "TP")
                elif teraz() - datetime.fromisoformat(p["otwarta"]) > timedelta(minutes=cfg["czas"]):
                    self.zamknij(w, para, p, bid if p["kierunek"] == "LONG" else ask, f"CZAS {cfg['czas']} min")
        # wejścia
        cache = {}
        for para in PARY:
            if para not in c:
                continue
            h1 = cache.setdefault((para, "h1"), self.swiece(para, "1 hour", "10 D"))
            if len(h1) < 60:
                continue
            zam = [x.close for x in h1[-120:]]
            w_gore = ema(zam, 20) > ema(zam, 50)
            for w, cfg in WARIANTY.items():
                s = self.st[w]
                b = cache.setdefault((para, cfg["tf"]), self.swiece(para, cfg["tf"], cfg["okres"]))
                if len(b) < 20:
                    continue
                zamkn = b[:-1]
                d = zamkn[-1].date
                d = d if isinstance(d, datetime) else util.parseIBDatetime(d)
                if d.tzinfo is None:
                    d = d.replace(tzinfo=timezone.utc)
                ost = str(d)
                if s["ostatnia_swieca"].get(para) == ost or teraz() - d > timedelta(minutes=40):
                    continue
                s["ostatnia_swieca"][para] = ost
                if para in s["pozycje"]:
                    continue
                o = zamkn[-3:]
                kier = None
                if all(x.close > x.open for x in o) and w_gore:
                    kier = "LONG"
                elif all(x.close < x.open for x in o) and not w_gore:
                    kier = "SHORT"
                if not kier:
                    continue
                bid, ask = c[para]
                wej = ask if kier == "LONG" else bid
                dyst = cfg["tp"] * pip(para) if cfg["tp"] != "atr" else max(4 * pip(para), 0.8 * atr(zamkn))
                tp = wej + dyst if kier == "LONG" else wej - dyst
                s["pozycje"][para] = {"kierunek": kier, "wejscie": wej, "tp": tp,
                                      "prowizja": prowizja_usd(para, wej),
                                      "otwarta": teraz().isoformat(timespec="seconds")}
                log(f"[{w}] OTWARTA {kier} {para} @ {wej} TP {tp:.5f} ({dyst / pip(para):.1f} pips)")
        zapisz(self.st)


def main():
    log("=== Tester wariantów FX (na sucho, ceny IBKR) START ===")
    while True:
        t = Tester()
        try:
            t.polacz()
            while t.ib.isConnected():
                t.obieg()
                if "--raz" in sys.argv:
                    log("TEST ceny: " + str(t.ceny()))
                    t.ib.disconnect()
                    return
                t.ib.sleep(20)
            log("Rozłączono – ponawiam za 60 s")
        except Exception as e:
            log(f"BŁĄD: {e} – ponawiam za 60 s")
        try:
            t.ib.disconnect()
        except Exception:
            pass
        if "--raz" in sys.argv:
            return
        time.sleep(60)


if __name__ == "__main__":
    main()
