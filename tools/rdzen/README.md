
## Stan 16.11.2026
- Rdzeń działa na serwerze (100.67.199.43:8770, tylko Tailscale). Test: zły token → 403, dobry token + fałszywy klucz → 502 (Anthropic odrzuca), telefon widzi port.
- APK z rdzeniem: `C:\Hexa\orb\ORB_rdzen.apk` (budowa: `C:\Hexa\orb\build_rdzen.ps1`, kopia orb-src → orb-rdzen; oryginał nietknięty). Wgranie tylko po słowie szefa: `build_rdzen.ps1 -Install`.
- Autostart: rejestracja zadania „Hexa Rdzen” wymaga PowerShella jako administrator (sesja MCP nie ma uprawnień). Krok dla szefa – patrz niżej.
- Gdy rdzeń nie odpowiada, ORB sam wraca do starego trybu (bezpośrednio do API).
