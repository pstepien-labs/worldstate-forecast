# Współpraca / Contributing

Język pracy projektu to polski; zgłoszenia po angielsku też są w porządku. / The project works in Polish; issues in English are welcome too.

## Co jest mile widziane / Welcome

- Zgłoszenia błędów w `narzedzia/wyniki.py` (z przykładowym wierszem CSV). / Bug reports for the scoring script, with a sample CSV row.
- Wskazanie błędnego faktu lub martwego linku w wydaniu (data, wydawca, URL poprawnego źródła). / Reports of wrong facts or dead links, with a corrected source.
- Propozycje źródeł do `zrodla/mapa_zrodel.md`, zwłaszcza perspektywy strony-aktora (A) i trzeciej (T). / Source suggestions, especially actor-side (A) and third-party (T) perspectives.
- Propozycje zmian metodologii — jako issue; trafiają do przeglądu kwartalnego. / Methodology proposals — as issues; they are considered at the quarterly review.

## Zasady / Rules

1. **Rejestr tylko do dopisywania.** Pull requesty edytujące lub usuwające istniejące wiersze w `rejestr/prognozy.csv`, `benchmarki.csv`, `rozstrzygniecia.csv` nie będą przyjmowane. Korekta rozstrzygnięcia = nowy wiersz z wyższą `wersja`. / **Append-only registry** — PRs that edit or delete existing rows will not be merged.
2. **Metodologia v1.0 jest zamrożona** do przeglądu kwartalnego (`metodologia/zmiany_metodologii.md`). / **Methodology v1.0 is frozen** until the quarterly review.
3. **Bez przepisywania historii git** (rebase, force-push) na gałęzi głównej. / **No history rewrites** on the main branch.
4. Formaty zgodnie z `CLAUDE.md` §5: CSV z separatorem `;`, UTF-8 z BOM, prawdopodobieństwa 0.01–0.99. / Formats per `CLAUDE.md` §5.
5. Bez dodatkowego oprogramowania — `wyniki.py` pozostaje jedynym skryptem, tylko biblioteka standardowa Pythona. / No extra software — `wyniki.py` stays the only script, stdlib only.

## Uruchomienie własnego wydania / Running your own issue

Zob. `README.md` → „Jak uruchomić jedno wydanie”. Fork jest najlepszym sposobem na prowadzenie niezależnej serii prognoz. / See the README; forking is the best way to run an independent forecast series.
