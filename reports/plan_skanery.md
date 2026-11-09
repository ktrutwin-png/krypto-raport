# PLAN AGENTA SKANERY (7.11–7.12.2026) – czyta go zadanie „Opiekun Skanera Claude”
Szef 7.11.2026: „ułóż plan każdemu agentowi… chcę widzieć wyniki od każdego agenta”. Skaner tylko wysyła sygnały na Telegram – nie handluje.


## ROZKAZY OD MÓZGU (🔭 Zwiadowca) – czytaj NAJPIERW, wykonuj po kolei
Mózg (Claude) wydaje rozkazy i kontroluje wyniki; agent odpowiada za wykonanie. Po wykonaniu: zmień [ ] na [x] i dopisz do „Postęp” jedną linijkę „ROZKAZ Rn: zrobione – dowód (plik/liczby)”. Nie da się? „ROZKAZ Rn: blokada – dlaczego”.
- [x] Z1 (7.11) Sprawdź, czy sygnały skanera na złocie zgadzają się z regułą szefa „3 świece M15 + dolar” – ile sygnałów było zgodnych, jaki wynik w R.

- [ ] Z2 (7.11) Skan WSZYSTKICH rynków: złoto, srebro, indeksy (US500, USTEC, DE40…), forex (główne pary), akcje z listy skanera i krypto (BTC, ETH, SOL, XRP + top 20 wg wolumenu – CoinGecko/Twelve_Data). Raz dziennie lista 3–5 najlepszych okazji na dzień / tydzień / miesiąc z oceną pewności i powodem; zapis do trading\\okazje_zwiadowcy.csv; wynik każdej okazji sprawdź po terminie (trafność).
- [x] Z3 (7.11) Po każdym przebiegu jedna linijka w reports/dziennik_zespolu.md.
## LEKCJE (📚 Nauczyciel dopisuje co tydzień – czytaj przed pracą i stosuj)
- (pierwsze lekcje po niedzieli 15.11.2026)

## UMIEJĘTNOŚCI I NARZĘDZIA (🔭 Zwiadowca)
- Narzędzia: skanery na laptopie (skaner_dzienny.py, ib_skaner.py), sygnaly_wyniki.csv, MT5 historia, Twelve_Data.
- Potrzebujesz nowego narzędzia? „PROŚBA DO MÓZGU: …” w „Postęp”.

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
- 2026-11-07: start planu
- 2026-11-08 (tydz. 1): ZDROWIE ok – skaner działa, stan co 2 min; 137× ERR 'No IPC' przy weekendowych zerwaniach MT5 (sam wraca po 2–4 min) → poprawka: po nieudanym połączeniu pomija rynki; restart 14:17 OK. Dane D1 świeże dla 6 rynków. ZADANIE TYG.: sygnaly_wyniki.py + sygnaly_wyniki.csv uruchomione i uzupełnione wstecz z logu (od 3.11): 1 sygnał – US500 RSI2 long 3.11→cel 5.11 = +0.59R netto, trafność 100% (n=1). Test ulepszenia: brak (wg planu).
- ROZKAZ Z1: zrobione – od 3.11 skaner nie wysłał ŻADNEGO sygnału na złocie (log: 0 wejść XAUUSD), więc 0 sygnałów do porównania z regułą „3 świece M15 + dolar”, wynik 0 R; skaner jest D1 (DON/SMA/USD), reguła szefa M15 – sprawdzać, gdy pojawi się pierwszy sygnał.
- ROZKAZ Z2: blokada – codzienny skan wszystkich rynków (3–5 okazji, okazje_zwiadowcy.csv) wymaga zadania dziennego; ten agent działa raz w tygodniu (nd). PROŚBA DO MÓZGU: przypisz Z2 do zadania codziennego Zwiadowcy albo dodaj mi dzienny przebieg.
- ROZKAZ Z3: zrobione – linijka w reports/dziennik_zespolu.md (8.11).
- ROZKAZ Z2: dzienny przebieg działa (pn–pt 06:47) – 9.11: 5 okazji w reports/okazje_zwiadowcy.csv (dane: Twelve_Data XAU/BTC, CoinGecko top 20, Yahoo Finance D1+1h dla 15 rynków), godziny w reports/godziny_rynkow.md. Uwaga: CSV w repo (reports/), nie w trading\\ na laptopie – przebieg chmurowy nie ma dostępu do laptopa.
