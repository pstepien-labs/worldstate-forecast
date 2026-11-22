# Input to the quarterly review 2026-Q4: panel importance and coverage

Draft of 21.11.2026. **Status: implemented on 22.11.2026** as methodology v1.1 / framework 2.0.0, by user approval ahead of the quarterly review. Where each proposal went:
- A (rubric): `registry/question_meta.csv`, methodology v1.1 §4.6;
- B (constraints): v1.1 §4.1, §4.4, §4.5 and §4.7;
- C (attention against importance): the `coverage.md` breadth sections, plus quarterly-review task 5a;
- D (quiet list): `world_model/quiet_list.md`;
- the hypothesis of §6: quarterly-review task 5d;
- the expert packet: `reviews/2026-Q4_expert_packet.md`.

The diagnosis below is kept as the baseline that v1.1 is measured against.

The problem: the panel is scored for **accuracy**, but nothing checks whether it asks **important** questions. A panel can be well calibrated and still miss what matters if question selection follows the news.

---

## 1. Diagnosis (registry state on 21.11.2026, 150 questions)

Reproduce with `registry/questions.csv` (fields `cluster`, `created`, `deadline`, `p_status_quo`, `region`).

| Finding | Number |
|---|---|
| Largest clusters | HORMUZ 10 · UA_TALKS 8 · OIL_PRICE 7 · EU_ENERGY 7 · CN_RARE_EARTHS 6 · BAB_EL_MANDAB 6 |
| Horizon (deadline − created) | median 38.5 days; 67 ≤ 30 days; 107 ≤ 90 days; 43 within 91–365 days; **0 > 365 days** |
| Active questions with a deadline after 31.03.2027 | 6 of 83 |
| `p_status_quo` = 0.10 (the question asks "will X change?") | 132 of 150 |
| Region "Poland" | 17 (the largest single region; by design through PIR-3 and PIR-6) |
| Question text mentions | India 0 · Japan 0 · nuclear arms control 0 · demography 0 · AI/semiconductors 1 · sovereign debt/dollar 1 · Turkey 1 · Gulf states 3 · food/climate 3 |

**Upstream cause.** `sources/harvest/keywords.csv` has 38 concepts. None covers India or South Asia, Japan, Turkey, the Gulf states as actors, nuclear arms control, defence industry and military spending, demography, migration or climate. Questions are written from harvested material, so these topics cannot reach the panel. ASSESSMENT: some of the attention bias is built in at collection, before question writing begins.

**Data hygiene.** `region` labels are inconsistent ("Global" / "global", "China–USA" / "USA-China", en dash vs hyphen). Region counts are approximate until these are normalised.

### 1.1 Coverage by structural driver

A fixed list of drivers, independent of the news. Clusters are mapped to one primary driver each (mapping in Appendix A; the mapping is an ASSESSMENT and open to challenge).

| Driver | Questions | Active | Median horizon (days) | > 182 days |
|---|---:|---:|---:|---:|
| D1 War-fighting capacity (manpower, munitions, air defence, front) | 5 | 4 | 99 | 1 |
| D2 Defence-industrial base and military spending | **0** | 0 | – | 0 |
| D3 Alliance cohesion (NATO, US–Europe, EU, US–Asia) | 11 | 8 | 85 | 4 |
| D4 Escalation, deterrence, nuclear and arms control | 8 | 6 | 50 | 1 |
| D5 Energy flows and chokepoints | **39** | 18 | **14** | 1 |
| D6 Technology, compute, critical minerals | 10 | 6 | 52 | 0 |
| D7 Trade and economic coercion (tariffs, sanctions) | 16 | 8 | 31 | 1 |
| D8 Fiscal-monetary capacity, debt, dollar system | 18 | 9 | 24 | 1 |
| D9 Domestic stability and leadership | 14 | 6 | 36 | 0 |
| D10 Swing states and realignment (India, Turkey, Gulf, Global South) | 5 | 4 | 189 | 3 |
| D11 Regional wars outside Europe (Middle East, Taiwan Strait, Korea) | 10 | 5 | 30 | 1 |
| D12 Slow stressors (food, climate, demography, migration, health) | 3 | 1 | 21 | 0 |
| D13 Great-power negotiation channels | 11 | 8 | 45 | 2 |

ASSESSMENT: D5 holds 26% of all questions, at the shortest median horizon. This is where the panel follows the news most closely. D2 and D12 are almost empty, and D10 exists mostly at the periphery (Panama, Venezuela, Sahel, Caucasus), not through the swing states themselves.

---

## 2. Proposal A: importance rubric (one rating per question)

Each new question is rated **when it is created, before any forecast**, and the rating is frozen. This prevents the rating from being bent toward questions that turn out to be easy.

| Field | Values | Anchors |
|---|---|---|
| `impact` | 1–5 | 5: changes the military or economic balance between great powers, or the survival of a great-power regime, for years. 4: changes the position of one great power or a major alliance for ≥ 1 year. 3: lasting effect on a region or a key market (≥ 1 quarter). 2: significant but reversible within a quarter. 1: procedural step or signal; matters only as a lead indicator |
| `decision` | 0–2 | 0: no named user would act on it. 1: informs a named decision of a PIR user. 2: would change a named decision within 12 months (name the user and the decision in `notes`) |
| `driver` | D1–D13 | primary structural driver (section 1.1) |
| `form` | EVENT · LEVEL · SIGNPOST | EVENT: yes/no on an occurrence. LEVEL: a quantity, range or bin (price, output, spending, stock). SIGNPOST: an intermediate question attached to a longer question (ID in `notes`) |
| `horizon` | Q · Y · M | Q ≤ 90 days · Y 91–365 days · M > 365 days |

`impact` rates **global** balance-of-power importance. Polish relevance is captured by `decision`, so the deliberate Poland focus (PIR-3, PIR-6) is reported openly and kept separate from global importance.

**Use in scoring (secondary only).** The official scores stay unweighted, and the baselines stay unchanged. The review additionally reports:
- the panel's mean `impact` and its distribution, per edition (trend over time);
- an impact-weighted Brier (weight = `impact`) next to the unweighted one, with a bootstrap interval by cluster;
- Brier by `form` and by `horizon`.

**Where to store it.** `registry/` is append-only and protected, so the rubric would be either new columns added in v1.1 or a separate `registry/importance.csv` (id; rated_on; impact; decision; driver; form; horizon; rater). To be decided at the review. The separate file keeps the existing schema intact.

**Rater check.** Questions are written by the pipeline, which also rates them, so the rating needs an outside check. Proposal: one or two experts rate a random 30 questions blind, and the review reports agreement (weighted kappa on `impact`). If agreement is poor, the anchors are rewritten before the rubric is used for anything else.

## 3. Proposal B: driver and horizon constraints for the new panel (task 6)

Task 6 asks for 40 questions, 5 per vector. Vectors (MIL, ENE, …) are channels, not structural variables, so a vector-balanced panel can still be driver-skewed. Keep the 5-per-vector rule and add:

1. **Driver floor and cap:** every driver D1–D13 has ≥ 2 questions; no driver has more than 6 (15%); no cluster has more than 3.
2. **Horizon mix:** 12 Q (30%) · 16 Y (40%) · 12 M (30%). Each M question has ≥ 2 SIGNPOST questions that resolve within the quarter, so long questions still produce feedback. Signposts are OPEN questions and do not count toward the 40.
3. **Form mix:** ≥ 8 of 40 are LEVEL questions (ranges or bins: e.g. defence spending in an adopted budget, EU artillery-ammunition output, a reserve or stock figure, a yield range). This lowers the "will X change?" share. LEVEL questions also suit the QNT shadow run.
4. **Panel mean `impact` ≥ 3.5**, reported but not optimised beyond that. The floor is a guard, not a target.

**Tail-risk standing questions.** 3–4 of the M questions should be low-probability, high-impact events kept open for the long run (examples of the type: nuclear use or test by a state that has not tested since 2000; a Taiwan blockade or quarantine; a sovereign default in the G20). They rarely resolve YES and will cost Brier in the short run. Report them as a separate group so they do not distort the comparison with baselines.

## 4. Proposal C: attention-vs-importance check (each edition)

For every active question: **attention** = the share of harvested items in the previous 30 days that match the question's harvester concept (`data/harvest`, concept tags from `keywords.csv`). **Importance** = `impact`.

- Flag **loud-but-minor** questions: attention in the top tercile and `impact` ≤ 2. Candidates for retirement.
- Flag **quiet-but-important** questions: attention in the bottom tercile and `impact` ≥ 4. Candidates to protect from retirement.
- Report the rank correlation between attention and importance. ASSESSMENT: a high positive correlation means the panel follows the news.

**Precondition:** attention can only be measured for topics the harvester collects. Add harvester concepts for: India and South Asia · Japan · Turkey · Gulf states (as actors, beyond shipping) · nuclear arms control and proliferation · defence industry and military spending · demography and migration · climate shocks. ASSESSMENT: this is the cheapest step and only widens collection. If it starts by early December, the review has about three weeks of data on these topics. It still needs the user's decision on whether a keywords change may go in before the review.

## 5. Proposal D: quarterly "quiet-but-important" list

Each quarter, a list of 5–8 developments, deliberately kept **separate from the harvester** (the harvester follows volume by design). Sources: expert nominations, the quiet-but-important flags from Proposal C, and long-range assessments (national-intelligence long-range reports, annual risk rankings, insurers' emerging-risk lists). Each item either becomes at least one question in the next panel, or is rejected with a one-line reason. Both outcomes are recorded in the review.

## 6. Hypothesis to test at the review (no change proposed)

The status-quo framing (132 of 150 at `p_status_quo` = 0.10) may contribute to the mid-range calibration bias. Test: calibration and Brier for questions with `p_status_quo` 0.10 vs the rest, using a bootstrap interval by cluster. If the interval includes zero, the conclusion is "no evidence of a difference".

## 7. What to ask experts for (packet)

Experts' time is scarce, so ask for **outputs**, not opinions. These outputs feed the review directly:

1. **Rate 20–30 questions** on the rubric (section 2), blind to the forecasts. Gives rater agreement.
2. **Delete 10 and add 3**: which panel questions they would drop, and which 3 they would add (with a deadline). Gives the quiet-but-important list.
3. **Challenge the driver list** (section 1.1, Appendix A): what is missing, what is merged wrongly, and which observable indicator tracks each driver.
4. **One method question** matched to their field:
   - strategy and history: "Which developments looked minor when they happened but changed the balance later? What is the equivalent now?"
   - macro and finance: "Which economic channels actually move geopolitics, and which are noise? Should I forecast levels instead of events?"
   - military: "Which measurable factors decide where the war and NATO deterrence are heading? Which can be forecast quarter by quarter?"
   - risk practitioners: "How do you stop media attention from setting your ranking? How often do you rebuild the list from scratch?"
   - decision-makers: "Which forecast would change a decision you will make in the next 12 months? Which would you ignore even if it were accurate?"
   - tail-risk and nuclear/biosecurity: "Which low-probability, high-impact events deserve standing questions?"

Attach: this file without Appendix A, the current panel (question texts only, no probabilities), and the PIR list.

## 8. Timeline to the review

| By | Step |
|---|---|
| 28.11.2026 | User approves or edits this draft; decision on the harvester concepts (section 4) |
| 01.12.2026 | Expert packet sent |
| 15.12.2026 | Expert responses collected; rater agreement computed |
| c. 21.12.2026 | Review: tasks 5–6 use the rubric and the constraints, if approved |

---

## Appendix A. Cluster → driver mapping (ASSESSMENT)

| Driver | Clusters |
|---|---|
| D1 | UA_FRONT, RU_MOBILIZATION |
| D2 | (none) |
| D3 | US_EUROPE, UA_USA, UA_EU, UA_FUNDING, GREENLAND, US_EU_TRADE |
| D4 | EASTERN_FLANK, BALTIC_INFRA, KOREA |
| D5 | HORMUZ, BAB_EL_MANDAB, OIL_PRICE, EU_ENERGY, PL_FUELS, OPEC, BLACK_SEA, URANIUM |
| D6 | US_CHINA_TECH, CN_RARE_EARTHS |
| D7 | US_CHINA_TRADE, RU_SANCTIONS_US, RU_SANCTIONS_EU, CN_SECONDARY_SANCTIONS, US_CHINA_FIN |
| D8 | RATES_RU, RATES_ECB, RATES_FED, RATES_PL, US_FISCAL, RU_FINANCE, PL_FINANCE, PL_INFLATION, PLN |
| D9 | RU_DOMESTIC, IRAN_LEADERSHIP, US_ELECTIONS, BRAZIL_ELECTIONS, LATVIA_ELECTIONS, BG_ELECTIONS, ES_ELECTIONS, IL_ELECTIONS, IL_GOVERNMENT, RS_GOVERNMENT |
| D10 | PANAMA, VENEZUELA, SAHEL, CAUCASUS |
| D11 | IRAN_WAR, TAIWAN |
| D12 | FOOD |
| D13 | UA_TALKS, US_CHINA_SUMMITS |

Contested mappings to note: HORMUZ and BAB_EL_MANDAB could sit under D11 (war) rather than D5 (energy). Moving them gives D5 23 and D11 26. The skew remains, but it moves to the Middle East war.
