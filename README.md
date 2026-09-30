# Calibrated Balance-of-Power Forecast — starter kit

**Mission:** forecast the moves of the great powers more accurately than simple baselines — and prove it by measurement.

*Calibrated Balance-of-Power Forecast* is an open, auditable process for forecasting great-power moves (USA, EU, Russia, China, Iran, Ukraine) with an AI agent (Claude Code) and **measuring** whether it beats simple baselines. Each two-weekly edition runs 9 stages: fact collection with three-perspective sourcing (Western / actor / third party), analysis, three blind forecasting "lenses", a red team, aggregation, freezing forecasts in an append-only CSV registry, benchmarking, and a report. Accuracy is scored with the Brier score, Brier skill score, calibration and bootstrap intervals (`tools/scores.py`, Python standard library only). The git history of the registry is the evidence that forecasts were not edited after the fact. Nothing here is investment advice.

The kit is a set of files for Claude Code plus three small tools (Python standard library only):

- a **local harvester** that collects news feeds, official pages, public Telegram channels, GDELT article lists and primary datasets continuously, across about 18 languages, resumably and observably;
- a **pipeline tool** that tells you the next step and records the **provenance** of every stage (framework version, methodology version, commit, prompt, model);
- the **scoring script**.

Everything else is instructions in Markdown and a registry in CSV.

> **Language note.** The project was run in Polish until 28.09.2026 and then translated into English in full (files, prompts, registry, editions 00–01). The method and all numbers are unchanged; the Polish originals remain at git tag `wydanie-01`. Details and the code mapping: `methodology/methodology_changes.md`.

## Quick start (local machine)

```bash
git clone https://github.com/pstepien-labs/worldstate-forecast.git && cd worldstate-forecast
python3 -m tools.harvester selftest      # 20/20 checks
claude                                   # then type: /gH start   (starts continuous harvesting)
                                         # any time:  /next       (where am I, what to run next)
```

**The full step-by-step procedure is in [RUNBOOK.md](RUNBOOK.md).** It covers setup, harvesting and recovery, the 14 edition steps, and the learning loop.

## Requirements

- Claude Code (CLI) with web search and fetch; macOS or Linux (Windows: WSL2).
- `git` and `python3` 3.9+ (no extra libraries).
- Optional: free API keys for primary data (`.env.example`); `pandoc` for a PDF of the report.

## Contents

| Path | What it is |
|---|---|
| `RUNBOOK.md` | Step-by-step guide: setup, harvest, edition, learning loop, troubleshooting |
| `CLAUDE.md` | Standing rules; Claude Code loads them automatically in every session in this directory |
| `VERSION` | Framework version (semantic versioning; scheme in `methodology/methodology_changes.md`) |
| `methodology/methodology_v1.0.md` | The method, frozen until the quarterly review |
| `prompts/00–08, H, M, Q` | Stage instructions: edition stages, harvest, mini-retrospective, quarterly review |
| `prompts/learning/L1–L5` | Learning loop: hindsight audit, performance by version, reasoning trace, sources, framework proposals |
| `.claude/commands/` | Shortcuts `/g00` … `/g08`, `/gH`, `/gL1` … `/gL5`, `/gM`, `/gQ`, `/next` |
| `registry/*.csv` | Questions, forecasts, benchmarks, resolutions, sources, **editions** (append-only) |
| `sources/source_map.md`, `sources/harvest/` | Sources by actor and perspective; harvester configuration (feeds, datasets, keywords, source universe) |
| `tools/harvester/` | Local harvester (`python3 -m tools.harvester --help`) |
| `tools/pipeline.py` | Next step, provenance, edition register |
| `tools/scores.py` | Brier, BSS, calibration, directional bias, bootstrap; filters by edition and framework version |
| `scripts/harvest.sh` | Start / stop / status / tail of the background harvester |
| `editions/` | Edition 00 (starting point) and edition 01 (first full edition) |

## How one edition runs

Harvest continuously between editions. Then run the stages 00–08 in Claude Code, one stage per session (`/clear` between stages). Stages pass results through files. Stage 00 builds the harvest digest, stage 02 verifies its leads and fills the flagged gaps with web search, and stages 03–06 reason and forecast blind. Stage 07 writes the report with a provenance line, and stage 08 checks everything and registers the edition. Details, times and recovery: [RUNBOOK.md](RUNBOOK.md).

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

1. Keep the harvester running between editions (`scripts/harvest.sh status`).
2. Approve resolutions flagged VERIFY (a new row with a higher `version` in `registry/resolutions.csv`).
3. Accept or reject proposals from the learning loop (`/gL5`), the mini-retrospective and the quarterly review.
4. Once per edition, read `08_quality_control.md`: blindness violations, edits to the registry history, coverage and provenance gaps.

## Three rules that must not be broken

1. **Append-only registry.** The forecast history is the evidence; git confirms it.
2. **Forecast blindness.** The lenses and the red team see neither the benchmarks nor each other.
3. **Method frozen for a quarter.** Otherwise it is impossible to tell what helped.

## Disclaimer

The forecasts are probabilistic and for research purposes. This is not investment, financial or political advice. Facts come from the public sources given in the records; their content belongs to the publishers.

## Contributing

Issues and change proposals are welcome — details in [CONTRIBUTING.md](CONTRIBUTING.md). Two things are not negotiable: we do not edit existing registry rows and we do not change methodology v1.0 outside the quarterly review.

## License

- Code (`tools/`, `scripts/`): [MIT](LICENSE).
- Methodology, prompts, registry, editions and other content: [CC BY 4.0](LICENSE-CONTENT.md).
