# Wieczór serwera — 14.11.2026 (pełna lista, nic nie pomijamy)
Zasada: krok po kroku, jeden naraz. Szef wpisuje hasła i zatwierdza zmiany zabezpieczeń; Claude prowadzi, sprawdza i zapisuje.

## A. Bezpieczeństwo (najpierw)
1. [ ] Migawka Contabo PRZED zmianami (szef: panel Contabo → Snapshot) — punkt powrotu.
2. [ ] Aktualizacje Windows (ostatnia: 09.2024) → restart serwera → sprawdzenie, że boty, panel, MT5, IB wstały.
3. [ ] Zapis logowań (audyt udanych i nieudanych) → Tarcza widzi próby.
4. [ ] Pulpit zdalny TYLKO przez Tailscale (najpierw test połączenia przez Tailscale, dopiero potem zamknięcie dla internetu).
5. [ ] Zamknąć od internetu porty 445 (SMB) i 5985/5986 (WinRM).
6. [ ] Konto cloudbase-init — sprawdzić, czy potrzebne; jeśli nie → wyłączyć.
7. [ ] Klucz adb (telefon) — dostęp tylko administrator.
8. [ ] Tarcza → test: lampka zielona.

## B. Serwer pracuje sam
9. [ ] Autologowanie + autostart START_WSZYSTKO.ps1 po restarcie (szef wpisuje hasło).
10. [ ] IB Gateway: automatyczne logowanie na demo (IBC) — szef wpisuje login/hasło.
11. [ ] Test: restart serwera → wszystko wstaje samo bez szefa.
12. [ ] Logi Hexa/Turbo — potwierdzić, że cisza w weekend = rynek zamknięty (nie awaria).

## C. Laptop bez firmy
13. [ ] Audyt laptopa: lista wszystkiego, co firmowe.
14. [ ] Przenieść na serwer to, czego tam brak (strażnik telefonu, kompilacja MQL5, inne).
15. [ ] Czyszczenie laptopa — tylko z listy i po „tak” szefa.

## D. Zasada 3 kopii
16. [ ] Kopia nocna szyfrowana poza serwerem (rclone → wybrany dysk w chmurze; szef loguje się raz).
17. [ ] Migawka Contabo — regularnie (szef ustawia w panelu, jeśli dostępne).
18. [ ] Test odtworzenia jednego pliku z kopii (hash zgodny).

## E. Na koniec
19. [ ] Raport 22:00 z lampką Tarczy — sprawdzić, że przyszedł.
20. [ ] Wpis do dziennika zespołu + aktualizacja planów.
