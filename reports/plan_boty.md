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
- L1 (15.11) Naprawa ≠ wdrożona: Z015 naprawiony 13.11, produkcja stara do 14.11; Z002 w pliku 11.11 04:50, aktywny dopiero 16:02 po restarcie. Każda naprawa kończy się testem NA ŻYWO albo linią DO RAPORTU z dokładnym poleceniem wdrożenia.
- L2 (15.11) Po każdej zmianie autostartu/usługi – test „co po restarcie serwera”: 3 przestoje z tej samej przyczyny (Z007 9–10.11 14,5 h, Z020 14–15.11 4,5 h, Z021 Kraken Pro nie wstał). Lista kontrolna = testy_agenta\lista_serwer.txt + Kraken Pro.
- L3 (15.11) Backtest Kraken M6c przesunięty 2× (11.11, 14.11), bo czas zjadły zgłoszenia → w środę ZACZNIJ od backtestu (pierwsze 15 min), zgłoszenia potem; Kraken 0 transakcji od 9.11, więc tylko backtest powie, czy strategie mają sens.
- L4 (15.11) Turbo stał przez brak marginu (Z011: 10019 No money przy poziomie 105%, ręczne XAUUSD szefa −2284 $) → boty na wspólnym koncie z ręcznymi pozycjami tracą wejścia. HIPOTEZA (nie wdrażać): osobne konto demo dla botów – przygotuj porównanie, decyzja po „wdróż”.
- L5 (15.11) Hexa ~12 tr/tydz. (PF 4,89, n=12) – próg 30 tr osiągnie ~28.11; do tego czasu NIE testuj zmian parametrów Hexy (mała próba), zbieraj kartę.
- L6 (15.11) Bot Szefa – HIPOTEZA do testu z dziennika szefa: 0/3 świec M15 zgodnych = 33% wygranych (n=6) vs ≥2 zgodne 94%; wszystkie 3 przegrane tygodnia = KUPNO trzymane przez CPI 10.11. Test filtra „0 świec zgodnych → nie wchodź” + „nie trzymaj przez CPI” dopiero przy n≥15.
- L7 (15.11) Zerwania MT5 „Authorization failed” (Z018) to aktualizacje buildu MetaQuotes, nie skrypty – nie szukaj błędu w kodzie botów, sprawdzaj journal terminala najpierw (oszczędza przebieg).
- L8 (15.11, wzorzec szybkich botów M7) Test szybkiego bota liczy KAŻDE zlecenie z prowizją IBKR + spreadem + poślizgiem min. 1 tick, i tylko na danych w czasie rzeczywistym – dane opóźnione (reqMarketDataType 3) nadają się do obserwacji, nie do oceny wyniku; zysk znika, jeśli średni ruch na transakcję < 3× koszt.

## UMIEJĘTNOŚCI I NARZĘDZIA (🔧 Mechanik)
- KONTO BOTÓW (od 16.11.2026 22:38, decyzja szefa): Hexa 830083, Turbo 830099, Indeksy 830122 handlują na OSOBNYM koncie MT5 demo **5058971085** (MetaQuotes-Demo, USD, start 5000 $, 1:25, hedging) w osobnym terminalu `C:\Hexa\MT5_boty\terminal64.exe /portable` (skrót „MT5 BOTY” na pulpicie serwera). Start: `launch_demo_boty.py hexa|turbo`, `START_HEXA_INDEKSY_boty.bat`, stan `state_demo_5058971085`. Konto 10013544792 (Program Files\MetaTrader 5) = TYLKO ręczne transakcje szefa (magic 0) – boty tam nie handlują. Każdy odczyt wyników botów: `mt5.initialize(r"C:\Hexa\MT5_boty\terminal64.exe")`. Raport 22:00 (raport22/zbierz_dzis.py) czyta oba konta (deals_raw z "konto":"boty"). Karty wyników/BAZA botów liczone od 16.11 od nowa (stare konto = historia do 16.11).
- Maszyna: od 9.11 SERWER vmi3737651 (Remote_Desktop_Commander – urządzenie vmi3737651; laptop DESKTOP-20N25SR wyłączony z obiegu, te same ścieżki C:\Users\ktrut\…). MT5 konto demo 10013544792 (3000 USD, 1:25), Hexa/Turbo po 0,01 lota.
- Narzędzia: desktop-commander, PowerShell, Python + MetaTrader5, MT5 historia, eToro (odczyt), IB paper, Freqtrade dry-run; testy w trading\testy_agenta.
- Potrzebujesz nowego narzędzia? „PROŚBA DO MÓZGU: …” w „Postęp”.
- 15.11 (Nauczyciel): skill `quanterlab:walk-forward-check` (akcje/ETF – np. Hexa Indeksy VOO DCH) – sprawdza, czy wynik backtestu nie jest dopasowany do historii; wynik do boty_rozwoj.log jako dodatkowy dowód przy „GOTOWE DO WDROŻENIA”. Kryptowalut (Kraken) nie obsługuje.

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
- 2026-11-14 Mechanik (sobota, BAZA tydz. 1 na nowym koncie od 9.11): Hexa 12 tr PF 4,89 śr R +1,30 netto +199,59 $; Turbo 4 tr PF 1,98 +32,09 $ (stoi – Z011); Indeksy 0; Kraken 0/0 tr; IB 0 (Gateway bez API); szef 37 tr traf 92% PF 2,72 +2417 $ (+6 otwartych -2284 $, margin 105%). Z018 = zerwania MetaQuotes-Demo przy aktualizacjach buildu (nie skrypty); szef_vs_boty.csv uzupełniony (Z019). Testy: brak – boty < 30 tr; M6c Kraken nadal zaległy (priorytet środa 18.11). Tydz. 2 (ryzyko, % kapitału, ATR) – zaczynam od Turbo/Hexa po wdrożeniu Z011.
- 2026-11-15 Mechanik: Z023/A1 – dziennik_szefa.py ma kolumny komentarz+koszyk (PANEL/MT5_RECZNY), test OK (37/87 uzupełnione; 2–6.11 brak historii MT5 na serwerze, 0 transakcji PanelTG od 9.11). Z021 Kraken Pro żyje (Autostart .bat→.ps1). Z020 cz.2 (Windows Update) i Z022 (prompty) – gotowe do wdrożenia.
- 2026-11-16 Mechanik: Z025 wygasło (do sprawdzenia), Z026 panel_tg poprawka gotowa do wdróż (timeout Telegrama blokuje przyciski do 35 s), Z027 strona naprawiona (test 390 px OK).
- 2026-11-18 Mechanik (środa, przegląd tydz. 2): Z029 Indeksy – SPY/indeksy CFD na koncie botów wyłączone (tm=0), DAX ETF niepłynny → GOTOWY DO WDROŻENIA PLAN {"VOO": ["DCH"]} (701 tr, +0,088R, PF 1,18, połowy +0,108/+0,069R); odrzucone IVV/EWG/QQQM/IWM. Z031 – mój skrypt zapchał Market Watch terminala botów (03:43–03:55 UTC, „Cannot select”), przywrócone. Karta (konto botów od 16.11): Hexa 1 tr −22,07 $, Turbo 1 tr −22,05 $, Indeksy 0, Kraken 0 tr (nowe boty), IB 0; szef 7 dni 26 tr PF 1,17 +448 $. Hexa/Turbo: brak testu (< 30 tr, ryzyko % i SL ATR już są).
- 2026-11-19 Mechanik: Z032 IB Gateway – zadziałało po restarcie Gateway 18.11 21:52 CET (lab/warianty/szybki znów połączone i handlują), do sprawdzenia przez Inspektora; Z033 – poprawka promptu Reel czeka na wdróż.

## Hexa – odczyt kont (szef 19.11.2026)
- [x] 19.11: narzędzie Hexy „boty” – stan konta botów MT5 5058971085 (saldo, wynik dnia per bot, otwarte pozycje), C:\Hexa\rdzen\stan_botow.py, tylko odczyt, tylko dla szefa.
- [ ] Gdy ruszy konto IBKR (Gateway/IBC na serwerze): dołożyć Hexie odczyt stanu konta IBKR (saldo, wynik dnia, pozycje) – tak samo jak „boty”, tylko odczyt. Szef: „dopisz to sobie w swoich planach”.
