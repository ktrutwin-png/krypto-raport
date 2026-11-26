# Serial „Przygody Hexy” – ZASADY OBOWIĄZKOWE (szef 22.11.2026)

## 🔆 ZNAK ENSŌ NA KAŻDEJ PUBLIKACJI (szef 26.11.2026 21:51) – OBOWIĄZUJE PRZED WSZYSTKIM PONIŻEJ
Szef: „na wszystkim, co publikujemy, zawsze znaczek – może być wpasowany w tło, ważne, żeby było go widać”.
- Ostatni krok przed KAŻDĄ publikacją (Reel 10:00, Raport 18:00, odcinek Hexy, karuzela, grafika, okładka): `python tools/znak/enso_znak.py <plik.mp4|.jpg>` (nadpisuje plik; dźwięk bez zmian). Domyślnie prawy górny róg, 10% szerokości, z miękkim cieniem. Jeśli w rogu jest napis – `--rog lg|pd|ld`.
- Po nałożeniu obejrzyj klatkę (ffmpeg -ss 5 … -frames:v 1, Read): znak widoczny, nie zasłania liczb ani twarzy. Bez znaku = NIE publikuj; w dzienniku dopisz „Ensō ✔”.
- Plik znaku: marka/Enso_znak_wodny.png (z zatwierdzonego Ensō, nie generować od nowa).




## 🎙️ NOWY GŁOS HEXY = SONIA (szef 26.11.2026 14:54) – zastępuje głos Pola
- Głos Hexy w serialu i wszędzie po angielsku: darmowy edge-tts `en-GB-SoniaNeural` (bez zmian tempa i tonu). Próbka: marka/propozycje/glos_hexy_20261126/hexa_EN_Sonia.mp3.
- Od odcinka #2 audio Hexy generuj DARMOWO Sonią (python -m edge_tts -v en-GB-SoniaNeural), a ElevenLabs używaj tylko do obrazu/wideo (OmniHuman dostaje gotowe audio Sonii). Dzięki temu głos się nie zmieni po 18.12 i zostaje więcej kredytów na odcinki.
- Głosu Pola (lqJpYZ185uAhVny7fXot) już nie używamy w nowych materiałach.

## ⛔ KONIEC ELEVENLABS – ZAPAS ODCINKÓW (szef 26.11.2026 14:49) – OBOWIĄZUJE PRZED WSZYSTKIM PONIŻEJ
Szef: „Resztę kredytów ElevenLabs wykorzystaj do stworzenia jak największej ilości serialu Hexy” – rezygnujemy z ElevenLabs (oszczędzamy).
- Stan 26.11 14:50: plan Pro, zostało ok. 231 000 kr., ważne do odnowienia 18.12.2026 12:50 UTC. Po tej dacie ElevenLabs NIE istnieje w naszym systemie.
- Limit 60 000/odcinek i rezerwa 150 000 z pkt 7 – UCHYLONE. Nowa zasada: zostaw tylko 10 000 kr. rezerwy (głos Hexy w telefonie do czasu przełączenia na darmowy), resztę zużyj na odcinki.
- Kolejność: #2 Szklane Miasto (28.11), #3 Archiwum Mgieł (5.12), #4 Miraż (12.12), #5 Planeta Zegarów (19.12), #6 Kuźnia (26.12), #7 Lustrzany Księżyc (2.01) – rób po kolei, aż skończą się kredyty. Jakość wg R40 i pkt 6 bez obniżania; jeśli kredyty na ostatni odcinek nie starczą na całość, zrób jego najdroższe ujęcia (Hexa mówi – OmniHuman, boss, planeta), a resztę dokończ darmowo.
- Zawsze estimate_only przed wideo; po każdej generacji wpis do reports/elevenlabs_budzet.md (Zużycie).
- Gotowe odcinki: tools/hexa_seria/epN/ (final.mp4 + kontrola.md + opis IG). Publikacja bez zmian: sobota 21:00, TYLKO Instagram.
- Rytuał (ep2/rytual.mp4) i intro nagrane raz – używaj ponownie, nie generuj drugi raz.
- Głos Hexy po 18.12 = darmowy (edge-tts, próbki: marka/propozycje/glos_hexy_20261126/, wybór szefa w toku) – NIE generuj nic w ElevenLabs po 18.12.

## ⛔ TYLKO INSTAGRAM (szef 25.11.2026 22:14) – OBOWIĄZUJE PRZED WSZYSTKIM PONIŻEJ
Szef: „na razie YouTube odpuszczamy, X i Facebook też – zostajemy na Instagramie; najpierw budujemy firmę, potem wydatki”. Od teraz publikujesz WYŁĄCZNIE na Instagramie (Windsor, konto erl.grey83, plan darmowy). NIE wysyłaj nic na YouTube (ani Windsor, ani Metricool), na X (Typefully) ani na Facebook. Nie kupujemy Windsor Basic. Brak YT/X w dzienniku to NIE błąd – nie zgłaszaj. Wszystkie wpisy o YT/X/FB poniżej są zawieszone, dopóki szef sam ich nie przywróci.


> Szef 22.11: „nie tak miał wyglądać pierwszy odcinek … ustalaliśmy”. Ep.1 z 22.11 zrobiono wg STAREGO scenariusza (`ep1_scenariusz.md`, R27/R34),
> a od 16.11 obowiązuje R40. Odcinek zostaje opublikowany, ale od Ep.2 każdy odcinek MUSI spełniać poniższe punkty.

1. **Jedyne źródło prawdy = biblia serialu** (Docs: https://claude.ai/artifact/8vHxSPX9LRMBJt1oHny3wT) + R40 w `reports/plan_wzrostu.md`.
   Przeczytaj OBIE przed napisaniem scenariusza. Pliki `ep1_scenariusz.md` i `karta_en.html` są NIEAKTUALNE (stara seria R34).
2. Kalendarz R40: 28.11 #2 Szklane Miasto (Szeptacz → Filtr Głosu), 5.12 #3 Archiwum Mgieł, 12.12 #4 Miraż, 19.12 #5 Planeta Zegarów, 26.12 #6 Kuźnia, 2.01 #7 Lustrzany Księżyc.
   Odcinek = planeta-serwer + boss + nowy klocek + Rytuał (5–6 s) + lekcja „jak dać ten klocek swojemu AI”. Bez krypto/złota.
3. **Zakończenie każdego odcinka: Hexa MÓWI wezwanie** – „Comment HEXA and I'll send you the map.” (głos Pola, OmniHuman, na ekranie napis COMMENT „HEXA”).
4. **Link w opisie** do strony Hexy z repozytoriami/klockami: https://erlgrey83-crypto-freaq.vercel.app/brain/ (ta sama co DM za komentarz HEXA, R31) + „Link in bio”.
5. Szef 22.11: „ty decydujesz o grafikach o wszystkim … ma wyglądać nowocześnie i zajebiście, nie tandetnie”. Bez pytania o zgodę – ale zgodnie z biblią.
6. JAKOŚĆ (zakaz „tandety”): kino pełnoekranowe 9:16, żadnych płaskich paneli z kółkami/ikonkami. Sceny planety-serwera i bossa = wideo AI
   (ElevenLabs: kling-3-pro / seedance-v2.5, 9:16, 1080p, prompt filmowy: głębia, światło wolumetryczne, mokre odbicia, ruch kamery),
   Hexa mówi = OmniHuman 1.5 (max 30 s audio na klip – dziel), Rytuał 5–6 s zawsze te same ujęcia (zapisz raz w ep2/rytual.mp4 i używaj ponownie).
   Napisy: duże, 2–4 słowa naraz, środek-dół, Anton/Inter, podświetlenie słowa. Muzyka filmowa cicho pod głosem. 30–60 s.
   Przed publikacją obejrzyj min. 6 klatek – jeśli cokolwiek wygląda tanio, popraw zanim wyjdzie.
7. Budżet ElevenLabs na odcinek: max 60 000 kr. (sprawdź account_get_usage; zostaw min. 150 000 kr. na resztę miesiąca). Zawsze estimate_only przed wideo.
8. Publikacja: SOBOTA 21:00 (Europe/Amsterdam) jednocześnie IG Reel + YT Short (Metricool brandId 7613270, isAiGenerated true)
   oraz X (Typefully social_set 366138; wideo < 10 MB → ffmpeg 720×1280 2-pass ~1,8 Mb/s, made_with_ai true; w treści link /brain/).
   W opisie IG/YT: CTA „Comment HEXA 👇” + link w bio. Wersja 16:9 na /brain/.

## KONTROLA PRZED PUBLIKACJĄ (obowiązkowa, szef 22.11: „kontroluj wszystko”)
Zanim cokolwiek zostanie zaplanowane, zapisz tools/hexa_seria/epN/kontrola.md z ✅/❌ dla każdego punktu. Każdy ❌ trzeba naprawić, a dopiero potem publikować:
a) temat, planeta, boss i klocek zgodne z biblią i kalendarzem R40 na tę datę;
b) Hexa na końcu MÓWI „Comment HEXA and I'll send you the map” (sprawdź w transkrypcji) + napis COMMENT „HEXA”;
c) opis IG/YT: „Comment HEXA”, „Link in bio”, „Hexa's Adventures – every Saturday”; X: link /brain/;
d) zaplanowane na 3 platformach (IG Reel, YT Short, X) na sobotę 21:00, flagi AI ustawione;
e) min. 8 klatek obejrzanych: pełny ekran, ostre, napisy w polu bezpiecznym (nie w górnych 220 px ani dolnych 300 px), bez literówek, liczby zgodne z reports/roj_status.json;
f) plansza końcowa zapowiada właściwy następny odcinek wg R40.

## KARTA POSTACI (Mózg 22.11.2026) – OBOWIĄZKOWY WZÓR WYGLĄDU
marka/Hexa_karta_postaci_B.png (główna) + marka/Hexa_karta_postaci_A.png: twarz ze złotymi oczami, ensō na czole (złote = mówi/aktywna, czerwone = złość, przygaszone = spokój), świecące niebiesko-fioletowe włosy ze światła, ciemny dopasowany strój ze złoto-cyjanowymi liniami, szpilki. Każdy obraz/film Hexy generuj z referencją tej karty + marka/Hexa_postac.png. Miny: lekki uśmiech, oczko, zamyślenie, złość.
