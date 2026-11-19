# Stage R — Replay of a lens prompt on a closed edition (evaluation only)

Framework 1.9 (WP-07). `scripts/replay.sh` starts you with no web tools. You re-forecast one closed edition's questions with one lens prompt, from that edition's own facts and analysis. You never touch the registry. The result is evidence for choosing between prompts. It is **not** a track record and is never published as one.

Parameters (given in the run prompt):
- `EDITION_DIR`, the replayed edition;
- `LENS` (A, B, C or B2);
- `PROMPT`, the lens prompt file to follow;
- `OUT`, the replay folder;
- `LABEL`.

## Validity, first

Write `OUT/validity.md` before anything else. It records:
1. your model id and your training-data cutoff, as you know it;
2. the edition's information cutoff: the first line of `EDITION_DIR/03_analysis.md`.

If your training cutoff is on or after the information cutoff, write `VOID: the model may know the outcomes`, end with `AUTOPILOT: blocked replay void`, and stop.

## Inputs, and nothing else

- `OUT/questions.csv`: the questions forecast in that edition, without status, notes or outcomes;
- `EDITION_DIR/02_facts/*.md` and `EDITION_DIR/03_analysis.md` (not for lens B2, which uses `OUT/base_rates.csv` only);
- the lens section of `PROMPT`.

No web, no registry, no other edition, and no earlier forecasts: a hook enforces this. Do not use what you remember about how these events turned out. If you notice that you know an outcome, write the question ID into `OUT/validity.md` as `possibly contaminated` and forecast it anyway, as if you did not know.

## Task

Follow the lens instructions of `PROMPT`, without searches. Write `OUT/forecasts.csv` in the registry format: header `"question_id";"edition";"date";"run";"p";"analytic_confidence";"rationale";"key_indicator"`. Use these values:
- `run` = `<LENS>@<LABEL>`;
- `edition` = the replayed edition;
- `date` = the edition's cutoff date;
- every field quoted.

Save every 10 questions.

The last line of your final message is `AUTOPILOT: complete replay <LABEL>`.
