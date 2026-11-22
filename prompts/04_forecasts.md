# Stage 04 — Forecasts (three independent sessions: A, B, C)

Parameter: `LENS` = A, B or C (from the command argument). Run each lens in a **new session** (after `/clear`) so that no context carries over between lenses.

## Permitted input

- `CLAUDE.md`, the methodology file named in `editions/CURRENT.md` (especially §4 of v1.0 / §5 of v1.1),
- `02_facts/*.md`, `03_analysis.md` of the current edition (including its INFO_CUTOFF line and the post-state-date records LT-01…),
- `registry/questions.csv` (ACTIVE questions),
- your own earlier forecasts only, through `python3 tools/pipeline.py lens-rows <LENS>`. Never open `registry/forecasts.csv` directly. From framework 1.9 a hook (`tools/blindness_guard.py`) blocks any file or command that rule 3.8 forbids for your stage.

## Forbidden

- other lenses' `04_forecasts_*` files, `05_*`, `06_*`, `07_annex_benchmarks.md` of any edition,
- `registry/benchmarks.csv`, AGG and AGG_RT rows in `forecasts.csv`,
- domains from CLAUDE.md item 9 and searches for phrases like "odds", "prediction market", "market-implied probability",
- other lenses' stage 04 entries in `log.md` — append your own entry at the end of the file without displaying its contents,
- facts dated after INFO_CUTOFF (first line of `03_analysis.md`). If a search shows one, do not use it in a forecast or a rationale and do not record it; count it in your log entry as "post-cutoff facts seen: N". This keeps all three lenses on the same information set.

## Lens instructions

**A — "Great-power game".** For every question:
1. who decides the outcome;
2. interests and payoffs of each side;
3. capabilities and constraints;
4. alternatives;
5. which move pays off for whom and what equilibrium follows by the deadline;
6. what would have to change for the equilibrium to shift.

**B — "Outside view".** For every question:
1. name the reference class and base rate (explicitly);
2. account for the persistence of the status quo and the time remaining to the deadline (at a constant rate: p ≈ 1 − (1 − r)^t);
3. only at the end, cautiously, adjust for the specifics of the case.

Avoid narrative; if there is no sensible reference class, say so.

**C — "Domestic and economic constraints".** For every question:
1. domestic politics and electoral calendars;
2. personal incentives of leaders (legitimacy, personal relationships);
3. budgets, markets, logistics;
4. institutional procedures and deadlines (e.g. notification to Congress, budget calendar, council meetings).

Do not mix lenses. If your lens says nothing about a question, note that and give a forecast with analytic confidence "low".

## Way of working (framework 1.9, WP-09)

Edition 02 gave each lens about 12 minutes for 88 questions. That is too little to think. Work like this:
1. **Batches.** Take the questions in batches of 10–15, grouped by cluster, so that related questions are judged together and consistently. Save the file after each batch.
2. **Before each probability**, write these short lines into the edition file (not the registry):
   - the two strongest reasons for YES;
   - the two strongest reasons for NO;
   - **"by now we would expect to see …"**: what should already be visible if YES were coming, and whether it is;
   - **the smallest event that resolves YES**: re-read the criterion and name the least dramatic event that would meet it (for example one confirmed strike, one listing, one outlook change). Judge the probability of that event, not of the event the title suggests;
   - **for a numeric or price threshold**: give a central estimate, a typical error for this series over the time left, and the p that this band gives. Take the error from the series' own recent history. For "on any day" questions, use the touch probability implied by recent volatility. Move away from that p only for a mechanism you name;
   - **when a party's statement carries the forecast** (a refusal, a pledge, a declared deployment, a claim about control or damage): say which kind it is: procedural follow-through of a decision already taken, declared own action, negotiating stance, or claim about contested facts. Then say how often statements of that kind hold over a horizon like this one. A stance or a contested-fact claim alone never keeps p near 0 or 1.

   Then give p. Watch for a known error: in editions 01–02 events that happened were forecast too low (mean forecast 0.42 against a YES rate of 0.58). Do not assume the status quo just because it is the default; judge the evidence.
3. **Searches:** up to 2 per question due within 28 days of the state date and 1 per other question, about 120 in all. Spend them on what would change your p most.
4. **Log** per batch: minutes taken and searches used.

## Tasks

1. For **every** active question give:
   - p (0.01–0.99),
   - a 1–2 sentence rationale in the lens's logic,
   - a key indicator,
   - analytic confidence,
   - the change relative to your own previous forecast and its reason.
2. You may fetch missing facts dated on or before INFO_CUTOFF, within the search budget above. Spend the searches first on questions due on or before STATE_DATE + 28 days, then on questions where your lens's confidence is low. Record them in the file in a section "Additional facts" as full records per CLAUDE.md item 2 (date, actor, action, target, vector, region, status, publisher, URL, source rating, perspective, PIR), numbered `<LENS>-01`, `<LENS>-02`… Every record has at least one URL, and every named publisher has its own URL. For a negative check ("no statement found"), give the URL of the place searched (release list, search page) and the date it was checked.
3. **Consistency of rationale and p.** Before saving each batch, re-read every rationale against its p. If all the arguments you give point one way, p must move that way relative to your base rate or previous forecast. If you keep an outlying value, say why in the rationale. The red team found such a contradiction in the same lens in editions 01 and 02.
4. Save `04_forecasts_<LENS>.md` (table) every 10 questions.
5. At the end write your rows to `<DIRECTORY>/04_rows_<LENS>.csv`, with the registry header that `lens-rows` prints and run `<LENS>`. Set `date` to the date of INFO_CUTOFF (YYYY-MM-DD), not the state date and not the run date. Then append them with `python3 tools/pipeline.py append-forecasts <DIRECTORY>/04_rows_<LENS>.csv --run <LENS>`, which validates every row.

**Log:** the stage entry gives the start and end time (dd.mm.yyyy hh:mm), number of forecasts, number of searches, incidents and gaps. No p ranges and no search topics.

Commit: `edition-NN stage-04<LENS>`.

**Completion criterion:** every active question has a forecast from this lens in this edition.

## Lens B2 — "base rates only" (shadow run, framework 1.9, WP-11)

`/g04 B2` runs a fourth, separate session. B2 never enters AGG or AGG_RT. It exists to measure whether an outside view that sees *less* than the other lenses (no facts, no narrative, no earlier forecasts) adds independent information.

- **Input, and nothing else:**
  - `registry/questions.csv` (ACTIVE questions: wording, criterion, deadline, vector, `p_status_quo`, created);
  - `python3 tools/pipeline.py cutoff` (the cutoff date);
  - the base rates file you build with `python3 tools/scores.py --base-rates <DIRECTORY>/04_base_rates.csv`.

  No web, no facts, no analysis, no forecasts. The hook enforces this.
- **For each question:**
  1. Pick its family: vector × horizon band (days from creation to deadline: ≤14, ≤100, >100) × `p_status_quo`. If that row has n < 10, use the next coarser level (band × `p_status_quo`, then `p_status_quo`, then all), and name the level used.
  2. Start from `yes_rate_smoothed`.
  3. If YES needs an event to happen within the remaining window, scale by the time left: p = 1 − (1 − r)^(days left / days of the question's full window).
  4. Stop there. Write one line of reasoning per question.
- **Output:**
  - `<DIRECTORY>/04_forecasts_B2.md` (table);
  - `<DIRECTORY>/04_rows_B2.csv`, appended with `python3 tools/pipeline.py append-forecasts <DIRECTORY>/04_rows_B2.csv --run B2`;
  - `analytic_confidence` = low;
  - commit `edition-NN stage-04B2`.
