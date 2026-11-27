# BUDŻET ELEVENLABS – plan Creator (~121 000 kredytów / miesiąc) – Mózg 12.11.2026
Szef 12.11: „rozłóż tak kredyty ElevenLabs, żeby wystarczyło na cały miesiąc, i niech agenci z tego korzystają, tworząc jak najlepsze grafiki na YouTube i Insta”.
Konektor: ElevenLabs-619b9b4c (mcp__ElevenLabs-619b9b4c__*). Konto wspólne z głosem Hexy na telefonie.


## ⛔ KONIEC ELEVENLABS – ZAPAS ODCINKÓW (szef 26.11.2026 14:49) – OBOWIĄZUJE PRZED WSZYSTKIM PONIŻEJ
Szef: „Resztę kredytów ElevenLabs wykorzystaj do stworzenia jak największej ilości serialu Hexy” – rezygnujemy z ElevenLabs (oszczędzamy).
- Stan 26.11 14:50: plan Pro, zostało ok. 231 000 kr., ważne do odnowienia 18.12.2026 12:50 UTC. Po tej dacie ElevenLabs NIE istnieje w naszym systemie.
- Limit 60 000/odcinek i rezerwa 150 000 z pkt 7 – UCHYLONE. Nowa zasada: zostaw tylko 10 000 kr. rezerwy (głos Hexy w telefonie do czasu przełączenia na darmowy), resztę zużyj na odcinki.
- Kolejność: #2 Szklane Miasto (28.11), #3 Archiwum Mgieł (5.12), #4 Miraż (12.12), #5 Planeta Zegarów (19.12), #6 Kuźnia (26.12), #7 Lustrzany Księżyc (2.01) – rób po kolei, aż skończą się kredyty. Jakość wg R40 i pkt 6 bez obniżania; jeśli kredyty na ostatni odcinek nie starczą na całość, zrób jego najdroższe ujęcia (Hexa mówi – OmniHuman, boss, planeta), a resztę dokończ darmowo.
- Zawsze estimate_only przed wideo; po każdej generacji wpis do reports/elevenlabs_budzet.md (Zużycie).
- Gotowe odcinki: tools/hexa_seria/epN/ (final.mp4 + kontrola.md + opis IG). Publikacja bez zmian: sobota 21:00, TYLKO Instagram.
- Rytuał (ep2/rytual.mp4) i intro nagrane raz – używaj ponownie, nie generuj drugi raz.
- Głos Hexy po 18.12 = darmowy (edge-tts, próbki: marka/propozycje/glos_hexy_20261126/, wybór szefa w toku) – NIE generuj nic w ElevenLabs po 18.12.

## Podział na miesiąc
| Pula | Kredyty / mies. | Limit / tydzień | Kto | Na co |
|---|---|---|---|---|
| Głos Hexy (telefon) | 25 000 | – | Hexa | rozmowy z szefem (Pola, eleven_v4) – NIE RUSZAĆ |
| Lektor Reels/Raport/Shorts | 15 000 | 3 800 | 🎬 Reżyser | lektor EN do Reela 10:00 i Raportu 18:00 (Short YT używa tego samego audio) |
| Lektor Weekly (niedziela) | 18 000 | 4 500 | 🎬 Reżyser | ~5 min przeglądu tygodnia |
| Obrazy (tła GŁĘBIA, miniatury, okładki) | 25 000 | 6 000 | 🎬 Reżyser, Handlowiec, Pisarz | tylko „hero”: miniatura YT, okładka Weekly, tło sceny 1 (hook). Resztę teł nadal Canva/HF (darmowe) |
| Wideo (klip ruchomy) | 14 000 | 1 klip / miesiąc | 🎬 Reżyser | jeden 5 s klip-otwieracz do Weekly w 1. niedzielę miesiąca (seedance ~14k) – albo tańszy model, jeśli jakość ta sama |
| Rezerwa | 24 000 | – | Mózg | awarie, poprawki, ważny news |

**Bieżący cykl (do odnowienia planu):** ~60 000 kredytów już zużyte 12.11 (budowa twarzy Hexy). Do odnowienia: limity tygodniowe ×0,5, wideo = 0.

## HEXA W FILMACH (szef 13.11: „wdrażamy”) – ok. 12–14 tys./mies.
- INTRO HEXY (zrobione 13.11): `site/assets/hexa_intro.mp4` (+ wersja pionowa `hexa_intro_9x16.mp4`) – ~6 s, usta zgrane, „Hi, I'm Hexa – the voice of Erl.grey83. Pure information, no noise. Let's begin.” Otwiera KAŻDY cotygodniowy film Hexy i film na /brain/. NIE generować ponownie.
- Treść tygodnia: głos Hexy (Pola `lqJpYZ185uAhVny7fXot`, eleven_v4, ~1 kr./znak) nad nowymi grafikami/3D – 500–1000 kr. na film, z puli Lektor.
- Raz w miesiącu nowy fragment z ruchem ust (creatify-aurora ~1 000 kr./s, max 10 s) – z puli Wideo zamiast klipu seedance.

## Zasady
1. Przed użyciem przeczytaj tabelę „Zużycie” i policz sumę tygodnia (pon–nd) w swojej puli. Limit przekroczony → wróć do darmowych (piper, Canva, HF hexa_gen.py) i nic nie generuj w ElevenLabs.
2. Po każdej generacji dopisz wiersz do „Zużycie” (data, agent, pula, co, model, ~kredyty). Lektor: kredyty ≈ liczba znaków tekstu (multilingual v2 / v3), flash ≈ połowa.
3. Jedna generacja na rzecz (generations_count=1 dla lektora, 2 dla obrazu). Nigdy nie ponawiaj tej samej generacji – płaci się drugi raz. Najpierw sprawdź tekst skillem no-ai-slop i liczby (Analityk), dopiero potem generuj.
4. Lektor (szef 24.11.2026): JEDEN STAŁY GŁOS we wszystkich filmach – darmowy piper `en_US-hfc_male-medium` (głos nr 6 z próbek `marka/glosy/`). NIE generuj lektora w ElevenLabs, nie wpisuj pola `"glos"` w scenes.json (KINO je ignoruje). Pula „Lektor” wolna na inne cele.
5. Obrazy ElevenLabs: prompt GŁĘBIA z R17 + kolory marki R21, bez ludzi, bez tekstu; 9:16 dla Reels, 16:9 dla miniatur. Najpierw `creative_get_model_guide` dla modelu.
6. Raz w tygodniu (niedziela) Analityk sumuje zużycie w dzienniku zespołu: „ElevenLabs: X / limit” – bez powiadomień do szefa.

## Zużycie
| Data | Agent | Pula | Co | Model | ~Kredyty |
|---|---|---|---|---|---|
| 2026-11-12 | Mózg | Hexa | twarz Hexy (wideo seedance ×4) + test głosów | seedance-v2.5 / eleven_v4 | ~60 000 |
| 2026-11-12 | Mózg | Rezerwa | tła wzoru raportów 22:00 i briefingu 8:00 (4 obrazy) | seedream-5-pro | ~3 300 |
| 2026-11-13 | Mózg | Obrazy | próbka slajdu karuzeli z Hexą (referencja) | gemini-3-pro-image | ~1 830 |
| 2026-11-13 | Mózg | Lektor | próbka głosu Hexy (Pola, EN, 10 s) do filmu /brain | eleven_v4 | ~150 |
| 2026-11-13 | Mózg | Wideo | INTRO HEXY (głos 104 + Aurora lip-sync ~6 790) – jednorazowe, wielokrotnego użytku | eleven_v4 + creatify-aurora | ~6 900 |
| 2026-11-15 | Reżyser (Raport 18) | Lektor | lektor Raportu 18:00 (5 scen, Patrick) | eleven_multilingual_v2 | ~535 |
| 2026-11-16 | Reżyser (Reel 10:00) | Lektor | lektor Reela CLAIM CHECK (4 sceny, Patrick) | eleven_multilingual_v2 | ~277 |
| 2026-11-16 | Mózg (dla szefa) | Obrazy | szkic koncepcyjny Rytuału nowej mocy – Przygody Hexy (2 warianty, ref. Hexa_cala) | gemini-3-pro-image | ~3 654 |
| 2026-11-16 | Reżyser (Raport 18) | Lektor | lektor Raportu 18:00 (5 scen, Patrick) | eleven_multilingual_v2 | ~375 |
| 2026-11-17 | Reżyser (Reel 10:00) | Lektor | lektor Reela CRYPTO 101 Fear & Greed (4 sceny, Patrick) | eleven_multilingual_v2 | ~325 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #2 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #3 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #4 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #5 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #6 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #7 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #8 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #9 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #10 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Wideo | Przygody Hexy #11 – 3 ujęcia Veo (8 s, 9:16) | veo-3.1-fast | ~21 800 |
| 2026-11-27 | Mózg | Stan | po serii #2–#11 zostało 9 778 kredytów (rezerwa na głos Hexy w telefonie do 18.12) | – | – |
