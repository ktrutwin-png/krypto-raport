# Sceny 3D do Reels / Shorts / Weekly (szef 11.11.2026)

Prawdziwy render 3D (three.js, metal PBR wg skilla `3d-metal-material`: ciemne studio, jasne karty, fazowane krawędzie, bloom).
Każda scena się rusza i ma wolne, ciemniejsze miejsce u góry na nagłówek.

## Najprościej: w `scenes.json` (kino.py robi resztę)
Zamiast `"img"` (albo obok, jako zapas) daj w scenie:
```json
{"d3": {"typ": "waga", "p": {"przechyl": 0.7}}, "head": ["…"], "say": "…"}
```
`kino.py` sam renderuje scenę na długość lektora. Jeśli render 3D się nie uda, bierze `"img"` (jeśli jest) – dlatego warto podać oba.

## Typy scen i parametry (`p`)
| typ | co widać | parametry |
|---|---|---|
| `liczba` | wielka metalowa liczba/napis, obraca się i łapie światło | `text` (np. `"0.4%"`, `"$73,689"`; znaki: cyfry, litery, `$ % + - . ,`), `sub` (mały napis pod spodem), `kolor`/`kolor2`: `gold` \| `silver` \| `btc` |
| `waga` | waga szalkowa: monety BTC (lewa) kontra sztabki złota (prawa), belka się przechyla | `przechyl` od -1 do 1: **dodatni = złoto cięższe (prawa szala w dół)**, ujemny = BTC cięższe. Cięższe = to, co dziś wygrało/zyskało |
| `swiece` | świece z wykresu w 3D, rosną po kolei, złota linia ceny | `dir`: `up` \| `down` \| `chop` (zgodnie z faktami), `n` (liczba świec, domyślnie 10) albo `dane`: lista prawdziwych zamknięć |
| `pokretlo` | zegar/pokrętło (stopy Fed, Fear & Greed, ryzyko): wskazówka jedzie od–do, podświetla się skala cyjan→złoto→czerwień | `od`, `do` w zakresie 0–1 (np. Fear & Greed 26 → `0.26`) |
| `skarbiec` | drzwi sejfu się otwierają, w środku piramida sztabek (rezerwy złota, banki centralne) | – |
| `globus` | Ziemia z kropek + złote łuki przepływów (ETF-y, banki centralne, kapitał) | `luki`: `[[szer1, dług1, szer2, dług2], …]` (stopnie), `lon0`: długość geogr. na środku kadru (np. `-30` Atlantyk, `60` Azja) |

Wspólne: `seed` (inny układ iskier/świec), `dy` (0–0.15: o ile obniżyć obiekt w kadrze).

## Zasady dla agentów
1. **W każdym filmie 1–2 sceny 3D**, dobrane do tematu dnia (BTC kontra złoto → `waga`; jedna liczba dnia → `liczba`; ruch ceny → `swiece`; Fed/stopy/sentyment → `pokretlo`; rezerwy/banki → `skarbiec`; przepływy/świat → `globus`). Reszta scen jak dotąd (obrazy holo).
2. **Za każdym razem coś innego**: nie ten sam typ 3D dwa dni z rzędu w tym samym miejscu filmu; zmieniaj parametry, `seed`, kolory.
3. **Fakty**: kierunek świec, przechył wagi i wartości pokrętła muszą zgadzać się z danymi dnia.
4. Render na CPU trwa ok. 0,8–1,5 s na klatkę (scena 5 s ≈ 2–4 min) – stąd limit 1–2 scen. `KINO_3D_FULL=1` = pełna rozdzielczość (ok. 2× dłużej).
5. Po renderze obejrzyj 2–3 klatki z gotowego filmu (ffmpeg `-ss`), zanim opublikujesz.

## Ręcznie (klatka albo film)
```
cd tools/3d && npm i            # raz: three@0.169.0
node scena.js waga '{"przechyl":-0.6}' waga.mp4 5            # film 5 s, 1080x1920
node scena.js liczba '{"text":"26","sub":"FEAR"}' okladka.jpg 4 1080 1350   # jedna klatka (np. tło miniatury/okładki)
```
Gotowy film można też podać w scenie jako `"img": "waga.mp4"`. Miniatury YouTube i okładki: klatka z `scena.js` jako tło (`.jpg`), tekst jak dotąd z `wzor_okladki.html`.

Stary szablon (moneta ₿ + sztabka): `scena_zloto.html` + `render.js`. Monety na stronę: `monety_sprite.html` + `sprite.js`.
