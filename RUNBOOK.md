# Runbook — from a copy of the repository to the final report

You type only a handful of commands. Everything else runs by itself, and anything long can be interrupted and resumed with the same command.

| You type | When | What happens |
|---|---|---|
| `/gH start` | once, right after setup | The harvester starts collecting news and data in the background and keeps running for days |
| `/edition` | every two weeks, on or after the date `/next` shows | The whole edition runs, about 15 stages and 10–20 hours unattended, and ends with the report |
| `/next` | whenever you are unsure | Tells you what is running, what is finished, and what to type next |
| `/learn` | optional, between editions | Reviews past editions and proposes improvements for you to approve |

---

## 1. One-time setup (about 20 minutes)

### 1.1 Requirements

- macOS or Linux (on Windows use WSL2).
- `git`.
- Python 3.9 or newer (`python3 --version`).
- Claude Code: `curl -fsSL https://claude.ai/install.sh | bash`, then run `claude` once to log in.
- About 5 GB of free disk.

### 1.2 Get the repository

The repository is private, so log in to GitHub first (once):

```bash
brew install gh          # macOS; Linux: see https://cli.github.com
gh auth login            # GitHub.com → HTTPS → yes, authenticate Git → login with browser
gh repo clone pstepien-labs/worldstate-forecast
cd worldstate-forecast
git fetch --tags
```

Every command below is run inside the `worldstate-forecast` folder.

**Already have a copy?** Update it with `git pull --no-rebase` instead of cloning again. `--no-rebase` keeps your local commits (for example a source repair) and merges the update into them.

### 1.3 Optional free API keys

```bash
cp .env.example .env     # then edit .env
```

| Key | Adds |
|---|---|
| `HARVEST_CONTACT` | Your e-mail in the harvester's identification. Some sites that refuse anonymous bots then allow it |
| `AGSI_API_KEY` | EU, Polish and German gas storage |
| `EIA_API_KEY` | Brent price and US crude stocks |
| `FIRMS_MAP_KEY` | NASA satellite fire detections near refineries and ports |

You can skip all of them. Sources that need a missing key are skipped, not failed. Keys added later are picked up without a restart.

### 1.4 Check the installation

```bash
python3 -m tools.harvester selftest     # expect: 21/21 checks passed
```

---

## 2. Start harvesting (once)

```bash
claude
```

Then type:

```
/gH start
```

This takes 15–30 minutes the first time:
- it fetches every source once;
- if more than 20% fail, it repairs the source list (fixes addresses, disables sites that block bots, adds replacements) and commits the changes;
- it starts the harvester in the background.

The harvester keeps running after you close Claude Code.

What is normal:
- "Throttled" sources, mostly GDELT: the server asked us to slow down, and they are retried automatically later.
- A few disabled sources: sites that block automated access are never worked around.

To check on it at any time (no Claude needed):

```bash
scripts/harvest.sh status    # running? sources OK? recent errors
scripts/harvest.sh tail      # live log (Ctrl+C leaves the view; harvesting continues)
```

If the computer slept, restarted, or `status` says NOT RUNNING:

```bash
scripts/harvest.sh start     # resumes where it stopped; nothing is lost or duplicated
```

The computer has to be on and online for the harvester to collect.

---

## 3. Produce an edition (every two weeks)

Editions are **two weeks apart**, counted from the previous edition's **state date**: the day the report describes the world "as of". The rule exists so that the questions that come due in between can be resolved and scored in the next edition. Edition 01's state date is 23.09.2026, so **edition 02 can start on or after 07.10.2026**. `/next` always shows the exact date.

On that day:

```bash
claude
```

```
/edition
```

That is all. `/edition` then works through these steps:

1. It asks you one question: whether to pause for your approval of uncertain question resolutions, or continue and let you review them later.
2. It runs every stage in order, each as a separate sub-agent with a clean context: plan and harvest digest → resolutions and scores → facts in four topic groups → analysis → three independent forecasts → red team → aggregation and freezing → report → quality control.
3. It prints one progress line per stage. Each stage commits its own results to git.
4. It finishes with the location of the report and a short summary.

Practical notes:

- **Duration:** 10–20 hours of agent work. You can leave it running overnight.
- **Permissions:** Claude Code may ask you to approve some actions the first time. Choose "Yes, and don't ask again" for web search, web fetch and the project's own commands. File edits inside the project are pre-approved in `.claude/settings.json`.
- **Interrupted?** Closed window, lost connection, budget limit, Esc: just type `/edition` again. It continues from the first unfinished stage, and an interrupted stage continues from its gaps.
- **Result:** `editions/<date>_edition-NN/07_report.md`. The line under its title shows which framework version, methodology, models and harvest coverage produced it. The full stage-by-stage record is in `provenance.md` in the same folder.
- **Publishing (optional):** `git push` sends your commits to GitHub.

### Why so many stages

A single prompt cannot do this well:
- **Collecting** about 200 facts with three perspectives each needs more context than one session has.
- The three **forecasts** must not see each other, or they stop being independent.
- The **red team** must not see the benchmarks.

So `/edition` runs each stage in its own clean context and passes results only through files. You still type one command.

### Manual mode (optional)

You can run single stages yourself: `/g00 <date> <NN>`, `/g01`, `/g02 G1`…`G4`, `/g03`, `/g04 A`/`B`/`C`, `/g05`, `/g06`, `/g07`, `/g08`. Use one stage per session and type `/clear` between them. `/next` shows which stage is next. This is useful for re-running one stage or for debugging; normally `/edition` is simpler.

---

## 4. Learning loop (optional, between editions)

```
/learn latest        (or: /learn 01-03, /learn all)
```

It runs four reviews and then works with you on proposals:

| Review | What it checks |
|---|---|
| Hindsight audit | Facts that did not hold, and surprises the report missed |
| Accuracy | Results by lens, framework version and model |
| Reasoning trace | The biggest misses and hits |
| Sources | Coverage gaps and how reliable each source proved |

It then presents at most 5 improvement proposals and asks you to approve, reject or postpone each one. Approved process changes are applied with a new framework version. Changes to the method itself wait for the quarterly review (`/gQ`, around 21.12.2026).

Run it when questions have resolved: after edition 03 at the earliest, ideally with 30 or more resolved questions.

---

## 5. Troubleshooting

| Symptom | Fix |
|---|---|
| `git clone` / `git pull`: "Password authentication is not supported" | Log in with `gh auth login` (step 1.2) |
| `/next` says the next edition can start on a later date | Keep the harvester running; type `/edition` on that date |
| Harvester NOT RUNNING | `scripts/harvest.sh start` |
| Many sources failing | In Claude: `/gH repair` |
| Many sources "throttled" | Normal for GDELT; they retry automatically after the pause |
| `/edition` stopped with a question or blocker | Answer it, then `/edition` again |
| Disk filling up | Stop the harvester, move `data/harvest`, set `HARVEST_DATA=<new path>` in `.env`, start it again |

## Where things are

| Path | Content | In git? |
|---|---|---|
| `editions/<date>_edition-NN/07_report.md` | The report | yes |
| `editions/<date>_edition-NN/provenance.md` | Versions, commits and models behind each stage | yes |
| `registry/editions.csv` | One row per edition: versions, models, tag | yes |
| `data/harvest/` | Harvested corpus, logs, status | no (stays on your machine) |
| `reviews/learning/` | Learning reviews and proposals | yes |
| `.env` | Your API keys | **never** |
