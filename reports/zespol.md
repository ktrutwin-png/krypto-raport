# Zespół agentów szefa (od 7.11.2026)
Szef rozmawia TYLKO z Claude („mózg”). Claude prowadzi agentów, uczy ich, sprawdza wyniki i odpowiada za całość.

| Agent | Dział | Plan | Co robi |
|---|---|---|---|
| 🎬 Reżyser | Social Media (Instagram + YouTube @erl.grey83) | reports/plan_wzrostu.md | filmy i Reels wg planu wzrostu, Weekly Market Brief, wyniki zasięgów |
| 📊 Analityk | Trading szefa (MT5, Panel Szefa, dziennik głosowy, wyzwanie 5 000 € → 1 000 000 €) | reports/plan_boty.md (Bot Szefa) | sobotnia analiza handlu szefa, reguły (3 świece, knoty, dolar), tempo wyzwania |
| 🔧 Mechanik | Boty (Hexa, Turbo, Kraken, eToro, IB) | reports/plan_boty.md | zdrowie i wyniki botów, testy ulepszeń, budowa Bota Szefa |
| 🔭 Zwiadowca | Skanery (sygnały, rynki) | reports/plan_skanery.md | jakość sygnałów, wyniki w R, filtry, nowe rynki |
| ✍️ Pisarz | Książka „Filozofia tradingu” | laptop ksiazka\\rozdzialy.md (zasady stylu) | co niedzielę 15:23 wpis do dziennika + jeden rozdział, po cichu, pokaz po roku |
| 💼 Handlowiec | Biznes – usługi AI dla firm, sprzedaż produktów | reports/plan_biznes.md | oferty, cenniki, lista firm, szkice wiadomości – wysyła szef |
| 📐 Projektant | (później) projekt wózka dziecięcego | – | uruchamiany, gdy szef zacznie projekt |

Zasady wspólne: konta demo/paper, nic nie zmieniają bez zgody szefa, uruchamia szef, przegląd miesięczny 7.12.2026.

## Jak dowodzi Mózg
- Rozkazy: sekcja „ROZKAZY OD MÓZGU” na górze planu każdego agenta (plan_wzrostu, plan_boty, plan_skanery). Agent czyta je najpierw, wykonuje, odhacza [x] i zapisuje dowód w „Postęp”.
- Umiejętności: sekcja „UMIEJĘTNOŚCI I NARZĘDZIA” w tym samym planie. Brakuje narzędzia → agent pisze „PROŚBA DO MÓZGU”, Mózg podpina.
- Kontrola: Mózg sprawdza odhaczone rozkazy i dowody przy każdej rozmowie z szefem o agentach i w przeglądzie 7.12.

## Role rozszerzone (szef 7.11.2026: „z dnia na dzień agenci mają być lepsi… mają współpracować, sprawdzać siebie nawzajem, ale działać też na zewnątrz każdy w swojej dziedzinie”)
- 🔧 Mechanik – naprawia WSZYSTKO: oprócz botów sprawdza każdego agenta (ostatnie przebiegi zadań, błędy, czy zostawił wpis w dzienniku zespołu, czy rozkazy stoją); diagnoza + gotowa poprawka dla Mózgu.
- 🔭 Zwiadowca – skanuje WSZYSTKIE rynki (złoto, srebro, indeksy, forex, akcje, krypto); szuka najlepszych okazji na dany termin (dzień / tydzień / miesiąc) z oceną pewności; tylko informacja, decyzję podejmuje szef.
- 📊 Analityk – największe ruchy walut i rynków na świecie (co, o ile, dlaczego, co dalej), najmniejsze szczegóły; oraz kontrola jakości pracy innych agentów (liczby, trafność sygnałów Zwiadowcy, wyniki filmów Reżysera).
- ✍️ Pisarz – pisze elokwentnie od razu, bez potrzeby poprawiania; prowadzi dziennik książki ORAZ kronikę zespołu (co zrobił każdy agent w tygodniu).
- 🎬 Reżyser – social media ORAZ reżyser zespołu: co tydzień czyta plany i dziennik zespołu i proponuje ulepszenia reguł i planów działania innym agentom (sekcja „Propozycje Reżysera” niżej); Mózg zatwierdza i wpisuje jako rozkazy.

## Wspólne zasady współpracy
- Każdy agent po każdym przebiegu dopisuje JEDNĄ linijkę do reports/dziennik_zespolu.md: `RRRR-MM-DD HH:MM | Agent | co zrobił | wynik/liczby | problem lub „ok”` (git pull --rebase, commit, push).
- Przed pracą: przeczytaj reports/zespol.md, swoje ROZKAZY i ostatnie 20 linijek dziennika zespołu – jeśli inny agent zgłosił coś, co dotyczy Ciebie, uwzględnij to.
- Kontrola wzajemna: Mechanik – sprawność, Analityk – jakość i liczby, Reżyser – plany i reguły, Pisarz – kronika. Uwagi o innym agencie wpisuj w dzienniku zespołu jako „UWAGA DLA <Agent>: …”.
- Hierarchia: szef rozmawia tylko z Mózgiem; Mózg wydaje rozkazy i zatwierdza zmiany. Agent nie zmienia cudzego planu ani kodu botów – proponuje.

## Propozycje Reżysera (dla innych agentów – Mózg zatwierdza)

## Rozkazy dla Pisarza (Pisarz czyta ten plik na początku pracy)
- [ ] P1 (7.11) Strumień 3 z reports/plan_biznes.md: e-book/mini-kurs „Czytanie świec – przeciąganie liny” (metafora szefa z 28.10: świeca = przeciąganie liny, knot = najdalsza wstążka, korpus = gdzie lina stała na gwizdek, doji = remis). Najpierw spis treści (8–10 krótkich lekcji dla początkujących) + lekcja 1, PL, w repo biznes/ebook/. Edukacja, bez obietnic zysku, z dopiskiem „to nie jest porada inwestycyjna”. To JAWNY produkt – osobno od poufnej „Filozofii tradingu”. Odhacz [x] i zapisz postęp w plan_biznes.md.

## Rozkazy dla Analityka (czytaj na początku pracy)
- [ ] A1 (7.11) Rozdzielaj handel szefa na dwa koszyki: PANEL (komentarz pozycji „PanelTG…”, szybkie pewne strzały z Telegrama) i MT5 RĘCZNY (reszta, magic 0). Dla każdego osobno: wejścia, % wygranych, czas do TP (+0,3%), najgłębszy minus po drodze, śr. % na wejście. To czas do zysku i głębokość minusa mierzą przewagę szefa – nie sam % wygranych (test 7.11: bez SL oba kierunki zwykle trafiają TP).
