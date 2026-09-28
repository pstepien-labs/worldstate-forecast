# Stage 00 — Start of edition

**Parameters (from the command arguments):** `STATE_DATE` (YYYY-MM-DD) and `NR` (two digits, e.g. 01).

## Tasks

1. If the directory is not a git repository: `git init` and a commit "initial state".
2. Create the directory `editions/<STATE_DATE>_edition-<NR>/` with a subdirectory `02_facts/` and a file `log.md` (start time of stage 00).
3. Update `editions/CURRENT.md`: NR, STATE_DATE, PERIOD_FROM (state date of the previous edition), current DIRECTORY, PREVIOUS directory, PREV_TAG (tag of the previous edition), REGISTRY_BASELINE (git ref the registry is compared against — the previous edition's tag, unless `methodology_changes.md` names a different baseline).
4. Load the previous edition: its state block and report. For edition 01 the starting point was `editions/2026-09-21_edition-00/state_00.md` and `report_00.md`.
5. Check registry integrity: CSV headers match the template, question IDs are unique, no forecasts for non-existent questions, no changes to history (compare with REGISTRY_BASELINE). Record problems — do not repair history.
6. List the questions to resolve in stage 01: status ACTIVE and deadline ≤ STATE_DATE, or the event may already have occurred.
7. Build a calendar for 6 weeks ahead (summits, central-bank meetings, elections, treaty and sanctions deadlines, expiring suspensions). Confirm every date on the web.
8. Quick headline scan (at most 15 searches): which vectors and regions have changed most since the previous edition. Use it to set priorities for stage 02.

## Output

`00_plan.md`: edition parameters; list of questions to resolve; calendar; PIRs (unchanged, from the methodology); collection priorities for groups G1–G4; registry problems.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-00`.

**Completion criterion:** `00_plan.md` exists, `CURRENT.md` is updated, commit done.
