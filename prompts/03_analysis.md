# Stage 03 — Analysis and question bank

**Input:** `02_facts/G1–G4.md`, `00_plan.md`, `03W_world_model.md` and `world_model/` (methodology v1.1), the previous report and state block, the methodology.

If any group is marked incomplete in `log.md` — report it first and ask the user whether to continue.

## Information cutoff (from framework 1.5)

Write the first line of `03_analysis.md` as `INFO_CUTOFF: dd.mm.yyyy hh:mm` (local time), using the start time of this stage. This is the information set of the edition. Stages 03–05 use only facts dated on or before INFO_CUTOFF, and every forecast row of this edition carries its date. The lenses see the same post-state-date facts because they all come from item 1.7 below.

## Part 1: Analysis

1. **Draft sections A–G** according to the report structure of the methodology (v1.1 §12: section B ends with the table of active chains from `03W_world_model.md`; section G is written from the power-ledger changes). Conclusions marked with the word ASSESSMENT, with analytic confidence. Each of sections B–F ends with a "Mechanism" paragraph (how events affect other sections) and a "For Poland" line.
2. **Comparison with the previous edition.** For every assessment of the previous edition: confirmed / refuted / unresolved — with evidence.
3. **Key assumptions check.** 5–8 assumptions of the current picture of the world. For each: what it rests on, what would refute it, current state.
4. **Analysis of competing hypotheses** for the three most important open questions: 3–4 hypotheses, an evidence matrix, which evidence rules hypotheses out (not only which supports them).
5. **Indicators and warnings matrix:** indicator → threshold → scenario it supports. Update relative to the previous edition.
6. **Mirror test:** identify places where the analysis may assume that another actor weighs costs and benefits the way the West does, and places where it relies on sources from only one side.
7. **Developments after the state date.** Facts dated after STATE_DATE and on or before INFO_CUTOFF that bear on an active question or a PIR. Carry over the post-state-date records of stage 02, and use at most 10 searches for decisive developments (questions due before STATE_DATE + 28 days, events in the `00_plan.md` calendar). Write full fact records (CLAUDE.md item 3.2) numbered `LT-01`, `LT-02`… This section is the only route by which post-state-date facts reach the lenses.
8. **Questions already determined.** For every ACTIVE question, check whether its YES criterion was met by an event dated on or before INFO_CUTOFF. Resolve each such question now, as `prompts/01_resolutions.md` tasks 1 and 3 describe: append a row to `registry/resolutions.csv` with `verify = Y` and the note "resolved in stage 03, before forecasts", and set its status to RESOLVED. It gets no forecast in this edition. List these questions in `03_question_bank_changes.md`. NO cannot be determined before the deadline, so only YES applies here.

## Part 2: Question bank (methodology v1.1 §4)

Editions that run on methodology v1.0 (`METHODOLOGY=v1.0` in `CURRENT.md`) follow the v1.0 version of this part (git tag `pre-v1.1`). From edition 04 the rules below apply.

**Inputs for questions, in order of priority:**
1. the "Model candidates" of `03W_world_model.md` (origins LEDGER, CHAIN, DRIVER_GAP, QUIET, TAIL);
2. the "Question candidates" of stage 02, which name the news gate they pass (§4.3);
3. `<PREVIOUS>/next_question_candidates.md`, if it exists (mirrors of questions asked elsewhere; EXACT benchmark matches possible).

**A. Retro metadata (first v1.1 edition only).** If `registry/question_meta.csv` has no rows yet, first append one row for every ACTIVE question created before v1.1: `rating = RETRO`, `origin = V1.0`, `rated_on` = today, `edition` = this edition, plus driver (the cluster mapping in `world_model/drivers.csv` decides; a cluster not in the mapping gets the closest driver and a note), impact, decision, form (EVENT, or LEVEL for a numeric threshold) and horizon class (from its own created and deadline dates). Retro rows are excluded from importance weighting (§4.6).

**B. Panel rebuild (first v1.1 edition, then the first edition after each quarterly review).** If `question_meta.csv` has no row with `panel` = the current panel set (`v1.1-2026Q4` until the next review names a new one), build the panel of 40:
- 5 per vector;
- every driver D1–D13 at least 2, none more than 6;
- at most 3 per cluster;
- about 12 Q, 16 Y and 12 M horizons;
- 3–4 tail questions (`tail = Y`, horizon M).

Adopt existing ACTIVE questions that meet the rules (append a metadata row with the panel set; for v1.0 questions this is the RETRO row of step A, with the `panel` field filled), and create new ones for the rest. Newly created panel questions have type PANEL. Panel questions created under v1.0 that are not adopted run to their deadlines without replacement. List the panel in `03_question_bank_changes.md` with vector, driver, horizon class and form.

**C. Open questions: 20–30 new ones in every edition.**
- **Origin.** At least 60% have origin LEDGER, CHAIN, DRIVER_GAP, QUIET or TAIL. A NEWS question names in `notes` the gate it passes: (a) a ledger cell moved outside its normal range, (b) a chain trigger or response, (c) a new chain involving a great power.
- **Horizons** (§4.4): Q ≤ 90 days, Y 91–365 days, M > 365 days. At most 50% Q, at least 25% Y, at least 15% M. Signposts are not counted in these shares.
- **Forms** (§4.2, §4.5):
  - At least 20% are LEVEL questions, as ladders of 2–3 binary thresholds on one series and date (one cluster). Phrase every rung as "above X" so the ladder is monotonic, and append `higher_threshold` relations (a = the higher threshold).
  - When active chains exist, add at least 3 CONDITIONAL pairs: a trigger EVENT question plus "If <trigger> occurs between <dates>, will <actor> <response> within <N> days of it?" Append a `conditional_on` relation (a = conditional, b = trigger), and record `chain_id` and `actor` in the metadata.
  - Every M question has at least 2 SIGNPOST questions due within the quarter (`signpost_of` = the M question's ID).
- **ACTIVE count:** at most 100 after the additions. When near the cap, add fewer open questions; panel questions take priority.

**D. For every new question** append the question to `registry/questions.csv` (status ACTIVE; sequential IDs Q-0001, Q-0002…), with `p_status_quo` (mechanical rule, §4.8), `who_benefits`, `pir` (PIR-1 to PIR-8), `cluster` and `key_indicator`. **No forecast.** Then append its row to `registry/question_meta.csv`:
- `rated_on`, `edition`, `driver`, `impact` (1–5), `decision` (0–2; for 2, name the user and decision in `notes`), `form`, `horizon`, `origin`;
- `chain_id`, `actor`, `signpost_of`, `panel`, `tail` as applicable;
- `rating = NEW`.

Write the metadata now, before any forecast exists. It is never edited afterwards.

**E. Window.** The counting window of every new question starts after INFO_CUTOFF: write the start date into the criterion ("between dd.mm and dd.mm.yyyy"). Confirm that no qualifying event occurred up to INFO_CUTOFF (the event can still occur after creation).

**F. Readable resolution source.** Create a question only if its resolution source was read successfully in this edition (stage 02, stage W, `02_harvest/indicators.md` or a check in this stage). Record, per new question in `03_question_bank_changes.md`, the source, the value or item read and its date. The criterion names:
- the exact series (contract and field, publication, first release or revision);
- one deciding source that the pipeline can read without a login, key or paywall;
- a named fallback for when the deciding source is unavailable.

"Source X or Y; in case of discrepancy Z decides" is allowed only if Z is readable. A source that needs a missing API key, a login or a paywall cannot be the deciding source.

**G. Computed forecasts (framework 1.9, WP-10).** For every new question decided by a harvested numeric series (`sources/harvest/datasets.csv`, e.g. Brent, EUR/PLN, EU gas storage), append a row to `registry/quant_map.csv`: indicator, optional history indicator, condition (`last_above`, `last_below`, `any_above`, `any_below`), threshold, window start and end. Name any proxy in `notes`. Every rung of a LEVEL ladder on a harvested series gets its own row.

**H. Relations (framework 1.9, WP-12; v1.1).** For pairs of active questions where one logically implies the other (same event with a later deadline, a higher threshold, a narrower event), or which are mutually exclusive, append a row to `registry/relations.csv`: `implies`, `same_event_later_deadline`, `higher_threshold` or `exclusive` (a = the narrower question). Add `conditional_on` for conditional pairs.

**I. Quiet list.** For each `world_model/quiet_list.md` item turned into a question, write the question ID into its Outcome column. For each item rejected, write a one-line reason.

## Output

- `03_analysis.md` — the INFO_CUTOFF line and parts 1.1–1.8.
- `03_question_bank_changes.md` — new questions with the resolution source read for each, the panel (when rebuilt), rejected candidates with reasons, questions resolved in item 1.8, and the statistics after the additions: vectors, drivers (active and panel per driver, floors and caps), horizon classes, forms, origins (share from the model), mean `impact` of the panel, CONDITIONAL pairs, signposts per M question, ACTIVE count.

## Prohibitions

No probabilities other than the mechanical `p_status_quo`. No benchmarks and no domains from CLAUDE.md item 9. No facts dated after INFO_CUTOFF: if a search shows one, do not use or record it; count it in the log as "post-cutoff facts seen".

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-03`.
