# Stage P — Apply learning proposals by policy (autopilot)

Framework 1.10 (user decision 20.11.2026: "auto-apply with guardrails"). The autopilot runs this after an edition's learning reports, in a **separate git worktree on its own branch**. You prepare commits; **`scripts/autopilot.sh` then checks each commit and lets onto `main` only those that pass**: tests, track-record guard, protected files, and the replay gate for lens-prompt changes. Nothing you do here is published directly.

Provenance: `python3 tools/pipeline.py stage-start P --model "<your model id>"` … `python3 tools/pipeline.py stage-end P`. Output: `reviews/learning/<today>_apply.md`.

## Which proposals

Rows of `reviews/learning/proposals.csv` with status `PROPOSED` or `APPROVED`, except the IDs the run prompt lists as rejected earlier. For each one:

| Level / what it changes | Action |
|---|---|
| `major`, or anything in the methodology core (lenses, aggregation, red-team limits, panel, scales, PIRs, score definitions) | do not apply; set status `DEFERRED_TO_Q` (only `status` and `notes` may change in existing rows) |
| changes to `prompts/03_analysis.md`, `05_red_team.md`, `06_aggregation_and_benchmarks.md`, `tools/scores.py`, `tools/quant.py`, `tools/coherence.py` | do not apply: they change forecasts and cannot be replayed. Set `DEFERRED_TO_Q`, with the note "needs the user (not replayable)" |
| changes to `prompts/04_forecasts.md` | apply. The script replays it on a past edition and keeps it only if it is no worse than the best replay so far plus the noise floor |
| everything else (`patch` and process `minor`: harvester code and configuration, sources, stages 00–02, H, 07, 08, E, I, V, the learning prompts, `RUNBOOK.md`) | apply |
| a proposal that needs something only the owner can do (an API key, a login) | apply the part that needs no owner. Name the owner action in the commit message and in your output file |

**Never change:**
- `CLAUDE.md`, every file in `methodology/`, `registry/`, `world_model/drivers.csv`;
- `tools/blindness_guard.py`, `tools/registry_guard.py`, `tools/autopilot.py`, `scripts/autopilot.sh`;
- `.claude/`, `.github/`, `editions/`, `docs/`, `autopilot.conf`, `AUTOPILOT_INBOX.md`;
- existing files in `tests/`. You may add new test files.

The script rejects any commit that touches these.

## How

1. Order: `patch` first, then process `minor`, then `prompts/04_forecasts.md` changes last. The script accepts commits in order and stops at the first that fails, so put the riskiest last.
2. **One commit per proposal**, made in this order:
   1. edit the files;
   2. if you changed harvester code, run `python3 -m tools.harvester selftest`;
   3. run `python3 -m unittest discover -s tests -t .`. Do not commit a proposal whose tests fail: set its status to `REJECTED` with the reason instead;
   4. bump `VERSION` (patch: x.y.Z+1; minor: x.Y+1.0);
   5. add a row to `methodology/methodology_changes.md` with "approved by policy (user decision 20.11.2026)";
   6. set the proposal's status to `IMPLEMENTED` with the version in `notes`;
   7. commit `framework <version>: <ID> <title> (applied by policy)`.
3. Write `reviews/learning/<today>_apply.md`: per proposal, the action, the files and the commit, plus the owner actions. Commit it last.
4. Never push and never touch `main` yourself. You are on the branch the script created.
5. The last line of your final message is `AUTOPILOT: complete improve <N applied>` or `AUTOPILOT: blocked improve <reason>`.
