# Stage S — Social drafts (X)

Parameter `MODE`: `watch` (default), `release`, `resolved`. Output: `social/drafts/<YYYY-MM-DD>_<MODE>.md`. **Drafts only: never post, log in or publish anything** (CLAUDE.md §6). The user reviews, edits and posts by hand.

Provenance: `python3 tools/pipeline.py stage-start S --arg <MODE> --model "<your model id>"` … `stage-end S --arg <MODE>`. Commit: `social <date> <MODE>`.

## Voice and rules (all modes)

- **The account is the project's lab notebook, not a pundit.** Calm, precise, non-partisan. No insults, no sarcasm, no engagement bait, no emoji walls, no hashtags beyond one topical tag where useful.
- **Fact ≠ assessment ≠ forecast.** A fact has a source link and date. An assessment says so ("Our reading:"). A forecast is quoted only as published: the official value (AGG_RT) from `registry/forecasts.csv` with question ID, edition and deadline — e.g. "Q-0028 · edition 01 · 30% by 31.12.2026".
- **Never state a new probability between editions.** Frozen forecasts are never changed. New evidence is described by its direction ("pushes up / down for the next edition") and weighed formally only in the next edition. This keeps the track record honest.
- **Three perspectives.** For a contested event, link at least two sides (e.g. the actor's own statement and a third-party source). A government statement is a fact about a statement.
- **Every post stands alone:** ≤ 280 characters, link to the source, and where it fits a link to the question on the site (`<site_url>#forecasts`) or the report.
- **Never quote, link or screenshot** outlets in `sources/harvest/no_republish.txt` (Russian state media, sanctioned outlets). If their statement matters, write "according to Russian state agency X" and link an independent report of that statement instead.
- **Not advice.** No buy/sell language, no market calls. Forecasts on prices are framed as research questions.
- **Disclosure:** the account bio (and the first post of a thread) says the project is AI-assisted with human review.

## MODE watch — "Signals" (2–3 times a week)

Find recent news that **cuts against** a current official forecast, i.e. evidence that the less likely outcome has become more likely (or that the likely one is slipping).

1. Read `docs/data/forecasts.json` (or `registry/forecasts.csv`, latest AGG_RT) for open questions, and `social/watch_log.csv` for signals already posted (do not repeat).
2. Search the harvest corpus since the last watch: `python3 -m tools.harvester search <concept|text> --from <last watch date>`, for the concepts and actors of questions with p ≤ 0.35 or ≥ 0.65 first (that is where a contradiction matters most), then web search to verify and reach the primary source and a second perspective.
3. Keep at most 5 signals that are (a) dated after the edition's state date, (b) verified in a primary or two independent sources, (c) clearly relevant to the question's resolution criterion. Discard opinion pieces without new facts.
4. For each signal write: question ID and current official value; the fact (one sentence, source, date); why it cuts against the forecast; what would confirm or refute it next (a dated indicator); direction for the next edition (up / down). Then one post draft (≤ 280 characters), and optionally a 2–3 post thread.
5. Append one row per kept signal to `social/watch_log.csv` (date;question_id;edition;official_p;direction;strength low/medium/high;source_url;summary). This log is used by the learning loop (L1/L4) to check whether signals were right.

## MODE release — new edition thread (after stage 08)

A thread of 6–8 posts: (1) edition number, state date, link to the report and site, one-line method + AI-assisted disclosure; (2–5) the four most decision-relevant official forecasts (one per post: question, value, deadline, the main reason in one line, the key indicator to watch); (6) what changed since the previous edition; (7) track record so far (resolved count, Brier vs status quo, "indicative" below 30) — **including misses**; (8) invitation: challenge a forecast on GitHub, contribute sources, support.

## MODE resolved — scoring posts (after stage 01)

One post per resolved question: question, outcome, what we said (official value, edition, date), Brier for that question, one line on why we were right or wrong. Misses get the same prominence as hits. If the user has not yet approved a flagged resolution, wait.

## Output format

```
# Social drafts — <date> — <MODE>
## 1. <short title>
Question: Q-XXXX · edition NN · official p · deadline
Evidence: <facts with links>
Draft post (N chars):
> …
Alt / thread:
> …
```
