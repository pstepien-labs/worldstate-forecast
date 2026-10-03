# Stage 00 — Start of edition

**Parameters (from the command arguments):** `STATE_DATE` (YYYY-MM-DD) and `NR` (two digits, e.g. 01).

## Tasks

0. `python3 tools/pipeline.py status` — confirm that the previous edition is closed (stage 08 done and tagged). If it is not, stop and tell the user which stage is missing.
1. If the directory is not a git repository: `git init` and a commit "initial state".
2. Create the directory `editions/<STATE_DATE>_edition-<NR>/` with a subdirectory `02_facts/` and a file `log.md` (start time of stage 00).
3. Update `editions/CURRENT.md`: NR, STATE_DATE, PERIOD_FROM (state date of the previous edition), current DIRECTORY, PREVIOUS directory, PREV_TAG (tag of the previous edition), REGISTRY_BASELINE (git ref the registry is compared against — the previous edition's tag, unless `methodology_changes.md` names a different baseline), METHODOLOGY (the methodology file version in force, e.g. `v1.0`).
4. **Provenance.** Only now (the new DIRECTORY exists): `python3 tools/pipeline.py stage-start 00 --model "<your model id>"`. Write into `00_plan.md` the output of `python3 tools/pipeline.py versions` (framework version, methodology version, harvester version, commit, Claude Code version).
5. **Harvest.** `python3 -m tools.harvester status`. If the harvester has been running during the window: carry out stage H, MODE `digest` (`prompts/H_harvest.md`), including its provenance records. If it has not: record the gap in `00_plan.md` and `log.md`, start it (`scripts/harvest.sh start`) for the next edition, and continue with web search only.
6. Load the previous edition: its state block and report. For edition 01 the starting point was `editions/2026-09-21_edition-00/state_00.md` and `report_00.md`.
7. Check registry integrity: CSV headers match the template, question IDs are unique, no forecasts for non-existent questions, no changes to history (compare with REGISTRY_BASELINE). Record problems — do not repair history.
8. List the questions to resolve in stage 01: status ACTIVE and deadline ≤ STATE_DATE, or the event may already have occurred. Where a resolution source is harvested (`02_harvest/indicators.md`), note the value and its date next to the question.
9. Build a calendar for 6 weeks ahead (summits, central-bank meetings, elections, treaty and sanctions deadlines, expiring suspensions). Confirm every date on the web.
10. Priorities for stage 02: use `02_harvest/coverage.md` (concept volumes, flagged imbalances) and at most 10 searches to decide which vectors and regions changed most since the previous edition.

## Output

`00_plan.md`: edition parameters and versions (item 4); harvest window actually covered and its gaps; list of questions to resolve; calendar; PIRs (unchanged, from the methodology); collection priorities for groups G1–G4; registry problems.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

`python3 tools/pipeline.py stage-end 00`, then commit: `edition-NN stage-00`.

**Completion criterion:** `00_plan.md` exists, `CURRENT.md` is updated, commit done.
