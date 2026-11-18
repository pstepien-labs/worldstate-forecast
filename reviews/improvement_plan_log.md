# Improvement plan — execution log

Plan: `reviews/improvement_plan_2026-11.md` (approved by the user 16.11.2026: "ensure all implemented … then return to regular operations").
Built on branch `improve/plan-2026-11` in a separate worktree while edition 03 ran; merged after edition 03 closed.

## Evidence before changes

- **R1 confirmed 17.11.2026 00:0x:** a throwaway launchd job that started `nohup sleep 600 &` and exited had its child killed by launchd within 5 s (`child … KILLED by launchd`). A harvester restarted by `tick()` would therefore die at the end of the tick.
- **Data defect found during the review:** 6 rows of `data/harvest/datasets/observations.jsonl` (FRED, 21.10.2026) carry the date `    <link ` (an HTML page parsed as CSV). Fixed in WP-04 (`obs()` rejects non-ISO dates); the 6 rows are ignored by readers.

## Packages
