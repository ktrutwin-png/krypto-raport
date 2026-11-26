# Daily Reel pipeline (erl.grey83)


## 🎙️ NOWY LEKTOR = ANDREW (szef 26.11.2026 15:01) – zastępuje piper hfc_male („nie podoba mi się”)
JEDEN lektor we WSZYSTKICH Reelach, Raporcie 18:00, Weekly i karuzelach: darmowy edge-tts `en-US-AndrewNeural` (naturalny męski głos), przez `tools/reel/lektor.py`.
- Użycie zamiast piper:  `"<say>" | python tools\reel\lektor.py -f <plik.wav>`  (WAV 22 050 Hz jak piper, reszta potoku bez zmian). Na serwerze działa; kino.py i raport/video.py same używają lektora.
- piper hfc_male zostaje TYLKO jako zapas, gdy lektor.py zwróci kod 3 (brak sieci do edge-tts) – wtedy wpis do reports/zgloszenia.md.
- Lektor generuj NA SERWERZE (chmura agenta nie łączy się z edge-tts). Wyjątek: serial Hexy – mówi Hexa głosem Sonia.

## ⛔ TYLKO INSTAGRAM (szef 25.11.2026 22:14) – OBOWIĄZUJE PRZED WSZYSTKIM PONIŻEJ
Szef: „na razie YouTube odpuszczamy, X i Facebook też – zostajemy na Instagramie; najpierw budujemy firmę, potem wydatki”. Od teraz publikujesz WYŁĄCZNIE na Instagramie (Windsor, konto erl.grey83, plan darmowy). NIE wysyłaj nic na YouTube (ani Windsor, ani Metricool), na X (Typefully) ani na Facebook. Nie kupujemy Windsor Basic. Brak YT/X w dzienniku to NIE błąd – nie zgłaszaj. Wszystkie wpisy o YT/X/FB poniżej są zawieszone, dopóki szef sam ich nie przywróci.


Template for the 15:00 (Europe/Amsterdam) daily Reel and the Sunday 22:00 weekly summary Reel.
Copy this folder to a scratchpad, then:

1. Edit `reel.html`: scenes sc1..sc6 (hook with big number + 7-day BTC chart from `prices.js`, why/cause scene, drivers, funds, levels + key dates, CTA question). Keep all on-screen text in English, nick @erl.grey83, footer "For information only, not investment advice."
   Replace `PX` in `prices.js` with fresh 7-day BTC prices (CoinGecko get-coin-market-chart, id=bitcoin, days=7).
2. Edit `segs` in `vo.py` - narration explains WHY it happened (do not read the slide text), only facts from >=2 sources, hedge causes ("analysts point to"). Voice: piper en_US-hfc_male-medium (THE ONE fixed brand voice since 24.11.2026). Download once:
   `curl -L -o voice/en_US-hfc_male-medium.onnx https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/hfc_male/medium/en_US-hfc_male-medium.onnx` (+ `.onnx.json`). Needs `pip install --break-system-packages piper-tts` and `export no_proxy= NO_PROXY=` for pip/curl.
3. `python3 vo.py` -> timing.json + voice.m4a. `python3 music.py <T> <nastroj>` -> melody.wav (oryginalny podklad synthwave; nastroj: calm / tense / uplift / gold - dobierz do tematu, opis w music.py), then `ffmpeg -i melody.wav -af "lowpass=f=3500,aecho=0.8:0.55:380|760:0.3|0.2" melody_fx.wav` (dla tense: `lowpass=f=6000,aecho=0.8:0.6:310|690:0.35|0.25`; dla uplift: `highpass=f=70,aecho=0.8:0.75:140|290|560|1100:0.38|0.3|0.22|0.15`). Szef 5.11.2026: tense = HORROR (drastyczna muzyka przy spadkach/krachu), uplift = NIEBO (anielski chór przy wzrostach) - patrz special.py.
4. Frames: run 4 in parallel `python3 frames.py <i> 4` (i=0..3) -> f/%05d.jpg (30 fps, 1080x1920).
5. Mix (music ducked under voice, loudnorm) and mux:
   `ffmpeg -i melody_fx.wav -i voice.m4a -filter_complex "[0]aresample=44100,aformat=channel_layouts=stereo,volume=0.55[m];[1]aresample=44100,aformat=channel_layouts=stereo,equalizer=f=140:t=q:w=1:g=3,asplit[v1][v2];[m][v1]sidechaincompress=threshold=0.015:ratio=5:attack=30:release=600:makeup=1[duck];[duck][v2]amix=inputs=2:normalize=0:weights=1 1.2,loudnorm=I=-15:TP=-1.5:LRA=7[out]" -map "[out]" -ar 44100 -c:a aac -b:a 160k mix.m4a`
   `ffmpeg -framerate 30 -i f/%05d.jpg -i mix.m4a -shortest -c:v libx264 -pix_fmt yuv420p -crf 21 -movflags +faststart reel.mp4`
6. Cover = a frame around 5-6 s (jpg). Push mp4 + cover + caption.txt to `reports/YYYY-MM-DD-reel/`, publish with Windsor `create_video_post` (raw GitHub URLs, share_to_feed true).
Caption: hook first line, 3 facts, a question for comments, "Follow @erl.grey83", disclaimer, 5-8 hashtags.

## ⭐ NOWY FORMAT „KARUZELA GRA” – TEST od śr. 25.11.2026 (Reel 10:00; szef zatwierdził 24.11)
**OBOWIĄZKOWO (Mózg 25.11): od czw. 26.11 do 9.12 KAŻDY Reel 10:00 pon–sob = Karuzela gra. Filar dnia idzie na Raport 18:00. 25.11 Reel wyszedł w starym formacie – błąd, nie powtarzać.**

## 🎙️ GŁOS – ZASADA STAŁA (szef 25.11, „pamiętaj”)
JEDEN lektor we WSZYSTKICH Reelach, Shortach, Raporcie 18:00, Weekly i karuzelach: piper en_US-hfc_male-medium. Jedyny wyjątek: seria „Przygody Hexy” – tam mówi Hexa swoim głosem. Godziny publikacji stałe (Reel 10:00, Raport 18:00, Weekly niedziela, Hexa sobota 21:00) – film MA wyjść codziennie o tej godzinie.

## ⚠️ WYSYŁKA YOUTUBE (Mózg 25.11)
Metricool FREE wyczerpał limit miesiąca (od 24.11 każdy YT = ERROR „account limit”). Od teraz YouTube wysyłasz przez Windsor: connector `youtube`, akcja `upload_video` (video_url = raw URL mp4 z GitHuba, title ≤100 znaków z #shorts, description, tags, category_id 25 News, made_for_kids false, privacy_status public). Metricool tylko gdy Windsor nie ma konta youtube. PO KAŻDEJ wysyłce sprawdź prawdziwy status (Windsor zwraca video id / Metricool getScheduledPosts → providers.status). W dzienniku „YT ok” wolno wpisać TYLKO z video id; inaczej „BŁĄD: YT …”.
Wzór gotowy: marka/propozycje/karuzela_2411/ (config.json, podglad.jpg, reel/). 6 kart = złoto, BTC, ETH, XRP, XLM, XDC; każda karta = INNA postać w INNYM miejscu (styl półrealistyczny jak nowoczesna gra, tropikalne neonowe miasto), emocja i pogoda wg ruchu 24h; BEZ monet w scenie, BEZ nagości, bez nazw/logo GTA.
1. Dane: CoinGecko get-coin-markets ids pax-gold,bitcoin,ethereum,ripple,stellar,xdce-crowd-sale → cena + 24h %. Kolejność kart: od największego wzrostu do największego spadku.
2. Nastrój: ≤−4% burza/ulewa/rozpacz (sila 1.0, piorun true) · −4…−1% pochmurno/nerwy (sila 0.4) · −1…+1% spokój (sila 0) · +1…+4% słońce, plaża/drink (sila 0) · ≥+4% złote światło, jacht/zakupy/fura, na bogato (sila 0).
3. Sceny: unikaj postaci i miejsc z reports/sceny_karuzeli.json z ostatnich 14 dni. Prompt: "Cinematic semi-realistic AAA open-world video game render, tropical Miami-like neon city, highly detailed, depth of field, no text, no letters, no logos, no signs with writing. <postać, miejsce, emocja, pogoda>". Generuj na SERWERZE (Remote_Desktop_Commander, deviceId 0b708a8f-66a5-4eeb-8a28-ac5878aae932): `python C:\Hexa\generatory\flux_gen.py "<prompt>" C:\Hexa\krypto-raport\marka\propozycje\karuzela_RRRRMMDD\s_<kod>.jpg` (darmowy FLUX, ~3 s), potem na serwerze `git stash; git pull; git add …; git commit; git push; git stash pop` i pull tutaj. Obejrzyj każdą scenę (Read); zła → nowy prompt. x0 = lewa krawędź kadru 824 px wokół postaci (0–200).
4. Powód ruchu: WebSearch (≥2 źródła dla złota/BTC/ETH; mała moneta bez newsa → uczciwie „follows the market”). Dla każdej karty: say (EN, 20–30 słów, „analysts point to”) i cap (≤8 słów; NIE jest pokazywany na wideo – szef 24.11: bez podpisu na dole, wystarczy lektor). Bez obietnic, bez porad.
5. config.json w folderze dnia – format jak karuzela_2411/config.json (k, pc, cena, haslo, scena, x0, sila, piorun, say, cap).
6. Lektor na serwerze (JEDEN stały głos): dla każdej karty `"<say>" | python tools\reel\lektor.py -f marka\propozycje\karuzela_RRRRMMDD\reel\vN.wav` (N = numer karty), push, pull.
7. Render tutaj: `python3 tools/monety/karuzela.py <config>` (karty + podglad.jpg) → `python3 tools/monety/reel_karuzela.py <config>` → `python3 tools/monety/audio_reel.py <config> tense|calm|uplift` (tense gdy większość spada, uplift gdy rośnie) → reel/reel.mp4 (~55 s, Ken Burns, deszcz, pioruny, żółty pasek z adresem strony; bez podpisów na dole).
8. Obejrzyj min. 6 klatek. Publikacja jak zwykle (Reel IG + Short YT): opis = hak, po jednej linijce na aktywo, „Live prices → link in bio”, disclaimer, hashtagi; na YouTube w opisie pełny link https://erlgrey83-crypto-freaq.vercel.app (klikalny).
9. Dopisz dzień i sceny do reports/sceny_karuzeli.json; jedna linia w reports/dziennik_zespolu.md.
10. Gdy coś padnie i nie da się naprawić do 10:30 → zwykły Reel jak niżej + „BŁĄD:” w dzienniku. Test A/B prowadzi Laboratorium treści (wyświetlenia, czas oglądania vs zwykły Reel).

## Styl CYBERPUNK (od 5.11.2026)
Tlo `bg()` ma neonowe miasto (cyjan #00f0ff + roz #ff2bd6 + zolte okna), rozowa linie horyzontu i siatke. Karty sa ciemne (min. 82% krycia), zeby tekst byl czytelny.
Zasady wzrostu z zadania 12:00 (hook w 1 s, 20-35 s, filar dnia) maja pierwszenstwo przed czasami scen w tym README.

> 25.11.2026: opis posta (IG/YT/X) i teksty lektora przepuść przez skill `humanizer` przed publikacją.
## ZASADY Z DANYCH (Laboratorium tresci, 22.11.2026) – maja pierwszenstwo przed gustem
Metricool, 54 Reelsy 23.10–22.11: srednio 83% widzow odpada w pierwszych 3 s; newsy "price today" 88–89%, pytanie/konflikt 77%, Hexa 77%. Mediana wyswietlen spada (13 -> 6), czas ogladania ~8–9 s, zapisy+udostepnienia ~0.
1. Kadr 0,0 s: jedna liczba albo pytanie, max 6 slow, duzy napis + ruch od pierwszej klatki. Zero intro z data/logo. Data i zrodla na koncu.
2. ZAKAZ "Bitcoin price today" w pierwszym kadrze. Ten sam news jako konflikt/liczba: "$55K -> $60K in 6 hours", "Who sold $1B?", "BTC -14%, gold -4%: why?".
3. Dzien duzego ruchu (>=5% w 24 h): hak = sama liczba ruchu ("BTC UNDER $60K") – to jest temat dnia (20.11: 109 wyswietlen vs mediana 10).
4. Dlugosc: jedna mysl, cel 15–25 s. Gdy >25 s – w 8–10 s nowa liczba/zwrot akcji.
5. Min. 1 Reel z Hexa / "jak dziala nasz system AI" w tygodniu + CTA komentarzowe jednym slowem (jak "Comment HEXA" – najlepszy Reel: 353 wysw.).
6. Raz w tygodniu "cheat sheet": 3 liczby/poziomy na jednej planszy w ostatniej klatce (powod do zapisu).
7. TEST A/B TLA 23–29.11: 23/25/27/29.11 poranny Reel = A (obecne tlo bg()), wieczorny = B (generator neon 3D C:\Hexa\wideo_hf\reel_zloto\tlo_neon.js, SEED = data RRRRMMDD); 24/26/28.11 odwrotnie (poranny = B, wieczorny = A). Wszystko inne bez zmian. Podsumowanie tygodnia i seria Hexa poza testem. Kazdy Reel wpisz do C:\Hexa\tresci\testy_ab.md (data godz | wariant | temat).
8. Bez wpadek: nowy wariant – przed publikacja 3 klatki obejrzane (ostrosc, czytelnosc, pole bezpieczne, prawdziwe liczby, literowki). Bez zdjec szefa. Zero kosztow (nie uzywac kredytow ElevenLabs ani platnych generatorow).
Aktualne liczby, wnioski i kolejka testow: C:\Hexa\tresci\analiza_widza.md (aktualizowane co tydzien).
