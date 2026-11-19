# Stage I — Interim resolutions (autopilot, off-week)

Framework 1.9 (WP-08). The autopilot runs this stage about 7 days after an edition's state date, between two editions. It resolves questions whose deadline has passed or whose event has happened, so that scores and the public site are never more than a week old. **It makes no forecasts and adds no questions.**

Provenance: `python3 tools/pipeline.py stage-start I --model "<your model id>"` … `python3 tools/pipeline.py stage-end I`. Output: `<DIRECTORY>/01_interim_resolutions.md` of the **current, closed** edition (`editions/CURRENT.md`). Commit: `edition-NN interim resolutions`.

## Steps

1. `python3 tools/pipeline.py status --json` must show `edition_closed: true`. Otherwise print `AUTOPILOT: blocked interim edition not closed` and stop.
2. **The list.** Take ACTIVE questions in `registry/questions.csv` whose deadline is before today, plus those whose YES event may already have happened (check at most 15 of these with one search each, starting with the nearest deadlines).
3. **Resolve** each one as `prompts/01_resolutions.md` tasks 1–3 describe: evidence, resolution date and confidence; VERIFY flags (ambiguous or disputed, plus a random 20%, with seed = edition number × 100 + day of month); new rows in `registry/resolutions.csv` (version 1); status in `registry/questions.csv`. Rule 3.9 applies: no forecasting or betting sites.
4. If any resolution of this stage has `verify = Y`, or `verification_retry` in `status --json` is not empty, carry out stage V (`prompts/V_autoverify.md`) in this same session, with its own provenance records. If a retried question is now confirmed, remove its line from `## Waiting for the user` in `AUTOPILOT_INBOX.md`.
5. `python3 tools/scores.py --out <DIRECTORY>/01_scores_interim.md`. Then `python3 tools/site.py` to rebuild the public page.
6. Commit `edition-NN interim resolutions` (registry, the two files, `docs/`). Never push.
7. The last line of your final message is `AUTOPILOT: complete interim <N resolved>` or `AUTOPILOT: blocked interim <reason>`.

## Rules

- The registry is append-only (CLAUDE.md rule 3.7).
- Do not open forecast files of the open or next edition. The edition is closed, and its forecasts are frozen; you do not need them.
- The next edition's stage 01 resolves whatever is still due and does not repeat what this stage resolved: it reads `registry/resolutions.csv`.
