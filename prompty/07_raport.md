# Etap 07 — Raport wydania

**Wejście:** wszystkie pliki bieżącego wydania, poprzedni raport, `01_wyniki.md`.

## Produkty

1. **`07_raport.md`** — raport według struktury z metodologii §11.
   - Sekcja **0 (Wyniki trafności)**, od wydania 02: najważniejsze liczby z `01_wyniki.md` — liczba rozstrzygniętych pytań, Brier i BSS dla AGR_RT vs status quo, najlepsza i najgorsza soczewka (z adnotacją „orientacyjnie” poniżej 30 pytań), błąd kierunkowy.
   - Sekcja **H**:
     - scenariusze w trzech horyzontach z prawdopodobieństwami, czynnikami uruchamiającymi i sygnałami z datami;
     - pełna lista prognoz AGR_RT pogrupowana według wektorów: ID, pytanie, termin, AGR_RT, rozrzut soczewek (min–max), zmiana względem poprzedniego wydania.
   - **Nie umieszczaj w raporcie głównym prognoz tłumu ani rynków.**
   - Sekcja **K** w formacie K.1–K.7, gotowym do wklejenia do raportu krajowego.
2. **`07_zalacznik_benchmarki.md`** — porównanie z tłumem i rozbieżności (z `06_benchmarki.md`). Ten plik jest zakazany dla etapów 03–05 we wszystkich przyszłych wydaniach.
3. **`07_blok_stanu.md`** — blok L w formacie jednej linii na wskaźnik. Rozszerzenie względem wydania 00: `pytania_aktywne=… | rozstrzygniete_lacznie=… | Brier_AGR_RT=… | BSS_vs_SQ=…`.
4. **`07_raport.pdf`** — jeśli w systemie jest `pandoc` albo inny konwerter; w przeciwnym razie tylko Markdown i adnotacja w `dziennik.md`.

## Zasady redakcyjne

- Fakty z poprzedniego wydania przenoś tylko wtedy, gdy etap 02 je potwierdził; oznacz je „potwierdzone bez zmian, dd.mm.rrrr”. Fakty usunięte wypisz w sekcji J z powodem.
- Wszystkie reguły z CLAUDE.md p. 3: rozróżnienie fakt / ocena / prognoza, wydawca i data przy każdym fakcie, dwie interpretacje przy sporach, liczby zamiast przymiotników.
- Tekst słowny o prawdopodobieństwach — według skali z metodologii §10.
- Długość: tekst główny 15–25 stron A4; lista prognoz jako aneks.
- Bez waty i powtórzeń. Tytuły sekcji dokładnie jak w metodologii, żeby wydania były porównywalne.

Commit: `wydanie-NN etap-07`.
