# Methodology v1.1

In force from edition 04 (state date on or after 30.11.2026). Approved by the user on 22.11.2026, ahead of the quarterly review, as one change set (framework 2.0.0). `methodology_v1.0.md` stays unchanged. Every score is reported separately for questions created under v1.0 and under v1.1.

**What v1.1 changes, in one line.** Under v1.0, the questions followed the news. Under v1.1, they come from a model of power: a fixed set of **structural drivers**, a **power ledger** (who holds which capabilities), **move → counter-move chains** and **actor models**. News becomes evidence for the model. It turns into a question only through a gate (§4.3).

## 1. Measure of success

- **Primary measure (unchanged):** the Brier skill score (BSS) of the official AGG_RT forecast relative to (a) the mechanical status-quo baseline (`p_status_quo`) and (b) the crowd or market, on EXACT matches only.
- **Auxiliary measures (v1.0):** calibration, directional bias, comparison of runs A / B / C / AGG / AGG_RT.
- **Auxiliary measures (new in v1.1), never instead of the primary measure:**
  - Brier by structural driver, by question form, by horizon class and by question origin;
  - **importance-weighted Brier** (weight = `impact`, §4.6). Questions rated retroactively are excluded;
  - **actor-model score:** Brier of CONDITIONAL questions grouped by the responding actor. How well do we predict each power's reactions?
  - headline BSS with and without the tail-risk group (§4.7).
- **Cohorts.** v1.0 questions and v1.1 questions are scored and reported separately. The baselines do not change.

## 2. Priority intelligence requirements (PIR) and structural drivers

PIR-1 to PIR-7 are unchanged. They are the owner's standing priorities, including the deliberate focus on Poland.

- **PIR-1** Russia's capability and will to escalate against NATO and the eastern flank.
- **PIR-2** US/NATO capability and will to respond; US presence in Europe and in Poland.
- **PIR-3** Prices and availability of energy (oil, gas, fuels) in Europe and in Poland.
- **PIR-4** US–China rivalry: trade, technology, raw materials, Taiwan.
- **PIR-5** The war with Iran and sea lanes (Hormuz, Bab el-Mandeb, Suez).
- **PIR-6** Financial condition of the great powers and capital-market conditions, including PLN.
- **PIR-7** Shifts in the orientation of states (elections, alliances, changes of government).
- **PIR-8 (new)** The global balance of power: capabilities, defence-industrial capacity and alignment of the great powers and the swing states (India, Japan, Turkey, the Gulf states, Brazil, Indonesia), plus slow structural stressors (debt, demography, climate, food).

**Structural drivers.** A fixed list, independent of the news, used for coverage, selection and scoring. Definitions, example indicators and the cluster mapping are in `world_model/drivers.csv`.

| Code | Driver |
|---|---|
| D1 | War-fighting capacity (manpower, munitions, air defence, front) |
| D2 | Defence-industrial base and military spending |
| D3 | Alliance cohesion (NATO, US–Europe, EU, US–Asia) |
| D4 | Escalation, deterrence, nuclear and arms control |
| D5 | Energy flows and chokepoints |
| D6 | Technology, compute, critical minerals |
| D7 | Trade and economic coercion (tariffs, sanctions, export controls) |
| D8 | Fiscal-monetary capacity, debt, dollar system |
| D9 | Domestic stability and leadership |
| D10 | Swing states and realignment |
| D11 | Regional wars outside Europe (Middle East, Taiwan Strait, Korea) |
| D12 | Slow stressors (food, climate, demography, migration, health) |
| D13 | Great-power negotiation channels |

The PIRs say **whose decisions** the project serves. The drivers say **what moves the balance of power**. A question carries both.

## 3. World model (new)

Kept in `world_model/` and updated in every edition by stage W (`prompts/W_world_model.md`), which runs after stage 02 and before stage 03. Git history keeps every earlier state.

**3.1 Power ledger** (`world_model/ledger.csv`). One row per actor × power factor.
- **Actors:** US, CN, RU, EU; IN, JP, TR, GULF (Saudi Arabia, UAE, Qatar), BR, ID; UA, IR, PL.
- **Factors:** MIL military capacity · IND defence-industrial base · ECO economic scale and growth · FIS fiscal-monetary capacity · FIN currency and financial reach · TEC technology and compute · ENR energy and resources · ALL alliances and alignment · DOM domestic cohesion and leadership.
- **Each row:** a measurable indicator, its latest value with date and source URL, the trend (UP / FLAT / DOWN), a one-line ASSESSMENT and the analytic confidence.
- **Gaps:** a cell with no data is marked `NO DATA` and listed in the report as a gap. It is never filled from memory (CLAUDE.md rule 1).

**3.2 Chains** (`world_model/chains.csv`). A chain is a sequence of moves and counter-moves between actors on one driver. Example: an export control, then a counter-control on minerals, then a licensing truce.
- **Each chain records:** its ID (`CH-001`…), the driver, the actors, the fact IDs of its links in order, its status (ACTIVE / DORMANT / CLOSED), the last move, and the expected next moves with the actor model that predicts them.
- **Fact records** gain an optional field `reaction_to` (a fact ID or chain ID) when the fact is a response to an earlier move.

**3.3 Actor models** (`world_model/actor_models.md`). For each great power and each swing state, the model records:
- what it reacts to;
- its response repertoire: escalate, mirror, absorb, delay or negotiate;
- its typical lag;
- its declared and revealed red lines;
- the chains that support each claim.

Each actor model is scored through CONDITIONAL questions (§1).

## 4. Question bank

**4.1 Types.**
- **Standing panel:** 40 questions, 5 for each of the 8 vectors. In addition:
  - each driver D1–D13 has at least 2 panel questions;
  - no driver has more than 6;
  - no cluster has more than 3.
  
  The panel is **rebuilt from the model** at the first v1.1 edition (04) and again at each quarterly review. An existing ACTIVE question may be adopted into the panel when it meets the rules. Membership is recorded in `registry/question_meta.csv` (`panel` = the panel set, e.g. `v1.1-2026Q4`). Panel questions created under v1.0 run to their deadlines and are not replaced.
- **Open questions:** 20–30 new ones in every edition.
- **ACTIVE count:** at most 100 at any time. When near the cap, add fewer open questions; panel questions take priority.

**4.2 Question requirements.** Binary YES/NO; an unambiguous resolution criterion; a named public resolution source; a deadline; an event that can still occur after the creation date; no duplicates; an assigned cluster; and the metadata of §4.6. Each question has one **form**:
- **EVENT:** will something happen by a date.
- **LEVEL:** a value of a measured series on or by a date, asked as a **ladder** of 2–3 binary threshold questions on the same series and date (one cluster, linked in `registry/relations.csv` as `higher_threshold`). A ladder covers the plausible range, so the panel is no longer only "will something change?".
- **CONDITIONAL:** "If <trigger> happens between <dates>, will <actor> <response> within <N> days of it?" It always comes with a separate EVENT question for the trigger, linked in `registry/relations.csv` as `conditional_on` (a = the conditional question, b = the trigger question). If the trigger question resolves NO, the conditional question is VOID ("trigger did not occur") and leaves the scores. The responding actor is recorded in `question_meta.csv` (`actor`).
- **SIGNPOST:** a shorter question whose outcome is evidence about a longer question. The longer question's ID is recorded in `signpost_of`. Every question with a horizon over 365 days has at least 2 signposts that resolve within the quarter.

**4.3 Origin and the news gate.** Each new question records its origin in `question_meta.csv`:
- `LEDGER`: a ledger cell with an indicator; usually a LEVEL ladder.
- `CHAIN`: the next move of an active chain; usually a CONDITIONAL pair.
- `DRIVER_GAP`: a driver below its floor.
- `QUIET`: an item of the quarterly quiet-but-important list.
- `TAIL`: a standing tail-risk question.
- `NEWS`: a news event **that passes the gate**. It must do at least one of the following, and the gate condition is named in `notes`:
  - (a) move a ledger indicator outside its normal range;
  - (b) be a trigger or a response in an active chain;
  - (c) open a new chain involving at least one great power.
  
  A news event that passes no gate goes into the report, not the panel.

At least 60% of the new questions in an edition come from LEDGER, CHAIN, DRIVER_GAP, QUIET or TAIL.

**4.4 Horizons.** Horizon classes:

| Class | Days from creation to deadline |
|---|---|
| Q | ≤ 90 |
| Y | 91–365 |
| M | > 365 |

- **Panel:** about 12 Q, 16 Y and 12 M.
- **Open questions in an edition:** at most 50% Q, at least 25% Y, at least 15% M. Signposts are not counted in these shares.

This replaces v1.0 §3.3, which required about 40% of new questions to fall due within 14 days.

**4.5 Form mix.**
- At least 20% of the new questions in an edition are LEVEL questions.
- When active chains exist, each edition adds at least 3 CONDITIONAL pairs.
- Each M question has its signposts (§4.2).

**4.6 Importance metadata** (`registry/question_meta.csv`, append-only, one row per question, written when the question is created and **before any forecast**; never edited afterwards):

| Field | Values | Meaning |
|---|---|---|
| `driver` | D1–D13 | primary structural driver |
| `impact` | 1–5 | effect on the balance of power. 5: changes the military or economic balance between great powers, or the survival of a great-power regime, for years. 4: changes the position of one great power or a major alliance for ≥ 1 year. 3: lasting effect on a region or a key market (≥ 1 quarter). 2: significant but reversible within a quarter. 1: a procedural step or signal |
| `decision` | 0–2 | relevance to a named decision of a PIR user. 0: none. 1: informs. 2: would change a named decision within 12 months; name the user and the decision in `notes` |
| `form` | EVENT / LEVEL / CONDITIONAL / SIGNPOST | §4.2 |
| `horizon` | Q / Y / M | §4.4 |
| `origin` | LEDGER / CHAIN / DRIVER_GAP / QUIET / TAIL / NEWS | §4.3 |
| `chain_id`, `actor`, `signpost_of`, `panel`, `tail` | as applicable | links |
| `rating` | NEW / RETRO | RETRO: rated after forecasts existed (v1.0 questions); excluded from importance weighting |

`impact` rates **global** importance. Polish relevance is carried by `decision` and the PIRs. The panel's mean `impact` is reported in every edition. A mean below 3.5 is flagged in stage 08.

**4.7 Tail group.** 3–4 panel questions of horizon M on low-probability, high-impact events (`tail = Y`). They stay open even though they rarely resolve YES. The headline BSS is reported with and without them.

**4.8 p_status_quo** (unchanged mechanical rule): 0.10 when YES requires a change; 0.90 when YES means the current state continues (for a LEVEL threshold, when the latest value already satisfies YES and the criterion is "on the date"); 0.50 when the status quo cannot be determined. CONDITIONAL questions: 0.50. Set at creation, without looking at any forecast.

**4.9 who_benefits, cluster, voiding, triviality.** As in v1.0 §3.4, §3.6, §3.7 and §3.8. Additional voiding case: a CONDITIONAL question whose trigger did not occur.

## 5. Lenses (three independent, blind runs)

The definitions of lenses A, B and C are unchanged from v1.0 §4. New in v1.1:
- **All lenses read the world model** (`world_model/ledger.csv`, `chains.csv`, `actor_models.md`), as a shared input like the analysis of stage 03.
- **Lens A** states, for every CONDITIONAL question, which actor-model claim it relies on.
- **For a CONDITIONAL question, p is the probability of the response given that the trigger occurs.**
- **For a LEVEL ladder,** the probabilities must be monotonic: a higher threshold never gets a higher p for "above".

## 6. Aggregation and red team

As in v1.0 §5. The red team also checks:
- monotonic LEVEL ladders;
- that CONDITIONAL questions are consistent with their actor models and chains;
- signpost–long-question consistency.

## 7. External benchmarks

Unchanged (v1.0 §6).

## 8. Resolution

As in v1.0 §7. In addition:
- **CONDITIONAL questions** are resolved only after their trigger question. Trigger NO gives VOID ("trigger did not occur"). Trigger YES gives a judgement on the response within its window, counted from the trigger date.
- **LEVEL ladders** are resolved together from one reading of the series.

## 9. Scores

As in v1.0 §8, plus the auxiliary measures of §1. They are computed by `tools/scores.py` from `registry/question_meta.csv`. For questions without a metadata row, the driver comes from the cluster mapping in `world_model/drivers.csv`. The statistical note of v1.0 §8 applies to every breakdown: below about 30 resolved questions a breakdown is indicative only.

## 10. Sources, facts and collection

As in v1.0 §9, plus:
- the optional `reaction_to` field of a fact record (§3.2);
- **Collection breadth.** The harvester stores every item from every source, and the topic concepts only shape the digest. Each edition's `02_harvest/coverage.md` reports:
  - the **unmatched share** (items matching no concept), by country and by language;
  - **source balance by power** (items per actor against the actor's weight in `sources/harvest/source_universe.csv`);
  - **emerging terms**: terms that surge in unmatched items against their 90-day baseline.
  
  Stage W reads the emerging terms. A term that names a development relevant to a driver becomes a temporary concept for 30 days (`sources/harvest/keywords_emerging.csv`, maintained by stage W). It is kept for longer only by the quarterly review.
- **Structural data.** Slow power indicators (military spending, reserves, trade, debt, demography) are collected as datasets where a free, readable source exists. Event data on great-power dyads (GDELT event counts by quad class) is collected as an indicator of cooperation and conflict, never as proof of a single event.

## 11. Verbal probability scale

Unchanged (v1.0 §10).

## 12. Edition report structure

As in v1.0 §11, with these contents:
- **section B** (friction points) includes a table of active chains: chain, last move, expected next move, linked questions;
- **section G** (map of shifts in influence) is written from the power-ledger changes since the previous edition;
- **section J** includes driver coverage: questions per driver, the panel's mean impact, and ledger cells marked NO DATA.

Section titles do not change.

## 13. Quarterly review

As in `prompts/Q_quarterly_review.md`, plus:
- **Error tracing by layer.** For each of the largest errors, search the stored corpus for the deciding fact and classify where the chain broke: collection gap (not harvested) · digest gap (harvested, not surfaced) · model gap (wrong ledger or chain) · actor-model gap (reaction mispredicted) · probability (right model, wrong number) · timing · ambiguous question.
- **Attention against importance.** Rank correlation between media attention (harvested items per concept) and `impact`. List questions with high attention and low importance, and the reverse.
- **Quiet-but-important list.** 5–8 developments a quarter, from outside experts and the low-attention / high-importance flags, deliberately kept separate from the harvester. Each one becomes a question or is rejected with a reason.
- **Zero-based panel rebuild** from the model (§4.1).
- Review of the driver list, the ledger factors and the emerging concepts.

## 14. What we do not change until the next quarterly review

Lenses, aggregation and red-team rules, the panel rules, the drivers, scales and score definitions. Process fixes only after user approval and an entry in `methodology_changes.md`.
