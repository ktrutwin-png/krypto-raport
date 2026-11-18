# Kraken – nowy bot (podmiana 18.11.2026)

Agent Kraken, zlecenie szefa z 16.11.2026. Tylko dry-run (wirtualne 1000 € na bota), bez kluczy i bez prawdziwych zleceń.

## Werdykt

- **Podmieniono oba boty Freqtrade** na serwerze:
  - `Donch4hBTC` → **`Kelt1h`** (wybicie z kanału Keltnera 1h z wolumenem), config `config_Kelt1h.json`, baza `Kelt1h.sqlite`
  - `Mom1dBTC` → **`Ema4h`** (przecięcie EMA9/21 nad EMA200 na 4h), config `config_Ema4h.json`, baza `Ema4h.sqlite`
- Oba przeszły kryteria na sprawdzianie (out-of-sample, opłata 0,4%/stronę):
  - Kelt1h: **+7,1%**, PF 1,18, 109 transakcji, maxDD 12,7%
  - Ema4h: **+17,3%**, PF 1,42, 60 transakcji, maxDD 15,5%
- **Uczciwie:** na okresie nauki (spadki: BTC −31%, ETH −38%, XRP −50%) obie strategie traciły (−44% i −32%). Zarabiały tylko w sprawdzianie, kiedy rynek odbijał (sierpień–wrzesień).
  - W ostatnich 4 tygodniach (BTC −27%) backtest daje: Kelt1h 16 transakcji, −7,3%; Ema4h 3 transakcje, −3,7%.
  - Czyli **będą handlować** (o to chodziło), ale w dalszych spadkach wynik będzie raczej na minusie.

## Dane i metoda

- **Dane:** Kraken nie udostępnia historii świec (freqtrade: „Historic klines not available for Kraken”, zostaje tylko `--dl-trades`, co trwałoby wiele godzin). Dlatego backtest liczyłem na **świecach OKX dla tych samych par EUR**. Ceny różnią się od Krakena o ułamki procenta.
- **Pary:** BTC/ETH/XRP EUR, potem pełna lista 10 par z obecnych botów (dochodzą SOL, ADA, LINK, DOGE, AVAX, DOT, LTC). PAXG testowane jako PAXG/USDT, bo OKX nie ma PAXG/EUR.
- **Okresy:**
  - nauka: 18.11.2025–01.08.2026 (ok. 70%)
  - sprawdzian: 01.08–18.11.2026 (ok. 30%)
- **Opłaty:** 0,4% i 0,25% na stronę (taker i maker Kraken Pro). Wybór robiłem po wariancie 0,4%.
- **Kryteria:**
  - zysk po opłatach na sprawdzianie
  - PF > 1,1
  - co najmniej ok. 30 transakcji w sprawdzianie
  - rozsądne obsunięcie
- **Gotowe strategie społeczności:** freqtrade-strategies i NostalgiaForInfinity mają licencję GPL-3.0. Tej nocy nie udało się ich otworzyć: prośba o dostęp do strony wygasła bez odpowiedzi, bo przebieg był nienadzorowany.
  - NFI jest zbudowane pod 5m i dziesiątki par z dużym wolumenem, więc nie pasuje do 10 par EUR na Krakenie.
  - Zamiast kopiować kod, napisałem własne wersje znanych wzorców w `user_data/strategies/Kandydaci20261118.py`: EMA200+RSI, Bollinger, Connors RSI2, Donchian, EMA cross, MACD, Keltner.

## Kandydaci – wyniki (opłata 0,4%/stronę, nauka → sprawdzian)

### Runda 1–2, 3 pary (BTC/ETH/XRP EUR)

| Strategia | TF | Nauka: tr. / zysk / PF | Sprawdzian: tr. / zysk / PF / maxDD |
|---|---|---|---|
| EmaRsiDip1h (EMA200 + RSI<35) | 1h | 17 / −9,0% / 0,19 | 7 / +2,4% / – / 0% |
| BbRevert1h (Bollinger + EMA200) | 1h | 139 / −42,0% / 0,15 | 70 / −12,4% / 0,31 / 12,4% |
| BbRevertNoF1h (Bollinger bez filtra) | 1h | 170 / −43,6% / 0,33 | 80 / −14,9% / 0,45 / 17,7% |
| Rsi2Trend1h (Connors RSI2) | 1h | 292 / −55,7% / 0,07 | 125 / −30,8% / 0,04 / 30,8% |
| Rsi2Trend15m | 15m | 1435 / −98,0% / 0,02 | 523 / −74,5% / 0,02 / 74,5% |
| Rsi2Trend4h | 4h | 50 / −14,9% / 0,15 | 41 / −12,8% / 0,11 / 12,8% |
| RsiDip15m (RSI<25, bez filtra) | 15m | 109 / −35,4% / 0,17 | 48 / −12,6% / 0,31 / 12,9% |
| Donch1hTrend (Donchian 48/24 + EMA50>200) | 1h | 81 / −25,7% / 0,35 | 40 / −5,1% / 0,82 / 20,5% |
| Donch4hFast | 4h | 17 / −21,3% / 0 | 13 / −3,1% / 0,75 / 10,3% |
| Donch4hLoose (bez filtra BTC) | 4h | 57 / −35,1% / 0,25 | 25 / −2,2% / 0,93 / 21,8% |
| EmaCross1h | 1h | 173 / −42,0% / 0,33 | 83 / −18,7% / 0,52 / 26,5% |
| EmaCross4h | 4h | 33 / −16,0% / 0,17 | 29 / −1,6% / 0,94 / 15,2% |
| EmaCross4hV2 (EMA100 + trailing) | 4h | 55 / −15,1% / 0,54 | 29 / −13,0% / 0,42 / 16,6% |
| MacdTrend4h | 4h | 53 / −15,6% / 0,43 | 46 / −9,1% / 0,65 / 14,6% |
| MacdTrend4hV2 | 4h | 48 / −24,1% / 0,27 | 28 / −17,4% / 0,19 / 17,4% |
| Oversold4h (RSI<30 + BB, bez filtra) | 4h | 54 / −29,4% / 0,36 | 17 / −12,7% / 0,29 / 15,9% |
| Capit1h (kapitulacja −5%/24h) | 1h | 25 / −9,1% / 0,48 | 2 / −3,0% / 0 / 3,0% |
| Keltner1h (2 ATR, wolumen 2x) | 1h | 157 / −35,0% / 0,41 | 55 / **+5,9%** / **1,23** / 12,6% |
| Keltner1hStrong (2,5 ATR, wolumen 2,5x) | 1h | 106 / −20,5% / 0,54 | 41 / **+11,0%** / **1,59** / 8,7% |
| Keltner1hTS (z trailing) | 1h | 188 / −45,8% / 0,35 | 72 / −15,3% / 0,51 / 21,1% |
| Keltner4h | 4h | 59 / −24,3% / 0,36 | 20 / +5,4% / 1,22 / 14,2% |
| Keltner15m | 15m | 796 / −88,5% / 0,23 | 278 / −49,8% / 0,32 / 49,9% |
| *stary* Donch4hBTC | 4h | 2 / −2,1% / 0,13 | 8 / +7,4% / 2,13 / 5,3% |
| *stary* Mom1dBTC | 1d | 4 / −6,2% / 0 | 3 / +13,1% / – / 0% |

### Runda 3, 10 par EUR (jak w botach na żywo)

| Strategia | TF | Nauka: tr. / zysk / PF | Sprawdzian: tr. / zysk / PF / maxDD |
|---|---|---|---|
| **Keltner1hStrong → Kelt1h** | 1h | 304 / −43,6% / 0,42 | **109 / +7,1% / 1,18 / 12,7%** |
| Keltner1h | 1h | 429 / −59,5% / 0,33 | 147 / −1,7% / 0,96 / 17,7% |
| Keltner1hTS | 1h | 519 / −65,9% / 0,35 | 229 / −24,7% / 0,61 / 30,3% |
| Donch1hTrend | 1h | 197 / −44,5% / 0,24 | 95 / +1,6% / 1,04 / 12,6% |
| EmaCross1h | 1h | 422 / −62,3% / 0,28 | 209 / −22,7% / 0,66 / 27,8% |
| **EmaCross4h → Ema4h** | 4h | 86 / −31,8% / 0,19 | **60 / +17,3% / 1,42 / 15,5%** |
| Donch4hFast | 4h | 33 / −21,7% / 0,06 | 26 / +20,3% / 2,20 / 6,9% (za mało transakcji) |
| Keltner4h | 4h | 130 / −33,9% / 0,36 | 54 / +3,6% / 1,10 / 15,2% |
| Donch4hLoose | 4h | 130 / −49,2% / 0,23 | 62 / +1,3% / 1,03 / 23,5% |
| *stary* Donch4hBTC | 4h | 5 / −0,3% / 0,75 | 15 / +13,7% / 2,36 / 4,1% (za mało transakcji) |

### PAXG/USDT (proxy złota)

Żadna strategia nie przeszła na PAXG: złoto rusza się za słabo względem opłaty 0,8% za cały cykl. Przykłady:

- Keltner1h: 27 transakcji w sprawdzianie, −25%
- BbRevert1h: 35 transakcji, −25%
- EmaCross4h: 3 transakcje, −2%

**PAXG nie został dodany** do botów.

### Wnioski

- Częsta gra na 15m–1h z powrotem do średniej (RSI2, Bollinger) przegrywa z opłatami Krakena. Przy 0,4% za stronę cały cykl kosztuje 0,8%, a typowe odbicie 1h jest mniejsze.
- Przeżywają tylko strategie łapiące większe ruchy: wybicia z wolumenem i przecięcia na 4h.
- Długo zasypiał głównie filtr reżimu BTC (cena nad SMA100 dziennie) w starych botach. Nowe boty go nie mają. Kelt1h nie ma filtra trendu, tylko wymaga rosnącej EMA50. Ema4h ma filtr EMA200 na własnej parze.

## Co zrobiono na serwerze

1. Kopie pod nazwą `*.bak_20261118`:
   - `config_Donch4hBTC.json`, `config_Mom1dBTC.json`
   - `user_data\KrakenTrendBTC.py`
   - `START_KRAKEN.bat` na pulpicie
   - `C:\Hexa\narzedzia\START_WSZYSTKO.ps1`, `roj_straz.py`

   Stare configi i bazy sqlite zostały na miejscu, nic nie usunięto.
2. Nowa strategia `user_data\strategies\KrakenNowe20261118.py` (klasy `Kelt1h`, `Ema4h`) i nowe configi:
   - dry_run true, dry_run_wallet 1000
   - te same 10 par EUR
   - max_open_trades 5
   - `fee` 0,004
3. `START_KRAKEN.bat` uruchamia teraz Kelt1h i Ema4h.
   - Zatrzymane zostały tylko procesy `freqtrade trade` z configami Donch4hBTC i Mom1dBTC.
   - Boty ruszyły 18.11 03:53 (czas serwera): „Dry run is enabled”, heartbeat RUNNING, bez błędów.
   - Kontrolny backtest klas `Kelt1h`/`Ema4h` dał identyczne wyniki jak kandydaci (109/+7,09% i 60/+17,27%).
4. `roj_straz.py`: wpisy „Kraken Donchian/Momentum” zamienione na „Kraken Keltner 1h” (`config_Kelt1h.json`) i „Kraken EMA 4h” (`config_Ema4h.json`). Strażnik zrestartowany przez `restart_roj.ps1`.
5. `START_WSZYSTKO.ps1` zostawiony bez zmian. Wpis „Kraken x2” szuka ogólnie `freqtrade.exe trade` i woła `START_KRAKEN.bat`, więc działa z nowymi nazwami. Dzięki temu nie dotykam pliku, który edytuje też Laboratorium (Z030).
6. `reports/roj_status.json`: wpisy przemianowane i opisane jak wyżej.

Skrypty, logi i surowe wyniki są na serwerze w `C:\Users\ktrut\kraken-boty\agent_20261118\` (`wyniki_eur.json`, `wyniki_eur10.json`, `wyniki_paxg.json`).

## Jak wrócić do starych botów

Przywrócić `START_KRAKEN.bat.bak_20261118` i `roj_straz.py.bak_20261118`, potem zrestartować procesy freqtrade.
