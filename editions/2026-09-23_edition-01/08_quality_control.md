# Stage 08 — Quality control and closing of edition 01

Date of check: 24.09.2026 · Edition state date: 23.09.2026 · Directory: `editions/2026-09-23_edition-01`

Scope of corrections: only `07_report.md` and `07_state_block.md`. Forecasts, the registry and files 02–06 were not changed — discrepancies in them are only recorded.

## Summary

| # | Checkpoint | Result |
|---|---|---|
| 1 | Facts (completeness of records, sample of 15 URLs) | **Discrepancy** — 2 of 15 records inconsistent with the source, 1 partly confirmed; stage 04 records shortened (report corrected) |
| 2 | Separation of fact / assessment / forecast | **Discrepancy (corrected)** — numbers outside section H: block L (55%), section J.5 (+0.01) |
| 3 | Forecast completeness | **OK** — 73/73 questions with A, B, C, AGG, AGG_RT |
| 4 | Append-only registry | **OK** — only appended rows |
| 5 | Blindness | **OK with reservations** — 2 reported accidental exposures (04-B, 04-C); no references to benchmarks or forbidden domains |
| 6 | Question bank | **OK** — horizons 38/44/18%, triviality 1.4%, 8/8 vectors, panel 40 |
| 7 | Source perspectives | **Discrepancy (no content to correct in the records)** — three perspectives for 15 of 24 key events (63%); J.3 supplemented |
| 8 | Log | **Discrepancy (supplemented here)** — no stage times in the log; no reported prompt-injection attempts |

## 1. Facts

**Completeness of records in the report.** Facts in sections A–J refer to the records in `02_facts/G*.md` (213 records, each with 13 fields: date, actor, action, target, vector, region, status, publisher, URL, rating A–F/1–6, perspective, PIR — checked mechanically, no empty fields). Discrepancies:

- Facts fetched in stage 04 (A-add., B-add., C-01…C-14) have a shortened record: date, publisher, URL — without source rating, perspective or PIR. "A-add." and "B-add." have no numbers, so a reference in the report does not point to a single record. **Correction in the report:** a note in the "Notation conventions". The records in the 04 files were not changed.
- Several facts in section K come from `00_plan.md`, not from a G record (e.g. conscription decree no. 998 — Garant.ru, kremlin.ru). They have a source and URL in `00_plan.md`, but no source rating. No correction; for edition 02: move such facts into G records.

**Sample of 15 facts.** Population: 171 record identifiers (G1–G4, C-xx) cited in the main text of the report. Draw: `random.seed(1)` (Python), `random.sample(sorted(ids), 15)`. One-off command, no file in the repository.

| Record | URL checked | Result | Notes |
|---|---|---|---|
| C-12 | energyriskiq.com/gas-storage-levels-in-europe | **Discrepancy** | Source: approx. 5.6 TWh/d needed for the **90%** target on 01.11, not 80%. Known error (05 §1 item 9); the report describes it in J.5 |
| G1-007 | iranintl.com (via Kyodo) | Confirmed | 7-day offer, handed over on 16.09, a Pezeshkian–Trump meeting ruled out. US News — fetch timed out |
| G1-018 | globalsecurity.org (oprep) | Partly | The page (updated daily) gives "the decision of 19.09 not to strike the Houthis". The crown prince's repeated request was not confirmed — it comes from CNN, already unavailable in stage 02 (rating C/3 appropriate) |
| G1-025 | stripes.com | Confirmed | "Major progress", location "very soon"; no information on permanent stationing |
| G1-030 | anews.com.tr (NBC — excerpt only) | Confirmed | 25–40k out of approx. 80k, possible shift to the flank, recommendation 06.11 |
| G1-059 | windward.ai | Confirmed | 1–2 mn USD per ship per voyage; article of 09.09.2026 |
| G2-011 | rigzone.com | Confirmed with a note | Production held in X, Saudi quota 10.478 mn b/d, meeting 04.10 — confirmed. "Completion of the 1.65 mn b/d unwinding in IX" — not in this source (element of the record not used in the report) |
| G3-006 | theweek.in | Confirmed with a note | Content of the Indian MEA position confirmed; the spokesman's name (Jaiswal) does not appear in this article |
| G3-010 | china-briefing.com | Confirmed | 12.5% under s.301 since 24.07.2026, Supreme Court ruling of 20.02.2026, average 36.8% → 29.7% |
| G3-028 | chinanews.com.cn | Confirmed with a note | LPR 3.0% and 3.5%, 20.09.2026; the article does not say "unchanged" explicitly |
| G3-035 | euronews.com | Confirmed with a note | 36 months, delisting of Usmanov and Fridman, Latvia's abstention. Number covered: Euronews "over 2,600", record "approx. 3,000" (number not used in the report) |
| G3-040 | eurointegration.com.ua; globalsecurity.org (gov.ua) | Confirmed | 32.6 bn USD gap in 2027, approx. 50 bn USD/year, "a concept, not a ready plan" |
| G3-043 | tariffstool.com | Confirmed | 15% ceiling including MFN since 01.07.2026, cars 15%, steel and aluminium 50% |
| G4-020 | aljazeera.com | Confirmed | Trump's claim of an energy ceasefire, strikes resumed almost immediately |
| G4-049 | armenianweekly.com; cacianalyst.org | **Discrepancy** | Treaty not signed and the constitutional condition — confirmed. **"Referendum in 2027" — absent from both sources** (CACI: referendum "without a set date"; CACI article of 15.01.2026) |

Result: 12 of 15 confirmed (including 4 with minor notes on record elements not used in the report), 1 partly, 2 discrepancies. **Corrections in the report:** G4-049 — section E (Armenia–Azerbaijan row, also the ASSESSMENT "blocked until 2027") and block L ("Caucasus"); the same in `07_state_block.md`. C-12 — the report already describes the error in J.5, no change.

Discrepancy not corrected: the rationales of the Q-0072 forecasts in the 04 files may rely on the "2027 referendum". Forecasts are not changed — for the lenses to take into account in edition 02.

## 2. Separation of fact / assessment / forecast

The text outside section H and the annex was searched for values 0.xx and percentages next to the words "probab…"/"chance…". Found:

- Block L (report, line `base_scenario`) and `07_state_block.md`: "55%". A numerical probability outside section H (CLAUDE.md item 3.1; the edition 00 format contained no number). **Corrected** to a reference to H.1.
- J.5: "(+0.01)" — the size of the red-team adjustment. **Corrected** to a reference to the annex.
- The convention (verbal scale from §10) and percentage price changes (e.g. Brent −4–5%) — these are not forecasts, no change.

Consistency of the verbal scale: H.1 described 55% as "likely", while the annex assumes 0.45–0.55 inclusive is "even chances". **Corrected** to "roughly even chances (the most likely of the three)".

Consistency of numbers with the registry: 73 annex rows — AGG_RT, A/B/C, spread, confidence, question text and deadline consistent with `registry/forecasts.csv` and `questions.csv`. In the registry p has 3 decimal places, in the report 2. All differences ≤ 0.005, i.e. rounding only. Numbers in H.1–H.3 consistent. The H.3 statistics (mean 0.338, bins 23/28/11/8/3, confidence 50/23, triviality 1/73) confirmed by recomputation.

## 3. Forecast completeness

73 ACTIVE questions; for each, edition 01 has exactly one A, B, C, AGG and AGG_RT row (365 rows). AGG = mean of A, B, C (differences ≤ 0.005). AGG_RT ≠ AGG for 9 questions, in line with the adjustments accepted in 06 (Q-0002 +0.01, Q-0003 +0.07, Q-0013 +0.10, Q-0031 −0.05, Q-0039 −0.07, Q-0040 +0.10, Q-0050 +0.05, Q-0054 +0.12, Q-0062 +0.08; all within the ±0.15 limit). All p in the range 0.01–0.99. **OK.**

## 4. Append-only registry

No tag of the previous edition exists — the repository was created at the start of edition 01. Reference point: commit `cd7a7bd` ("initial state", registry headers).

| File | Added | Deleted or changed |
|---|---|---|
| forecasts.csv | 365 | 0 |
| benchmarks.csv | 43 | 0 |
| resolutions.csv | 0 | 0 |
| questions.csv | 73 | 0 |
| sources.csv | 186 | 0 |

Each commit was also checked separately (`git diff <c>~1 <c> -- registry/`): no row was deleted or changed in any of them. `benchmarks.csv` changed only in the stage 06 commit (3d9c888), which came after the "forecasts frozen" commit (32a635e). **OK.** From edition 02 the reference point will be the tag of edition 01.

## 5. Blindness

- Files 03, 04_A/B/C and 05 were searched for names of forecasting services (list in CLAUDE.md item 9, plus robinhood, octagonai, natesilver, racetothewh), the words "odds", "prediction", "prediction market" and "benchmark", and references to the `06_*` and `07_annex*` files. The hits concern only declarations that these files were not opened, and the report of a robinhood.com link in search results (04-A; the link was not opened).
- Git history: `06_aggregation.md` was created in the freezing commit, `06_benchmarks.md` in stage 06, `07_annex_benchmarks.md` in stage 07 — all after stages 03–05.
- The session histories of stages 03–05 cannot be checked from this session. The check relies on the files and the log.
- Reported exposures (log): 04-B saw 2 rows of lens A (Q-0001, Q-0002) with p values. 04-C saw a fragment of a B rationale (Q-0073, without p) and the 04-A/04-B log entries after saving its forecasts. Both described in report J.5. Structural risk: the edition log, read by subsequent lenses, contains other lenses' search topics and p ranges. **Process conclusion (for user approval):** 04 log entries without p ranges, and lenses do not read other lenses' 04 entries.

Result: **OK with reservations** (accidental exposures, reported, no references to benchmarks).

## 6. Question bank

| Requirement | State | Result |
|---|---|---|
| Horizons (§3.3: approx. 40/40/20) | to 10.10.2026: 28 (38%); to 31.12.2026: 32 (44%); longer: 13 (18%) | OK |
| Triviality (§3.8: ≤ 20% outside 0.05–0.95) | 1/73 (1.4%) — Q-0001 (0.03) | OK |
| Coverage of 8 vectors | MIL 15, FIN 12, ENE 10, DIP 9, DOM 8, ECO 7, INF 7, TEC 5 | OK |
| Panel (40, 5 per vector) | 40; 5 in each of the 8 vectors | OK |
| Open questions (20–40) | 33 | OK |
| Completeness of fields | criterion, resolution source, cluster — all filled in; no duplicate content | OK |

Observations (not discrepancies): p_status_quo = 0.10 in 65 of 73 questions (0.50 — 6, 0.90 — 2), so the status-quo baseline will be almost uniform. who_benefits = NONE in 58 of 73 questions, so directional bias can be computed on 15 questions (COMPROMISE 7, RUSSIA 3, UKRAINE 2, EU, CHINA, US_WEST 1 each).

## 7. Source perspectives

**Facts by perspective** (213 records G1–G4; a record may have several perspectives):

| Perspective | Records with this perspective | Share | This perspective only |
|---|---|---|---|
| W | 118 | 55% | 76 (36%) |
| A | 83 | 39% | 54 (25%) |
| T | 66 | 31% | 34 (16%) |
| More than one | — | — | 49 (23%) |

Distribution by group: G1 the most Western (W 43, A 19, T 14); G4 the most balanced (A 29, T 26, W 25).

**Key events with three perspectives: 15 of 24 (63%).**

- Complete (15): Iran's offer and Hormuz; Houthi attack on Riyadh; US troops in PL; CCG–BFAR collision; oil and the East–West pipeline; rare earths; H.R. 5334; preparation of the US–PRC summit; EU sanctions (36 months); currencies and payments; Iran–US talks; talks on Ukraine; Greenland; Mali; Venezuela.
- Missing (9): Baltic incidents (no T and RU/BY); front in Ukraine (T); Taiwan (A — PRC); DPRK (A, T); Qatar LNG (T); refineries in Russia (T); Russia's 2027 budget (W); Poland's rating (T); Duma elections (T).

**Correction in the report:** table J.3 did not list 4 events with gaps (Qatar LNG, refineries, Russian budget, Polish rating) — they were added. For edition 02: T for the front and Baltic incidents are recurring gaps; sources/source_map.md should list T sources for PIR-1.

## 8. Log

- **Stage times** — the log does not give times (except the start of 00 at 00:14). Supplemented from git history (commit times, 23.09.2026):

| Stage | Commit | Time |
|---|---|---|
| 00 | cbe7e4f | 00:18 |
| 01 | e643392 | 00:20 |
| 02-G1 / G2 | f669846 / 4bc0e21 | 00:35 / 00:50 |
| 02-G3 (2 sessions) | 0a5826c | 09:41 |
| 02-G4 | 5b7b7ef | 10:27 |
| 03 (+ log correction) | 9e78c4c, c97c33f | 22:03–22:04 |
| 04-A / 04-B / 04-C | 506cf77 / a643929 / bac8b26 | 22:14 / 22:23 / 22:43 |
| 05 | 59462d4 | 23:11 |
| forecasts frozen | 32a635e | 23:13 |
| 06 | 3d9c888 | 23:27 |
| 07 | 5bfe42e | 23:44 |
| 08 | — | 24.09.2026 |

- **Interrupted stages:** 02-G3 was carried out in two sessions, and the second continued from the gaps (in line with item 10). No other interruptions were recorded.
- **Problems:** unavailable sources (Reuters, CNN, Bloomberg, CNBC, USNI, UKMTO, Metaculus and others), "partial" gaps in G1–G4 (user decision in 03: continue), no PDF of the report (no converter), arithmetic error C-12, unresolved value of 5.13% for A Just Russia.
- **Prompt-injection attempts:** none reported in any stage. None found in stage 08 either, on 18 fetched pages (19 attempts, 1 timeout — US News).
- **Links to prediction markets in search results** (not opened): 00 (robinhood.com), 02-G1 (polymarket.com, octagonai.co), 02-G4 (racetothewh.com, natesilver.net), 04-A (robinhood.com).

## Corrections made in the report (stage 08)

| File | Location | Change | Reason |
|---|---|---|---|
| 07_report.md | Notation conventions | Note: records from stage 04 are shortened (no source rating, perspective, PIR; A-add./B-add. without numbers) | Item 1 |
| 07_report.md | E, Armenia–Azerbaijan row | "referendum only in 2027" → referendum without a set date; ASSESSMENT "blocked until 2027" → "until the constitution is changed; date not set" | Item 1, G4-049 |
| 07_report.md, 07_state_block.md | L, `Caucasus` | "referendum in Armenia 2027" → "date not set" | Item 1, G4-049 |
| 07_report.md, 07_state_block.md | L, `base_scenario` | "55%" removed, reference to H.1 added | Item 2 |
| 07_report.md | H.1, base scenario 6–12 months | "likely" → "roughly even chances (the most likely of the three)" | Item 2, consistency of the §10 scale with the annex |
| 07_report.md | J.5 | "(+0.01)" removed | Item 2 |
| 07_report.md | J.3 | 4 key events with a missing perspective added | Item 7 |

## Discrepancies not corrected (recorded only)

1. C-12 (04_forecasts_C.md): 5.5 TWh/d attributed to the 80% target instead of 90%. The impact on the C forecast for Q-0067 was described by the red team.
2. G4-049 (02_facts/G4.md): "referendum 2027" not supported by the sources.
3. Stage 04 fact records without source rating, perspective and PIR (inconsistent with CLAUDE.md item 3.2).
4. Blindness exposures of 04-B and 04-C (described in the log and J.5).
5. No stage times in `log.md` (supplemented in this file).

## Process proposals (require user approval and an entry in `methodology_changes.md`)

1. Record facts fetched in stage 04 as full records (rating, perspective, PIR) and with a number (A-01…, B-01…).
2. Stage 04 log entries without p ranges and without search topics; lenses do not read other lenses' 04 entries.
3. Every log entry with the start and end time of the stage.
