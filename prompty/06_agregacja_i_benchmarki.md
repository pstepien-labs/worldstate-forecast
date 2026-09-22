# Etap 06 — Agregacja, zamrożenie, benchmarki

Kolejność kroków jest obowiązkowa.

## Krok 1: Agregacja

1. Dla każdego aktywnego pytania policz AGR = średnia A, B, C z tego wydania. Jeśli brakuje którejś soczewki — przerwij i zgłoś (nie licz z dwóch).
2. Zastosuj korekty z `05_red_team.md`. Odrzuć korekty przekraczające ±0.15 albo bez dowodu i wypisz je z powodem. AGR_RT = AGR + zaakceptowana korekta; bez korekty AGR_RT = AGR. Przytnij do zakresu 0.01–0.99.
3. Dopisz do `rejestr/prognozy.csv` wiersze z przebiegami AGR i AGR_RT.
4. Sprawdź regułę trywialności (§3.8) i zapisz wynik.

## Krok 2: Zamrożenie

Commit z komunikatem `wydanie-NN prognozy zamrożone`. Hash commita zapisz w `dziennik.md`. Od tej chwili prognozy tego wydania są niezmienne.

## Krok 3: Benchmarki (dopiero teraz)

1. Dla aktywnych pytań wyszukaj odpowiedniki na: Metaculus, Good Judgment Open, Polymarket, Kalshi, Manifold, RAND Forecasting Initiative.
2. Zapisz do `rejestr/benchmarki.csv`: ID pytania, wydanie, datę, źródło, p, URL, dopasowanie (DOKLADNE / PRZYBLIZONE), uwagi. Dla rynków — wolumen lub płynność, jeśli widoczne.
3. Nie zmieniaj żadnej prognozy.

## Wyjście

- `06_agregacja.md` — tabela AGR i AGR_RT, odrzucone korekty, wynik testu trywialności.
- `06_benchmarki.md` — lista dopasowań i rozbieżności |AGR_RT − tłum| ≥ 0.20, z krótką hipotezą o przyczynie każdej. To materiał do przeglądu, **nie** podstawa zmiany prognoz.

Commit: `wydanie-NN etap-06`.
