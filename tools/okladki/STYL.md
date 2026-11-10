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

## POPRAWKI SZEFA (10.11, 18:17)
- Szef NIE MA wąsów: tylko bródka na brodzie, zwykłe czarne prostokątne okulary (nie przeciwsłoneczne), krótki irokez.
- FLUX Kontext dorysowuje wąsy → do scen z szefem używaj jego PRAWDZIWYCH zdjęć (C:\Hexa\generatory\szef\: studio, dubai, miasto, moto, usmiech). Kontext tylko gdy nie ma pasującego zdjęcia i zawsze sprawdź twarz.
- Reel = kilka scen co 3–5 s (nie jeden obraz): 1) szef + hook, 2–4) sceny tematu z hexa_gen (BTC/XRP/złoto…) z liczbą dnia, 5) szef + pytanie/CTA. Przejścia xfade slideleft 0.4 s, lekki zoom. Szef pojawia się co jakiś czas, nie cały czas.
- Nakładki: nakladki_scen.py (Playwright, przezroczyste PNG 1080x1920).
