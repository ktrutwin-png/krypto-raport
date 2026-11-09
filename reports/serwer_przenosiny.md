# Przenosiny na serwer – stan i dalsze kroki (Mózg, 9.11.2026 18:45)

Serwer: Contabo, Windows Server 2025, nazwa urządzenia vmi3737651 (Tailscale 100.67.199.43). Laptop: DESKTOP-20N25SR.

## Zrobione 9.11
- MT5 na serwerze: nowe konto demo 10013544792 (MetaQuotes-Demo, Hedge, 3000 USD, 1:25), Algo Trading włączony.
- Boty Hexa (magic 830083) i Turbo (830099): C:\Users\ktrut\Claude-telefon\boty_poprawki\launch_demo_625.py -> konto 10013544792, state_demo_10013544792; corrected\hexa_bot.py i hexa_turbo.py max_volume=0.01 (szef: „wdróż” 9.11 18:05). Kopie: *.bak_114989625.
- Uwaga: paczka2.tgz nie zawierała podfolderów boty_poprawki (corrected itd.) – doniesione osobno (corrected.tgz). Inne foldery sprawdzone skryptem srvchk.py: OK.
- IB Gateway (paper) na serwerze zalogowany, Lock and Exit = Auto restart 23:45 (logowanie raz w tygodniu). Read-Only API odznaczył szef.
- START_WSZYSTKO uruchomił szef 18:24: działają HEXA BOT, HEXA TURBO, Skaner dzienny, IB SKANER, Kraken Donch4hBTC i Mom1dBTC (dry-run), Panel Szefa, wykres.
- Laptop: wszystkie boty/skanery/panel/MT5/IB zatrzymane 18:19 (nic nie chodzi podwójnie). Aplikacja Claude na laptopie zamknięta 18:40.

## Do zrobienia (szef: „wszystko, czym zarządzasz, ma być na serwerze”)
1. Przepiąć zadania harmonogramu powiązane z laptopem (bound_device DESKTOP-20N25SR: Raport 22:00, Sekretarz, Analityk, Inspektor, Mechanik, przypomnienia itd.) na urządzenie vmi3737651 – list_triggers, update_trigger. Ścieżki C:\Users\ktrut\... są na serwerze takie same.
2. Zadania, które czytają laptop przez Remote_Desktop_Commander (Nauczyciel, Inspektor…): na serwerze zainstalować Desktop Commander Remote albo przepisać je na urządzenie vmi3737651.
3. Raport 22:00: ma liczyć nowe konto 10013544792 (stare 114989625 już nie handluje).
4. ORB/adb (telefon) – narzędzia budowania są na laptopie; przenieść później.
5. Czyszczenie laptopa DOPIERO gdy serwer działa dobę: pokazać szefowi listę, nic nie usuwać bez jego „tak”.
Zasady bez zmian: konta demo/paper, nie uruchamiam botów handlujących sam, nie ruszam ręcznych pozycji szefa (magic 0), cisza w tygodniu, książka (ksiazka) poufna.

## Postęp 9.11 ~19:00 (Mózg)
- Sesja Claude połączona z serwerem vmi3737651 (device bridge działa: Desktop Commander lokalnie, PowerShell).
- Pliki na serwerze OK: C:\Users\ktrut\Claude-telefon (boty_poprawki, panel_tg, trading, ib…), kraken-boty (bazy Donch4hBTC/Mom1dBTC żyją, zapis 18:25).
- Ustalenie: większość agentów (Inspektor, Mechanik, Sekretarz, Handlowiec, Pisarz, Nauczyciel, Zwiadowca, rozliczenie 7.12) to zadania CHMUROWE, które sięgają po laptop przez konektor Remote_Desktop_Commander. Ten konektor widzi dziś tylko DESKTOP-20N25SR (offline). Klucz do pkt 1–2: dodać serwer jako urządzenie w Remote_Desktop_Commander (npx @wonderwhy-er/desktop-commander@0.3.1 remote na serwerze + zatwierdzenie w przeglądarce). Próba instalacji przez Mózg zablokowana przez zabezpieczenia – czeka na decyzję szefa.
- update_trigger nie zmienia przypisanego komputera; zadania z bound_device = laptop (np. przypomnienie 10.11 07:17) trzeba przepiąć w aplikacji Claude na serwerze („Require this computer”) albo utworzyć na nowo z serwerem.
- 19:00 Desktop Commander Remote ZAINSTALOWANY na serwerze (C:\dcremote, start.cmd, log remote.log); serwer zweryfikowany i Online w Remote_Desktop_Commander (device 0b708a8f…). Test: agenci chmurowi czytają C:\Users\ktrut\Claude-telefon\trading – wykonane na vmi3737651. Pkt 1–2 dla zadań chmurowych załatwione (te same ścieżki).
- Brak autostartu po restarcie serwera (zadanie Windows DC_Remote zablokowane przez zabezpieczenia – czeka na „autostart” szefa). Po restarcie serwera trzeba uruchomić C:\dcremote\start.cmd.
- Skrypty raportu (raport_wieczor.py, raport_wieczorny.py) biorą konto zalogowane w MT5 → na serwerze liczą 10013544792.
- 19:05 Autostart: Startup\DC_Remote.vbs (Administrator) – rusza po zalogowaniu Administratora. Serwer nie ma automatycznego logowania: po restarcie trzeba się raz zalogować (RDP), dotyczy też botów i aplikacji Claude.
- 19:20 Przegląd zadań: agenci (Inspektor, Mechanik, Sekretarz, Handlowiec, Pisarz, Nauczyciel, Zwiadowca, Skanery, Analityk, Raport 22:00, rozliczenie 7.12) to zadania chmurowe – przez Remote_Desktop_Commander trafiają teraz na serwer (te same ścieżki). Jedyne zadanie przypięte do laptopa (przypomnienie 10.11 07:17, trig_012zov…) wyłączone i zastąpione chmurowym trig_019iF7ekkdf4f6mUYg4eopUy. Pkt 1–3 zamknięte.
- 19:46 Telegram na serwerze: Python nie ufał certyfikatowi (świeży Windows bez korzenia GoDaddy G2) – po pobraniu korzenia restart Panelu Szefa i skanera dziennego; panel odpowiada (szef potwierdził 19:50). Przy nowym serwerze: najpierw test https z Pythona.
