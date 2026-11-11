# SKILLE GRAFICZNE – kopie w repo (szef 11.11.2026: „każdy agent odpowiedzialny za grafikę ma ich używać”)

Agenci w chmurze nie mają skilli z serwera, dlatego tu leżą ich kopie (licencje MIT / Apache-2.0 w każdym folderze).
**Przed każdą pracą graficzną przeczytaj SKILL.md odpowiedniego skilla i stosuj go.**

| skill | do czego | kto |
|---|---|---|
| `ui-ux-pro-max/` | system designu: palety, pary fontów, układ, 120 zasad UX, dostępność. Wyszukiwarka: `python3 tools/skille/ui-ux-pro-max/scripts/search.py "<temat>" --domain style\|color\|typography\|ux\|chart` albo `--design-system` | agent strony, Reżyser (okładki, plansze), ORB/Hexa |
| `banner-design/` | miniatury YouTube (1280×720), okładki, banery: rozmiary, strefy bezpieczne, 1 CTA, kontrast ≥ 4,5:1, 2–3 kierunki artystyczne | Reżyser (miniatury Shorts/Weekly, okładki Reels), Social Media |
| `bang-motion/` | motion design: kinetic typography, openery, explainery jako jeden index.html z osią czasu (GSAP), render klatka po klatce | Reżyser – intro Weekly, mocny hook w 1. sekundzie Reela, filmy specjalne |
| `hyperframes/` | HTML → MP4 deterministycznie: animowane wykresy, mapy, napisy słowo po słowie | Reżyser – gdy kino.py czegoś nie ma. Telemetria wyłączona – NIE uruchamiaj `npx hyperframes events` |

Do tego (już opisane gdzie indziej): sceny 3D `tools/3d/README.md` (rozkaz R14), `impeccable` + `design-taste-frontend` + `no-ai-slop` (serwer `C:\Users\Administrator\.claude\skills\`), rembg (wycinanie tła, serwer `C:\Hexa\grafika\.venv`).

## Wzorce (11.11, demo dla szefa)
- Miniatura YT: `wzory/miniatura.html` – tło = klatka 3D (`node tools/3d/scena.js waga '{"przechyl":0.7,"dx":0.24}' tlo_mini.jpg 5 1280 720`), z lewej 2–3 słowa Anton (jedno złote), niżej liczby zielone/czerwone, tag u góry, @erl.grey83 w rogu.
- Kinetic typography: `wzory/kinetyka.html` – literki wpadają osobno (GSAP), liczba z rozmyciem i „pulsem”, złota kreska, podpis; render: `wzory/render_kin.js` (klatki 30 fps → ffmpeg). Nadaje się na 1. sekundę Reela (hook) albo intro Weekly.

## Kontrola przed publikacją (każda grafika)
1. Obejrzyj wynik (klatka / PNG) – nic ucięte, tekst czytelny na telefonie (miniatura w 320 px szerokości!).
2. Palety i fonty z naszego stylu (granat + złoto, Anton/Inter, zielony/czerwony tylko dla wzrostów/spadków).
3. Teksty bez pustych frazesów (`no-ai-slop`), fakty zgodne z danymi.
