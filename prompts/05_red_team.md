# Stage 05 — Red team

Run in a new session. Your role: to refute, not to confirm.

**Input:** `03_analysis.md`, `04_forecasts_A.md`, `04_forecasts_B.md`, `04_forecasts_C.md`, `02_facts/*.md`, `registry/questions.csv`.

**Forbidden:** `06_*` files, `07_annex_benchmarks.md`, `registry/benchmarks.csv`, domains from CLAUDE.md item 9.

## Tasks

1. **Ten weakest points of the analysis.** Look in particular for:
   - assumptions without evidence,
   - sources from only one side,
   - Western bias and mirror-imaging,
   - overreaction to headlines,
   - omitted actors.

   For each point: evidence or argument and the impact on specific questions.
2. **Forecast review.** Compute AGG (mean of A, B, C) for every question and identify questions where:
   - AGG is inconsistent with the facts in `02_facts`,
   - there is a logical inconsistency between questions (e.g. P(A and B) > P(A), mutually exclusive questions summing to > 1),
   - lenses differ by more than 0.30 — explain which has the better basis.
3. **Proposed AGG adjustments.** Every adjustment must rest on specific evidence or an identified logical error. Limit: ±0.15 per question. No adjustments "to be safe" and no pulling towards 0.5 without a reason.
4. **Directional bias test.** Compare mean AGG with `p_status_quo` within `who_benefits` groups. Do the forecasts systematically favour one side? Identify the questions responsible.
5. **Consistency with scenarios.** Are the question forecasts consistent with the scenario probabilities the analysis anticipates?

## Output

`05_red_team.md` with an adjustments table: ID | AGG | proposed adjustment | AGG_RT | rationale | type (evidence / logic / consistency).

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-05`.
