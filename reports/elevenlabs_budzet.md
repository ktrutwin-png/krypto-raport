# BUDŻET ELEVENLABS – plan Creator (~121 000 kredytów / miesiąc) – Mózg 12.11.2026
Szef 12.11: „rozłóż tak kredyty ElevenLabs, żeby wystarczyło na cały miesiąc, i niech agenci z tego korzystają, tworząc jak najlepsze grafiki na YouTube i Insta”.
Konektor: ElevenLabs-619b9b4c (mcp__ElevenLabs-619b9b4c__*). Konto wspólne z głosem Hexy na telefonie.

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

## Zasady
1. Przed użyciem przeczytaj tabelę „Zużycie” i policz sumę tygodnia (pon–nd) w swojej puli. Limit przekroczony → wróć do darmowych (piper, Canva, HF hexa_gen.py) i nic nie generuj w ElevenLabs.
2. Po każdej generacji dopisz wiersz do „Zużycie” (data, agent, pula, co, model, ~kredyty). Lektor: kredyty ≈ liczba znaków tekstu (multilingual v2 / v3), flash ≈ połowa.
3. Jedna generacja na rzecz (generations_count=1 dla lektora, 2 dla obrazu). Nigdy nie ponawiaj tej samej generacji – płaci się drugi raz. Najpierw sprawdź tekst skillem no-ai-slop i liczby (Analityk), dopiero potem generuj.
4. Lektor: głos „Patrick International Narration” `9Ft9sm9dzvprPILZmLJl` (głęboki, spokojny, dokumentalny – „przyciąga, nie krzyczy”, R19); zapas: „Ken Franson” `kJKMPwrIKzwVkMKOfRtr`. Jeden głos na stałe = rozpoznawalność marki. Pobierz plik audio na serwer i wpisz ścieżkę w polu `"glos"` sceny w scenes.json (KINO od 12.11 używa go zamiast piper; puste `glos` = piper jak dotąd). Jeden plik na scenę albo jedno nagranie pocięte ffmpeg na sceny.
5. Obrazy ElevenLabs: prompt GŁĘBIA z R17 + kolory marki R21, bez ludzi, bez tekstu; 9:16 dla Reels, 16:9 dla miniatur. Najpierw `creative_get_model_guide` dla modelu.
6. Raz w tygodniu (niedziela) Analityk sumuje zużycie w dzienniku zespołu: „ElevenLabs: X / limit” – bez powiadomień do szefa.

## Zużycie
| Data | Agent | Pula | Co | Model | ~Kredyty |
|---|---|---|---|---|---|
| 2026-11-12 | Mózg | Hexa | twarz Hexy (wideo seedance ×4) + test głosów | seedance-v2.5 / eleven_v4 | ~60 000 |
| 2026-11-12 | Mózg | Rezerwa | tła wzoru raportów 22:00 i briefingu 8:00 (4 obrazy) | seedream-5-pro | ~3 300 |
