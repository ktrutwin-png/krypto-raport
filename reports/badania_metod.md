# Badania metod (agent Badacz)


## KOLEJKA OD SZEFA (do zrobienia przy najbliÅ¼szym przebiegu)
- 2026-11-28: KRONOS â€“ model AI do prognoz Å›wiec. Oficjalne repo TYLKO github.com/shiyu-coder/Kronos (MIT, praca AAAI/Tsinghua); forkÃ³w innych uÅ¼ytkownikÃ³w nie uÅ¼ywaÄ‡. Po przeglÄ…dzie bezpieczeÅ„stwa: osobny venv C:\Hexa\quant\kronos\.venv (nigdy Python botÃ³w), model NeoQuasar/Kronos-small z Hugging Face (CPU). Test: XAUUSD M15, min. 1 rok, kroczÄ…co bez zaglÄ…dania w przyszÅ‚oÅ›Ä‡ â€“ czy kierunek na 1â€“4 Å›wiece trafia istotnie >50% i czy jako FILTR (wejÅ›cie tylko gdy Kronos zgadza siÄ™ z sygnaÅ‚em) podnosi profit factor innych metod po kosztach. Brak przewagi = odrzuciÄ‡ z uzasadnieniem.
- 2026-11-28: pary zÅ‚otoâ€“srebro (stosunek XAU/XAG, powrÃ³t do Å›redniej) â€“ pomysÅ‚ z repo je-suis-tm/quant-trading (tylko do czytania).
- 2026-11-28: zrodla pomyslow (tylko do czytania, nie instalowac): paperswithbacktest/awesome-systematic-trading (strategie z publikacjami i backtestami - szukaj takich na zloto/srebro/towary/FX), wilsonfreitas/awesome-quant (lista narzedzi), stefan-jansen/machine-learning-for-trading (cechy do modeli ML/Kronos).
- 2026-11-28 01:00: od szefa - HKUDS/Vibe-Trading (agent AI: strategie z opisu, backtesty, eksport do MetaTradera) - tylko do przejrzenia pomyslow i sprawdzenia eksportu MT5, bez kluczy i bez instalacji na produkcji. Odrzucone: Gainium, OctoBot, Jesse, Passivbot, AutoHedge (krypto, mamy Freqtrade), Fincept (za ciezki na serwer), reszta nie o tradingu. heygen-com/hyperframes - zapas dla kino.py, gdyby nasz render nie wystarczal.

## 2026-11-28 - Kronos-small (foundation model swiec) na XAUUSD H1
Trafnosc kierunku: 1h 50,8% | 4h 51,2% | 12h 55,2% (rzut moneta = 50%)
Korelacja prognozy z ruchem: 0,05 / -0,02 / 0,08 (praktycznie zero)
PnL na uncje bez kosztow: 1h -67 $ | 4h -1 $ | 12h +131 $ (prosta regula momentum na 12h: +860 $)

Wniosek: na zlocie H1 Kronos nie ma przewagi. 1h i 4h = rzut moneta. 12h 55% wyglada lepiej,
ale okna sie nakladaja (krok 6h, horyzont 12h), wiec realnie ok. 125 niezaleznych prob -
to w granicach przypadku; prosta regula momentum zarobila w tym okresie wiecej.
WERDYKT: NIE bierzemy na zloto H1. Dalej: ten sam test na srebrze (XAGUSD) i Bitcoinie (dane Kraken),
ewentualnie zloto D1.
Pliki: C:\Hexa\lab\kronos (test_xau.py, wyniki.json, wyniki_okna.csv). Inferencja CPU: ~1h40 na 250 okien x3 scenariusze.



## 2026-11-28 – Metody sesyjne XAUUSD/XAGUSD (M15, 25.08.2022–27.11.2026, ~4,25 roku)
Dane: terminal MT5 botów (limit 100 000 świec → M5 tylko od 06.2025, więc test na M15). Czas: serwer = Amsterdam +1 h.
Koszty na transakcję: XAU 0,30 $ spread + 0,10 $ poślizg; XAG 0,030 + 0,010. SL ma pierwszeństwo w tej samej świecy, wyjście najpóźniej 21:30.
Poza próbą (OOS) = 28.11.2025–27.11.2026. Strojony tylko TP (1 / 1,5 / 2 R) na danych sprzed OOS; walk‑forward kotwiczony co rok. Wynik %/rok przy ryzyku 1%/transakcję.
Skrypty: C:\Hexa\quant\badania\ (backtest_sesje.py, vp_rozbicie.py, vp_retest_lata.py, wyniki_2026-11-28.json, vp_retest_transakcje.csv).

| Metoda | Rynek | n (całość/OOS) | Trafność | PF całość | PF OOS | PF walk‑fwd | Max DD | %/rok | Werdykt |
|---|---|---|---|---|---|---|---|---|---|
| Wybicie zakresu Azji (ASIA_BRK) | XAU | 843/163 | 50,7% | 1,02 | 1,35 | 0,99 | −33,5% | +0,6 | ODRZUCONA |
| Wybicie zakresu Azji | XAG | 845/164 | 43,1% | 0,76 | 1,32 | 0,76 | −71% | −21,5 | ODRZUCONA |
| Fałszywe wybicie Londynu (LON_FAKEOUT) | XAU | 491/102 | 35,0% | 0,87 | 0,76 | 0,85 | −46% | −11 | ODRZUCONA |
| Fałszywe wybicie Londynu | XAG | 502/90 | 34,3% | 0,60 | 0,48 | 0,58 | −82% | −34 | ODRZUCONA |
| Otwarcie NY 15:30–16:00 (NY_OPEN) | XAU | 340/73 | 41,8% | 0,89 | 0,72 | 0,82 | −25% | −4,7 | ODRZUCONA |
| Otwarcie NY | XAG | 371/70 | 38,8% | 0,67 | 0,75 | 0,60 | −55% | −15 | ODRZUCONA |
| Stosunek złoto/srebro (z>2, H1) | para | 311/69 | 56,9% | 0,57 | 0,69 | 0,55 | −62% | −20 | ODRZUCONA |
| Volume Profile szefa – całość (VP_SZEF) | XAG | 484/108 | 35,5% | 0,59 | 0,79 | 0,58 | −75% | −28 | ODRZUCONA |
| Volume Profile szefa – całość | XAU | 487/115 | 54,2% | 1,17 | 1,28 | 1,10 | −16% | +6,9 | częściowo |
| ↳ VP: fałszywe wybicie wartości → kontra | XAU | 260/67 | 45,4% | 0,87 | 0,85 | – | −18% | −3,1 | ODRZUCONA |
| **↳ VP: akceptacja poza wartością + retest VAH/VAL** | **XAU** | **227/48** | **64,3%** | **1,50** | **2,00** | – | **−9,5%** | **+10,4** | **PRZESZŁA (DEMO)** |

Wnioski (1 zdanie na metodę):
- ASIA_BRK XAU: działa tylko w 2026 (PF 2022–23 < 0,8), walk‑forward 0,99 – przewaga z jednego okresu, odrzucona.
- ASIA_BRK XAG: koszty srebra zjadają wybicia, tylko ostatni rok na plusie – odrzucona.
- LON_FAKEOUT (oba): kontra do fałszywego wybicia Azji traci we wszystkich latach poza 2022 – odrzucona.
- NY_OPEN (oba): kontynuacja pierwszych 30 min USA traci od 2023 – odrzucona.
- Stosunek XAU/XAG: małe zyski, duże straty (trend stosunku 2025–26 nie wraca do średniej), PF 0,57 – odrzucona.
- VP_SZEF XAG: na srebrze profil Azji nie działa po kosztach – odrzucona.
- VP_SZEF XAU fałszywe wybicie: część „fake” traci (PF 0,85–0,92) – odrzucona.
- **VP_SZEF XAU akceptacja + retest: PF > 1,2 w KAŻDYM roku (2022: 1,9 | 2023: 1,26 | 2024: 1,5 | 2025: 1,25 | 2026: 2,2), oba kierunki na plusie (long PF 1,66 / short 1,30), przy koszcie 0,60 $ nadal PF 1,34 – idzie na DEMO.**
Uwaga uczciwości: podział VP na „retest” i „fake” zrobiony po obejrzeniu wyników całości (ryzyko dopasowania); dlatego tylko DEMO i minimum 60 transakcji demo przed jakąkolwiek decyzją. Na M15 nie widać kolejności SL/TP w świecy (przyjęty gorszy wariant).

### Gotowe reguły – VP_RETEST_XAU (dla skanera / Laboratorium MT5, DEMO)
1. Profil Azji: świece M15 00:00–09:00 Amsterdam, wolumen tickowy rozłożony równo na zakres świecy, krok koszyka = 0,02% ceny; POC = koszyk z max wolumenem, Value Area 70% (rozszerzanie od POC w stronę większego wolumenu) → VAH/VAL.
2. Londyn 09:00–14:30: zamknięcie świecy 14:15–14:30 POWYŻEJ VAH → nastawienie LONG; PONIŻEJ VAL → SHORT; w środku – brak transakcji tego dnia.
3. USA: otwarcie 15:30 nadal po tej samej stronie (nad VAH dla long / pod VAL dla short), inaczej brak transakcji.
4. Wejście: zlecenie limit na VAH (long) / VAL (short), ważne 15:30–19:00 Amsterdam, maks. 1 transakcja dziennie.
5. SL: POC, ale nie bliżej niż 0,1 × ATR(14) dzienny (wtedy SL = VAH − 0,1·ATR / VAL + 0,1·ATR).
6. TP = 1 R (test 1,5 R: PF 1,30 całość / 1,65 OOS – wariant B do porównania w Lab).
7. Wyjście czasowe 21:30 Amsterdam; ryzyko 1% na transakcję (Lab: 0,5% do czasu 60 transakcji).
8. Oczekiwania z testu: ~55 transakcji/rok, trafność ~64%, PF ~1,5, max DD ~10% przy 1% ryzyka.

Następne kandydaty (kolejka): Kronos na XAGUSD/BTC/D1 (z kolejki szefa), Donchian/Keltner z filtrem trendu D1, sezonowość godzin/dni na XAU, VP_RETEST z filtrem trendu D1 (czy poprawi shorty).
