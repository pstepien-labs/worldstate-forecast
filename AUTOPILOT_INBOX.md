# Autopilot inbox

What the unattended cycle (`scripts/autopilot.sh`, framework 1.8) could not settle alone. Nothing here blocks the cycle except items under **Blockers**. Remove an item once it is dealt with.

- To approve a disputed resolution, append a row to `registry/resolutions.csv`: copy the latest row with `version` + 1, `user_approved` = `Y` and a note. Or correct the outcome in that row.
- To stop the autopilot: `scripts/autopilot.sh pause`. To restart it: `scripts/autopilot.sh resume`.

## Blockers

## Waiting for the user

## Decisions taken without the user
