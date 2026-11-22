# LEARNINGS

(wpisy na dole, format w README.md)

---

### L-20261111-01 [wideo] Darmowy plan ElevenLabs nie robi wideo
- Co się stało: próba kling-3-pro / veo dla klipu „Hexa w skarbcu” – brak modeli wideo na darmowym planie, dzienny limit obrazów i zajęty lektor.
- Wniosek / zasada: ruch postaci robimy paralaksą (rembg wycina postać, tło wolniej niż postać) + sceny 3D z tools/3d; do prawdziwego chodzenia/ruchu ust potrzebny płatny plan – decyzja szefa.
- Klucz: elevenlabs-darmowy-limit
- Powtórzenia: 1
- Status: nowy
- L-20261111-02: Pełne obrazy z Canva generate-image pobieramy tylko przez projekt + export-design (link z get-assets to miniatura 200 px z podpisem, zmiana rozmiaru = 403). Vercel buildCommand max 256 znaków → skrypt b.sh w files.

- L-20261116-01: Metricool „Could not upload video thumbnail” = YouTube odrzuca custom thumbnail (kanał bez weryfikacji telefonem; Shorts bez miniatur przez API). Shorts: bez videoThumbnailUrl, klatka 0 = okładka. Zmiana narzędzia nic nie da – to limit YouTube API.

### L-20261122-01 [skaner] RSI2 na indeksach: filtr zmienności zamiast filtra trendu
- Co się stało: test filtrów dla US30 RSI2 (bt_filtr_rsi2.py) – „zamknięcie nad SMA50” psuje okres do 2019 (-0.011R), a „ATR20/cena poniżej mediany 252 dni” poprawia obie połowy (+0.13/+0.16R vs +0.10/+0.11R); to samo na US500.
- Wniosek / zasada: kupowanie wyprzedania (RSI2) działa najlepiej w spokojnym rynku – w skoku zmienności (jak tydzień 16–20.11, Nasdaq -10%) sygnały RSI2 dochodzą do SL; dodatkowy filtr trendu tylko odsiewa dobre wejścia.
- Klucz: rsi2-filtr-zmiennosci
- Powtórzenia: 1
- Status: nowy
