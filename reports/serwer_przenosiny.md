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
