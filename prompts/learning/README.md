# Learning loop (L1–L5)

A separate set of prompts that looks **back**: at finished reports, at what actually happened since, at the reasoning that produced the forecasts, at the sources and at the framework itself — and turns that into concrete, versioned improvement proposals.

| Step | Command | Question it answers | Output |
|---|---|---|---|
| L1 | `/gL1 <scope>` | What did the reports get wrong or miss, judged against the facts known today? | `L1_hindsight.md` |
| L2 | `/gL2 <scope>` | How accurate were the forecasts — by run, lens, vector, horizon, cluster, framework version, model? | `L2_performance.md` |
| L3 | `/gL3 <scope>` | For the biggest misses and hits: at which step of the pipeline was the right signal lost or found? | `L3_reasoning.md` |
| L4 | `/gL4 <scope>` | Which sources and which coverage gaps drove errors; which sources proved reliable? | `L4_sources.md` |
| L5 | `/gL5 <scope>` | What should change in the framework, at which version level, and how will we know it helped? | `L5_proposals.md` + rows in `reviews/learning/proposals.csv` |

`<scope>`: editions, e.g. `01-03`, `02,04`, `latest`, or `all`. Run L1–L4 in any order (each in a new session), L5 last. Every step reads the outputs of the earlier steps in the same review folder if they exist.

## Where results go

`reviews/learning/<YYYY-MM-DD>_<scope>/` — one folder per review. Provenance of every step: `reviews/learning/provenance.jsonl` (`python3 tools/pipeline.py stage-start L1 --arg <scope> --model "<model id>"` … `stage-end L1 --arg <scope>`).

## Rules for every learning step

1. **Versions first.** Read `registry/editions.csv` and the `provenance.md` of each edition in scope. Every finding is reported together with the framework version, methodology version and models that produced the edition. Never pool editions from different framework versions without saying so; if you compare versions, compare like with like (same question types, horizons).
2. **Evidence discipline.** Findings about accuracy need numbers with sample sizes and, for comparisons, cluster bootstrap intervals (`python3 tools/scores.py --bootstrap …`). Below 30 resolved questions: describe, do not conclude. One crisis or one cluster must not drive a general rule (overfitting check).
3. **Hindsight is dated.** When you use facts from after a report's state date, give their date and source, and separate "what was knowable at the state date" from "what became known later". A miss caused by information that did not exist yet is not an analytic error.
4. **Read-only history.** Learning never edits reports, facts, forecasts or the registry of past editions. Corrections to past facts are recorded in the learning output, not in the edition files.
5. **Blindness.** Learning outputs contain benchmark and score information. Stages 03–05 of any edition must not read `reviews/learning/` (CLAUDE.md rule 3.8). Lessons reach forecasting only through approved changes to prompts, configuration or methodology.
6. **Web and corpus.** Use web search and the harvest corpus (`python3 -m tools.harvester search …`). Forecasting services and markets (CLAUDE.md rule 3.9) only as data already stored in `registry/benchmarks.csv`.
7. **No change without approval.** L5 proposes; the user approves; the change is then implemented with a version bump (see `methodology/methodology_changes.md`, "Versioning").
