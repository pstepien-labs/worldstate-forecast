# Autopilot inbox

What the unattended cycle (`scripts/autopilot.sh`, framework 1.8) could not settle alone. Nothing here blocks the cycle except items under **Blockers**. Remove an item once it is dealt with.

- To approve a disputed resolution, append a row to `registry/resolutions.csv`: copy the latest row with `version` + 1, `user_approved` = `Y` and a note. Or correct the outcome in that row.
- To stop the autopilot: `scripts/autopilot.sh pause`. To restart it: `scripts/autopilot.sh resume`.

## Blockers

## Waiting for the user

- 17.11.2026 · Q-0079 · stage V (edition 03) could not re-read IMF PortWatch (HTTP 429 quota exceeded), so the stage 01 YES (13.10.2026 = 17 transits) is unconfirmed for 08, 09 and 12–15.10; re-check the PortWatch series and approve or correct (see `editions/2026-11-16_edition-03/V_autoverify.md`).

## Decisions taken without the user
