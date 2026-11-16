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
- Odrzucone: ComfyUI/Stable Diffusion (potrzebują karty graficznej, serwer jej nie ma), Remotion (licencja firmowa – POPRAWKA 16.11.2026: darmowa dla osób prywatnych i firm do 3 osób, więc nas obejmuje → przyjęte), Upscayl (AGPL), Vanta/Theatre (porzucone).

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

## Kolejka do instalacji (Zwiadowca skilli 15.11 – serwer był offline, wstępny przegląd zrobiony w chmurze)
Instalować w następnym przebiegu po końcowym przeglądzie na serwerze (C:\Hexa\przeglad\<repo>), pojedynczo przez `-s <skill>`, bez pluginów i hooków:
- `AgriciDaniel/claude-seo` (★29k, MIT, aktualizacja 14.11) – skille `seo-audit`, `seo-technical`, `seo-geo`, `seo-schema`, `seo-page` dla agenta strony (audyt SEO + widoczność w ChatGPT/Perplexity). Rdzeń bez telemetrii i bez kluczy; NIE instalować wersji plugin (ma hook PostToolUse na Edit/Write) ani rozszerzeń płatnych (DataForSEO, Ahrefs, SE Ranking, Firecrawl).
- `coreyhaines31/marketingskills` (★60k, MIT, 11.11) – `social`, `copywriting`, `content-strategy`, `video` dla Reżysera/Social Media (Instagram/YouTube). Bez hooków; `tools/clis/*` wymagają płatnych kluczy – pomijamy.
- Do oceny: `tt-a1i/archify` (★96k, Apache-2.0) – interaktywne diagramy z planu/kodu (strona /brain/, wyjaśnienia dla szefa).
- Odrzucone: OpenMontage (AGPL-3.0), alpaca-skills / hypergrok-trading-desk / roman-rr/trading-skills (składanie zleceń lub sygnały na żywo), aiskillstore/marketplace (brak licencji).

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
- Odłożone (16.11.2026): ethanplusai/sellbird (~5,7k ★) – automat cold-mail B2B; przyda się dopiero na etapie sprzedaży usług; uwaga RODO/NL. Zasada szefa: mało ale najlepsze.

- Do instalacji (16.11.2026, znalezione przez szefa, przegląd bezpieczeństwa OK na serwerze w C:\Hexa\przeglad – brak sieci, kluczy, hooków):
  - `Jakeschincariol/instagram-agent-skill` (★6,6k, MIT) – 13 skilli /ig-reel, /ig-caption, /ig-plan, /ig-audit, /ig-human… dla Social Media/Reżysera.
  - `remotion-dev/skills` (oficjalne) – remotion-best-practices, -create, -render, -captions, -multimedia, -docs, -license: filmowe napisy i animacje zamiast „tandetnych” (decyzja szefa 16.11).
  - `Remocn/remocn` (★1,7k, MIT) – gotowe animacje/przejścia do Remotion.
  - `Motionsites-AI/claude-skill` (★2,1k; instrukcje MIT, przykłady i media © MotionSites – wolno używać do budowy stron, nie wolno odsprzedawać) – skill motionsites-web-builder: kinowe strony i hero (spec z prawdziwymi wartościami, media, pętla screenshot→ocena→poprawki przez scripts/shoot.py, Playwright). Dla agenta strony (erlgrey83-crypto-freaq) i ORB; zastępuje zgadywanie przy „wow” stronach. Przegląd 16.11: shoot.py robi tylko lokalne zrzuty, bez kluczy i wysyłek. (Szef 16.11, Reels thedigitalkinggg.)
  - `DeusData/codebase-memory-mcp` (MIT, jeden plik wykonywalny, Windows OK, zero telemetrii i ruchu sieciowego, bez klucza API) – lokalny graf wiedzy kodu jako serwer MCP: kto wywołuje co, zależności, skutki zmian; typy dla Javy i Pythona. TEST na serwerze na kodzie ORB (C:\Hexa\orb\orb-src) + krypto-raport. Opcjonalnego CBM Lens (model z Hugging Face) nie włączać. Zostaje, jeśli przyspieszy poprawki ORB. (Szef 16.11, Reel valeridoesai.)
  - Odrzucone 16.11: `trailhq/Trail-Code` (dawniej Graft) – to samo zadanie co codebase-memory-mcp, ale z telemetrią i opcją chmury; bierzemy jedno narzędzie do mapy kodu, lżejsze i w pełni lokalne.
  - `calesthio/OpenMontage` (AGPLv3 – do użytku wewnętrznego OK, nie udostępniać jako usługi) – agentowe studio wideo: koncepcje → storyboard z akceptacją i kosztem PRZED generowaniem → Remotion/HyperFrames/FFmpeg, self-review (ffprobe, klatki, audio). Dubluje częściowo nasz KINO + Remotion/HyperFrames/piper/ElevenLabs → TEST dopiero PO premierze odc. 1 (21.11), na jednym Reelu albo odc. 2; jeśli lepsze od KINO – zastępuje część naszego łańcucha zamiast dokładać. Klucze tylko darmowe (Pexels/Pixabay) + nasz ElevenLabs z puli Lektor. (Szef 16.11, Reel valeridoesai.)
  - `msitarzewski/agency-agents` (MIT, 330 person agentów) – NIE instalujemy całości; 4 wzorce skopiowane do `reports/wzorce/agency-agents/` (Pisarz, Reżyser ×2, Inspektor). Działa od 16.11 – gwiazdka, jeśli poprawi jakość.
  - Kopiowanie do C:\Users\Administrator\.claude\skills z sesji Mózgu zablokowane przez zabezpieczenia → instaluje Zwiadowca skilli w swoim przebiegu (`npx skills add`).
