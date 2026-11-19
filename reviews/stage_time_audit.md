# Stage-time audit (WP-20)

Date: 19.11.2026. Sources: `provenance.jsonl` of editions 02 and 03; `data/autopilot/runs/*.log`.

## Finding

The long stages are not long because of their work. In edition 03, **every stage that took more than 2 hours of wall time is exactly a stage that was interrupted and resumed**:

| Stage | Wall time (h) | Resumed |
|---|---|---|
| 01 | 2.35 | 1 |
| 02 G2 | 4.43 | 1 |
| 02 G4 | 8.39 | 1 |
| 03 | 8.62 | 1 |
| 04 C | 8.18 | 1 |
| 07 | 8.29 | 1 |
| E | 8.17 | 1 |

Every stage that was never interrupted took 0.1–0.3 h. That includes stage 06 (0.27 h in edition 03, against 2.97 h in edition 02).

The cause of the interruptions: **25 of the 26 headless runs** of edition 03 ended on the 5-hour usage limit ("You've hit your 5-hour limit · resets …"). The 1.8 autopilot counted each stop as a failure and backed off 1→2→4 h, often well past the reset. Example: the limit reset at 04:20 on 18.11, but the next run started at 08:09.

Edition 02's long stages (02 G3 at 43.9 h, 06 at 3.0 h, E at 3.1 h) come from the manual era: they were interrupted sessions continued later.

## Consequences

1. **Fixed in 1.9 (R9):** a limit stop is classified as `limit`. The autopilot waits until the reset plus 5 minutes and is not counted as failing (`tools/autopilot.py classify`, tests in `tests/test_autopilot.py`).
2. **No stage split is needed.** Step 2 of WP-20 was planned only for causes found (`tools/aggregate.py`, a longer render timeout), and the work of stages 06 and E is short. Nothing was built.
3. **Budget:** the binding constraint is the 5-hour usage window, not the agents' speed. From edition 04 the lenses get more searches (WP-09), so editions will cross more limit windows. With waits that end at the reset, an edition should still finish within about 2 days of its start, well inside the 14-day cycle. Measure it in edition 04: hours from the start to the `site` commit (target under 48 h).
