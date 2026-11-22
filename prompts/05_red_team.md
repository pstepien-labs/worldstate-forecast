# Stage 05 — Red team

Run in a new session. Your role: to refute, not to confirm.

**Input:** `03_analysis.md`, `04_forecasts_A.md`, `04_forecasts_B.md`, `04_forecasts_C.md`, `05_coherence.md` (you create it in task 0), `02_facts/*.md`, `registry/questions.csv`, `registry/relations.csv`; from methodology v1.1 also `registry/question_meta.csv`, `03W_world_model.md` and `world_model/` (chains, actor models, ledger).

**Forbidden:** `06_*` files, `07_annex_benchmarks.md`, `registry/benchmarks.csv`, domains from CLAUDE.md item 9.

**Information cutoff:** evidence for adjustments must be dated on or before INFO_CUTOFF (first line of `03_analysis.md`). A fact on or before the cutoff that a lens missed is valid evidence. A later fact is not used; count it in the log as "post-cutoff facts seen: N".

## Tasks

0. **Coherence first (framework 1.9, WP-12).** Run `python3 tools/coherence.py <NN> --out <DIRECTORY>/05_coherence.md` and read it. Every violated relation (P(a) above P(b) where a implies b; or two exclusive questions summing to more than 1) gets a **logic** adjustment in task 3, in the direction that removes the violation and within the ±0.15 limit. If a relation itself looks wrong, say so; do not adjust for it. Shadow runs (B2, QNT) are not lens forecasts: ignore their files.
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
5a. **Model consistency (methodology v1.1 §6).**
   - LEVEL ladders are monotonic (the coherence check covers `higher_threshold`).
   - Every CONDITIONAL forecast is consistent with the actor model and chain it relies on. A lens that contradicts `actor_models.md` without new evidence is a weak point; so is an actor model that the facts of this edition contradict (report it to stage W of the next edition through `05_red_team.md`).
   - Each SIGNPOST is consistent with its long question.
   - Name any active chain whose `expected_next` move has no question, and any driver whose questions all point one way without evidence.
6. **Determined before the cutoff.** List active questions whose YES criterion was already met by an event dated on or before INFO_CUTOFF but which stage 03 did not resolve. Give the evidence. Do not adjust them: `tools/scores.py` leaves a forecast out of the scores when the question resolved on or before the forecast date, and the next stage 01 resolves them with that event date.

## Output

`05_red_team.md` with an adjustments table: ID | AGG | proposed adjustment | AGG_RT | rationale | type (evidence / logic / consistency).

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-05`.
