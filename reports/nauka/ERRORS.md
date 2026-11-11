# ERRORS

(wpisy na dole, format w README.md)

---

### E-20261111-01 [skaner] Restart skanera: nie uruchamiaj drugiej kopii
- Co się stało: po Stop-Process pythona Mózg sam odpalił skaner, a pętla START_SKANER_DZIENNY.bat po 60 s podniosła drugi – przez ~1 min działały dwa skanery.
- Wniosek / zasada: skaner dzienny na serwerze ma własną pętlę w .bat – do restartu wystarczy zabić sam proces python z skaner_dzienny.py i poczekać ~60 s; NIGDY nie uruchamiać go ręcznie obok pętli.
- Klucz: restart-skanera-podwojny
- Powtórzenia: 1
- Status: nowy
