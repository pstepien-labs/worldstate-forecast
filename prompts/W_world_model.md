# Stage W — World model update (methodology v1.1 §3)

Runs once per edition, **after all four groups of stage 02 and before stage 03**. It keeps the model of power that the question bank is built from: the power ledger, the move → counter-move chains and the actor models. It writes no probabilities.

**Input, in this order:**
1. `world_model/` — `drivers.csv`, `ledger.csv`, `chains.csv`, `actor_models.md`, `quiet_list.md` (the state left by the previous edition).
2. `<DIRECTORY>/02_facts/G1–G4.md` — this edition's fact records.
3. `<DIRECTORY>/02_harvest/indicators.md` and `coverage.md`: primary-data values, unmatched share, source balance by power, and emerging terms.
4. `<DIRECTORY>/01_scores.md` — only the "Actor models" and "Drivers" sections (track record; no forecast values are needed).
5. The previous edition's `03_analysis.md` (key assumptions, indicators and warnings).
6. Web search and fetch, to fill ledger cells and verify chain links (budget below).

Blindness: the rules of CLAUDE.md 3.8 for stage 03 apply. Do not open any `04_*`, `05_*`, `06_*` file, `07_annex_benchmarks.md`, `registry/benchmarks.csv`, `registry/forecasts.csv`, `reviews/learning/`, `social/`, `docs/data/` or `docs/briefs/`. Do not visit the domains of CLAUDE.md item 9.

## Tasks

1. **Power ledger** (`world_model/ledger.csv`, one row per actor × factor; do not add or remove rows; a new actor or factor is decided by the quarterly review).
   - Update every row whose indicator has a new value in the facts, in `indicators.md` or in a primary source you can read. Write the value, unit, `as_of` (YYYY-MM-DD), `source_url`, `trend` (UP / FLAT / DOWN compared with the previous value), a one-line `assessment` beginning with ASSESSMENT, `confidence` (low / medium / high) and `updated_edition`.
   - **Priority this edition:** cells still marked `NO DATA`. In the first v1.1 edition, fill at least the rows of US, CN, RU and EU for all factors, plus the IND (defence-industrial) and ALL (alignment) rows of every actor. Cells you cannot fill stay `NO DATA` and are listed in the output file; they are never filled from memory (CLAUDE.md rule 1).
   - The indicator text may be made more precise, never replaced with a different measure. A change of measure is a quarterly-review decision.
2. **Chains** (`world_model/chains.csv`).
   - For each fact of this edition that responds to an earlier move by another actor, link it: add the fact ID to the chain's `links` (in order), update `last_move`, and write `reaction_to` into the output file's link table. A new chain needs at least two linked moves by different actors on one driver: open it with the next free ID `CH-NNN`.
   - For every ACTIVE chain, write `expected_next`: the most likely next move by each party, with its instrument and lag, and in `actor_model_basis` the actor-model claim it rests on. No probabilities.
   - Set a chain DORMANT after two editions with no new move, and CLOSED when it has ended (agreement, the issue gone), with the reason in `notes`.
3. **Actor models** (`world_model/actor_models.md`). Update what each actor reacts to, its repertoire, lag, red lines and constraints, citing chain IDs and fact IDs. Copy the actor-model track record from `01_scores.md` when it exists. Claims without evidence are marked ASSESSMENT with low confidence.
4. **Emerging terms → temporary concepts.** Read the "Emerging terms" table of `coverage.md`. For each term that names a development relevant to a driver and is not covered by a concept in `sources/harvest/keywords.csv`, append a row to `sources/harvest/keywords_emerging.csv`: concept `em_<short_name>`, label, groups, driver, terms (the term and up to 5 variants, `|`-separated, English first, other languages when the coverage table shows them), `added` (today), `expires` (today + 30 days), and the reason. Remove rows whose `expires` date has passed. At most 10 active emerging concepts.
5. **Question candidates from the model.** In the output file, section "Model candidates": 15–30 candidates for stage 03, each with:
   - origin `LEDGER` / `CHAIN` / `DRIVER_GAP` / `QUIET` / `TAIL`;
   - driver, form (EVENT / LEVEL / CONDITIONAL / SIGNPOST) and horizon class;
   - draft question and criterion, resolution source (readable without login, key or paywall), deadline;
   - for LEVEL: the series, its latest value and date, and 2–3 thresholds that span the plausible range;
   - for CONDITIONAL: the trigger question, the responding actor, the response and the window in days, and the chain ID;
   - a proposed `impact` (1–5) and `decision` (0–2) with a one-line reason (methodology v1.1 §4.6).
   
   Cover first: drivers below their panel floor (§4.1, count from `registry/question_meta.csv` and `registry/questions.csv`), open items of `quiet_list.md` (write the candidate's number into its Outcome column as `candidate W-NN`), and active chains with an `expected_next` move.
6. **Driver coverage table.** For each driver D1–D13: active questions, panel questions, mean `impact` of active questions with metadata, ledger cells with `NO DATA`, active chains.

## Output

- `world_model/ledger.csv`, `chains.csv`, `actor_models.md`, `quiet_list.md` (Outcome column only), `sources/harvest/keywords_emerging.csv`: updated in place.
- `<DIRECTORY>/03W_world_model.md`:
  - "Ledger changes" (actor, factor, old → new, source);
  - "NO DATA cells";
  - "Chain links" (fact ID → `reaction_to`);
  - "Chains" (ID, title, status, last move, expected next);
  - "Actor-model changes";
  - "Emerging concepts" (added, expired);
  - "Model candidates";
  - "Driver coverage".

**Budget:** 40–60 searches and fetches, spent first on NO DATA cells of the great powers and on verifying chain links. Save the ledger after every actor (checkpoint, CLAUDE.md rule 3.10). When the budget runs out, save, write "W incomplete: missing …" to `log.md` and stop. A rerun continues from the gaps.

## Prohibitions

No numerical probabilities. No benchmarks and no domains from CLAUDE.md item 9. Values in the ledger have a date, a publisher and a URL; anything else is ASSESSMENT.

**Log:** the stage entry in `log.md` gives the start and end time of the stage (dd.mm.yyyy hh:mm).

**Provenance:** `python3 tools/pipeline.py stage-start W --model "<your model id>"` at the start and `python3 tools/pipeline.py stage-end W` before the commit.

Commit: `edition-NN stage-W`.
