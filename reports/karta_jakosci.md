# Karta jakości zespołu (📊 Analityk, co sobotę)
Ocena 1–5 = czy praca działa DOBRZE (wynik, jakość, sens), nie czy się uruchomiła. Jedna liczba-dowód, jedna rzecz do poprawy.

## Tydzień 2026-11-14 (8–14.11)
| Agent | Ocena | Liczba-dowód | Jedna rzecz do poprawy |
|---|---|---|---|
| 🔧 Mechanik | 5 | 6 napraw z testem (Z002 suchy test: 2 fantomy → 0, prawdziwe wybicia 2/2; Z008, Z015, Z016, Z018, Z019) + przyczyna Z011 znaleziona w kodzie (hexa_runtime l.273–400); 7 poprawek GOTOWYCH DO WDROŻENIA | Z015 naprawiony w repo, ale nie na żywo – po naprawie strony zawsze sprawdzić produkcję albo od razu „DO RAPORTU: wdróż” |
| 🔍 Inspektor | 5 | 18 nowych zgłoszeń (Z002–Z019), 8 zamkniętych po własnej weryfikacji; 8 INSPEKCJI UPDATE z testem w środku (render 3D, 390 px, procesy, logi); wyłapał niewdrożony Z015 i własny błąd odczytu klatki (14.11 03:50) | harmonogram nadal tylko niedziela (Z014) – BŁĘDY czekały do 29 h; dopilnować „wdróż” Z014 |
| 🎬 Reżyser | 2 | 10 Reeli/raportów + 5 Shorts, ale zasięg Reeli 1–22, skip 50–100%, 0 udostępnień i 0 zapisów w 7 dniach; obserwujący IG 190 → 127 (czyszczenie botów); YT 13 sub., dzienne wyśw. 165 → 7; Short 11.11 przepadł | R23c (15–22 s, 4 sceny) dotrzymane dopiero 14.11 – trzymać w KAŻDYM filmie, potem porównać skip |
| 🔭 Zwiadowca | 2 | 5 przebiegów (100% terminowość), 20 okazji; rozliczone 7: trafność 0%, śr. −0,55 R (2 stopy, 4× brak wejścia, 1 otwarta BTC +1,15 R) | mniej okazji, tylko z wejściem ≤0,5 ATR od ceny (sam to zauważył 12.11) – liczyć R także dla „brak wejścia” osobno |
| 💼 Handlowiec | 4 | lista firm 30 → 40, oferta NL PDF, 5 szkiców; ceny €595/€950 + abonament realne i poniżej rynku (Searchlab: agent AI €2 000–8 000, social €300–2 000/mies.) | 0 wysłanych (decyzja szefa) – przygotować 1 przykład (Reel-demo) dla pierwszej firmy, przesunięty 12.11 |
| 📬 Sekretarz | 4 | 6/6 przebiegów, 14 DO RAPORTU; kosz 7 dni: 46 wątków, ważny Microsoft „kod zabezpieczający” 9.11 (IMPORTANT) w koszu – zbiega się z alertem logowania z USA | wypisywanie nie działa (OneSignal, Unsplash, AlphaX, Metricool wracają co tydzień); nie łączy faktów: 20× „Jotform Luna Social Media Assistant” 8.11 = źródło auto-odpowiedzi „Check your DMs” na IG |
| ✍️ Pisarz | 3 | kronika 8.11 terminowo, rzetelna (liczby z dziennika, plusy i minusy) | P1 e-book otwarty od 7 dni bez startu |
| 📚 Nauczyciel | 1 | 0 wpisów w dzienniku zespołu w tygodniu, LEKCJE agentów bez planu: puste („po 15.11”) | pierwszy przebieg 15.11 – lekcje z liczb tego tygodnia (np. skip 100% przy 5 scenach, Zwiadowca 0/7) |
| 👁 Opiekun IG | 4 | 4 raporty dzienne z liczbami (Windsor/Metricool), poprawił scenę 3D „liczba” i „świece” (klatka 0) | ustalić źródło botów – Jotform Luna (patrz Sekretarz) |
| 🛡 Tarcza | – | nowy 14.11, pierwszy audyt 🟡 (RDP/SMB/WinRM – zapora Contabo już 11.11) | ocena od 21.11 |

Projekty: rozkazy otwarte >7 dni: A1, P1, M5, R6, R8, R9, R10, R11 (R11 wymaga weryfikacji Analityka – brak publikacji), Z2/Z4 (Z4 de facto zrobione przez Z002 – odhaczyć). Cel 30-dniowy Reels (ocena 7.12): zasięg/skip bez poprawy (0%).
Boty (Mechanik, 7 dni): Hexa 12 tr PF 4,89 +199,59 $ | Turbo 4 tr +32,09 $ (stoi od 11.11 – Z011) | Kraken 0 tr (brak przewagi do oceny) | IB Skaner ślepy ~4 dni (Z010) | Indeksy 0 tr | szybki bot IBKR M7 – bez postępu (Gateway).
Pule eToro (kolumna B, zamknięte 8–14.11): Improwizacja 1 tr +370,26 $ | Pula 1k 1 tr +14,45 $ | Sesje 1 tr +15,19 $ | Pula 500 Turbo 7 tr (2 wygr.) −27,66 $ | Pula 500 4 tr (0 wygr.) −138,70 $. Otwarte: Turbo 17, Pula 1k 3, 1 bez puli (puste B) + 1 „nieprzypisana” – do Inspektora.
CISZA: brak dowodu pushu do szefa w tygodniu poza raportami; ryzyko nadal otwarte (Z004 – 8 zadań z push, eToro przegląd tygodnia w niedzielę; Z017 od 1.12).

## Tydzień 2026-11-21 (15–21.11)
| Agent | Ocena | Liczba-dowód | Jedna rzecz do poprawy |
|---|---|---|---|
| 🔍 Inspektor | 5 | 17 nowych zgłoszeń (Z020–Z036), 9 zamkniętych po teście na żywo; wyłapał niewdrożoną stronę (Z027), martwe Indeksy na koncie botów (Z029, 0 zleceń), powrót awarii IBKR (Z032), niezgrane szef_vs_boty (Z035) | Z032 – pierwsza diagnoza (brak autorestartu) poprawiona przez Mechanika; przy usterce wracającej sprawdzać log Gateway przed diagnozą |
| 🔧 Mechanik | 4 | naprawione/zamknięte: Z021, Z023/A1, Z025, Z027, Z031, Z035; 7 poprawek gotowych do „wdróż” (Z020, Z022, Z026, Z029 VOO DCH PF 1,18 obie połowy +, Z033, Z034, Z036) | Z031 – własny skrypt zapchał Market Watch botów na 12 min; diagnostyka na terminalu botów tylko w kopii /portable; karta „szef 39 tr −2 362 $” niezgodna z dziennikiem (33 tr +1 604 €) – uzgodnić okno |
| 🔭 Zwiadowca | 4 | 19 okazji, 10 rozliczonych z R: suma +2,96 R, śr. +0,30 R (tydz. wcześniej −0,55 R); trafność 30 dni 6% → 18%, z trendem od 11.11: 26%, +0,35 R | 8 okazji „brak wejścia” – nadal za daleko od ceny; liczyć wejście ≤0,3 ATR |
| 🎬 Reżyser | 3 | 12 Reeli/raportów IG + Shorts YT terminowo; zasięg 7 dni 404 (Raport 18 20.11 rekord newsowy 84–90), ale obserwujący IG 127 → 122, YT 14 sub., zapisy/udostępnienia 0 w tygodniu | Raport 18:00 2× z rzędu 3 linie nagłówka mimo UWAGI PLAN – max 2 linie, ~25 s |
| 💼 Handlowiec | 4 | lista firm 40 → 50, 2 Reele-przykłady (menu, warsztat), szkice 5 → 9 (biznes/szkice 10 plików) | 0 wysłanych – czeka na KvK i przegląd szefa; przygotować 1 gotową wiadomość z linkiem do przykładu |
| 📬 Sekretarz | 4 | 7/7 przebiegów; wyłapał mail Contabo o incydencie bezpieczeństwa (17.11), logowanie ElevenLabs (16.11), paragon ElevenLabs (18.11); wypisano 3 | wypisywanie: 3 w tygodniu, reklamy wracają (Zapier, InstaForex, alphax, railway); kontrola kosza po mojej stronie – 0 wyników (konektor) |
| ✍️ Pisarz | 4 | kronika 15.11 15:30 terminowo, jawna, oparta na dzienniku | wpis 22.11 – dodać liczby zgłoszeń (nowe/zamknięte) z zgloszenia.md |
| 📚 Nauczyciel | 3 | 15.11: +45 lekcji, 7 narzędzi, trafna lekcja dla Reżysera (kontrast 2 aktywów: skip 50–57% vs 67–100%) | lekcje z tego tygodnia: 0 zapisów/udostępnień – co zmienić w CTA |
| 🧪 Laboratorium | 4 | +13 botów papierowych, 19 tr PF 4,53 +1 149 $ (karta Mechanika); LAB_Donchian_XAG +1 032 $ | M9 (memecoiny, szef 19.11) nie ruszył – prompt tylko M8 (Z034) |
| 🛰 Strażnik | 3 | wykrył offline serwera 15.11 i IB Gateway 15.11/18.11 | push do szefa 7× (15.11 00:40–02:41, 12:41, 13:41; 18.11 06:40) – wbrew CISZY (BŁĄD dla Inspektora) |

Projekty: plan_wzrostu 30 rozkazów otwartych (7 [x]), w tym R6, R8, R9, R10, R11 z 7.11 (14 dni), R12–R29 z 10–13.11 (>7 dni); plan_boty 13 otwartych / 12 zrobionych (48%); plan_hexa_os 5/0; plan_skanery 3/3 (50%). Cel 30-dniowy Reels (ocena 7.12): zasięg +, zapisy/udostępnienia 0 – postęp ~20%.
Boty (Mechanik 21.11, 7 dni, konto botów 5058971085): Hexa 13 tr PF 2,74 +214 $ | Turbo 12 tr PF 4,05 +254 $ | Lab 19 tr PF 4,53 +1 149 $ | Kraken 1 tr −6 $ | IBKR 0 (Gateway stoi od 19.11 05:30 – Z032) | Indeksy 0 (Z029).
Pule eToro (kolumna B, zamknięte 15–21.11): Pula 500 Turbo 1 tr −30,51 $; inne pule 0 zamkniętych. Otwarte: System 1, nieprzypisana 1, „do przypisania” 1 – do Inspektora.
Trading szefa i rynki: trading\analiza_szefa.log, trading\rynki_tydzien.md (serwer).
CISZA: złamana – Strażnik 7 pushy do szefa w tygodniu (alarmy serwera/IB Gateway); eToro przegląd tygodnia 22.11 nadal z push (Z004).
