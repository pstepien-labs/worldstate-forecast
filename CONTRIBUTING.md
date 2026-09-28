# Contributing

The project works in English.

## Welcome

- Bug reports for `tools/scores.py`, with a sample CSV row.
- Reports of a wrong fact or a dead link in an edition (date, publisher, URL of the correct source).
- Source suggestions for `sources/source_map.md`, especially actor-side (A) and third-party (T) perspectives.
- Methodology proposals — as issues; they are considered at the quarterly review.

## Rules

1. **Append-only registry.** Pull requests that edit or delete existing rows in `registry/forecasts.csv`, `benchmarks.csv` or `resolutions.csv` will not be merged. A correction to a resolution = a new row with a higher `version`.
2. **Methodology v1.0 is frozen** until the quarterly review (`methodology/methodology_changes.md`).
3. **No git history rewrites** (rebase, force-push) on the main branch.
4. Formats per `CLAUDE.md` §5: CSV with `;` as separator, UTF-8 with BOM, probabilities 0.01–0.99.
5. No extra software — `scores.py` stays the only script, Python standard library only.

## Running your own edition

See `README.md` → "How to run one edition". Forking is the best way to run an independent forecast series.
