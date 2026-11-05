# Evening crypto report (18:00 Amsterdam)
1. Copy example_data.json to reports/YYYY-MM-DD-18/data.json and fill in fresh numbers (CoinMarketCap) and 3 verified news items.
2. `python3 tools/raport/build.py reports/YYYY-MM-DD-18/data.json` -> slide1-3.png next to data.json.
3. Convert to slide1-3.jpg (quality 92), write caption.txt, commit + push (repo is public; Instagram fetches raw.githubusercontent.com URLs).
4. Post with Windsor: connector instagram, account 17841402387775007, action create_carousel_post.

## Hook (od 5.11.2026)
Pole `"hook"` w data.json: duży nagłówek slajdu 1 (max ok. 7 słów, liczba albo pytanie, WIELKIE LITERY, np. "$466M OF SHORTS GONE IN 1 HOUR").
Zastępuje stały napis "CRYPTO REPORT" (ten idzie małą linijką pod hookiem z datą). `"kick"` zostaje jako krótki podtytuł nad hookiem.
Bez pola `hook` slajd wygląda jak dawniej.
