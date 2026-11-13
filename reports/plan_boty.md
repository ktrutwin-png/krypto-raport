# PLAN AGENTA BOTY (7.11–7.12.2026) – czyta go zadanie „Agent Boty”
Szef 7.11.2026: „ułóż plan każdemu agentowi… chcę widzieć wyniki w każdej dziedzinie od każdego agenta”. Wszystko DEMO / paper / dry-run. Agent tylko mierzy i testuje; wdrożenie po „wdróż” szefa w rozmowie z Claude.


## ROZKAZY OD MÓZGU (🔧 Mechanik) – czytaj NAJPIERW, wykonuj po kolei
Mózg (Claude) wydaje rozkazy i kontroluje wyniki; agent odpowiada za wykonanie. Po wykonaniu: zmień [ ] na [x] i dopisz do „Postęp” jedną linijkę „ROZKAZ Rn: zrobione – dowód (plik/liczby)”. Nie da się? „ROZKAZ Rn: blokada – dlaczego”.
- [x] M1 (7.11) Bot Szefa: test KONFLUENCJI reguł szefa (3 świece + knot + dolar) na 2,5 roku M15, wynik do boty_rozwoj.log.
- [x] M2 (7.11) Przygotuj listę wszystkiego, co trzeba przenieść na serwer (procesy, foldery, autostart, pliki stanu) – serwer Contabo Windows od 8.11.

- [x] M3 (7.11) Kontrola wszystkich agentów: przy każdym przebiegu list_triggers (wszystkie strony) – ostatni przebieg każdego agenta i zadania (Reżyser/Reels, Weekly, Analityk, Zwiadowca/Opiekun Skanera, Pisarz, eToro…), błędy, czy jest wpis w dzienniku zespołu, czy rozkazy w planach nie stoją > 7 dni. Problem → „UWAGA DLA <Agent>” w dzienniku + gotowa poprawka dla Mózgu.
- [x] M4 (7.11) Po każdym przebiegu jedna linijka w reports/dziennik_zespolu.md.
- [ ] M5 (7.11) Strumień 2 z reports/plan_biznes.md: wskaźnik MT5 (MQL5) „3S+K+DXY” – strzałki na wykresie, gdy 3 świece M15 + knot + dolar są zgodne; skompiluj w MetaEditor, test na demo, zrzuty ekranu i opis produktu w trading\produkty\. Bez handlu (tylko wskaźnik).
- [ ] M6 (9.11, PILNE – szef: „Kraken trzeba gęsto pilnować i poprawiać, dawno nic nie robiliśmy i nie wiemy, jak działają”) KRAKEN NA SERWERZE. Od 9.11 18:24 Freqtrade chodzi na serwerze vmi3737651 (dry-run, portfel 1000 EUR): C:\Users\ktrut\kraken-boty, strategie Donch4hBTC i Mom1dBTC (user_data\strategies\KrakenTrendBTC.py), bazy Donch4hBTC.sqlite / Mom1dBTC.sqlite, logi user_data\logs\*.log. Przy KAŻDYM przebiegu (codziennie 04:41): (a) czy oba procesy freqtrade żyją i log jest świeży (heartbeat), błędy/wyjątki z logu; (b) z baz sqlite (tylko odczyt, sqlite3 w Pythonie): otwarte i zamknięte transakcje, wynik dnia i od 9.11 (EUR i %), trafność, PF, maks. obsunięcie; (c) raz w tygodniu (środa) backtest obu strategii na świeżych danych (freqtrade backtesting w .venv, osobny katalog wyników) i porównanie z wynikiem dry-run – czy strategia w ogóle ma przewagę; (d) jedna hipoteza poprawy na tydzień (np. filtr trendu, ATR-stop, inny interwał, inne pary EUR), test w obu połowach historii, ≥ 30 transakcji – wynik do boty_rozwoj.log jako GOTOWY DO WDROŻENIA albo ODRZUCONY. Zmiany w configach/strategii i restart Freqtrade – TYLKO po „wdróż” szefa (przez Mózg). Karta wyników Kraken w boty_rozwoj.log co przebieg. Problem → „BŁĄD: Kraken …” w dzienniku zespołu (Inspektor).
- [ ] M7 (10.11, szef: „zleć wszystkim agentom stworzenie nowego bota na IBKR do szybkich transakcji, w tle na serwerze”) NOWY BOT IBKR – SZYBKIE TRANSAKCJE (konto PAPER DUR315177, serwer vmi3737651, IB Gateway port 4002, biblioteka ib_async w C:\Users\ktrut\Claude-telefon\pylib, wzór połączenia: C:\Users\ktrut\Claude-telefon\ib\ib_skaner.py). Kolejność: (1) DANE: IB Skaner używa danych OPÓŹNIONYCH (reqMarketDataType(3)) – sprawdź, czy konto paper ma dane w czasie rzeczywistym dla wybranych rynków; jeśli nie – „DO RAPORTU: szybki bot wymaga subskrypcji danych IBKR <jakiej, koszt/mies.>” (decyzja szefa, budżet ~20 €/mies.) albo sygnał z danych MT5/Twelve Data, a wykonanie na IBKR. (2) RYNKI i GODZINY: rynki z Zwiadowcą (reports/godziny_rynkow.md) – płynne (np. MGC/GC złoto, MES/ES, EUR.USD, akcje US o dużym wolumenie). (3) KOSZTY: prowizje IBKR + spread + poślizg ZAWSZE w teście – przy szybkich transakcjach to one decydują. (4) STRATEGIA: 2–3 kandydatów (np. wybicie z otwarcia sesji, powrót do VWAP, momentum M1–M5), backtest na danych 1-min ≥ 3 mies., obie połowy historii, ≥ 100 transakcji, PF po kosztach ≥ 1,1, maks. obsunięcie < 10%. (5) KOD: nowy folder C:\Users\ktrut\Claude-telefon\ib\szybki\ (osobny clientId, np. 31, osobny orderRef „SZYBKI”), tryb obserwacji (bez zleceń) + log sygnałów przez min. 3 dni sesyjne; sprawdzenie, że to konto paper (DU…), limit pozycji i dziennego stopu. (6) Wynik: „GOTOWY DO WDROŻENIA” w boty_rozwoj.log i DO RAPORTU – uruchomienie handlu (nawet paper) dopiero po „wdróż” szefa. Pracuj w tle, jeden krok na przebieg, postęp w „Postęp”.
## LEKCJE (📚 Nauczyciel dopisuje co tydzień – czytaj przed pracą i stosuj)
- (pierwsze lekcje po niedzieli 15.11.2026)

## UMIEJĘTNOŚCI I NARZĘDZIA (🔧 Mechanik)
- Maszyna: od 9.11 SERWER vmi3737651 (Remote_Desktop_Commander – urządzenie vmi3737651; laptop DESKTOP-20N25SR wyłączony z obiegu, te same ścieżki C:\Users\ktrut\…). MT5 konto demo 10013544792 (3000 USD, 1:25), Hexa/Turbo po 0,01 lota.
- Narzędzia: desktop-commander, PowerShell, Python + MetaTrader5, MT5 historia, eToro (odczyt), IB paper, Freqtrade dry-run; testy w trading\testy_agenta.
- Potrzebujesz nowego narzędzia? „PROŚBA DO MÓZGU: …” w „Postęp”.

## Boty w zakresie
MT5: Hexa (830083), Turbo (830099) · IBKR paper: IB Skaner · Kraken: Freqtrade/FreqAI dry-run · eToro demo: Pula 500, Pula 500 Turbo, Pula 1k, łowcy sygnałów (EU/USA). Ręczne transakcje szefa (magic 0) tylko do porównania.

## Cele na 30 dni (ocena 7.12.2026)
- Każdy bot: pełna karta wyników (transakcje, trafność, profit factor, średni R, maks. obsunięcie, wynik netto po kosztach) aktualizowana co przebieg.
- Bot z ≥ 30 transakcjami i profit factor < 0,8 → propozycja wyłączenia albo przebudowy (z dowodem).
- Cel jakości: profit factor ≥ 1,1 po kosztach i maks. obsunięcie < 15% kapitału demo dla każdego bota, który zostaje.
- Co najmniej 2 ulepszenia „GOTOWE DO WDROŻENIA” w miesiącu (test w obu połowach historii, ≥ 30 transakcji).
- Tabela „szef vs boty” co tydzień.

## Kolejność pracy
- Tydzień 1 (do 14.11): audyt i linia bazowa – karta wyników każdego bota zapisana w boty_rozwoj.log jako BAZA.
- Tydzień 2 (do 21.11): ryzyko – wielkość pozycji jako stały % kapitału zamiast stałego lota, SL/TP oparte o ATR; najpierw bot z największym obsunięciem.
- Tydzień 3 (do 28.11): filtry – trend (EMA/wyższy interwał), zmienność (ATR), godziny handlu; najpierw bot z najniższym PF.
- Tydzień 4 (do 7.12): rozszerzenie – najlepsza strategia testowana na 1–2 nowych rynkach.

## Zasady
- Jedna hipoteza na bota na przebieg; zapisuj też testy odrzucone (żeby ich nie powtarzać).
- Bez wyjść czasowych; koszty (spread/prowizja) zawsze w teście.
- Nigdy: real, ręczne pozycje szefa, hasła/klucze, uruchamianie wyłączonych botów.

## Projekt „Bot Szefa” – skalping bez SL (cel: start realnego konta 1.01.2027)
- Wzorzec = ręczne transakcje szefa na demo MT5 (magic 0, XAUUSD), tylko ODCZYT historii. Baza 2–6.11.2026: 46 transakcji, 83% wygranych, śr. +0,18% ruchu na wejście, śr. czas 2,5 h, ~2,2–2,5% ruchu złota łapane dziennie.
- Zasady bota: bez SL, maks. 3 pozycje naraz, lot = reguła szefa (3 pozycje przetrwają ruch 25%, maks. strata 60% kapitału), krótkie TP.
- Zadania: co tydzień przelicz statystyki szefa (dzień po dniu) → szukaj w danych M5/M15, co łączy jego wejścia (godzina, kierunek trendu H1, odległość od EMA, ATR) → zbuduj regułę wejścia → test na historii lat (najgorszy dołek, czas zamrożenia, czy konto przeżywa), z kosztami i dźwignią 1:20 (UE).
- Reguły szefa (7.11, z jego słów): (1) kierunek 3 ostatnich zamkniętych świec M15 = kierunek wejścia (u szefa 72% wejść, 88% wygranych); (2) 6 świec: czerwona z dolnym knotem pod dołkami 5 poprzednich → spadek w ≤45 min; potem zielona z górnym knotem ponad ostatnią czerwoną → wybicie w 15–45 min; (3) dolar (DXY z 6 par, wykres.dxy) – przy skokach na newsach złoto reaguje odwrotnie w tej samej świecy (82%). Każda reguła osobno ≈ 50% na 2,5 roku M15 → testuj KONFLUENCJĘ 1+2+3 razem oraz porównanie sygnałów wziętych vs pominiętych przez szefa.
- Dziennik szefa: panel_tg\notatki\ (głosówka .ogg + tekst + wykres + świece + pozycje w .json, zbiorczo notatki.csv) – czytaj co tydzień i łącz z jego transakcjami.
- Gotowe do wdrożenia dopiero gdy: ≥ 200 transakcji w teście, wynik dodatni w obu połowach historii, konto przeżywa najgorszy okres. Bot tylko na demo; uruchamia szef.
- Tygodniowo: tabela „szef vs Bot Szefa” + tempo wyzwania 5 000 € → 1 000 000 €.

## Postęp
- 2026-11-07: start planu
- 2026-11-07: dodany projekt „Bot Szefa” (skalping bez SL) i cel realnego konta od 1.01.2027
- 2026-11-07: reguły szefa (3 świece, knoty, dolar) + dziennik głosowy w panelu
- 2026-11-07: BAZA tydz. 1 w boty_rozwoj.log – Hexa 4 tr PF 2.41 +131 USD; Turbo 5 tr PF 0.91 −45; IB 0 tr; Freqtrade NIE DZIAŁA od 26.10 (0 tr); eToro demo bez kopii 60 tr PF 0.30 −1746 (kwalifikuje się do przebudowy); szef 50 tr PF 3.50.
- ROZKAZ M1: zrobione – konfluencja 1+2+3 na XAUUSD M15 05.2024–11.2026: 321 tr, PF 0.88, śr. R −0.064 (obie połowy ujemne) → ODRZUCONY; skrypt testy_agenta\konfluencja_szefa.py.
- ROZKAZ M2: zrobione – testy_agenta\lista_serwer.txt (10 procesów, foldery, pliki stanu; brak autostartu botów; Hexa i Turbo mają po 2 procesy – do wyjaśnienia).
- ROZKAZ M3: zrobione (ten przebieg) – 34 zadania: eToro kontrola maszyny i eToro przegląd tygodnia ostatnio FAILED 01.11 (limit), Kronikarz FAILED 02.11 i dubluje Pisarza; reszta aktywnych OK.
- ROZKAZ M4: zrobione – linijka w dziennik_zespolu.md.
- 2026-11-07 ANALITYK (wnioski dla Mechanika): 50 tr szefa 2–6.11: 82% wygr., śr. +0,205% ruchu/wejście, PF 3,50, najgłębszy minus −2,77%; reguły a/b/c: 0–1 zgodnych → 68% wygr. (25 tr), 2–3 zgodne → 96% (25 tr). Szkic „a+c” (≥2 z 3 świec M15 + DXY przeciwnie) na XAUUSD M15 04.2024–11.2026, TP +0,2%, bez SL: 11 621 syg., 95,9% TP w 20 dni, śr. 16,5 h, minus >3% w 7,6% – KIERUNEK PRZECIWNY 95,6% / 7,6→8,6%, LOSOWO 95,4% / 9,0% → szkic BEZ przewagi (wysoka trafność to skutek braku SL + mały TP). Przewaga szefa = selekcja chwili, nie reguła. Skrypty: testy_agenta\analiza_szefa.py, bt_metoda_szefa.py; wyniki trading\analiza_szefa.log. Dla Bota Szefa: nie budować wejścia z a+c; kolejny krok – cechy, gdzie szef NIE wchodzi (pominięte sygnały) i czas do TP zamiast % wygranych.
- 2026-11-10 Mechanik: Z002 (fałszywy sygnał USDJPY) – blokada, serwer i laptop offline; Z003–Z006 → GOTOWE DO WDROŻENIA; M6 Kraken – dziś brak karty (brak dostępu do serwera).
- 2026-11-11 Mechanik (środa, przegląd): Z002 poprawione w skaner_dzienny.py (kopia .bak_20261111, test suchy OK; czeka na restart skanera – wdróż); Z008 → naprawione u źródła (panel loguje „MT5 OK (wrocil)”); nowe Z010 – IB Gateway bez API od 23:45 (czeka na logowanie). Karta: Hexa 0 tr, Turbo 2 tr +60,16, Kraken 0/0 tr, IB 0, szef 24 tr PF 0,80 −283,62. M6: karta Kraken zrobiona (0 tr), backtest M6c – blokada czasu, przeniesiony na sobotę 14.11.
- 2026-11-12 Mechanik: Z011 Turbo – przyczyna w hexa_runtime.py (wyjątek order_check omija 'rejected', intencja blokuje wejścia) → poprawka gotowa do wdróż; Z009 – zamiennik SPY: VOO DCH (701 tr, +0,088R, obie połowy +), D15 na S&P odrzucone; Z012 nieaktualne. Wolny margin konta 47 $.
- 2026-11-13 Mechanik (pt): Z015 strona – <main> + linki stopki 29 px (repo, test 390 px OK; na żywo po wdrożeniu Vercel); Z016 kino.py "glos" – działa przy pustym "say", ostrzeżenie przy złej ścieżce, opis + README (test OK); Z013/Z014 harmonogram → gotowe do wdróż.
