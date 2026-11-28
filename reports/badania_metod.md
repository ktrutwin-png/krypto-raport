# Badania metod (agent Badacz)


## KOLEJKA OD SZEFA (do zrobienia przy najbliÅ¼szym przebiegu)
- 2026-11-28: KRONOS â€“ model AI do prognoz Å›wiec. Oficjalne repo TYLKO github.com/shiyu-coder/Kronos (MIT, praca AAAI/Tsinghua); forkÃ³w innych uÅ¼ytkownikÃ³w nie uÅ¼ywaÄ‡. Po przeglÄ…dzie bezpieczeÅ„stwa: osobny venv C:\Hexa\quant\kronos\.venv (nigdy Python botÃ³w), model NeoQuasar/Kronos-small z Hugging Face (CPU). Test: XAUUSD M15, min. 1 rok, kroczÄ…co bez zaglÄ…dania w przyszÅ‚oÅ›Ä‡ â€“ czy kierunek na 1â€“4 Å›wiece trafia istotnie >50% i czy jako FILTR (wejÅ›cie tylko gdy Kronos zgadza siÄ™ z sygnaÅ‚em) podnosi profit factor innych metod po kosztach. Brak przewagi = odrzuciÄ‡ z uzasadnieniem.
- 2026-11-28: pary zÅ‚otoâ€“srebro (stosunek XAU/XAG, powrÃ³t do Å›redniej) â€“ pomysÅ‚ z repo je-suis-tm/quant-trading (tylko do czytania).
- 2026-11-28: zrodla pomyslow (tylko do czytania, nie instalowac): paperswithbacktest/awesome-systematic-trading (strategie z publikacjami i backtestami - szukaj takich na zloto/srebro/towary/FX), wilsonfreitas/awesome-quant (lista narzedzi), stefan-jansen/machine-learning-for-trading (cechy do modeli ML/Kronos).
- 2026-11-28 01:00: od szefa - HKUDS/Vibe-Trading (agent AI: strategie z opisu, backtesty, eksport do MetaTradera) - tylko do przejrzenia pomyslow i sprawdzenia eksportu MT5, bez kluczy i bez instalacji na produkcji. Odrzucone: Gainium, OctoBot, Jesse, Passivbot, AutoHedge (krypto, mamy Freqtrade), Fincept (za ciezki na serwer), reszta nie o tradingu. heygen-com/hyperframes - zapas dla kino.py, gdyby nasz render nie wystarczal.

## 2026-11-28 - Kronos-small (foundation model swiec) na XAUUSD H1
Trafnosc kierunku: 1h 50,8% | 4h 51,2% | 12h 55,2% (rzut moneta = 50%)
Korelacja prognozy z ruchem: 0,05 / -0,02 / 0,08 (praktycznie zero)
PnL na uncje bez kosztow: 1h -67 $ | 4h -1 $ | 12h +131 $ (prosta regula momentum na 12h: +860 $)

Wniosek: na zlocie H1 Kronos nie ma przewagi. 1h i 4h = rzut moneta. 12h 55% wyglada lepiej,
ale okna sie nakladaja (krok 6h, horyzont 12h), wiec realnie ok. 125 niezaleznych prob -
to w granicach przypadku; prosta regula momentum zarobila w tym okresie wiecej.
WERDYKT: NIE bierzemy na zloto H1. Dalej: ten sam test na srebrze (XAGUSD) i Bitcoinie (dane Kraken),
ewentualnie zloto D1.
Pliki: C:\Hexa\lab\kronos (test_xau.py, wyniki.json, wyniki_okna.csv). Inferencja CPU: ~1h40 na 250 okien x3 scenariusze.

