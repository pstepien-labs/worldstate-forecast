# Etap 01 — Rozstrzygnięcia i wyniki

**Wejście:** `00_plan.md` (lista pytań do rozstrzygnięcia), `rejestr/*.csv`, metodologia §7–§8.

W wydaniu 01 zwykle nie ma nic do rozstrzygnięcia. Wtedy utwórz `01_rozstrzygniecia.md` i `01_wyniki.md` z adnotacją „brak rozstrzygnięć w tym wydaniu”, zrób commit i zakończ.

## Zadania

1. Dla każdego pytania z listy ustal:
   - wynik: 1 (TAK), 0 (NIE) albo ANUL (z uzasadnieniem według §3.7),
   - datę rozstrzygnięcia,
   - dowód: URL, wydawca, data publikacji; dla pytań z PIR — drugie, niezależne źródło,
   - pewność rozstrzygnięcia (niska / średnia / wysoka).
   
   Pytanie, którego termin nie minął, a zdarzenie nie zaszło, pozostaje AKTYWNE.
2. Oznacz WERYFIKUJ: rozstrzygnięcia niejednoznaczne i sporne oraz losowe 20% pozostałych. Losowanie wykonaj w Pythonie z ziarnem równym numerowi wydania i zapisz listę wylosowanych ID.
3. Dopisz wiersze do `rejestr/rozstrzygniecia.csv` (wersja = 1). Zmień `status` w `rejestr/pytania.csv` na ROZSTRZYGNIETE albo ANULOWANE (tylko to pole i ewentualnie `uwagi`).
4. Policz wyniki skryptem `narzedzia/wyniki.py` (istnieje; uruchom `python3 narzedzia/wyniki.py --out <KATALOG>/01_wyniki.md`). Nie modyfikuj skryptu bez akceptacji użytkownika; jeśli znajdziesz błąd — opisz go w `dziennik.md`. Skrypt liczy zakres z metodologii §8:
   - Brier i BSS dla przebiegów A, B, C, AGR, AGR_RT,
   - BSS vs `p_status_quo` oraz vs tłum (tylko dopasowania DOKLADNE z `benchmarki.csv`),
   - kalibracja w przedziałach co 10 p.p.,
   - błąd kierunkowy wg `czyj_sukces`,
   - wyniki z wagą 1 na klaster,
   - rozbicie według wektorów i horyzontów.
   
   Skrypt bierze pod uwagę wiersz z najwyższą `wersja` dla danego pytania, a pytania z flagą WERYFIKUJ bez zatwierdzenia użytkownika pomija i wypisuje osobno.

## Wyjście

- `01_rozstrzygniecia.md` — lista rozstrzygnięć z dowodami, wyraźnie wydzielona sekcja „DO WERYFIKACJI PRZEZ UŻYTKOWNIKA”.
- `01_wyniki.md` — tabele wyników z liczbą rozstrzygniętych pytań i adnotacją, jeśli jest ich mniej niż 30 („wyniki orientacyjne”).

**Dziennik:** wpis etapu w `dziennik.md` podaje godzinę rozpoczęcia i zakończenia etapu (dd.mm.rrrr gg:mm).

Commit: `wydanie-NN etap-01`.

**Po etapie użytkownik** przegląda flagi WERYFIKUJ. Korekty dopisuje jako nowy wiersz w `rozstrzygniecia.csv` z wyższą `wersja` i `zatwierdzone_przez_uzytkownika = T`.
