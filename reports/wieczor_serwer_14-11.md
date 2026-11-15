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


## ⚠️ OTWARTE 14.11 21:03
- Zapora Contabo „Hexa-tylko-Tailscale” WYŁĄCZONA tymczasowo → włączyć z powrotem po naprawie Tailscale na serwerze (Network → Firewall → Enable).
- Hasło Administratora zresetowane przez Contabo (szef ma je w Proton Pass). Logowanie: vmi3737651\Administrator.
- ✅ 21:07 NAPRAWIONE: serwer wstał po twardym restarcie (stop/start w panelu), szef zalogowany przez RDP, Tailscale działa, zapora Contabo z powrotem ACTIVE (publiczny 3389 zamknięty, Tailscale 3389 otwarty). Wszystkie boty/panel/MT5 chodzą (START_WSZYSTKO OK). Brak tylko IB Gateway (wymaga logowania szefa → krok 10).
- Autostart po zalogowaniu działa; problem: po restarcie bez logowania nic nie startuje → krok 9 (autologon) priorytet.

## 🔴 PRIORYTET 1 (szef 15.11 01:44: „musimy to zabezpieczyć”)
Serwer 2x nie wrócił sam po restarcie (14.11 ~19:52 po resecie hasła; 14.11 ~22:53 po aktualizacjach – offline w Tailscale >2 h, Strażnik alarm 01:41). Wieczorem pomógł dopiero twardy stop/start w panelu Contabo.
Plan przy laptopie: 1) podgląd TightVNC (co na ekranie) 2) twardy stop/start 3) przyczyna: dziennik System (zdarzenia 41/6008, usługi przy starcie, Tailscale), sterownik sieci 4) autologowanie + START_WSZYSTKO przy logowaniu, Tailscale jako usługa automatyczna z odzyskiwaniem 5) test: restart i sprawdzenie, że wszystko wstaje samo w <10 min.

## ✅ 15.11 03:55 PRZYCZYNA ZNALEZIONA + CZĘŚĆ 1 NAPRAWIONA
- Serwer po aktualizacjach wstał normalnie o 23:00 (zdarzenie 6005) – nie wisiał. Tailscale był „offline”, bo działał w trybie przypiętym do zalogowanego użytkownika: bez logowania na pulpit = brak Tailscale = brak dostępu (a publiczny RDP zamknięty zaporą). Do tego Desktop Commander i boty startują dopiero po zalogowaniu.
- Naprawa 1 (03:56): `tailscale set --unattended=true` → ForceDaemon=true. Tailscale łączy się teraz zaraz po starcie Windows, bez logowania.
- Do zrobienia (część 2): start botów + Desktop Commander bez logowania (autologowanie – hasło wpisuje szef, albo zadania przy starcie systemu) i test restartu.
- Aktualizacje zainstalowane: KB5122871 (2026-09 Security), KB5127690 (.NET). 03:02 twardy restart (zdarzenie 41) – bez skutków.
- ✅ 15.11 03:58 CZĘŚĆ 2: autologowanie Windows (Sysinternals Autologon, podpis Microsoft, hasło wpisał szef, zaszyfrowane w LSA) + Autostart (START_WSZYSTKO.lnk, DC_Remote.vbs w Startup) + ZABLOKUJ_EKRAN.cmd (blokada ekranu 2 min po starcie, procesy działają dalej).
- ✅ 04:00 TEST RESTARTU (reboot z panelu Contabo): start 04:00:38, autologowanie 04:00, Tailscale + Claude połączeni ~2,5 min po restarcie, MT5 + boty działają. SERWER WSTAJE SAM. Pozostaje tylko IB Gateway (logowanie szefa / IBC).

## ✅ 15.11 04:28 KOPIA ZAPASOWA POZA SERWEREM (krok 16)
- Serwer: zadanie „Hexa Kopia dzienna” 03:30 → C:\Hexa\narzedzia\kopia\kopia_dzienna.ps1: Hexa + Claude-telefon + kraken-boty + profile/EA MT5 → ZIP (~800 MB, 21 tys. plików), BEZ sekretów (sejf, .env, klucze, adbkey), bez venv/logów/wideo; 3 ostatnie lokalnie; wysyłka Taildrop na laptop.
- Laptop: Taildrop zapisuje do Pobranych → zadanie „Odbierz kopie serwera” (05:00 + przy logowaniu) przenosi do C:\Users\ktrut\KopieSerwera, trzyma 3 ostatnie.
- Test 04:28: ZIP 804 MB doszedł na laptop, 21 471 plików, w środku tylko adbkey.pub (publiczny – OK).
- Zasada 3 kopii: serwer + laptop + snapshot Contabo (ręcznie przed dużymi zmianami).

## 🔎 PRZEGLĄD LAPTOPA (tylko odczyt, NIC nie usunięte – czeka na „tak” szefa)
Wolne 75 GB z 238 GB. Najwięksi kandydaci do sprzątnięcia:
- Documents\Codex\2026-10-19\…\Heksa-pelna-kopia-20261019 – 20 GB (stara pełna kopia z 19.10)
- LivePortrait (folder 9,5 GB) + Downloads\LivePortrait…zip 5 GB
- .gradle 5,8 GB (cache budowania Androida – ORB budujemy na serwerze)
- stare testy botów: NexScalperDemo 5,4 GB, Nex_Github_Gold_Tests 2 GB, NexRSIDemo 0,7 GB, OpenSourceBotResearch 0,7 GB
- .cache 4 GB, .codex 1,3 GB, instalatory w Pobranych (~0,7 GB)
Razem ~55 GB do odzyskania. Przed usunięciem: sprawdzić, czy coś z tych folderów nie jest jedyną kopią (porównać z serwerem).

## Snapshot (15.11)
- Stary snapshot 2L84U (14.11, sprzed napraw) usunięty.
- Nowy snapshot **po-naprawach-15-11**: autostart, Tailscale unattended, zapora, aktualizacje, Tarcza, Kraken Pro. Auto-usunięcie po ~30 dniach (Contabo), limit 1 snapshot.
- Auto Backup w Contabo: włączony.
