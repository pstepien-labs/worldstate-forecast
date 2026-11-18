# Run the learning loop (orchestrator)

Argument `SCOPE`: editions, e.g. `01-03`, `latest` (default) or `all`. Read `prompts/learning/README.md` first.

1. `python3 tools/pipeline.py status --json`. If an edition is between stage 03 and stage 06, stop: the learning loop may run before stage 03 or after stage 08 (it reads benchmarks and scores, and its approved changes must not alter a running edition).
2. Resolve the scope into a list of closed editions (`registry/editions.csv`). If none of them has resolved questions yet, say that L2 and L3 will be descriptive only.
3. Run **L1, L2, L3, L4 one after another**, each as a separate `stage-runner` sub-agent (Task/Agent tool) with the prompt: *"Run learning stage `L<n>` with argument `<scope>`. Stage prompt file: `prompts/learning/<file>`. Follow `.claude/agents/stage-runner.md`."* (`L1_hindsight.md`, `L2_forecast_performance.md`, `L3_reasoning_trace.md`, `L4_sources_coverage.md`.) After each, one progress line to the user; on `incomplete` retry once; on `blocked` stop and report.
4. Run **L5 yourself in this session** (it needs the user's decisions): follow `prompts/learning/L5_framework_proposals.md`, present each proposal with the question tool (Approve / Reject / Decide later), and implement approved patch/minor proposals as L5 describes.
5. Final summary (at most 10 lines): the review folder, the three main findings, proposals approved / rejected / deferred, the new framework version if one was set.

## AUTO mode (framework 1.9, WP-19)

If the arguments contain `--auto`, the autopilot started you after an edition closed, and nobody is watching.
- Run steps 1–3 as written.
- **Step 4:** run L5 yourself, but stop after its task 4. Append each proposal to `reviews/learning/proposals.csv` with status `PROPOSED`. Add one line per proposal under `## Waiting for the user` in `AUTOPILOT_INBOX.md`: date, proposal ID, title, level. **Apply nothing**: no change to prompts, tools, `CLAUDE.md`, the methodology or `VERSION`. Approval and implementation wait for the user (`/learn` in a normal session, or the quarterly review).
- Never ask the user anything and never push. Commit `learning <scope> auto`.
- The last line of your final message is `AUTOPILOT: complete learning <scope>` or `AUTOPILOT: blocked learning <reason>`.
