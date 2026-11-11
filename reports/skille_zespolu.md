# Skille zespołu (serwer = główna siedziba)

Wszystkie leżą na serwerze w `C:\Users\Administrator\.claude\skills\<nazwa>\SKILL.md` (kopie także na laptopie).
Agent w chmurze: zanim zacznie zadanie z listy niżej, czyta odpowiedni `SKILL.md` przez Remote_Desktop_Commander → read_file (deviceId 0b708a8f-66a5-4eeb-8a28-ac5878aae932). Czytaj tylko ten skill, którego potrzebujesz.

## Trading – boty, backtesty, sygnały (Mózg, Mechanik, Analityk, Inspektor)
- Nowa strategia / zmiana bota → `backtest-expert` + `backtesting-frameworks` (uczciwy test, out-of-sample, koszty, stress-test). Zmiana bota dalej tylko po „wdróż” szefa.
- Strategia stoi w miejscu → `strategy-pivot-designer`.
- Ocena wyników tygodnia/miesiąca → `trade-performance-coach`.
- Analiza wykresu (złoto, srebro, krypto, indeksy) → `technical-analyst`; kondycja rynku krypto → `crypto-regime-analyzer`.
- Ryzyko: obsunięcie konta → `drawdown-circuit-breaker`; zanim padnie ręczna transakcja szefa (Panel Szefa) → `pre-trade-discipline-gate` (bez planu / za duża / „odegranie się”).
- Bezpieczeństwo agentów handlujących → `llm-trading-agent-security`.
- Skille dają wiedzę i procedury – same niczego nie handlują. Zasady stałe: tylko DEMO/paper, nie ruszać pozycji ręcznych (magic 0).

## Grafika 3D (Reżyser, agent strony)
- threejs-* (13) + `3d-metal-material`, `3d-sky-rays`, `3d-high-resolution-textures`, `3d-retina-resolution` → szczegóły w `tools/okladki/STYL.md` i szablon `tools/3d/`.

## Ogólne
- `no-ai-slop` – teksty (opisy, książka, skrypty lektora), `unlazy` – duże zadania z bramkami, `find-skills` – szukanie nowych skilli (instalujemy tylko sprawdzone: najpierw serwer, potem laptop).
