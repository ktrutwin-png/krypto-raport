# Laboratorium – tabela stanu (demo / paper / virtual)

Aktualizacja: 2026-11-27 01:50 UTC

| Nazwa | Platforma | Magic / clientId | Start | Transakcje (zamkn.) | Wynik | PF | Status | Backtest (spr. PF, n) |
|---|---|---|---|---|---|---|---|---|
| LAB_Londyn_XAU | MT5 demo 5058971085 · XAUUSD M15 | 830201 | 2026-11-18 | 3 | +249,75 $ | 7,89 (2/1) | ✅ działa | 2,19 (90) |
| LAB_Donchian_XAG | MT5 demo · XAGUSD H1 | 830202 | 2026-11-18 | 5 | +729,68 $ | 2,93 (4/1) | ✅ działa – kandydat „Silver King” (23.11 pierwszy SL −377,70 $ – srebro w górę po otwarciu) | 1,50 (94) |
| LAB_Kontra_FX_off | MT5 demo · EURUSD, USDJPY M15 | 830203 | 2026-11-18 | 0 | 0,00 $ | – | ⏸️ zawieszony 21.11 (0 transakcji, slot dla M8) | 1,32 / 1,36 |
| LAB_RSI2_FX | MT5 demo · USDJPY, GBPUSD M15 | 830204 | 2026-11-18 | 12 | +24,22 $ | 1,48 | ✅ działa (część sygnałów odrzuca limit 30%) | 1,37 / 1,10 |
| LAB_KR_RSI2_H4 | Kraken na sucho · BTC/EUR, XRP/EUR H4 | paper | 2026-11-18 | 3 (+2 otwarte SHORT BTC/XRP od 26.11) | +48,68 € (kapitał 548,68 €; wolna gotówka 544,98 €) | 7,76 (1/2) | ✅ działa | 1,31 (9) / 1,60 (11) |
| LAB_IB_RSI2_AUD_off | IBKR paper · AUDUSD M15 | clientId 50 | 2026-11-18 | 0 | 0,00 $ | – | ⏸️ zawieszony 22.11 (0 transakcji w 4 dni, bez werdyktu – slot dla M9 Bot C) | 1,22 (237) |
| LAB_ET_Kontra_D1 | eToro DEMO · GBPUSD D1 | – | 2026-11-18 | 0 | 0,00 $ | – | ⏳ brak sygnału | 2,16 (7) |
| LAB_Luka_FX_off | MT5 demo · 4 pary H1 | 830205 | 2026-11-19 | 0 | 0,00 $ | – | ⏸️ zawieszony 24.11 (0 transakcji w 5 dni – bez werdyktu, slot dla M9 Bot B) | 1,87–4,97 |
| LAB_Kons_H1_off | MT5 demo · USDJPY, EURUSD H1 | 830206 | 2026-11-19 | 1 | −23,51 $ | 0,00 | ⏸️ zawieszony 23.11 (1 transakcja w 4 dni, sygnały blokował limit 30% – bez werdyktu, slot dla M9 Bot A) | 1,78 (68) / 1,69 (72) |
| LAB_NYFade_off | MT5 demo · XAU/EUR/GBP M15 | 830207 | 2026-11-19 | 0 | 0,00 $ | – | ⏸️ zawieszony 21.11 (0 transakcji – lot > limit 30%, slot dla M8) | 1,44 / 1,58 / 1,57 |
| LAB_M8_HexaTurbo | MT5 demo · 16 wariantów (niżej) | 830210–830228 | 2026-11-20 | 101 (+3 otwarte) | −220,64 $ (rdzeń 830210–830223: 86 tr., −239,45 $) | 0,86 (rdzeń) | ✅ działa – 27.11 pierwszy werdykt: H_XAU_M15 ZOSTAJE (20 tr., PF 1,23) | patrz M8 |
| LAB_IB_M8_XAU | IBKR paper · XAUUSD H1/H4/D1 (Hexa, 1 oz) | clientId 51 | 2026-11-21 | 6 (H1: TP +40,02/+39,81/+31,58, SL −0,97/−50,75; H4 SL −78,09) | −18,40 $ | 0,86 | ✅ działa | 1,35 / 1,58 / 2,34 |
| LAB_KR_M8_D1 | Kraken na sucho · BTC/ETH/XRP D1 (500 € wirt./para) | paper | 2026-11-21 | 1 (ETH DCH SL −10,85 €; otwarte SHORT BTC DCH, ETH D15) | −10,85 € + opłaty | 0,00 | ✅ działa | 1,02 / 1,09 / 1,18 |
| LAB_KR_M9_MemyC | Kraken na sucho · DOGE/SHIB/PEPE/BONK/WIF/FLOKI EUR H4, tylko LONG | paper | 2026-11-22 | 0 | 0,00 € | – | 🆕 działa (BTC pod EMA50 H4 → filtr blokuje) | 1,51 (35) |
| LAB_DEX_M9_SnajperA_off | DEX Solana na papierze · nowe tokeny 15–90 min (10 $/transakcja, 500 $ wirt.) | paper | 2026-11-23 | 29 (6 otwartych zamrożonych, wycena ~65 $) | −105,14 $ (kapitał 400,22 $, −20%) | 0,15 (3/29) | ❌ WYŁĄCZONY 25.11 (≥ 20 tr., PF < 0,9); wariant A2 odrzucony na sprawdzianie | replay 3 dni: PF 0,35 (44) |
| LAB_DEX_M9_FalaB | DEX Solana na papierze · memy ≥ 3 dni, płynność ≥ 250k, mc 5–200 mln, kupno po kapitulacji H1 (10 $/transakcja) | paper | 2026-11-24 | 3 | −6,91 $ (ANSEM −45%/−16%, VINE −8%, trailing) | 0,00 | ✅ działa (GeckoTerminal czasem 429 – bot ponawia) | 1,99 (29) |
| LAB_ET_M8_XAU_D1 | eToro DEMO · GOLD D1 | poz. 3646949765 | 2026-11-20 | 0 (1 otwarta SHORT @ 3563,87, −7,84 $) | 0,00 $ | – | ✅ SL 3805 / TP 3334 | 2,32 (69) |
| LAB_Dyw_XAU | MT5 demo · XAUUSD H1 (dywergencja złoto–srebro) | 830230 | 2026-11-26 | 0 | 0,00 $ | – | ✅ działa, brak sygnału | 1,15 (106), siatka 132/144 |
| LAB_KR_PAXG_LongBezSL | Kraken na sucho · PAXG/EUR H1, tylko LONG, bez SL (pomysł szefa 26.11) | paper | 2026-11-26 | 0 | 0,00 € | – | ✅ działa (dodany w innej sesji na polecenie szefa) | bt H1: 233 tr., 90% traf. |
| LAB_IB_DCH_INDIA | IBKR paper · INDA DCH H1 (szef 26.11, Indie) | clientId 52 | 2026-11-27 | 0 | 0,00 $ | – | ✅ działa (dodany w innej sesji na polecenie szefa) | 611 tr., PF 1,84 |

Wyłączone na stałe: LAB_DEX_M9_SnajperA (25.11 – 29 tr., PF 0,15). Zawieszone (bez lekcji, brak danych): Kontra_FX, NYFade, IB_RSI2_AUD (22.11), Kons_H1 (23.11), Luka_FX (24.11).
Razem MT5 lab: 122 zamknięte, +759,50 $; konto demo botów (27.11 01:25 UTC, trade_mode DEMO): saldo 6689,35 $, kapitał 6679,91 $; Hexa 830083 i Turbo 830099 bez otwartych pozycji – nietknięte. Aktywne procesy: 12 (lista.json podniesiona do 12 przez PAXG i INDIA szefa) + zbieracz memów. W kolejce na slot: NR7 (noc 10), GBPUSD seria H1 (noc 9).

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

**Wyniki na demo (stan 27.11 01:25 UTC, MT5):**

| Wariant | Magic | Zamkn. | Wynik | PF | Werdykt |
|---|---|---|---|---|---|
| H_XAU_M15 / T_XAU_M15 | 830210 / 830211 | **20** / 17 | +57,89 / +73,56 $ | **1,23** / 1,36 | ✅ **H_XAU_M15 ZOSTAJE** (27.11: 20 tr., PF 1,23 ≥ spr 1,01) / T – 3 tr. do werdyktu |
| H_XAU_M15_TP2 / H_XAU_M15_TP3 | 830225 / 830228 | 9 / 6 | +0,79 / +18,02 $ | 1,01 / 1,41 | ⏳ |
| H_XAU_M30 / T_XAU_M30 | 830212 / 830213 | 10 / 10 | +47,88 / +48,43 $ | 1,28 / 1,28 | ⏳ |
| H_XAU_H1 / T_XAU_H1 | 830214 / 830215 | 3 / 4 | +31,44 / −11,60 $ | 1,62 / 0,88 | ⏳ |
| HT_XAU_H4 / HT_XAU_D1 / H4_TP2x2 | 830216 / 830217 / 830218 | 3 / 0 / 2 | −279,87 / – / −190,95 $ | 0,00 / – / 0,00 | ⏳ (2 zdarzenia, nie 5 transakcji) |
| H_XAG_M30 | 830219 | 9 | +78,37 $ | 1,44 | ⏳ |
| HT_XAG_H4 / HT_XAG_D1 | 830220 / 830221 | 2 / 0 | −81,33 $ / – | 0,00 | ⏳ |
| HT_GBP_H4 | 830222 | 1 (+1 otw.) | −10,62 $ | 0,00 | ⏳ |
| T_JPY_H1 | 830223 | 5 (+1 otw.) | −2,65 $ | 0,61 | ⏳ |
| **Razem M8 MT5** | | **101** | **−220,64 $** | rdzeń 0,86 | 3 otwarte |

27.11: noc z 26 na 27.11 dała 2 SL-e na M15 (−9…−14 $ na każdy z 4 wariantów M15, ten sam sygnał DCH). H_XAU_M15 jako pierwszy przekroczył 20 transakcji: na żywo PF 1,23 przy sprawdzianie 1,01 – zostaje bez zmian.

**Krok 4 – test „druga pozycja” (max 2 na rodzinę zamiast 1, złoto, sprawdzian 30%; ΣR/DD = zysk na jednostkę obsunięcia):**

| TF · bot · TP | MT5 1 poz. → 2 poz. (PF · ΣR · DD · ΣR/DD) | IBKR ΣR/DD | eToro ΣR/DD |
|---|---|---|---|
| M15 Hexa · baza | 1,01 · +4 · 30 · 0,12 → 1,02 · +12 · 50 · 0,25 | −0,11 → 0,05 | −0,44 → −0,25 |
| M15 Turbo · baza | 1,02 · +12 · 26 · 0,45 → 1,05 · +34 · 41 · 0,81 | 0,15 → 0,52 | −0,30 → 0,06 |
| M30 Hexa · baza | 1,28 · +134 · 20 · 6,62 → 1,27 · +173 · 30 · 5,79 ❌ | 6,10 → 5,10 ❌ | 4,74 → 3,73 ❌ |
| **M30 Turbo · baza** | 1,26 · +139 · 24 · 5,70 → **1,29 · +214 · 28 · 7,56** ✅ | 5,24 → **6,81** ✅ | 4,34 → **4,78** ✅ |
| H1 Hexa · baza | 1,37 · +135 · 19 · 7,20 → 1,32 · +156 · 31 · 5,04 ❌ | 6,73 → 4,67 ❌ | 5,62 → 3,78 ❌ |
| H1 Turbo · baza | 1,32 · +139 · 18 · 7,62 → 1,31 · +190 · 31 · 6,04 ❌ | 7,01 → 5,63 ❌ | 5,54 → 4,38 ❌ |
| H1 Hexa · TP 2R | 1,40 · +123 · 23 · 5,42 → 1,43 · +169 · 29 · 5,84 ≈ | 5,13 → 5,47 | 4,42 → 4,60 |

Wniosek kroku 4: druga pozycja zwykle podnosi ΣR o 30–55%, ale obsunięcie rośnie o 30–80% – w większości kombinacji poprawia tylko ryzyko, nie wynik. Wyraźnie lepiej (na wszystkich 3 platformach) tylko **Turbo M30 (TP bazowy)**; dla H_XAU_M15 (jedyny wariant z werdyktem) zysk +8R kosztem DD 30 → 50R – **nie dublujemy**. Dublowanie Turbo M30 – dopiero po werdykcie T_XAU_M30 (dziś 10 tr.).

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


## Memy (M9) – stan 27.11.2026

**Stan M9 27.11:** zbieracz 79,3k tokenów (20,6k śledzonych, 809 martwych), cykle 3 min, 0 błędów; B 3 tr. (ANSEM −45%/−16%, VINE −8%), −6,91 $, 0 otwartych, 17 kandydatów; C 0 tr. (BTC 60,6k pod EMA50 H4 61,4k – filtr blokuje od 22.11).

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
| A „Snajper z filtrem” (`LAB_DEX_M9_SnajperA`) – papier na żywo 23–25.11 | ❌ wyłączony 25.11 | 29 (+6 otw. zamrożonych) | 10% | **0,15** | −3,63 $ (−36%) | −21% kapitału | 582 kandydatów, weszło 35. Odrzuceni za bezpieczeństwo: 530, z nich **81% padło** (≥ −90% lub płynność < 1k) – ale z 35 przepuszczonych też padło **49%** (śr. obsunięcie od wejścia −74%). Odrzuty: LP < 90% 494, wolumen 309, sprzedający ≥ kupujący 148, top 10 > 30% 68, freeze 14, mint 8 |
| A – replay 24 h (22–23.11) | test silnika | 11 (+2 otw.) | 36% | 1,36 | +0,70 $ (+7%) | – | odrzuceni za bezpieczeństwo: 23% padło (≥ −90% lub płynność < 1k) vs 8% przepuszczonych |
| B „Fala” (`LAB_DEX_M9_FalaB`) – kupno po kapitulacji | ✅ papier od 24.11 | 3 | 0% | 0,00 | −2,30 $ (−23%) | −1,4% | 17 kandydatów, 3 sygnały (27.11) |
| C „Duże memy” (`LAB_KR_M9_MemyC`) | ✅ papier od 22.11 (27.11: BTC 60,6k pod EMA50 H4 61,4k – filtr blokuje) | 0 | – | – | – | – | – |

**Bot A – replay 24 h (22.11 01:00 → 23.11 01:30, te same reguły co bot):** 287 kandydatów (płynność ≥ 30k, wiek 15–90 min). Odrzuty (token może mieć kilka powodów): LP < 90% – 265, wolumen nie rośnie – 158, sprzedający ≥ kupujący – 72, top 10 > 30% – 30, freeze – 14, mint – 1. Wejść 13, zamkniętych 11: TRAIL 2 (+89%, +133%), SL 5 (−38…−45%), „brak danych” 4 (zbieracz przestał śledzić – wycena po ostatniej cenie, +6 $ netto). Uczciwie: 1 doba, 11 transakcji, a ~40% wyniku to wyceny bez danych – to tylko test, że silnik działa; werdykt przy ≥ 100 transakcjach na papierze. „Dev nie sprzedał wszystkiego” – nie mierzymy (brak darmowego źródła w zbieraczu), do dopracowania.

**Bot B – backtest 24.11** (`memy\m9b_bt.py`, `m9b_bt2.py`; 23 memy z bazy: wiek ≥ 3 dni, płynność ≥ 250k, świece H1 GeckoTerminal do 4000 h, 06–11.2026; koszty 1% swap w każdą stronę + poślizg + sieć; wejście na otwarciu następnej świecy; nauka 70% / spr 30%):

| Wariant | Nauka n · PF · ΣR% | Sprawdzian n · PF · traf. · ΣR% |
|---|---|---|
| Wybicie z planu: zamkn. > szczyt 24 h, wol. ≥ 3×, SL pod świecą, trailing 2 ATR | 313 · 0,85 · −230% | 94 · **0,21** ❌ · 15% · −423% |
| Najlepsze z 36 wybić (N 6, K 5, 2 ATR, SL zakres) | 229 · 0,70 | 75 · **0,36** ❌ · 19% |
| Wybicia z najlepszą nauką (N 24, K 5, 3 ATR) | 180 · 3,39 · +2434% | 54 · 0,19 ❌ (przeuczenie – kilka rakiet) |
| **Kapitulacja: świeca H1 −10%, wol. ≥ 3×, SL −35%, trailing 3 ATR** ✅ (na papier) | 65 · 10,6 · +4916% | 29 · **1,99** · 45% · +145% |
| Kapitulacja −10%, wol. 2×, SL −35%, 3 ATR | 102 · 6,35 | 34 · 1,44 · 41% |
| Kapitulacja −15%, wol. 3×, SL −25%, 3 ATR | 32 · 10,4 | 10 · 2,78 · 30% |
| Kapitulacja −10%, wol. 5×, SL −15/−25%, 3 ATR | 36 · 11,3 | 20–21 · 0,98–1,02 |
| Kapitulacja −25% (wszystkie) | 8 · 1,6–2,1 | 1 · 0,00 |

Wniosek: wybicie z wolumenem na memach DEX = moment wyjścia wcześniejszych kupujących; 36/36 wariantów przegrało na sprawdzianie. Odwrotna reguła (kupno paniki u memów, które mają ≥ 3 dni i dużą płynność) przeszła. **Uczciwie:** survivorship bias (w danych tylko tokeny, które przetrwały do dziś), 29 transakcji w sprawdzianie, nauka PF 10 to kilka odbić o setki procent; backtest kapitulacji nie miał filtra market cap (bot ma 5–200 mln). Werdykt przy ≥ 100 transakcjach na papierze.

**Bot A2 – próba ratunku (25.11, replay po 3 dobach danych zbieracza 22–25.11, te same wejścia co A, nauka 70% / sprawdzian 30% po czasie):** pomysł z lekcji 24.11 – 12 z 29 transakcji A na żywo było ≥ +40% nad wejściem i wróciło do SL.

| Wariant (TP połowa · trailing · stop na +3% po szczycie · SL) | Razem n · PF · wynik | Nauka n · PF | Sprawdzian n · PF |
|---|---|---|---|
| baza A (+100% · 30% · – · 35%) | 44 · 0,35 · −102 $ | 33 · 0,38 | 11 · **0,27** ❌ |
| +100% · 30% · po +40% · 35% | 44 · 0,31 · −89 $ | 33 · 0,33 | 11 · 0,27 ❌ |
| +60% · 25% · po +40% · 35% | 44 · 0,59 · −46 $ | 33 · 0,79 | 11 · 0,27 ❌ |
| +50% · 25% · po +30% · 35% | 44 · 0,65 · −36 $ | 33 · 0,80 | 11 · 0,33 ❌ |
| +60% · 25% · po +40% · 25% | 44 · 0,66 · −34 $ | 33 · 0,90 | 11 · 0,29 ❌ |
| +40% · 20% · po +25% · 20% | 45 · 0,84 · −13 $ | 33 · 1,10 | 12 · 0,44 ❌ |
| +40% · 20% · po +25% · 12% | 46 · 0,72 · −21 $ | 33 · 1,23 | 13 · 0,09 ❌ |
| +30% · 20% · po +20% · 20% | 45 · 0,76 · −18 $ | 33 · 0,95 | 12 · **0,49** ❌ |
| +30% · 15% · po +15% · 15% | 46 · 0,71 · −22 $ | 33 · 1,16 | 13 · 0,14 ❌ |
| +50% · 20% · po +20% · 15% | 46 · 0,57 · −34 $ | 33 · 0,95 | 13 · 0,04 ❌ |

Wniosek: ciaśniejsze wyjścia poprawiają naukę (PF do 1,23), ale sprawdzian 0,04–0,49 we wszystkich 10 wariantach – A2 nie idzie na papier. Snajper na tokenach 15–90 min nie ma przewagi przy kosztach ~2% w obie strony; filtr bezpieczeństwa odsiewa najgorsze (81% padłych), ale z przepuszczonych też pada prawie połowa.



## Noc 9 (26.11.2026) – nowe pomysły: SERIA i DYWERGENCJA złoto–srebro

Silnik `lab_silnik.backtest` bez zmian, dane MT5 (M15 od 01–04.2025, H1 od 03–06.2024), koszt = spread świecy, nauka 70% / sprawdzian 30%. „Siatka” = ile wariantów parametrów ma spr PF ≥ 1 (odporność, nie jeden szczęśliwy punkt). 1728 przebiegów.

- **SERIA** (kontra po dokładnie N = 4–6 świecach w jedną stronę o łącznym ruchu ≥ k ATR; SL za ekstremum + bufor, TP 38–62% ruchu, max 8/24 świece).
- **DYWERGENCJA** (w ostatnich 4/12/24 świecach jeden metal uciekł drugiemu o ≥ k ATR → maruder dogania lidera; SL/TP w ATR).

| Instrument · strategia · TF | Nauka PF (n) | Sprawdzian PF (n) · traf. | Siatka spr PF ≥ 1 | Decyzja |
|---|---|---|---|---|
| **XAUUSD · dywergencja · H1** (lb 4, k 3, SL 2,5 / TP 3 ATR, 48 h) | 1,38 (280) | **1,15 (106)** · 48% | **132/144** | ✅ na demo: `LAB_Dyw_XAU` (830230) |
| XAUUSD · dywergencja · M15 | 1,13 (535) | 1,13 (69) | 123/144 | kandydat (ten sam pomysł, H1 wystarczy) |
| **GBPUSD · seria · H1** (N 6, k 1,5, TP 0,618, 24 h) | 1,20 (118) | **1,47 (53)** | **62/72** | ✅ kandydat – czeka na wolny slot (10/10) |
| USDJPY · seria · M15 | 1,17 (217) | 1,37 (64) | 44/72 | kandydat słabszy |
| EURUSD · seria · H1 | 1,19 (159) | 1,21 (59) · ΣR −1,2 | 54/72 | ❌ ΣR ujemne |
| XAGUSD · dywergencja · M15 | 1,96 (300) | 1,61 (24) | 26/144 | ❌ jeden szczęśliwy punkt |
| XAGUSD · seria · M15 | 1,36 (161) | 1,48 (60) | 32/72 | ❌ ΣR +0,4 – nic |
| XAUUSD · seria · M15 / H1 | 1,70 / 1,71 | 0,84 / 0,90 | 45 / 24 z 72 | ❌ złoto w trendzie nie oddaje serii |
| US500 / US30 · seria | 0,99–1,25 | 0,79–1,07 | – | ❌ (i tak handel indeksami wyłączony na koncie botów) |
| AUDUSD / GBPUSD M15 · seria | 1,06–1,29 | 0,56–0,90 | – | ❌ |

Wniosek: przeciw serii działa tylko na wolniejszym forexie (GBP H1), na złocie w trendzie 2026 – nie. Dywergencja złoto–srebro to pierwszy pomysł z korelacji, który przechodzi na całej siatce (132/144) – mała przewaga (PF 1,15), ale stabilna.


## Noc 10 (27.11.2026) – nowe pomysły: TYDZIEŃ i NR7

Skrypt `C:\Hexa\lab\narzedzia\backtest_noc10.py`, wyniki `logi\backtest_runda10.json`. MT5 H1/D1 (od 03.2025), koszt = spread świecy, wyjście tylko SL/TP, nauka 70% / spr 30%.

- **TYDZIEŃ** – w czwartek 10:00 (czas serwera) wejście w kierunku ruchu tygodnia, jeśli od otwarcia poniedziałku ≥ k × ATR(D1); SL/TP w ATR(D1). 27 wariantów/instrument. Siatka spr ≥ 1: XAU 15/27, EUR 18/27, GBP 15/27, XAG 6/27, AUD 3/27, **JPY 0/27** → niestabilne, nauka ~1,0–1,1 → ❌ odrzucony.
- **NR7 (Crabel)** – dzień z najwęższym zakresem z 7 → następnego dnia H1 zamknięcie za zakresem ± 0,25 zakresu, SL po drugiej stronie, TP 1,5R. Siatka spr ≥ 1: **XAU 12/12, EUR 12/12, GBP 11/12, JPY 10/12, XAG 9/12, AUD 9/12** – najszersza stabilność z dotychczasowych pomysłów.

| NR7 (TP 1,5R, bufor 0,25) | Nauka PF (n) | Sprawdzian PF (n) · ΣR |
|---|---|---|
| XAUUSD | 1,23 (137) | 1,12 (56) · +3,9R |
| XAGUSD | 1,15 (131) | **1,52** (57) · +14,7R |
| USDJPY | 1,33 (136) | **1,43** (53) · +11,7R |
| EURUSD | 0,95 (118) | 1,13 (51) · +3,8R |
| GBPUSD | 0,77 (135) | 1,19 (56) · +6,0R |
| AUDUSD | 1,06 (125) | 1,02 (51) · +0,6R |

→ kandydat `LAB_NR7` (XAU + XAG + USDJPY, TP 1,5R; razem spr ~166 tr., +30R, nauka i spr ≥ 1 na każdym). **Nie uruchomiony** – 12 aktywnych botów (limit), czeka na slot razem z GBPUSD seria H1.
