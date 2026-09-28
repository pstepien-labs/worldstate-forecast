# Calibrated Balance-of-Power Forecast — starter kit

**Mission:** forecast the moves of the great powers more accurately than simple baselines — and prove it by measurement.

*Calibrated Balance-of-Power Forecast* is an open, auditable process for forecasting great-power moves (USA, EU, Russia, China, Iran, Ukraine) with an AI agent (Claude Code) and **measuring** whether it beats simple baselines. Each two-weekly edition runs 9 stages: fact collection with three-perspective sourcing (Western / actor / third party), analysis, three blind forecasting "lenses", a red team, aggregation, freezing forecasts in an append-only CSV registry, benchmarking, and a report. Accuracy is scored with the Brier score, Brier skill score, calibration and bootstrap intervals (`tools/scores.py`, Python standard library only). The git history of the registry is the evidence that forecasts were not edited after the fact. Nothing here is investment advice.

The kit is a set of files for Claude Code (with web access). It is not software: the only script (`tools/scores.py`) computes accuracy scores. Everything else is instructions in Markdown and a registry in CSV.

> **Language note.** The project was run in Polish until 28.09.2026 and then translated into English in full (files, prompts, registry, editions 00–01). The method and all numbers are unchanged; the Polish originals remain at git tag `wydanie-01`. Details and the code mapping: `methodology/methodology_changes.md`.

## Requirements

- Claude Code with web search and fetch.
- `git` and `python3` (no extra libraries).
- Optionally `pandoc` — to generate a PDF of the report.

## Contents

| Path | What it is |
|---|---|
| `CLAUDE.md` | Standing rules; Claude Code loads them automatically in every session in this directory |
| `methodology/methodology_v1.0.md` | The method, frozen until the quarterly review |
| `prompts/00–08, M, Q` | Instructions for the stages, the mini-retrospective and the quarterly review |
| `.claude/commands/` | Shortcuts `/g00` … `/g08`, `/gM`, `/gQ` that start the stages |
| `registry/*.csv` | Questions, forecasts, benchmarks, resolutions, sources (append-only) |
| `registry/question_proposals_edition_00.csv` | 28 proposed panel questions, verified in edition 01 |
| `sources/source_map.md` | Sources by actor and perspective |
| `editions/2026-09-21_edition-00/` | Starting point: report and state block |
| `editions/2026-09-23_edition-01/` | First full edition |
| `tools/scores.py` | Brier, BSS, calibration, directional bias, bootstrap |

## How to run one edition

In a terminal, in the kit directory: `claude`, then `/model` to choose the model. Run each stage in a **new session** (`/clear` between stages). Stages pass results to each other through files.

| Step | Command | Indicative time | Notes |
|---|---|---|---|
| 1 | `/g00 2026-10-07 02` | 15–30 min | state date and edition number |
| 2 | `/g01` | 0–60 min | resolutions and scores |
| — | **You** | 10–20 min | review the "FOR USER VERIFICATION" section in `01_resolutions.md` |
| 3–6 | `/g02 G1`, `/g02 G2`, `/g02 G3`, `/g02 G4` | 1–3 h each | the heaviest stage; re-run an interrupted group with the same command |
| 7 | `/g03` | 1–2 h | analysis and question bank |
| 8–10 | `/g04 A`, `/g04 B`, `/g04 C` | ~1 h each | three separate sessions, always after `/clear` |
| 11 | `/g05` | ~1 h | red team |
| 12 | `/g06` | ~1 h | freeze forecasts, then benchmarks |
| 13 | `/g07` | 1–2 h | report |
| 14 | `/g08` | 30–60 min | quality control, git tag |

In total about 12–20 hours of agent work per edition; edition 01 took about 24 hours of wall-clock time. If the shortcuts do not work in your version of Claude Code, type manually: "Read CLAUDE.md, editions/CURRENT.md and prompts/0X_….md, carry out the stage. Parameters: …".

Permissions: Claude Code will ask for permission for search, page fetches, `git` and `python3`. You can allow them permanently for this project via `/permissions`. Do not switch off permission prompts globally.

## Schedule

**Edition 01 — state 23.09.2026: "Start-up with measurement"** (done).
- Full collection in four vector groups.
- Standing panel of 40 questions from the edition 00 proposals plus 33 open questions.
- About 40% of questions with a deadline around 06–07.10, so that edition 02 has its first resolutions.
- First blind forecasts of the three lenses, red team, freezing, benchmarks, report.

**Edition 02 — state on or after 07.10.2026: "First feedback loop".**
- Run it no earlier than 07.10: 23 questions have deadlines on 06–07.10.
- First resolutions and indicative scores.
- Collection in "changes and verification" mode: facts from 01 confirmed or removed with a reason.
- A larger share of actor-side sources for key events.

**Edition 03 — around 02.11.2026: "Before the cluster of dates".**
- Just before 03.11 (US elections), 10.11 (rare earths) and 18–19.11 (APEC). Many questions will resolve within three weeks — a good test.
- After the edition: `/gM` — mini-retrospective of the **process** (no change of method).

Then editions 04–06 (every two weeks) without changes to the method and the quarterly review `/gQ` around 21.12.2026.

## What you do

1. Approve resolutions flagged VERIFY (a new row with a higher `version` in `registry/resolutions.csv`).
2. Accept or reject proposals from the mini-retrospective and the quarterly review.
3. Once per edition, read `08_quality_control.md`: were there any blindness violations or edits to the registry history.

## Three rules that must not be broken

1. **Append-only registry.** The forecast history is the evidence; git confirms it.
2. **Forecast blindness.** The lenses and the red team see neither the benchmarks nor each other.
3. **Method frozen for a quarter.** Otherwise it is impossible to tell what helped.

## Disclaimer

The forecasts are probabilistic and for research purposes. This is not investment, financial or political advice. Facts come from the public sources given in the records; their content belongs to the publishers.

## Contributing

Issues and change proposals are welcome — details in [CONTRIBUTING.md](CONTRIBUTING.md). Two things are not negotiable: we do not edit existing registry rows and we do not change methodology v1.0 outside the quarterly review.

## License

- Code (`tools/scores.py`): [MIT](LICENSE).
- Methodology, prompts, registry, editions and other content: [CC BY 4.0](LICENSE-CONTENT.md).
