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


## ✨ RÓJ HEXY – OBOWIĄZUJE WSZYSTKICH (13.11, szef: „czy ilość agentów zgadza się z ilością światełek?”)
Każdy agent i bot ma swoje światełko w `reports/roj_status.json` (aplikacja ORB czyta go co 10 min). Po KAŻDYM przebiegu zaktualizuj swój wpis: `s` = praca / czeka / blad, `ostatnio` = data + jedno zdanie. Nowy agent lub bot = Mózg dopisuje wpis. JSON musi zostać poprawny (`python -m json.tool`). Inspektor co niedzielę sprawdza, czy liczba światełek = liczba działających zadań i botów.


## ➕ NOWY AGENT / BOT / REPO – PROCEDURA (13.11, szef: „przybywa agent → przybywa światełko, zmiana na stronie i odcinek Hexy”)
Za każdym razem, gdy przybywa agent, bot albo nowe repo z GitHuba, w tym samym dniu:
1. ŚWIATEŁKO – Mózg dopisuje wpis do `reports/roj_status.json` (aplikacja ORB pokaże je sama).
2. STRONA /brain/ – karta agenta (co robi, prawdziwie) w sekcji agentów, licznik „N workers” i „N AI agents” = liczba wpisów w roj_status.json; nowe repo → karta w „Built with” z linkiem i znaczkiem gwiazdek (`class="star" data-repo="owner/repo"`). Wdrożenie na Vercel + sprawdzenie na telefonie.
3. ODCINEK HEXY – Reżyser w najbliższym cotygodniowym odcinku (R27/R28): intro → Hexa przedstawia nowego agenta („Meet our new agent: …”), co robi i z jakiego repo jest zbudowany (nazwa projektu na ekranie, link w opisie YT, „link in bio” na IG) → jeśli pasuje, „PREVIOUSLY” z odcinka o agencie, z którym współpracuje.
4. KARUZELA/LICZBY – wszędzie aktualna liczba z roj_status.json, nigdy z pamięci.
5. DZIENNIK – linia „UPDATE: nowy agent/repo <nazwa> – światełko, /brain, odcinek zaplanowany” + fire Inspektora.
Usunięcie agenta = odwrotnie (światełko, karta, licznik), bez odcinka.
WYMIANA NA LEPSZE (repo, skill, narzędzie, agent): wszystko jest połączone – w tym samym dniu usuń stare WSZĘDZIE i wstaw nowe: `reports/skille_zespolu.md` / `reports/narzedzia.md` (stare → „Zastąpione: X przez Y (powód)”), karta i znaczek gwiazdek na /brain/, światełko i opis w roj_status.json, linki w opisach. W najbliższym odcinku Hexa mówi jednym zdaniem, co wymieniliśmy i dlaczego („We replaced X with Y – it does Z better”). Na stronie nigdy nie zostaje coś, czego już nie używamy. Inspektor co niedzielę porównuje: /brain/ ↔ roj_status.json ↔ skille_zespolu.md – każda różnica = zgłoszenie.

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

## 🪙 KRAKEN (szef 9.11.2026: „gęsto tego pilnować i poprawiać”)
- 🔧 Mechanik: rozkaz M6 w plan_boty.md – codzienna karta wyników Kraken (Freqtrade dry-run na serwerze), cotygodniowy backtest i jedna hipoteza poprawy; zmiany tylko po „wdróż”.
- 🔍 Inspektor: codziennie – czy oba procesy freqtrade (Donch4hBTC, Mom1dBTC) żyją na serwerze vmi3737651, świeżość logów, błędy → zgłoszenia.
- 📊 Analityk: w sobotnim raporcie osobna linijka Kraken (wynik tygodnia, PF, czy strategia ma przewagę vs backtest).

## ⚡ SZYBKI BOT IBKR (szef 10.11.2026: „zleć wszystkim agentom”)
- 🔧 Mechanik – prowadzi (rozkaz M7 w plan_boty.md): dane, koszty, backtest, kod w trybie obserwacji; start handlu tylko po „wdróż”.
- 🔭 Zwiadowca – wybór rynków i najlepszych okien godzinowych dla szybkich transakcji (z godziny_rynkow.md), wynik do plan_boty.md „Postęp” jako „Zwiadowca → M7: …”.
- 📊 Analityk – ocena wyników testów (PF, obsunięcie, koszty) w sobotnim raporcie.
- 🔍 Inspektor – po starcie trybu obserwacji: czy proces żyje na serwerze, logi, czy na pewno konto paper.
- 📚 Nauczyciel – co tydzień 1 wzorzec najlepszych praktyk dla szybkich botów (koszty, poślizg, dane w czasie rzeczywistym).

## 🔕 CISZA (szef 8.11.2026 – nadrzędna dla WSZYSTKICH agentów)
Żadnych powiadomień push ani wiadomości do szefa w ciągu tygodnia – ani o sukcesie, ani o błędzie, ani o decyzji. Problemy → „BŁĄD: …” w dzienniku zespołu (dla Inspektora). Sprawy dla szefa (np. „wdróż”, awans, mail czekający na jego ruch) → „DO RAPORTU: …” w dzienniku zespołu. Szef dostaje TYLKO jeden raport tygodnia od 📊 Analityka (sobota 11:17): co się działo między agentami, poprawki, naprawy, 🏆 najlepszy agent. Wyjątek nie dotyczy agentów: raport tradingowy poranny i wieczorny 22:00 zostają.

## 📚 NAUKA (szef 8.11.2026 – „agenci mają się uczyć, z dnia na dzień coraz lepsi”)
- Każdy plan agenta (plan_wzrostu, plan_boty, plan_skanery, plan_biznes) ma sekcję „LEKCJE” – agent czyta ją przed pracą i stosuje. Lekcja = jedna linijka: co działa / co nie działa + liczba-dowód (np. „hook z liczbą w 1. s: skip 48% vs 71% bez liczby”).
- 📚 Nauczyciel (niedziela 16:37) co tydzień: wyciąga z logów i wyników nowe lekcje i dopisuje je do planów; skreśla lekcje obalone przez nowe liczby; max 15 lekcji na plan (najmocniejsze).
- Nowe narzędzia: Nauczyciel sprawdza dostępne już umiejętności i konektory oraz nowe darmowe narzędzia w sieci; co da się użyć od razu – dopisuje do „UMIEJĘTNOŚCI I NARZĘDZIA” danego agenta; co wymaga instalacji/połączenia/płatności – „DO RAPORTU” dla szefa (instaluje i podłącza tylko szef).
- Granica: lekcje zmieniają sposób pracy, nie zasady szefa (demo, bez zmian w botach handlujących bez „wdróż”, cisza, budżet ok. 20 €/mies.).
- Szef 8.11.2026: „szkol ich, by byli jak najlepsi w tym, co im dajesz do roboty”. Nauczyciel szkoli każdego agenta pod JEGO konkretne zadania z planu (nie ogólnie): co tydzień dla każdego 1 wzorzec najlepszej praktyki z sieci (np. jak piszą najlepsze oferty B2B w NL, jak wyglądają topowe produkty na MQL5, jakie okładki e-booków sprzedają) + porównanie z tym, co agent oddał, + 1 konkretna poprawka na następny przebieg. Priorytet do końca listopada: 💼 Handlowiec, 🔧 Mechanik (produkt MQL5), ✍️ Pisarz (e-book), 🎬 Reżyser (okładka, Adobe Stock).

## LEKCJE AGENTÓW BEZ WŁASNEGO PLANU (📚 Nauczyciel dopisuje co tydzień – czytaj swoją część przed pracą)
- 🔍 Inspektor: (pierwsze lekcje po 15.11.2026)
- 📊 Analityk: (pierwsze lekcje po 15.11.2026)
- 📬 Sekretarz: (pierwsze lekcje po 15.11.2026)
- ✍️ Pisarz (tylko kronika zespołu): (pierwsze lekcje po 15.11.2026)

## Wspólne zasady współpracy
- Każdy agent po każdym przebiegu dopisuje JEDNĄ linijkę do reports/dziennik_zespolu.md: `RRRR-MM-DD HH:MM | Agent | co zrobił | wynik/liczby | problem lub „ok”` (git pull --rebase, commit, push).
- Przed pracą: przeczytaj reports/zespol.md, swoje ROZKAZY i ostatnie 20 linijek dziennika zespołu – jeśli inny agent zgłosił coś, co dotyczy Ciebie, uwzględnij to.
- Kontrola wzajemna: Mechanik – sprawność, Analityk – jakość i liczby, Reżyser – plany i reguły, Pisarz – kronika. Uwagi o innym agencie wpisuj w dzienniku zespołu jako „UWAGA DLA <Agent>: …”.
- Hierarchia: szef rozmawia tylko z Mózgiem; Mózg wydaje rozkazy i zatwierdza zmiany. Agent nie zmienia cudzego planu ani kodu botów – proponuje.

## Propozycje Reżysera (dla innych agentów – Mózg zatwierdza)

## Rozkazy dla Pisarza (Pisarz czyta ten plik na początku pracy)
- [ ] P1 (7.11) Strumień 3 z reports/plan_biznes.md: e-book/mini-kurs „Czytanie świec – przeciąganie liny” (metafora szefa z 28.10: świeca = przeciąganie liny, knot = najdalsza wstążka, korpus = gdzie lina stała na gwizdek, doji = remis). Najpierw spis treści (8–10 krótkich lekcji dla początkujących) + lekcja 1, PL, w repo biznes/ebook/. Edukacja, bez obietnic zysku, z dopiskiem „to nie jest porada inwestycyjna”. To JAWNY produkt – osobno od poufnej „Filozofii tradingu”. Odhacz [x] i zapisz postęp w plan_biznes.md.

- [ ] P2 (13.11, szef: „rozdziałów może być otwartych kilka naraz… pisać wszystkie rozdziały naraz, w zależności od tego, w jakim jestem nastroju poprzez rynek”) ROZKAZ STAŁY – „Filozofia tradingu” to KILKA OTWARTYCH ROZDZIAŁÓW naraz, nie po kolei. (1) W `ksiazka\rozdzialy.md` prowadź mapę: rozdział → jego temat/emocja (np. strach, chciwość, cierpliwość, odegranie się, ego, cisza, zaufanie, poznawanie) → lista przypisanych złotych myśli i wątków z dziennika. (2) Każdą nową myśl szefa z `ksiazka\dziennik.md` przypisz do rozdziału, do którego pasuje najlepiej (może do dwóch); nowy temat = nowy otwarty rozdział. (3) Co niedzielę dopisz fragment do tego rozdziału, który pasuje do NASTROJU SZEFA I RYNKU z mijającego tygodnia (odczytaj z dziennika i z tego, jak szło na rynku/demo: spadki → strach/cierpliwość, odbicie → chciwość/pokora, cisza → obecność). Tak każdy rozdział rośnie wtedy, gdy szef naprawdę to przeżywa. Zasady stylu bez zmian: bez wykresów, bez słów technicznych w złotych myślach, filozofia pokazuje, nie doradza.

## Rozkazy dla Analityka (czytaj na początku pracy)
- [ ] A1 (7.11) Rozdzielaj handel szefa na dwa koszyki: PANEL (komentarz pozycji „PanelTG…”, szybkie pewne strzały z Telegrama) i MT5 RĘCZNY (reszta, magic 0). Dla każdego osobno: wejścia, % wygranych, czas do TP (+0,3%), najgłębszy minus po drodze, śr. % na wejście. To czas do zysku i głębokość minusa mierzą przewagę szefa – nie sam % wygranych (test 7.11: bez SL oba kierunki zwykle trafiają TP).

## 🛠️ ZASADA NARZĘDZI (od szefa, 10.11)
- KAŻDY agent korzysta z naszych narzędzi na serwerze: generatory `C:\Hexa\generatory\hexa_gen.py` (obrazy teraz; wideo, głos, usuwanie tła dopisujemy), spis w reports/narzedzia.md.
- Brakuje programu? Agent pisze go sam (Python/PowerShell) w `C:\Hexa\narzedzia\<nazwa>\`, testuje i dopisuje do reports/narzedzia.md. Lepsza wersja istniejącego → zastępuje starą po teście.
- Granice bez zmian: boty handlowe tylko po „wdróż”, zero realnych pieniędzy, klucze wpisuje szef sam przez stronkę „Klucz dla Hexy” do `C:\Hexa\sejf\`, niczego nie kasujemy bez zgody.
- Szef chce WIDZIEĆ efekty: co tydzień w sobotnim raporcie 1–3 najlepsze rzeczy zrobione nowymi narzędziami (obraz/wideo/okładka) z linkiem; YouTube @erl.grey83 i Instagram mają się stale poprawiać (miniatury, krótkie wideo, lektor) — Reżyser prowadzi, reszta pomaga.

## 👁️ OBSERWACJA DO PORANNEGO BRIEFINGU (szef 13.11.2026)
- Jensen Huang (były CEO NVIDIA, zrezygnował 12.11.2026): jeśli pojawi się OFICJALNA informacja o jego nowej roli (np. zarząd/zespół przy Terafabie Elona Muska albo inna firma) – wrzucić do porannego briefingu w sekcji „RYNEK – WAŻNE”, z linkiem do źródła. Przeczucie szefa: Huang trafi do zespołu przy Terafabie. Podawać TYLKO potwierdzone fakty, nigdy plotki.
- NVIDIA wyniki 17.11.2026 – w briefingu 18.11 krótko: przychód, prognoza, reakcja kursu (fakty, bez prognoz, not financial advice).

## Podręcznik marketingowy (13.11.2026)
- Reżyser i Handlowiec przed planowaniem treści czytają C:\Hexa\wiedza\marketing (5 ról z agency-agents, MIT): Instagram Curator, Carousel Growth Engine, Content Creator, Growth Hacker, Social Media Strategist + README z naszymi zasadami.
- Do tego umiejętności content-skills (viral-hooks, viral-instagram-reels, viral-captions-and-ctas…).
- Bez nowych kluczy API i bez zewnętrznej autopublikacji. Żadnych „growth hacków” łamiących zasady Instagrama.

## 🛡️ NOWY AGENT: Tarcza (bezpieczeństwo) — szef: „wdrożyć natychmiast” (14.11.2026, 01:17)
- Rola: kontrola bezpieczeństwa całej firmy, część Hexy. Sprawdza KAŻDĄ próbę logowania i wszystko poniżej. Sam nie zmienia ustawień systemu/zabezpieczeń — poprawki po „tak” szefa, robione razem z szefem.
- Co niedzielę + na bieżąco: serwer (otwarte porty, nieudane logowania, aktualizacje, zapora, konta, urządzenia w Tailscale), telefon (adb tylko przez Tailscale, nieznane aplikacje), repo (skan sekretów), pliki z tokenami, kopie zapasowe, boty (tylko demo, magic 0 nietykalne), 2FA na kontach.
- Raport: 🟢/🟡/🔴 w tygodniowym raporcie zespołu; 🔴 pilne → od razu wiadomość do szefa na Telegram (zgoda szefa 14.11).
- TOŻSAMOŚĆ SZEFA (Hexa + Tarcza): ważne polecenia (handel, usuwanie, ustawienia, przelewy) tylko po potwierdzeniu, że to szef:
  1) teraz: odcisk palca / twarz przez systemowe BiometricPrompt Androida w ORB (dane biometryczne zostają w telefonie, nie wychodzą na serwer);
  2) później: głos szefa (z nagrań testu głosu) jako druga warstwa;
  3) w przyszłości: tęczówka — jeśli telefon/urządzenie będzie to wspierać.
  Rozmawiać Hexa może z każdym; wykonywać polecenia — tylko dla szefa.
- PIERWSZY AUDYT 14.11 (odczyt): 🟡 RDP 3389 otwarty na internet → przenieść na sam Tailscale · 🟡 nasłuch 445 (SMB) i 5985/5986 (WinRM) → sprawdzić zaporę · 🟡 brak logów nieudanych logowań (audyt prawdopodobnie wyłączony) → włączyć · 🟢 zapora włączona.
- Do zrobienia razem z szefem (dziś przy serwerze): włączenie audytu logowań, RDP tylko przez Tailscale, przegląd reguł zapory.
