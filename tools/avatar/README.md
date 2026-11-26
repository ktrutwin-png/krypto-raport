# AVATAR SZEFA – bohater Raportu 18:00 (szef 26.11.2026 16:02)
Wzór postaci: `marka/Erl_avatar.jpg` (i na serwerze C:\Hexa\generatory\szef_avatar.jpg). NIE zmieniać wyglądu.
Wygląd: krótkie ciemne włosy postawione do góry, wygolone boki, ciemne okulary przeciwsłoneczne, BEZ WĄSÓW (szef), tylko cienki pasek bródki na brodzie, zawsze elegancko i z klasą (garnitur / płaszcz / kamizelka), świat nowoczesny cyberpunk (neon cyjan + ciepłe złoto).

## Generowanie (darmowe, serwer)
`python C:\Hexa\generatory\flux2_ref.py "<PROMPT>" wynik.jpg`  → FLUX.2 [dev] na Cloudflare z referencją postaci, 768x1344 (9:16), ~15 s, darmowa dzienna pula.
PROMPT = "The same man from the reference image: same face, same short dark hair styled up with shaved sides, clean-shaven upper lip with NO mustache, only a thin dark goatee strip on the chin, dark sunglasses, elegant and classy. High-end stylized 3D animated feature film still, detailed textures, cinematic lighting, modern cyberpunk world with neon cyan and warm gold lights, no text, no letters, no logos. Scene: <scena>"
- Napoje: tylko kawa, herbata albo woda – nigdy alkohol.
- Bank gotowych scen: `tools/avatar/bank/` – możesz użyć ponownie, ale min. 2 nowe sceny na każdy raport.
- Zapas (gdy Cloudflare odmówi): FLUX Kontext na HF (`C:\Hexa\lab\film_szef\sceny.py`, ref C:\Hexa\generatory\szef.png, dopisać „no mustache”), dzienny limit ok. 6 obrazów.
