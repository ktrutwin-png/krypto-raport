# Styl okładek i Reels (od szefa, 10.11) — wzór: okladka_wzor.jpg
Inspiracja: konto o XRP z 78 tys. obserwujących (styl, nie kopiujemy ich twarzy, logo ani grafik).
1. Tło: fotorealistyczna scena filmowa z hexa_gen.py (ludzie z emocją, flagi/miasta krajów z newsa, wielka złota 3D moneta). Prompt kończ "no text".
2. Nagłówek 2–3 słowa, Anton kursywa, biały + czerwony/złoty, gruby czarny obrys, w górnej 1/3.
3. Pasek na dole: krótkie zdanie WIELKIMI, jedna liczba/słowo na żółto (#ffd400).
4. Znak @erl.grey83 w prawym dolnym rogu.
5. Fakty prawdziwe (liczby z CoinGecko/CMC), bez obietnic zysków; w opisie "not financial advice".
Szablon: wzor_okladki.html (podmień bg, teksty), render Playwright 1080x1080 (feed) lub 1080x1920 (Reels).

## Z SZEFEM W ROLI GŁÓWNEJ (10.11)
- Szef chce być na okładkach zamiast obcych ludzi. Zdjęcie bazowe: C:\Hexa\generatory\szef.png (złota kurtka, irokez, okulary).
- Scena: `python C:\Hexa\generatory\edycja.py szef.png "Keep this exact man's face, mohawk, sunglasses, goatee and golden jacket. Place him ... no text" nazwa` (FLUX Kontext, zachowuje twarz).
- Reel wzór: tło z lekkim zoomem (ffmpeg zoompan), nakładka wzor_reel_nakladka.html (nagłówek NAD głową, nie na twarzy), lektor piper joe + muzyka music.py (tense przy spadkach, uplift przy wzrostach), ~20 s.
