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
