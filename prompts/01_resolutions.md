# Stage 01 — Resolutions and scores

**Input:** `00_plan.md` (list of questions to resolve), `registry/*.csv`, methodology §7–§8.

In edition 01 there is usually nothing to resolve. In that case create `01_resolutions.md` and `01_scores.md` with the note "no resolutions in this edition", commit and stop.

## Tasks

1. For every question on the list determine:
   - outcome: 1 (YES), 0 (NO) or VOID (with a justification per §3.7),
   - resolution date,
   - evidence: URL, publisher, publication date; for PIR questions — a second, independent source,
   - resolution confidence (low / medium / high).

   A question whose deadline has not passed and whose event has not occurred stays ACTIVE.

   **Methodology v1.1 forms** (`registry/question_meta.csv`, `registry/relations.csv`):
   - **CONDITIONAL** (relation `conditional_on`, a = conditional, b = trigger): resolve the trigger question first. Trigger NO → the conditional question is VOID with the justification "trigger did not occur (Q-xxxx resolved NO)". Trigger YES → judge the response within its window counted from the trigger date; it stays ACTIVE until that window ends.
   - **LEVEL ladders** (relation `higher_threshold` within one cluster): resolve all rungs together from one reading of the series, and record the value, date and source once in each row's evidence.
   - **SIGNPOST**: resolved like any question; its long question is unaffected.
2. Mark VERIFY: ambiguous and disputed resolutions plus a random 20% of the rest. Draw the sample in Python with the seed equal to the edition number and record the list of drawn IDs.
3. Append rows to `registry/resolutions.csv` (version = 1). Change `status` in `registry/questions.csv` to RESOLVED or VOID (only that field and, if needed, `notes`).
4. Compute scores with `tools/scores.py` (it exists; run `python3 tools/scores.py --out <DIRECTORY>/01_scores.md`). Do not modify the script without user approval; if you find a bug — describe it in `log.md`. The script computes the scope of methodology §8:
   - Brier and BSS for runs A, B, C, AGG, AGG_RT,
   - BSS vs `p_status_quo` and vs the crowd (only EXACT matches from `benchmarks.csv`),
   - calibration in 10-percentage-point bins,
   - directional bias by `who_benefits`,
   - scores with a weight of 1 per cluster,
   - breakdown by vector and horizon,
   - methodology v1.1 breakdowns: by driver, form, horizon class and origin; importance-weighted Brier; actor-model scores (CONDITIONAL questions by responding actor); headline with and without the tail group; v1.0 and v1.1 cohorts separately.

   The script takes the row with the highest `version` for each question, and skips questions flagged VERIFY without user approval, listing them separately. From framework 1.5 it also leaves out the forecasts of an edition made on or after the question's resolution date (the outcome was already known), lists them, and adds a diagnostics section (other reference baselines, lens diversity). The diagnostics are not the official measure (methodology §1).
   - **Resolution date** = the date the YES event occurred, or the deadline for NO. Never the date you found the evidence.

## Output

- `01_resolutions.md` — list of resolutions with evidence, with a clearly separated section "FOR USER VERIFICATION".
- `01_scores.md` — score tables with the number of resolved questions and a note if there are fewer than 30 ("indicative scores").

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-01`.

**After the stage the user** reviews the VERIFY flags. Corrections are appended as a new row in `resolutions.csv` with a higher `version` and `user_approved = Y`.
