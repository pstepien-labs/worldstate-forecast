# Quarterly methodology review (c. 21.12.2026)

> Methodology v1.1 came into force early, on 22.11.2026, by user approval (framework 2.0.0). This review is its first check on data. It may confirm v1.1, adjust it (v1.2), or roll parts of it back.

**Goal:** derive the inference methodology for the next quarter from the data — on the basis of measurement, not impressions.

## Tasks

0. **Inputs from the learning loop.** Read the latest learning review(s) in `reviews/learning/` (L1–L5), every proposal with status `DEFERRED_TO_Q` in `reviews/learning/proposals.csv`, `reviews/2026-Q4_input_panel_importance.md`, and any expert responses filed under `reviews/experts/`. Group all results by framework and methodology version (`registry/editions.csv`; `python3 tools/scores.py --framework <v>`). If no learning review covers the quarter, run `/gL1`–`/gL4` for the quarter first.
1. **Full scores** (script `tools/scores.py`, all editions of the quarter):
   - Brier and BSS for AGG_RT relative to the status quo and to the crowd (EXACT only),
   - calibration,
   - runs A / B / C / AGG / AGG_RT — does aggregation help, does the red team help,
   - vectors, horizons, clusters (with a weight of 1 per cluster),
   - directional bias by `who_benefits`,
   - if the data allow: accuracy on questions whose key facts had an A perspective vs the rest.
2. **Uncertainty of the scores.** For every difference compared (e.g. lens A vs B) compute a bootstrap confidence interval (at least 2000 draws, resampling by cluster). If the interval includes zero — the conclusion is "no evidence of a difference".
3. **Ten largest errors** (highest AGG_RT Brier), **traced by layer** (methodology v1.1 §13). For each one, search the stored corpus for the deciding fact (`python3 -m tools.harvester search "<keyword>" --from <date> --to <forecast date>`). Then classify where the chain broke:
   - **collection gap:** not harvested;
   - **digest gap:** harvested, not surfaced to stage 02;
   - **model gap:** wrong ledger or chain;
   - **actor-model gap:** reaction mispredicted (name the actor);
   - **probability:** right model, wrong number;
   - **overreaction or underreaction to a headline**;
   - **timing**;
   - **ambiguous question.**
   
   Count the causes by layer. A layer with three or more errors gets a proposal in task 5.
4. **Protection against overfitting.** Judge whether the quarter was dominated by a single crisis or cluster. Identify conclusions that should not be generalised.
5. **Proposal for the next methodology version** (v1.2; v1.1 is already in force). At most 2–3 changes. Each with a justification in the data and an expected effect. The baselines stay unchanged. Examples of permitted changes:
   - lens weights in the aggregation,
   - dropping a lens that adds no value,
   - a new lens,
   - a change to the red-team adjustment limit,
   - a change to the horizon distribution,
   - a change to the PIRs.
5a. **Attention against importance** (methodology v1.1 §13). For every active question, attention = harvested items in the last 30 days for its concept (`world_model/drivers.csv` maps drivers to concepts), importance = `impact` (`registry/question_meta.csv`). Report the rank correlation, and list questions with high attention and low importance, and the reverse.
5b. **Quiet-but-important list.** Collect 5–8 items for next quarter in `world_model/quiet_list.md`: from outside experts (`reviews/2026-Q4_expert_packet.md`), the low-attention / high-importance list of 5a, and long-range assessments. Close the current quarter's items: question ID or reason.
5c. **Model review.**
   - **Drivers and ledger:** keep, merge or add drivers (`world_model/drivers.csv`) and ledger factors; review the actor list and `sources/harvest/power_weights.csv`.
   - **Emerging concepts:** promote the useful ones from `keywords_emerging.csv` to `keywords.csv`, and let the rest expire.
   - **Actor models:** compare their track record by actor (`python3 tools/scores.py`, "Actor models").
5d. **v1.0 against v1.1.** Compare the two cohorts on the same horizon classes only (`scores.py`, "Methodology v1.1 measures"). A difference counts only when its bootstrap interval excludes zero.
6. **New panel** for the next quarter, built **zero-based from the model** (methodology v1.1 §4.1): 40 questions, 5 per vector; every driver at least 2 and at most 6; at most 3 per cluster; about 12 Q, 16 Y and 12 M; 3–4 tail questions. Name the new panel set (e.g. `v1.1-2027Q1`); stage 03 of the next edition builds it.
7. **Approval.** Present the proposals to the user. After approval create `methodology/methodology_v1.2.md` as a new file — earlier versions stay unchanged. Bump `VERSION` to the next major version, set `METHODOLOGY=v1.2` in `editions/CURRENT.md` for the next edition, add a row to `methodology/methodology_changes.md`, and set the related proposals to `IMPLEMENTED`.

## Output

`reviews/2026-Q4.md` and, after approval, `methodology/methodology_v1.2.md`. Commit and tag `review-2026-Q4`.
