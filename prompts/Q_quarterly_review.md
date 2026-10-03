# Quarterly methodology review (c. 21.12.2026)

**Goal:** derive the inference methodology for the next quarter from the data — on the basis of measurement, not impressions.

## Tasks

0. **Inputs from the learning loop.** Read the latest learning review(s) in `reviews/learning/` (L1–L5) and every proposal with status `DEFERRED_TO_Q` in `reviews/learning/proposals.csv`. Group all results by framework and methodology version (`registry/editions.csv`; `python3 tools/scores.py --framework <v>`). If no learning review covers the quarter, run `/gL1`–`/gL4` for the quarter first.
1. **Full scores** (script `tools/scores.py`, all editions of the quarter):
   - Brier and BSS for AGG_RT relative to the status quo and to the crowd (EXACT only),
   - calibration,
   - runs A / B / C / AGG / AGG_RT — does aggregation help, does the red team help,
   - vectors, horizons, clusters (with a weight of 1 per cluster),
   - directional bias by `who_benefits`,
   - if the data allow: accuracy on questions whose key facts had an A perspective vs the rest.
2. **Uncertainty of the scores.** For every difference compared (e.g. lens A vs B) compute a bootstrap confidence interval (at least 2000 draws, resampling by cluster). If the interval includes zero — the conclusion is "no evidence of a difference".
3. **Ten largest errors** (highest AGG_RT Brier). Classify the cause:
   - missing information,
   - wrong model of the actor,
   - overreaction to a headline,
   - underreaction,
   - wrong timing,
   - ambiguous question.
4. **Protection against overfitting.** Judge whether the quarter was dominated by a single crisis or cluster. Identify conclusions that should not be generalised.
5. **Proposal for methodology v1.1.** At most 2–3 changes. Each with a justification in the data and an expected effect. The baselines stay unchanged. Examples of permitted changes:
   - lens weights in the aggregation,
   - dropping a lens that adds no value,
   - a new lens,
   - a change to the red-team adjustment limit,
   - a change to the horizon distribution,
   - a change to the PIRs.
6. **New panel** for the next quarter: 40 questions, 5 per vector.
7. **Approval.** Present the proposals to the user. After approval create `methodology/methodology_v1.1.md` as a new file — v1.0 stays unchanged. Bump `VERSION` to the next major version, set `METHODOLOGY=v1.1` in `editions/CURRENT.md` for the next edition, add a row to `methodology/methodology_changes.md`, and set the related proposals to `IMPLEMENTED`.

## Output

`reviews/2026-Q4.md` and, after approval, `methodology/methodology_v1.1.md`. Commit and tag `review-2026-Q4`.
