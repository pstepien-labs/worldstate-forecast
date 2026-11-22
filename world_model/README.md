# World model (methodology v1.1 §3)

The layer between collection and questions. Under v1.1 the questions come from this model, and news is evidence for it (`methodology/methodology_v1.1.md`).

| File | Content | Updated by |
|---|---|---|
| `drivers.csv` | the 13 structural drivers D1–D13: definition, example indicators, the question clusters and harvester concepts mapped to each | quarterly review only |
| `ledger.csv` | power ledger: actor × factor, with indicator, latest value, date, source URL, trend, one-line ASSESSMENT, confidence. `NO DATA` = a gap, never filled from memory | stage W, every edition |
| `chains.csv` | move → counter-move chains: driver, actors, linked fact IDs in order, status, last move, expected next move, the actor-model claim behind it, linked questions | stage W, every edition |
| `actor_models.md` | what each power reacts to, its repertoire, lag, red lines, constraints and track record | stage W, every edition |
| `quiet_list.md` | the quarterly quiet-but-important list (outside experts and low-attention / high-importance flags) | quarterly review |

Git history keeps every earlier state: `git log -p world_model/` shows how the model changed and when. Stages 03–05 read these files. The site shows only counts and coverage, never probabilities.
