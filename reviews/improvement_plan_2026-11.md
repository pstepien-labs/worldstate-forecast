# Worldstate Forecast — improvement plan

Written 16.11.2026, after a review of the repository at commit `a297ad5` (framework 1.8.0, edition 03 in progress).
Reader: the model that will execute this plan (Opus 5.5 in Claude Code), and the project owner who approves it.

The plan lives outside the repository on purpose. Edition 03 was running during the review, and its stages commit with `git add -A`. Move this file to `reviews/improvement_plan_2026-11.md` in the first commit of the execution.

---

## 1. What the review found

The project's goal is to forecast better than simple baselines and prove it by measurement. Judged against that goal, the pipeline around the forecasts is strong and the forecasting step itself is the weakest part.

### 1.1 Forecast quality (the most important findings)

All numbers come from `registry/*.csv` on 16.11.2026: 26 scored questions, almost all forecast in edition 01. This is a small sample. Treat every number as a lead to re-check, not a conclusion.

| # | Finding | Evidence |
|---|---|---|
| Q1 | **The lenses get almost no time.** Each lens forecast 88 questions in about 12 minutes, with at most 20 searches. That is about 8 seconds and 0.2 searches per question. Forecasting took 0.6 h of a 9.6 h edition. | Edition 02 `provenance.jsonl`: stage 04 A/B/C = 0.20, 0.20, 0.19 h. Stage 06 = 2.97 h and stage E = 3.14 h. |
| Q2 | **The three lenses are one forecast repeated.** Averaging them adds nothing. | Correlation 0.90–0.95, median spread 0.06. Brier A 0.163, B 0.159, C 0.157, AGG 0.158. |
| Q3 | **Forecasts were too low on events that happened.** | Mean official forecast 0.42, YES rate 0.58. 9 of 15 YES outcomes had a forecast below 0.50; 1 of 11 NO outcomes had one above 0.50. |
| Q4 | **Finding Q3 is partly a selection effect**, and so is the headline skill score. A YES resolves on the day the event happens; a NO waits for the deadline. Early scores therefore over-count YES outcomes. | 32 active questions were past their deadline and unresolved on 16.11. Edition 03 resolves them, and most will be NO. |
| Q5 | **The official baseline is too easy.** 80 of 88 active questions have `p_status_quo` = 0.10, yet half of such questions resolved YES. | Scored questions with 0.10: N = 21, YES rate 0.52. BSS vs status quo 0.59, but vs a constant 0.50 only 0.36. Already recorded as P-0007. |
| Q6 | **The red team has not shown value yet.** | 18 adjustments in 161 forecasts. Of the 4 resolved: 2 improved the forecast, 2 made it worse. AGG 0.158 vs AGG_RT 0.160. |
| Q7 | **Simple extremizing does not help.** The error is a bias, not general under-confidence. | Pushing AGG away from 0.5 in log-odds: exponent 1.5 gives 0.156, exponent 2 gives 0.163. |
| Q8 | **About a fifth of the questions are numeric thresholds** (prices, rates, exchange rates). A language model guesses these; the harvester already stores the daily series to compute them. | About 19 of 88 active questions. Series in `sources/harvest/datasets.csv`: NBP, ECB, FRED, Bank of Russia, PortWatch. |
| Q9 | **The comparison with the crowd is still empty.** | 52 EXACT benchmark rows recorded, 3 scored pairs. |
| Q10 | **No uncertainty is reported.** With N = 26, a Brier difference of 0.003 between runs means nothing, but the tables invite reading it. | `tools/scores.py` prints point values only. |

### 1.2 Architecture and robustness

| # | Finding | Evidence |
|---|---|---|
| R1 | **Defect in the new autopilot: the harvester will not survive a restart.** When the hourly job restarts a dead harvester, launchd is expected to kill it again when the hourly job exits, because both share a process group. The harvester running today was started by hand, so it is safe until it dies or the Mac restarts. | `scripts/autopilot.sh` `tick()` calls `scripts/harvest.sh start`; the plist has no `AbandonProcessGroup`. Verify with the test in WP-01. |
| R2 | **Defect in the new autopilot: editions will drift to three weeks.** An edition starts only on a Sunday evening, but the due date is the previous state date + 14 days. Edition 03's state date is Monday 16.11, so edition 04 is due on Monday 30.11 and would start on Sunday 06.12. | `decide()` in `scripts/autopilot.sh`. |
| R3 | **The model is not pinned.** The headless runs use the alias `opus`, which changes when a new model ships. An edition could then mix models without anyone choosing that. | `~/.claude/settings.json`: `"model": "opus"`. `AUTOPILOT_MODEL` is empty. |
| R4 | **No tests and no CI outside the harvester.** `scores.py`, `pipeline.py`, `site.py`, `brief.py` and `autopilot.sh` have none. The scores are the project's product, and the append-only rule is enforced only by a prompt. | Only `tools/harvester/selftest.py` exists. `.github/` holds issue templates only. |
| R5 | **The autopilot's decision logic is Python inside a bash here-document.** It cannot be unit-tested as it stands. | `scripts/autopilot.sh`: `decide`, `heartbeat`, `state_set`. |
| R6 | **One machine.** The corpus (205 MB), the job and the credentials are on one Mac. FileVault blocks an unattended restart, automatic restart after a power cut is off, and the corpus has no backup. | Checked 16.11: `autorestart 0`, FileVault on, `data/` is git-ignored. |
| R7 | **Stage 06 and stage E are slow or fragile.** Each took about 3 h in edition 02, against 0.2–0.4 h for other stages. The cause is unknown: real work or interruptions. | Edition 02 provenance. |
| R8 | **The learning loop never runs.** `/learn` and the mini-retrospective "after edition 03" need the user, who is not there. | `prompts/M_mini_retro.md`, `prompts/RUN_learning.md`; `reviews/learning/` holds only `proposals.csv`. |

### 1.3 Security

The unattended agent reads the open web and 205,000 harvested items, has a shell, and runs as the owner's own macOS user. Text it reads can try to give it instructions.

| # | Finding | Evidence |
|---|---|---|
| S1 | **The GitHub credential is far wider than needed.** The stored token can write to every repository of the account and edit workflows. | `gh auth status`: scopes `repo`, `workflow`, `gist`, `read:org`. |
| S2 | **The push ban on agents is a prefix rule.** `git push` is denied, but other spellings (`git -C . push`, `gh api`) are not, and the credential is readable by the agent. | `.claude/settings.json` deny list. |
| S3 | **`.env` is protected from the Read tool only.** `Bash(cat:*)` is on the allow list, so `cat .env` is pre-approved. `.env` does not exist today; it will once X keys are added. | `.claude/settings.json`. |
| S4 | **Published HTML is not sanitised.** The brief body is written by an agent from web-derived text and published on GitHub Pages. The brief checker verifies numbers, not markup. | `tools/brief.py`: no check for `<script>`, event handlers or external URLs (verify). |
| S5 | **Nothing can stop a bad edition from being published.** Stage 08 records discrepancies and never blocks. | `prompts/08_quality_control.md`. |
| S6 | **History on `main` can be rewritten.** The public track record depends on it not being. | No branch protection was set up (verify with `gh api`). |

### 1.4 Simplicity

- X automation, the execution book, the social modes and two disabled routines are dead weight until X posting is decided.
- `RUNBOOK.md` describes both the manual and the unattended way of working. The manual way is now the exception.
- The report is about 130 KB. Nobody has measured which sections readers or the brief use.

---

## 2. Rules for the executing model

1. **When to work.** Never change the framework while an edition is between stages 03 and 06 (`CLAUDE.md` rule 3.14). Before any work package:
   ```bash
   scripts/autopilot.sh pause
   python3 tools/pipeline.py status          # must say the edition is finished
   ```
   Resume with `scripts/autopilot.sh resume` when the package is committed and its checks pass. The next window is from the end of edition 03 (expected 17–18.11) to 30.11.
2. **One work package = one proposal = one commit.** Add a row to `reviews/learning/proposals.csv` (next free ID is P-0013), a row to `methodology/methodology_changes.md`, and bump `VERSION` as each package says. Commit message: `framework X.Y.Z: <title> (P-00NN)`.
3. **The methodology is frozen until the quarterly review (about 21.12.2026).** Packages marked **[Q]** only prepare evidence and a proposal for that review. They must not change the official forecast (`AGG_RT`), the lenses, the aggregation, the red-team limit, the panel, the scales or the official score definitions.
4. **Shadow runs are the way to test forecast changes.** A shadow run is a new `run` label in `registry/forecasts.csv` (for example `QNT`). It is scored like any run and never enters `AGG` or `AGG_RT`. The registry stays append-only.
5. **Software stays standard-library Python and bash.** Every new file below needs the owner's approval of this plan (rule 3.13). No new dependencies.
6. **Do not weaken blindness.** Lenses never see benchmarks, other lenses, `reviews/learning/` or crowd values.
7. **Each package ends with its "Done when" checks.** Paste the command output into the commit body or into `reviews/improvement_plan_log.md`. If a check fails, stop and write the failure to `AUTOPILOT_INBOX.md` under `## Blockers`. Do not mark a package done with a failing check.
8. **Re-check the evidence first.** Section 1 was measured with N = 26. Package WP-06 repeats the measurements after edition 03. If a finding no longer holds, skip the packages that depend on it and say so in the log.

---

## 3. Work packages

Order: phase A first, then B, C and D. Within a phase, the order given.

### Phase A — Repair and safety net (framework 1.8.1 → 1.9.0)

#### WP-01 Harvester under its own launchd job (fixes R1)
- **Change.** Add `scripts/autopilot.sh install` step: a second launchd agent `com.worldstate-forecast.harvester` that runs `python3 -m tools.harvester watch` with `KeepAlive` true and `RunAtLoad` true, wrapped in `caffeinate -i -s`. Remove the harvester start from `tick()`; `tick()` only reports a dead harvester. `scripts/harvest.sh start` must refuse to start a second copy when the launchd job owns one (the lock file already prevents two).
- **Test first, to confirm the defect.** With the autopilot paused, stop the harvester, run `launchctl kickstart gui/$(id -u)/com.worldstate-forecast.autopilot`, wait for the tick to end, and check `scripts/harvest.sh status`. Record whether the harvester survived.
- **Done when.**
  - `launchctl print gui/$(id -u)/com.worldstate-forecast.harvester` shows the job running.
  - `kill <harvester pid>` is followed within 60 s by a new pid in `scripts/harvest.sh status`.
  - After a tick ends, the harvester is still running.
- **Version.** 1.8.1 (patch).

#### WP-02 Edition start on the due date (fixes R2)
- **Change.** In the decision logic, start the next edition on the first day on or after `earliest_state_date`, from `AUTOPILOT_START_HOUR` local time. Drop the Sunday condition for editions. Keep Sunday for the weekly source repair.
- **Done when.** A unit test (WP-04) feeds the decision function these cases and gets the expected action:

  | Today | Earliest date | Hour | Expected |
  |---|---|---|---|
  | Mon 30.11 | 30.11 | 19 | none |
  | Mon 30.11 | 30.11 | 20 | start |
  | Sun 29.11 | 30.11 | 21 | none |
  | Tue 01.12 | 30.11 | 08 | none (before the hour) |
  | Tue 01.12 | 30.11 | 20 | start |

- **Version.** Same commit as WP-01.

#### WP-03 Pin the model and record it (fixes R3)
- **Change.** Default `AUTOPILOT_MODEL` to an explicit model ID, set in one place: a new file `autopilot.conf` (`KEY=value`, read by the script). The first value is `claude-opus-5-5`. The orchestrator passes the same model to its stage-runner sub-agents. A model change is a patch-level proposal and never happens inside an open edition: the script refuses to start a run if `autopilot.conf` names a different model from the one in the open edition's first provenance record.
- **Done when.** `grep -c '"model": "claude-opus-5-5"' <edition>/provenance.jsonl` equals the number of start records in the next edition; the refusal is covered by a unit test.
- **Version.** Same commit as WP-01.

#### WP-04 Tests and a testable autopilot (fixes R4, R5)
- **Change.**
  1. Move the Python logic out of `scripts/autopilot.sh` into `tools/autopilot.py` with subcommands `decide`, `heartbeat`, `state-set`. The bash script keeps only process handling: lock, launchd, running `claude`, `git push`.
  2. Create `tests/` using `unittest` and a fixture registry in `tests/fixtures/registry/` (about 12 questions, 2 editions, resolutions covering YES, NO, VOID, VERIFY pending, `user_approved` Y, A and N).
  3. Tests to write:
     - `test_scores.py`: Brier and BSS against values computed by hand in the test; highest `version` wins; VERIFY pending excluded; `A` included and listed; a forecast dated on or after the resolution date is excluded; VOID excluded.
     - `test_pipeline.py`: next stage for an empty, a half-done and a closed edition; `pending_verification` splits unchecked from disputed; `site_done`.
     - `test_autopilot.py`: the WP-02 table; back-off after 1, 2, 3 and 6 failures; heartbeat unchanged → no new file; model mismatch refusal.
     - `test_registry_guard.py`: see WP-05.
     - `test_site.py`: the generated page contains no forecast for an unresolved VERIFY question as "resolved"; all values escaped.
  4. One command runs everything: `python3 -m unittest discover -s tests -v`, plus the existing `python3 -m tools.harvester selftest`.
- **Done when.** Both commands pass. `bash -n scripts/autopilot.sh` passes. `scripts/autopilot.sh status` prints the same "Next action" as before the move for the current state.
- **Version.** 1.9.0 (minor).

#### WP-05 Server-side guard for the track record (fixes R4, S6)
- **Change.**
  1. `tools/registry_guard.py <base-ref> <head-ref>`: fails if, between the two commits, any existing line of `forecasts.csv`, `benchmarks.csv` or `resolutions.csv` changed or disappeared, or if any field of `questions.csv` other than `status` and `notes` changed. It prints the offending lines.
  2. `.github/workflows/ci.yml`: on every push to `main`, run the unit tests and `registry_guard.py` on the pushed range. No secrets. Read-only permissions (`contents: read`).
  3. Branch protection on `main`: block force pushes and deletion. Direct pushes stay allowed, because the autopilot pushes directly. Ask the owner before running the `gh api` call that sets it.
  4. The daily cloud watchdog adds one check: the latest CI run on `main` is green (public API: `https://api.github.com/repos/pstepien-labs/worldstate-forecast/actions/runs?per_page=1`).
- **Done when.**
  - `python3 tools/registry_guard.py edition-02 HEAD` passes on the real history.
  - The fixture test with an edited forecast row fails with that row named.
  - A push shows a green run in `gh run list --limit 1`.
  - `git push --force` to `main` is rejected (test on a throwaway commit only with the owner's consent; otherwise check the protection with `gh api repos/pstepien-labs/worldstate-forecast/branches/main/protection`).
- **Version.** Same commit series as WP-04 (1.9.0).

### Phase B — Measure properly before changing the method (framework 1.9.x)

#### WP-06 Honest scores: cohorts, intervals, paired comparison (fixes Q4, Q10)
- **Change in `tools/scores.py`.** Official tables stay byte-for-byte the same. All additions go under "Diagnostics (not the official measure)".
  1. **Closed-cohort scores.** Score only questions whose deadline has passed, so early YES resolutions of still-open questions are left out. Print N, YES rate, Brier and BSS for this set next to the current set.
  2. **Intervals.** For every Brier and BSS in the Runs table, a 90% bootstrap interval, resampling whole clusters (2,000 resamples, fixed seed).
  3. **Paired differences.** Brier difference of each run against `AGG_RT` on the same forecasts, with the same bootstrap interval and the count of questions where each run was closer.
  4. **Derived aggregates, computed at scoring time, no registry rows:** median of A, B, C; mean in log-odds; log-odds mean with exponent 1.5. Listed as `derived:` rows.
  5. **Bias table.** Mean forecast minus YES rate, overall and by horizon (≤14 days, ≤100 days, longer) and by vector.
- **Then re-measure section 1.1** on the registry after edition 03 and write `reviews/measurements_after_edition_03.md`: each finding Q1–Q9 with its new numbers and "holds / does not hold / unclear".
- **Done when.**
  - `diff` of the official sections of `01_scores.md` before and after the change, for `--to-edition 02`, is empty.
  - Unit tests cover the cohort filter and check the bootstrap is reproducible (same seed, same interval).
  - The measurements file exists and gives a verdict per finding.
- **Version.** 1.9.1 (patch; diagnostics only).

#### WP-07 Replay harness: test a prompt change before using it
- **Why.** Without it, every forecast-quality idea needs two months of live editions to judge.
- **Change.** `prompts/R_replay.md` and `/gR`. It re-runs one lens prompt (the current one or a candidate) on a **closed** edition's inputs: that edition's `02_facts/*.md`, `03_analysis.md` and the questions active then. Web search and fetch are off, and the files of later editions are not read. Output goes to `reviews/replay/<date>_<label>/forecasts.csv` in the registry format. It never touches `registry/`. `tools/scores.py --forecasts <file>` scores a replay file against today's resolutions.
- **Validity conditions, checked and written into each replay report.**
  - The replay model's training data must end before the edition's information cutoff. Ask the model for its knowledge cutoff and record the answer; if it is on or after the cutoff, the replay is void.
  - Tools are disabled (`--disallowedTools WebSearch WebFetch`), so no outcome can leak in.
  - A replay is evidence for choosing between prompts. It is not a track record and is never published as one.
- **First use.** Replay the unchanged lens B prompt on edition 02 three times. The spread between the three is the noise floor: a candidate must beat the original by more than that.
- **Done when.** Three replays exist, each with a validity section; the scores of the three and of the original edition 02 lens B are in one table in `reviews/replay/README.md`, with the noise floor stated.
- **Version.** 1.9.2 (minor: new stage R; it produces no edition output).

#### WP-08 Weekly resolutions (fixes Q4 at the source; part of the owner's "weekly" request)
- **Change.** In the week between editions, the autopilot runs stage 01 and stage V only, for questions that are due or whose event has happened, then `scores.py` and `site.py`, then pushes. Label the stage argument `interim` so provenance separates it from the edition's own stage 01. No forecasts are made.
- **Why now.** It keeps the public scores and the site at most a week old, doubles the number of points at which resolutions are read while the evidence is fresh, and costs about one hour of agent time.
- **Done when.** A dry run on a copy of the repository (`git worktree add /tmp/wf-test`) resolves at least one due question, appends rows only (WP-05 guard passes), and rebuilds `docs/`. The decision test covers "day 7 after the state date → interim resolutions".
- **Version.** 1.10.0 (minor).

### Phase C — Better forecasts (shadow runs, framework 1.10.x–1.11.x)

Nothing in this phase changes the official forecast. Each package adds a shadow run or a check, with a rule fixed in advance for judging it.

**Judging rule for every shadow run (write it into `methodology_changes.md` with the package):** a shadow run is proposed for promotion at a quarterly review only if, on at least 30 resolved questions forecast by both, its paired Brier difference against the run it would replace has a 90% interval that excludes zero (WP-06 item 3). Otherwise it keeps running or is dropped.

#### WP-09 Give the lenses time and searches (addresses Q1)
- **Change.** The cap "at most 20 searches" and the single pass are in `prompts/04_forecasts.md`, not in the methodology, so this is a process change.
  1. Each lens works in batches of 10–15 questions grouped by cluster, saving after each batch (the checkpoint rule already requires it).
  2. Search budget per lens: 2 per question due within 28 days, 1 per other question, about 120 in total instead of 20.
  3. For each question the lens writes, before its probability: the two strongest reasons for YES, the two strongest for NO, and what it would expect to see by now if YES were coming. These go in the edition file, not in the registry.
  4. The log records minutes and searches per batch.
- **Check before adopting.** Replay (WP-07) the new prompt's steps 1 and 3 on edition 02 without searches. Adopt if it is not worse than the noise floor; the search budget cannot be replayed and is judged live.
- **Live measure.** Lens time per edition (target at least 1 h per lens), searches used, and Brier by horizon against editions 01–03.
- **Done when.** Edition 04 provenance shows each stage 04 run of at least 45 minutes and at least 60 searches logged, and stage 08 item 3 still passes.
- **Version.** 1.10.1 (minor).

#### WP-10 Computed forecasts for numeric questions: shadow run `QNT` (addresses Q8)
- **Change.**
  1. `registry/quant_map.csv` (new, append-only): question ID → series ID from `sources/harvest/datasets.csv`, condition type (`last_above`, `last_below`, `any_above`, `any_below`, `month_end_above`…), threshold, window start and end. Stage 03 fills a row for every new question that a harvested series decides; older active questions are mapped once by hand in this package.
  2. `tools/quant.py`: reads the series from `data/harvest/datasets/observations.jsonl` up to the information cutoff. It resamples historical daily log-changes in blocks of 5 days from the last 2 years (10,000 paths, fixed seed) and returns the share of paths that meet the condition, clipped to 0.01–0.99. For policy-rate questions decided at a scheduled meeting, it returns nothing: those stay with the lenses.
  3. Stage 06 appends the results as run `QNT` after the lens rows and before the freeze commit. `AGG` ignores them.
- **Validation.**
  - Unit test on a synthetic random-walk series: the computed probability of ending above the start is 0.50 ± 0.03, and of touching a level one standard deviation away matches the reflection-principle value within 0.03.
  - Back-test with real history, which is legitimate here because the method uses no model knowledge: for every already-resolved numeric question, compute `QNT` from data up to that edition's cutoff and score it. Report N and Brier against the lens runs on the same questions.
- **Done when.** The unit tests pass; the back-test table is in `reviews/quant_backtest.md`; edition 04's frozen commit contains `QNT` rows for every mapped question; the guard (WP-05) passes.
- **Version.** 1.11.0 (minor: new tool, new run label).

#### WP-11 A truly independent outside view: shadow run `B2` (addresses Q2, Q3)
- **Change.** A fourth, separate stage-04 session that sees less, not more:
  - **Input:** the question, its criterion, its deadline, the days remaining, and `registry/base_rates.csv`. Nothing else: no `03_analysis.md`, no fact files, no previous forecasts.
  - **`registry/base_rates.csv`** (new, append-only), built by `tools/scores.py --base-rates` from the project's own closed-cohort resolutions: YES rate by question family (vector × horizon band × `p_status_quo`), with N. A family with N below 10 falls back to the next coarser level.
  - **Task:** name the reference class, start from its rate, adjust for time remaining with the constant-rate formula, and stop. One line of reasoning per question.
- **Why.** It breaks the three sources of correlation at once: same facts, same narrative, same anchor. It also feeds the project's own hit rate back into a forecast, which no lens has today.
- **Check before adopting.** Replay on edition 02 (it needs no web). Report its Brier, its correlation with A, B and C, and the Brier of the mean of A, B, C and `B2`.
- **Done when.** The replay report exists; edition 04's frozen commit contains `B2` rows for every active question; `01_scores.md` diagnostics show the correlation of `B2` with each lens.
- **Version.** 1.11.1 (minor).

#### WP-12 Mechanical coherence check before the red team (addresses Q6)
- **Change.**
  1. `registry/relations.csv` (new, append-only): pairs of question IDs with a relation: `implies` (if A then B, so P(A) ≤ P(B)), `exclusive` (P(A) + P(B) ≤ 1), `same_event_later_deadline` (P(later) ≥ P(earlier)), `higher_threshold` (P(above higher) ≤ P(above lower)). Stage 03 adds rows for new questions in the same cluster.
  2. `tools/coherence.py <edition>`: reads the three lens rows, computes the mean, and lists every violated relation with the size of the violation. Output: `<DIRECTORY>/05_coherence.md`.
  3. Stage 05 reads that file first. A violation is a "logic" adjustment by definition; the ±0.15 limit is unchanged.
  4. `scores.py` diagnostics split red-team adjustments by type (evidence / logic / consistency) and score each type against the unadjusted mean.
- **Done when.** Unit tests cover each relation type; running it on edition 02 produces a file (list the violations found in the log); edition 04's `05_red_team.md` cites it.
- **Version.** 1.11.2 (minor).

#### WP-13 More questions that the crowd also answers (addresses Q9)
- **Change.** A new last step in stage 06, after the benchmarks: write up to 10 question candidates for the **next** edition to `<DIRECTORY>/06_mirror_candidates.md`. Each copies the event, deadline and criterion of a liquid external question on a PIR topic. The file holds no crowd value, no price and no URL of the external question; those go only to `benchmarks.csv` when the question exists. Stage 03 of the next edition may read this one file and treats the candidates like any other.
- **Guard.** Add the file to stage 08 item 5 (blindness check): it must contain no number between 0 and 1 and no forbidden domain.
- **Done when.** Edition 04 produces the file and it passes the guard. From edition 05, the count of EXACT matches among new questions is reported in `06_benchmarks.md`. Target: at least 8 per edition.
- **Version.** 1.11.3 (minor).

#### WP-14 **[Q]** Package for the quarterly review (about 21.12.2026)
Prepare, do not decide. One file, `reviews/quarterly_2026Q4_evidence.md`, with:
1. **P-0007 baselines.** BSS against: status quo, constant 0.50, the family base rate (`base_rates.csv`), `QNT` for numeric questions. Recommendation text for making the family base rate the official first baseline.
2. **P-0008 lens diversity.** Correlations and the paired comparison for `B2`, the derived aggregates and the lens-time change.
3. **Red team.** Brier with and without adjustments, by type.
4. **A second model as a lens.** The owner has xAI (Grok) credentials. Design only: a stdlib client `tools/lens_api.py` that sends the same lens packet (facts, analysis, questions) to another model with no web access and appends run `D`. Costs, the data sent to a third party (only already-public facts and questions), and the key in `.env`. Needs the owner's yes and a change to rule 3.13.
5. **Weekly editions.** Agent hours and usage per edition from provenance (editions 03–05), and whether WP-08 already gives enough freshness. Options: stay at 14 days; weekly re-forecast of questions due within 21 days only; full weekly editions.
6. **Recalibration.** If closed-cohort N ≥ 60: a one-parameter shift in log-odds fitted with leave-one-cluster-out, as a possible shadow run `CAL`. Otherwise "not enough data".

### Phase D — Security, resilience, simplicity (framework 1.12.x)

Can run in parallel with phase C, since it does not touch prompts 03–06.

#### WP-15 Least-privilege publishing (fixes S1, S2)
- **Step 1 (owner, 5 minutes).** Create a fine-grained GitHub token limited to `pstepien-labs/worldstate-forecast` with "Contents: read and write" only. Store it with `git credential-osxkeychain` for a remote URL that only the autopilot uses.
- **Step 2.** `scripts/autopilot.sh publish` pushes with that credential (a dedicated remote `publish`). The repository's `origin` for agents becomes read-only (`git remote set-url --push origin DISABLED`).
- **Step 3 (stronger, optional, owner decides).** Run the headless agent under a separate macOS user with no access to the owner's home folder and no GitHub credential; the publishing step stays with the owner's user. This is the real boundary against instructions hidden in web text. It needs shared group permissions on the project folder.
- **Done when.** From inside a headless run, `git push origin main` fails with "DISABLED". `scripts/autopilot.sh tick` still publishes. `gh auth status` for the token used shows access to one repository.
- **Version.** 1.12.0.

#### WP-16 Tighter permissions for unattended runs (fixes S3)
- **Change in `.claude/settings.json`.** Remove the broad `Bash(cat:*)`, `Bash(head:*)`, `Bash(tail:*)`, `Bash(grep:*)` allows, since the Read and search tools cover them. Deny: `Bash(*.env*)`, `Read(./.env)`, `Read(~/.ssh/**)`, `Read(~/.config/gh/**)`, `Bash(security:*)`, `Bash(gh:*)`, `Bash(curl:*)`, `Bash(osascript:*)`, `Bash(launchctl:*)`. Check the current Claude Code documentation for the exact pattern syntax and for the Bash sandbox setting, and enable the sandbox with writes limited to the project folder if it is available.
- **Done when.** A headless probe (`claude -p "run: cat .env" --permission-mode auto`) with a dummy `.env` is refused, and the same for `gh auth token`. A full dry stage (`/gH status`) still works.
- **Version.** Same commit as WP-15.

#### WP-17 Sanitise what gets published and add a publish gate (fixes S4, S5)
- **Change.**
  1. `tools/brief.py check` and `tools/site.py` fail if the output contains: `<script`, `<iframe`, `<object`, an `on…=` attribute, `javascript:`, or a URL whose host is in `sources/harvest/no_republish.txt` or `forbidden_domains.txt`. External hosts allowed in the brief: the project site, the repository and the font host already in the template.
  2. Stage 08 marks each discrepancy `critical` or `minor`. Critical: a sampled fact not supported by its source (item 1), a probability outside section H (item 2), a registry change that is not an append (item 4), a blindness breach (item 5). The orchestrator in AUTO mode does not build the brief or the site while a critical item is open; it writes a blocker to the inbox.
- **Done when.** Unit tests: a brief body with `<script>` or `<img onerror=…>` fails the check. A fixture `08_quality_control.md` with one critical item makes `pipeline.py status --json` report `publish_blocked: true`.
- **Version.** 1.12.1.

#### WP-18 Survive the owner being away (fixes R6)
- **Owner actions, listed in `RUNBOOK.md` section 5:** `sudo pmset -a autorestart 1`; turn off automatic macOS update installation; decide on remote access (Tailscale with SSH, or Claude Remote Control).
- **Change.** A weekly `tar` of `data/harvest/datasets`, `data/harvest/state` and the last 60 days of `data/harvest/items` to a path named in `autopilot.conf` (`BACKUP_DIR`; an external disk or a synced folder), keeping 4 copies. Skip silently if the path is not set.
- **Done when.** `scripts/autopilot.sh backup` writes an archive and `tar -tzf` lists it; a restore into `/tmp` passes `python3 -m tools.harvester status`.
- **Version.** 1.12.2.

#### WP-19 The learning loop without the owner (fixes R8)
- **Change.** After each edition closes, the autopilot runs L1–L4 (reports only) in AUTO mode. L5 writes its proposals to `reviews/learning/` and to `AUTOPILOT_INBOX.md` under `## Waiting for the user` and applies nothing. Replace `prompts/M_mini_retro.md` by a note pointing to this.
- **Done when.** After edition 04: the four review files exist, the inbox lists the proposals, and `git diff` shows no change to prompts, tools or `VERSION` from that run.
- **Version.** 1.12.3.

#### WP-20 Find out why stage 06 and stage E take three hours (R7), then simplify
- **Step 1.** From the provenance and `data/autopilot/runs/*.log` of editions 03 and 04, split each stage's time into work and waiting (interruptions, retries, Chrome rendering). Write `reviews/stage_time_audit.md`.
- **Step 2, only for causes found.** Likely candidates: split stage 06 into `06a` aggregation and freeze (mechanical, a few minutes, could be a `tools/aggregate.py` that computes AGG and applies accepted adjustments exactly) and `06b` benchmarks; give `brief.py` a longer render timeout and a retry.
- **Step 3.** Housekeeping, no behaviour change: move the X material (`prompts/S_social.md` modes, `social/STRATEGY.md` rhythm section, the execution book) behind one line in `RUNBOOK.md` saying X is parked; make section 5 (autopilot) the main path in `RUNBOOK.md` and the manual commands an appendix.
- **Done when.** The audit file names a cause for each slow stage with evidence. If `tools/aggregate.py` is built: on editions 01 and 02 it reproduces the registry's AGG rows exactly and the AGG_RT rows from each `05_red_team.md`.
- **Version.** 1.12.4.

#### WP-21 A citable, timestamped archive per edition
- **Why.** The owner plans a PhD on this project; a DOI per edition is cheap proof of when each forecast existed.
- **Owner action.** Link the repository to Zenodo once (zenodo.org → GitHub → switch the repository on).
- **Change.** After the tag, the publishing step runs `gh release create edition-NN` with the report and brief attached. Zenodo then archives each release and issues a DOI. `register-edition` leaves the DOI column empty; the next edition's stage 00 fills it into `notes` when the DOI is visible.
- **Done when.** `gh release view edition-04` shows the two files; the Zenodo record exists (owner confirms).
- **Version.** 1.12.5.

---

## 4. Sequence and calendar

| When | What |
|---|---|
| After edition 03 closes (about 18.11) | Phase A: WP-01 to WP-05. Then WP-06 and the re-measurement. |
| By 29.11 | WP-07 (replay), WP-08 (weekly resolutions), WP-09, WP-10, WP-11, WP-12, WP-13 — whatever is finished and passing. Unfinished packages wait for the next window. |
| 30.11 | Edition 04 starts on the due date, with the shadow runs that are ready. |
| 01–13.12 | Phase D: WP-15 to WP-21. WP-20 step 1 needs edition 04's logs. |
| 14.12 | Edition 05. |
| About 21.12 | WP-14: evidence file for the quarterly review. The owner decides on the baselines, the lens changes, the second model and the cadence. |

If time is short, the order of value is: WP-01/02 (the cycle keeps running) → WP-06 (know what is true) → WP-09 and WP-10 (largest expected gain in accuracy) → WP-05 and WP-15 (protect the record and the account) → the rest.

## 5. How to validate the whole plan

1. **After every package:** its "Done when" checks, plus `python3 -m unittest discover -s tests -v`, `python3 -m tools.harvester selftest`, `python3 tools/registry_guard.py edition-02 HEAD` and `scripts/autopilot.sh status`.
2. **After phase A:** one supervised tick (`scripts/autopilot.sh tick` in a terminal) that ends with a push and a green CI run.
3. **Edition 04 is the integration test.** Afterwards fill this table in `reviews/improvement_plan_log.md`:

   | Measure | Editions 01–02 | Edition 03 | Edition 04 | Target |
   |---|---|---|---|---|
   | Days from due date to state date | 0 / 0 | 26 | | 0–1 |
   | Hours from start to publication | n/a | | | under 36 |
   | Autopilot blockers | n/a | | | 0 |
   | Lens time per lens (h) | 0.2 | | | at least 1 |
   | Searches per lens | at most 20 | | | at least 60 |
   | Lens correlation (A–B, A–C, B–C) | 0.90–0.95 | | | report; `B2` below 0.8 |
   | Flagged resolutions: auto-verified / disputed | n/a | | | report |
   | EXACT benchmark matches among new questions | | | | at least 8 |
   | Closed-cohort Brier, official run, with interval | | | | report |
   | Critical QC items | | | | 0 |

4. **Forecast quality is judged only by the rule in phase C** (30 paired resolved questions, interval excluding zero) and decided at a quarterly review. A package in phase C is "done" when its shadow run is produced correctly; whether it is *better* is a later, separate answer.

## 6. Decisions the owner must make

1. **Approve this plan** as proposals P-0013 onward (new files under `tools/`, `tests/`, `.github/`, new registry files, new run labels).
2. **WP-05:** allow branch protection on `main` (no force push, no deletion).
3. **WP-15:** create the single-repository token; decide whether to go as far as a separate macOS user.
4. **WP-18:** the power and update settings; where backups go.
5. **WP-21:** link Zenodo.
6. **At the quarterly review:** baselines, lens changes, a second model (Grok), weekly cadence.

## 7. What this plan deliberately does not do

- It does not change the official forecast, the lenses or the scores before the quarterly review.
- It does not automate X.
- It does not move the project off the Mac. If the Mac proves unreliable after WP-18, the next step is a small always-on Linux machine running the same two jobs; the code already avoids macOS-only parts except launchd and `caffeinate`.
- It does not shorten the report. That needs evidence of what readers use.
