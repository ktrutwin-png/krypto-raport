# -*- coding: utf-8 -*-
"""
Szukanie najlepszej reguły wejścia dla Kraken Pro (backtest, nic nie handluje).
Dane: świece 15 min z Binance (BTC/ETH/XRP do EUR, ~6 mies.) – ceny prawie identyczne jak na Krakenie.
Koszty jak na Kraken Pro: wejście 0.40% + margin 0.02%, TP limitem 0.25%, SL/inne rynkowo 0.40%, rollover 0.02%/4h.
Wyjście dla wszystkich reguł takie samo jak w agencie: TP + przesuwany SL (start 1.5x TP, od 50% drogi na zero,
potem 0.5x dystansu za najlepszą ceną). Jeśli w jednej świecy padłby i SL, i TP – liczymy SL (ostrożnie).
Pozycja: 500 EUR (50 EUR x10), max 1 na parę na regułę.
Podział: pierwsze 2/3 danych = nauka, ostatnia 1/3 = sprawdzian (to się liczy przy wyborze).
"""
import json, os, sys, time, urllib.request
from datetime import datetime, timezone

KAT = os.path.dirname(os.path.abspath(__file__))
PARY = {"BTC/EUR": "BTCEUR", "ETH/EUR": "ETHEUR", "XRP/EUR": "XRPEUR"}
DNI = 180
POZ = 500.0
F_TAKER, F_MAKER, F_OPEN, F_ROLL = 0.004, 0.0025, 0.0002, 0.0002
SL_START, SL_BE, SL_TRAIL = 1.5, 0.5, 0.5


def pobierz(sym):
    plik = os.path.join(KAT, f"dane_{sym}_15m.json")
    if os.path.exists(plik) and time.time() - os.path.getmtime(plik) < 6 * 3600:
        return json.load(open(plik))
    koniec = int(time.time() * 1000)
    start = koniec - DNI * 86400 * 1000
    out = []
    while start < koniec:
        url = f"https://api.binance.com/api/v3/klines?symbol={sym}&interval=15m&limit=1000&startTime={start}"
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "hexa"}), timeout=30) as r:
            d = json.load(r)
        if not d:
            break
        out += [[int(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4])] for x in d]
        start = d[-1][0] + 1
        time.sleep(0.2)
    json.dump(out, open(plik, "w"))
    return out


def ema_seria(v, n):
    k, e, out = 2 / (n + 1), v[0], []
    for x in v:
        e = x * k + e * (1 - k)
        out.append(e)
    return out


def rsi_seria(c, n=14):
    out, g, l = [50.0] * len(c), 0.0, 0.0
    for i in range(1, len(c)):
        d = c[i] - c[i - 1]
        g = (g * (n - 1) + max(d, 0)) / n
        l = (l * (n - 1) + max(-d, 0)) / n
        out[i] = 100 - 100 / (1 + g / l) if l > 0 else 100
    return out


def atr_seria(s, n=14):
    out, a = [0.0] * len(s), 0.0
    for i in range(1, len(s)):
        tr = max(s[i][2] - s[i][3], abs(s[i][2] - s[i - 1][4]), abs(s[i][3] - s[i - 1][4]))
        a = (a * (n - 1) + tr) / n
        out[i] = a
    return out


def wskazniki(s):
    c = [x[4] for x in s]
    # trend H1: EMA20/50 z zamknięć pełnych godzin (co 4 świece), przeniesiony na M15 bez zaglądania w przyszłość
    h_idx = [i for i in range(len(s)) if (s[i][0] // 900000) % 4 == 3]
    h_close = [c[i] for i in h_idx]
    e20, e50 = ema_seria(h_close, 20), ema_seria(h_close, 50)
    trend = [0] * len(s)
    j = -1
    for i in range(len(s)):
        while j + 1 < len(h_idx) and h_idx[j + 1] <= i:
            j += 1
        if j >= 50:
            trend[i] = 1 if e20[j] > e50[j] else -1
    e9, e21 = ema_seria(c, 9), ema_seria(c, 21)
    rsi = rsi_seria(c)
    ma20 = [sum(c[max(0, i - 19):i + 1]) / min(20, i + 1) for i in range(len(c))]
    sd20 = [(sum((x - ma20[i]) ** 2 for x in c[max(0, i - 19):i + 1]) / min(20, i + 1)) ** 0.5 for i in range(len(c))]
    e12, e26 = ema_seria(c, 12), ema_seria(c, 26)
    macd = [a - b for a, b in zip(e12, e26)]
    sig = ema_seria(macd, 9)
    hist = [a - b for a, b in zip(macd, sig)]
    return dict(c=c, trend=trend, e9=e9, e21=e21, rsi=rsi, ma20=ma20, sd20=sd20, hist=hist, atr=atr_seria(s))


def sygnal(regula, s, w, i):
    t = w["trend"][i]
    if t == 0 or i < 60:
        return None
    o, c = s[i][1], s[i][4]
    if regula == "3_swiece_trend (obecna)":
        z = all(s[k][4] > s[k][1] for k in range(i - 2, i + 1))
        r = all(s[k][4] < s[k][1] for k in range(i - 2, i + 1))
        return "LONG" if z and t > 0 else "SHORT" if r and t < 0 else None
    if regula == "EMA9/21_przeciecie_trend":
        up = w["e9"][i - 1] <= w["e21"][i - 1] and w["e9"][i] > w["e21"][i]
        dn = w["e9"][i - 1] >= w["e21"][i - 1] and w["e9"][i] < w["e21"][i]
        return "LONG" if up and t > 0 else "SHORT" if dn and t < 0 else None
    if regula == "RSI_cofniecie_w_trendzie":
        up = w["rsi"][i - 1] < 35 <= w["rsi"][i]
        dn = w["rsi"][i - 1] > 65 >= w["rsi"][i]
        return "LONG" if up and t > 0 else "SHORT" if dn and t < 0 else None
    if regula == "Bollinger_powrot_w_trendzie":
        lo_p = w["ma20"][i - 1] - 2 * w["sd20"][i - 1]
        hi_p = w["ma20"][i - 1] + 2 * w["sd20"][i - 1]
        lo, hi = w["ma20"][i] - 2 * w["sd20"][i], w["ma20"][i] + 2 * w["sd20"][i]
        up = w["c"][i - 1] < lo_p and c > lo
        dn = w["c"][i - 1] > hi_p and c < hi
        return "LONG" if up and t > 0 else "SHORT" if dn and t < 0 else None
    if regula == "Wybicie_20_swiec_trend":
        hh = max(x[2] for x in s[i - 20:i])
        ll = min(x[3] for x in s[i - 20:i])
        return "LONG" if c > hh and t > 0 else "SHORT" if c < ll and t < 0 else None
    if regula == "MACD_zwrot_w_trendzie":
        up = w["hist"][i - 1] <= 0 < w["hist"][i]
        dn = w["hist"][i - 1] >= 0 > w["hist"][i]
        return "LONG" if up and t > 0 else "SHORT" if dn and t < 0 else None
    return None


REGULY = ["3_swiece_trend (obecna)", "EMA9/21_przeciecie_trend", "RSI_cofniecie_w_trendzie",
          "Bollinger_powrot_w_trendzie", "Wybicie_20_swiec_trend", "MACD_zwrot_w_trendzie"]
TPY = {"TP 0.8%": 0.008, "TP 1.2%": 0.012, "TP 2%": 0.02, "TP ATR": "atr"}
TRYBY = ["trail", "bez_SL"]


def symuluj(regula, tp_cfg, s, w, od, do, tryb="trail"):
    wyniki, poz = [], None
    for i in range(od, do):
        hi, lo = s[i][2], s[i][3]
        if poz:
            kier, wej, tp, sl, best, dyst, start = poz
            zamk = None
            if kier == "LONG":
                if lo <= sl:
                    zamk = (sl, F_TAKER)
                elif hi >= tp:
                    zamk = (tp, F_MAKER)
                else:
                    best = max(best, hi)
                    if tryb == "trail" and (best - wej) / dyst >= SL_BE:
                        sl = max(sl, best - SL_TRAIL * dyst)
            else:
                if hi >= sl:
                    zamk = (sl, F_TAKER)
                elif lo <= tp:
                    zamk = (tp, F_MAKER)
                else:
                    best = min(best, lo)
                    if tryb == "trail" and (wej - best) / dyst >= SL_BE:
                        sl = min(sl, best + SL_TRAIL * dyst)
            if zamk:
                cena, fee = zamk
                ruch = (cena - wej) / wej if kier == "LONG" else (wej - cena) / wej
                rollover = ((i - start) * 15 // 240) * F_ROLL
                wyniki.append(POZ * (ruch - F_TAKER - F_OPEN - fee - rollover))
                poz = None
            else:
                poz = (kier, wej, tp, sl, best, dyst, start)
            continue
        kier = sygnal(regula, s, w, i)
        if kier and i + 1 < do:
            wej = s[i + 1][1]   # wejście na otwarciu następnej świecy
            pct = tp_cfg if tp_cfg != "atr" else max(0.008, 4 * w["atr"][i] / s[i][4])
            dyst = wej * pct
            tp = wej + dyst if kier == "LONG" else wej - dyst
            sm = SL_START if tryb == "trail" else 0.06 / pct      # bez SL: zamknięcie dopiero ok. -6% (okolice likwidacji)
            sl = wej - sm * dyst if kier == "LONG" else wej + sm * dyst
            poz = (kier, wej, tp, sl, wej, dyst, i + 1)
    return wyniki


def statystyki(w):
    if not w:
        return dict(n=0, wynik=0, trafnosc=0, pf=0, dd=0)
    zysk = sum(x for x in w if x > 0)
    strata = -sum(x for x in w if x < 0)
    eq, szczyt, dd = 0, 0, 0
    for x in w:
        eq += x
        szczyt = max(szczyt, eq)
        dd = max(dd, szczyt - eq)
    return dict(n=len(w), wynik=round(sum(w), 2), trafnosc=round(100 * sum(x > 0 for x in w) / len(w), 1),
                pf=round(zysk / strata, 2) if strata else 99, dd=round(dd, 2))


def main():
    dane = {}
    for para, sym in PARY.items():
        s = pobierz(sym)
        dane[para] = (s, wskazniki(s))
        print(f"{para}: {len(s)} świec od {datetime.fromtimestamp(s[0][0] / 1000, timezone.utc):%Y-%m-%d}", flush=True)
    wiersze = []
    for regula in REGULY:
      for tryb in TRYBY:
        for tpn, tpv in TPY.items():
            nauka, spr = [], []
            for para, (s, w) in dane.items():
                gr = len(s) * 2 // 3
                nauka += symuluj(regula, tpv, s, w, 60, gr, tryb)
                spr += symuluj(regula, tpv, s, w, gr, len(s), tryb)
            a, b = statystyki(nauka), statystyki(spr)
            tpn2 = f"{tpn} {tryb}"
            wiersze.append((regula, tpn2, a, b))
            print(f"{regula:30s} {tpn2:16s} | NAUKA n={a['n']:4d} {a['wynik']:+9.2f}€ traf {a['trafnosc']:5.1f}% PF {a['pf']:5.2f} | "
                  f"SPRAWDZIAN n={b['n']:4d} {b['wynik']:+9.2f}€ traf {b['trafnosc']:5.1f}% PF {b['pf']:5.2f} DD {b['dd']:.2f}€", flush=True)
    json.dump([dict(regula=r, tp=t, nauka=a, sprawdzian=b) for r, t, a, b in wiersze],
              open(os.path.join(KAT, "szukaj_reguly_wynik.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
