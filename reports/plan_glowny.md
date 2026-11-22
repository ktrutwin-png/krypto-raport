# PLAN GŁÓWNY – jedna tablica całej firmy (prowadzi 🗂️ Planista, od 22.11.2026)
Szef 22.11: „poukładaj nasze plany, sprawdzaj co mamy do zrobienia, chcę te informacje dostawać w briefingu”.
Źródła: plan_wzrostu.md, plan_boty.md, plan_hexa_os.md, plan_skanery.md, plan_biznes.md, zgloszenia.md, tools/hexa_seria/README.md, dziennik_zespolu.md.
Planista codziennie 07:31 aktualizuje ten plik i C:\Hexa\plan\na_dzis.json (sekcja PLAN DNIA w briefingu 8:00: max 3 rzeczy dla szefa + 4 dla zespołu).

## 1. CZEKA NA SZEFA (decyzja/logowanie) – wąskie gardło
- 11 zgłoszeń „czeka na wdróż szefa” (Z005, Z013, Z017, Z020, Z022, Z023, Z026, Z028, Z033, Z037, Z038, Z039) – poprawki gotowe, brak tylko „wdróż”.
- Pon. 23.11 przy laptopie: logowanie MQL5 Gold Reaper; porządek ze starym kontem ElevenLabs.
- Pt. 27.11 rano: przypomnienie o prawdziwym koncie MT5.

## 2. TEN TYDZIEŃ (zespół)
- Sob. 28.11 21:00: Ep.2 „Szklane Miasto” (produkcja czw. 19:41, kontrola pt. 17:47 + Mózg pt. 19:00) – IG, YT, X.
- 23–29.11: test A/B tła Reelsów (Laboratorium), potem test „Hexa pyta w 1. sekundzie”.
- Raport tygodniowy: ramka WYNIKI (IG/YT/X).
- Z029 Hexa Indeksy (VOO) – sprawdzić 23.11 po otwarciu USA.

## 3. CO JESZCZE MOŻNA POPRAWIĆ (lista Mózgu 22.11)
- Pilnowanie dostarczenia: każda wysyłka Telegram w C:\Hexa\wysylki.log – brak „OK” dla briefingu/raportu = alarm i ponowienie (wdrożone 22.11).
- ZASADA SZEFA 22.11: NIC na laptopie – każde zadanie i działanie na serwerze/w chmurze; ma działać przy zamkniętym laptopie i padniętym telefonie. Z022: prompty → serwer (partia 2), odpięcie zadań przypiętych do DESKTOP-20N25SR – pon. 23.11 z szefem w aplikacji desktop.
- Za dużo otwartych rozkazów: plan_wzrostu 29 otwartych – Planista co tydzień zamyka nieaktualne (R27/R34 zastąpione R40 itd.).
- X: codzienna obecność (nie tylko odcinki) – 1 post dziennie z najlepszego Reela (do testu w Laboratorium).

- [ ] 2026-11-22 (Mózg, szef: „sprawdź i w razie dobrej jakości wdróż”): TEST RUCHOMYCH GRAFIK – darmowy image-to-video Wan na serwerze (C:\Hexa\generatory\wan_api.txt) na 3 grafikach z banku (5 s, 9:16). Kryteria: ostrość, brak zniekształceń i napisów, czas < 5 min/scena. Jeśli OK → wdrożyć do kino.py (1–2 sceny ruchome na Reel), linia w zmiany.md. Jeśli nie → zostaje ruch kamery.
- [x] 2026-11-22 (Mózg, propozycje szefa z IG) WYKONANE: Analityk ma 3 kontrole (pkt A8); context7 = konektor do podłączenia przez szefa; claude-mem ODRZUCONE (działa tylko w lokalnym Claude Code, nasi agenci startują w chmurze – pamięć mamy w repo + pamięci Claude). Pierwotnie:: TEST claude-mem (pamięć agentów) i context7 (świeże dokumentacje) na serwerze – wdrożyć tylko jeśli realnie pomagają; 3 komendy tradingowe dla Analityka (risk-check, mistake-review, pre-market) dopisać do jego zadania jako kroki. ODRZUCONE: 50 agentów marketingu (dubel zespołu), reszta listy 32 repo (mamy odpowiedniki).
