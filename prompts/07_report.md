# Stage 07 — Edition report

**Input:** all files of the current edition, the previous report, `01_scores.md`.

## Outputs

1. **`07_report.md`** — report following the structure in methodology §11.
   - **Provenance line** directly under the title (from framework 1.1): `Framework <VERSION> · methodology <METHODOLOGY> · commit <short hash at stage 07 start> · models: <from provenance.md> · harvest: <items in window>, <languages>, <countries>, Western share <x>% (02_harvest/manifest.json)`. Run `python3 tools/pipeline.py provenance` first. The same values go into section J.5 (process quality).
   - Section **0 (Accuracy scores)**, from edition 02: the key numbers from `01_scores.md` — number of resolved questions, Brier and BSS for AGG_RT vs status quo, best and worst lens (marked "indicative" below 30 questions), directional bias.
   - Section **H**:
     - scenarios in three horizons with probabilities, triggers and dated signals;
     - full list of AGG_RT forecasts grouped by vector: ID, question, deadline, AGG_RT, lens spread (min–max), change vs the previous edition.
   - **Do not put crowd or market forecasts in the main report.**
   - Section **K** in the format K.1–K.7, ready to paste into a national report.
2. **`07_annex_benchmarks.md`** — comparison with the crowd and discrepancies (from `06_benchmarks.md`). This file is forbidden to stages 03–05 in all future editions.
3. **`07_state_block.md`** — block L in a one-line-per-indicator format. Extension relative to edition 00: `active_questions=… | resolved_total=… | Brier_AGG_RT=… | BSS_vs_SQ=…`. From framework 1.1 add a last line `framework=<VERSION> | methodology=<METHODOLOGY> | edition_commit=<hash>`. Where a value comes from a harvested primary dataset, give that dataset as the source.
4. **`07_report.pdf`** — if `pandoc` or another converter is available; otherwise Markdown only, with a note in `log.md`.

## Editorial rules

- Outlets in `sources/harvest/no_republish.txt`: paraphrase only ("according to state agency X"), no quotations, no headlines; the report is published.

- Carry facts over from the previous edition only if stage 02 confirmed them; mark them "confirmed unchanged, dd.mm.yyyy". List removed facts in section J with the reason.
- All rules of CLAUDE.md item 3: distinction between fact / assessment / forecast, publisher and date with every fact, two interpretations for disputes, numbers instead of adjectives.
- Verbal text about probabilities — according to the scale in methodology §10.
- Length: main text 15–25 A4 pages; the forecast list as an annex.
- No padding or repetition. Section titles exactly as in the methodology, so that editions are comparable.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-07`.
