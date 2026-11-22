# Autopilot inbox

What the unattended cycle (`scripts/autopilot.sh`, framework 1.8) could not settle alone. Nothing here blocks the cycle except items under **Blockers**. Remove an item once it is dealt with.

- To approve a disputed resolution, append a row to `registry/resolutions.csv`: copy the latest row with `version` + 1, `user_approved` = `Y` and a note. Or correct the outcome in that row.
- To stop the autopilot: `scripts/autopilot.sh pause`. To restart it: `scripts/autopilot.sh resume`.

## Blockers

## Waiting for the user

- 22.11.2026 · `/gH repair` · YE state/loyal cell is empty: `saba_ye` (Saba, Houthi-run) was disabled after 7 weeks of HTTP 403. Stage 02 G1 proposed 21sept.net or ypagency.net (Houthi-run). Not added: a sanctions judgement is needed, and the domain would have to go into `sources/harvest/no_republish.txt`, which a repair may not edit. Decide: add one (with the no_republish entry) or keep YE as a standing gap.
- 22.11.2026 · `/gH repair` · Should `kcna.kp` and the newly added `rodong.rep.kp` (DPRK state media, `kcna_kp` and `rodong_en`) be listed in `sources/harvest/no_republish.txt`? Neither is listed now; a repair may not edit that file.
- 22.11.2026 · `/gH repair` · TR:western is a required cell with no source, but Türkiye is flagged `⚠ over` (ratio 2.22) and H §3a forbids adding sources for over-covered actors. Decide which rule wins (e.g. one low-volume BBC Türkçe or DW Türkçe feed), or drop `western` from TR's required roles.

## Decisions taken without the user
- 22.11.2026 framework 2.0.0 / methodology v1.1 (P-0042), approved by the owner in one decision: stage W, model-driven questions, broader harvester. The autopilot was paused during the change and resumed after it. Rollback: `git log --oneline pre-v1.1..` and revert.
- 22.11.2026 user decisions on all edition 03 items and on Q-0079 (approved YES): recorded in `editions/2026-11-16_edition-03/log.md`. The repair of 22.11.2026 left the harvester outside launchd; it was restored the same evening and `infra/verify.sh` passed.
