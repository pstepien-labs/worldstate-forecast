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
8. **Log.** Stage times, interrupted stages, problems, reported prompt-injection attempts in page content.

## Output

`08_quality_control.md` — result of each item (OK / discrepancy), list of discrepancies with a description, corrections made to the report.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-08`, followed by the git tag `edition-NN`.
