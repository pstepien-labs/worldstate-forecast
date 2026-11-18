# Stage 06 — Aggregation, freezing, benchmarks

The order of the steps is mandatory.

## Step 1: Aggregation

1. For every active question compute AGG = mean of A, B, C from this edition. If a lens is missing — stop and report it (do not compute from two).
2. Apply the adjustments from `05_red_team.md`. Reject adjustments exceeding ±0.15 or lacking evidence and list them with the reason. AGG_RT = AGG + accepted adjustment; without an adjustment AGG_RT = AGG. Clip to the range 0.01–0.99.
3. Append rows with runs AGG and AGG_RT to `registry/forecasts.csv`, with `date` = the date of INFO_CUTOFF (first line of `03_analysis.md`), the same date as the lens rows.
4. Check the triviality rule (§3.8) and record the result.
5. **Shadow run QNT (framework 1.9, WP-10).** `python3 tools/quant.py forecast --edition <NN> --cutoff <INFO_CUTOFF date> --append`. It appends computed forecasts for the numeric questions mapped in `registry/quant_map.csv`, with run `QNT`. QNT and B2 are shadow runs: they never enter AGG or AGG_RT, and they are frozen with the rest in step 2. Record the number of QNT rows in the log.

## Step 2: Freezing

Commit with the message `edition-NN forecasts frozen`. Record the commit hash in `log.md`. From this moment the forecasts of this edition are immutable.

## Step 3: Benchmarks (only now)

1. For active questions look for counterparts on: Metaculus, Good Judgment Open, Polymarket, Kalshi, Manifold, RAND Forecasting Initiative.
2. Record in `registry/benchmarks.csv`: question ID, edition, date, source, p, URL, match (EXACT / APPROX), notes. For markets — volume or liquidity, if visible.
3. Do not change any forecast.

## Step 4: Question candidates for the next edition (framework 1.9, WP-13)

Write up to 10 candidates for the **next** edition's question bank to `<DIRECTORY>/next_question_candidates.md`. Each candidate copies the event, the deadline and the resolution criterion of a liquid external question on a PIR topic, so that the next edition can create a question with an EXACT benchmark match.

The file must contain **no probability or price**, no number between 0 and 1, and no name or URL of a forecasting site: stage 03 of the next edition reads it, and it must not leak crowd values. Record the external question's URL only in `registry/benchmarks.csv`, and only once the question exists. Stage 08 checks this file.

## Output

- `06_aggregation.md` — table of AGG and AGG_RT, rejected adjustments, result of the triviality test.
- `06_benchmarks.md` — list of matches and discrepancies |AGG_RT − crowd| ≥ 0.20, with a short hypothesis about the cause of each. This is material for review, **not** grounds for changing forecasts.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-06`.
