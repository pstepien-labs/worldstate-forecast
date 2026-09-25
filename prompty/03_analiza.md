# Etap 03 — Analiza i bank pytań

**Wejście:** `02_fakty/G1–G4.md`, `00_plan.md`, poprzedni raport i blok stanu, metodologia.

Jeśli którakolwiek grupa w `dziennik.md` jest oznaczona jako niepełna — najpierw to zgłoś i zapytaj użytkownika, czy kontynuować.

## Część 1: Analiza

1. **Szkic sekcji A–G** według metodologii §11. Wnioski oznaczone słowem OCENA, z pewnością analityczną. Każda z sekcji B–F kończy się akapitem „Mechanizm” (jak zdarzenia wpływają na inne sekcje) i linią „Dla Polski”.
2. **Porównanie z poprzednim wydaniem.** Dla każdej oceny poprzedniego wydania: potwierdzona / obalona / nierozstrzygnięta — z dowodem.
3. **Sprawdzenie kluczowych założeń.** 5–8 założeń obecnego obrazu świata. Dla każdego: na czym się opiera, co by je obaliło, aktualny stan.
4. **Analiza konkurencyjnych hipotez** dla trzech najważniejszych pytań otwartych: 3–4 hipotezy, macierz dowodów, które dowody hipotezy wykluczają (nie tylko które je wspierają).
5. **Matryca wskaźników i ostrzeżeń:** wskaźnik → próg → scenariusz, który wspiera. Zaktualizuj względem poprzedniego wydania.
6. **Test lustra:** wskaż miejsca, gdzie analiza może zakładać, że inny aktor liczy koszty i zyski tak jak Zachód, oraz miejsca, gdzie opiera się tylko na źródłach jednej strony.

## Część 2: Bank pytań

- **Wydanie 01:** ustal panel stały — 40 pytań, po 5 na każdy z 8 wektorów. Punkt wyjścia: `rejestr/pytania_propozycje_z_wydania_00.csv`. Każdą propozycję zweryfikuj (czy nie jest już rozstrzygnięta, czy kryterium jest jednoznaczne, czy źródło rozstrzygnięcia istnieje), popraw albo odrzuć, uzupełnij brakujące wektory.
- **Każde wydanie:** dodaj 20–40 pytań swobodnych, głównie z „Kandydatów na pytania” z etapu 02. Zastąp rozstrzygnięte pytania panelu nowymi z tego samego wektora i klastra.
- Dla każdego nowego pytania wypełnij: `p_status_quo` (reguła mechaniczna z §3.5), `czyj_sukces`, `pir`, `klaster`, `kluczowy_wskaznik`. **Bez prognozy.**
- Sprawdź proporcje horyzontów (§3.3) i pokrycie wektorów.
- Dopisz pytania do `rejestr/pytania.csv` (status AKTYWNE; ID kolejne: Q-0001, Q-0002…).

## Wyjście

- `03_analiza.md` — części 1.1–1.6.
- `03_bank_pytan_zmiany.md` — nowe pytania, zastąpienia, odrzucone propozycje z powodem, statystyka horyzontów i wektorów.

## Zakazy

Żadnych prawdopodobieństw poza mechanicznym `p_status_quo`. Żadnych benchmarków ani domen z CLAUDE.md p. 9.

**Dziennik:** wpis etapu w `dziennik.md` podaje godzinę rozpoczęcia i zakończenia etapu (dd.mm.rrrr gg:mm).

Commit: `wydanie-NN etap-03`.
