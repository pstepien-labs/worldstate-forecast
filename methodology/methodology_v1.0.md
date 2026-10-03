# Methodology v1.0

In force from edition 01 until the quarterly review (c. 21.12.2026). Changes only through the quarterly review (a new file `methodology_v1.1.md`; this file stays unchanged).

> Translation note: this is the English translation (28.09.2026) of the frozen Polish original, which remains at git tag `wydanie-01`. The content of the method is unchanged; only language and code names differ (mapping in `methodology_changes.md`).

## 1. Measure of success

- **Primary measure:** the Brier skill score (BSS) of the official AGG_RT forecast relative to:
  a) the mechanical status-quo baseline (`p_status_quo`),
  b) the crowd or market — only on questions with an EXACT benchmark match.
- **Auxiliary measures:** calibration, directional bias, comparison of runs A / B / C / AGG / AGG_RT.

## 2. Priority intelligence requirements (PIR)

- **PIR-1** Russia's capability and will to escalate against NATO and the eastern flank.
- **PIR-2** US/NATO capability and will to respond; US presence in Europe and in Poland.
- **PIR-3** Prices and availability of energy (oil, gas, fuels) in Europe and in Poland.
- **PIR-4** US–China rivalry: trade, technology, raw materials, Taiwan.
- **PIR-5** The war with Iran and sea lanes (Hormuz, Bab el-Mandeb, Suez).
- **PIR-6** Financial condition of the great powers and capital-market conditions, including PLN.
- **PIR-7** Shifts in the orientation of states (elections, alliances, changes of government).

The resolution of collection follows from the PIRs. A region with no link to any PIR gets one line in the report.

## 3. Question bank

**3.1 Types.**
- *Standing panel:* 40 questions, 5 for each of the 8 vectors. Set in edition 01, unchanged until the quarterly review. Exception: a resolved question is replaced by a new one from the same vector and cluster.
- *Open questions:* 20–40 new ones in every edition.

**3.2 Question requirements.** Binary YES/NO; an unambiguous resolution criterion; a named public resolution source; a deadline (date); an event that can still occur after the creation date; no duplicates; an assigned cluster.

**3.3 Horizons of new questions in an edition.** About 40% with a deadline by the date of the next edition (14 days); about 40% by the end of the quarter (31.12.2026); about 20% longer.

**3.4 Cluster.** A label for a group of questions that depend on the same outcome, e.g. HORMUZ, BAB_EL_MANDAB, UA_TALKS, UA_FRONT, EASTERN_FLANK, US_EUROPE, CN_RARE_EARTHS, TAIWAN, EU_ENERGY, OIL_PRICE, RATES, US_ELECTIONS, RU_FINANCE, SAHEL, VENEZUELA.

**3.5 p_status_quo.** A mechanical probability of "what happens if nobody takes a new decision":
- 0.10 — when YES requires a change to the current state,
- 0.90 — when YES means the current state continues,
- 0.50 — when the status quo cannot be determined.

Set when the question is created, without looking at any forecasts.

**3.6 who_benefits.** Name an actor only when YES clearly strengthens its position at another's expense. Otherwise NONE. Resolve doubt in favour of NONE.

**3.7 Voiding.** The criterion turned out to be ambiguous or the resolution source ceased to exist → status VOID with a justification. The question is excluded from the scores.

**3.8 Triviality.** At most 20% of active questions may have AGG_RT below 0.05 or above 0.95. If exceeded — add harder questions in the next edition.

## 4. Lenses (three independent, blind runs)

**A — "Great-power game".** Who decides; interests and payoffs of each side; capabilities and constraints; available alternatives; which move pays off for whom; what equilibrium of moves follows by the deadline; what would have to happen for the equilibrium to shift.

**B — "Outside view".** Reference class and base rate; persistence of the status quo; time remaining to the deadline (at a constant event rate: p ≈ 1 − (1 − r)^t); adjustment for case specifics only at the end and cautiously. Narrative reduced to a minimum.

**C — "Domestic and economic constraints".** Domestic politics and electoral calendars; personal incentives of leaders (legitimacy, personal relationships); budgets, markets, logistics; institutional procedures and deadlines (e.g. budget calendar, legal steps, notifications to Congress).

For every active question each lens gives: p, a 1–2 sentence rationale in its own logic, a key indicator, analytic confidence, and the change relative to its own previous forecast with the reason.

## 5. Aggregation and red team

- **AGG** = arithmetic mean of A, B, C.
- **Red team** (stage 05) proposes adjustments only on the basis of specific evidence or a logical error (including inconsistency between questions). Limit: ±0.15 per question. No adjustments "to be safe".
- **AGG_RT** = AGG + accepted adjustments (in stage 06). Without an adjustment AGG_RT = AGG.
- **The official forecast is AGG_RT.** The registry holds all runs, which makes it possible to measure whether the red team helps.

## 6. External benchmarks

- Only in stage 06, **after** the "forecasts frozen" commit.
- Sources: Metaculus, Good Judgment Open, Polymarket, Kalshi, Manifold, RAND Forecasting Initiative.
- Matching: EXACT (the same event, deadline ±7 days, similar criterion) or APPROX. Only EXACT matches enter the scores.
- Forecasts of the current edition do not change after the benchmarks are seen. In later editions the lenses still do not see them.
- Benchmarks go only into `07_annex_benchmarks.md`, not into the main report.

## 7. Resolution

- Every resolution has evidence (URL, publisher, date). For PIR questions — two independent sources.
- A question "will Y happen by date X" resolves YES on the day Y occurs, and NO once X has passed.
- VERIFY flag: ambiguous and disputed questions plus a random 20% of the rest (random seed = edition number). Flags are approved by the user.

## 8. Scores

- **Brier** = (p − o)², where o ∈ {0, 1}. Computed for every forecast in every edition separately and as a per-question average.
- **BSS** = 1 − Brier_model / Brier_reference.
- **Calibration:** 10-percentage-point bins.
- **Directional bias:** mean (p − o) within `who_benefits` groups (excluding NONE). A neutral source or method has a mean close to 0 in every group.
- **Clusters:** scores also with a weight of 1 per cluster.
- **Runs:** Brier of A vs B vs C vs AGG vs AGG_RT.
- **Statistical note:** below ~30 resolved questions the scores are indicative; differences between runs are not interpreted before the quarterly review.

## 9. Sources and facts

- Fact record (table in `02_facts/G*.md`): ID | date | actor | action | target | vector | region | status | publisher | URL | source rating | perspective | PIR.
- Key events: three perspectives (W, A, T); search in the actor's language (RU, ZH, AR, FA, TR; for India — English-language media).
- State sources: acceptable as a fact about a statement and as a perspective; never as the only confirmation of a disputed event.
- Wikipedia: only as a chronology index.
- Source map: `sources/source_map.md`.

## 10. Verbal probability scale (report text)

Almost ruled out 1–5% · very unlikely 5–20% · unlikely 20–45% · roughly even chances 45–55% · likely 55–80% · very likely 80–95% · almost certain 95–99%.

## 11. Edition report structure

Header (number, state date, notation conventions) → Executive summary (6–8 paragraphs) → **0. Accuracy scores** (from edition 02) → A. Strategic goals of the great powers → B. Friction points → C. Chokepoints and locations → D. Raw materials and supply chains → E. Shifts in state orientation → F. Economic and technological rivalry → G. Map of shifts in influence → H. Scenarios and forecasts (scenarios for 6–12 months / 2–3 years / 5–10 years with probabilities; full list of AGG_RT forecasts by vector, with the lens spread and the change vs the previous edition) → I. Table of the most significant changes → J. Uncertainties and gaps → K. Implications for Poland (K.1–K.7) → L. State block.

Sections B–F end with a "Mechanism" paragraph and a "For Poland" line. Section titles do not change between editions.

## 12. What we do not change until the quarterly review

Lenses, aggregation and red-team rules, the standing panel, scales, score definitions. Process fixes — only after user approval and an entry in `methodology_changes.md`.
