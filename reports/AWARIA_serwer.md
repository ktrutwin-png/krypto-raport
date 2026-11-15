# 🛟 AWARIA SERWERA – jak wrócić w 3 minuty (szef 15.11: „jednym kliknięciem, nie godzinami”)

## Co działa samo (sprawdzone testem 15.11 04:00)
- Restart serwera → Windows loguje się sam (Autologon, hasło zaszyfrowane) → Tailscale łączy się bez logowania (unattended) → START_WSZYSTKO uruchamia MT5, boty, panel, Krakena, Kraken Pro, Claude → ekran blokuje się po 2 min. Czas: ~2,5 min.
- Strażnik co godzinę: serwer milczy → push do szefa.
- Kopia: codziennie 03:30 serwer → laptop (C:\Users\ktrut\KopieSerwera), 3 dni wstecz. Bez sekretów.

## Jeśli serwer nie odpowiada – JEDEN krok dla szefa
1. Napisz do Claude „serwer leży”. Claude sam: sprawdza Tailscale → robi Reboot w panelu Contabo (przeglądarka szefa, już zalogowana) → czeka 3 min → sprawdza.
2. Tylko jeśli Contabo wyloguje: szef loguje się na my.contabo.com (hasło + potwierdzenie na telefonie) – reszta jak wyżej.
3. Ostateczność: Contabo → Snapshots → przywrócenie snapshotu.

## Czego NIE robić
- Nie resetować hasła w Contabo bez potrzeby (14.11 zerwało dostęp na 8 h).
- Nie wyłączać zapory „Hexa-tylko-Tailscale” (14.11: 8 min bez zapory = 13 prób bota).
- Hasła wpisuje tylko szef; kody/klucze tylko w sejfie i Proton Pass.

## Do zrobienia (żeby było w pełni automatycznie)
- Klucz API Contabo (szef wpisuje do sejfu) → Strażnik sam robi Reboot, gdy serwer milczy >15 min.
- IB Gateway: auto-logowanie (IBC) po naprawie logowania IBKR.
