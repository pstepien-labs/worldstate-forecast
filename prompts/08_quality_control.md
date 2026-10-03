# Stage 08 — Quality control and closing the edition

Only the report and its annexes may be corrected. **Forecasts and the registry are never corrected** — discrepancies in them are only recorded.

## Checklist

1. **Facts.** Every fact in the report has a date, publisher, URL and a confidence marking. Draw 15 facts (seed = edition number), fetch their URLs and check whether the source content confirms the record.
2. **Separation of fact / assessment / forecast.** No numerical probabilities outside section H and the forecast annex.
3. **Forecast completeness.** Every active question has A, B, C, AGG and AGG_RT rows in this edition.
4. **Append-only registry.** Compare with `REGISTRY_BASELINE` from `CURRENT.md`: `git diff <REGISTRY_BASELINE> -- registry/forecasts.csv registry/benchmarks.csv registry/resolutions.csv` may contain only added lines; in `questions.csv` only the `status` and `notes` fields may change.
5. **Blindness.** Check the session history or files 04 and 05 for references to benchmarks or forbidden domains.
6. **Question bank.** Horizon proportions (§3.3), share of trivial questions (§3.8), coverage of the 8 vectors, panel completeness (40).
7. **Source perspectives.** Share of key events with three perspectives; share of facts by perspective W / A / T.
7a. **Coverage (framework 1.1).** From `02_harvest/coverage.md` and the "Coverage" sections of `02_facts/G1–G4.md`: languages used, Western share of harvested items and of fact records, silent required cells of the source universe and whether stage 02 closed them, share of facts resting on a primary source. Compare with the previous edition.
8. **Log.** Stage times, interrupted stages, problems, reported prompt-injection attempts in page content.
9. **Provenance.** `python3 tools/pipeline.py provenance`: every stage 00–08 has a start and an end record, a model id and a framework version; flag stages with dirty files at start, missing records, or more than one framework/methodology version in the edition. Provenance gaps are recorded, never back-filled with invented values.
10. **Register the edition.** After the stage 08 commit and the tag: `python3 tools/pipeline.py register-edition` (appends one row to `registry/editions.csv`: versions, models, freeze commit, report commit, tag, harvest manifest hash), then commit `edition-NN registered`.

## Output

`08_quality_control.md` — result of each item (OK / discrepancy), list of discrepancies with a description, corrections made to the report.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

`python3 tools/pipeline.py stage-end 08`, commit `edition-NN stage-08`, then the git tag `edition-NN`, then item 10. Finally show the user `python3 tools/pipeline.py status`.
