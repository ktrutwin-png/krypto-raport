# Laboratorium – tabela stanu (demo / paper / virtual)

Aktualizacja: 2026-11-22 01:40 UTC

| Nazwa | Platforma | Magic / clientId | Start | Transakcje (zamkn.) | Wynik | PF | Status | Backtest (spr. PF, n) |
|---|---|---|---|---|---|---|---|---|
| LAB_Londyn_XAU | MT5 demo 5058971085 · XAUUSD M15 | 830201 | 2026-11-18 | 1 | +219,38 $ | – (1/0) | ✅ działa | 2,19 (90) |
| LAB_Donchian_XAG | MT5 demo · XAGUSD H1 | 830202 | 2026-11-18 | 3 (+1 otwarta, −1,00 $) | +1032,53 $ | – (3/0) | ✅ działa – kandydat „Silver King” | 1,50 (94) |
| LAB_Kontra_FX_off | MT5 demo · EURUSD, USDJPY M15 | 830203 | 2026-11-18 | 0 | 0,00 $ | – | ⏸️ zawieszony 21.11 (0 transakcji, slot dla M8) | 1,32 / 1,36 |
| LAB_RSI2_FX | MT5 demo · USDJPY, GBPUSD M15 | 830204 | 2026-11-18 | 1 | +16,20 $ | – (1/0) | ✅ działa | 1,37 / 1,10 |
| LAB_KR_RSI2_H4 | Kraken na sucho · BTC/EUR, XRP/EUR H4 | paper | 2026-11-18 | 0 (+1 otwarta SHORT XRP) | opłaty | – | ✅ działa (pojedyncze błędy SSL Krakena, sam wraca) | 1,31 (9) / 1,60 (11) |
| LAB_IB_RSI2_AUD_off | IBKR paper · AUDUSD M15 | clientId 50 | 2026-11-18 | 0 | 0,00 $ | – | ⏸️ zawieszony 22.11 (0 transakcji w 4 dni, bez werdyktu – slot dla M9 Bot C) | 1,22 (237) |
| LAB_ET_Kontra_D1 | eToro DEMO · GBPUSD D1 | – | 2026-11-18 | 0 | 0,00 $ | – | ⏳ brak sygnału | 2,16 (7) |
| LAB_Luka_FX | MT5 demo · 4 pary H1 | 830205 | 2026-11-19 | 0 | 0,00 $ | – | ✅ działa (handluje w poniedziałki) | 1,87–4,97 |
| LAB_Kons_H1 | MT5 demo · USDJPY, EURUSD H1 | 830206 | 2026-11-19 | 1 | −23,51 $ | 0,00 | ✅ działa | 1,78 (68) / 1,69 (72) |
| LAB_NYFade_off | MT5 demo · XAU/EUR/GBP M15 | 830207 | 2026-11-19 | 0 | 0,00 $ | – | ⏸️ zawieszony 21.11 (0 transakcji – lot > limit 30%, slot dla M8) | 1,44 / 1,58 / 1,57 |
| LAB_M8_HexaTurbo | MT5 demo · 14 wariantów (niżej) | 830210–830223 | 2026-11-20 | 13 (+13 otwartych) | −96,02 $ | 0,68 | ✅ działa (21.11: rezerwa 8% limitu dla pustych wariantów) | patrz M8 |
| LAB_IB_M8_XAU | IBKR paper · XAUUSD H1/H4/D1 (Hexa, 1 oz) | clientId 51 | 2026-11-21 | 0 | 0,00 $ | – | 🆕 działa, D1 SHORT czeka na otwarcie rynku | 1,35 / 1,58 / 2,34 |
| LAB_KR_M8_D1 | Kraken na sucho · BTC/ETH/XRP D1 (500 € wirt./para) | paper | 2026-11-21 | 0 (3 otwarte: SHORT BTC DCH, ETH DCH+D15) | opłaty | – | 🆕 działa | 1,02 / 1,09 / 1,18 |
| LAB_KR_M9_MemyC | Kraken na sucho · DOGE/SHIB/PEPE/BONK/WIF/FLOKI EUR H4, tylko LONG | paper | 2026-11-22 | 0 | 0,00 € | – | 🆕 działa (BTC pod EMA50 H4 → filtr blokuje) | 1,51 (35) |
| LAB_ET_M8_XAU_D1 | eToro DEMO · GOLD D1 | poz. 3646949765 | 2026-11-20 | 0 (1 otwarta SHORT @ 3563,87, +2,50 $) | 0,00 $ | – | ✅ SL 3805 / TP 3334 | 2,32 (69) |

Wyłączone na stałe: brak (żaden bot nie ma ~20 transakcji). Zawieszone (bez lekcji, brak danych): Kontra_FX, NYFade, IB_RSI2_AUD (22.11).
Razem MT5 lab: 19 zamkniętych, +1148,58 $; konto demo botów: saldo 6655 $, kapitał 6936 $. Aktywne procesy: 10/10.

## M8 – Hexa i Turbo na M15/M30/H1/H4/D1, wszystkie platformy (backtest 20.11.2026)

Logika 1:1 z hexa_bot.py / hexa_turbo.py, zmienia się tylko interwał X i instrument: ASIA (wybicie zakresu Azji, tylko X ≤ H1, TP 1R), DCH (Donchian 20 na X + trend EMA100 z 4X, SL 2 ATR, TP 1R), D15 (Donchian 40 na X + trend EMA100 z 16X, SL 3 ATR, TP 2R, BE przy 1R). Hexa = filtr dolara na ASIA + max 3 pozycje; Turbo = bez filtra, max 5. Na H4/D1 nie ma ASIA → Hexa = Turbo. Wejście na otwarciu następnej świecy, tylko gdy cena nadal za poziomem. Koszty: MT5 spread świecy; IBKR 0,7× spread + 0,2 bp×2; eToro złoto 0,50 $, krypto 1% w każdą stronę; Kraken 0,75% w obie strony. Wynik w R (1R = odległość SL). **Nauka** = pierwsze 70% danych, **spr** = ostatnie 30%. Dane: MT5 M15 od 03.2025 (60k), M30 50k, H1 40k, H4 12k, D1 3000 świec; krypto Binance (proxy ceny) – BTC M15 2 lata, ETH/XRP M15 1 rok, D1 od 2018.

Format komórki: **PF spr (n)** · ΣR spr · maks. obsunięcie R | nauka PF. Hexa / Turbo, gdy się różnią.

| Platforma · instrument | M15 | M30 | H1 | H4 | D1 |
|---|---|---|---|---|---|
| MT5 · XAUUSD | **1,01 / 1,02** (915/977) · +4/+12R · DD 30/26 \| 1,06 | **1,28 / 1,26** (1039/1161) · +134/+139R · DD 20/24 \| 1,02 | **1,37 / 1,32** (838/984) · +135/+139R · DD 19/18 \| 0,95/0,93 | **1,59** (362) · +88R · DD 18 \| 0,98 | **2,35** (69) · +31R · DD 5 \| 1,66 |
| MT5 · XAGUSD | **1,04 / 1,04** (903/967) · +20R · DD 50/44 \| 0,95 | **1,14 / 1,13** (870/965) · +58R · DD 17 \| 0,86 | **1,11 / 1,06** (825/964) · +44/+30R \| 0,91/0,88 | **1,29** (223) · +30R · DD 13 \| 1,04 | **1,99** (58) · +21R · DD 4 \| 0,82 |
| MT5 · EURUSD | 0,99 / 1,00 (901/966) · −3/+1R \| 0,87 | 1,02 / 0,98 (906/988) \| 0,88 | 0,97 / 0,95 \| 0,92 | 1,00 (182) \| 1,03 | 0,95 (43) \| 1,11 |
| MT5 · GBPUSD | 0,94 / 0,94 ❌ | 0,97 / 0,94 \| 0,91 | 0,98 / 0,96 \| 0,90 | 1,03 (172) · +3R \| 0,91 | 0,50 ❌ |
| MT5 · USDJPY | 0,81 / 0,79 ❌ | 0,89 ❌ | 0,96 / 1,00 (679/911) \| 1,19/1,15 | 0,84 ❌ | 0,87 ❌ |
| MT5 · AUDUSD | 0,87 / 0,89 ❌ | 0,88 / 0,90 ❌ | 0,82 / 0,84 ❌ | 0,90 ❌ | 0,72 ❌ |
| IBKR · XAUUSD | 0,99 / 1,01 | **1,27 / 1,24** · +127/+131R | **1,35 / 1,30** · +130/+133R | **1,58** (362) · +87R | **2,34** (69) · +31R |
| IBKR · EURUSD | 0,90 ❌ | 0,95 / 0,91 | 0,92 / 0,89 ❌ | 0,99 (182) | 0,94 |
| IBKR · USDJPY | 0,73 ❌ | 0,84 ❌ | 0,93 / 0,97 | 0,83 ❌ | 0,86 ❌ |
| IBKR · AUDUSD | 0,81 ❌ | 0,85 ❌ | 0,82 ❌ | 0,89 ❌ | 0,71 ❌ |
| eToro · GOLD | 0,97 / 0,98 | **1,23 / 1,21** · +112R \| 0,89 | **1,31 / 1,26** · +117R \| 0,84 | **1,54** (362) · +83R \| 0,94 | **2,32** (69) · +31R · DD 5 \| 1,63 |
| eToro · BTC | 0,00 ❌ (koszt 2% ≫ SL) | 0,01 ❌ | 0,02 ❌ | 0,22 ❌ | 0,69 ❌ |
| Kraken · BTC | 0,03 ❌ | 0,09 ❌ | 0,21 ❌ | 0,60 ❌ | **1,02** (47) · +0,5R \| 1,06 |
| Kraken · ETH | 0,09 ❌ | 0,19 ❌ | 0,30 ❌ | 0,63 ❌ | **1,09** (42) · +2R \| 0,73 |
| Kraken · XRP | 0,12 ❌ | 0,29 ❌ | 0,32 ❌ | 0,77 ❌ | **1,18** (53) · +4R \| 0,38 |

**TP 1R / 1,5R / 2R / 3R i drugie wejście z własnym SL (złoto MT5, spr PF / ΣR):**

| Interwał · bot | baza (dziś) | TP 1R | TP 1,5R | TP 2R | TP 3R | baza + 2. wejście |
|---|---|---|---|---|---|---|
| M15 Hexa | 1,01 / +4 | 1,03 / +13 | 1,06 / +25 | 1,08 / +28 | 1,08 / +26 | 1,02 / +12 (DD 50) |
| M15 Turbo | 1,02 / +12 | 1,04 / +20 | 1,09 / +37 | 1,10 / +40 | 1,11 / +37 | 1,05 / +34 |
| M30 Hexa | 1,28 / +134 | 1,23 / +113 | 1,28 / +119 | 1,35 / +134 | **1,47 / +158** | 1,27 / +173 |
| M30 Turbo | 1,26 / +139 | 1,22 / +118 | 1,26 / +125 | 1,34 / +148 | **1,46 / +178** | 1,29 / +214 (TP3R+2.: 1,40 / +239) |
| H1 Hexa | 1,37 / +135 | 1,33 / +125 | 1,30 / +101 | 1,40 / +123 | **1,47 / +130** | 1,32 / +156 (TP3R+2.: 1,50 / +177) |
| H1 Turbo | 1,32 / +139 | 1,29 / +129 | 1,28 / +111 | 1,37 / +138 | **1,43 / +149** | 1,31 / +190 (TP3R+2.: 1,45 / +218) |
| H4 (Hexa=Turbo) | 1,59 / +88 | 1,45 / +76 | **1,80 / +97** | 1,79 / +93 | 2,00 / +86 | 1,62 / +130 (Turbo TP2R+2.: 1,82 / +164) |
| D1 (Hexa=Turbo) | 2,35 / +31 | 2,29 / +31 | 3,03 / +35 | 3,26 / +34 | **4,80 / +38** | 2,48 / +46 (Turbo TP2R+2.: 4,09 / +71) |

Wniosek TP: na każdym interwale TP 1R (obecne ustawienie DCH/ASIA od 10.11) daje najniższy PF; TP 2–3R podnosi PF i zwykle ΣR. Drugie wejście z własnym SL zwiększa ΣR o 30–80%, ale też obsunięcie (~1,5×). Zmiana w Hexie/Turbo tylko po „wdróż” szefa – na demo laboratorium testuje wariant HT_XAU_H4_TP2x2.

**Uwaga (uczciwie):** sprawdzian złota przypada na mocny trend 2026 – na nauce PF złota był ~1,0 (M30/H1 nawet < 1). Wynik zależy od reżimu rynku; werdykt dopiero po ~20 transakcjach na wariant na demo.

**Wyniki na demo (stan 21.11 01:30 UTC, MT5):**

| Wariant | Magic | Zamkn. | Wynik | PF | Otwarte |
|---|---|---|---|---|---|
| H_XAU_M15 | 830210 | 5 | −27,37 $ | 0,73 | 0 |
| T_XAU_M15 | 830211 | 2 | −6,11 $ | 0,87 | 1 |
| H_XAU_M30 / T_XAU_M30 | 830212 / 830213 | 2 / 2 | −9,63 / −9,36 $ | 0,82 / 0,82 | 1 / 1 |
| H_XAU_H1 / T_XAU_H1 | 830214 / 830215 | 0 | – | – | 0 (głodzone limitem 30% – poprawione 21.11) |
| HT_XAU_H4 / HT_XAU_D1 / H4_TP2x2 | 830216 / 830217 / 830218 | 0 | – | – | 2 / 1 / 2 (wszystkie na plusie ~+43 $) |
| H_XAG_M30 | 830219 | 1 | −46,05 $ | 0,00 | 1 |
| HT_XAG_H4 | 830220 | 0 | – | – | 2 (+90 $) |
| T_JPY_H1 | 830223 | 1 | +2,50 $ | – | 1 |
| **Razem M8 MT5** | | **13** | **−96,02 $** | **0,68** | 13 |

Uwaga: 6 wariantów złota bierze ten sam sygnał DCH → jedna zła świeca (20.11 10:02) to 4 straty naraz. Warianty nie są niezależne – werdykt trzeba liczyć per interwał, nie sumować.

**Na demo od 20.11 (spr PF ≥ 0,95):**

| Wariant | Platforma | Magic / ID | spr PF (n) | Status |
|---|---|---|---|---|
| H_XAU_M15 / T_XAU_M15 | MT5 demo | 830210 / 830211 | 1,01 / 1,02 | 🆕 po 1 SHORT DCH |
| H_XAU_M30 / T_XAU_M30 | MT5 demo | 830212 / 830213 | 1,28 / 1,26 | 🆕 po 1 SHORT DCH |
| H_XAU_H1 / T_XAU_H1 | MT5 demo | 830214 / 830215 | 1,37 / 1,32 | 🆕 czeka na sygnał |
| HT_XAU_H4 | MT5 demo | 830216 | 1,59 | 🆕 SHORT DCH + D15 |
| HT_XAU_D1 | MT5 demo | 830217 | 2,35 | 🆕 SHORT DCH |
| HT_XAU_H4_TP2x2 (TP 2R + 2. wejście) | MT5 demo | 830218 | 1,82 | 🆕 SHORT DCH + D15 |
| H_XAG_M30 | MT5 demo | 830219 | 1,14 | 🆕 SHORT DCH |
| HT_XAG_H4 / HT_XAG_D1 | MT5 demo | 830220 / 830221 | 1,29 / 1,99 | 🆕 HT_XAG_H4 SHORT DCH; reszta odrzucona limitem 30% |
| HT_GBP_H4 | MT5 demo | 830222 | 1,03 | 🆕 sygnał odrzucony limitem 30% |
| T_JPY_H1 | MT5 demo | 830223 | 1,00 | 🆕 czeka |
| LAB_ET_M8_XAU_D1 | eToro DEMO | poz. 3646949765 | 2,32 | 🆕 SHORT GOLD |
| LAB_IB_M8_XAU: H1 / H4 / D1 | IBKR paper | clientId 51 | 1,35 / 1,58 / 2,34 | 🆕 21.11 działa; D1 DCH SHORT ponawiany, rynek zamknięty w weekend |
| LAB_KR_M8_D1: BTC / ETH / XRP D1 | Kraken paper | – | 1,02 / 1,09 / 1,18 (nauka 1,06 / 0,73 / 0,38) | 🆕 21.11 SHORT BTC (DCH), SHORT ETH (DCH + D15); uwaga: rollover 0,12%/dobę – backtest go nie liczył |


## Memy (M9) – stan 22.11.2026

**Krok 0 – zbieracz** `C:\Hexa\lab\memy\zbieracz.py` (cykl 3 min, darmowe API, tylko odczyt): GeckoTerminal new_pools + trending_pools (Solana), DexScreener profile/boosty/tokens, RugCheck (mint/freeze authority, top 10 z i bez puli, % zablokowanej płynności, ryzyka). Pierwsze 4 cykle: 165 tokenów, ~160 snapshotów/cykl, 0 błędów, 17 raportów RugCheck (2 z aktywnym mint+freeze authority). Autostart: START_WSZYSTKO („Memy – zbieracz M9”), test restartu ok.

**Bot C „Duże memy” – backtest** (Binance H1 06.2024–11.2026, 21,7k świec/mem, koszt 0,4% taker + 0,1% poślizg na stronę, tylko LONG, wyjście tylko SL/trailing, nauka 70% / spr 30%, stawka 50 $):

| Wariant (TF · wejście · SL/trailing ATR · filtr BTC) | Nauka n · PF · ΣR% | Sprawdzian n · PF · traf. · ΣR% · DD% | PF spr per mem (DOGE/SHIB/PEPE/BONK/WIF/FLOKI) |
|---|---|---|---|
| **H4 · EMA20/50 w górę + wol. 1,5× · 2/3 · tak** ✅ (na papier) | 75 · **1,82** · +217% | 35 · **1,51** · 29% · +58% · 69% | 5,23 / 0,86 / 1,93 / 1,11 / 1,17 / 2,72 |
| H4 · EMA20/50 + wol. · 2/2 · tak | 75 · 0,77 · −44% | 35 · 1,51 · 23% · +44% · 47% | (nauka < 1 – odpada) |
| H4 · EMA20/50 + wol. · 3/3 · tak | 75 · 1,65 · +191% | 35 · 1,35 · 29% · +45% · 76% | – |
| H4 · EMA20/50 + wol. · 2/3 · bez filtra | 81 · 1,63 · +188% | 42 · 1,30 · 26% · +41% · 79% | filtr BTC pomaga |
| H4 · EMA20/50 + wol. · 3/4 · tak | 75 · 1,24 | 35 · 0,94 ❌ | trailing 4 ATR za luźny |
| H4 · skok wolumenu 3× · 3/3 · tak | 140 · 1,52 | 74 · 0,69 ❌ | przeuczony |
| H1 · EMA20/50 + wol. (najlepszy) | 161 · 1,14 | 109 · 0,87 ❌ | – |
| H1/H4 · Donchian 20/24/48 (wszystkie 24) | 0,58–1,20 | **0,36–0,59** ❌ | koszty 1% w obie strony zjadają wybicia |

Wniosek: na memach z Krakena działa tylko wolny trend H4 z filtrem BTC; szybkie wybicia to dla nas maszynka do płacenia prowizji. Uczciwie: sprawdzian to tylko 35 transakcji, obsunięcie 69% stawki, a DOGE robi połowę wyniku.

| Bot | Status | Transakcje | Trafność | PF po kosztach | Śr. wynik | Maks. DD | Odrzuceni przez filtr / padli |
|---|---|---|---|---|---|---|---|
| A „Snajper z filtrem” | ⏳ czeka (zbieracz zbiera dane) | – | – | – | – | – | – |
| B „Fala” | ⏳ czeka | – | – | – | – | – | – |
| C „Duże memy” (`LAB_KR_M9_MemyC`) | 🆕 papier od 22.11 | 0 | – | – | – | – | – |
