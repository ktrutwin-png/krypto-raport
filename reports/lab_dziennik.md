# Laboratorium – dziennik (tylko demo / paper / virtual)

Zasady: co noc przegląd → wyłączenie słabych (PF < 0,9 po ~20 transakcjach albo −30% kapitału) → 1–3 nowe pomysły → backtest z kosztami (nauka 70% / sprawdzian 30%) → na demo idą te ze sprawdzianem PF ≥ 0,95.
Kod: `C:\Hexa\lab` (silnik `lab_silnik.py`, boty `boty\*.py`, start `START_LAB.ps1` + `lista.json`, logi `logi\`, stan `stan\`).

---

## 2026-11-18 (noc 1 – start laboratorium)

**Przegląd poprzednich dni:** brak – pierwsza noc, nic do wyłączenia.

**Budowa:**
- `C:\Hexa\lab` utworzony: wspólny silnik strategii (te same reguły w backteście i na żywo), bot MT5 (`lab_mt5.py`: przed każdym zleceniem login 5058971085 + tryb DEMO, magic 830200–830299, łączny depozyt lab ≤ 30% kapitału, konto hedging – pozycji Hexy/Turbo/Indeksów nie dotyka), Kraken na sucho (`lab_kraken.py`: 500 € wirtualne/bot, dźwignia do 10x, opłaty Kraken Pro), IBKR paper (`lab_ib.py`: clientId 50–59, konto „DU”, pary wolne od szybki/warianty, OCA TP+SL).
- Dopisany wpis „Laboratorium” do `START_WSZYSTKO.ps1` (wzorzec `Hexa\\lab\\boty`, start przez START_LAB.ps1) i do `roj_straz.py` (wzorzec `Hexa\lab\boty`); kopie `.bak_lab_20261118`; strażnik zrestartowany.
- Raport 22:00: `zbierz_dzis.py` liczy teraz osobno Laboratorium → pole `wiersz_laboratorium` („Laboratorium (demo)”, zysk/strata w €) w `zbierz_out.json` (kopia `zbierz_dzis.py.bak_20261118`, test uruchomienia ok).

**Backtest (runda 1, 1140 zestawów; MT5: M15 od 02–04.2025, H1 od 2024; Kraken 15m od 19.05.2026):**

| Pomysł | Rynek | Nauka PF (n) | Sprawdzian PF (n) | Decyzja |
|---|---|---|---|---|
| Londyn – wybicie z zakresu Azji, SL środek, TP 2R | XAUUSD M15 | 1,21 (209) | **2,19 (90)** | ✅ demo |
| Donchian 55 H1, SL 2,5 ATR / TP 3 ATR | XAGUSD H1 | 1,40 (240) | **1,50 (94)** | ✅ demo |
| Kontra – przeciw tłumowi po świecy ≥3×ATR, TP 61,8% | EURUSD / USDJPY M15 | 1,25 / 1,21 | **1,32 (77) / 1,36 (89)** | ✅ demo |
| RSI(2) + EMA200, SL 3 / TP 2 ATR | USDJPY / GBPUSD M15 | 1,10 / 0,93 | **1,37 (240) / 1,10 (252)** | ✅ demo |
| RSI(2) + EMA200 | AUDUSD M15 (IBKR) | 1,00 (563) | **1,22 (237)** | ✅ IBKR paper |
| Kontra na złocie | XAUUSD H1 | 1,66 | 0,59 | ❌ przeuczone |
| Donchian | US30 H1 | 1,19 | 0,51 | ❌ |
| Wszystko na krypto M15/H1 (opłaty 0,75%) | BTC/ETH/XRP | ≤ 0,97 | ≤ 0,55 | ❌ |

**Lekcje:**
- Krypto na Krakenie: krótkie TF są martwe – 0,75% kosztów w obie strony zjada każdą przewagę (kontra M15 na BTC: PF 0,00). Ratunek: wejścia LIMIT (maker, ~0,52%) i H4.
- Runda 3 (Kraken, maker, H4): RSI(2) + EMA200, SL 4 / TP 5 ATR – BTC nauka 1,61 → spr **1,31 (n9)**, XRP 2,46 → **1,60 (n11)**. Mała próba – puszczone odważnie, demo jest od nauki.
- Kontra D1 (pod eToro, zarządzane raz na noc): tylko GBPUSD przeszło (nauka 1,26 n16 → spr 2,16 n7). Reszta ≤ 0,54.
- Indeksy US500/US30 na koncie botów mają handel wyłączony (trade_mode 0) – pominięte.

**Uruchomione na demo (6 botów + 1 strategia eToro):** LAB_Londyn_XAU (830201), LAB_Donchian_XAG (830202), LAB_Kontra_FX (830203), LAB_RSI2_FX (830204), LAB_KR_RSI2_H4 (Kraken na sucho), LAB_IB_RSI2_AUD (IBKR paper, clientId 50). Ryzyko MT5: 0,4–0,5% kapitału na transakcję (lot liczony od SL).

**eToro (konto DEMO, odczyt `account=demo` potwierdzony):** strategia „Kontra D1” na GBPUSD – dziś brak sygnału (świeca 17.11: zakres 0,8×ATR < 1,8×ATR), 0 transakcji. Pozycje laboratorium zapisuję w `C:\Hexa\lab\etoro_pozycje.json` (pusto).

**Zablokowane (nie obchodzę):**
- IBKR: IB Gateway odpowiada bardzo wolno – połączenie trwa ~30 s, potem timeout na pozycjach/zleceniach/kwalifikacji kontraktu; bot `LAB_IB_RSI2_AUD` kończy się TimeoutError i sam ponawia co 60 s. Bot szybki_fx też milczy od 17.11 06:12. Gateway nie ruszałem – do sprawdzenia przez Inspektora/Mechanika.
- Dane akcji pod eToro (Stooq zwraca puste pliki, Twelve Data limit 8/min) – backtest „kontra tygodnia na akcjach” odłożony.

**Najlepszy na start (backtest):** LAB_Londyn_XAU – sprawdzian PF 2,19, +33 R na 90 transakcjach.
