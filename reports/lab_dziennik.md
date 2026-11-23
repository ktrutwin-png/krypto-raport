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
