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

## Postęp
- 2026-11-07: start planu
