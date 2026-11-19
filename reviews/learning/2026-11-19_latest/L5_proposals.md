# L5 — Framework improvement proposals (scope `latest`)

Run: 20.11.2026 · stage L5 · framework 1.9.2 · methodology v1.0 · model claude-opus-5-5 · commit at start ed9c64a · **unattended autopilot run (AUTO mode of `prompts/RUN_learning.md`)**: tasks 1–4 only. Every new proposal is recorded as `PROPOSED`, and **nothing is applied**: no change to prompts, tools, configuration, `CLAUDE.md`, the methodology or `VERSION`. Approval and implementation wait for the user (`/learn` in a normal session, or the quarterly review).

**Folder.** This file sits in the folder of 19.11.2026 with its inputs. L1–L3 ran on 19.11. L4 started on 19.11, was interrupted and finished on 20.11. The folder keeps the name of the day the review started.

**Inputs (all present):**
- `L1_hindsight.md`: audits edition 02 (framework 1.4.0).
- `L2_performance.md`: edition 02 forecasts, N = 36 scored, 26 clusters; lens diversity for editions 01–03.
- `L3_reasoning.md`: 10 misses and 5 hits of edition 02.
- `L4_sources.md`: coverage of edition 03 against editions 02 and 01; source track record of edition 02.

Also read: `methodology/methodology_changes.md` (versioning), `reviews/learning/proposals.csv`, `reviews/edition_metrics.csv`, `reviews/improvement_plan_log.md`, `reviews/measurements_after_edition_03.md`, `reviews/stage_time_audit.md`, and the edition 03 `08_quality_control.md`, `01_scores.md`, `05_red_team.md` and `log.md`. Also read: `prompts/02_collection.md`, `prompts/04_forecasts.md`, `sources/source_map.md`, and `tools/harvester/store.py` and `adapters.py` (read only).

**Versions.** Edition 02 forecast under framework 1.4.0 and edition 03 under 1.8.0. Both used methodology v1.0 and the model claude-opus-5-5. Every accuracy finding below concerns edition 02 alone: one framework version and one model. The coverage findings compare editions 02 and 03. Those two editions share the harvester version (1.4.0) and harvester configuration (same hashes), so the comparison is like with like (L4 "Versions").

---

## 1. Status of earlier proposals (task 1)

Checked against the metric in each row of `proposals.csv`. Only the `status` and `notes` fields of existing rows were changed.

| ID | Metric (short) | Evidence on 20.11.2026 | Verdict |
|---|---|---|---|
| P-0001 information cutoff | forecasts left out by `scores.py`; one date per edition; no stage 03–05 fact after the cutoff | Edition 03: all 415 rows are dated 2026-11-17, the INFO_CUTOFF date, and no stage 03–05 record is dated after it (08 item 3). The left-out count needs edition 03 resolutions, which none of its questions has yet | **keep IMPLEMENTED**. Two of three measures met; the third becomes measurable at stage 01 of edition 04 (from 30.11.2026) |
| P-0002 deciding source + fallback | ambiguous or unresolvable share among questions created from edition 03, N ≥ 20; target < 10% | Edition 03 questions have no resolutions yet. Stage 08 found that all new questions have a deciding source with a fallback and a recorded read (08 item 6) | **keep IMPLEMENTED**. Measurable from edition 04 stage 01, more likely at edition 05 (N ≥ 20) |
| P-0003 question load | active questions; red-team logic adjustments for rationale vs p (target 0); Brier by horizon from edition 04 | Edition 03: 83 active questions and 22 new open questions, inside 20–30. No red-team adjustment for a rationale that contradicts p (`05_red_team.md`) | **keep IMPLEMENTED**. Brier by horizon is due from edition 04 resolutions |
| P-0004 URLs, dirty files, resume | records without a URL; provenance names dirty files; resume records | Edition 03: 0 of 242 records lack a URL (edition 02: 2 of 323). Negative checks name the place searched. Provenance names its dirty files and records each resume (08 items 1 and 9) | **CONFIRMED** |
| P-0005 diagnostics | diagnostics in `01_scores.md` from edition 03; used by L2 and Q | Edition 03 `01_scores.md` has "Diagnostics", "YES rate by p_status_quo", "other reference baselines" and "lens diversity". L2 §2.3 and §3.3 use them | **CONFIRMED** |
| P-0006 T sources for PIR-1 | key PIR-1 events with T in edition 03; the front lacked T in editions 01 and 02 | `sources/source_map.md` has the section. Black Sea and Baltic key events had T in edition 03; their gaps were A-side. **The third-party front assessment is still missing, for the third edition running** (08 item 7; ISW and Russia Matters HTTP 403). The listed T outlets relay both sides' claims and give no measure of their own | **NO_EFFECT** for the front. Handled as a standing gap in P-0040 |
| P-0007, P-0008 | (major) | Unchanged, still for the quarterly review. L2 findings 1–2 add evidence: BSS vs constant 0.50 is 0.383 (N = 36); lens correlations 0.90–0.96 in three editions | DEFERRED_TO_Q (unchanged) |
| P-0009 brief and cards | brief published with the check passed; no number missing from the report | Edition 03 stage E: "Check passed: 56 forecast values injected from the registry … every number in the prose found in the report or `01_scores.md`". `docs/briefs/edition-03.html/.pdf` exist | **CONFIRMED** (editions 02 and 03) |
| P-0010 X strategy | weekly metrics in `social/x_metrics.csv` | **The file does not exist.** No measurement is possible | **keep IMPLEMENTED**. The metric needs the file. Owner input, since posting is manual |
| P-0011 two sessions a week | days from the earliest start to the actual start (target 0–4) | Edition 03 started **26 days** after its due date (`edition_metrics.csv`) | **NO_EFFECT**. Superseded by the autopilot (P-0012) and the due-date start (P-0014) |
| P-0012 autopilot | days after due (target 0–7); hours to publication; blockers; VERIFY share | Edition 03 began on the day the autopilot was approved (16.11), so its lateness predates the autopilot. Start to site took 50.4 h. 13 resolutions auto-verified and 1 disputed (Q-0079) | **keep IMPLEMENTED**. First clean measurement is edition 04 (due 30.11) |
| P-0013 harvester launchd | killed pid restarted within 60 s | Log of 19.11: pid 12256 killed and restarted as 12307 within 75 s. The harvester has run without a gap since (status 20.11) | **CONFIRMED** (75 s against a target of 60 s; judged as met in substance) |
| P-0014, P-0015, P-0016, P-0020, P-0021, P-0022, P-0023, P-0024, P-0025, P-0029, P-0031, P-0034 | edition-04 metrics | No edition has run under 1.9 yet | **keep IMPLEMENTED**. Measured in edition 04 (from 30.11) and at the quarterly review (QNT, B2: 30 pairs) |
| P-0017 registry guard and CI | CI green on main; guard passes | `registry_guard.py edition-03 HEAD` OK (run 20.11); edition-02..HEAD OK and CI green on 9ee968e (log 19.11) | **CONFIRMED** |
| P-0018 honest scores | official tables byte-identical; diagnostics present | Byte-identical diff and diagnostics recorded 19.11 (`measurements_after_edition_03.md`) | **CONFIRMED** |
| P-0019 replay harness | noise floor from three replays | Five valid replays of edition 02 give a noise floor of 0.011 Brier (`reviews/replay/README.md`) | **CONFIRMED** |
| P-0026 quarterly evidence file | file exists before `/gQ` | Due 19.12.2026 | **keep IMPLEMENTED** |
| P-0027, P-0028, P-0030 | owner actions pending (token, `BACKUP_DIR`, power settings) | Built; the owner steps are not done (log, "Status 19.11.2026") | **keep IMPLEMENTED** |
| P-0032 stage-time audit | audit names a cause per slow stage | `reviews/stage_time_audit.md`: every stage over 2 h was a usage-limit interruption | **CONFIRMED** |
| P-0033 release per edition | `gh release view edition-NN` | Log of 19.11: releases edition-02 and edition-03 created. **Not re-checked in this run**: `gh` is blocked for agents (WP-16) | **CONFIRMED** on the recorded check |
| P-0035 retries, metrics, owner setup | Q-0079 resolved by the interim stage of 23.11; edition 04 metrics row | Both are in the future | **keep IMPLEMENTED** |

Summary: **CONFIRMED 9** (P-0004, P-0005, P-0009, P-0013, P-0017, P-0018, P-0019, P-0032, P-0033), **NO_EFFECT 2** (P-0006, P-0011). P-0007 and P-0008 stay DEFERRED_TO_Q. The rest stay IMPLEMENTED until their data arrives (dates above).

---

## 2. Candidate problems (task 2)

Kept only when the evidence comes from at least two editions, or from at least three questions in two clusters.

| # | Problem | Evidence | Threshold met by |
|---|---|---|---|
| C1 | The lenses price the wrong event: the reference class is missing, generic, or overridden without a cited mechanism. Data and price thresholds are forecast without an error band | L3 §3.3 pattern 1: M3, M4, M5, M6 and M9, 5 misses in 5 clusters and 5 vectors. Sub-type 1a: M5–M8, 4 questions in 3 clusters. L2 finding 4 (compression in 0.10–0.50, N = 18) and L2 §4 (ECO +0.44) | ≥3 questions in ≥2 clusters |
| C2 | One party's statement of present intent or claim about contested facts is used as a forecast, with no base rate for how often such statements hold | L3 pattern 2: M1, M4, M5 and M10, 4 misses in 3 clusters. L1 lesson 2: assessments #6 and #9, and KA1. L4 §2.3: procedural claims held fully 11 of 12; contested-fact claims 1 of 7; stances 4 of 7 | ≥3 questions in ≥2 clusters; three independent steps agree |
| C3 | Watched official pages yield one item ever, because of an item-ID defect | L4 §4.2: 12 pages with exactly one item each in October and November, covering editions 02 and 03. Cause confirmed in this step: `adapters.run_page` builds `<url>#change-<hash>`, and `store.canonical_url` drops the fragment, so `item_id` is the same for every change | two editions; deterministic code defect |
| C4 | Signals are collected but never reach a digest or a record. Several topic classes have no keyword concept, and several sources have failed for two editions | L1 §6: 4 of 10 surprises "collected but not used", plus 3 facts from inside the window that were missed. L3 anecdotes M1 and M3. L4 §3.1: Tribunal items 0 of 8 matched in edition 02 and 12% in edition 03; Serbia 0 digest hits; no espionage concept; "swift" at least 17 false matches out of 56. L4 §4.1: 13 GDELT queries never produced an item; ISW, Saba and teleSUR failing in both editions | two editions |
| C5 | No harvested series for the thresholds that decide ECO and ENE questions | L3 1a (TTF, AGSI+, GUS CPI and FAO FFPI are not harvested). L4 §4.5: 13 resolution rows read by hand or through secondary carriers across editions 02–03. CHANGELOG proposals of 08.10 and 17.11 still open | ≥3 questions in ≥2 clusters; two editions |
| C6 | Stage 02 does not turn the larger corpus into wider records | L4 §1, edition 02 → 03: single-perspective records 57% → 69%; languages 14 → 11; Persian (5,046) and Turkish (5,611) items, none opened. Edition 03 stage 08: 6 of 8 incomplete key events were missing from J.3. Third-party front assessment missing in editions 01, 02 and 03 | two or three editions |

**Watch** (below the threshold; see §4): the confidence cap when a poll margin is below the polling error (M2, M9: 2 questions); the corpus delta read to the forecast date (M1: 1 question); stale values and dropped DECL flags in the report (L1 lesson 3: 2 items in one edition); the CRISIS signal list (L1 §5: one edition).

---

## 3. Proposals (task 3), ranked by expected benefit

### P-0036 — Stage 04: three checks before each probability (smallest resolving event, error band, statement type)

- **Problem:** C1 and C2. References: L3 §3.3 patterns 1 and 2 and §3.4; L1 §7 lesson 2; L4 §2.3 claim-type table; L2 finding 4.
- **Change:** in `prompts/04_forecasts.md`, section "Way of working", item 2 ("Before each probability"), add three bullets after the "by now we would expect to see …" bullet:

  > - **the smallest event that resolves YES**: re-read the criterion and name the least dramatic event that would meet it (for example one confirmed strike, one listing, one outlook change). Judge the probability of that event, not of the event the title suggests.
  > - **for a numeric or price threshold**: give a central estimate, a typical error for this series over the time left, and the p that this band gives. Take the error from the series' own recent history. For "on any day" questions, use the touch probability implied by recent volatility. Move away from that p only for a mechanism you name.
  > - **when a party's statement carries the forecast** (a refusal, a pledge, a declared deployment, a claim about control or damage): say which kind it is: procedural follow-through of a decision already taken, declared own action, negotiating stance, or claim about contested facts. Then say how often statements of that kind hold over a horizon like this one. A stance or a contested-fact claim alone never keeps p near 0 or 1.

  The lens definitions (A, B, C), aggregation, red team and scales are untouched. The text names no question, edition or outcome.
- **Level:** `minor` (stage prompt; methodology core untouched).
- **Expected effect:** fewer misses where the lens priced a harder event than the criterion requires; less compression for threshold questions in the 0.10–0.50 range. L3 §3.4 judged that 5 of the 10 misses would have moved toward the outcome by about 0.05–0.20, and that no hit would have been lowered.
- **How it will be measured:**
  1. **Before going live, out of sample.** These checks were derived from edition 02 misses, so a replay on edition 02 is in-sample and serves only as a harm check. The decision rests on an offline replay on **edition 03**, once at least 30 of its questions have resolved (expected about early January 2027).
     - Run `scripts/replay.sh` for lens B and lens A, three replays each, with the old and the new prompt.
     - Adopt the change if the new prompt's mean Brier is lower than the old one's by more than the noise floor (0.011, `reviews/replay/README.md`).
     - Also require that the A–B correlation of the replays does not rise above the live value for edition 03 (0.91).
  2. **Live, from the first edition after adoption, N ≥ 30 resolved questions.**
     - Paired Brier against the previous framework version, on questions of the same type and horizon.
     - Closed-cohort calibration in the 0.10–0.50 bins.
     - Mean p − YES rate for numeric-threshold questions.
- **Risks:**
  - **Overfitting:** the rules come from one edition's ten misses. That is why the decision rests on an out-of-sample replay.
  - **Lens diversity:** a shared checklist could make the lenses more alike (P-0008). This is measured in step 1.
  - **Lens time:** about 3 extra lines per question, inside the WP-09 budget.
  - **Blindness:** the wording is generic; it cites no outcome or benchmark.
  - **Comparability:** a new framework version. Scores are grouped by version (`scores.py --framework`).
- **Rollback:** remove the three bullets with a patch bump and a row in `methodology_changes.md`.
- **Timing:** not while an edition is between stages 03 and 06. The out-of-sample replay points to edition 05 or 06.

### P-0037 — Harvester: each page change gets its own item ID

- **Problem:** C3. References: L4 §4.2, §3.3 and §5.6 item 1; L4 §4.5 (`ofac_recent`, 3 resolutions read by hand).
- **Change:**
  - In `tools/harvester/store.py`, `item_id` keeps a `change-` fragment, so that each page change has a distinct ID. Every other URL is still de-duplicated on its canonical form:

    ```python
    def item_id(url, fallback=''):
        key = canonical_url(url) if url else fallback
        frag = urlparse(url).fragment if url else ''
        if frag.startswith('change-'):
            key += '#' + frag
        return hashlib.sha1(key.encode('utf-8')).hexdigest()[:16]
    ```

  - Add a unit test in `tests/`: two successive different changes of one page give two items; an unchanged page gives none; an RSS URL with an ordinary fragment still de-duplicates.
  - Before the change, check every other caller of `canonical_url` for de-duplication that bypasses `item_id`.
- **Level:** `patch`. A bug fix that restores the intended behaviour of `run_page` without changing the meaning of any output.
- **Expected effect:** official pages produce one item per actual change. The PL, IN and TW official silent cells close without a new source, and NATO and CN official stop being near-silent.
- **How it will be measured:**
  - Edition 04 harvest (`02_harvest/manifest.json`, `coverage.md`): at least 2 items in the window for at least 8 of the 12 `kind = page` sources.
  - Silent cells at most 5 (edition 02 level; edition 03: 8).
  - In the first 48 h after deployment, no page above 10 items a day.
  - Minimum N: 12 pages, one edition.
- **Risks:**
  - Pages with rotating content (dates, counters) could produce an item every sweep. Mitigate with the 48-hour check, and add a line filter if a page is noisy.
  - Page-source counts in edition 04 coverage are not comparable with editions 02–03; note this in `coverage.md`.
  - No blindness or scoring effect.
- **Rollback:** revert the function. The extra IDs in `seen.txt` are harmless.

### P-0038 — Harvester configuration: route the missed topics into the digests and retire failing sources

- **Problem:** C4. References: L1 §6 and §7 lesson 1; L4 §3.1, §3.2, §4.1, §5.1, §5.2 and §5.4.
- **Change** (for the next `/gH repair`; every addition subject to the robots, terms and sanctions checks of CLAUDE.md §6):
  - **`keywords.csv`:** K1–K8 as worded in L4 §5.1. The main ones:
    - K1, Polish rule of law: pl `trybunał konstytucyjny|trybunał|krs|sąd najwyższy|praworządn|weto|zawetow|wotum nieufności`; en `constitutional tribunal|constitutional court|rule of law|presidential veto`.
    - K2, a `western_balkans` concept, plus the `elections` terms `president resign|resigns as president|snap election|early election|caretaker government`.
    - K3, `swift` narrowed to `swift system|swift network|swift messag|swift payment`.
    - K4, a `sabotage_espionage` concept in en, de, pl and ru.
    - K5, LNG contract terms.
    - K6, `elections` terms in he, ar, fa, uk and zh.
    - K7, rebalance `russia_domestic`.
    - K8, narrow `elections` in pt.
  - **`feeds.csv`:**
    - F1: disable the 13 GDELT queries that have never produced an item, and raise `interval_h` of the rest to 24.
    - F2: disable `telesur_en` (robots.txt).
    - F3: replace `saba_ye`.
    - F4: repair `presstv`.
    - F5: replace `isw` with the criticalthreats.org listing.
    - F7: one Western Balkans pair.
    - F8: lower the volume of `g1`. The drops of `yle_news` and `faz_politik` are left to the quarterly review.
  - **`source_universe.csv`:** U1 (RS; RO, BG and EE official) and U2 (annotate SA and JP official as "no harvestable source").
  - **`registry/sources.csv`:** the notes texts proposed in L4 §2.5 for Interfax, Vedomosti, Euronews and Al Jazeera, in the notes field only. No rating changes.
- **Level:** `patch` (source configuration; batched under one bump).
- **Expected effect:** the topic classes that produced "collected but not used" surprises reach the digests. Fewer false matches and fewer dead queries in the shared host budget.
- **How it will be measured:**
  - Immediately after the repair, search the corpus by concept over the edition 02 and 03 windows (`python3 -m tools.harvester search`). Each L4 §3.1 topic should match its new concept for at least half of its items (Tribunal, Serbia/Vučić, Bosnia, Hanning, the QatarEnergy contract, Hebrew polls).
  - Edition 04: 0 false "swift" matches in a hand count of titles; the disabled sources no longer appear in `sources_health.md`.
  - L1 of editions 04 and 05: "collected but not used" at most 2 of 10 surprises (edition 02: 4).
- **Risks:**
  - More concepts compete for digest slots, which could dilute the PIR concepts. Check the digest line count per group in edition 04.
  - The concepts are general classes, not this quarter's events, which limits overfitting.
  - Config hashes change, so coverage trends from edition 04 carry that note.
  - No blindness or scoring effect.
- **Rollback:** revert the CSV rows. The manifest records the config hashes.

### P-0039 — Harvested series for data-threshold questions

- **Problem:** C5. References: L3 §3.3 pattern 1a and §4 gaps; L4 §3.1 last row, §3.3 "Data type", §4.5, §5.3 (D1–D4) and §5.6 item 5.
- **Change** (`sources/harvest/datasets.csv`, in the next `/gH repair`, subject to robots and terms):
  - D1: a TTF front-month daily series from a source whose terms allow it. If none exists, record the gap.
  - D2: Global Energy Flow storage as the AGSI+ fallback.
  - D3: EC Weekly Oil Bulletin, Eurostat HICP flash, GUS CPI flash and the FAO Food Price Index.
  - D4: a longer `portwatch` interval and retry window.
  - Only series that an existing adapter can read are added under this patch. A series that needs a new adapter is recorded as a separate `minor` proposal.
  - After the repair, add `registry/quant_map.csv` rows for active questions that the new series decide; stage 03 does this for new questions.
  - **Owner action, not part of the proposal:** set `AGSI_API_KEY`, `EIA_API_KEY` and `FIRMS_MAP_KEY` in `.env`. They have been missing since 05.10.2026, and 7 datasets are skipped.
- **Level:** `patch` (source configuration).
- **Expected effect:** threshold questions resolved from harvested primary data instead of vendor pages. The shadow run QNT can compute more questions, so the 30 pairs needed at the quarterly review arrive sooner. Lenses can read the series for the P-0036 error band.
- **How it will be measured:**
  - Editions 04–05: share of active numeric-threshold questions with a `quant_map.csv` row (target ≥ 80%).
  - Resolution rows read by hand or from a secondary carrier for these series: editions 02–03 had 13; target ≤ 2 per edition.
  - PortWatch days harvested in the window: edition 03 had 13 of 41; target ≥ 80%.
- **Risks:**
  - Licensing of exchange data (TTF): only terms-compliant sources; otherwise the gap is recorded.
  - No blindness effect (data only). No scoring change.
- **Rollback:** disable the rows.

### P-0040 — Stage 02: actor-language reads, a fixed "Incomplete key events" table, standing gaps

- **Problem:** C6. References: L4 §1.2 and §5.5 (M1, M3); edition 03 `08_quality_control.md` items 7 and 7a and its proposals 4, 5 and 7; P-0006 verdict (§1).
- **Change:**
  - `prompts/02_collection.md`, task 3, add:
    > **Actor-language read.** For every PIR-linked key event whose actor's language has at least 500 harvested items in the window (`02_harvest/coverage.md`), open at least one item in that language before you record an A-side gap. For PIR-5 key events this always includes Persian and Turkish.
  - `prompts/02_collection.md`, task 9, add:
    > End the Coverage section with a table **"Incomplete key events"**: event · missing perspective(s) · places searched (URL and date). Stage 07 copies these tables into J.3 unchanged.
    >
    > **Standing gaps.** A gap recorded in the same form in each of the two previous editions (for example the third-party front assessment) is listed once under "Standing gaps", with the date first recorded. Search for it only in the sources listed in `sources/source_map.md`; spend no further budget on it.
  - `prompts/02_collection.md`, "Indicative budget", add:
    > The budget is for a 14-day window. If the window is longer, scale it by window length / 14, at most double.
  - `prompts/07_report.md`, J.3 instruction, add one sentence: "Copy the 'Incomplete key events' tables of G1–G4; add events only, never drop one."
- **Level:** `minor` (stage prompts).
- **Expected effect:** more multi-perspective records; J.3 complete; no repeated rediscovery of the same standing gap.
- **How it will be measured** (editions 04 and 05, stage 08 items 7 and 7a):
  - Records with more than one perspective ≥ 43% (edition 02 level; edition 03 31%).
  - Languages used in stage 02 ≥ 14.
  - At least one Persian and one Turkish source used per edition.
  - Incomplete key events missing from J.3 = 0 (edition 03: 6).
  - Minimum: two editions.
  - Confounder: the edition 04 window is 14 days against 41 days in edition 03, so the per-day rate is not used as the measure.
- **Risks:**
  - More stage 02 work under the 5-hour usage window (`stage_time_audit.md`). Check the hours from start to site in `edition_metrics.csv`; the target is under 48 h.
  - No blindness effect: stage 02 is not a blind stage, and the text cites no outcome.
- **Rollback:** remove the added lines.

**Order of implementation if approved.** P-0037, P-0038 and P-0039 can go together in one `/gH repair` before edition 04's stage H (30.11). P-0040 can go before edition 04 as well. P-0036 waits for the out-of-sample replay. None may be applied while an edition is between stages 03 and 06.

---

## 4. What not to change yet (task 4)

| Looks bad | Why not now | Evidence that would justify a change |
|---|---|---|
| Red team adds nothing measurable (L2 finding 3) | Edition 02 −0.002 (90% [−0.0046, −0.0003]), edition 01 +0.004, pooled +0.001 (95% [−0.002, 0.006], N = 77). Signs differ by edition. A change is major (methodology core) | Paired AGG_RT − AGG interval on ≥ 30 red-team-changed forecasts, or the interval excluding 0 in the same direction in two editions. For the quarterly review |
| Aggregation adds nothing; lenses correlate at 0.90–0.96 (L2 finding 2) | Already P-0008 (DEFERRED_TO_Q). Shadow run B2 is the test in progress | B2 correlation and paired Brier, 30 pairs, at Q |
| Status quo baseline is weak (L2 finding 1) | Already P-0007 (DEFERRED_TO_Q) | Q review with N ≥ 30 (now N = 66 overall) |
| Compression in the 0.10–0.50 range (L2 finding 4) | N = 18; part of it is early-YES timing; extremising did not help (+0.007, interval includes 0). P-0036 attacks the cause, not the scale | Closed-cohort calibration with ≥ 30 forecasts in the range, over two editions |
| Confidence cap when a poll margin is below the recent polling error; polling error assumed to keep its direction (L3 M2, M9) | 2 questions | A third election miss of the same kind |
| Corpus delta read from the state date to the forecast date (L3 M1) | 1 question, under framework 1.4.0. Since 1.5.0 INFO_CUTOFF is the start of stage 03, which narrows the gap | A repeat in the L3 trace of edition 03 |
| Stale dataset values and dropped DECL flags in the report (L1 lesson 3) | 2 items in one edition (plus G1-029 at record level in edition 03, 08 discrepancy 1) | A repeat in L1 of edition 03 (possible from 30.11) |
| CRISIS signals set below the switching rule (L1 §5) | One edition; scenarios are not scored | The same pattern in L1 of edition 03 |
| Claim-type field in every fact record; "contested-fact claims stay DECL until a non-party measure" (L4 §5.6 item 3, §5.5 M4) | Changes the fact-record format and the status vocabulary of methodology §9, so it is major. P-0036 tests the idea inside stage 04 first | P-0036 adopted and helpful; then take the record field to Q |
| 429-aware back-off in the harvester code (L4 §5.6 item 2) | Configuration (F1, D4) comes first | PortWatch days harvested below 80% in edition 04 after D4 |
| Scaling the stage 02 budget as the main fix for record breadth (L4 §5.6 item 4) | Windows are 14 days again from edition 04 (P-0014). P-0040 adds only a safeguard | Multi-perspective share still below 43% in a 14-day edition |
| Source ratings (L4 §2.5) | Carriers relayed accurately; every failure belonged to the claimant | ≥ 3 decided claims per source with outlet-side errors |

---

## 5. Recorded in this run

- `reviews/learning/proposals.csv`:
  - status changes per §1 (CONFIRMED: P-0004, P-0005, P-0009, P-0013, P-0017, P-0018, P-0019, P-0032, P-0033; NO_EFFECT: P-0006, P-0011), with "L5 20.11.2026" notes;
  - new rows P-0036 – P-0040 with status `PROPOSED`.
- `AUTOPILOT_INBOX.md`, "Waiting for the user": one line per new proposal.
- Not applied: no prompt, tool, configuration, `CLAUDE.md`, methodology or `VERSION` change (AUTO mode, task 5–6 skipped).
- No web search; no forecasting service or market visited; no benchmark value used. No instruction-like content found in the files read.
