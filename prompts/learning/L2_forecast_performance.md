# L2 — Forecast performance

Parameter `SCOPE` (editions). Read `prompts/learning/README.md` first. Output: `reviews/learning/<today>_<scope>/L2_performance.md`.

## Tasks

1. **Scores.** `python3 tools/scores.py --editions <list>` for the scope, and additionally once per framework version present in scope (`--framework <version>`). Include the tables in the output. State N resolved questions; below 30 mark everything as indicative.
2. **Against baselines.** BSS of AGG_RT vs the status quo and vs the crowd (EXACT matches). Does the official forecast beat the simple baselines? With a cluster bootstrap interval for AGG_RT vs SQ where the tool supports it; otherwise report the paired mean difference and N. From framework 1.5, also report the diagnostics section of `scores.py`:
   - the YES rate by `p_status_quo` value: how hard is the status-quo baseline?
   - BSS vs a constant 0.50, vs the YES rate of earlier resolutions, and vs the previous edition's AGG_RT (did updating help?).

   This is evidence for proposal P-0007 (deferred to the quarterly review).
3. **Pipeline components.** Does aggregation help (AGG vs best single lens)? Does the red team help (AGG_RT vs AGG)? Which lens is best / worst, and is the difference outside the bootstrap interval (`--bootstrap A B`, `--bootstrap AGG_RT AGG`, …)? Report lens diversity by edition (correlations, median spread). Near-identical lenses cannot gain from averaging: this is evidence for proposal P-0008, deferred to the quarterly review.
4. **Where it fails.** Breakdowns by vector, horizon, cluster (weight 1 per cluster), `who_benefits` (directional bias), analytic confidence (low/medium/high: are high-confidence forecasts more accurate?), and by model when more than one model appears in provenance.
5. **Calibration.** 10-point bins: over- or under-confidence; extremes (p ≤ 0.10 or ≥ 0.90) — how often wrong.
6. **Version comparison.** If the scope spans framework versions: compare only overlapping question types/horizons and report whether the newer version is better, worse or indistinguishable. Never attribute a difference to a version change when the bootstrap interval includes zero.
7. **Ten largest errors** (highest AGG_RT Brier) and **ten best calls** (lowest Brier among questions with p far from the status quo, |p − p_status_quo| ≥ 0.20) — the input list for L3.
8. **Findings** — at most 5, each with numbers, N and interval; mark "no evidence of a difference" explicitly where applicable.

**Log and provenance:** `stage-start L2 --arg <scope>` … `stage-end L2 --arg <scope>`. Commit: `learning <scope> L2`.
