# Autopilot inbox

What the unattended cycle (`scripts/autopilot.sh`, framework 1.8) could not settle alone. Nothing here blocks the cycle except items under **Blockers**. Remove an item once it is dealt with.

- To approve a disputed resolution, append a row to `registry/resolutions.csv`: copy the latest row with `version` + 1, `user_approved` = `Y` and a note. Or correct the outcome in that row.
- To stop the autopilot: `scripts/autopilot.sh pause`. To restart it: `scripts/autopilot.sh resume`.

## Blockers

## Waiting for the user

## Decisions taken without the user
- 22.11.2026 framework 2.0.0 / methodology v1.1 (P-0042), approved by the owner in one decision: stage W, model-driven questions, broader harvester. The autopilot was paused during the change and resumed after it. Rollback: `git log --oneline pre-v1.1..` and revert.
- 22.11.2026 user decisions on all edition 03 items and on Q-0079 (approved YES): recorded in `editions/2026-11-16_edition-03/log.md`. The repair of 22.11.2026 left the harvester outside launchd; it was restored the same evening and `infra/verify.sh` passed.
- 22.11.2026 owner decisions on the three repair items: `ypa_ye` replaces `saba_ye`; ypagency.net, kcna.kp and rodong.rep.kp are in `no_republish.txt`; `dw_turkce` fills TR:western; the over-coverage flag never blocks a missing required role (`prompts/H_harvest.md` 3a). Repair no longer stops the harvester (framework 2.0.1).
