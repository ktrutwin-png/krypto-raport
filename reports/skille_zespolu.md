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
- (11.11) Z pakietu day-trader-skill: `trader-timemachine` (zanim padnie nowa strategia/setup: 10 000 symulacji sesji + każdy wcześniejszy raz, gdy setup wystąpił – uczciwe szanse), `trader-risk` (limity dzienne, max strata), `trader-exit` (stop i cel ustalone PRZED wejściem), `trader-budget` (wielkość pozycji do budżetu), `trader-scanner` i `trader-news` (akcje USA – dla IB Skanera i Zwiadowcy). Dane: Yahoo/SEC/Nasdaq (darmowe). `trader-broker` NIE jest zainstalowany – żaden skill nie składa zleceń.
- Skille dają wiedzę i procedury – same niczego nie handlują. Zasady stałe: tylko DEMO/paper, nie ruszać pozycji ręcznych (magic 0).

## Grafika 3D (Reżyser, agent strony)
- threejs-* (13) + `3d-metal-material`, `3d-sky-rays`, `3d-high-resolution-textures`, `3d-retina-resolution` → szczegóły w `tools/okladki/STYL.md` i szablon `tools/3d/`.

## Wideo (Reżyser, Social Media)
- Nasz własny silnik: `tools/kino/kino.py` + sceny 3D `tools/3d/` (podstawa każdego filmu, rozkaz R14).
- `hyperframes` + `hyperframes-cli` (11.11, HeyGen, Apache-2.0) – HTML → MP4 klatka po klatce: animowane wykresy, mapy, napisy, plansze tytułowe. Użyj, gdy potrzebny element, którego kino nie ma (np. animowany wykres słupkowy, mapa z liczbami, napisy słowo po słowie). Telemetria wyłączona (`npx hyperframes telemetry disable`); NIE uruchamiaj `npx hyperframes events` (to beacon telemetrii ze skilla – pomijamy). Tylko darmowe funkcje, bez planu Pro.
- `lemo-opuscar` (11.11) – biblioteka 66 stylów filmowych robionych w kodzie (np. caption-news, briefing-board, countdown, blueprint, „Evidence Films” z liczbami ze źródłami). Inspiracja, gdy Weekly albo specjalny film ma mieć inny charakter; zasada świeżych grafik dalej obowiązuje.

## Strona i design (agent strony, Reżyser – okładki/miniatury)
- `design-taste-frontend` (taste-skill) – kierunek artystyczny zamiast „generycznej strony AI”, referencje, sprawdzenie w przeglądarce.
- `impeccable` – słownik designu: polish/bolder, krytyka i audyt, wyłapuje AI-slop przed publikacją. Każda zmiana strony przechodzi audyt impeccable.
- `playwright-cli` – zrzuty ekranu i sprawdzanie strony w przeglądarce (narzędzie `playwright-cli` zainstalowane globalnie na serwerze).
- `img2threejs` – z obrazka referencyjnego model 3D w three.js (np. moneta, sztabka, logo) – łączyć z `3d-metal-material`.
- `ui-ux-pro-max` (11.11) – wiedza o układzie, paletach (192), parach fontów (74), dostępności i 120 zasadach UX; pytaj go przy każdej zmianie wyglądu strony/ORB/Hexy. `banner-design` – rozmiary i układy banerów, miniatur YT, okładek.
- Biblioteka DESIGN.md znanych marek: `C:\Hexa\design-md\` (awesome-design-md) – wzorce układu/typografii; nie kopiujemy logo ani nazw marek.

## Ogólne
- `no-ai-slop` – teksty (opisy, książka, skrypty lektora), `unlazy` – duże zadania z bramkami, `find-skills` – szukanie nowych skilli (instalujemy tylko sprawdzone: najpierw serwer, potem laptop).
