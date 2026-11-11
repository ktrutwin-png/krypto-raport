# KINO – Reel z lektorem
## Styl "news" (DOMYŚLNY od 6.11.2026 – wzór szefa: „taka forma jest najlepsza dla YT i Insta”)
Gruby naglowek u góry (Anton, biały + *żółty* + ~zielony~, lekko pochylony), opcjonalnie tag (np. LIVE MARKET UPDATE), sub, chip (▲/▼ liczba), note (ciemna ramka wchodząca w połowie sceny). Obrazy = holograficzne sceny z wykresami/panelami danych (bank: *_holo_*). Szybki energiczny lektor: piper **en_US-ryan-high** (obniżony o 10%), ~2,5 słowa/s. Na końcu automatyczna plansza „This Is Not Financial Advice! Just data. @erl.grey83”. 4–6 scen, 25–40 s.
Głos pobierz do tools/reel/voice/: https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/ryan/high/en_US-ryan-high.onnx (+ .onnx.json), export no_proxy= NO_PROXY=. Folder voice/ jest w .gitignore.
Prompt obrazu (news): "Futuristic holographic <temat> dashboard, vertical composition, <wykres/obiekt>, floating translucent data panels, deep navy background, neon cyan and gold light, ultra detailed 3D render, top third darker and empty for headline, no readable words".

### Sceny 3D (od 11.11.2026 – szef: 1–2 w każdym filmie)
`"d3": {"typ": "waga", "p": {"przechyl": 0.7}}` w scenie – prawdziwy render 3D zamiast obrazu, na długość lektora (typy: liczba, waga, swiece, pokretlo, skarbiec, globus; parametry i zasady: `tools/3d/README.md`). Podaj też `"img"` jako zapas. `"img"` może być gotowym filmem `.mp4`.
Nagłówki same się dopasowują (jedna linia = jeden wiersz), u góry złoty pasek postępu.

### Ruchome grafiki (od 6.11.2026 – szef: „żeby to naprawdę przyciągało oko”)
- `"ticker": "BTC $78,934 ▼0.2% · ETH $2,640 ▼1.1% · GOLD $4,100 ▲0.4%"` (na poziomie pliku) – przewijany pasek z cenami na każdej scenie. Zawsze dodawaj (prawdziwe ceny z danych).
- `"anim": {"dir": "up"|"down"|"chop", "label": "$4,100"}` w scenie – żywe świeczki rysowane klatka po klatce (pojawiają się po kolei, ostatnia drga, świecąca linia ceny). Używaj w 1–2 scenach o ruchu ceny; kierunek zgodny z faktami.
- Obrazy NIE muszą być wykresami: dowolna scena w tym stylu (holo-hologramy, budynki, monety, sejfy, statki z ropą, chipy…), byle mocno przyciągała oko.

## Styl "cinema" (stary, "style":"cinema")
Pełnoekranowe pionowe zdjęcia (9:16), wolny ruch kamery, duża liczba + podpis na każdej scenie, @erl.grey83 + data u góry, lektor (piper joe) i muzyka ściszana pod głosem. 5–7 scen, ok. 35–60 s.

## Użycie
1. Folder z obrazami scen + `scenes.json` (format w nagłówku `kino.py`).
2. `python3 tools/kino/kino.py <folder>` -> `reel.mp4` + `cover.jpg`. Głos: `tools/reel/voice/en_US-joe-medium.onnx` (pobierz wg `tools/reel/README.md`) albo env `KINO_VOICE`.

## Skąd obrazy (wszystko darmowe, kolejność)
1. **Bank** `tools/kino/bank/<temat>_NN.jpg` (1080x1920). Użyj, jeśli pasuje do tematu; nie powtarzaj tego samego zdjęcia 2 dni z rzędu.
2. **Figma** `generate_image` (darmowe kredyty AI, model gpt-image-2.5-flare, width 1152 height 2048) w pliku `XSucIPOTvPfIBfy6ietmFL` (create_session przed). Pobierz `image.url` curl-em.
3. **Unsplash** `search_photos` (orientation portrait, plus none) + `download_asset` – prawdziwe zdjęcia HD (Kapitol, złoto, giełda). Pobierz z `&w=1440`.
4. **ElevenLabs** (darmowy dzienny limit): flow + add_flow_node `bytedance-seedream-5-pro` z `{"aspect_ratio":"9:16","resolution":"2K"}`, run z generations_count 1.
Każde nowe zdjęcie przytnij do 9:16, zapisz 1080x1920 do banku z nazwą tematu i commituj – bank rośnie.

Prompt obrazu: "Cinematic photorealistic vertical shot, <temat>, dramatic light, subtle cyan and magenta neon rim light, shallow depth of field, ultra detailed, dark empty space in the lower third, no text". Bez prawdziwych osób, bez logo.
