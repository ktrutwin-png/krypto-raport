# Nauka zespołu (szef 11.11: „lepsze szkolenie dla ciebie i dla agentów”)

Pętla uczenia się z własnych błędów. Każdy agent (Reel, Raport 18, Shorts, Weekly, Opiekun, Skanery, Inspektor, Mózg) korzysta z tych samych trzech plików:

| plik | co tu trafia |
|---|---|
| `LEARNINGS.md` | poprawka od szefa, lepszy sposób, wiedza, której brakowało |
| `ERRORS.md` | błąd narzędzia/skryptu/API i jak go obejść |
| `ZYCZENIA.md` | rzecz, o którą szef prosił, a której jeszcze nie umiemy |

## Zasady (krótko)
1. **Przed zadaniem**: przeczytaj wpisy ze swojego działu (szukaj po tagu, np. `[reel]`, `[3d]`, `[strona]`). Nie powtarzaj błędu, który już tu jest.
2. **Po zadaniu**: jeśli coś poszło źle albo szef coś poprawił – dopisz JEDEN wpis na dole właściwego pliku, w formacie:
   ```
   ### L-RRRRMMDD-NN [dział] krótki tytuł
   - Co się stało: …
   - Wniosek / zasada: … (jedno zdanie, które da się zastosować)
   - Klucz: slowo-klucz-wzorca   (ten sam klucz dla powtórek tego samego problemu)
   - Powtórzenia: 1   (jeśli wpis już jest – zwiększ licznik zamiast dublować)
   - Status: nowy
   ```
3. Bez danych prywatnych szefa, haseł, kluczy, kwot z kont. Bez tematu książki i KenT.
4. **Promocja** (Inspektor w niedzielę, skill `learning-aggregator` + `self-improvement`): wzorce z licznikiem ≥ 3 → propozycja jednej zasady (1–3 zdania) do pliku, który dany agent czyta (plan_wzrostu.md, tools/kino/README.md, tools/okladki/STYL.md …). Mózg zatwierdza i wpisuje; wpis dostaje `Status: wypromowany → <plik>`. **Wszystko, co dotyczy botów/tradingu – tylko po „wdróż” szefa.**
5. Ważna wypromowana zasada z jasnym „zdał/nie zdał” → przypadek testowy w `TESTY.md` (skill `eval-creator`); Inspektor co niedzielę sprawdza, czy zasady dalej są przestrzegane.
6. Zanim agent napisze „zrobione/działa” – dowód (skill `verification-before-completion`: klatki filmu, kod wyjścia, zrzut strony). Przy błędzie najpierw przyczyna, potem poprawka (`systematic-debugging`).
