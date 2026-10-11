# Stage 04 — Forecasts (three independent sessions: A, B, C)

Parameter: `LENS` = A, B or C (from the command argument). Run each lens in a **new session** (after `/clear`) so that no context carries over between lenses.

## Permitted input

- `CLAUDE.md`, `methodology/methodology_v1.0.md` (especially §4),
- `02_facts/*.md`, `03_analysis.md` of the current edition (including its INFO_CUTOFF line and the post-state-date records LT-01…),
- `registry/questions.csv` (ACTIVE questions),
- `registry/forecasts.csv` — **only rows whose run equals your lens** (for continuity of your own forecasts).

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

## Tasks

1. For **every** active question give:
   - p (0.01–0.99),
   - a 1–2 sentence rationale in the lens's logic,
   - a key indicator,
   - analytic confidence,
   - the change relative to your own previous forecast and its reason.
2. You may fetch missing facts dated on or before INFO_CUTOFF (at most 20 searches). Spend them first on questions due on or before STATE_DATE + 28 days, then on questions where your lens's confidence is low. Record them in the file in a section "Additional facts" as full records per CLAUDE.md item 2 (date, actor, action, target, vector, region, status, publisher, URL, source rating, perspective, PIR), numbered `<LENS>-01`, `<LENS>-02`… Every record has at least one URL, and every named publisher has its own URL. For a negative check ("no statement found"), give the URL of the place searched (release list, search page) and the date it was checked.
3. **Consistency of rationale and p.** Before saving each batch, re-read every rationale against its p. If all the arguments you give point one way, p must move that way relative to your base rate or previous forecast. If you keep an outlying value, say why in the rationale. The red team found such a contradiction in the same lens in editions 01 and 02.
4. Save `04_forecasts_<LENS>.md` (table) every 10 questions.
5. At the end append rows to `registry/forecasts.csv` with run `<LENS>`. Set `date` to the date of INFO_CUTOFF (YYYY-MM-DD), not the state date and not the run date.

**Log:** the stage entry gives the start and end time (dd.mm.yyyy hh:mm), number of forecasts, number of searches, incidents and gaps. No p ranges and no search topics.

Commit: `edition-NN stage-04<LENS>`.

**Completion criterion:** every active question has a forecast from this lens in this edition.
