# Styl okładek i Reels (od szefa, 10.11) — wzór: okladka_wzor.jpg

> ⛔ ZAKAZ (szef 10.11, 22:34): ŻADNYCH zdjęć szefa (prawdziwych ani wygenerowanych) w Reels, Shorts, YouTube, okładkach i miniaturach. Sekcje „Z SZEFEM” i „SZEF RZADKO” poniżej są NIEAKTUALNE. Tylko grafika bez jego twarzy.
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
- Reel = kilka scen co 3–5 s (nie jeden obraz), same mocne grafiki tematu z hexa_gen (BTC/XRP/złoto/flagi krajów…) z liczbą dnia + pytanie/CTA na końcu. Przejścia xfade slideleft 0.4 s, lekki zoom.
- SZEF RZADKO (decyzja 10.11 18:29): jego zdjęcie najwyżej w 1 na 3–5 Reelsów (ok. raz na 1–2 tygodnie), wtedy jedna scena ~1 s. Może być prawdziwe zdjęcie albo wygenerowane, byle bez wąsów. Reszta = grafika „dojebana” jak we wzorze reel_szef_v2.
- Nakładki: nakladki_scen.py (Playwright, przezroczyste PNG 1080x1920).

## ZASADA ŚWIEŻYCH GRAFIK (szef 10.11.2026)
- Każdy reel/Short = NOWE grafiki do każdej sceny, generowane pod temat dnia (C:\Hexa\generatory\hexa_gen.py → obraz(..., "9:16", ...)).
- Ta sama grafika najwyżej raz – nie powtarzamy tej samej monety/sejfu/tła w kolejnych filmach.
- Różne ujęcia w jednym filmie: inne kadry, kolory, obiekty (wykresy, ludzie, miasta, giełdy, symbole), nie 3× ta sama moneta.
- Lektor: domyślnie polski/angielski Piper (pl_PL-darkman-medium / en_US-joe), czyta i dopowiada wyjaśnienia.
- Ruch obowiązkowy (szef 10.11): każda scena się rusza (zoom/przesuw, przejścia slide, animowane napisy) – jakość grafik jak dotąd, tylko bez powtórek.
- Te zasady (świeże grafiki, ruch, lektor) obowiązują tak samo na YouTube: Shorts, Weekly Market Brief i miniatury (szef 10.11).
