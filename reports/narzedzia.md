# Narzędzia zespołu (nazwa | do czego | komu | od kiedy)

## Darmowe generatory obrazów i wideo (Mózg 10.11.2026, szef: „znajdź darmowy generator i podaj agentom”)
- Canva generate-image | obrazy (tekst→obraz i edycja z obrazem referencyjnym przez create-upload-url) – działa, dobra jakość; pełna rozdzielczość zostaje w Canvie (na zewnątrz tylko miniatura) | Reżyser, Handlowiec, Pisarz | 10.11.2026
- Hugging Face Spaces (konektor Hugging_Face → dynamic_space) | FLUX.1-Krea-dev i Qwen-Image (obrazy), FLUX.1-Kontext-Dev (edycja zdjęć), zerogpu-aoti/wan2-2-fp8da-aoti-faster (WIDEO z obrazu, 3–5 s), mcp-tools/wan-2-2-first-last-frame (wideo między dwoma klatkami), ResembleAI/Chatterbox (lektor), not-lain/background-removal (usuwanie tła) | Reżyser (Reels, okładki, strona), Handlowiec (przykładowe Reels do ofert), Pisarz (okładka e-booka) | ✅ DZIAŁA (10.11) przez nasz skrypt na serwerze: `python C:\Hexa\generatory\hexa_gen.py obraz "opis" 16:9 nazwa` → C:\Hexa\generatory\out\; inne Space: `hexa_gen.py api <space>` i gradio_client z tokenem z C:\Hexa\sejf\huggingface.txt. Konektor dynamic_space nadal ma invoke zablokowany (gradio=none) – nie używać. Darmowy dzienny limit GPU
- Pollinations (https://image.pollinations.ai/prompt/<opis>?width=..&height=..&nologo=true) | awaryjny generator obrazów bez konta, przez curl | wszyscy | 10.11.2026 – UWAGA: słaba zgodność z opisem i znak wodny – tylko szkice, nie do publikacji
- ElevenLabs (konektor ElevenLabs-619b9b4c) | od 12.11 PŁATNY plan Creator: lektor EN, obrazy hero, 1 klip wideo/mies. – WYŁĄCZNIE wg budżetu `reports/elevenlabs_budzet.md` (pule, limity tygodniowe, wpis po każdej generacji) | Reżyser, Handlowiec, Pisarz | 12.11.2026
- Gamma generate_image | NIE – brak kredytów na darmowym planie
- Animacje 3D w przeglądarce (three.js r128 z cdnjs, strona-artefakt) | darmowe „filmy” i spacery 3D bez generatora – wzór: artefakt „Pokój Szefa” 10.11.2026 | Reżyser, Mózg


## 🔐 SEJF KLUCZY
Wszystkie klucze szefa: C:\Hexa\sejf\ na serwerze, spis w SPIS.md (bez wartości). Nowy klucz wpisuje ZAWSZE szef sam przez stronkę „Klucz dla Hexy” (wzór: laptop C:\Users\ktrut\migracja\hfform.ps1 + adb reverse na telefon). Agent nigdy nie przepisuje kluczy.
