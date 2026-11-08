# Zespół agentów szefa (od 7.11.2026)
Szef rozmawia TYLKO z Claude („mózg”). Claude prowadzi agentów, uczy ich, sprawdza wyniki i odpowiada za całość.

| Agent | Dział | Plan | Co robi |
|---|---|---|---|
| 🎬 Reżyser | Social Media (Instagram + YouTube @erl.grey83) | reports/plan_wzrostu.md | filmy i Reels wg planu wzrostu, Weekly Market Brief, wyniki zasięgów |
| 📊 Analityk | Trading szefa (MT5, Panel Szefa, dziennik głosowy, wyzwanie 5 000 € → 1 000 000 €) | reports/plan_boty.md (Bot Szefa) | sobotnia analiza handlu szefa, reguły (3 świece, knoty, dolar), tempo wyzwania |
| 🔍 Inspektor | Kontrola CAŁEJ maszyny (MT5, eToro, IBKR, Kraken, wszyscy agenci) | reports/zgloszenia.md | codziennie przyjmuje zgłoszenia, sprawdza w środku, diagnozuje, przekazuje Mechanikowi, sprawdza naprawę |
| 🔧 Mechanik | Naprawy + boty (Hexa, Turbo, Kraken, eToro, IB) | reports/plan_boty.md, reports/zgloszenia.md | naprawia zgłoszenia Inspektora, zdrowie i wyniki botów, testy ulepszeń |
| 🔭 Zwiadowca | Skanery (sygnały, rynki) | reports/plan_skanery.md | jakość sygnałów, wyniki w R, filtry, nowe rynki |
| ✍️ Pisarz | Książka „Filozofia tradingu” | laptop ksiazka\\rozdzialy.md (zasady stylu) | co niedzielę 15:23 wpis do dziennika + jeden rozdział, po cichu, pokaz po roku |
| 💼 Handlowiec | Biznes – usługi AI dla firm, sprzedaż produktów | reports/plan_biznes.md | oferty, cenniki, lista firm, szkice wiadomości – wysyła szef |
| 📚 Nauczyciel | Nauka zespołu | sekcje LEKCJE w planach | co niedzielę 16:37: lekcje z wyników, nowe umiejętności i narzędzia dla agentów |
| 📐 Projektant | (później) projekt wózka dziecięcego | – | uruchamiany, gdy szef zacznie projekt |

Zasady wspólne: konta demo/paper, nic nie zmieniają bez zgody szefa, uruchamia szef, przegląd miesięczny 7.12.2026.

## Jak dowodzi Mózg
- Rozkazy: sekcja „ROZKAZY OD MÓZGU” na górze planu każdego agenta (plan_wzrostu, plan_boty, plan_skanery). Agent czyta je najpierw, wykonuje, odhacza [x] i zapisuje dowód w „Postęp”.
- Umiejętności: sekcja „UMIEJĘTNOŚCI I NARZĘDZIA” w tym samym planie. Brakuje narzędzia → agent pisze „PROŚBA DO MÓZGU”, Mózg podpina.
- Kontrola: Mózg sprawdza odhaczone rozkazy i dowody przy każdej rozmowie z szefem o agentach i w przeglądzie 7.12.

## Role rozszerzone (szef 7.11.2026: „z dnia na dzień agenci mają być lepsi… mają współpracować, sprawdzać siebie nawzajem, ale działać też na zewnątrz każdy w swojej dziedzinie”)
- 🔍 Inspektor i 🔧 Mechanik – RÓWNORZĘDNI (szef 8.11.2026). Inspektor wykrywa i diagnozuje (także u Mechanika), Mechanik naprawia (także Inspektora).

## OBIEG BŁĘDÓW (szef 8.11.2026 – obowiązuje WSZYSTKICH agentów)
1. Agent prowadzi swoją platformę/dział. Gdy coś nie działa (błąd, brak danych, proces nie żyje, zlecenie odrzucone, zadanie się wysypało) – NIE naprawia sam, tylko dopisuje do reports/dziennik_zespolu.md linijkę z problemem zaczynającym się od `BŁĄD:` (platforma, co, kiedy, komunikat błędu).
2. 🔍 Inspektor (codziennie 19:13) zbiera błędy z dziennika zespołu i ze stanu zadań, wchodzi do środka (logi, procesy, pliki, konto), ustala przyczynę i zakłada zgłoszenie w reports/zgloszenia.md (status „dla Mechanika”).
3. 🔧 Mechanik (codziennie 04:41) bierze zgłoszenia „dla Mechanika”, naprawia (w swoich granicach) i ustawia status „naprawione – do sprawdzenia” albo „czeka na wdróż szefa”.
4. 🔍 Inspektor sprawdza naprawę: działa → „zamknięte”; nie działa → z powrotem „dla Mechanika” z opisem.
5. Granice Mechanika: sam naprawia skrypty i pliki, które NIE składają zleceń (raporty, dzienniki, skanery sygnałów, backtest, logi, panel bez handlu – zawsze z kopią .bak przed zmianą). Kod/konfiguracja botów handlujących (Hexa, Turbo, Freqtrade, IB Skaner, zadania eToro), restart procesów, pozycje, konta i zadania harmonogramu – tylko „GOTOWY DO WDROŻENIA” → Mózg wdraża po „wdróż” szefa. Naprawa = sprawność, nie gwarancja zysku.
- 🔭 Zwiadowca – skanuje WSZYSTKIE rynki (złoto, srebro, indeksy, forex, akcje, krypto); szuka najlepszych okazji na dany termin (dzień / tydzień / miesiąc) z oceną pewności; tylko informacja, decyzję podejmuje szef.
- 📊 Analityk – największe ruchy walut i rynków na świecie (co, o ile, dlaczego, co dalej), najmniejsze szczegóły; oraz (szef 8.11) KONTROLA JAKOŚCI WSZYSTKICH agentów i projektów raz w tygodniu (sobota): Reżyser, Zwiadowca, Mechanik, Inspektor, Handlowiec, Sekretarz, Pisarz (tylko regularność i kronika, nie książka), plany i pule. Inspektor = czy działa; Analityk = czy działa dobrze. Karta: reports/karta_jakosci.md.
- ✍️ Pisarz – pisze elokwentnie od razu, bez potrzeby poprawiania; prowadzi dziennik książki ORAZ kronikę zespołu (co zrobił każdy agent w tygodniu).
- 🎬 Reżyser – social media ORAZ reżyser zespołu: co tydzień czyta plany i dziennik zespołu i proponuje ulepszenia reguł i planów działania innym agentom (sekcja „Propozycje Reżysera” niżej); Mózg zatwierdza i wpisuje jako rozkazy.

## 🔕 CISZA (szef 8.11.2026 – nadrzędna dla WSZYSTKICH agentów)
Żadnych powiadomień push ani wiadomości do szefa w ciągu tygodnia – ani o sukcesie, ani o błędzie, ani o decyzji. Problemy → „BŁĄD: …” w dzienniku zespołu (dla Inspektora). Sprawy dla szefa (np. „wdróż”, awans, mail czekający na jego ruch) → „DO RAPORTU: …” w dzienniku zespołu. Szef dostaje TYLKO jeden raport tygodnia od 📊 Analityka (sobota 11:17): co się działo między agentami, poprawki, naprawy, 🏆 najlepszy agent. Wyjątek nie dotyczy agentów: raport tradingowy poranny i wieczorny 22:00 zostają.

## 📚 NAUKA (szef 8.11.2026 – „agenci mają się uczyć, z dnia na dzień coraz lepsi”)
- Każdy plan agenta (plan_wzrostu, plan_boty, plan_skanery, plan_biznes) ma sekcję „LEKCJE” – agent czyta ją przed pracą i stosuje. Lekcja = jedna linijka: co działa / co nie działa + liczba-dowód (np. „hook z liczbą w 1. s: skip 48% vs 71% bez liczby”).
- 📚 Nauczyciel (niedziela 16:37) co tydzień: wyciąga z logów i wyników nowe lekcje i dopisuje je do planów; skreśla lekcje obalone przez nowe liczby; max 15 lekcji na plan (najmocniejsze).
- Nowe narzędzia: Nauczyciel sprawdza dostępne już umiejętności i konektory oraz nowe darmowe narzędzia w sieci; co da się użyć od razu – dopisuje do „UMIEJĘTNOŚCI I NARZĘDZIA” danego agenta; co wymaga instalacji/połączenia/płatności – „DO RAPORTU” dla szefa (instaluje i podłącza tylko szef).
- Granica: lekcje zmieniają sposób pracy, nie zasady szefa (demo, bez zmian w botach handlujących bez „wdróż”, cisza, budżet ok. 20 €/mies.).

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
