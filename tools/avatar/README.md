# AVATAR SZEFA – bohater Raportu 18:00 (szef 26.11.2026 16:02)
Wzór postaci: `marka/Erl_avatar.jpg` (i na serwerze C:\Hexa\generatory\szef_avatar.jpg). NIE zmieniać wyglądu.
Wzór stylu i kolorów: film o szefie (marka/propozycje/film_szef_20261126). Wygląd: krótkie ciemne włosy postawione do góry, wygolone boki, ciemne okulary przeciwsłoneczne, BEZ WĄSÓW (szef), tylko cienki pasek bródki na brodzie, zawsze elegancko i z klasą (garnitur / płaszcz / kamizelka), świat nowoczesny cyberpunk (neon cyjan + ciepłe złoto).

## Generowanie (darmowe, serwer)
`python C:\Hexa\generatory\flux2_ref.py "<PROMPT>" wynik.jpg`  → FLUX.2 [dev] na Cloudflare z referencją postaci, 768x1344 (9:16), ~15 s, darmowa dzienna pula.
PROMPT = "Keep EXACTLY the same rendering style, realism, skin detail, lighting quality and face of the man in the reference image (semi-realistic cinematic 3D, like a high-end video game cutscene). Same man, same face, same hairstyle, dark sunglasses, clean-shaven upper lip with NO mustache, only the thin dark goatee strip on the chin. Elegant and classy outfit. Modern cyberpunk world, neon cyan and warm gold lights, no text, no letters, no logos. Scene: <scena>"
SZEF 26.11 16:08: styl jak w filmie o nim („kolorystycznie zajebiście”, „widać, że to ja”) – półrealistyczny, filmowy, NIE bajkowy/Pixar. Marka opiera się na NIM (wiarygodność), więc twarz ma być rozpoznawalna w każdej scenie; plan ogólny (daleko) max 1 na raport.
- Napoje: tylko kawa, herbata albo woda – nigdy alkohol.
- Bank gotowych scen: `tools/avatar/bank/` – możesz użyć ponownie, ale min. 2 nowe sceny na każdy raport.
- Zapas (gdy Cloudflare odmówi): FLUX Kontext na HF (`C:\Hexa\lab\film_szef\sceny.py`, ref C:\Hexa\generatory\szef.png, dopisać „no mustache”), dzienny limit ok. 6 obrazów.
