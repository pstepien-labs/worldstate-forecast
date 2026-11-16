# Stage V — Independent re-check of resolutions awaiting verification (autopilot)

Framework 2.0 (P-0012). The user does not review resolutions any more. A resolution flagged VERIFY (stage 01 item 2) is instead re-resolved **independently** by this stage. If the re-check agrees, the resolution becomes auto-verified and enters the scores. If it disagrees, it stays out of the scores and is listed for the user. This stage never changes an outcome.

Provenance: `python3 tools/pipeline.py stage-start V --model "<your model id>"` … `python3 tools/pipeline.py stage-end V`. Output: `<DIRECTORY>/V_autoverify.md`. Commit: `edition-NN autoverify`.

## Input

The list of question IDs is `pending_verification` in `python3 tools/pipeline.py status --json`. If it is empty, write "nothing to check" into `V_autoverify.md`, record the stage end, commit and stop.

## Steps

1. **Resolve blind first.** For every ID, read only its row in `registry/questions.csv`: the question, `resolution_criterion`, `resolution_source` and `deadline`. **Do not open `registry/resolutions.csv`, `01_resolutions.md` or `03_analysis.md` yet.** Determine your own outcome (1, 0 or VOID) with a resolution date and evidence, using the methodology §3.7 and §7 rules and the same strict reading of the criterion as stage 01:
   - the readable deciding source first, then the fallback;
   - the evidence URL and publisher;
   - for PIR questions, a second independent source;
   - your confidence (low / medium / high).

   Write all of them into `V_autoverify.md` under "Blind re-check" **before** step 2. Checkpoint every 5 questions.
2. **Compare.** Now open the latest row of each ID in `registry/resolutions.csv`.
   - **AGREE**: the outcome is the same and your confidence is medium or high. Append a new row that copies the latest row with `version` + 1, `user_approved` = `A`, and `notes` = `autoverify <dd.mm.yyyy>: independent re-check agrees (<your evidence URL>); <previous notes>`.
   - **DISAGREE**: the outcome differs, or your confidence is low. Append a new row that copies the latest row with `version` + 1, `user_approved` = `N`, and `notes` = `autoverify <dd.mm.yyyy>: DISPUTED, re-check says <outcome> (<evidence URL>), reason <one line>; <previous notes>`. The outcome itself is never changed. The user decides later by appending a row with `user_approved` = `Y`.
3. Run `python3 tools/scores.py --out <DIRECTORY>/01_scores.md` **only** if stage 07 of the current edition has not started yet (no `07_report.md`). Otherwise leave the scores file alone: the next edition picks the change up.
4. In `V_autoverify.md`, below the blind section, add a table: ID · stage 01 outcome · re-check outcome · AGREE/DISAGREE · evidence. Also append the DISAGREE IDs to the `## Waiting for the user` list in `AUTOPILOT_INBOX.md` (repository root; create the file if it is missing, with one line per ID: date, ID, one-line reason).

## Rules

- The registry is append-only (CLAUDE.md rule 3.7): only new rows.
- Rule 3.9 applies as in stage 01: no forecasting or betting sites.
- This stage reads no forecasts (no `04_*`, `05_*` or `06_*` files, no `forecasts.csv`). A resolution is a fact about the world, not about our forecast.
