# Laboratorium – dziennik (tylko demo / paper / virtual)

Zasady: co noc przegląd → wyłączenie słabych (PF < 0,9 po ~20 transakcjach albo −30% kapitału) → 1–3 nowe pomysły → backtest z kosztami (nauka 70% / sprawdzian 30%) → na demo idą te ze sprawdzianem PF ≥ 0,95.
Kod: `C:\Hexa\lab` (silnik `lab_silnik.py`, boty `boty\*.py`, start `START_LAB.ps1` + `lista.json`, logi `logi\`, stan `stan\`).

---

## 2026-11-18 (noc 1 – start laboratorium)

**Przegląd poprzednich dni:** brak – pierwsza noc, nic do wyłączenia.

**Budowa:**
- `C:\Hexa\lab` utworzony: wspólny silnik strategii (te same reguły w backteście i na żywo), bot MT5 (`lab_mt5.py`: przed każdym zleceniem login 5058971085 + tryb DEMO, magic 830200–830299, łączny depozyt lab ≤ 30% kapitału, konto hedging – pozycji Hexy/Turbo/Indeksów nie dotyka), Kraken na sucho (`lab_kraken.py`: 500 € wirtualne/bot, dźwignia do 10x, opłaty Kraken Pro), IBKR paper (`lab_ib.py`: clientId 50–59, konto „DU”, pary wolne od szybki/warianty, OCA TP+SL).
- Dopisany wpis „Laboratorium” do `START_WSZYSTKO.ps1` (wzorzec `Hexa\\lab\\boty`, start przez START_LAB.ps1) i do `roj_straz.py` (wzorzec `Hexa\lab\boty`); kopie `.bak_lab_20261118`; strażnik zrestartowany.
- Raport 22:00: `zbierz_dzis.py` liczy teraz osobno Laboratorium → pole `wiersz_laboratorium` („Laboratorium (demo)”, zysk/strata w €) w `zbierz_out.json` (kopia `zbierz_dzis.py.bak_20261118`, test uruchomienia ok).

**Backtest (runda 1, 1140 zestawów; MT5: M15 od 02–04.2025, H1 od 2024; Kraken 15m od 19.05.2026):**

| Pomysł | Rynek | Nauka PF (n) | Sprawdzian PF (n) | Decyzja |
|---|---|---|---|---|
| Londyn – wybicie z zakresu Azji, SL środek, TP 2R | XAUUSD M15 | 1,21 (209) | **2,19 (90)** | ✅ demo |
| Donchian 55 H1, SL 2,5 ATR / TP 3 ATR | XAGUSD H1 | 1,40 (240) | **1,50 (94)** | ✅ demo |
| Kontra – przeciw tłumowi po świecy ≥3×ATR, TP 61,8% | EURUSD / USDJPY M15 | 1,25 / 1,21 | **1,32 (77) / 1,36 (89)** | ✅ demo |
| RSI(2) + EMA200, SL 3 / TP 2 ATR | USDJPY / GBPUSD M15 | 1,10 / 0,93 | **1,37 (240) / 1,10 (252)** | ✅ demo |
| RSI(2) + EMA200 | AUDUSD M15 (IBKR) | 1,00 (563) | **1,22 (237)** | ✅ IBKR paper |
| Kontra na złocie | XAUUSD H1 | 1,66 | 0,59 | ❌ przeuczone |
| Donchian | US30 H1 | 1,19 | 0,51 | ❌ |
| Wszystko na krypto M15/H1 (opłaty 0,75%) | BTC/ETH/XRP | ≤ 0,97 | ≤ 0,55 | ❌ |

**Lekcje:**
- Krypto na Krakenie: krótkie TF są martwe – 0,75% kosztów w obie strony zjada każdą przewagę (kontra M15 na BTC: PF 0,00). Ratunek: wejścia LIMIT (maker, ~0,52%) i H4.
- Runda 3 (Kraken, maker, H4): RSI(2) + EMA200, SL 4 / TP 5 ATR – BTC nauka 1,61 → spr **1,31 (n9)**, XRP 2,46 → **1,60 (n11)**. Mała próba – puszczone odważnie, demo jest od nauki.
- Kontra D1 (pod eToro, zarządzane raz na noc): tylko GBPUSD przeszło (nauka 1,26 n16 → spr 2,16 n7). Reszta ≤ 0,54.
- Indeksy US500/US30 na koncie botów mają handel wyłączony (trade_mode 0) – pominięte.

**Uruchomione na demo (6 botów + 1 strategia eToro):** LAB_Londyn_XAU (830201), LAB_Donchian_XAG (830202), LAB_Kontra_FX (830203), LAB_RSI2_FX (830204), LAB_KR_RSI2_H4 (Kraken na sucho), LAB_IB_RSI2_AUD (IBKR paper, clientId 50). Ryzyko MT5: 0,4–0,5% kapitału na transakcję (lot liczony od SL).

**eToro (konto DEMO, odczyt `account=demo` potwierdzony):** strategia „Kontra D1” na GBPUSD – dziś brak sygnału (świeca 17.11: zakres 0,8×ATR < 1,8×ATR), 0 transakcji. Pozycje laboratorium zapisuję w `C:\Hexa\lab\etoro_pozycje.json` (pusto).

**Zablokowane (nie obchodzę):**
- IBKR: IB Gateway odpowiada bardzo wolno – połączenie trwa ~30 s, potem timeout na pozycjach/zleceniach/kwalifikacji kontraktu; bot `LAB_IB_RSI2_AUD` kończy się TimeoutError i sam ponawia co 60 s. Bot szybki_fx też milczy od 17.11 06:12. Gateway nie ruszałem – do sprawdzenia przez Inspektora/Mechanika.
- Dane akcji pod eToro (Stooq zwraca puste pliki, Twelve Data limit 8/min) – backtest „kontra tygodnia na akcjach” odłożony.

**Najlepszy na start (backtest):** LAB_Londyn_XAU – sprawdzian PF 2,19, +33 R na 90 transakcjach.

---

## 2026-11-19 (noc 2)

**Przegląd (od startu 18.11):**
- MT5 (konto demo 5058971085, trade_mode DEMO potwierdzony): **2 zamknięte, obie na plus, razem +514,13 $** – LAB_Londyn_XAU short złota, wyjście czasowe +219,38 $; LAB_Donchian_XAG short srebra +294,75 $ (TP). Otwarta: Donchian_XAG short 0,06 lot @ 45,221 (−88,80 $).
- Kraken na sucho: LAB_KR_RSI2_H4 trzyma SHORT XRP/EUR @ 0,91141 (100 € × 5); jeden błąd SSL Krakena 18.11 15:08 – bot sam wrócił, stan aktualny.
- IBKR paper: Gateway znów odpowiada – LAB_IB_RSI2_AUD połączony od 18.11 20:53 (konto DUR…), czeka na sygnał.
- eToro DEMO (odczyt `account: demo` potwierdzony): Kontra D1 GBPUSD – brak sygnału (świeca 18.11: zakres 1,03×ATR < 1,8×ATR). Pozycji lab: 0.
- LAB_RSI2_FX: 1 sygnał USDJPY odrzucony przez limit 30% depozytu (zajęte 1522 + 600 > 1611 $) – limit działa; depozyt srebra (Donchian) jest ciężki.
- **Wyłączone: nic** (za mało transakcji do oceny; próg ~20).

**Kreacja – runda 4 (2952 zestawy, świeże dane MT5, koszty: spread świecy; Kraken 0,52% maker):**

| Pomysł | Rynek | Nauka PF (n) | Sprawdzian PF (n) | Decyzja |
|---|---|---|---|---|
| **Luka poniedziałkowa** – po weekendzie gra na zamknięcie luki ≥0,6 ATR, TP 50% luki, SL 2× | EURUSD / GBPUSD / USDJPY / AUDUSD H1 | 2,07 / 3,36 / 1,40 / 1,16 | **4,97 (26) / 2,71 (22) / 99 (18) / 1,87 (27)** | ✅ demo `LAB_Luka_FX` 830205 |
| **Konsolidacja** – wybicie z 12 świec H1 ≤ 2× ATR50, SL pół pudełka, TP 3× | USDJPY / EURUSD H1 | 1,93 (98) / 1,30 (189) | **1,78 (68) / 1,69 (72)** | ✅ demo `LAB_Kons_H1` 830206 |
| **NY fade** – przeciw pierwszej godzinie Nowego Jorku (≥2,5 ATR), TP 61,8% | XAUUSD / EURUSD / GBPUSD M15 | 2,60 / 1,35 / 1,10 | **1,44 (30) / 1,58 (19) / 1,57 (18)** | ✅ demo `LAB_NYFade` 830207 |
| NY fade | USDJPY / AUDUSD / XAGUSD | 0,61 / 0,99 / 2,02 | 0,69 / 0,96 / 1,06 | ❌ pominięte |
| Konsolidacja M15 | wszystkie | ≤ 1,35 | ≤ 1,30, GBP/AUD/XAG/XAU < 0,9 | ❌ szum |
| Konsolidacja na krypto H1/H4 (Kraken) | BTC/ETH/XRP | ≤ 1,82 | ≤ 0,80 | ❌ opłaty znów zabijają |

**Lekcje:**
- Luka weekendowa na FX zamyka się częściej, niż się wydaje (spr. wr 85–100%), ale to profil „dużo małych wygranych, rzadka duża strata” (TP 0,5 / SL 2) – suma R na nauce bywała ujemna mimo PF > 1. Obserwować, czy jedna strata nie zjada miesiąca.
- Konsolidacja działa tylko przy bardzo ciasnym pudełku (kz 2,0); kz 3–4 to już szum – parametr wrażliwy, ryzyko przeuczenia.
- NY fade działa na złocie i EUR/GBP, nie na jenie – jen w otwarciu NY częściej kontynuuje ruch.
- Krypto na Krakenie: trzecia noc z rzędu potwierdza – krótkie TF i wybicia tracą na opłatach; zostaje tylko H4 RSI2 z wejściem maker.

**Uruchomione dziś:** LAB_Luka_FX (830205), LAB_Kons_H1 (830206), LAB_NYFade (830207) – ryzyko 0,4% na transakcję, test `--raz` ok, procesy żyją, logi bez błędów. Razem aktywnych: 9/10.

**Zablokowane / uwagi:** brak nowych blokad. Dane akcji pod eToro nadal niedostępne (odłożone).

**Najlepszy (na żywo):** LAB_Donchian_XAG +294,75 $ (1 zamknięta); w backteście nowych – LAB_Kons_H1 USDJPY (+40 R na 68 transakcjach sprawdzianu).

---

## 2026-11-20 (noc 3) – priorytet szefa: M8

**Przegląd (konto demo botów 5058971085, trade_mode DEMO potwierdzony):**
- MT5 lab: **4 zamknięte, razem +848,40 $** – Donchian_XAG +294,75 $ i +357,78 $ (2/2, TP), Londyn_XAU +219,38 $, Kons_H1 USDJPY −23,51 $ (pierwsza strata). Otwarta: Donchian_XAG SHORT srebra @ 42,542 (+92,75 $).
- **Problem nocy:** limit 30% depozytu laboratorium zatyka boty – Kontra_FX, RSI2_FX, NYFade i Kons_H1 (EURUSD) dostawały „limit laboratorium 30% – pomijam”. Powód: lot liczony od ryzyka 0,4–0,5% przy ciasnym SL daje duże loty (NYFade na złocie chciał 7373 $ depozytu). Lekcja: przy wielu botach na jednym koncie ryzyko trzeba liczyć też od depozytu, nie tylko od SL – do poprawy jutro (cap lota).
- Kraken na sucho: KR_RSI2_H4 żyje (stan 20.11 01:31), SHORT XRP bez zmian.
- IBKR paper: **IB Gateway nie słucha na 127.0.0.1:4002** (ConnectionRefused co minutę od 19.11 rano) – nie restartuję (zakaz), zgłoszone już przez Inspektora (Z032).
- eToro DEMO: Kontra D1 GBPUSD – brak sygnału.
- **Wyłączone: nic** (żaden bot nie ma ~20 transakcji).

**M8 – Hexa i Turbo na M15/M30/H1/H4/D1, wszystkie platformy (krok 1–3):**
- Napisany backtest `C:\Hexa\lab\m8\m8_bt.py` – 3 rodziny sygnałów 1:1 z hexa_bot.py/hexa_turbo.py (ASIA, DCH, D15) przeniesione na interwał X, koszty każdej platformy, nauka 70% / sprawdzian 30%. 150 przebiegów + 100 testów TP. Pełna tabela: `reports/lab_tabela.md` (sekcja M8).
- **Złoto to dom Hexy i Turby:** na każdym interwale sprawdzian PF ≥ 1 (MT5: M15 1,01 · M30 1,28 · H1 1,37 · H4 1,59 · D1 2,35), to samo na IBKR i eToro (inne koszty, prawie ten sam wynik). Srebro też na plus na wszystkich TF (1,04–1,99).
- **Forex słabo:** EURUSD ~1,0, GBPUSD tylko H4 (1,03), USDJPY tylko H1 Turbo (1,00), AUDUSD wszędzie < 0,9 ❌.
- **Krypto martwe na krótkich TF:** koszty 0,75% (Kraken) / 2% (eToro) są większe niż SL z ATR na M15–H4 → PF 0,0–0,6. Przeżywa tylko D1: Kraken BTC 1,02 (n47), ETH 1,09 (n42), XRP 1,18 (n53, ale nauka 0,38); eToro BTC D1 0,69 ❌.
- **TP (dodatkowe zadanie szefa):** TP 1R (obecny od 10.11) to najsłabszy wariant na każdym interwale; TP 2–3R podnosi PF (H1 Hexa 1,37 → 1,47, H4 1,59 → 1,80–2,00, D1 2,35 → 4,80). Drugie wejście z własnym SL: +30–80% ΣR, ale ~1,5× większe obsunięcie. Do decyzji szefa – w Hexie/Turbo nic nie zmieniam.
- **Uczciwie:** sprawdzian złota trafił na silny trend 2026, a na nauce złoto miało PF ~1,0 (M30/H1 < 1). To może być „reżim”, nie przewaga – rozstrzygnie demo.

**Uruchomione dziś (krok 2):** `LAB_M8_HexaTurbo` – jeden proces, 14 wariantów (magic 830210–830223, 0,01 lota jak oryginał, oryginalne Hexa 830083 / Turbo 830099 nietknięte), test `--raz` ok, proces żyje. Od razu weszło 12 pozycji SHORT (złoto i srebro wybijają dołem) – reszta odrzucona limitem 30%. eToro DEMO: `LAB_ET_M8_XAU_D1` – SHORT GOLD @ 3563,87, SL 3805, TP 3334 (500 $ × 5, poz. 3646949765, zapisane w etoro_pozycje.json). Aktywnych botów: 10/10.

**Zablokowane / czeka:** IBKR (Gateway nie działa) – warianty złota M30/H1/H4/D1 na IBKR czekają; Kraken BTC/ETH D1 – czekają na wolny slot (limit 10 botów).

**Najlepszy (na żywo):** LAB_Donchian_XAG +652,53 $ (2/2). W M8 najlepszy w backteście: Hexa/Turbo D1 na złocie (PF 2,35, DD 5R), a z największym zyskiem w R – M30/H1 na złocie (+134–139R na sprawdzianie).

---

## 2026-11-21 (noc 4) – M8 na wszystkich platformach

**Przegląd (konto demo botów 5058971085, trade_mode DEMO potwierdzony; Hexa/Turbo/Indeksy bez otwartych pozycji, nietknięte):**
- MT5 lab: **19 zamkniętych, razem +1148,58 $**. Gwiazda: LAB_Donchian_XAG 3/3 (+294,75 / +357,78 / +380,00 $ = +1032,53 $), znów SHORT srebra od 20.11. RSI2_FX pierwsza transakcja +16,20 $ (GBPUSD).
- **M8 na MT5 (pierwsza doba): 13 zamkniętych, −96,02 $, PF 0,68.** Straty prawie w całości z M15/M30 na złocie i M30 na srebrze – 20.11 o 10:02 jedna świeca wybiła 4 warianty naraz. H4/D1 jeszcze nic nie zamknęły, ale 7 pozycji H4/D1 jest na plusie (~+43 $ każda złota, +90 $ srebro H4). Za wcześnie na werdykt (próg ~20 transakcji na wariant).
- Kraken na sucho: KR_RSI2_H4 trzyma SHORT XRP; pojedynczy błąd SSL Krakena, bot sam wrócił.
- IBKR paper: **IB Gateway znów słucha na 4002 (od 20.11 22:16)** – LAB_IB_RSI2_AUD połączony (DUR…).
- eToro DEMO (`account: demo` w odpowiedzi): LAB_ET_M8_XAU_D1 SHORT GOLD @ 3563,87 → 3544,40, +13,66 $ (SL 3805 / TP 3334 bez zmian). Kontra D1 GBPUSD – brak sygnału.
- **Wyłączone (lekcja): nic.** **Zawieszone:** LAB_Kontra_FX i LAB_NYFade (pliki `_off`, aktywny=false) – 0 transakcji w 2–3 dni, bo lot z ryzyka % przy ciasnym SL przekraczał limit 30%; to nie werdykt o strategii, tylko oddanie slotów priorytetowi M8.

**M8 – dziś (krok 2 domknięty na wszystkich platformach):**
- 🆕 `LAB_IB_M8_XAU` – IBKR paper, clientId 51, XAUUSD (CMDTY/SMART, 1 oz = 0,01 lota): Hexa H1 / H4 / D1 (spr PF IBKR 1,35 / 1,58 / 2,34). Sygnały tym samym kodem m8_bt.py, świece MIDPOINT z IB, OCA TP/SL GTC, BE dla D15. Test `--raz`: kontrakt i 8 lat D1 pobrane; sygnał D1 DCH SHORT – zlecenie anulowane (sobota, rynek zamknięty) → dodałem ponawianie co 15 min tej samej świecy.
- 🆕 `LAB_KR_M8_D1` – Kraken na sucho, BTC/ETH/XRP D1 (500 € wirt./para, ryzyko 2%, max 5x). Sygnały na świecach Binance (potrzeba 2000+ dni do trendu 16×D1), wykonanie na cenach Krakena EUR. Od razu weszły: SHORT BTC (DCH), SHORT ETH (DCH + D15).
- MT5: poprawka w LAB_M8_HexaTurbo (kopia `.bak_20261121`): ostatnie 8% limitu 30% zarezerwowane dla wariantów bez pozycji – H1 (najlepszy PF w backteście) przez całą dobę nie dostał ani jednego wejścia, bo M15 zjadał limit. Logika sygnałów bez zmian.

**Lekcje:**
- Kilka wariantów tego samego bota na jednym instrumencie = jedna pozycja ×N, nie N niezależnych testów. Werdykt M8 liczę per interwał, a o łącznym ryzyku decyduje limit.
- Kraken margin pobiera rollover 0,02%/4 h (~0,12%/dobę) – na D1 z pozycjami trzymanymi tygodniami to może być więcej niż cała przewaga z backtestu (który liczył tylko 0,75% za wejście i wyjście). Paper to policzy – zobaczymy.
- Limit 30% przy wielu botach wymaga podziału, nie „kto pierwszy, ten lepszy”.

**Nowe pomysły:** dziś bez nowych strategii – noc w całości na M8 (priorytet szefa). Aktywne procesy: 10/10.

**Najlepszy:** LAB_Donchian_XAG +1032,53 $ (3/3). W M8 na żywo – na razie H4/D1 złota (otwarte na plusie), M15 najsłabszy (PF 0,73).

---

## 2026-11-22 (noc 5) – M8 przegląd, M9 ruszyło: zbieracz memów + Bot C

**Przegląd (konto demo botów 5058971085, trade_mode DEMO; Hexa/Turbo/Indeksy bez pozycji, nietknięte):** weekend – rynki zamknięte, MT5 bez nowych zamknięć. Lab MT5: 19 zamkniętych, +1148,58 $ (Donchian_XAG 3/3 +1032,53 $, znów SHORT srebra). M8 na MT5: 13 tr., −96 $, PF 0,68; otwarte H4/D1 złota po +43 $, srebro H4 +49/+41 $. IBKR M8 D1 SHORT czeka na otwarcie rynku (zlecenie PreSubmitted, ponawia co 15 min). Kraken: KR_RSI2_H4 zamknął SHORT XRP **+55,88 €** (TP) i otworzył SHORT BTC i XRP; KR_M8_D1 trzyma SHORT BTC/ETH. eToro DEMO (`account: demo` w odpowiedzi): GOLD SHORT +2,50 $. Wszystkie 10 procesów żyło, logi bez błędów.

**M8:** kroki 1–3 na bieżąco, do werdyktu (~20 transakcji na wariant) daleko – kroku 4 nie zaczynam.

**Wyłączone (lekcja): nic.** **Zawieszony:** LAB_IB_RSI2_AUD (plik `_off`, aktywny=false) – 0 transakcji w 4 dni, z czego półtora dnia Gateway nie działał; bez werdyktu, slot oddany M9.

**M9 – nowe:**
- 🆕 **KROK 0 – zbieracz** `C:\Hexa\lab\memy\zbieracz.py`: co 3 min GeckoTerminal (nowe i trendujące pule Solany), DexScreener (profile, boosty, ceny/płynność/wolumen/kupna-sprzedaże), RugCheck dla kandydatów bota A (10–180 min, płynność ≥ 10k) i B (≥ 3 dni, ≥ 250k). Tylko odczyt, 0 €, bez kluczy. Autostart w START_WSZYSTKO (kopia .bak), test restartu przeszedł (wykrycie → zabicie → BRAK → start → druga instancja sama się zamyka). Pierwsze cykle: 165 tokenów, 0 błędów. Do poprawy: „top 10 bez puli” nie zawsze odcina konto puli (np. PUMP 59,5%) – dopracuję przy bocie A.
- 🆕 **Bot C – backtest** 56 wariantów na DOGE/SHIB/PEPE/BONK/WIF/FLOKI (wszystkie są na Kraken EUR). Wybicia Donchiana i skoki wolumenu – PF sprawdzianu 0,3–0,75 ❌ (koszt 1% w obie strony > przewaga). Przeżył tylko **H4 EMA20/50 + wolumen 1,5×, filtr BTC, SL 2 ATR, trailing 3 ATR: nauka PF 1,82 (n75), sprawdzian PF 1,51 (n35)**. Puszczony na papier jako `LAB_KR_M9_MemyC` (50 € na transakcję, tylko LONG). Dziś BTC pod EMA50 H4 → filtr nie pozwala wejść – i dobrze.

**Lekcje:** na memach liczy się koszt, nie trafność – trafność zwycięzcy to 29%, zarabia kilka dużych trendów. Filtr BTC podnosi PF (1,30 → 1,51) i zmniejsza obsunięcie.

**Najlepszy:** LAB_Donchian_XAG +1032,53 $ (3/3). Aktywne procesy: 10/10 + zbieracz memów.

---

## 2026-11-23 (noc 6) – poniedziałkowe otwarcie boli M8, M9 Bot A ruszył

**Przegląd (konto demo botów 5058971085, trade_mode DEMO; Hexa/Turbo/Indeksy bez otwartych pozycji, nietknięte):** po otwarciu rynku złoto i srebro skoczyły w górę – SHORT-y laboratorium dostały po głowie. Lab MT5: **25 zamkniętych, +596,83 $** (było +1148,58 $). LAB_Donchian_XAG pierwszy SL: −377,70 $ (4 tr., +654,83 $, PF 2,73 – wciąż najlepszy). Konto botów: saldo 6103,64 $, kapitał 5828,39 $.
- **M8 MT5: 18 zamkniętych, −270,07 $, PF 0,43.** Nowe straty z nocy: M15 Turbo −34,54, M30 Hexa/Turbo −44,06/−44,06, XAG M30 −48,29, JPY H1 −3,10. H1 złota wciąż 0 zamknięć; 5 SHORT-ów H4/D1 złota po −47 $, XAG H4 −15/−24 $. Maks. 5 transakcji na wariant – do progu ~20 daleko, kroku 4 nie ruszam. Obraz na razie zgodny z backtestem: M15/M30 najsłabsze.
- **IBKR paper:** D1 SHORT XAUUSD wreszcie wypełniony (22.11 23:01 @ 3575,81, OCA TP/SL).
- **Kraken na sucho:** KR_RSI2_H4 SHORT BTC i XRP otwarte (kapitał 551,78 €), KR_M8_D1 SHORT BTC/ETH otwarte, MemyC – filtr BTC blokuje (BTC pod EMA50 H4).
- **eToro DEMO** (`account: demo` w odpowiedzi): LAB_ET_M8_XAU_D1 GOLD SHORT −37,94 $ (SL 3805 / TP 3334), wiersz w arkuszu Transakcje jest (128). Brak nowych otwarć → brak nowych wierszy.

**Wyłączone (lekcja): nic** (żaden bot nie ma ~20 transakcji ani −30% kapitału). **Zawieszony:** LAB_Kons_H1 (plik `_off`, aktywny=false, bez otwartych pozycji) – 1 transakcja w 4 dni, od 19.11 sygnały blokował limit 30%; bez werdyktu, slot oddany M9 Bot A.

**M9 – nowe:**
- 🆕 **`LAB_DEX_M9_SnajperA`** (Bot A, papier): kandydaci z memy.sqlite (tylko odczyt), filtr: wiek 15–90 min, płynność ≥ 30k, LP ≥ 90% zablokowana/spalona, mint i freeze odebrane, top 10 bez puli ≤ 30%, nie „rugged”, kupujący > sprzedający 5 min, rosnący wolumen 5 min. Wejście po cenie NASTĘPNEGO odczytu (realne opóźnienie), 10 $, koszty 1% + poślizg 2×wartość/płynność + 0,01 $ sieci w każdą stronę. Wyjście: +100% połowa, reszta trailing −30%, SL −35%, rug (płynność < 1k / zniknięcie > 2 h) = wyjście po tym, co się da. Ceny otwartych pozycji bot bierze sam z DexScreener. Test `--raz` ok, proces działa.
- **Replay na 24 h zebranych danych** (te same reguły): 287 kandydatów → 13 wejść, 11 zamkniętych, 36% trafnych, **+7,73 $, PF 1,36**; czysto: 5 × SL (≈ −20 $) i 2 × trailing (+89%, +133%) – klasyka memów, zarabiają pojedyncze strzały. 4 zamknięcia to „brak danych” (patrz niżej) – wynik traktuję jako test silnika, nie dowód.
- **Dowód filtra (wstępny):** odrzuceni za bezpieczeństwo – 23% padło (−90% albo płynność < 1k) w ~0,5 h obserwacji; przepuszczeni – 8% w ~3,8 h.
- 🔧 **Zbieracz – poprawka** (kopia `zbieracz.py.bak_20261123`): nowy status „mały” (po 15 min płynność < 5k i nigdy ≥ 10k → nie śledzimy). Lekcja: ~670 nowych tokenów/h przy limicie 450 śledzonych oznaczało, że każdy token był odświeżany tylko ~40 min od odkrycia – kandydaci bota A i obserwacja „czy padł” urywały się w połowie. Po restarcie od razu 189 tokenów „małych”, 0 błędów.

**Lekcje:**
- Weekendowa luka na złocie/srebrze uderza we wszystkie SHORT-y naraz – 6 wariantów M8 + Donchian_XAG to w praktyce jedna duża pozycja kierunkowa. Przy werdykcie M8 trzeba to liczyć jako jedno zdarzenie.
- Zbieracz z limitem musi mieć priorytet „ważne tokeny”, a nie „najnowsze” – inaczej mierzymy tylko pierwsze 40 minut życia memów.

**Nowe pomysły:** brak nowych strategii poza M9 Bot A – noc na M8 + M9 (priorytet szefa). Następny przebieg M9: Bot B „Fala” (tokeny ≥ 3 dni, płynność ≥ 250k).

**Najlepszy:** LAB_Donchian_XAG +654,83 $ (4 tr., PF 2,73). Aktywne procesy: 10/10 + zbieracz memów.

---

## 2026-11-24 (noc 7) – M8 bez werdyktu, M9 Bot B: wybicia odrzucone, gra „przeciw tłumowi”

**Przegląd (konto demo botów 5058971085, trade_mode DEMO; Hexa/Turbo/Indeksy bez otwartych pozycji, nietknięte):** saldo 5904,43 $, kapitał 5710,35 $. Lab MT5: **44 zamknięte, +311,81 $** (było +596,83 $). Donchian_XAG bez zmian (4 tr., +654,83 $, PF 2,73), RSI2_FX 6 tr. +26,48 $ (PF 3,28), Londyn_XAU 1 tr. +219,38 $.
- **M8 MT5: 32 zamknięte, −565,37 $, PF 0,43.** Obraz się odwrócił: M15 złota teraz na plusie (Hexa 7 tr. +34,98 $ PF 1,35, Turbo 5 tr. +22,02 $ PF 1,26), M30 ~0 (−10,85/−10,57 $, PF 0,89), a najwięcej straciły H4 (HT_XAU_H4 i H4_TP2x2 po 2 tr. −190,9 $ – SHORT-y sprzed weekendu wybite w poniedziałek) i srebro (XAG M30 −94,34, XAG H4 −81,39 $). H1: 1 tr. (Turbo −42,60 $). Otwarte: D1 złota SHORT −98,75 $, XAG H4 SHORT −94,50 $, GBP H4 2× ~0. Maks. 7 transakcji na wariant (próg ~20) → **werdyktu i kroku 4 jeszcze nie ma**.
- **IBKR paper:** D1 SHORT XAUUSD @ 3575,81 nadal otwarty (złoto ~3668 → ok. −92 $ na 1 oz). W logu 2 timeouty połączenia 23.11 po południu, bot sam wstał 16:28 (konto DUR…, paper).
- **Kraken na sucho:** KR_M8_D1 – ETH DCH SHORT zamknięty SL **−10,85 €** (23.11 14:27); otwarte BTC DCH i ETH D15 SHORT. KR_RSI2_H4 kapitał 550,58 € (rollover zjada ~0,6 €/dobę). MemyC – BTC 61 271 pod EMA50 H4 62 777 → filtr blokuje, 0 transakcji.
- **eToro DEMO** (`"account":"demo"` w odpowiedzi): LAB_ET_M8_XAU_D1 GOLD SHORT −73,28 $ (SL 3805 / TP 3334). Brak nowych otwarć i zamknięć → arkusz bez zmian.
- **M9 Bot A na żywo:** 13 zamkniętych, **0 trafnych, −53,44 $** (kapitał 443,55 $ z 500), wszystkie wyjścia SL −35…−44%. 7 z 13 było w trakcie +40…+65% nad wejściem (BONER +65%, ChristmASS +60%, HUANG +49%, JENSEN +47%) i wróciło do SL – TP dopiero przy +100% to za daleko na memy po pierwszej fali. Do progu (≥ 20 tr. na wyłączenie, ≥ 100 na werdykt M9) jeszcze nie – bot zostaje; kandydat na wariant „BE po +40%”.

**Wyłączone (lekcja): nic** (żaden bot nie ma ~20 transakcji ani −30% kapitału). **Zawieszony:** LAB_Luka_FX (plik `_off`, aktywny=false, bez otwartych pozycji) – 0 transakcji od 19.11, bez werdyktu; slot oddany M9 Bot B.

**M9 Bot B „Fala” – backtest** (`memy\m9b_bt.py`): 23 memy z bazy zbieracza (wiek ≥ 3 dni, płynność ≥ 250k; bez WETH/ZEC/ORCA), świece H1 z darmowego GeckoTerminal (do 4000 h, 06–11.2026), koszty 1% swap w każdą stronę + poślizg 2×(10 $/płynność) + sieć, wejście na otwarciu następnej świecy, nauka 70% / spr 30%.
- **Wybicie z planu** (zamknięcie > szczyt N h, wolumen ≥ K × śr. 24 h, SL pod dołkiem wybicia, trailing 2–3 ATR): 36 wariantów (N 1/6/24 × K 2/3/5 × ATR 2/3 × SL świeca/zakres) – **sprawdzian PF 0,10–0,36 ❌ we wszystkich**, trafność 11–21%. Nauka bywała świetna (PF do 3,4), ale to kilka rakiet z wczesnego życia tokenów – klasyczne przeuczenie.
- **Odwrotnie – kupno po kapitulacji** (`m9b_bt2.py`): świeca H1 −10% przy wolumenie ≥ 3× średniej, SL −35%, trailing 3 ATR: **nauka n65 PF 10,6, sprawdzian n29 PF 1,99, trafność 45%, ΣR +145%**. Sąsiedzi też trzymają (K 2/3, SL 25/35%, spadek 10/15%: spr PF 1,44–2,78), trailing 2 ATR i spadek 25% – słabo.
- 🆕 **`LAB_DEX_M9_FalaB`** na papierze (10 $/transakcja, 500 $ wirt.): co godzinę skan kandydatów z bazy (wiek ≥ 3 dni, płynność ≥ 250k, market cap 5–200 mln), sygnał „kapitulacja”, wejście po cenie następnego odczytu DexScreener, stop co 5 min. Test `--raz` ok (12 kandydatów, 0 sygnałów), proces działa.
- **Uczciwie:** to backtest na tokenach, które PRZEŻYŁY do dziś (survivorship bias – kupowanie dołków u ocalałych zawsze wygląda dobrze), tylko 29 transakcji w sprawdzianie, a w backteście kapitulacji nie było filtra market cap (bot go ma). Papier pokaże, ile z tego jest prawdą.

**Lekcje:**
- Na memach DEX wybicie z wolumenem to moment, w którym wcześni sprzedają późnym – po kosztach 2% w obie strony to maszynka do strat (zgodne z Botem C na Krakenie: wybicia Donchiana też odpadły).
- Bot A: SL −35% przy TP +100% na tokenach 15–90 min to za mało miejsca na zyski, a za dużo na straty – przy werdykcie trzeba sprawdzić wcześniejsze zabezpieczenie zysku.
- M8: przez weekendową lukę złota/srebra jedno zdarzenie dało ~−560 $ na H4/D1/XAG – przy werdykcie liczę je jako jedną stratę kierunkową, nie 6 niezależnych.

**Nowe pomysły:** poza M9 Bot B – brak (noc na M8 + M9, priorytet szefa).

**Najlepszy:** LAB_Donchian_XAG +654,83 $ (4 tr., PF 2,73). Aktywne procesy: 10/10 + zbieracz memów.

---

## 2026-11-25 (noc 8) – M8 odrabia, M9 Bot A wyłączony (A2 też nie przeszedł)

**Przegląd (konto demo botów 5058971085, trade_mode DEMO; Hexa 830083 i Turbo 830099 po 1 otwartej, nietknięte):** saldo 6171,13 $, kapitał 6639,94 $. Lab MT5: **55 zamkniętych, +445,31 $** (było +311,81 $). Donchian_XAG bez zmian (4 tr., +654,83 $, PF 2,73), Londyn_XAU 2 tr. +183,11 $ (24.11 SL −36,27 $), RSI2_FX 7 tr. +42,14 $ (PF 4,63).
- **M8 MT5: 45 zamkniętych, −433,56 $, PF 0,60** (było 0,43). M15 złota: Hexa 10 tr. +17,90 $ (PF 1,13), Turbo 8 tr. +4,71 $; nowe M15_TP2/TP3 – 3 i 2 tr., +3,68 / +18,62 $; M30 złota Hexa/Turbo po 5 tr. +18,65 / +19,10 $ (PF 1,2); XAG M30 5 tr. +25,21 $ (PF 1,27); T_JPY_H1 5 tr. −2,65 $. Cała strata to dalej jedno zdarzenie 23.11 (H4 / H4_TP2x2 / XAG H4 / T_H1). Złoto zeszło w nocy do ~3555 → 10 otwartych SHORT-ów ok. **+405 $** niezrealizowane (M15 i XAG M30 ze stopem na BE). Maks. 10 tr./wariant – bez werdyktu.
- **IBKR paper (DUR…):** D1 SHORT @ 3575,81 + nowy H1 SHORT @ 3567,53 (24.11 16:00, SL 3607,53 / TP 3527,53) – obie na plusie.
- **Kraken na sucho:** KR_M8_D1 bez zmian (otwarte SHORT BTC DCH, ETH D15); KR_RSI2_H4 kapitał 549,38 € (2 SHORT-y od 21.11); MemyC 0 tr. – BTC 59,8k pod EMA50 H4 62,2k.
- **eToro DEMO** (`"account":"demo"` w odpowiedzi): LAB_ET_M8_XAU_D1 GOLD SHORT **+6,31 $** (SL 3805 / TP 3334). Brak otwarć i zamknięć → arkusz bez zmian.

**Wyłączone (lekcja): `LAB_DEX_M9_SnajperA`** – 29 transakcji, 3 trafne, **PF 0,15, −105,14 $** (kapitał 400 z 500 = −20%), 26 × SL −35…−44%. Plik `_off`, aktywny=false, 6 otwartych pozycji papierowych zamrożonych po ostatniej wycenie (~65 $). Lekcja: memy w 15–90 min życia po „przeżyciu pierwszej fali” to wciąż rynek, na którym wcześni sprzedają późnym – nawet przepuszczone przez filtr padają w 49% (śr. −74% od wejścia), a koszty ~2% w obie strony zjadają resztę. Filtr bezpieczeństwa działa (odrzuceni: 81% padło), ale nie daje przewagi, tylko mniejszą stratę.

**Nowy pomysł (przetestowany, odrzucony): A2 – zabezpieczenie zysku.** Lekcja z 24.11: 12/29 transakcji A było ≥ +40% i wróciło do SL. Replay 3 dób (te same wejścia, 44–46 tr.), 10 wariantów: stop na +3% po szczycie +15…+40%, TP połowy +30…+60%, trailing 15–30%, SL 12–35%. Nauka do PF 1,23, ale **sprawdzian (ostatnie 30% czasu) PF 0,04–0,49 we wszystkich** → nie idzie na papier. Szczegóły w lab_tabela.md (Memy).

**Karta M9 (lab_tabela.md):** A wyłączony; B 1 tr. (ANSEM −45%, trailing), 1 otwarta; C 0 tr. Do werdyktów B (≥ 100) i C (≥ 30) daleko.

**Lekcje:**
- Ciaśniejsze wyjścia na memach poprawiają tylko naukę – na nowych danych znika wszystko. Przy 2% kosztów i 50% zgonów tokenów sam timing wyjścia nie robi przewagi.
- M8: bez weekendowej luki M15/M30 złota i M30 srebra są na plusie – zgodne z backtestem (PF 1,0–1,3); werdykt nadal przy ~20 tr.

**Najlepszy:** LAB_Donchian_XAG +654,83 $ (4 tr., PF 2,73). Aktywne procesy: 9/10 + zbieracz memów (wolny slot po Bocie A).


---

## 2026-11-26 (noc 9) – M8 prawie odrobione, M15 złota blisko werdyktu; nowy LAB_Dyw_XAU

**Przegląd (konto demo botów 5058971085, trade_mode DEMO; Hexa 830083 i Turbo 830099 bez otwartych pozycji, nietknięte):** saldo 6788,00 $, kapitał 6794,07 $. Lab MT5: **106 zamkniętych, +858,15 $** (było +445,31 $). Donchian_XAG 5 tr. +729,68 $ (PF 2,93), Londyn_XAU 3 tr. +249,75 $ (PF 7,89), RSI2_FX 9 tr. +30,54 $ (PF 2,32).
- **M8 MT5: 88 zamkniętych, −128,31 $** (rdzeń 830210–830223: 81 tr., −193,50 $, PF 0,88; było 0,60). Złoto M15: Hexa 18 tr. +80,83 $ (PF 1,35), Turbo 15 tr. +96,63 $ (PF 1,53), TP2/TP3 7/4 tr. +23,98/+41,21 $; M30 Hexa/Turbo po 10 tr. +48 $ (PF 1,28); XAG M30 9 tr. +78,37 $ (PF 1,44); H1 Hexa +31,44 $ / Turbo −11,60 $; H4 −279,87 $ i H4_TP2x2 −190,95 $ (23.11 luka + 25.11 SL, gdy złoto odbiło z 3467 do 3576). Maks. 18 tr./wariant – werdykt przy następnym przeglądzie.
- **IBKR paper (DUR…):** 6 zamkniętych, −18,40 $ – H1 3 × TP (+40,02/+39,81/+31,58), 2 × SL (−0,97/−50,75), H4 SL −78,09.
- **Kraken na sucho:** KR_M8_D1 bez zmian; KR_RSI2_H4 zamknął oba SHORT-y czasem (BTC −1,20 €, XRP −6,00 €), kapitał 548,68 €; MemyC 0 tr. (BTC 60,5k pod EMA50 H4 61,6k).
- **eToro DEMO** (`"account":"demo"` w odpowiedzi): LAB_ET_M8_XAU_D1 GOLD SHORT **+32,42 $** (SL 3805 / TP 3334). Brak otwarć/zamknięć → arkusz bez zmian.
- **M9:** zbieracz 63,6k tokenów, 0 błędów; FalaB 2 tr. −6,13 $, 1 otwarta (GeckoTerminal 429 – bot ponawia z przerwą); C bez sygnału.

**Wyłączone (lekcja): nic** – żaden aktywny bot nie ma ~20 transakcji z PF < 0,9 ani −30% kapitału.

**Nowe pomysły (1728 przebiegów, `narzedzia\backtest_noc9.py`, wyniki `logi\backtest_runda9.txt`):**
- **SERIA** – kontra po dokładnie 4–6 świecach w jedną stronę. Przeszło tylko GBPUSD H1 (spr PF 1,47, n53, siatka 62/72) i słabiej USDJPY M15 (1,37, n64). Na złocie i indeksach odpada (spr 0,79–0,90) – w trendzie seria to nie wyczerpanie, tylko początek.
- **DYWERGENCJA złoto–srebro** – gdy w 4 h jeden metal ucieknie drugiemu o ≥ 3 ATR, maruder dogania. **XAUUSD H1: nauka PF 1,38 (n280), sprawdzian PF 1,15 (n106, traf. 48%), 132/144 wariantów z spr PF ≥ 1** – najstabilniejszy wynik laboratorium. Srebro jako maruder – tylko jeden szczęśliwy punkt (26/144) ❌.
- 🆕 **`LAB_Dyw_XAU`** (magic 830230, XAUUSD H1, SL 2,5 / TP 3 ATR, max 48 h, ryzyko 0,5%) – test `--raz` ok, proces działa (START_LAB). Kod strategii w pliku bota (wspólny silnik i lab_mt5 bez zmian).
- GBPUSD seria H1 – czeka na wolny slot (10/10 aktywnych).

**Lekcje:**
- M8: na żywo M15/M30 złota idą lepiej niż sprawdzian (PF 1,28–1,53 vs 1,01–1,28), a H4 – gorzej; wszystkie warianty H4 biorą ten sam sygnał DCH, więc 2 złe dni = −470 $. Przy werdykcie H4 liczę jako 2 zdarzenia, nie 5 transakcji.
- Kontra po serii działa tylko tam, gdzie rynek nie jest w silnym trendzie (forex H1) – złoto 2026 karze każdą kontrę.

**Najlepszy:** LAB_Donchian_XAG +729,68 $ (5 tr., PF 2,93). Aktywne procesy: 10/10 + zbieracz memów.

---

## 2026-11-27 (noc 10) – pierwszy werdykt M8: H_XAU_M15 zostaje; krok 4 przetestowany; NR7 czeka na slot

**Przegląd (konto demo botów 5058971085, trade_mode DEMO; Hexa 830083 i Turbo 830099 bez otwartych pozycji, nietknięte):** saldo 6689,35 $, kapitał 6679,91 $. Lab MT5: **122 zamknięte, +759,50 $** (było +858,15 $). Donchian_XAG 5 tr. +729,68 $ (PF 2,93, 1 SHORT otwarty), Londyn_XAU 3 tr. +249,75 $, RSI2_FX 12 tr. +24,22 $ (PF 1,48).
- **M8 MT5: 101 zamkniętych, −220,64 $** (rdzeń 86 tr., −239,45 $, PF 0,86). Noc 26/27.11: 2 SL-e DCH na wszystkich 4 wariantach M15 (−9…−14 $ każdy).
- **Werdykt (≥ 20 tr.): H_XAU_M15 – 20 tr., +57,89 $, PF 1,23** (sprawdzian 1,01) → **zostaje**. T_XAU_M15 17 tr. PF 1,36 – werdykt za ~3 transakcje.
- **IBKR paper (DUR…):** bez nowych zamknięć (6 tr., −18,40 $). LAB_IB_DCH_INDIA (clientId 52) wystartował 26.11 22:47 – dodany w innej sesji na polecenie szefa.
- **Kraken na sucho:** KR_M8_D1 bez zmian; KR_RSI2_H4 2 nowe SHORT-y (BTC @ 55 393 €, XRP @ 0,873 €); MemyC 0 tr. (filtr BTC); PAXG_LongBezSL (pomysł szefa) działa, 0 tr.
- **eToro DEMO** (`"account":"demo"` w odpowiedzi): LAB_ET_M8_XAU_D1 GOLD SHORT **−7,84 $** (SL 3805 / TP 3334). Brak otwarć/zamknięć → arkusz bez zmian.
- **M9:** zbieracz 79,3k tokenów, 0 błędów; FalaB 3 tr. −6,91 $ (VINE −8% nowa); C bez sygnału.

**Wyłączone (lekcja): nic** – żaden aktywny bot nie ma ~20 transakcji z PF < 0,9 ani −30% kapitału (najbliżej: rdzeń M8 PF 0,86, ale to 15 niezależnych wariantów, liczonych osobno).

**M8 krok 4 – test drugiej pozycji (`m8\krok4_bt.py`, wynik `m8\m8_krok4.json`):** max 2 pozycje na rodzinę zamiast 1, złoto M15/M30/H1 × Hexa/Turbo × TP baza/2R × MT5/IBKR/eToro (72 przebiegi). ΣR rośnie o 30–55%, obsunięcie o 30–80%. Poprawa zysku na jednostkę ryzyka tylko **Turbo M30** (MT5 ΣR/DD 5,70 → 7,56, na 3 platformach). H_XAU_M15: +8R za DD 30 → 50R – **nie dublujemy**. Nic nie wdrażam.

**Nowe pomysły (162 przebiegi, `narzedzia\backtest_noc10.py`):**
- **TYDZIEŃ** (czwartek w kierunku ruchu tygodnia) – niestabilny (JPY 0/27, XAG 6/27, AUD 3/27) ❌.
- **NR7** (wybicie z najwęższego dnia z 7, H1, TP 1,5R) – siatka spr ≥ 1 na 63/72 wariantach; XAU/XAG/JPY nauka 1,15–1,33 i sprawdzian 1,12–1,52 → kandydat `LAB_NR7`. **Nie uruchomiony – 12/12 aktywnych**; czeka na slot (z GBPUSD seria).

**Lekcje:**
- Werdykt per wariant ≠ suma: M8 jako całość −220 $, ale wynik to dwa weekendowe zdarzenia H4; M15/M30 złota i srebra są na plusie.
- Druga pozycja to dźwignia, nie przewaga – opłaca się tylko tam, gdzie sygnały same się nie nakładają (Turbo M30).

**Najlepszy:** LAB_Donchian_XAG +729,68 $ (5 tr., PF 2,93). Aktywne procesy: 12 + zbieracz memów, wszystkie żyją.
