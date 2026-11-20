# PLAN AGENTA SKANERY (7.11–7.12.2026) – czyta go zadanie „Opiekun Skanera Claude”
Szef 7.11.2026: „ułóż plan każdemu agentowi… chcę widzieć wyniki od każdego agenta”. Skaner tylko wysyła sygnały na Telegram – nie handluje.


## ROZKAZY OD MÓZGU (🔭 Zwiadowca) – czytaj NAJPIERW, wykonuj po kolei
Mózg (Claude) wydaje rozkazy i kontroluje wyniki; agent odpowiada za wykonanie. Po wykonaniu: zmień [ ] na [x] i dopisz do „Postęp” jedną linijkę „ROZKAZ Rn: zrobione – dowód (plik/liczby)”. Nie da się? „ROZKAZ Rn: blokada – dlaczego”.
- [x] Z1 (7.11) Sprawdź, czy sygnały skanera na złocie zgadzają się z regułą szefa „3 świece M15 + dolar” – ile sygnałów było zgodnych, jaki wynik w R.

- [ ] Z2 (7.11) Skan WSZYSTKICH rynków: złoto, srebro, indeksy (US500, USTEC, DE40…), forex (główne pary), akcje z listy skanera i krypto (BTC, ETH, SOL, XRP + top 20 wg wolumenu – CoinGecko/Twelve_Data). Raz dziennie lista 3–5 najlepszych okazji na dzień / tydzień / miesiąc z oceną pewności i powodem; zapis do trading\\okazje_zwiadowcy.csv; wynik każdej okazji sprawdź po terminie (trafność).
- [ ] Z4 (9.11, PILNE) Fałszywy sygnał: 9.11 17:05 skaner_dzienny wysłał „SPRZEDAŻ USDJPY (DON) – cena przebiła minimum z 55 dni (152.888)”, a cena była ~158.16 (minimum NIE przebite). Znajdź przyczynę (warunek DON, indeksy świec, dane D1 z MT5, tekst powodu), dopisz test, który by to złapał, i zgłoś poprawkę Mechanikowi przez Inspektora. Do czasu naprawy – sygnały DON z dopiskiem „do weryfikacji”. Szef: „zapisać w dzienniku agenta, który był za to odpowiedzialny”.
- [x] Z3 (7.11) Po każdym przebiegu jedna linijka w reports/dziennik_zespolu.md.
## LEKCJE (📚 Nauczyciel dopisuje co tydzień – czytaj przed pracą i stosuj)
- L1 (15.11) Okazje Zwiadowcy 9–13.11: 0/7 trafień, śr. −0,55 R; WSZYSTKIE 3 okazje z wejściem skończyły się stopem (śr. −1,0 R) – liczy się R okazji z wejściem, raportuj go osobno od „brak wejścia”.
- L2 (15.11) 4 z 7 okazji = brak wejścia (strefa za daleko od ceny) → strefa wejścia ≤0,5 ATR od ostatniego zamknięcia (stosowane od 12.11 – zmierz w tygodniu 16–20.11).
- L3 (15.11) Kontry pod trend przegrywają: XAU long 9.11 i GBP/USD long 10.11 = stopy; od 11.11 tylko „z trendem” (D1 pod/nad SMA20/50/200) – trzymaj, porównaj trafność po n≥10.
- L4 (15.11) Skala pewności nie kalibruje: obie okazje z pewnością 3 (XAU, USTEC 9.11) = −1 R. Co piątek tabela pewność → wynik; jeśli 3 nie bije 2 przy n≥10, zmień kryteria pewności.
- L5 (15.11) Cele 2–3 R przy stopie ~1 ATR dają 0 trafień w tygodniu z dużymi ruchami – HIPOTEZA: dla horyzontu „dzień” cel 1–1,5 R; sprawdź na historii okazji po n≥10.
- L6 (15.11) Skaner D1 (bt_ranking.py): najlepsze XAU SMA +1,65 R (n79), XAG SMA +0,94 R (n123); usunięty USDJPY DON short (−0,21 R od 2020). Decyzje o CFG tylko z rankingu historii – sygnaly_wyniki.csv ma n=1 (brak sygnałów od 3.11).
- L7 (15.11) Każdy warunek wybicia na ticku najpierw waliduje tick (ask>0, ask≥bid, spread ≤0,5%) – fantom USDJPY 9.11 powstał z pustego ticka (Z002).

## UMIEJĘTNOŚCI I NARZĘDZIA (🔭 Zwiadowca)
- Narzędzia: skanery na laptopie (skaner_dzienny.py, ib_skaner.py), sygnaly_wyniki.csv, MT5 historia, Twelve_Data.
- Potrzebujesz nowego narzędzia? „PROŚBA DO MÓZGU: …” w „Postęp”.
- 15.11 (Nauczyciel): CoinMarketCap `get_upcoming_macro_events` i `crypto_upcoming_event_calendar` (konektor, odczyt) – okna godzinowe okazji ustawiaj pod realne publikacje (CPI, FOMC, NFP) zamiast stałego 14:00–17:00; CoinGecko `get-trending` – szybki przegląd krypto, które się ruszają.

## Skanery w zakresie
skaner_dzienny.py (MT5, D1, pętla co 2 min) · IB Skaner (paper) – tylko obserwacja jego sygnałów.

## Cele na 30 dni (ocena 7.12.2026)
- Dziennik wyników sygnałów: każdy wysłany sygnał zapisany z wynikiem (SL/TP trafiony, wynik w R) w C:\Users\ktrut\Claude-telefon\trading\sygnaly_wyniki.csv.
- Średni wynik wysłanych sygnałów > 0 R po kosztach; rynek/strategia z ujemnym R po ≥ 10 sygnałach → usunąć z CFG (z komentarzem).
- Zero przestojów > 1 dnia; zero duplikatów (jedna wiadomość na sygnał).
- Co najmniej 1 przyjęte ulepszenie w miesiącu (reguły testu z zadania).

## Kolejność pracy
- Tydzień 1 (8.11): uruchom dziennik wyników sygnałów (osobny skrypt, nie zmienia logiki skanera) i uzupełnij go wstecz z logu.
- Tydzień 2 (15.11): ranking rynków/strategii wg R; usuń słabe.
- Tydzień 3 (22.11): filtr zmienności/trendu dla najsłabszej strategii.
- Tydzień 4 (29.11): test nowego rynku dla najlepszej strategii.

## Postęp
Zasada (Z005c, 11.11): każdy pisze TYLKO w swojej podsekcji – Zwiadowca w „### Zwiadowca”, Agent Skanery w „### Agent Skanery”. Starsze wpisy poniżej zostają, jak są.

### Agent Skanery
- 2026-11-15 (tydz. 2): ZDROWIE ok – skaner na serwerze żyje (1 proces, stan co 2 min), 7 dni bez ERR poza 8.11, po wyłączeniu serwera 14.11 22:51 wstał sam 15.11 04:03; poprawka Z002 (tick ask=0) jest w kodzie. SYGNAŁY: brak nowych od 3.11 – sygnaly_wyniki.csv n=1, +0.59R, 100%. RANKING (trading\\bt_ranking.py, D1 MT5, po spreadzie): XAU SMA +1.65R n79, XAG SMA +0.94 n123, XAU DON +0.61 n46, XAG DON +0.35 n29, XAU USD +0.25 n133, US500 RSI2 +0.17 n126, USTEC +0.16 n39, USDJPY DON L +0.16 n67, US30 +0.11 n128 – dodatnie w obu połówkach; USDJPY DON SHORT -0.03R (od2020 -0.21) → usunięty z CFG (kopia .bak_20261115, py_compile OK), restart zgłoszony (Z024). Dotyczy też Z4: SPRZEDAŻ USDJPY DON (źródło fantomu 9.11) po restarcie nie będzie wysyłana.

### Zwiadowca
- 2026-11-07: start planu
- 2026-11-08 (tydz. 1): ZDROWIE ok – skaner działa, stan co 2 min; 137× ERR 'No IPC' przy weekendowych zerwaniach MT5 (sam wraca po 2–4 min) → poprawka: po nieudanym połączeniu pomija rynki; restart 14:17 OK. Dane D1 świeże dla 6 rynków. ZADANIE TYG.: sygnaly_wyniki.py + sygnaly_wyniki.csv uruchomione i uzupełnione wstecz z logu (od 3.11): 1 sygnał – US500 RSI2 long 3.11→cel 5.11 = +0.59R netto, trafność 100% (n=1). Test ulepszenia: brak (wg planu).
- ROZKAZ Z1: zrobione – od 3.11 skaner nie wysłał ŻADNEGO sygnału na złocie (log: 0 wejść XAUUSD), więc 0 sygnałów do porównania z regułą „3 świece M15 + dolar”, wynik 0 R; skaner jest D1 (DON/SMA/USD), reguła szefa M15 – sprawdzać, gdy pojawi się pierwszy sygnał.
- ROZKAZ Z2: blokada – codzienny skan wszystkich rynków (3–5 okazji, okazje_zwiadowcy.csv) wymaga zadania dziennego; ten agent działa raz w tygodniu (nd). PROŚBA DO MÓZGU: przypisz Z2 do zadania codziennego Zwiadowcy albo dodaj mi dzienny przebieg.
- ROZKAZ Z3: zrobione – linijka w reports/dziennik_zespolu.md (8.11).
- ROZKAZ Z2: dzienny przebieg działa (pn–pt 06:47) – 9.11: 5 okazji w reports/okazje_zwiadowcy.csv (dane: Twelve_Data XAU/BTC, CoinGecko top 20, Yahoo Finance D1+1h dla 15 rynków), godziny w reports/godziny_rynkow.md. Uwaga: CSV w repo (reports/), nie w trading\\ na laptopie – przebieg chmurowy nie ma dostępu do laptopa.
- 2026-11-09 17:08 (Mózg): ⚠️ BŁĄD Zwiadowcy – fałszywy sygnał USDJPY SELL (DON) wysłany szefowi; minus do karty jakości tygodnia. Rozkaz Z4.
- 2026-11-10 (Zwiadowca): ROZKAZ Z4: częściowo – przyczyna ustalona przez Inspektora (Z002: warunek sprzedaży na `t.ask < lo55` przy pustym/zerowym ask po reconnectach MT5), poprawka i test (tick ask=0 → brak sygnału; poprawny tick USDJPY 158 > 152.888 → brak SPRZEDAŻY) opisane w zgłoszeniu Z002 u Mechanika; blokada: przebieg chmurowy bez dostępu do laptopa/serwera, więc testu nie dopisałem w kodzie. Sygnały DON traktować „do weryfikacji” do zamknięcia Z002.
- 2026-11-13 (Zwiadowca, TRAFNOŚĆ TYG. 9–13.11): rozliczone n=7, trafienia celu 0% (0/7), śr. R -0.55 (3× stop, 4× brak – w tym 3 bez wejścia, 0R). Horyzont: dzień n=4 0% śr. -0.21R · tydzień n=3 0% śr. -1.00R · miesiąc n=0. Klasa: forex n=4 0% -0.46R · metale n=1 0% -1.00R · indeksy n=2 0% -0.50R · krypto n=0 (otwarte BTC short 11.11 na +1.15R). Okno: 14:00–17:00 n=5 0% -0.57R · 15:30–17:30 n=1 0% -1.00R · 09:00–11:00 n=1 0% 0R. Wniosek: kontry/korekty pod trend (XAU long, GBP long) = stopy; 3 z 7 okazji uciekły bez retestu → wejścia ≤0.5 ATR od ceny (od 12.11).
- 2026-11-20 (Zwiadowca, TRAFNOŚĆ TYG. 16–20.11 + całość 30 dni): rozliczone razem n=28, cel 18%, śr. R +0.06 (z wejściem n=12, śr. +0.15R); w tym tygodniu dopisano 12 rozliczeń (5 celów, 3 stopy, 4× brak 0R). Horyzont: dzień n=9 11% +0.04R · tydzień n=14 29% +0.24R · miesiąc n=5 0% -0.40R. Klasa: forex n=12 25% +0.28R (z wejściem +0.68R) · metale n=6 17% +0.18R · krypto n=3 33% +0.43R · indeksy n=7 0% -0.57R (4 wejścia = 4 stopy). Okno: 14:00–17:00 n=15 27% +0.30R · 15:00–18:00 n=3 33% +0.43R · 15:30–17:30 n=4 0% -0.75R · 09:00–11:00 n=3 0% -0.33R · 14:30–17:00 n=3 0% 0R. Pewność (L4): 2 → n=25 20% +0.15R · 3 → n=3 0% -0.67R. Filtr „z trendem” (L3, od 11.11): n=19 26% +0.35R, z wejściem n=7 +0.95R vs przed 11.11 n=9 0%. Wniosek: forex/metale z trendem w 14:00–17:00 działają; indeksy na razie same stopy – od 20.11 max 1 okazja na indeksach dziennie.
