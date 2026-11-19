# Improvement plan — execution log

Plan: `reviews/improvement_plan_2026-11.md` (approved by the user 16.11.2026: "ensure all implemented … then return to regular operations").
Built on branch `improve/plan-2026-11` in a separate worktree while edition 03 ran; merged after edition 03 closed.

## Evidence before changes

- **R1 confirmed 17.11.2026 00:0x:** a throwaway launchd job that started `nohup sleep 600 &` and exited had its child killed by launchd within 5 s (`child … KILLED by launchd`). A harvester restarted by `tick()` would therefore die at the end of the tick.
- **Data defect found during the review:** 6 rows of `data/harvest/datasets/observations.jsonl` (FRED, 21.10.2026) carry the date `    <link ` (an HTML page parsed as CSV). Fixed in WP-04 (`obs()` rejects non-ISO dates); the 6 rows are ignored by readers.

## Packages

| Package | Done | Evidence (“done when” checks) |
|---|---|---|
| WP-01 harvester under launchd | 19.11 | R1 confirmed beforehand (launchd killed a test child). After install: `kill` of pid 12256 → launchd restarted it as 12307 within 75 s; LIVENESS running |
| WP-02 start on the due date | 19.11 | `tests/test_autopilot.py::test_start_on_due_date_from_start_hour` (the plan's table); edition 04 decision: due 30.11 from 20:00 |
| WP-03 pinned model | 19.11 | `autopilot.conf` AUTOPILOT_MODEL=claude-opus-5-5; mismatch refusal tested; `claude -p --model` in every run |
| WP-04 tests, testable autopilot, R9 | 19.11 | 46+ unit tests pass locally (Python 3.9) and in CI (3.11). R9 (new finding): usage-limit stops are classified and waited out (4 real reset messages tested); FRED date defect fixed in `obs()` |
| WP-05 guard + CI + protection | 19.11 | `registry_guard.py edition-02 HEAD` and `edition-03 HEAD` OK; CI run on 9ee968e green (tests, selftest, guard); branch protection: force pushes and deletions off, enforce admins on |
| WP-06 honest scores | 19.11 | Official section byte-identical for `--to-edition 02` (before/after diff); re-measurement: `reviews/measurements_after_edition_03.md` |
| WP-07 replay harness | 19.11 | `scripts/replay.sh`, `prompts/R_replay.md`, hook replay mode (bug found and fixed in 1.9.1: the prompt file itself was blocked). Five valid replays of edition 02; noise floor 0.011 Brier (`reviews/replay/README.md`) |
| WP-08 interim resolutions | 19.11 | `prompts/I_interim.md`; decision tested (7 days after the state date → interim). First live run: 23.11 from 20:00 |
| WP-09 lens time and searches | 19.11 | Replay of the new prompt: 0.171 against 0.173–0.185 for the old one (within the noise floor) → adopted. Live with searches from edition 04 (target at least 45 min and 60 searches per lens). Searches are worth about 0.02 Brier (live 0.159 against offline 0.18) |
| WP-10 QNT | 19.11 | Unit tests: random walk 0.50 ± 0.03, touch probability equal to the reflection value ± 0.03 (this test exposed a drift bias; fixed by centring). EUR/PLN history source added (531 values). Back-test: QNT 0.058 against AGG_RT 0.214 on 4 questions (`reviews/quant_backtest.md`) |
| WP-11 B2 | 19.11 | Built (lens section, `--base-rates`, hook B2 mode, pipeline step for 1.9+). Replay on edition 02: correlation with the lenses 0.07 (independent) but Brier 0.293 (base rates from 26 YES-heavy early questions); kept as a shadow run with 57-question base rates from edition 04; drop proposal if still worse than 0.50 after editions 04–05 |
| WP-12 coherence | 19.11 | `tools/coherence.py`, `registry/relations.csv` (empty until stage 03 of edition 04 adds pairs); tests for each relation type; run on edition 02: 0 relations, 0 violations |
| WP-13 question candidates | 19.11 | Stage 06 step 4, stage 03, stage 08 check; first file in edition 04 |
| WP-14 quarterly evidence | 19.11 | `prompts/Q_evidence.md`; the autopilot runs it from 19.12.2026 |
| WP-15 least privilege | 19.11 | `origin` push URL = DISABLED (a plain `git push origin main` fails); the script pushes by URL. Owner action pending: fine-grained token + `publish` remote (RUNBOOK §5) |
| WP-16 secrets guard | 19.11 | Hook blocks `.env`, keychain, gh token, push, remotes, launchctl in every stage (tests); deny rules added |
| WP-17 publish check + QC gate | 19.11 | `tools/safehtml.py` in `brief.py` and `site.py` (site rebuilt cleanly through it); `Critical discrepancies open: N` → `publish_blocked` (tests) |
| WP-18 backup | 19.11 | `scripts/autopilot.sh backup`; owner action pending: `BACKUP_DIR`, `pmset autorestart`, automatic updates |
| WP-19 learning loop | 19.11 | `prompts/RUN_learning.md` AUTO mode; first run after 19.11 20:00 for edition 03 |
| WP-20 stage-time audit | 19.11 | `reviews/stage_time_audit.md`: the long stages are usage-limit waits, not work; no stage split needed |
| WP-21 releases | 19.11 | GitHub releases `edition-02` and `edition-03` created by the script. Owner action pending: link Zenodo |
| WP-22 blindness hook (new) | 19.11 | Live headless test: the exact incident command (`tail -2 registry/forecasts.csv` in stage 04 A) was blocked, also inside a sub-agent |

Watchdog (cloud routine) updated 18.11: CI status, publication gate, usage-limit waits are not alerts.

## Status 19.11.2026

All 22 packages are implemented and merged (framework 1.9.1). The autopilot resumed regular operation at 06:20. Owner actions pending: power and update settings, `BACKUP_DIR`, the fine-grained publishing token, Zenodo, and the inbox item Q-0079. Live validation: interim resolutions on 23.11; edition 04 from 30.11 (fill in the table in plan §5).
