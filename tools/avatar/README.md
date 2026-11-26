# AVATAR SZEFA – bohater Raportu 18:00 (szef 26.11.2026 16:02)
Wzór postaci: `marka/Erl_avatar.jpg` (i na serwerze C:\Hexa\generatory\szef_avatar.jpg). NIE zmieniać wyglądu.
Wzór stylu i kolorów: film o szefie (marka/propozycje/film_szef_20261126). Wygląd: krótkie ciemne włosy postawione do góry, wygolone boki, ciemne okulary przeciwsłoneczne, BEZ WĄSÓW (szef), tylko cienki pasek bródki na brodzie, zawsze elegancko i z klasą (garnitur / płaszcz / kamizelka), świat nowoczesny cyberpunk (neon cyjan + ciepłe złoto).

## Generowanie (darmowe, serwer)
`python C:\Hexa\generatory\flux2_ref.py "<PROMPT>" wynik.jpg`  → FLUX.2 [dev] na Cloudflare z referencją postaci, 768x1344 (9:16), ~15 s, darmowa dzienna pula.
PROMPT = "Keep EXACTLY the same rendering style, realism, skin detail, lighting quality and face of the man in the reference image (semi-realistic cinematic 3D, like a high-end video game cutscene). Same man, same face, same hairstyle, dark sunglasses, clean-shaven upper lip with NO mustache, only the thin dark goatee strip on the chin. Elegant and classy outfit. Modern cyberpunk world with varied cinematic colour grading that fits the scene (warm lamplight, rainy blue night, golden sunrise, orange industrial light, neon accents), no text, no letters, no logos. Scene: <scena>"
SZEF 26.11 16:08: styl jak w filmie o nim („kolorystycznie zajebiście”, „widać, że to ja”) – półrealistyczny, filmowy, NIE bajkowy/Pixar. Marka opiera się na NIM (wiarygodność), więc twarz ma być rozpoznawalna w każdej scenie; plan ogólny (daleko) max 1 na raport.
- Napoje: tylko kawa, herbata albo woda – nigdy alkohol.
- Bank gotowych scen: `tools/avatar/bank/` – możesz użyć ponownie, ale min. 2 nowe sceny na każdy raport.
- Zapas (gdy Cloudflare odmówi): FLUX Kontext na HF (`C:\Hexa\lab\film_szef\sceny.py`, ref C:\Hexa\generatory\szef.png, dopisać „no mustache”), dzienny limit ok. 6 obrazów.

## WĄTEK „BUDUJĘ HEXĘ” (szef 26.11.2026 16:09: „pokazujemy, jak budujemy Hexę – to nasze dzieło, nie mamy się czego wstydzić”)
- W The Trader's Diary 1–2 razy w tygodniu jedna scena o budowie Hexy: szef w warsztacie/przy biurku, przed nim holograficzna Hexa (w trakcie budowy, ze światła i kodu), lektor mówi np. „At night I also build Hexa – an AI that helps me stay disciplined.” Uczciwie: Hexa to projekt w budowie, bez przesadnych obietnic.
- Dwie referencje naraz: `python C:\Hexa\generatory\flux2_ref.py "<prompt>" wynik.jpg C:\Hexa\generatory\szef_avatar.jpg 768 1344 C:\Hexa\krypto-raport\marka\Hexa_postac.png` (prompt: „the man from the first reference image … the AI woman from the second reference image …” – wygląd Hexy wg karty postaci: złote oczy, ensō na czole, niebiesko-fioletowe włosy, ciemny strój ze złoto-cyjanowymi liniami).
- Na końcu takiej sceny/opisu można dodać: „Meet Hexa – every Saturday 21:00”.

## DZIENNY LIMIT (sprawdzone 26.11)
- Cloudflare Workers AI: 10 000 neuronów/dzień (reset 00:00 UTC) – starcza na ok. 5–6 obrazów FLUX.2 + karuzelę 10:00 (flux-1-schnell, tani). KOLEJNOŚĆ: najpierw karuzela 10:00 (schnell), potem max 4 nowe sceny FLUX.2 na 18:00, resztę scen bierz z `tools/avatar/bank/`. Każdą nową scenę dopisz do banku.
- Zapas: HF FLUX Kontext (ok. 6 obrazów/dzień). Nie kupujemy płatnych planów bez zgody szefa.

## KOLORY (szef 26.11.2026 16:13)
Postać zostaje jak w `marka/Erl_avatar.jpg`, ale NIE wszystko w dwóch kolorach (cyjan + złoto). Ma być nowocześnie i różnorodnie jak w filmie o szefie (marka/propozycje/film_szef_20261126): każda scena ma własną, pasującą paletę – ciepła lampa nocą, deszczowy niebieski, złoty wschód słońca, pomarańczowe światło hali, neon tylko jako akcent. W jednym odcinku min. 2 różne palety.

## ⛔ 26.11 16:34 – w Raporcie 18:00 bez Hexy (ani wyglądu, ani głosu). Sekcja „WĄTEK BUDUJĘ HEXĘ” wyżej – NIEAKTUALNA dla 18:00.
