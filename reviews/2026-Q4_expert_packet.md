# Request for expert input: is this forecast panel asking the right questions?

*Calibrated Balance-of-Power Forecast · quarterly review 2026-Q4 (c. 21.12.2026) · packet of 22.11.2026*

## What the project is

The project produces an open, scored forecast of the moves of the great powers every two weeks. Every forecast is kept in an append-only public registry and scored against simple baselines with the Brier score. The method, prompts and registry are public in this repository.

## Why we are asking

Accuracy is measured. **Importance is not.** A review of the 150 questions asked so far (21.11.2026) found that the panel followed the news:
- Hormuz, the Ukraine talks and the oil price held the most questions;
- the median horizon was 39 days, and no question ran longer than a year;
- 132 of 150 questions asked "will something change?";
- India, Japan, nuclear arms control, the defence-industrial base and demography had no questions at all.

From 22.11.2026 (methodology v1.1), questions come from a **model of power**: 13 structural drivers, a power ledger of 13 actors × 9 factors, move → counter-move chains and actor models. News enters only through a gate. We want outside experts to challenge this model before the first review on data.

## What we ask of you (about 60–90 minutes)

1. **Rate 20 questions** (list attached) on the importance rubric, without seeing our forecasts:
   - `impact`, 1–5:
     - 5: changes the balance between great powers, or the survival of a great-power regime, for years;
     - 4: changes one great power's or a major alliance's position for ≥ 1 year;
     - 3: a lasting effect on a region or a key market;
     - 2: significant but reversible within a quarter;
     - 1: a procedural signal.
   - `decision`, 0–2: would the answer change a decision someone makes within 12 months?
2. **Delete 10, add 3.** Which of the attached questions would you drop? Which 3 questions would you add, each with a deadline and a public resolution source?
3. **Challenge the drivers** (table below). What is missing? What is merged wrongly? Which observable indicator best tracks each driver?
4. **One question for your field:**
   - **strategy and history:** which developments looked minor when they happened but changed the balance later, and what is the equivalent now?
   - **macro and finance:** which economic channels actually move geopolitics, and which are noise? Should we forecast levels and ranges instead of events?
   - **military:** which measurable factors decide where the war in Ukraine and NATO deterrence are heading, and which can be forecast quarter by quarter?
   - **risk practice:** how do you stop media attention from setting your ranking, and how often do you rebuild the list from scratch?
   - **policy or business:** which forecast would change a decision you will make in the next 12 months, and which would you ignore even if it were accurate?
   - **tail risk (nuclear, biosecurity):** which low-probability, high-impact events deserve standing questions?

Reply in any form. Answers are summarised, without names unless you agree, in `reviews/experts/` and in the quarterly review.

## The 13 structural drivers

| Code | Driver |
|---|---|
| D1 | War-fighting capacity (manpower, munitions, air defence, front) |
| D2 | Defence-industrial base and military spending |
| D3 | Alliance cohesion (NATO, US–Europe, EU, US–Asia) |
| D4 | Escalation, deterrence, nuclear and arms control |
| D5 | Energy flows and chokepoints |
| D6 | Technology, compute, critical minerals |
| D7 | Trade and economic coercion |
| D8 | Fiscal-monetary capacity, debt, dollar system |
| D9 | Domestic stability and leadership |
| D10 | Swing states and realignment (India, Japan, Turkey, Gulf, Brazil, Indonesia) |
| D11 | Regional wars outside Europe (Middle East, Taiwan Strait, Korea) |
| D12 | Slow stressors (food, climate, demography, migration, health) |
| D13 | Great-power negotiation channels |

Definitions and example indicators: `world_model/drivers.csv`. Method: `methodology/methodology_v1.1.md`.

## Attachments to send

- **The 20 questions to rate and the full list of active questions:** `reviews/experts/2026-Q4_questions_to_rate.md` (drawn 22.11.2026; wording and deadline only, **no probabilities**).
- **This page.**

Do not attach forecasts, benchmarks or harvested headlines.
