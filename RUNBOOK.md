# Runbook — running the forecast on your own machine

This is the complete, step-by-step procedure. It has three parts:

- **Harvest:** continuous, runs in the background for days.
- **Edition:** the 9 reasoning stages, run in Claude Code, which produce the report.
- **Learning:** looks back at finished editions and improves the framework.

At any moment, `/next` inside Claude Code (or `python3 tools/pipeline.py status` in a terminal) tells you where you are and the exact next command.

---

## Part 0 — One-time setup (about 20 minutes)

### 0.1 What you need

| Item | Check with | Notes |
|---|---|---|
| macOS or Linux (Windows: use WSL2 Ubuntu) | — | The background harvester script is for macOS/Linux shells |
| `git` | `git --version` | |
| Python 3.9 or newer | `python3 --version` | No extra packages: standard library only |
| Claude Code (CLI) | `claude --version` | Install: `curl -fsSL https://claude.ai/install.sh \| bash` or `npm install -g @anthropic-ai/claude-code` (Node 18+). Log in on first start. |
| About 5 GB free disk | — | The corpus grows ~20–100 MB per day |

### 0.2 Download the repository

```bash
git clone https://github.com/pstepien-labs/worldstate-forecast.git
cd worldstate-forecast
git fetch --tags
git checkout claude/sharp-babbage-nmv7od    # only until this branch is merged into main; afterwards stay on main
```

If the repository is private, authenticate first: `gh auth login`, or clone with SSH (`git@github.com:pstepien-labs/worldstate-forecast.git`).

**From now on, every command in this runbook is run inside the `worldstate-forecast` directory.**

### 0.3 Optional API keys (free; they add primary data)

```bash
cp .env.example .env
```

Open `.env` in an editor and fill in what you have:

| Key | Unlocks | Where to get it |
|---|---|---|
| `HARVEST_CONTACT` | Your e-mail in the harvester's User-Agent, so site operators can reach you instead of blocking you | — |
| `AGSI_API_KEY` | EU, Polish and German gas storage | agsi.gie.eu (free account) |
| `EIA_API_KEY` | Brent spot and US crude stocks | eia.gov/opendata |
| `FIRMS_MAP_KEY` | NASA satellite fire detections near refineries and ports (independent check of strike claims) | firms.modaps.eosdis.nasa.gov/api |

Without keys everything still works: those sources are skipped, not failed. You can add a key later without restarting anything.

### 0.4 Verify the installation

```bash
python3 -m tools.harvester selftest     # expect: 20/20 checks passed (offline, uses a temporary folder)
python3 -m tools.harvester doctor       # Python, disk, sources, languages, keys
```

### 0.5 Open Claude Code in the project

```bash
claude
```

- Accept "trust this folder" the first time.
- Choose the model with `/model` (the strongest available is recommended for stages 03–05). Each stage records the model you used.
- `.claude/settings.json` pre-approves the project's own commands, `git` commit/status and web search/fetch. You will still be asked before anything else runs.

---

## Part 1 — Harvest (start now; it runs continuously)

### 1.1 Start

In Claude Code type:

```
/gH start
```

Claude runs `doctor`, then the first `check`: every source is fetched once, which takes about 10–20 minutes, and the result goes to `data/harvest/CHECK.md`. It then starts the background harvester and confirms it is running.

The same without Claude, in a terminal:

```bash
python3 -m tools.harvester check
scripts/harvest.sh start
```

If more than 20% of sources fail on the first check, run `/gH repair`. Claude looks up the current feed addresses, fixes `sources/harvest/feeds.csv`, verifies the fixes and commits them.

### 1.2 Watch it (observability)

| What | Command / file |
|---|---|
| Progress, source health, recent errors, liveness | `scripts/harvest.sh status` (also `data/harvest/STATUS.md`) |
| Live event stream | `scripts/harvest.sh tail` (Ctrl+C leaves the view; harvesting continues) |
| Structured log (one JSON line per event) | `data/harvest/logs/events-YYYY-MM-DD.jsonl` |
| Per-source state (schedule, failures, last success) | `data/harvest/state/sources.json` |
| Result of the last full check | `data/harvest/CHECK.md` |
| Inside Claude Code | `/gH status` or `/next` |

A healthy run shows `LIVENESS: running` and a heartbeat less than 15 minutes old. Each source is fetched on its own schedule: news feeds every 4–6 h, GDELT queries every 12 h, datasets every 12–24 h. Failing sources back off, up to one attempt per 24 h.

### 1.3 If it breaks: resume

The harvester saves its state after every source. Whatever happened, run:

```bash
scripts/harvest.sh start
```

It continues where it stopped. It only fetches sources that are due and never stores an item twice.

| Situation | What to do |
|---|---|
| Computer slept or restarted | `scripts/harvest.sh start` |
| Terminal or Claude Code closed | Nothing: the harvester runs independently (check with `scripts/harvest.sh status`) |
| `LIVENESS: not running` | `scripts/harvest.sh start` |
| Process exists but heartbeat older than 30 min | `scripts/harvest.sh stop`, then `scripts/harvest.sh start` |
| "Another harvester is running" | It is already running; use `status` |
| Many failing sources | `/gH repair` |
| Disk getting full | Stop, move `data/harvest` elsewhere, set `HARVEST_DATA=<new path>` in `.env`, start |
| Planned stop | `scripts/harvest.sh stop` (finishes the current source cleanly) |

On a laptop the start script keeps the machine awake while it harvests: `caffeinate` on macOS, `systemd-inhibit` on Linux where available. Closing the lid may still suspend it; the harvester resumes on the next `start`.

### 1.4 How long to harvest

Harvest continuously from the day after one edition's state date up to the next state date, which is typically 14 days. GDELT and the numeric datasets back-fill up to 14 days (`HARVEST_BACKFILL_DAYS`); news feeds keep only their recent items. So a late start loses part of the feed coverage. The digest records the window actually covered.

**Now:** edition 01 has state date 23.09.2026. Edition 02 can run with a state date on or after 07.10.2026. Start harvesting today and let it run until then.

---

## Part 2 — One edition (the reasoning stages)

Rules:
- **One stage per session.** Before each stage type `/clear`, or quit and start `claude` again. Stages pass results through files, not through the conversation.
- Each stage records its provenance itself (framework version, commit, prompt hash, model) and commits its outputs.
- If a stage is interrupted (budget, error, closed window), run **the same command again**: it continues from the gaps and never restarts from scratch.
- The harvester keeps running during the whole edition.

| # | Command (in Claude Code) | What happens | Time |
|---|---|---|---|
| 1 | `/g00 2026-10-07 02` | Starts the edition: plan, calendar, **harvest digest** (stage H), versions | 30–45 min |
| 2 | `/g01` | Resolves questions whose deadline passed; computes scores | 0–60 min |
| — | **You** | Review "FOR USER VERIFICATION" in `01_resolutions.md` | 10–20 min |
| 3–6 | `/g02 G1`, `/g02 G2`, `/g02 G3`, `/g02 G4` | Facts: verify digest leads, primary data, close flagged gaps (separate sessions) | 1–3 h each |
| 7 | `/g03` | Analysis and question bank | 1–2 h |
| 8–10 | `/g04 A`, `/g04 B`, `/g04 C` | Three blind forecasting lenses (**separate sessions**) | ~1 h each |
| 11 | `/g05` | Red team | ~1 h |
| 12 | `/g06` | Aggregation, **freezing** of forecasts, then benchmarks | ~1 h |
| 13 | `/g07` | Report (with provenance line) | 1–2 h |
| 14 | `/g08` | Quality control, tag `edition-02`, entry in `registry/editions.csv` | 30–60 min |

The final report is `editions/<date>_edition-NN/07_report.md`. Its first line after the title states the framework version, methodology version, commit, models and harvest coverage that produced it. The full stage-by-stage record is in `provenance.md` in the same folder.

If a slash command is not recognised, type the equivalent instruction, for example: *"Read CLAUDE.md, editions/CURRENT.md and prompts/02_collection.md and carry out stage 02 for group G1."*

**Publishing your results (optional):** `git push` sends your commits to GitHub. The git history is the evidence that forecasts were not edited after freezing, so never rewrite it.

---

## Part 3 — Learning loop (between editions)

When editions have closed, and especially once questions have resolved, run the learning steps. Each runs in its own session. `<scope>` is a set of editions such as `01-03`, `latest` or `all`.

| # | Command | Output (in `reviews/learning/<date>_<scope>/`) |
|---|---|---|
| 1 | `/gL1 <scope>` | Hindsight audit: facts that did not hold, surprises, and whether they were foreseeable in the harvested corpus |
| 2 | `/gL2 <scope>` | Accuracy by run, lens, vector, horizon, cluster, **framework version** and **model**, with bootstrap intervals |
| 3 | `/gL3 <scope>` | Reasoning trace of the biggest misses and hits: at which pipeline step the signal was lost or found |
| 4 | `/gL4 <scope>` | Source track record and coverage gaps; concrete source configuration changes |
| 5 | `/gL5 <scope>` | At most 5 proposals, each with level (patch/minor/major), expected effect and how it will be measured. You approve or reject each one; approved patch/minor changes are implemented with a `VERSION` bump. Major changes wait for the quarterly review (`/gQ`) |

Every edition records its framework version, methodology version and models (`registry/editions.csv`, `provenance.md`). This lets the learning steps tell whether a change helped: compare results before and after a version and check the bootstrap interval. Do not implement framework changes while an edition is between stages 03 and 06.

Recommended rhythm:
- Run L1 and L4 after every second edition.
- Run L2–L5 once at least 30 questions have resolved.
- Run the quarterly review `/gQ` around 21.12.2026.

---

## Where things are

| Path | Content | Committed to git? |
|---|---|---|
| `data/harvest/` | Full local corpus, logs, state | No (your machine only) |
| `editions/<edition>/02_harvest/` | Digest, coverage, indicators, source health, manifest | Yes |
| `editions/<edition>/provenance.md` | Who/what produced each stage | Yes |
| `registry/editions.csv` | One row per edition: versions, models, commits, tag | Yes |
| `sources/harvest/` | Harvester configuration and its changelog | Yes |
| `reviews/learning/` | Learning outputs, `proposals.csv` | Yes |
| `.env` | Your API keys | **Never** |
