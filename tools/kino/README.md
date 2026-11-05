# KINO – filmowy Reel z lektorem (styl główny od 5.11.2026)
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
