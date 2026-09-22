# Etap 04 — Prognozy (trzy niezależne sesje: A, B, C)

Parametr: `SOCZEWKA` = A, B albo C (z argumentu komendy). Każdą soczewkę uruchamiaj w **nowej sesji** (po `/clear`), żeby nie przenosić kontekstu między soczewkami.

## Dozwolone wejście

- `CLAUDE.md`, `metodologia/metodologia_v1.0.md` (zwłaszcza §4),
- `02_fakty/*.md`, `03_analiza.md` bieżącego wydania,
- `rejestr/pytania.csv` (pytania AKTYWNE),
- `rejestr/prognozy.csv` — **wyłącznie wiersze z przebiegiem równym Twojej soczewce** (dla ciągłości własnych prognoz).

## Zabronione

- pliki `04_prognozy_*` innych soczewek, `05_*`, `06_*`, `07_zalacznik_benchmarki.md` dowolnego wydania,
- `rejestr/benchmarki.csv`, wiersze AGR i AGR_RT w `prognozy.csv`,
- domeny z CLAUDE.md p. 9 i wyszukiwania fraz typu „odds”, „prediction market”, „szanse według rynku”.

## Instrukcja soczewki

**A — „Rozgrywka mocarstw”.** Dla każdego pytania:
1. kto decyduje o wyniku;
2. interesy i wypłaty każdej strony;
3. zdolności i ograniczenia;
4. alternatywy;
5. który ruch jest dla kogo opłacalny i jaka równowaga z tego wynika do terminu;
6. co musiałoby się zmienić, żeby równowaga się przesunęła.

**B — „Widok z zewnątrz”.** Dla każdego pytania:
1. wskaż klasę odniesienia i częstość bazową (jawnie);
2. uwzględnij trwałość status quo i czas pozostały do terminu (przy stałym tempie: p ≈ 1 − (1 − r)^t);
3. dopiero na końcu, ostrożnie, skoryguj o specyfikę przypadku.

Unikaj narracji; jeśli nie ma sensownej klasy odniesienia, powiedz to.

**C — „Ograniczenia wewnętrzne i ekonomiczne”.** Dla każdego pytania:
1. polityka wewnętrzna i kalendarze wyborcze;
2. bodźce osobiste przywódców (legitymizacja, relacje personalne);
3. budżety, rynki, logistyka;
4. procedury i terminy instytucjonalne (np. notyfikacja w Kongresie, kalendarz budżetowy, posiedzenia rad).

Nie mieszaj soczewek. Jeśli Twoja soczewka nic nie mówi o danym pytaniu, zaznacz to i daj prognozę z pewnością analityczną „niska”.

## Zadania

1. Dla **każdego** aktywnego pytania podaj:
   - p (0.01–0.99),
   - uzasadnienie w 1–2 zdaniach w logice soczewki,
   - kluczowy wskaźnik,
   - pewność analityczną,
   - zmianę względem własnej poprzedniej prognozy i jej powód.
2. Możesz dociągnąć brakujące fakty (najwyżej 20 wyszukiwań). Zapisz je w pliku w sekcji „Fakty dodatkowe” z URL.
3. Zapisuj `04_prognozy_<SOCZEWKA>.md` (tabela) co 10 pytań.
4. Na końcu dopisz wiersze do `rejestr/prognozy.csv` z przebiegiem `<SOCZEWKA>`.

Commit: `wydanie-NN etap-04<SOCZEWKA>`.

**Kryterium ukończenia:** każde aktywne pytanie ma prognozę tej soczewki w tym wydaniu.
