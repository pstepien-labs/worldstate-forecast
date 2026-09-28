# Log of process and methodology changes

Entries only after user approval. Methodology v1.0 stays frozen until the quarterly review — this file records only process fixes (e.g. clarifying a stage instruction) and, after the quarterly review, a pointer to the new methodology version.

| Date | Version | File | Change | Rationale | Approved by |
|---|---|---|---|---|---|
| 25.09.2026 | v1.0 (process fix) | prompts/04_forecasts.md | Facts fetched in stage 04 are recorded as full records per CLAUDE.md item 3.2 (date, actor, action, target, vector, region, status, publisher, URL, source rating, perspective, PIR), numbered within the lens: A-01…, B-01…, C-01… | Stage 08 check of edition 01: records "A-add.", "B-add." and C-01…C-14 lacked source rating, perspective and PIR; "A-add." references in the report did not point to a single record (08_quality_control.md item 1) | user (25.09.2026) |
| 25.09.2026 | v1.0 (process fix) | prompts/04_forecasts.md; edition log.md | Stage 04 log entries without p ranges and without search topics (only: number of forecasts, number of searches, incidents, gaps). A lens in stage 04 does not read other lenses' stage 04 entries in the log | Stage 08 check of edition 01: the log, read by subsequent lenses, revealed other lenses' search topics and p ranges (exposure of 04-C; 08_quality_control.md item 5) | user (25.09.2026) |
| 25.09.2026 | v1.0 (process fix) | prompts/00–08; edition log.md | Each stage entry in the log gives the start and end time of the stage (dd.mm.yyyy hh:mm) | Stage 08 check of edition 01: log without stage times; times reconstructed from git history (08_quality_control.md item 8) | user (25.09.2026) |
| 28.09.2026 | v1.0 (translation, no change of method) | whole repository | Repository translated from Polish into English: files, directories, prompts, registry (headers, codes and free text), edition 00 and 01 outputs. Method, numbers, IDs, dates and probabilities unchanged. One-off exception to the append-only rule (CLAUDE.md item 3.7): text fields of existing registry rows were translated in place; a field-by-field check confirmed that all IDs, dates, probabilities and p_status_quo values are identical. Polish originals: git tag `wydanie-01`. Code mapping below | User request to make the project English-only | user (28.09.2026) |

## Code mapping of the English migration (28.09.2026)

Stage 08 of edition 02 compares the registry with the migration commit (`REGISTRY_BASELINE` in `editions/CURRENT.md`), not with tag `wydanie-01`, because every row of the registry changed language in the migration.

| Field | Polish (before) | English (after) |
|---|---|---|
| Paths | `rejestr/`, `wydania/`, `prompty/`, `metodologia/`, `zrodla/`, `narzedzia/wyniki.py`, `przeglady/` | `registry/`, `editions/`, `prompts/`, `methodology/`, `sources/`, `tools/scores.py`, `reviews/` |
| Registry files | `pytania.csv`, `prognozy.csv`, `benchmarki.csv`, `rozstrzygniecia.csv`, `zrodla.csv`, `pytania_propozycje_z_wydania_00.csv` | `questions.csv`, `forecasts.csv`, `benchmarks.csv`, `resolutions.csv`, `sources.csv`, `question_proposals_edition_00.csv` |
| Edition files | `AKTUALNE.md`, `dziennik.md`, `01_wyniki.md`, `02_fakty/`, `07_raport.md`, `07_blok_stanu.md`, `07_zalacznik_benchmarki.md`, `08_kontrola.md`, … | `CURRENT.md`, `log.md`, `01_scores.md`, `02_facts/`, `07_report.md`, `07_state_block.md`, `07_annex_benchmarks.md`, `08_quality_control.md`, … |
| Commit / tag convention | `wydanie-NN etap-XX`, tag `wydanie-NN` | `edition-NN stage-XX`, tag `edition-NN` |
| Vectors | GOS, DYP, WEW (MIL, ENE, FIN, TEC, INF unchanged) | ECO, DIP, DOM |
| Runs | AGR, AGR_RT | AGG, AGG_RT |
| who_benefits (`czyj_sukces`) | USA_ZACHOD, UE, UKRAINA, ROSJA, CHINY, IRAN, KOMPROMIS, BRAK | US_WEST, EU, UKRAINE, RUSSIA, CHINA, IRAN, COMPROMISE, NONE |
| Perspective | Z, A, T | W, A, T |
| Event status | DEKL, WYK, SPOR | DECL, DONE, DISP |
| Analytic confidence | niska, średnia, wysoka | low, medium, high |
| Question type | PANEL, SWOBODNE, PROPOZYCJA_PANEL | PANEL, OPEN, PANEL_PROPOSAL |
| Question status | AKTYWNE, ROZSTRZYGNIETE, ANULOWANE, PROPOZYCJA | ACTIVE, RESOLVED, VOID, PROPOSAL |
| Benchmark match | DOKLADNE, PRZYBLIZONE | EXACT, APPROX |
| Resolution outcome / flags | 1, 0, ANUL; weryfikuj T/N; zatwierdzone_przez_uzytkownika T | 1, 0, VOID; verify Y/N; user_approved Y |
| Marker words | OCENA, WERYFIKUJ | ASSESSMENT, VERIFY |
| Clusters | e.g. ORMUZ, FLANKA, UA_ROZMOWY, CN_ZIEMIE_RZADKIE, ROPA_CENA, STOPY_PL … | e.g. HORMUZ, EASTERN_FLANK, UA_TALKS, CN_RARE_EARTHS, OIL_PRICE, RATES_PL … (one-to-one; full list in `registry/questions.csv`) |
