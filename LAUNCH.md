# Launch plan — public site, contributions, support, X

## 1. Positioning

**Worldstate Forecast is an open research experiment.** An AI-assisted, fully documented process forecasts the moves of the great powers every two weeks. Each forecast is frozen in public before the outcome and scored afterwards.

It is niche on purpose. It is not a news site, a think tank or a trading signal. Its credibility comes from four things that are rare in geopolitical commentary:

1. **Pre-registration.** Every forecast is a probability with a dated resolution criterion, in an append-only registry whose git history proves nothing was edited.
2. **Measurement.** Brier scores against a "nothing changes" baseline and forecasting crowds, with misses published as prominently as hits.
3. **Three perspectives.** Western sources, the actor's own side and a third party, across about 200 sources in 18 languages.
4. **Openness and versioning.** Method, prompts, code and data are public, and every report names the framework version and AI models behind it.

Tone everywhere: calm, precise, non-partisan, honest about limits ("one person with AI assistance").

## 2. What to offer — and what not

The natural model for a research project like this is **open core plus support plus services later**. Selling the forecasts would destroy the main asset: a public, checkable track record.

| Tier | What | Status | Why it fits |
|---|---|---|---|
| Free, always | Reports, forecast registry (CSV/JSON), methodology, prompts, code | **now** | The track record only counts if anyone can check it |
| Free | "For AI assistants": `llms.txt` and `forecasts.json` that let anyone point their own AI at the data | **now** | Gives an "LLM query" option at zero cost and zero legal risk |
| Support | Donations: GitHub Sponsors, Ko-fi, later Open Collective | **at launch** | Normal for open research; keeps it independent |
| Services | Custom questions on a client's topic, a structured data feed, briefings | **later**: after ≥ 30 resolved questions with a positive skill score | Clients pay for convenience and custom work, not for exclusivity |
| Hosted "ask the forecasts" chat | A web chat answering questions from the reports and registry | **optional, later** | Possible, but it costs per query; start with `llms.txt` |

**Do not sell or redistribute the harvested news corpus.**
- The headlines and summaries belong to their publishers. In the EU, press publishers also have their own right over online use of their content (DSM Directive, Article 15).
- Many sources' terms forbid reuse, and GDELT requires attribution.
- Publish only what the project produces itself: forecasts, resolutions, fact records written in its own words with links, source ratings and coverage statistics.

**Benchmarks.** Crowd and market values (Metaculus, Polymarket and others) are kept out of the site and the data pack. Their terms limit reuse, especially commercial reuse.

**Legal and tax** (not legal advice; check with an accountant or lawyer before taking money):
- Donations and sales are income: check how they are taxed and whether you need to register a business in Poland.
- Never give buy/sell calls. Price questions (Brent, EUR/PLN) are research, and paid market recommendations can fall under investment-advice rules.
- Keep the "Research, not advice" disclaimer on the site and the X profile.

### Legal notice and requests

The site has a legal notice page (`docs/legal.html`, linked in the footer). It covers: research not advice, AI-assisted content, copyright and data mining, publisher opt-out and takedown, state and sanctioned media, licences, privacy and corrections. Fill `operator_name` and `contact_email` in `site/config.json` so it names who is responsible and how to reach you.

If a publisher asks to opt out:
1. Add the domain to `sources/harvest/optout_domains.txt`, with the date of the request.
2. Run `python3 -m tools.harvester purge-domain <domain>`.
3. Commit and push, and reply to the publisher.

The notice promises this within 7 days.

## 3. Launch checklist (you)

### A. Before making the repository public (30 min)

1. **Commit e-mail.** Your personal e-mail is in 22 commits. That cannot be removed without rewriting history, which the project forbids. If you mind, use GitHub's private noreply address for future commits: GitHub → Settings → Emails → "Keep my email address private", then `git config user.email <id>+<user>@users.noreply.github.com`.
2. **Secrets.** `.env` was never committed; I checked the full history.
3. **Third-party text in edition files.** These hold short quotes and headline snippets with links. That is normal for research, but keep the snippets short (as now).

### B. Make it public and switch on the site (10 min)

1. On GitHub, open the repository → **Settings → General → Danger Zone → Change visibility → Public**.
2. **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, folder `/docs` → Save.** About a minute later the site is live at https://pstepien-labs.github.io/worldstate-forecast/.
3. **Repository "About"** (gear icon on the main page):
   - description: "Calibrated balance-of-power forecasts. Frozen before the outcome. Scored after.";
   - website: the Pages URL;
   - topics: `forecasting`, `geopolitics`, `open-data`, `osint`, `ai`.
4. **Settings → Features:** turn on **Issues** and, if you want, **Discussions**. The "Challenge a forecast" and "Propose a source" issue templates are already in the repository.

### C. Support links (30 min)

1. **Ko-fi:** create a page today; it is instant.
2. **GitHub Sponsors:** apply (GitHub reviews applications; it can take days).
3. **Open Collective:** later, if others join and you want transparent shared accounting.
4. Put the links, your contact e-mail (a project address is better than a personal one) and the X handle in `site/config.json`.
5. Run `python3 tools/site.py`, then `git add -A && git commit -m "site config"` and `git push`. Empty fields stay hidden.

### D. X account (1 hour)

| Item | Suggestion |
|---|---|
| Handle | Short and close to the name, e.g. `@worldstatefc` (check availability) |
| Name | Worldstate Forecast |
| Bio | "Open forecasting experiment on great-power moves. Probabilities frozen before the outcome, scored after. AI-assisted, human-reviewed. Not advice." + site link |
| Pinned post | What the project is, one frozen forecast as an example, the site link, how to challenge a forecast |
| Header image | A screenshot of the site's "frozen forecast" card |

## 4. X playbook

Claude drafts every post (`/social …`). You review, edit and post by hand. Never post anything you have not read.

| Rhythm | Command | Content |
|---|---|---|
| Every edition (2 weeks) | `/edition` drafts it automatically, or `/social release` | Thread: what's new, 4 key forecasts with deadlines and the indicator to watch, track record including misses, invitation to challenge |
| After resolutions | `/social resolved` | "We said 30%, it happened / didn't — Brier 0.49 — here's why we were wrong/right" |
| 2–3× a week | `/social watch` | "Signal": a verified fact that cuts against a frozen forecast, with sources from more than one side and the direction it pushes the next edition |
| Ad hoc | — | Replies to analysts and journalists with evidence and a link to the relevant question; no fights |

Rules:
- **Never post a new probability between editions.** Say "this pushes our next estimate up" and let the next edition decide. This keeps the public record clean and makes the account more credible than ordinary commentary.
- Every signal is logged in `social/watch_log.csv`. The learning loop later checks whether your signals were right, which is a track record of its own.

Growth comes slowly and from credibility:
- **Post misses openly.** Publishing them builds more trust than anything else.
- **Reply with sources.** Answer people in this space with a source and a question ID rather than an opinion.
- **Match posts to the calendar.** Post before scheduled events (central-bank meetings, summits, elections) where you hold a question.
- **Credit outside help.** Credit contributors whose evidence or sources made it into a report.

## 5. First 90 days

| When | Milestone |
|---|---|
| Week 0 | Repository public, Pages live, Ko-fi, X account with pinned post |
| 07.10.2026 | Edition 02: first resolved questions. Post the scoring openly, hits and misses |
| Every 2 weeks | Edition, release thread, site refresh (automatic in `/edition`, published with `git push`) |
| ~02.11.2026 | Edition 03 before the US midterms. The most "newsworthy" moment to invite challenges |
| After edition 03 | `/learn` and `/gM`: publish the process lessons as a short post or thread |
| ~21.12.2026 | Quarterly review `/gQ`. Publish the full post-mortem; decide whether the record justifies offering services |
