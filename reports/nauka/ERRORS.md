# ERRORS

(wpisy na dole, format w README.md)

---

### E-20261111-01 [skaner] Restart skanera: nie uruchamiaj drugiej kopii
- Co się stało: po Stop-Process pythona Mózg sam odpalił skaner, a pętla START_SKANER_DZIENNY.bat po 60 s podniosła drugi – przez ~1 min działały dwa skanery.
- Wniosek / zasada: skaner dzienny na serwerze ma własną pętlę w .bat – do restartu wystarczy zabić sam proces python z skaner_dzienny.py i poczekać ~60 s; NIGDY nie uruchamiać go ręcznie obok pętli.
- Klucz: restart-skanera-podwojny
- Powtórzenia: 1
- Status: nowy

## E-20261111-02 [social] Raport 18 opóźniony → YouTube Short 18:23 bez filmu
- Co się stało: pierwszy render 36.7 s (za długi lektor), skracanie + ponowny render 3D; publikacja ~18:35, a Reżyser YouTube o 18:23 nie znalazł out/2026-11-11-18/reel.mp4 (404) – Short przepadł.
- Wniosek / zasada: przed pierwszym renderem policz długość lektora (~2.6 słowa/s, cel ≤ 30 s → ≤ 75 słów łącznie); reel.mp4 + cover.jpg mają być w repo najpóźniej 18:20. Reżyser YouTube przy 404 próbuje jeszcze 2× co 10 min zanim wpisze BŁĄD.
- Klucz: raport-za-pozno-yt
- Powtórzenia: 1
- Status: nowy

## E-20261111-03 [social] Tekst ucięty przy krawędzi kadru
- Co się stało: Raport 18 11.11, scena końcowa: podpis „BULL OR BEAR BY FRIDAY? 🐂 / 🐻” wychodzi poza lewą krawędź (ucięte „B”).
- Wniosek / zasada: każdy wiersz tekstu musi mieścić się w bezpiecznej strefie (64 px od krawędzi w 1080×1920); przed publikacją obejrzyj klatkę KAŻDEJ sceny (nie tylko pierwszej), za długi wiersz → mniejsza czcionka albo zawinięcie.
- Klucz: tekst-poza-kadrem
- Powtórzenia: 1
- Status: nowy
