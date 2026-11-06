# PLAN AGENTA SKANERY (7.11–7.12.2026) – czyta go zadanie „Opiekun Skanera Claude”
Szef 7.11.2026: „ułóż plan każdemu agentowi… chcę widzieć wyniki od każdego agenta”. Skaner tylko wysyła sygnały na Telegram – nie handluje.

## Skanery w zakresie
skaner_dzienny.py (MT5, D1, pętla co 2 min) · IB Skaner (paper) – tylko obserwacja jego sygnałów.

## Cele na 30 dni (ocena 7.12.2026)
- Dziennik wyników sygnałów: każdy wysłany sygnał zapisany z wynikiem (SL/TP trafiony, wynik w R) w C:\Users\ktrut\Claude-telefon\trading\sygnaly_wyniki.csv.
- Średni wynik wysłanych sygnałów > 0 R po kosztach; rynek/strategia z ujemnym R po ≥ 10 sygnałach → usunąć z CFG (z komentarzem).
- Zero przestojów > 1 dnia; zero duplikatów (jedna wiadomość na sygnał).
- Co najmniej 1 przyjęte ulepszenie w miesiącu (reguły testu z zadania).

## Kolejność pracy
- Tydzień 1 (8.11): uruchom dziennik wyników sygnałów (osobny skrypt, nie zmienia logiki skanera) i uzupełnij go wstecz z logu.
- Tydzień 2 (15.11): ranking rynków/strategii wg R; usuń słabe.
- Tydzień 3 (22.11): filtr zmienności/trendu dla najsłabszej strategii.
- Tydzień 4 (29.11): test nowego rynku dla najlepszej strategii.

## Postęp
- 2026-11-07: start planu
