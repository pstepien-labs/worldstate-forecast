# Stage 03 — Analysis and question bank

**Input:** `02_facts/G1–G4.md`, `00_plan.md`, the previous report and state block, the methodology.

If any group is marked incomplete in `log.md` — report it first and ask the user whether to continue.

## Part 1: Analysis

1. **Draft sections A–G** according to methodology §11. Conclusions marked with the word ASSESSMENT, with analytic confidence. Each of sections B–F ends with a "Mechanism" paragraph (how events affect other sections) and a "For Poland" line.
2. **Comparison with the previous edition.** For every assessment of the previous edition: confirmed / refuted / unresolved — with evidence.
3. **Key assumptions check.** 5–8 assumptions of the current picture of the world. For each: what it rests on, what would refute it, current state.
4. **Analysis of competing hypotheses** for the three most important open questions: 3–4 hypotheses, an evidence matrix, which evidence rules hypotheses out (not only which supports them).
5. **Indicators and warnings matrix:** indicator → threshold → scenario it supports. Update relative to the previous edition.
6. **Mirror test:** identify places where the analysis may assume that another actor weighs costs and benefits the way the West does, and places where it relies on sources from only one side.

## Part 2: Question bank

- **Edition 01:** set the standing panel — 40 questions, 5 for each of the 8 vectors. Starting point: `registry/question_proposals_edition_00.csv`. Verify each proposal (is it already resolved, is the criterion unambiguous, does the resolution source exist), fix or reject it, fill in missing vectors.
- **Every edition:** add 20–40 open questions, mainly from the "Question candidates" of stage 02. Replace resolved panel questions with new ones from the same vector and cluster.
- For every new question fill in: `p_status_quo` (mechanical rule from §3.5), `who_benefits`, `pir`, `cluster`, `key_indicator`. **No forecast.**
- Check the horizon proportions (§3.3) and vector coverage.
- Append the questions to `registry/questions.csv` (status ACTIVE; sequential IDs: Q-0001, Q-0002…).

## Output

- `03_analysis.md` — parts 1.1–1.6.
- `03_question_bank_changes.md` — new questions, replacements, rejected proposals with reasons, horizon and vector statistics.

## Prohibitions

No probabilities other than the mechanical `p_status_quo`. No benchmarks and no domains from CLAUDE.md item 9.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

Commit: `edition-NN stage-03`.
