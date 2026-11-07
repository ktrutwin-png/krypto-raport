# PLAN AGENTA BOTY (7.11–7.12.2026) – czyta go zadanie „Agent Boty”
Szef 7.11.2026: „ułóż plan każdemu agentowi… chcę widzieć wyniki w każdej dziedzinie od każdego agenta”. Wszystko DEMO / paper / dry-run. Agent tylko mierzy i testuje; wdrożenie po „wdróż” szefa w rozmowie z Claude.

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
