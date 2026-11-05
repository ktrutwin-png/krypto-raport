# Evening crypto report (18:00 Amsterdam)
1. Copy example_data.json to reports/YYYY-MM-DD-18/data.json and fill in fresh numbers (CoinMarketCap) and 3 verified news items.
2. `python3 tools/raport/build.py reports/YYYY-MM-DD-18/data.json` -> slide1-3.png next to data.json.
3. Convert to slide1-3.jpg (quality 92), write caption.txt, commit + push (repo is public; Instagram fetches raw.githubusercontent.com URLs).
4. Post with Windsor: connector instagram, account 17841402387775007, action create_carousel_post.

## Hook (od 5.11.2026)
Pole `"hook"` w data.json: duży nagłówek slajdu 1 (max ok. 7 słów, liczba albo pytanie, WIELKIE LITERY, np. "$466M OF SHORTS GONE IN 1 HOUR").
Zastępuje stały napis "CRYPTO REPORT" (ten idzie małą linijką pod hookiem z datą). `"kick"` zostaje jako krótki podtytuł nad hookiem.
Bez pola `hook` slajd wygląda jak dawniej.

## Styl CYBERPUNK (od 5.11.2026) - domyslny
`build.py` robi 3 slajdy **1080x1350 (4:5)** w neonowym stylu (cyjan = krypto, roz = alarm, zolty = wnioski/zloto), haslo "FACTS, NOT HYPE" na kazdym slajdzie.
Nowe pola: `"btc7d"` (ok. 8-12 cen BTC z 7 dni z CoinGecko get-coin-market-chart, do wykresu na slajdzie 1), `"bg"` (opcjonalne tlo AI bez tekstu, plik obok data.json albo URL; bez niego rysowane jest neonowe miasto).
`kick` = krotki podtytul (max ~40 znakow). Stary kwadratowy szablon: `build_old_square.py`.

## Tla AI (znak rozpoznawczy: postac "The Watcher")
Folder `tools/raport/bg/` - tla wygenerowane AI (bez tekstu/logo). Ustaw w data.json `"bg": "watcher_01.png"` (szablon sam znajdzie plik w bg/). Z tlem AI wykres BTC na slajdzie 1 jest ukryty, zeby nie zaslanial postaci. `"bgpos"` (domyslnie "12% center") przesuwa kadr.
Kiedy w bg/ jest kilka plikow, uzywaj ich po kolei (dzien miesiaca modulo liczba plikow).

## Raport jako film z muzyka (od 5.11.2026, domyslnie)
Po `build.py` uruchom `python3 tools/raport/video.py reports/RRRR-MM-DD-18 <nastroj>` -> `report.mp4` (ok. 17,5 s, 1080x1920) + `cover.jpg`.
Nastroj muzyki wg dnia: tense (spadki/hack/likwidacje), uplift (wzrosty), gold (zloto/Fed/makro), calm (spokojny dzien).
W data.json ustaw `"swipe": "FOLLOW @ERL.GREY83"` (w filmie nie ma przesuwania). Publikacja: Windsor `create_video_post` (Reel, share_to_feed true).
