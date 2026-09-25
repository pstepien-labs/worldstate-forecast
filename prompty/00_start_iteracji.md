# Etap 00 — Start wydania

**Parametry (z argumentów komendy):** `DATA_STANU` (RRRR-MM-DD) i `NR` (dwie cyfry, np. 01).

## Zadania

1. Jeśli katalog nie jest repozytorium git: `git init` i commit „stan początkowy”.
2. Utwórz katalog `wydania/<DATA_STANU>_wydanie-<NR>/` z podkatalogiem `02_fakty/` oraz plik `dziennik.md` (godzina startu etapu 00).
3. Zaktualizuj `wydania/AKTUALNE.md`: NR, DATA_STANU, OKRES_OD (data stanu poprzedniego wydania), KATALOG bieżący, KATALOG poprzedni.
4. Wczytaj poprzednie wydanie: blok stanu i raport. Dla wydania 01 punktem wyjścia jest `wydania/2026-09-21_wydanie-00/stan_00.md` (oraz PDF w tym samym katalogu, jeśli potrafisz go odczytać).
5. Sprawdź integralność rejestru: nagłówki CSV zgodne z szablonem, unikalne ID pytań, brak prognoz do nieistniejących pytań, brak zmian w historii (porównaj z poprzednim tagiem git, jeśli istnieje). Problemy zapisz — historii nie naprawiaj.
6. Wypisz pytania do rozstrzygnięcia w etapie 01: status AKTYWNE i termin ≤ DATA_STANU, albo zdarzenie mogło już zajść.
7. Zbierz kalendarz na 6 tygodni naprzód (szczyty, posiedzenia banków centralnych, wybory, terminy traktatowe i sankcyjne, wygasające zawieszenia). Każdą datę potwierdź w sieci.
8. Szybki przegląd nagłówków (najwyżej 15 wyszukiwań): które wektory i regiony zmieniły się najbardziej od poprzedniego wydania. Na tej podstawie ustal priorytety dla etapu 02.

## Wyjście

`00_plan.md`: parametry wydania; lista pytań do rozstrzygnięcia; kalendarz; PIR (bez zmian, z metodologii); priorytety zbierania dla grup G1–G4; problemy z rejestrem.

**Dziennik:** wpis etapu w `dziennik.md` podaje godzinę rozpoczęcia i zakończenia etapu (dd.mm.rrrr gg:mm).

Commit: `wydanie-NN etap-00`.

**Kryterium ukończenia:** istnieje `00_plan.md`, `AKTUALNE.md` jest zaktualizowany, commit wykonany.
