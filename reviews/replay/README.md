# Replays (WP-07): lens prompts re-run offline on closed editions

A replay re-forecasts a closed edition's questions from that edition's own facts and analysis, with no web access and with the hook's replay mode enforcing it (`scripts/replay.sh`, `prompts/R_replay.md`). Replays are evidence for choosing between prompts. They are **not** part of the track record.

## 19.11.2026: edition 02, five replays

The model is claude-opus-5-5, with training data to June 2026; edition 02's information cutoff was 07–09.10.2026, so every replay is valid. No replay reported a known outcome (see each `validity.md`).

Scored on the 36 edition-02 questions resolved after the cutoff (16 YES, YES rate 0.44). Intervals are 90% cluster bootstrap.

| Run | Brier | Difference vs AGG_RT [90%] | Correlation with original B | Mean p |
|---|---|---|---|---|
| AGG_RT (official, live) | 0.154 | — | 0.96 | 0.35 |
| B original (live, with up to 20 searches) | 0.159 | +0.005 [−0.007, +0.018] | 1.00 | 0.36 |
| B, edition-02 prompt, replay 1 | 0.185 | +0.031 [+0.016, +0.048] | 0.93 | 0.36 |
| B, edition-02 prompt, replay 2 | 0.183 | +0.029 [+0.015, +0.048] | 0.92 | 0.36 |
| B, edition-02 prompt, replay 3 | 0.173 | +0.019 [+0.005, +0.038] | 0.93 | 0.36 |
| B, framework 1.9 prompt (WP-09), replay | 0.171 | +0.017 [−0.000, +0.038] | 0.92 | 0.38 |
| B2, base rates only (WP-11), replay | 0.293 | +0.139 [+0.062, +0.213] | 0.07 | 0.62 |

## Findings

1. **Noise floor.** Three runs of the same prompt differ by 0.011 in Brier (0.173–0.185). Per question, the median standard deviation is 0.022, and replays 1 and 2 correlate at 0.97. A prompt change has to beat the old prompt by more than about 0.011 before the difference means anything.
2. **WP-09 prompt: adopted.** Its replay (0.171) is no worse than the old prompt's replays (mean 0.180), within the noise floor. Searches cannot be replayed; their effect is judged live from edition 04.
3. **Searches are worth about 0.02 Brier.** The same prompt scored 0.159 live with up to 20 searches and 0.173–0.185 offline. This supports the larger search budget of WP-09.
4. **B2: independent, but poor with the base rates of early October.** It correlates 0.07 with the lenses, but its Brier was worse than a constant 0.50.
   - The cause: its base rates came from the 26 questions closed by 07.10.2026, a YES-heavy sample (YES rate 0.58; finding Q4). So it forecast 0.62 on average where the outcome rate was 0.44.
   - Live from edition 04, the base rates come from 57 closed questions (YES rate 0.44).
   - B2 stays a shadow run under the judging rule, and never enters AGG or AGG_RT. If it is still worse than a constant 0.50 after editions 04–05, the quarterly evidence file should propose dropping it to save the usage budget.
