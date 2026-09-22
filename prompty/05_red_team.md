# Etap 05 — Red team

Uruchamiaj w nowej sesji. Twoja rola: obalić, a nie potwierdzić.

**Wejście:** `03_analiza.md`, `04_prognozy_A.md`, `04_prognozy_B.md`, `04_prognozy_C.md`, `02_fakty/*.md`, `rejestr/pytania.csv`.

**Zabronione:** pliki `06_*`, `07_zalacznik_benchmarki.md`, `rejestr/benchmarki.csv`, domeny z CLAUDE.md p. 9.

## Zadania

1. **Dziesięć najsłabszych punktów analizy.** Szukaj w szczególności:
   - założeń bez dowodu,
   - źródeł tylko jednej strony,
   - zachodniego skrzywienia i błędu lustrzanego odbicia,
   - przereagowania na nagłówki,
   - pominiętych aktorów.
   
   Dla każdego punktu: dowód albo argument oraz wpływ na konkretne pytania.
2. **Przegląd prognoz.** Policz AGR (średnia A, B, C) dla każdego pytania i wskaż pytania, w których:
   - AGR jest niespójny z faktami z `02_fakty`,
   - występuje niespójność logiczna między pytaniami (np. P(A i B) > P(A), sprzeczne pytania z sumą > 1),
   - soczewki różnią się o więcej niż 0.30 — wyjaśnij, która ma lepsze podstawy.
3. **Propozycje korekt AGR.** Każda korekta musi mieć konkretny dowód albo wskazany błąd logiczny. Limit: ±0.15 na pytanie. Zakaz korekt „dla bezpieczeństwa” i ciągnięcia w stronę 0.5 bez powodu.
4. **Test skrzywienia kierunkowego.** Porównaj średnie AGR z `p_status_quo` w grupach `czyj_sukces`. Czy prognozy systematycznie faworyzują którąś stronę? Wskaż pytania, które to powodują.
5. **Spójność ze scenariuszami.** Czy prognozy pytań są zgodne z prawdopodobieństwami scenariuszy, które zapowiada analiza?

## Wyjście

`05_red_team.md` z tabelą korekt: ID | AGR | proponowana korekta | AGR_RT | uzasadnienie | typ (dowód / logika / spójność).

Commit: `wydanie-NN etap-05`.
