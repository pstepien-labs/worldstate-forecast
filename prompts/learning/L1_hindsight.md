# L1 — Hindsight audit of reports

Parameter `SCOPE` (editions). Read `prompts/learning/README.md` first and follow its rules. Output: `reviews/learning/<today>_<scope>/L1_hindsight.md`.

Run for editions whose state date is at least 14 days in the past; the further back, the more reality is available.

## Tasks

1. **Scope and versions.** For each edition in scope: state date, framework and methodology version, models (from `registry/editions.csv`, `provenance.md`). List them in a table.
2. **Facts that did not hold.** From `07_report.md` and `02_facts/` take the 20 facts most important for the conclusions (PIR-linked, used in scenarios or in key assumptions) plus every DISP (disputed) item. For each: does it still stand today? Check with current sources (web, harvest corpus). Classify: confirmed / corrected (what changed, source, date) / refuted / still disputed. For refuted or corrected facts: what source and perspective (W/A/T) did the report rely on?
3. **Disputed events resolved by time.** For each "two interpretations" item: which interpretation turned out closer to reality, and was the evidence available at the state date?
4. **Assessments and assumptions.** Every ASSESSMENT with confidence medium/high in sections A–G, and every key assumption (KA…) from `03_analysis.md`: held / failed / undecided, with the dated evidence.
5. **Scenarios and warning signals.** For each horizon-1 scenario: which of its dated early warning signals fired, which did not, and which unlisted developments moved the world towards or away from it. Was the probability ordering sensible in hindsight? (Descriptive only: scenarios are not scored.)
6. **Surprises (misses).** The 10 most consequential developments since each state date that the report did not mention or anticipate (no question, no signal, no assumption). For each:
   - was it foreseeable at the state date (precursors in the news)? Search the harvest corpus for the window before the state date: `python3 -m tools.harvester search "<keyword>" --from <YYYY-MM-DD> --to <state date>` and the digest files `02_harvest/*`;
   - if precursors existed: were they in the digest, in the facts, or nowhere (not collected)?
   - classify: *not collectable* (no public precursor) / *not collected* (outside sources or keywords) / *collected but not used* / *used but misjudged*.
7. **Summary table** — per edition: facts checked, % refuted or corrected, assessments held/failed, surprises by class. End with the three most important lessons, each tied to a class from item 6 or a type of fact failure from item 2.

**Log and provenance:** `python3 tools/pipeline.py stage-start L1 --arg <scope> --model "<model id>"` … `stage-end L1 --arg <scope>`. Commit: `learning <scope> L1`.
