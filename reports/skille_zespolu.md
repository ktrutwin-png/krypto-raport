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
- (11.11, z najlepszych repo na GitHubie) Test i walidacja: `walk-forward-validation` (czy strategia działa poza danymi, na których ją ustawiono – obowiązkowo przed każdą zmianą bota), `vectorbt-expert` (szybkie backtesty w Pythonie, wiele wariantów naraz), `slippage-modeling` (realne koszty wejścia/wyjścia). Rynek: `regime-detection` (trend/konsolidacja/zmienność – kiedy bot ma pauzować), `volatility-modeling` (ATR, GARCH – stop i wielkość pozycji do zmienności), `correlation-analysis` (złoto vs dolar vs BTC – czy boty nie grają tego samego), `mean-reversion`. Ryzyko: `risk-management`, `kelly-criterion` (górna granica wielkości pozycji – stosować ułamek, nigdy pełne Kelly), `exit-strategies`. Dziennik: `trade-journal` (dla Analityka i książki szefa). Newsy: `market-news-analyst`, `scenario-analyzer` (co jeśli – Fed, CPI, wojna). Treści: `data-quality-checker` – Reżyser sprawdza nim liczby w opisach i raportach przed publikacją (np. ETF vs kontrakt, złe skale cen). MT5: `mql-developer` – Mechanik przy wskaźnikach/EA w MQL5.
- (11.11) Narzędzia Python na serwerze, osobne środowisko `C:\Hexa\quant\.venv` (nie rusza Pythona botów): **vectorbt** (backtesty wielu wariantów naraz) + **quantstats** (raport HTML: Sharpe, obsunięcia, miesięczna mapa). Przykład i test: `C:\Hexa\quant\test_narzedzi.py` (dane MT5 tylko do odczytu). Analityk – raport miesięczny wyników botów przez quantstats; Mechanik/Inspektor – test każdej zmiany: wybór parametrów na 1. połowie danych, sprawdzenie na 2. i porównanie z „kup i trzymaj”. Test 11.11 na złocie D1: MA45/60 trzyma Sharpe poza próbą (0,98 → 0,91), ale zarabia mniej niż samo trzymanie złota (+83,6% vs +116,7%) – strategia musi bić „kup i trzymaj”, inaczej nie ma sensu.
- Skille dają wiedzę i procedury – same niczego nie handlują. Zasady stałe: tylko DEMO/paper, nie ruszać pozycji ręcznych (magic 0).

## Grafika 3D (Reżyser, agent strony)
- threejs-* (13) + `3d-metal-material`, `3d-sky-rays`, `3d-high-resolution-textures`, `3d-retina-resolution` → szczegóły w `tools/okladki/STYL.md` i szablon `tools/3d/`.

## Wideo (Reżyser, Social Media)
- Nasz własny silnik: `tools/kino/kino.py` + sceny 3D `tools/3d/` (podstawa każdego filmu, rozkaz R14).
- `hyperframes` + `hyperframes-cli` (11.11, HeyGen, Apache-2.0) – HTML → MP4 klatka po klatce: animowane wykresy, mapy, napisy, plansze tytułowe. Użyj, gdy potrzebny element, którego kino nie ma (np. animowany wykres słupkowy, mapa z liczbami, napisy słowo po słowie). Telemetria wyłączona (`npx hyperframes telemetry disable`); NIE uruchamiaj `npx hyperframes events` (to beacon telemetrii ze skilla – pomijamy). Tylko darmowe funkcje, bez planu Pro.
- `lemo-opuscar` (11.11) – biblioteka 66 stylów filmowych robionych w kodzie (np. caption-news, briefing-board, countdown, blueprint, „Evidence Films” z liczbami ze źródłami). Inspiracja, gdy Weekly albo specjalny film ma mieć inny charakter; zasada świeżych grafik dalej obowiązuje.

## Grafika – narzędzia open source (11.11, wybrane z najlepszych repo GitHub)
- `bang-motion` (skill, MIT) – motion design: openery, kinetic typography, explainery jako jeden index.html; render przez hyperframes/Playwright.
- `rembg` (MIT, CPU) – wycinanie tła z obrazów do okładek i miniatur: `C:\Hexa\grafika\.venv\Scripts\rembg.exe i wejscie.jpg wyjscie.png`.
- TradingView **Lightweight Charts** (Apache-2.0) – na stronie duży wykres 30 dni (BTC/złoto/ETH); zostaw logo TradingView (wymóg licencji).
- Sceny 3D: filmowe wykończenie (winieta, ziarno, lekka aberracja) – domyślnie włączone, `"czysto": 1` wyłącza.
- Odrzucone: ComfyUI/Stable Diffusion (potrzebują karty graficznej, serwer jej nie ma), Remotion (licencja firmowa), Upscayl (AGPL), Vanta/Theatre (porzucone).

## Strona i design (agent strony, Reżyser – okładki/miniatury)
- `design-taste-frontend` (taste-skill) – kierunek artystyczny zamiast „generycznej strony AI”, referencje, sprawdzenie w przeglądarce.
- `impeccable` – słownik designu: polish/bolder, krytyka i audyt, wyłapuje AI-slop przed publikacją. Każda zmiana strony przechodzi audyt impeccable.
- `playwright-cli` – zrzuty ekranu i sprawdzanie strony w przeglądarce (narzędzie `playwright-cli` zainstalowane globalnie na serwerze).
- `img2threejs` – z obrazka referencyjnego model 3D w three.js (np. moneta, sztabka, logo) – łączyć z `3d-metal-material`.
- `ui-ux-pro-max` (11.11) – wiedza o układzie, paletach (192), parach fontów (74), dostępności i 120 zasadach UX; pytaj go przy każdej zmianie wyglądu strony/ORB/Hexy. `banner-design` – rozmiary i układy banerów, miniatur YT, okładek.
- Biblioteka DESIGN.md znanych marek: `C:\Hexa\design-md\` (awesome-design-md) – wzorce układu/typografii; nie kopiujemy logo ani nazw marek.

## Nauka i jakość pracy (11.11, wszyscy agenci – rozkaz R16)
- `self-improvement` (pskoett/pskoett-ai-skills, ★330) – zapis błędów, poprawek szefa i braków do `reports/nauka/` (format w `reports/nauka/README.md`).
- `learning-aggregator` – Inspektor w niedzielę: grupuje wpisy, liczy powtórzenia, wzorce ≥3 → propozycja zasady.
- `eval-creator` – z wypromowanej zasady robi test w `reports/nauka/TESTY.md`; Inspektor sprawdza co tydzień, czy zasada dalej trzyma.
- `verification-before-completion` (obra/superpowers, ★316k, MIT) – żadnego „gotowe” bez dowodu (klatki filmu, kod wyjścia, zrzut strony).
- `systematic-debugging` (superpowers) – przy błędzie: najpierw przyczyna, potem poprawka (Mechanik, Opiekun, Mózg).
- `writing-skills` (superpowers) – Mózg pisze i testuje nowe własne skille dla agentów (test na agencie przed i po).
- Odrzucone: `self-improving-agent` (wersja tylko dla OpenClaw), `verify-gate`/`skill-tester` (pod cudze repo z kodem), hooki automatyczne (niepotrzebne – zapis robi agent).

## Ogólne
- `no-ai-slop` – teksty (opisy, książka, skrypty lektora), `unlazy` – duże zadania z bramkami, `find-skills` – szukanie nowych skilli (instalujemy tylko sprawdzone: najpierw serwer, potem laptop).

## Gwiazdki na GitHubie (szef 11.11: „jeśli działa zajebiście – daj im gwiazdki”)
Zasada: repo dostaje gwiazdkę od szefa dopiero, gdy jego skill/narzędzie działa u nas dobrze co najmniej 2 tygodnie (bez błędów w reports/nauka, realnie używany). Zwiadowca skilli co tydzień dopisuje tu kandydatów; Mózg daje szefowi listę linków (kliknięcie ★ zajmuje sekundę – my nie mamy tokenu do jego konta GitHub).
| repo | używane od | stan | gwiazdka |
|---|---|---|---|
| obra/superpowers | 11.11.2026 | test | – |
| pskoett/pskoett-ai-skills | 11.11.2026 | test | – |
| heygen-com/hyperframes | 11.11.2026 | test | – |
| nextlevelbuilder/ui-ux-pro-max-skill | 11.11.2026 | test | – |
| mrdoob/three.js | 11.11.2026 | działa (sceny 3D) | do dania 25.11 |
