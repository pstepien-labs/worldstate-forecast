# Przegląd kwartalny metodologii (ok. 21.12.2026)

**Cel:** wydobyć z danych metodologię wnioskowania na kolejny kwartał — na podstawie pomiaru, nie wrażeń.

## Zadania

1. **Pełne wyniki** (skrypt `narzedzia/wyniki.py`, wszystkie wydania kwartału):
   - Brier i BSS dla AGR_RT względem status quo i względem tłumu (tylko DOKLADNE),
   - kalibracja,
   - przebiegi A / B / C / AGR / AGR_RT — czy agregacja pomaga, czy red team pomaga,
   - wektory, horyzonty, klastry (z wagą 1 na klaster),
   - błąd kierunkowy według `czyj_sukces`,
   - jeśli dane pozwalają: trafność pytań, których kluczowe fakty miały perspektywę A, vs pozostałych.
2. **Niepewność wyników.** Dla każdej porównywanej różnicy (np. soczewka A vs B) policz przedział ufności metodą bootstrap (co najmniej 2000 losowań, losowanie po klastrach). Jeśli przedział obejmuje zero — wniosek brzmi „brak dowodu różnicy”.
3. **Dziesięć największych błędów** (najwyższy Brier AGR_RT). Klasyfikacja przyczyny:
   - brak informacji,
   - zły model aktora,
   - przereagowanie na nagłówek,
   - niedoreagowanie,
   - zły timing,
   - niejednoznaczne pytanie.
4. **Ochrona przed przeuczeniem.** Oceń, czy kwartał był zdominowany przez jeden kryzys lub klaster. Wskaż, których wniosków nie należy uogólniać.
5. **Propozycja metodologii v1.1.** Najwyżej 2–3 zmiany. Każda z uzasadnieniem w danych i przewidywanym efektem. Punkty odniesienia pozostają bez zmian. Przykłady dozwolonych zmian:
   - wagi soczewek w agregacji,
   - wyłączenie soczewki bez wartości dodanej,
   - nowa soczewka,
   - zmiana limitu korekt red teamu,
   - zmiana rozkładu horyzontów,
   - zmiana PIR.
6. **Nowy panel** na kolejny kwartał: 40 pytań, 5 na wektor.
7. **Akceptacja.** Przedstaw propozycje użytkownikowi. Po akceptacji utwórz `metodologia/metodologia_v1.1.md` jako nowy plik — v1.0 zostaje bez zmian.

## Wyjście

`przeglady/2026-Q4.md` oraz, po akceptacji, `metodologia/metodologia_v1.1.md`. Commit i tag `przeglad-2026-Q4`.
