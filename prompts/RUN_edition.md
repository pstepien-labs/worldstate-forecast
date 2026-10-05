# Run a whole edition (orchestrator)

You are the **orchestrator**. You produce a complete edition — from the start of the edition to the final report and its quality control — by running every stage as a separate **stage-runner** sub-agent (Task/Agent tool, `subagent_type: stage-runner`; if that agent type is not available, use `general-purpose` and paste the contents of `.claude/agents/stage-runner.md` at the top of its prompt). Each sub-agent has a clean context: this is what keeps the three forecasting lenses and the red team blind to each other, so never merge stages into one sub-agent and never run them yourself.

Optional argument `STATE_DATE` (YYYY-MM-DD). The run is resumable: if it stops for any reason, the user types `/edition` again and you continue from the first unfinished stage.

## 1. Before the first stage

1. `python3 tools/pipeline.py status --json`. Keep only what you need from it; do not read edition content files (blindness — you are the link between stages).
2. Harvester: if the `harvester` line says NOT RUNNING, run `scripts/harvest.sh start` and tell the user in one line.
3. If `edition_closed` is true, a new edition is due:
   - If the user gave `STATE_DATE`, use it; otherwise use `suggested_state_date`.
   - If `can_start_next_edition` is false (today is earlier than `earliest_state_date`): stop and tell the user in 3 lines, using `today`, `earliest_state_date` and `state_date`: when the next edition can run and why (editions are two weeks apart; questions due in between are resolved at the start of the next edition). Offer: keep the harvester running and type `/edition` on that day. Only if the user explicitly asks for an earlier date, warn that fewer questions will be resolvable and continue with their date.
   - A state date in the future is never allowed.
4. Ask the user **once**, with the question tool: *"Stage 01 may flag uncertain resolutions for your approval. Pause for you there, or continue and let you approve them later?"* Options: **Continue, I'll review later (Recommended)** / **Pause for my approval**. (Unapproved flagged resolutions are simply left out of the scores until approved.)
5. Tell the user in 3–4 lines what will happen: about 15 stages, roughly 10–20 hours in total, each stage commits its own results, they can stop at any time (Esc or closing the window) and resume with `/edition`; they may need to approve web or command permissions the first time.

## 2. The stage loop

Repeat until stage 08 is done:

1. `python3 tools/pipeline.py status --json` → take `next` (`stage`, `arg`, `prompt`). For a new edition the first `next` is stage 00 with `arg` = `"<STATE_DATE> <NR>"` (use the STATE_DATE chosen in 1.3).
2. Launch one stage-runner sub-agent with this prompt (fill in the brackets):
   > Run stage `<stage>` of the pipeline with argument `<arg>`. Stage prompt file: `<prompt>`. Follow `.claude/agents/stage-runner.md`.
   Stages **always run one at a time** (they write to shared files such as the registry; parallel runs could lose rows).
3. When it returns, run `python3 tools/pipeline.py status --json` again:
   - stage now done → print one progress line for the user, e.g. `✓ 02 G1 — facts collected (3 of 15 stages done)`, plus any problem line the sub-agent reported; continue;
   - `STATUS: incomplete` or the stage is still not done → launch the same stage once more (it continues from its gaps);
   - still not done after the second attempt, or `STATUS: blocked` → stop and show the user the sub-agent's blocker and the exact command to resume (`/edition`).
4. Questions the sub-agent returns for the user: ask the user (question tool), then launch a new stage-runner for the same stage with the answer appended to its prompt.
5. After stage 01: if `01_resolutions.md` has a "FOR USER VERIFICATION" section with items **and** the user chose "Pause for my approval": show the items (ID, question, proposed outcome, evidence link) and ask which to approve. For approved IDs launch a stage-runner with: *"Append, for each of these question IDs, a new row to registry/resolutions.csv that copies the latest row with version+1 and user_approved=Y and notes 'approved by user <dd.mm.yyyy>'; then run `python3 tools/scores.py --out <DIRECTORY>/01_scores.md`; commit `edition-NN user verification`."* Otherwise just list the IDs waiting for approval in the final summary.

Never read `04_*`, `05_*`, `06_*`, `07_annex_benchmarks.md` or `registry/benchmarks.csv` yourself, and never pass anything from one stage's output to another stage's prompt: stages communicate only through files, under their own rules.

## 3. When stage 08 is done

1. Rebuild the public page and open data: `python3 tools/site.py`, then commit `edition-NN site`.
2. Launch one stage-runner for stage `S` with argument `release` (prompt file `prompts/S_social.md`) to draft the release thread; if stage 01 resolved questions, launch another for `resolved`.


Tell the user, in at most 10 lines:
- where the report is: `<DIRECTORY>/07_report.md` (and `07_report.pdf` if it was produced);
- the provenance line of the report (framework, methodology, models, harvest coverage);
- the number of questions resolved and the headline score from `01_scores.md` (if any were resolved);
- open items: resolutions awaiting approval, quality-control discrepancies from `08_quality_control.md` (count and file);
- that the harvester keeps running for the next edition, and the date it can start (`python3 tools/pipeline.py status`);
- the X drafts in `social/drafts/` to review and post by hand;
- `git push` publishes the commits and updates the public site if GitHub Pages is on (ask before running it).
