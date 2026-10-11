# Stage 03 — Analysis and question bank

**Input:** `02_facts/G1–G4.md`, `00_plan.md`, the previous report and state block, the methodology.

If any group is marked incomplete in `log.md` — report it first and ask the user whether to continue.

## Information cutoff (from framework 1.5)

Write the first line of `03_analysis.md` as `INFO_CUTOFF: dd.mm.yyyy hh:mm` (local time), using the start time of this stage. This is the information set of the edition. Stages 03–05 use only facts dated on or before INFO_CUTOFF, and every forecast row of this edition carries its date. The lenses see the same post-state-date facts because they all come from item 1.7 below.

## Part 1: Analysis

1. **Draft sections A–G** according to methodology §11. Conclusions marked with the word ASSESSMENT, with analytic confidence. Each of sections B–F ends with a "Mechanism" paragraph (how events affect other sections) and a "For Poland" line.
2. **Comparison with the previous edition.** For every assessment of the previous edition: confirmed / refuted / unresolved — with evidence.
3. **Key assumptions check.** 5–8 assumptions of the current picture of the world. For each: what it rests on, what would refute it, current state.
4. **Analysis of competing hypotheses** for the three most important open questions: 3–4 hypotheses, an evidence matrix, which evidence rules hypotheses out (not only which supports them).
5. **Indicators and warnings matrix:** indicator → threshold → scenario it supports. Update relative to the previous edition.
6. **Mirror test:** identify places where the analysis may assume that another actor weighs costs and benefits the way the West does, and places where it relies on sources from only one side.
7. **Developments after the state date.** Facts dated after STATE_DATE and on or before INFO_CUTOFF that bear on an active question or a PIR. Carry over the post-state-date records of stage 02, and use at most 10 searches for decisive developments (questions due before STATE_DATE + 28 days, events in the `00_plan.md` calendar). Write full fact records (CLAUDE.md item 3.2) numbered `LT-01`, `LT-02`… This section is the only route by which post-state-date facts reach the lenses.
8. **Questions already determined.** For every ACTIVE question, check whether its YES criterion was met by an event dated on or before INFO_CUTOFF. Resolve each such question now, as `prompts/01_resolutions.md` tasks 1 and 3 describe: append a row to `registry/resolutions.csv` with `verify = Y` and the note "resolved in stage 03, before forecasts", and set its status to RESOLVED. It gets no forecast in this edition. List these questions in `03_question_bank_changes.md`. NO cannot be determined before the deadline, so only YES applies here.

## Part 2: Question bank

- **Edition 01:** set the standing panel — 40 questions, 5 for each of the 8 vectors. Starting point: `registry/question_proposals_edition_00.csv`. Verify each proposal (is it already resolved, is the criterion unambiguous, does the resolution source exist), fix or reject it, fill in missing vectors.
- **Every edition:** add 20–30 open questions, mainly from the "Question candidates" of stage 02. Methodology §3.1 allows up to 40; the lower intake stops lens research per question from thinning. After the additions, keep the number of ACTIVE questions at about 90 or fewer. Replace resolved panel questions with new ones from the same vector and cluster.
- For every new question fill in: `p_status_quo` (mechanical rule from §3.5), `who_benefits`, `pir`, `cluster`, `key_indicator`. **No forecast.**
- **Window.** The counting window of every new question starts after INFO_CUTOFF: write the start date into the criterion ("between dd.mm and dd.mm.yyyy"). Confirm that no qualifying event occurred up to INFO_CUTOFF (methodology §3.2: the event can still occur after creation).
- **Readable resolution source.** Create a question only if its resolution source was read successfully in this edition (stage 02, `02_harvest/indicators.md` or a check in this stage). Record, per new question in `03_question_bank_changes.md`, the source, the value or item read and its date. The criterion names:
  - the exact series (contract and field, publication, first release or revision);
  - one deciding source that the pipeline can read without a login, key or paywall;
  - a named fallback for when the deciding source is unavailable.
  
  "Source X or Y; in case of discrepancy Z decides" is allowed only if Z is readable. A source that needs a missing API key, a login or a paywall cannot be the deciding source. Edition 02: 10 of 27 resolutions were flagged ambiguous or unreadable, mostly ICE settlements and AGSI+.
- **Horizon proportions (§3.3)** and vector coverage. "By the next edition" means a deadline on or before STATE_DATE + 14 days. "By the end of the quarter" means a later deadline up to the last day of the current calendar quarter. Anything later counts as "longer".
- Append the questions to `registry/questions.csv` (status ACTIVE; sequential IDs: Q-0001, Q-0002…).

## Output

- `03_analysis.md` — the INFO_CUTOFF line and parts 1.1–1.8.
- `03_question_bank_changes.md` — new questions with the resolution source read for each, replacements, rejected proposals with reasons, questions resolved in item 1.8, horizon and vector statistics.

## Prohibitions

No probabilities other than the mechanical `p_status_quo`. No benchmarks and no domains from CLAUDE.md item 9. No facts dated after INFO_CUTOFF: if a search shows one, do not use or record it; count it in the log as "post-cutoff facts seen".

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-03`.
