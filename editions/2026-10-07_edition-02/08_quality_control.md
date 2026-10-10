# Stage 08 — Quality control and closing of edition 02

Date of check: 10.10.2026 · Edition state date: 07.10.2026 · Directory: `editions/2026-10-07_edition-02` · Model: claude-opus-5-5 · Framework 1.4.0 · Methodology v1.0

Scope of corrections: only `07_report.md`, `07_state_block.md` and `07_annex_benchmarks.md`. Forecasts, the registry and files 00–06 were not changed. Discrepancies in them are only recorded here.

## Summary

| # | Checkpoint | Result |
|---|---|---|
| 1 | Facts (completeness of records, sample of 15 URLs) | **OK with notes.** 14 of 15 confirmed, 8 of them with minor notes; 1 partly confirmed (G4-070); 0 contradicted by the source. 2 of 277 G records have empty fields (G1-036, G4-038). |
| 2 | Separation of fact / assessment / forecast | **OK.** No numerical probability outside section H and the annex. The section 0 numbers are scores, not forecasts. Values in H.1–H.3 and in the annex match the registry. |
| 3 | Forecast completeness | **OK.** 88 of 88 ACTIVE questions have exactly one A, B, C, AGG and AGG_RT row (440 rows). |
| 4 | Append-only registry | **OK.** Only appended rows. In `questions.csv` only `status` (27) and `notes` (31) changed. |
| 5 | Blindness | **OK with reservations.** 3 recorded accidental exposures (04-A, 04-B), all after the lens's forecasts were written; unrequested market or model figures in search summaries were not used. No references to benchmarks or forbidden domains. |
| 6 | Question bank | **OK with one note.** Horizons 36/48/17% (the 03 definition) or 33/50/17% (strict 14 days); triviality 3.4%; 8 of 8 vectors; panel 40 (5 per vector); 38 open questions. |
| 7 | Source perspectives | **Discrepancy (recorded, no correction needed).** 23 of 30 key events have three perspectives (77%; edition 01: 63%). The 7 incomplete events are all listed in J.3. |
| 7a | Coverage | **OK with gaps.** 14 languages used in stage 02; 30% Western share of harvested items vs 52% of fact records carrying W; 1 of 5 silent cells closed; 18% of records rest on a primary source. Edition 01 has no comparable measurement. |
| 8 | Log | **OK.** Every stage has a start and end time. 2 interrupted stages (02-G3, 06) were continued from the gaps. No prompt-injection attempts reported. |
| 9 | Provenance | **OK with notes.** Every stage 00–07 has start and end records. One framework version (1.4.0) and one methodology version (v1.0). Stages 00 and H started with 2 dirty files. |
| 10 | Registration | Done after the `edition-02` tag (see the end of this file and `registry/editions.csv`). |

## 1. Facts

**Completeness of records.** I parsed every record table mechanically.

- `02_facts/G1–G4.md` hold 277 records: G1 63, G2 50, G3 77, G4 87.
- The additional records of stages 04 and 05 add 46 more: A-01…A-14, B-01…B-14, C-01…C-15 and R-01…R-03.
- All 323 records have the 13 fields of methodology §9. This includes the stage 04 and 05 records, which closes discrepancy 3 of edition 01.

Empty fields:

- **G1-036** (no Article 4 request in the window) has no URL. It is a negative check that points to `01_resolutions.md` and to edition 01 G1-041. It is cited twice in the report ("no Article 4 request in 2026", sections B and C), and the content matches the record.
- **G4-038** (election calendar) has no region and no perspective. It is not cited in the report.

The report cites 219 distinct record identifiers in its main text, before the annex. Every one of them exists in a record table. All 19 "FACT:" passages carry a record ID or a stage-01 or registry reference. 18 of 23 occurrences of "ASSESSMENT" carry an explicit confidence. The other 5 are table headers or the definition in the conventions, where confidence is a table column.

**Sample of 15 facts.** Population: the 219 record IDs cited in the main text. Draw: `random.seed(2)` (Python), `random.sample(sorted(ids), 15)`, run as a one-off command with no file in the repository.

| Record | URL(s) checked | Result | Notes |
|---|---|---|---|
| R-02 | ofac.treasury.gov (selected general licences; recent action 20261009_33) | Confirmed | Listing: GL 135 of 09.10.2026 on Russian-origin diesel. Expiry 07.04.2027 and the carve-out for debits to Bank of Russia / NWF / MinFin accounts were confirmed through a search summary quoting the OFAC document. The PDF text itself could not be extracted (encoded fonts). The rating "A/2 via search summary" is appropriate. |
| C-03 | cnnbrasil.com.br; metropoles.com | Confirmed with a note | 52/48 of valid votes, 49/45 total (Metrópoles), 2,520 interviews, ±2 pp. The TSE registration is BR-02949/2026 in Metrópoles and BR-0949/2026 in CNN Brasil, so the sources differ (the record follows Metrópoles; the number is not used in the report). |
| G1-005 | euronews.com | Confirmed | Naqdi: "closed", "full control", blasted routes "soon blocked". Amirahmadi: about 10 ships a day vs about 125. Akrami-Nia: "pre-emptive operations". Article of 07.10. |
| G1-003 | aa.com.tr | Confirmed | MT On Peace, Panama flag, 19 crew (17 Indian), 12 injured (11 Indian), evacuated to Khasab. MEA: "deep concern", "immediate cessation". |
| G2-025 | forsal.pl | Confirmed | Signed 01.10. Rate 60% of the excess margin, profits III 2026–III 2027, about 4 bn PLN, follow-up referral to the Tribunal (does not suspend the law), preventive referral 24.07, the "Paliwo Kosztuje Normalnie" bill. |
| G4-084 | news.cgtn.com; middleeasteye.net; aa.com.tr | Confirmed with a note | Katz's threat and the denial of access to Gaza and East Jerusalem (Wafa) are confirmed, as is the PLC election on 28.11, the first since 2006. **"Kallas is sending EU observers"** is in none of the three linked sources. The fourth publisher (Bankier.pl) has no URL in the record. This element is not used in the report. |
| G1-030 | kyivindependent.com; zerkalo.io (HTTP 403); a search on lsm.lv, euromaidanpress.com and others | Confirmed with a note | Kyiv Independent confirms the core facts: 20 migrants, armed escorts, damaged cabinet, stolen cameras, Dombrava. The border-guard attribution (Pujāts: possibly organised criminal groups tolerated by Minsk), Sybiha ("Moscow"), the regime extended to 31.12 and 11,384 (to 24.09) come only from other outlets, found by search. Outlets also report 11,925 as the year-to-date figure. |
| G4-032 | ansabrasil.com.br; granma.cu | Confirmed | 42/38 released 01.10 (ANSA). 45/42 of valid votes on 04.10, "technical tie" (Granma). |
| G4-070 | folha.uol.com.br and thehindu.com (tool cannot fetch either); a search on AFP via Infobae and swissinfo | **Partly** | The phasing-out of the ration book is confirmed only as a gradual, de facto process: AFP saw bodegas closed on 05.10 and there is no official decree. The book dates from 1963 (63 years; "about 60" follows the Folha headline). The status "DONE (policy)" overstates a formal decision. The report wording "being phased out" is acceptable, so no correction. |
| G4-006 | aa.com.tr | Confirmed with a note | Qatari MFA spokesman al-Hashimi, 06.10: "exchange of messages", contacts and visits continue, "too early" to join the Mecca Alliance. AA says "mediation", not "indirect negotiations". The Mehr part (Momeni's message) was not checked. |
| R-03 | euronews.com | Confirmed with a note | Fitburg (SVG flag), Elisa Helsinki–Tallinn cable in Estonia's EEZ, 31.12.2025, 14 crew detained, aggravated criminal damage, sanctioned Russian steel impounded. The Latvian boarding "five days later" is not in Euronews (RFE/RL not checked). |
| G2-009 | nbcnews.com; oilprice.com; washingtonpost.com (HTTP 403); a search on Bloomberg and The Hill | Confirmed with a note | "As much as 100 million barrels" over four months, "substantial diesel release within the first 20 days", refinery coordination. The Trump quote "we're not going to be doing the export ban" is not in NBC or OilPrice. Bloomberg and The Hill carry it (Bloomberg is listed in the record). OilPrice confirms the additionality dispute but does not name Raymond James. |
| G1-056 | defensenews.com | Confirmed with a note | NMESIS and MADIS to Yonaguni (110 km from Taiwan) for Keen Sword, 19–29.10.2026, multi-island sea denial. The record does not name the exercise. USNI was not checked. |
| G3-059 | news.cn | Confirmed | MOFCOM 19.09.2026: opposition to unilateral and secondary sanctions, "not subject to" third-party interference, "closely monitor", "reserves the right", dialogue. |
| G1-043 | censor.net and ukranews.com (HTTP 403); a search summary of the Ukranews article | Confirmed | 154 km² in September (first estimate 66), July 63, August 124, total 341, and 270–320 km² of liberated territory not yet shown. |

Result: 14 of 15 confirmed (8 with minor notes on record elements), 1 partly (G4-070), 0 contradicted by the source. None of the notes affects a statement in the report, so **no correction to the report**.

Fetch statistics: 20 fetches, of which 6 failed (4 × HTTP 403, 2 domains the tool cannot fetch), plus 4 web searches. The rule 3.9 domains and robinhood.com were blocked in every search.

## 2. Separation of fact / assessment / forecast

I searched `07_report.md` outside section H (lines 229–299) and outside the annex, and all of `07_state_block.md`. The search looked for values 0.x/0.xx, "p =", "AGG", and percentages next to probability words ("likely", "chance", "probab…", "scenario", "forecast", "risk", "odds").

- **Section 0 (accuracy scores):** Brier scores, BSS and the edition-01 calibration bins. These are scores, required by methodology §11, not forecasts. No change.
- **J.5:** "±0.15 limit" is the red-team rule, not a forecast. No change.
- **Block L:** `base_scenario` gives only a reference to H.1, with no number (the edition 01 correction carried over). The report and `07_state_block.md` are identical apart from headings.
- Other percentages are economic data (GDP, CPI, rates, storage).
- Files 00, 02 and 03 contain no numerical probability next to probability words.

**Consistency with the registry.** All checks were run as one-off commands.

- All 88 annex rows match `registry/forecasts.csv` and `questions.csv` within rounding (≤ 0.005). The checked fields are AGG_RT; A, B and C; the spread; AGG_RT confidence; the question text; the deadline; the edition-01 value in "Change vs 01"; "new" for questions created in this edition; and the verbal label (§10, with 0.45–0.55 inclusive as even chances).
- In H.2, all 82 bold values match the registry.
- In H.1, the triggers quoted with "from" values match both editions.
- The H.3 statistics recompute to the same figures: mean, the five bins, confidence 51/34/3, deadline buckets 19/49/20, triviality 3 of 88.

**Crowd and market values** appear only in `07_annex_benchmarks.md`. The main report mentions only that the annex exists. **OK.**

## 3. Forecast completeness

The registry holds 88 ACTIVE questions and 440 edition-02 rows: A 88, B 88, C 88, AGG 88, AGG_RT 88. No question is missing a run, there is no duplicate, and there is no row for a non-active question.

- AGG equals the mean of A, B and C (largest difference 0.0003).
- AGG_RT ≠ AGG for 9 questions, which matches the 9 red-team adjustments accepted in stage 06. All are within the ±0.15 limit.
- All p values are in the range 0.01–0.99.
- No change to `forecasts.csv`, the 04/05 files or `06_aggregation.md` after the "forecasts frozen" commit f09a1d4 (`git diff f09a1d4 HEAD`, empty).

**OK.**

Discrepancy (recorded only; the registry is not corrected): the `date` field of the edition-02 rows is not uniform. Runs A, AGG and AGG_RT are dated 2026-10-09 (the run date). Runs B and C are dated 2026-10-07 (the state date). Edition 01 used the state date for every run. `tools/scores.py` carries the field but does not use it in any score.

## 4. Append-only registry

Reference point: `REGISTRY_BASELINE` 5669790 (CURRENT.md; English migration of 28.09.2026).

| File | Added lines | Deleted or changed lines |
|---|---|---|
| forecasts.csv | 440 | 0 |
| benchmarks.csv | 68 | 0 |
| resolutions.csv | 27 | 0 |
| questions.csv | 42 new rows + 31 changed rows | 31 changed rows, of which only `status` (27, ACTIVE → RESOLVED) and `notes` (31) differ; no other field differs (field-by-field comparison) |
| sources.csv | 141 | 0 |
| editions.csv | (file created after the baseline: header + editions 00, 01) | — |

Each commit since the baseline was also checked separately (`git diff <c>~1 <c>`). None of them deleted or changed a line in forecasts, benchmarks or resolutions.

`benchmarks.csv` changed only in the stage-06 commit 75c4c51, after the "forecasts frozen" commit f09a1d4. The first benchmark collection, written before an interruption, was committed in the same 75c4c51 commit.

**OK.**

## 5. Blindness

**Files.** I searched `03_analysis.md`, `03_question_bank_changes.md`, `04_forecasts_A/B/C.md` and `05_red_team.md` for:

- the domains of rule 3.9 and the watch list (robinhood, poliwave, natesilver, racetothewh, betfair, oddschecker, wionews);
- the terms "odds", "prediction market", "market-implied", "benchmark", "crowd";
- references to `06_*`, `07_annex*`, `reviews/learning`, `social/` and `docs/data`.

All hits are declarations of what was not opened, lists of blocked domains, or the 04-C report of unrequested market figures in search summaries.

**Git order.** `03_analysis` (22:46), `04_A` (22:58), `04_B` (23:10), `04_C` (23:22) and `05` (23:29) on 09.10 were all committed before `06_aggregation.md` (frozen commit, 23:31). `06_benchmarks.md` came in stage 06 (10.10 02:28) and `07_annex_benchmarks.md` in stage 07 (02:42).

**Session histories** of stages 03–05 cannot be inspected from this session. The check relies on the files and the log.

**Recorded exposures (log, J.5):**

- 04-A: a check command printed one edition-01 run-B row after all lens-A forecasts were written.
- 04-B: a grep printed lens A's stage-04 log lines (process data, no values), and later three edition-01 run-A rows, after lens B's forecasts were written.
- Stages 00, 01, 02-G3, 02-G4, 03, 04-A, 04-B and 04-C saw prediction-market or model figures in search summaries without requesting them. They were not opened, recorded or used.

Edition 01's process proposal 2 is being followed: the edition-02 stage-04 log entries contain no p ranges.

Result: **OK with reservations.** The exposures were reported, came after the forecasts were written or contained no values, and the files contain no references to benchmarks.

## 6. Question bank

| Requirement | State | Result |
|---|---|---|
| Horizons of the 42 new questions (§3.3: about 40/40/20) | 03 definition (next edition ≤ 24.10): 15 (36%) / 20 (48%) / 7 (17%). Strict 14 days (≤ 21.10): 14 (33%) / 21 (50%) / 7 (17%) | OK with a note: the quarter bucket is above target, and 03 §5 explains why |
| Triviality (§3.8: ≤ 20% outside 0.05–0.95) | 3 of 88 (3.4%) | OK |
| Coverage of 8 vectors (active) | MIL 15, FIN 15, ENE 12, DIP 12, DOM 10, INF 9, TEC 8, ECO 7 | OK |
| Panel (40, 5 per vector) | 40; 5 in each vector; 4 replacements from the same vector and cluster (Q-0074–Q-0077) | OK |
| Open questions (20–40 per edition) | 38 new | OK |
| Completeness of fields | criterion, resolution source, cluster, p_status_quo, who_benefits and PIR filled in for all 88; no duplicate question text | OK |
| Deadline passed while still ACTIVE | Q-0037, Q-0049 (no data; stage 01 notes) | Recorded |

Note on the horizon rule: §3.3 says "by the date of the next edition (14 days)". Stage 03 used 24.10 as the boundary, while the report header gives "about 20–21.10" for the next edition. The difference moves one question between buckets. For the user: fix one boundary convention (process clarification).

Observations, not discrepancies:

- p_status_quo is 0.10 for 80 of 88 active questions (0.50 for 4, 0.90 for 4), so the status-quo baseline stays nearly uniform.
- who_benefits ≠ NONE for 19 of 88 questions (COMPROMISE 9, RUSSIA 4, EU 3, CHINA 1, US_WEST 1, UKRAINE 1).

## 7. Source perspectives

**Facts by perspective.** I counted the 277 G records; a record may carry several tags.

| Perspective | Records with this tag | Share | This perspective only | Edition 01 (share with tag) |
|---|---|---|---|---|
| W | 143 | 52% | 55 (20%) | 55% |
| A | 146 | 53% | 69 (25%) | 39% |
| T | 125 | 45% | 34 (12%) | 31% |
| More than one | — | — | 118 (43%) | 23% |
| None | — | — | 1 (G4-038) | — |

By group: G1 W 35 / A 34 / T 31; G2 31/21/18; G3 37/34/26; G4 40/57/50. My mechanical count for G3 W is 37; the file's own coverage section gives 38 (a difference in tag counting).

**Key events with three perspectives: 23 of 30 (77%; edition 01: 15 of 24, 63%).** The events come from the key-event lists in the "Coverage" sections of G1–G4. "Poland build-up" (G1) and "US base / government dispute" (G4) are counted as one event.

- **Complete (23):** Hormuz; Houthi–Saudi war; Poland build-up and the base dispute (T only as RU/BY media statements); Ukraine strike of 07.10; Scarborough; DPRK launch; reserve releases and US diesel pressure; EU storage; Iran oil exports; rare earths; refinery campaign; OPEC+ (the A side is Russian, the Saudi official is missing); US–China truce (T weak); Russia's budget; EU listings of 07.10; rates; EU–China trade; Iran diplomacy (Omani gap); Ukraine talks; Brazil election; Greenland; Mali/Kidal; Tigray/Eritrea.
- **Incomplete (7):** Ukraine front (T); Black Sea strikes in NATO EEZs (actor side silent on the ships); Mi-8 incursion (Russian side silent on the incident); H.R. 5334 (PRC and Kremlin silent inside the window — documented as a finding by the G3 re-run); Qatar LNG force majeure (A); CPN III in Poland (W); Polish public finances (W).

All 7 appear in report J.3, so no correction. The third-party front assessment is missing for the second edition running (edition 01 also lacked T for the front and the Baltic). The edition 01 proposal to list T sources for PIR-1 in `sources/source_map.md` is still open.

## 7a. Coverage (framework 1.1)

| Measure | Edition 02 | Edition 01 |
|---|---|---|
| Harvested items in window / languages / countries | 19,077 (8,336 matched) / 47 / 103 (the report header says 102 from `manifest.json`; `coverage.md` lists 103) | no harvester (web search only) |
| Western share of harvested items | 30% | — |
| Western share of fact records | 52% carry W; 20% W only | 55% carry W; 36% W only |
| Languages used in stage 02 (opened or searched) | 14 in total: EN, RU, PL, ZH, UK, FA, AR, DE, EL, ES, TR, PT, FR, DA (G1 7, G2 8, G3 7, G4 10) | not recorded |
| Silent required cells | 5 (NATO:official, SA:official, TR:western, JP:official, GL:independent_exile) | — |
| Silent cells closed by stage 02 | GL:independent (KNR, Sermitsiaq via web) — closed. SA:official — partly (G1 via GACA/coalition statements in wire reports; G2 not reached). NATO:official — not closed (nato.int not opened; gap). JP:official — not closed (Japanese MoD not read; gap). TR:western — no key event needed it. | — |
| Facts resting on a primary source read directly | 49 of 277 (18%): G1 7, G2 5, G3 24, G4 13. With official statements relayed verbatim: G1 about 43%, G2 about 44% | not recorded |
| Flagged concepts (mandatory searches) | `poland_security` (G1 RU + third party; G4 RU/BY state media; German search gave no result), `fuel_poland` (German only; no LT/CZ/UA), `arctic_greenland` (DA/KL and RU) — all searched | — |

Comparison with edition 01 is possible only for perspective shares. The W share of records fell slightly, and the share of records with more than one perspective nearly doubled. Coverage measures did not exist in edition 01.

Recurring weaknesses:

- The late harvester start: 8% of items dated 23.09–01.10.
- NATO and Japanese official channels, which are both still silent cells.
- The Polish fuel concept, which was searched in German only.

## 8. Log

**Stage times** (log; local time, UTC+2):

| Stage | Start | End | Commit |
|---|---|---|---|
| 00 (+ H digest 00:29–00:31) | 08.10 00:29 | 00:38 | 88f1e9c (00), 85a4f7f (H) |
| 01 | 08.10 00:38 | 01:06 | 55da552 |
| 02 G1 / G2 / G3 | 08.10 01:06 / 01:23 / 01:43 | 01:23 / 01:43 / 02:04 | 2ba060a / 83ebd66 / b760d71 |
| 02 G4 | 08.10 12:41 | 13:04 | 6273eb0 |
| 02 G3 re-run | 09.10 21:28 | 21:37 | 136ab49 |
| 03 | 09.10 22:30 | 22:46 | fdc5e49 |
| 04 A / B / C | 09.10 22:46 / 22:58 / 23:11 | 22:58 / 23:11 / 23:22 | 7767619 / bb66ccf / 24f0b5e |
| 05 | 09.10 23:22 | 23:29 | 9ec53b7 |
| 06 (freeze f09a1d4 23:31; re-run 10.10 02:15) | 09.10 23:29 | 10.10 02:28 | 75c4c51 |
| 07 | 10.10 02:28 | 02:43 | 1bd6f1b |
| 08 | 10.10 02:43 | see the log entry | edition-02 stage-08 |

**Interrupted stages:**

- 02-G3 hit the web-tool session limit and was continued on 09.10.
- 06 was cut off by an API usage limit during the benchmark step and was continued on 10.10.

Both continued from the gaps, and no forecast changed.

**Problems recorded:**

- Late harvester start.
- Missing API keys: AGSI+, EIA, FIRMS.
- Inaccessible sources: ISW, Saba, Reuters/CNN/SCMP/consilium, the ICE settlement.
- 10 resolutions awaiting the user's VERIFY decision; Q-0037 and Q-0049 past their deadline without data.
- The `tools/pipeline.py` edition-01 fallback defect (for L5).
- GJO needs a login and Metaculus needs an account (benchmark gaps).
- No PDF converter.

**Prompt-injection attempts:** none reported in any stage. None found in stage 08 on the 14 pages fetched successfully or in the search results.

**Format note:** stages 00 to 04-B log as table rows, while 04-C, 05, 06 and 07 log as sections. Every entry gives start and end times, as edition 01 proposal 3 asked.

**Result: OK.**

## 9. Provenance

`python3 tools/pipeline.py provenance` (also written to `provenance.md`):

- **Start and end records:** every stage 00–07 has both (H digest, 00, 01, 02 G1–G4, 02 G3 re-run, 03, 04 A/B/C, 05, 06, 07). The 08 start record exists (00:43:26Z), and its end record is written at the end of this stage.
- **Versions:**
  - framework: 1.4.0 only (31 records);
  - methodology: v1.0 only;
  - harvester: 1.4.0;
  - one `methodology_sha` and one `claude_md_sha` across the edition;
  - model: claude-opus-5-5 on every start record (end records carry no model field, by tool design).
- **Dirty files at start:**
  - 2 at the start of 00 and of H digest (commit ba3a61d, before the edition directory existed). The tool records only the count, so the files cannot be identified afterwards. Gap recorded, not reconstructed.
  - 0 at the start of every other stage.
- **Other notes:**
  - `harvest_manifest_sha` is missing on the 00 and H start records, which were written before the manifest existed.
  - The Claude CLI version changed during the edition (2.1.293 → 2.1.294 → 2.1.296). It is not a framework version and is recorded for information.
  - Stage 06 has one start record for both runs (the re-run did not add a second start), so its 3-hour duration includes the interruption.
  - Stage 02 G3 has two start/end pairs (run and re-run).
- **Edition 01:** no provenance records for stages 00–08 (they ran before provenance existed), as recorded in the stage 00 log. Not back-filled.

**Result: OK with notes.**

## Corrections made in the report (stage 08)

None. No check found a statement in `07_report.md`, `07_state_block.md` or `07_annex_benchmarks.md` that contradicts its source or the registry, or that breaks rule 3.1.

## Discrepancies not corrected (recorded only)

1. `registry/forecasts.csv`: the `date` field differs between runs (A, AGG, AGG_RT 2026-10-09; B, C 2026-10-07). The registry is append-only and is not corrected.
2. G1-036 has no URL (negative check); G4-038 has no region and no perspective.
3. G4-084: "Kallas is sending EU observers" is not in the three linked sources (the fourth publisher, Bankier.pl, has no URL). Not used in the report.
4. G4-070: status "DONE (policy)" overstates a gradual, de facto phase-out, and the ration book dates from 1963.
5. C-03: the two sources differ on the TSE registration number (BR-02949/2026 vs BR-0949/2026).
6. G2-009: the Trump quote comes from Bloomberg/The Hill, not from the two linked URLs that could be read.
7. The horizon boundary for "to the next edition" in stage 03 is 24.10, not 14 days (21.10).
8. Provenance: the dirty files at the start of 00/H cannot be identified; stage 06 has a single start record spanning an interruption.
9. Silent cells NATO:official and JP:official were not closed; the third-party front assessment is missing for the second edition running.

## For the user (decisions and process proposals — need approval and an entry in `methodology_changes.md`)

1. **VERIFY flags:** 10 resolutions of stage 01 still await your approval (`01_resolutions.md`, "FOR USER VERIFICATION"; `user_approved` is empty in all 27 rows).
2. **Forecast row date convention:** use the state date (as in edition 01) or the run date, consistently for all runs.
3. **Horizon boundary of §3.3:** fix "to the next edition" as state date + 14 days, or as the planned next state date.
4. **Record URLs:** require at least one URL even for negative checks (e.g. the source searched), and a URL for every listed publisher.
5. **Provenance:** record the names, not just the count, of dirty files at stage start; add a "resume" record when a stage is continued after an interruption (both need an approved change to `tools/pipeline.py`, L5 or the quarterly review).
6. Still open from edition 01: list third-party sources for PIR-1 (front, Baltic) in `sources/source_map.md`.

## Registration (item 10)

After the stage-08 commit and the `edition-02` tag: `python3 tools/pipeline.py register-edition` appends the edition-02 row to `registry/editions.csv`, followed by the commit `edition-02 registered`.
