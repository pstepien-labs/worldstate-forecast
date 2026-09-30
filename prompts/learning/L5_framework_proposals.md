# L5 — Framework improvement proposals

Parameter `SCOPE`. Read `prompts/learning/README.md` first. Input: `L1_hindsight.md`, `L2_performance.md`, `L3_reasoning.md`, `L4_sources.md` from the same review folder (run the missing ones first, or state which are missing), `methodology/methodology_changes.md`, `reviews/learning/proposals.csv`. Output: `reviews/learning/<today>_<scope>/L5_proposals.md` and new rows in `reviews/learning/proposals.csv`.

## Tasks

1. **Status of earlier proposals.** For every row in `proposals.csv` with status IMPLEMENTED: did it have the expected, measurable effect (the metric named in its row)? If the data are not sufficient yet, say when they will be. Record the verdict in the new review, and set the old row's `status` to `CONFIRMED` or `NO_EFFECT` or keep `IMPLEMENTED` (only `status` and `notes` of existing rows may change).
2. **Candidate problems.** Collect problems from L1–L4 that are supported by evidence from at least two editions or at least three questions in two clusters. Drop anecdotes (list them under "watch").
3. **Proposals — at most 5 per review**, ranked by expected benefit. For each:
   - ID (next P-NNNN), title, problem with references (file + section/ID);
   - the exact change: file(s), what to add/remove/rewrite (quote the new wording);
   - **level**: `patch` (source configuration, clarifications, typos — no effect on method), `minor` (process: stages, prompts, harvester, provenance, report format — lenses/aggregation/scales untouched), `major` (methodology core: lenses, aggregation, red-team limits, panel, scales, PIRs — only through the quarterly review `/gQ` and a new methodology file);
   - expected effect and **how it will be measured** (metric, from which edition, minimum N);
   - risks: overfitting, blindness, comparability of future scores with past ones;
   - how to roll back.
4. **What not to change.** Name things that look bad in this sample but where the evidence is too thin, and the evidence that would justify a change later.
5. **Present to the user** for approval, proposal by proposal. Append all proposals to `reviews/learning/proposals.csv` with status `PROPOSED`, then set `APPROVED` or `REJECTED` according to the user's answer (with the date in `notes`).
6. **Implement approved `patch` and `minor` proposals** in the same session, one commit per proposal:
   - edit the files;
   - bump `VERSION` (patch: x.y.Z+1; minor: x.Y+1.0) — once per session if several proposals are implemented together, using the highest level;
   - add a row to `methodology/methodology_changes.md` (date, version, files, change, rationale with the proposal ID, approved by user);
   - set the proposal's status to `IMPLEMENTED` with the version in `notes`;
   - commit: `framework <new version>: <proposal ID> <title>`.
   `major` proposals are recorded as `DEFERRED_TO_Q` and handed to the next quarterly review.

Never implement a change while an edition is between stage 03 and stage 06 (check `python3 tools/pipeline.py status`): the edition must run on one framework version. If one is in progress, record the approval and implement after its stage 08.

**Log and provenance:** `stage-start L5 --arg <scope>` … `stage-end L5 --arg <scope>`. Commit: `learning <scope> L5`.
