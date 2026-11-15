# -*- coding: utf-8 -*-
"""
Agent „IBKR Szybki" – szybkie transakcje na koncie DEMO (paper) IBKR przez IB Gateway (127.0.0.1:4002).
Rynek: forex IDEALPRO (dane real-time za darmo na IBKR): EUR/USD, GBP/USD, USD/JPY.

Wejście (reguła szefa nr 1): 3 ostatnie zamknięte świece M5 w tym samym kolorze,
potwierdzone trendem H1 (EMA20 vs EMA50).
Wyjście: krótki TP limitem = max(6 pipsów, 0.8 x ATR14 z M5) – nasze liczby, liczone pod koszty IBKR.
Bez SL (styl szefa). Bezpiecznik czasowy: pozycja zamykana rynkowo po 90 min, żeby kapitał nie stał.
Maks. 1 pozycja na parę, 3 łącznie. Wielkość: 25 000 jednostek waluty bazowej.
Bot sprawdza, że konto jest PAPER (zaczyna się od "DU") – na prawdziwym koncie nic nie zrobi.
"""
import csv, json, os, sys, time
from datetime import datetime, timezone, timedelta
from ib_async import IB, Forex, MarketOrder, LimitOrder, util

KAT = os.path.dirname(os.path.abspath(__file__))
PARY = ["EURUSD", "GBPUSD", "USDJPY"]
ILOSC = 25000
MAX_POZYCJI = 3
MIN_PIPS = 6
ATR_MNOZNIK = 0.8
MAX_CZAS_MIN = 90
CLIENT_ID = 11


def teraz():
    return datetime.now(timezone.utc)


def log(msg):
    linia = f"{teraz():%Y-%m-%d %H:%M:%S} {msg}"
    print(linia, flush=True)
    with open(os.path.join(KAT, "agent.log"), "a", encoding="utf-8") as f:
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


def stan_wczytaj():
    p = os.path.join(KAT, "stan.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {"pozycje": {}, "ostatnia_swieca": {}}


def stan_zapisz(st):
    p = os.path.join(KAT, "stan.json")
    with open(p + ".tmp", "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=1)
    os.replace(p + ".tmp", p)


def zapisz_transakcje(w):
    p = os.path.join(KAT, "transakcje.csv")
    nowy = not os.path.exists(p)
    with open(p, "a", newline="", encoding="utf-8") as f:
        c = csv.writer(f)
        if nowy:
            c.writerow(["czas_zamkniecia", "para", "kierunek", "wejscie", "wyjscie", "ilosc",
                        "wynik_pips", "powod", "czas_otwarcia"])
        c.writerow(w)


class Bot:
    def __init__(self):
        self.ib = IB()
        self.st = stan_wczytaj()
        self.kontrakty = {p: Forex(p) for p in PARY}

    def polacz(self):
        self.ib.connect("127.0.0.1", 4002, clientId=CLIENT_ID, timeout=20)
        konta = self.ib.managedAccounts()
        if not konta or not all(k.startswith("DU") for k in konta):
            log(f"STOP: to nie jest konto paper ({konta}) – bot nic nie robi")
            self.ib.disconnect()
            sys.exit(1)
        self.ib.qualifyContracts(*self.kontrakty.values())
        log(f"Połączono z IB Gateway, konto paper {konta}")

    def swiece(self, para, rozmiar, okres):
        b = self.ib.reqHistoricalData(self.kontrakty[para], endDateTime="", durationStr=okres,
                                      barSizeSetting=rozmiar, whatToShow="MIDPOINT", useRTH=False,
                                      formatDate=2, timeout=30)
        return list(b or [])

    def otworz(self, para, kier, m5):
        c = self.kontrakty[para]
        dystans = max(MIN_PIPS * pip(para), ATR_MNOZNIK * atr(m5))
        akcja, zamk = ("BUY", "SELL") if kier == "LONG" else ("SELL", "BUY")
        wej = self.ib.placeOrder(c, MarketOrder(akcja, ILOSC))
        for _ in range(30):
            self.ib.sleep(1)
            if wej.orderStatus.status == "Filled":
                break
        if wej.orderStatus.status != "Filled":
            log(f"{para}: wejście niewypełnione ({wej.orderStatus.status}) – anuluję")
            self.ib.cancelOrder(wej.order)
            return
        cena = wej.orderStatus.avgFillPrice
        tp = cena + dystans if kier == "LONG" else cena - dystans
        tp = round(tp, 3 if para.endswith("JPY") else 5)
        tp_order = self.ib.placeOrder(c, LimitOrder(zamk, ILOSC, tp, tif="GTC"))
        self.st["pozycje"][para] = {"kierunek": kier, "wejscie": cena, "tp": tp,
                                    "tp_id": tp_order.order.orderId,
                                    "otwarta": teraz().isoformat(timespec="seconds")}
        stan_zapisz(self.st)
        log(f"OTWARTA {kier} {para} @ {cena} TP {tp} ({dystans / pip(para):.1f} pips)")

    def sprawdz_pozycje(self):
        otwarte = {t.order.orderId: t for t in self.ib.openTrades()}
        wypelnione = {f.execution.orderId: f for f in self.ib.fills()}
        for para, p in list(self.st["pozycje"].items()):
            kier = p["kierunek"]
            znak = 1 if kier == "LONG" else -1
            if p["tp_id"] in wypelnione or (p["tp_id"] not in otwarte and self.tp_wykonany(para)):
                wyj = p["tp"]
                self.zamknij_zapis(para, p, wyj, "TP")
                continue
            wiek = teraz() - datetime.fromisoformat(p["otwarta"])
            if wiek > timedelta(minutes=MAX_CZAS_MIN):
                t = otwarte.get(p["tp_id"])
                if t:
                    self.ib.cancelOrder(t.order)
                    self.ib.sleep(2)
                akcja = "SELL" if kier == "LONG" else "BUY"
                z = self.ib.placeOrder(self.kontrakty[para], MarketOrder(akcja, ILOSC))
                for _ in range(30):
                    self.ib.sleep(1)
                    if z.orderStatus.status == "Filled":
                        break
                wyj = z.orderStatus.avgFillPrice or p["wejscie"]
                self.zamknij_zapis(para, p, wyj, f"CZAS {MAX_CZAS_MIN} min")

    def tp_wykonany(self, para):
        # po restarcie bota fills() może być puste – sprawdzamy, czy na koncie nie ma już pozycji w tej parze
        for poz in self.ib.positions():
            if poz.contract.symbol + poz.contract.currency == para and abs(poz.position) > 0:
                return False
        return True

    def zamknij_zapis(self, para, p, wyj, powod):
        znak = 1 if p["kierunek"] == "LONG" else -1
        pipsy = (wyj - p["wejscie"]) * znak / pip(para)
        zapisz_transakcje([teraz().isoformat(timespec="seconds"), para, p["kierunek"], p["wejscie"], wyj,
                           ILOSC, round(pipsy, 1), powod, p["otwarta"]])
        log(f"ZAMKNIĘTA {p['kierunek']} {para} {p['wejscie']} -> {wyj} | {pipsy:+.1f} pips ({powod})")
        del self.st["pozycje"][para]
        stan_zapisz(self.st)

    def obieg(self):
        self.sprawdz_pozycje()
        for para in PARY:
            m5 = self.swiece(para, "5 mins", "2 D")
            h1 = self.swiece(para, "1 hour", "10 D")
            if len(m5) < 20 or len(h1) < 60:
                continue
            zamkn = m5[:-1]                       # ostatnia świeca jeszcze trwa
            ost = str(zamkn[-1].date)
            if self.st["ostatnia_swieca"].get(para) == ost:
                continue
            # świeża świeca? (rynek zamknięty = brak nowych świec)
            d = zamkn[-1].date
            d = d if isinstance(d, datetime) else util.parseIBDatetime(d)
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone.utc)
            if teraz() - d > timedelta(minutes=15):
                continue
            self.st["ostatnia_swieca"][para] = ost
            if para in self.st["pozycje"] or len(self.st["pozycje"]) >= MAX_POZYCJI:
                continue
            o = zamkn[-3:]
            zielone = all(x.close > x.open for x in o)
            czerwone = all(x.close < x.open for x in o)
            zam = [x.close for x in h1[-120:]]
            w_gore = ema(zam, 20) > ema(zam, 50)
            if zielone and w_gore:
                self.otworz(para, "LONG", zamkn)
            elif czerwone and not w_gore:
                self.otworz(para, "SHORT", zamkn)
        stan_zapisz(self.st)


def main():
    log("=== Agent IBKR Szybki (paper) START === pary: " + ", ".join(PARY))
    while True:
        bot = Bot()
        try:
            bot.polacz()
            while bot.ib.isConnected():
                bot.obieg()
                if "--raz" in sys.argv:
                    for para in PARY:
                        m5 = bot.swiece(para, "5 mins", "2 D")
                        log(f"TEST {para}: {len(m5)} świec M5, ostatnia {m5[-1].date if m5 else '-'} close {m5[-1].close if m5 else '-'}")
                    bot.ib.disconnect()
                    return
                bot.ib.sleep(30)
            log("Rozłączono z Gateway – ponawiam za 60 s")
        except SystemExit:
            raise
        except Exception as e:
            log(f"BŁĄD: {e} – ponawiam za 60 s")
        try:
            bot.ib.disconnect()
        except Exception:
            pass
        if "--raz" in sys.argv:
            return
        time.sleep(60)


if __name__ == "__main__":
    main()
