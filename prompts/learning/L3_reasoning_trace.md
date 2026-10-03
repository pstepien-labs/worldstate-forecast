# L3 — Reasoning trace of misses and hits

Parameter `SCOPE`. Read `prompts/learning/README.md` first. Input: the list of largest errors and best calls from `L2_performance.md` (if L2 has not run, take the ten resolved questions with the highest and lowest AGG_RT Brier), and the surprises from `L1_hindsight.md`. Output: `reviews/learning/<today>_<scope>/L3_reasoning.md`.

## Tasks

For each selected question (up to 10 misses + 5 hits) trace the chain **as it was at the time**, using only the files of that edition, then compare with what is known now:

| Step | Where to look | What to record |
|---|---|---|
| Harvest | `02_harvest/*_digest.md`, `coverage.md`; corpus search for the window | Were the decisive signals present in the corpus? In which languages / from which side? |
| Facts | `02_facts/G*.md` | Were they turned into fact records? Perspectives W/A/T? Source ratings? Gaps recorded? |
| Analysis | `03_analysis.md` | Which key assumptions, ACH hypotheses and indicators bore on the question? Were they right? |
| Lenses | `04_forecasts_A/B/C.md` | Each lens's p and one-line rationale; which lens was closest and why; shared anchors (identical p across lenses)? |
| Red team | `05_red_team.md` | Did it flag the question? Direction and size of the adjustment; was it right? |
| Aggregation | `06_aggregation.md` | AGG vs AGG_RT; rejected adjustments |
| Resolution | `01_resolutions.md` of the resolving edition | Was the resolution clean, or was the question ambiguous? |

Then for each question:

1. **Where was the signal lost (miss) or found (hit)?** Name the step.
2. **Cause** — one primary, optionally one secondary:
   - information: *not collectable* / *not collected* (source or keyword gap) / *collected but not used*;
   - source bias: reliance on one side, a party's claim treated as fact, wire repetition counted as independent;
   - actor model: wrong model of an actor's preferences or constraints (mirror-imaging);
   - base rate: missing or wrong reference class;
   - reaction: over-reaction to a headline / under-reaction to a trend;
   - correlation: a shared assumption across lenses (e.g. one key assumption carried by many forecasts);
   - timing: right direction, wrong deadline;
   - question design: ambiguous criterion or resolution source;
   - noise: a well-reasoned forecast that lost to chance (say why you believe it was reasoned well).
3. **Counterfactual:** the smallest process change that would have moved the forecast the right way, and whether that change would have hurt any of the hits.

## Synthesis

- Table: question → step lost/found → cause → counterfactual.
- Cause frequencies, and which causes cluster in which vectors or lenses.
- Patterns that appear in at least three questions from at least two clusters (fewer = anecdote; say so).

**Log and provenance:** `stage-start L3 --arg <scope>` … `stage-end L3 --arg <scope>`. Commit: `learning <scope> L3`.
