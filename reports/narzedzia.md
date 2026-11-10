# Narzędzia zespołu (nazwa | do czego | komu | od kiedy)

## Darmowe generatory obrazów i wideo (Mózg 10.11.2026, szef: „znajdź darmowy generator i podaj agentom”)
- Canva generate-image | obrazy (tekst→obraz i edycja z obrazem referencyjnym przez create-upload-url) – działa, dobra jakość; pełna rozdzielczość zostaje w Canvie (na zewnątrz tylko miniatura) | Reżyser, Handlowiec, Pisarz | 10.11.2026
- Hugging Face Spaces (konektor Hugging_Face → dynamic_space) | FLUX.1-Krea-dev i Qwen-Image (obrazy), FLUX.1-Kontext-Dev (edycja zdjęć), zerogpu-aoti/wan2-2-fp8da-aoti-faster (WIDEO z obrazu, 3–5 s), mcp-tools/wan-2-2-first-last-frame (wideo między dwoma klatkami), ResembleAI/Chatterbox (lektor), not-lain/background-removal (usuwanie tła) | Reżyser (Reels, okładki, strona), Handlowiec (przykładowe Reels do ofert), Pisarz (okładka e-booka) | CZEKA: szef musi włączyć Spaces w ustawieniach MCP Hugging Face (teraz „gradio=none” – invoke zablokowany); darmowy limit GPU dzienny
- Pollinations (https://image.pollinations.ai/prompt/<opis>?width=..&height=..&nologo=true) | awaryjny generator obrazów bez konta, przez curl | wszyscy | 10.11.2026 – UWAGA: słaba zgodność z opisem i znak wodny – tylko szkice, nie do publikacji
- ElevenLabs (konektor) | obrazy darmowe tylko gdy kolejka wolna („Free generations are busy” – nie ponawiać w tym samym przebiegu); WIDEO wymaga płatnego planu – nie używać; lektor oszczędnie (kredyty dzielone z głosem Hexy)
- Gamma generate_image | NIE – brak kredytów na darmowym planie
- Animacje 3D w przeglądarce (three.js r128 z cdnjs, strona-artefakt) | darmowe „filmy” i spacery 3D bez generatora – wzór: artefakt „Pokój Szefa” 10.11.2026 | Reżyser, Mózg
