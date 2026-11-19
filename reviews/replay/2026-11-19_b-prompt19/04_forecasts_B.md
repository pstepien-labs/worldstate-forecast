# Replay b-prompt19 — lens B "Outside view" on edition 02 (state 07.10.2026)

Run: `B@b-prompt19` · prompt: `prompts/04_forecasts.md` (lens B section, way of working WP-09) · inputs: `questions.csv` (88), `02_facts/G1–G4.md`, `03_analysis.md` of edition 02 · no web, no registry, no earlier forecasts.
Information cutoff: 07.10.2026 (see `validity.md`). Facts dated after 07.10 that appear in the inputs (03_analysis line 9: Kremlin/Ushakov call report 09.10, Araghchi 08.10, Council adoption date 12.10, NDAA calendar; G3-069 BOFIT 09.10; G4 §15 consulate outcome 08.10) are not used. Post-cutoff facts seen: 6.
Method per question: reference class and base rate → persistence and time left (p ≈ 1 − (1 − r)^t) → cautious case adjustment. Three lines before each p: two strongest YES reasons, two strongest NO reasons, "by now we would expect to see …". Searches: 0 (replay without web).
Horizon t is counted from 07.10.2026.

---

## Batch 1 — HORMUZ, IRAN_WAR, BAB_EL_MANDAB (12 questions)

### Q-0028 — US–Iran agreement incl. Hormuz opening by 31.12.2026
- Reference class: interstate wars/blockades with an active mediator and a prior ceasefire memorandum; monthly hazard of a signed interim deal ≈ 5% once talks have regressed to indirect exchange. t = 2.8 months → 1 − 0.95^2.8 ≈ 0.13.
- YES: Iran's crude loadings at zero (G2-012) and a precedent of a mediated memorandum (17.06, G4-086); Vance softens to a "meaningful reduction" of enrichment (G4-007).
- NO: talks indirect only, the 7-day plan rejected and "seven conditions" (G4-002, G4-003); the Iranian negotiating mandate is contested (impeachment motion, G4-009).
- By now we would expect: a confirmed face-to-face round or a text under discussion — not seen.
- p = 0.14 (low).

### Q-0036 — PortWatch Hormuz 7-day mean > 40 on any day to 31.12
- Reference class: AIS-visible traffic recovering from a closure; requires a deal plus about a week of normalisation. P(deal by early XII) ≈ 0.10 × P(fast AIS-visible return) ≈ 0.5, plus a small de facto opening path.
- YES: flow estimates suggest ships move (dark) and could become visible once a deal removes risk (G2-005); 12 empty Qatari LNG carriers wait near Qatar (G2-022).
- NO: 7-day mean 2.7 (G1-001); IRGC clearance rule and tanker strikes (G1-004, G1-002).
- By now: any upward trend in AIS counts — not seen (0–5/day).
- p = 0.06 (medium).

### Q-0037 — PortWatch ≥ 20 Hormuz transits on any day 24.09–07.10
- Base: 0 of 12 published days ≥ 20, maximum 5 (G1-001); only 05–07.10 unpublished, during the heaviest tanker-strike week.
- YES: Iranian adviser claims about 10/day (G1-005); data revisions.
- NO: maximum 5 in the window; strikes and route rule from 05.10.
- By now: rising counts by 04.10 — not seen.
- p = 0.02 (high).

### Q-0038 — US lifts or suspends the blockade by 31.12
- Reference class: blockades are lifted as part of a settlement, rarely unilaterally; p tracks Q-0028 minus deals without a blockade clause plus a small goodwill path.
- YES: Iran's plan makes lifting the first step (G4-002); US fuel prices and approval 32% (G4-045).
- NO: blockade is the main US lever and is intensifying (130 vessels, G1-007); third carrier group en route (G1-009).
- By now: a US signal of sequencing (lifting for reopening) — not seen.
- p = 0.12 (low).

### Q-0078 — PortWatch ≥ 10 Hormuz transits on a single day 08–17.10
- Base: daily counts 0–5 for 12 days (mean ≈ 3); a Poisson tail at ≥ 10 is about 0.1% a day; regime-change risk adds most of the probability.
- YES: IRGC "northern route with clearance" lets cleared ships pass visibly (G1-004); Qatari LNG carriers gathering (G2-022).
- NO: tanker strikes at their highest weekly level (G1-002); AIS-dark practice under escort (G1-006).
- By now: one day at 6–9 — not seen.
- p = 0.07 (medium).

### Q-0081 — US and Iranian representatives in the same room 08–21.10
- Reference class: since the June memorandum, face-to-face rounds have been rare (one direct contact 22.09); rate about one per 1–2 months, now lower. 14 days → ≈ 0.10.
- YES: Qatar says "contacts and visits continue" (G4-006); Pezeshkian "deal not out of reach" (G4-014).
- NO: the 22.09 meeting triggered an impeachment motion (G4-009), deterring the next one; Pezeshkian "talks futile" (G4-005).
- By now: an announced round with date/venue — not seen.
- p = 0.10 (medium).

### Q-0065 — CENTCOM/Pentagon confirms a US strike on Iranian land by 31.12
- Reference class: this war's own record — several US strike phases in 2026 ("attacked Iran three times after rounds of talks", G4-005), last strike 01.09; hazard ≈ 15–25% a month, suppressed before 03.11 (KA1). ~4 weeks at ≈ 5% + ~8 weeks at ≈ 22% → ≈ 0.42.
- YES: strike options "after the elections" (G1-010) and Trump "nice way or not-so-nice way" (G4-008); third carrier group and 9–10k personnel arriving by end-XI (G1-009).
- NO: no land strike for 5 weeks; US domestic constraints (approval 32%, UST10Y 24-year high, diesel crisis).
- By now: force build-up toward the stated end-state — seen (departures 27–28.09).
- p = 0.42 (low).

### Q-0099 — USNI tracker shows ≥ 3 carriers in CENTCOM waters by 30.11
- Reference class: officially stated deployment end-states are usually reached, often with slips of weeks; 3-carrier presence in CENTCOM occurred briefly in past crises. Stated end-state "three carriers by end-XI" (G1-009) gives ≈ 0.55 before timing risk.
- YES: George Washington already in the Arabian Sea; Roosevelt crossing the Pacific (G1-057).
- NO: third hull not identified (Bush in Phuket after 5 months, Eisenhower returning, G1-057); the last tracker before 30.11 is the only margin for slips.
- By now: Roosevelt departure and transit — seen; a named third carrier — not seen.
- p = 0.45 (low).

### Q-0068 — US strike on Houthi targets in Yemen by 31.12
- Reference class: US kept out of Yemen since the 2025 truce; renewed strikes would mostly follow a US–Iran escalation (Q-0065) or Houthi attacks on US ships. ≈ 0.42 × 0.5 + independent path ≈ 0.08.
- YES: Saudi pressure and Camp David deliberations on Yemen (G1-010); Saudi civilian deaths (G1-018).
- NO: US "not taking kinetic action for now"; Rubio leaves defence to Saudi Arabia (G1-021); Mecca Alliance takes the role (G1-020).
- By now: US naval posture or warnings toward the Houthis — not seen.
- p = 0.28 (low).

### Q-0079 — PortWatch Bab el-Mandeb < 20 on any day 08–17.10
- Base: 12 published days, range 22–37, mean ≈ 29, sd ≈ 4; per-day chance of < 20 ≈ 1–2% → ≈ 0.14 over 10 days; plus escalation risk at the strait.
- YES: ground war at Dhubab/Mocha (G1-015); Houthi airspace warnings (G1-017).
- NO: traffic stable and even rising through the window (G1-012); no ship hit since 24.08.
- By now: a falling trend in daily counts — not seen.
- p = 0.18 (medium).

### Q-0080 — Saudi source reports ≥ 1 killed on Saudi territory by a Yemeni strike 08–21.10
- Reference class: the current escalation since 19.09 produced fatalities on 06–07.10 after about 2.5 weeks of strikes; with the campaign intensifying the 14-day hazard ≈ 0.4–0.5.
- YES: Houthi strikes on airports with 3 dead and 36 injured (G1-018); coalition offensive and 60 strikes/day give the Houthis motive to escalate (G1-017).
- NO: most missiles and drones intercepted (G1-013, G1-018); Mecca Alliance air defence arriving (G1-020).
- By now: strikes continuing daily — seen.
- p = 0.45 (low).

### Q-0092 — UKMTO/JMIC: merchant ship hit in Red Sea/BaM/Gulf of Aden 08–21.10
- Reference class: since 24.08 one near-miss (04.10) and no hit; Houthi focus is Saudi territory. Rate of hits ≈ 1 per 6–8 weeks → ≈ 0.2 for 14 days, raised by the ground war at the strait.
- YES: attempted attack south of Mokha 04.10 (G1-022); Houthis threaten wider targeting (G1-017).
- NO: Houthi effort directed at Saudi Arabia; Bab el-Mandeb traffic stable (G1-012).
- By now: a run of incidents near the strait — one near-miss only.
- p = 0.22 (low).

Batch 1 log: questions 12; searches 0; consistency check done (each p moves in the direction of the listed evidence relative to the base rate).

---

## Batch 2 — OIL_PRICE, EU_ENERGY, PL_FUELS, URANIUM, FOOD (14 questions)

### Q-0007 — Brent front-month settlement > 120 on any day 24.09–31.12
- Reference class: barrier-touch probability for crude in a war regime; realised vol ≈ 35–45% (closes 93.7–110 within a month), ~12 weeks left, barrier +18% above 100.2 → 0.28–0.40; backwardation roll-down (Dated 114–121 vs futures 100; EIA 2027 avg 84) lowers each front-month roll → ≈ 0.25.
- YES: physical tightness (spot 13–20 above futures, G2-003); post-03.11 strike options and tanker-strike wave (G1-010, G1-002).
- NO: Gulf flows near pre-war per banks (G2-005), G7/IEA releases (G2-009, G2-010); front-month peaked "near 110" even during the September stress.
- By now: closes trending toward 110+ — not seen (97–103).
- p = 0.24 (medium).

### Q-0008 — Brent front-month settlement < 80 on any day 24.09–31.12
- Barrier −20%; vol 35% → ≈ 0.18; roll-down into steeply backwardated deferred months helps the downside; a deal (Q-0028 ≈ 0.14) would likely push toward the 80s.
- YES: flows recovering and Aramco's widest Asian discount since 2020 (G2-050); reserve releases.
- NO: EIA 4Q26 forecast 105 (G2-004); no deal in sight, escalation risk after 03.11.
- By now: closes below 95 — not seen.
- p = 0.16 (medium).

### Q-0074 — Brent front-month settlement on 20.10 > 100.00
- Same December contract (no roll before 20.10); threshold equals the current level (100.20). 13 days, vol 35% → near 0.5; slight downside from releases vs upside from strikes — balanced.
- YES: spot premium, EIA 105; tanker strikes.
- NO: "oil dips as Middle East flows recover" (G2-002); IEA acceleration (G2-010).
- By now: n/a (symmetric).
- p = 0.50 (low).

### Q-0115 — Brent < 70 on any day 08.10.2026–30.06.2027
- 8.7 months; barrier −30%; vol 35% gives ≈ 0.25 without drift; roll-down along a curve averaging ~84 for 2027 (EIA) and a ≈ 40% chance of a Hormuz settlement within the horizon (pre-war Brent in the 60s) raise it.
- YES: deal path; demand destruction plus stock rebuilding finished.
- NO: inventories to rebuild after 400 mn bbl releases; Qatar and Gulf capacity damage; Russian refining losses.
- By now: n/a (long horizon).
- p = 0.33 (low).

### Q-0106 — US ban/quota on distillate exports in force by 31.12
- Reference class: US product export controls — none since the 1970s; threats used as leverage. Base ≈ 3–5% a quarter in crisis conditions.
- YES: diesel 6.29 USD/gal and midterms; Republicans called for a ban (G2-008).
- NO: Trump 02.10 "not going to be doing the export ban" after G7 release (G2-009); industry opposition.
- By now: a draft order — not seen.
- p = 0.07 (medium).

### Q-0009 — TTF front-month > 90 on any day 24.09–31.12
- Barrier +14.6% above 78.53; TTF realised vol ≈ 40–50% → touch ≈ 0.47–0.57; roll into Dec/Jan winter contracts and lowest storage since 2011 add upside.
- YES: storage 72.8% and Qatari force majeure extended (G2-016, G2-021); cooler forecasts, JKM premium (G2-015, G2-020).
- NO: range 69.8–78.5 over two weeks (low realised vol); UBS Q4 target 75.
- By now: new highs in the window — seen (78.53 on 07.10).
- p = 0.50 (low).

### Q-0010 — EU storage on 01.01.2027 < 55.0%
- Reference class: drawdown 1 Nov → 1 Jan in recent winters: 2021 ≈ 24 pp (77 → 53), 2024 ≈ 23 pp, 2025 ≈ 22 pp, 2022–23 ≈ 12–13 pp (mild, demand destruction). Expected 1 Nov ≈ 79% → central 1 Jan ≈ 57%, sd ≈ 4–5 pp.
- YES: 2021 analog almost identical start (≈ 77%) ended at 53%; Qatari LNG shortfall limits refill.
- NO: high prices cut demand (as in 2022); member states restrain withdrawals.
- By now: n/a.
- p = 0.32 (low).

### Q-0049 — EU storage on gas day 06.10 > 73.0%
- 05.10 = 72.83%; recent pace 0.22–0.27 pp/day (70.87 on 26.09, 71.5 about 30.09 → 72.83); needs +0.17 in one day; daily variation ≈ 0.08.
- YES: steady injection pace (G2-016).
- NO: cooler weather from 06.10 reduces injections (G2-015); aggregator readings differ.
- By now: n/a.
- p = 0.68 (medium).

### Q-0067 — EU storage on 01.11 ≥ 80.0%
- Projection at the current pace 78.7% (GEF); needs ≈ 0.27 pp/day for 27 days while October injection normally slows.
- YES: incentive to reach the relaxed 80% target (G2-018).
- NO: pace and season; Lithuania: not "at any cost" (G2-019).
- By now: an acceleration above 0.25 pp/day — not seen.
- p = 0.18 (medium).

### Q-0084 — TTF front-month settlement on 20.10 > 80.00
- Same November contract; threshold +1.9% above 78.53; 13 days, vol 45% → ≈ 0.43; short upward momentum.
- YES: cooler weather, low storage, Hormuz LNG strike risk (G2-015).
- NO: two-week realised range below 80; LNG carriers preparing to sail from Qatar (G2-022).
- By now: n/a.
- p = 0.45 (low).

### Q-0085 — e-petrol diesel average on 21.10 < 7.70 PLN/l
- Station averages track the daily maximum price (avg 7.78 vs max 7.80 on 07.10); maximum fell 7.88 → 7.82 → 7.80 → 7.74 in five days (G2-026); a further 0.06 decline in two weeks is slightly more likely than not with diesel stock releases.
- YES: G7 "substantial diesel release within the first 20 days" (G2-009); falling maximum-price trend.
- NO: Brent flat around 100; PLN weaker against USD (G3-045).
- By now: max price ≤ 7.74 — seen (08.10 notice, published by 07.10 per G2-026).
- p = 0.55 (low).

### Q-0107 — Commission letter of formal notice to Poland on fuel VAT by 31.12
- Reference class: Poland's 8% fuel VAT in 2022 (11 months) drew no infringement; the Commission sent only a warning letter (III) during earlier CPN editions. Temporary crisis measures are usually tolerated.
- YES: Poland the only member state with reduced fuel VAT (G2-028); Commission "analysing".
- NO: measure planned to 31.12; Spain was persuaded without infringement.
- By now: Commission naming a procedure — not seen.
- p = 0.10 (medium).

### Q-0103 — Cameco month-end U3O8 spot > 95 for X, XI or XII
- Spot 89.4–89.9; needs +6% at one of three month-ends; monthly vol ≈ 7–9% → ≈ 0.30.
- YES: term price at a nominal record 96–97 (G2-048); Russia–Iran uranium news.
- NO: spot flat for a month (89.7 on 21.09 → 89.85 on 06.10).
- By now: n/a.
- p = 0.30 (low).

### Q-0076 — FAO FFPI October > 136.0
- Monthly changes positively autocorrelated; September +1.5% with cereals +5.1%, sugar +6.1% (G2-036); unconditional chance of a rise ≈ 0.5, momentum and energy/fertiliser costs → ≈ 0.6.
- YES: Black Sea shipping attacks (G1-031), Hormuz fertiliser risk (G2-039).
- NO: Brent flat in October vs September (vegetable-oil link); meat down.
- By now: n/a.
- p = 0.60 (low).

Batch 2 log: questions 14; searches 0; consistency check done.

---

## Batch 3 — RATES (PL, ECB, RU, Fed), PL_FINANCE, PLN, PL_INFLATION, US_CHINA_FIN, CN_SECONDARY_SANCTIONS (11 questions)

### Q-0016 — MPC changes the NBP rate at any meeting 24.09–31.12
- Remaining meetings: 03–04.11 (projection) and early XII. Reference class: when bank economists expect a first hike at the next meeting and the communiqué hardens, the hike comes within two meetings about half the time; NBP historically slow to hike on supply shocks (2021).
- YES: CPI 4.0% outside the band; wording "maintaining" → "ensuring" (G3-039, G3-040); Pekao expects a November hike.
- NO: CPN fuel caps cut measured October CPI by about 0.8 pp (G2-026), giving a reason to wait; falling employment (G3-040).
- By now: a hawkish press-conference signal — post-cutoff (08.10), not used.
- p = 0.45 (low).

### Q-0017 — ECB raises the deposit rate on 29.10 or 17.12
- Reference class: the ECB hiked in VI and IX (projection meetings, quarterly pace); continuation at the next projection meeting in a live cycle ≈ 0.6; October less likely.
- YES: HICP 3.8%, "second wave" upside risk (G3-037, G3-076); "measured response appropriate" (G3-075).
- NO: Lane: long-term yields are "material tightening", no pre-commitment (G3-076, G3-077); wages not responding.
- By now: guidance toward October — not seen.
- p = 0.55 (low).

### Q-0020 — Bank of Russia cuts at 23.10
- Reference class: after a pause with an upside inflation surprise, the CBR has usually held at the next meeting; guidance (avg 13.7–14% for the rest of 2026) still allows one cut.
- YES: guidance range allows a cut; growth ½% (G3-068); "key" meeting with new forecast (G3-066).
- NO: inflation 7.1–7.2% above the 6–7% range (G3-067); budget deficit doubled, rouble weaker after ×5 FX purchases (G3-016, G3-020).
- By now: a dovish signal from Nabiullina/Zabotkin — not seen (no direction).
- p = 0.22 (low).

### Q-0088 — Bank of Russia raises at 23.10
- Reference class: the CBR reverses a cutting cycle only on clear overheating or currency crisis; rare.
- YES: inflation above forecast; pro-inflation scenario judged more likely (G3-065).
- NO: Zabotkin: draft budget fits July assumptions (G3-066); rouble 85.7 is not a crisis.
- By now: hawkish warnings — not seen.
- p = 0.06 (medium).

### Q-0066 — FOMC hikes at 27–28.10
- Reference class: minutes "another increase by year end" leave two meetings (X, XII); in a slow hiking cycle the next move tends to come at alternate meetings; weak data shifts it later.
- YES: "most participants" favour another hike (G3-033); energy-driven upside risks.
- NO: payrolls +29k with revisions −60k (G3-034); 10Y at 5.3% tightening; Trump pressure for low rates (G3-078).
- By now: Fed speakers pointing to October — not in the facts.
- p = 0.32 (low).

### Q-0070 — Fitch or S&P cut Poland below A− by 31.03.2027
- Reference class: sovereign negative outlooks resolve in a downgrade within the next review cycle about 30–35% of the time; Fitch A− negative (affirmed twice), next review ~II 2027 inside the horizon; S&P would normally move to negative first.
- YES: deficit ~7%, Moody's cut on 18.09 (G3-049); Fiscal Council dispute (G3-046).
- NO: GDP forecasts raised (G3-048); Fitch affirmed at the last review.
- By now: n/a.
- p = 0.27 (low).

### Q-0105 — S&P downgrade or negative outlook in its 06.11 decision
- Reference class: S&P changes rating or outlook at roughly 15–20% of scheduled reviews; elevated when peers move and its own deficit forecast rises.
- YES: S&P raised its 2026 deficit forecast to 7.0% (G3-049); Moody's cut, Fitch negative.
- NO: growth forecasts raised; S&P affirmed in V.
- By now: n/a.
- p = 0.33 (low).

### Q-0086 — NBP EUR/PLN on 21.10 > 4.4000
- 4.3797 on 07.10, window range 4.3588–4.3900; needs +0.46% in 10 trading days; 10-day sd ≈ 1.0% → ≈ 0.32.
- YES: global risk aversion, UST10Y highs (G3-035); fiscal noise.
- NO: EUR/PLN stable through the window despite USD strength.
- By now: n/a.
- p = 0.30 (medium).

### Q-0075 — GUS flash CPI October < 3.5% y/y
- Mechanics: September 4.0%; CPN cut pump prices by about 1.3–1.4 PLN/l (−15%) from 03.10; fuel weight ≈ 6% → about −0.8 pp; other components roughly at last year's monthly pace → ≈ 3.1–3.4%.
- YES: price cut in force for the whole month (G2-026, G2-027).
- NO: "regulatory decisions on energy prices" flagged as risk (G3-040); food momentum (G2-036).
- By now: n/a.
- p = 0.62 (low).

### Q-0112 — Fed restricts HKMA FIMA access by 31.03.2027
- Reference class: no precedent of the Fed restricting a central bank's FIMA access on political grounds; congressional letters rarely change Fed facilities.
- YES: Moolenaar letter, Fed will respond (G3-064).
- NO: US–China truce; HKMA has not used the facility since 2020.
- By now: n/a.
- p = 0.04 (medium).

### Q-0018 — OFAC lists a mainland PRC bank (Iran/Russia) by 31.03.2027
- Reference class: OFAC has almost never placed a mainland bank on the SDN list; it targets refiners, terminals and HK/front firms (G3-026). Base ≈ 2–3% per quarter.
- YES: H.R. 5334 mandate; Iran maximum pressure.
- NO: truce to 10.01.2027 with the extension sought; designations so far stop at HK/PRC trading firms.
- By now: n/a.
- p = 0.05 (medium).

Batch 3 log: questions 11; searches 0; consistency check done.

---

## Batch 4 — RU_SANCTIONS_US, RU_SANCTIONS_EU, UA_FUNDING, US_EU_TRADE, US_CHINA_TRADE (10 questions)

### Q-0012 — Tariff under H.R. 5334 on a non-Russian country, effective by 31.12
- Reference class: mandatory third-country sanctions laws (CAATSA s.231, ISA) — executives usually delay, waive or comply minimally; timely compliance ≈ 20–30%. Precedent the other way: the 25% India "Russian oil" tariff of VIII 2025.
- YES: "shall" with any rate "up to" 100% satisfying the law (G3-001); Greer "will name names"; India talks deadlocked (G3-005).
- NO: no 10-day notice by 07.10 (G3-001 calendar); China truce excludes the biggest buyer (G3-010); Trump weighing sanctions relief (G3-002).
- By now: a USTR determination naming "countries described" — not seen.
- p = 0.22 (low).

### Q-0090 — Sec. 112 duty on Russian goods by an act published 08–21.10
- Same reference class; the 30-day deadline 18.10 is inside the window, but a duty on Russian uranium and fertiliser imports has domestic cost, and a bilateral channel with economic offers is open (G4-020).
- YES: legal mandate; congressional pressure (G3-006).
- NO: Wright: Trump "leaves every decision till the end" (G3-003); no notice; Lukoil talks.
- By now: a draft proclamation or leak — not seen.
- p = 0.18 (low).

### Q-0091 — OFAC adds a RUSSIA-EO14024 or H.R. 5334 SDN entry 08–21.10
- Reference class: under this administration Russia-programme designations have been infrequent (none 24.09–07.10, G3-026); H.R. 5334 Sec. 103 requires bank sanctions by 18.10, which may be met by existing listings or a waiver.
- YES: Sec. 103 deadline inside the window (G3-001); tagging under the new act would count.
- NO: bilateral channel and sanctions-relief deliberations (G3-002, G4-020); main banks already listed.
- By now: OFAC Russia activity in IX–X — not seen.
- p = 0.28 (low).

### Q-0019 — Council adopts a package named "22nd package" by 31.12
- Reference class: EU Russia packages arrive every 3–5 months and slip 1–2 months from the first target; Ukraine's envoy gives XI as realistic (G3-024). 12 weeks left → ≈ 0.6.
- YES: Hungary in a cooperative phase (veto on clusters lifted, G4-028); the listings track may itself be labelled 22nd by the Council (G3-023).
- NO: sectoral bans (fertiliser, metals) divide member states; Euronews does not number the listings (G3-022).
- By now: a Commission proposal for the sectoral package — not reported.
- p = 0.60 (low).

### Q-0083 — Council formally adopts ≥ 1,500 new Russia listings by 21.10
- Reference class: Coreper-agreed sanctions acts are adopted by the Council within days in the overwhelming majority of cases.
- YES: Coreper agreement 07.10 on 1,646 names, adoption scheduled at the FAC (G3-022).
- NO: last-minute block by a member state; count falling below 1,500 if the 77 Duma candidates are moved (still above 1,500).
- By now: adoption date set — seen.
- p = 0.92 (high).

### Q-0104 — Russia sanctions act with a new trade prohibition by 30.11
- Requires the sectoral 22nd package (or another act adding goods) by 30.11; envoy says November "more realistic", October theoretical; packages slip.
- YES: Ukrainian proposals for fertiliser and metal bans (G3-024).
- NO: slippage base rate; listings-only acts do not count.
- By now: a package text circulated — not reported.
- p = 0.33 (low).

### Q-0071 — Council act allowing use of Bank of Russia assets for Ukraine by 30.06.2027
- Reference class: the reparations-loan route failed in XII 2025 (Belgian opposition) and the EU chose joint borrowing (90 bn EUR); re-opening within ~9 months has a low base rate.
- YES: Ukraine's 2027 gap ≈ 15% of GDP and 32.6 bn USD uncovered (G3-054); refusal to front-load the loan (G3-053).
- NO: the legal and Belgian objections are unchanged; the joint loan covers 2027 in part.
- By now: Commission proposal to revive the assets route — not seen.
- p = 0.13 (low).

### Q-0015 — US tariff on EU goods above the 15% ceiling by 31.03.2027
- Reference class: since the 2025 framework the US has not breached the ceiling for ~15 months; per-quarter hazard ≈ 5–8% in friction periods.
- YES: diesel pressure on Europe (G2-008); EU deadline on steel derivatives (G3-058).
- NO: no new act in the window (G3-058); trade deal treated as a model.
- By now: a USTR threat naming the EU — not seen.
- p = 0.12 (medium).

### Q-0077 — US and PRC both announce extension beyond 10.01.2027 by 10.01.2027
- Reference class: every expiry of the 2025–26 truce so far has been extended before lapse, by announcements from both sides (latest: Bessent 23.09, MOFCOM 28.09).
- YES: both sides committed to seek an extension "through high-level interaction before year-end" (G3-010); APEC Shenzhen with mutual attendance (G3-008).
- NO: extensions are getting shorter (two months); rare-earth deliveries at two-thirds of commitments (G2-041); risk of a one-sided or late announcement.
- By now: n/a.
- p = 0.72 (medium).

### Q-0108 — US and PRC both put 30-for-30 tariff cuts into effect by 31.12
- Reference class: US tariff reductions requiring notice and comment take several months; announcements without a start date rarely take effect within a quarter.
- YES: China can act quickly; both sides want deliverables for APEC.
- NO: Greer: no timeline, legal process with public comment (G3-063).
- By now: a Federal Register notice opening comment — not seen.
- p = 0.08 (medium).

Batch 4 log: questions 10; searches 0; consistency check done.

---

## Batch 5 — CN_RARE_EARTHS, US_CHINA_TECH, TAIWAN, US_CHINA_SUMMITS (12 questions)

### Q-0021 — PRC announces extension/repeal of the rare-earth suspension by 10.11
- Reference class: China has formalised each truce step with MOFCOM/GAC or Tariff Commission announcements just before the legal date (e.g. 07.11.2025 for 10.11.2025); a lapse would contradict its own 28.09 readout extending "related Chinese export controls" to 10.01.2027 (G3-010).
- YES: MOFCOM readout covers related export controls (G3-010); high-level contact planned before year-end.
- NO: readout omits rare earths by name (G2-040); leverage motive to keep the date open (G2-041).
- By now: n/a (China publishes close to the deadline).
- p = 0.78 (medium).

### Q-0022 — PRC announces extension/repeal of the Ga/Ge/Sb suspension by 27.11
- Same reference class; the Ga/Ge/Sb suspension was issued in the same 2025 package; slightly less tied to the US 50% rule than the rare-earth suspension.
- YES: package logic; deadline after APEC gives a natural deliverable.
- NO: not named in the readout; China may let a less central measure lapse.
- By now: n/a.
- p = 0.72 (medium).

### Q-0089 — MOFCOM extension published 08–21.10
- Timing base rate: MOFCOM publishes 3–5 days before the legal date; publication a month early is uncommon.
- YES: Šefčovič and US contacts could prompt early clarity.
- NO: legal date 10.11; no sign of early drafting.
- By now: n/a.
- p = 0.12 (medium).

### Q-0023 — MOFCOM lists a US entity (export control list or UEL) 24.09–31.12
- Reference class: MOFCOM listed US entities many times in 2025 and once in 2026 during the truce (22.06, G3-032); typical trigger: US arms sales to Taiwan. Quarterly rate ≈ 0.4–0.5, lowered by the summit cycle.
- YES: F-16V deliveries and House members in Taiwan (G1-054, G4-078); listings happened even during the truce.
- NO: truce extension and APEC hosting; no listing since 22.06.
- By now: n/a.
- p = 0.38 (low).

### Q-0024 — US permits Blackwell-class exports to the PRC by 31.12
- Reference class: the administration licensed H200 but repeatedly declined Blackwell; a change would need a summit deliverable.
- YES: AI dialogue and APEC in Shenzhen (G3-008); transactional approach.
- NO: no change through the summit (G2-047); smuggling enforcement (G2-046); congressional resistance.
- By now: a reported offer — not seen.
- p = 0.10 (medium).

### Q-0025 — PRC magnet exports to the US in IX > 512 t
- Reference class: month-on-month changes in this series are about 50/50; August was a pre-summit dip (ed.01), so mean reversion in the summit month tilts up.
- YES: summit month, coal and Board-of-Trade goodwill (G3-008).
- NO: China meets only about two-thirds of delivery commitments (G2-041).
- By now: n/a.
- p = 0.55 (low).

### Q-0102 — BIS FR document extending the Affiliates rule suspension by 09.11
- Reference class: agreed truce steps are usually formalised by the US near the deadline; risk is publication on or after the expiry day.
- YES: practitioners expect it (G2-045); trade groups pressing on the parallel s.301 notice (G3-011).
- NO: no notice yet; US formalisation of the 23.09 deal is lagging (G3-011).
- By now: an FR public-inspection entry — not seen (normal at this distance).
- p = 0.68 (low).

### Q-0005 — Named PLA exercise around Taiwan by 31.03.2027
- Reference class: named exercises 2024–2025 ≈ 2 a year (Joint Sword 2024A/B, Strait Thunder 2025A, a December 2025 exercise) → ≈ 0.17/month → 1 − 0.83^5.8 ≈ 0.66; détente after two state visits lowers it.
- YES: triggers ahead (National Day speech, arms sales, House visits; G4-078); historic frequency.
- NO: summit cycle and truce (G4-076); no named exercise in 2026 so far per facts.
- By now: n/a.
- p = 0.40 (low).

### Q-0069 — DSCA notifications for Taiwan ≥ 1 bn USD by 31.12
- Reference class: ≥ 1 bn USD packages notified a few times a year, often in December; deferred around summits.
- YES: post-APEC December window; congressional pressure.
- NO: Trump avoids friction during the truce; F-16V delivery already absorbs attention.
- By now: n/a.
- p = 0.25 (low).

### Q-0087 — Taiwan MND reports ≥ 30 PLA aircraft in one daily report 08–21.10
- Reference class: in 2024–25, days with ≥ 30 aircraft occurred several times a month; since the summit the peak is 23 (01.10), other days 2–14.
- YES: National Day 10.10 traditionally draws a surge; joint combat-readiness patrols recur.
- NO: summit-cycle quiet (G1-053); pressure moved to Scarborough (G1-055).
- By now: one day above 20 — seen (23 on 01.10).
- p = 0.30 (low).

### Q-0029 — Trump personally attends the APEC leaders' meeting in Shenzhen
- Reference class: when the White House pre-announces "mutual attendance", attendance is likely (~0.8); but in Busan 2025 Trump met Xi and left before the leaders' meeting itself, which this question requires.
- YES: White House fact sheet (G3-008); truce extension needs high-level interaction (G3-010).
- NO: Busan precedent; possible Iran escalation after 03.11; FT: part of APEC moved online (G4-077).
- By now: travel planning — not reported.
- p = 0.60 (low).

### Q-0100 — Putin personally attends APEC in Shenzhen
- Reference class: Putin attends APEC when hosted by close partners (Beijing 2014, Da Nang 2017) and skips in the West; PRC MFA "welcomes Putin's attendance" (G4-027).
- YES: host China; Kremlin floats a Putin–Trump–Xi meeting.
- NO: part of the summit possibly online (G4-077); war events.
- By now: China's welcome — seen.
- p = 0.75 (medium).

Batch 5 log: questions 12; searches 0; consistency check done.

---

## Batch 6 — RU_MOBILIZATION, UA_FRONT, UA_TALKS, EASTERN_FLANK, BLACK_SEA, BALTIC_INFRA, UA_EU (14 questions)

### Q-0001 — Russian mobilisation decree by 31.12
- Reference class: one mobilisation (IX 2022) in four years of war, under front collapse; ≈ 5% a quarter.
- YES: Ukrainian local gains (G1-045); Duma elections over (G4-040).
- NO: contract recruitment financed by a defence budget +27% (G3-015); no front collapse.
- By now: legal or rhetorical preparation — not seen.
- p = 0.04 (medium).

### Q-0002 — Person killed on NATO territory by a Russian drone/missile (government attribution) by 31.12
- Reference class: no government-attributed Russian-caused death on NATO territory since 2022 (Przewodów was Ukrainian); ≈ 2% a quarter, raised by the new Black Sea campaign near NATO waters.
- YES: ships hit in RO/BG EEZs with deaths (G1-031, G1-032); drones over Moldova (G1-034).
- NO: EEZ is not territory; governments avoid attribution (G1-031).
- By now: an attributed incident — not seen.
- p = 0.05 (medium).

### Q-0004 — DeepState net Russian gain in October > 200 km²
- Base: VII 63, VIII 124, IX 154 (revised from 66) — none above 200; first publications are lower than revisions; 270–320 km² of Ukrainian gains are held back (G1-043).
- YES: upward trend; heavy fighting at Kostiantynivka/Pokrovsk (G1-046).
- NO: Vivaldi counteroffensive (G1-045); release of withheld Ukrainian gains would cut the net.
- By now: n/a.
- p = 0.12 (medium).

### Q-0026 — Trilateral US–UA–RU meeting by 30.11
- Reference class: the trilateral format met in bursts in 2026 and was "halted" around the Duma elections; restart within 7–8 weeks after an explicit Russian "no current plans" ≈ 0.2–0.3.
- YES: US proposal for a technical trilateral by end-X (G4-021); bilateral US–Russia channel active (G4-020).
- NO: Ryabkov/Lavrov 07.10 (G4-022); Putin's preconditions (G4-019).
- By now: Russian agreement in principle — not seen.
- p = 0.22 (low).

### Q-0082 — Trilateral meeting 08–31.10
- Same class, 3.5 weeks, after a public Russian refusal.
- YES: US deadline "by end of October".
- NO: Moscow: "does not depend on us"; retaliation strikes (G4-023).
- By now: date and venue — not seen.
- p = 0.08 (medium).

### Q-0030 — Putin and Trump meet in person by 31.03.2027
- Reference class: one meeting (Anchorage 2025) and one cancelled (Budapest) in ~20 months; main path now APEC Shenzhen if both attend (≈ 0.75 × 0.60, correlated) and they meet there (≈ 0.7), plus other summits.
- YES: Kremlin floats Putin–Trump–Xi (G4-027); APEC attendance signals.
- NO: Trump may avoid Putin without a Ukraine deliverable; Busan precedent of a short visit.
- By now: n/a.
- p = 0.38 (low).

### Q-0110 — Full ceasefire signed and confirmed by both by 30.06.2027
- Reference class: four years of failed ceasefire efforts; annual hazard ≈ 15% → ≈ 0.11 over 8.7 months.
- YES: US proposals and economic channel (G4-019, G4-020).
- NO: Putin's terms (Donbas, neutrality) unchanged; defence budget up for 2027.
- By now: n/a.
- p = 0.10 (medium).

### Q-0073 — ISW: whole of Kramatorsk or Sloviansk under Russian control by 30.06.2027
- Reference class: Russian capture of a large fortified city takes many months after reaching it; Russia has not yet taken Kostiantynivka, which lies before Druzhkivka and Kramatorsk.
- YES: pressure in Donetsk persists (G1-046).
- NO: pace 60–150 km²/month (G1-043); Vivaldi stopped the push toward the Sloviansk–Kramatorsk rear (G1-045).
- By now: n/a.
- p = 0.05 (medium).

### Q-0113 — ISW: whole of Kostiantynivka under Russian control by 31.03.2027
- Reference class: sieges of mid-size Donbas towns lasted 5–15 months (Avdiivka ≈ 5, Bakhmut ≈ 10, Pokrovsk longer); Kostiantynivka has been contested for over a year; ISW requires whole-town control.
- YES: heaviest fighting near Kostiantynivka (G1-046).
- NO: slow pace and Ukrainian counterattacks (G1-044, G1-045).
- By now: n/a.
- p = 0.28 (low).

### Q-0027 — Article 4 request 24.09–31.12
- Reference class: Art. 4 invoked in II 2022 and twice in IX 2025, after airspace incursions; ≈ 10–15% a quarter in high-incident periods. 12 weeks left.
- YES: ships sunk in RO/BG EEZs, Kaliningrad nuclear note (G1-031, G1-032, G1-029).
- NO: no request after the 05–06.10 incidents (G1-036); states respond nationally (G1-026, G1-027).
- By now: a request after the EEZ incidents — not seen.
- p = 0.13 (medium).

### Q-0097 — Confirmed RU/BY violation of Polish airspace 08.10–31.12
- Reference class: confirmed violations in 2025–26 came every few months (drones in IX 2025, Mi-8 23.09.2026); 12 weeks → ≈ 0.4–0.5.
- YES: Russian strikes near the border continue; helicopter and drone probing pattern (G1-024).
- NO: two quiet weeks (G1-025); air-defence build-up (G1-026).
- By now: n/a.
- p = 0.45 (low).

### Q-0098 — RO/BG/TR confirm a merchant ship hit by drone/missile in their waters/EEZ 08.10–31.12
- Reference class: Russia's declared campaign against ships serving Ukraine (G1-033) and Ukraine's naval-drone strikes on shadow-fleet tankers (G1-050; Turkish EEZ cases in 2025) both run through these EEZs; two such incidents in two days at the start of X.
- YES: Putin refuses to halt Black Sea strikes (G1-051); Bulgaria already named drones (G1-032).
- NO: possible Russian route adjustment after Western protests; authorities may not state the cause (Romania did not, G1-031).
- By now: campaign active — seen.
- p = 0.65 (low).

### Q-0040 — Baltic cable/pipeline damage with external-action investigation by 31.03.2027
- Reference class: every winter since 2023 had at least one such case (Balticconnector X 2023, cables XI 2024, Estlink 2 XII 2024, I 2025, XII 2025); the horizon covers a full winter.
- YES: shadow-fleet traffic and heightened tension (G3-029).
- NO: stronger NATO patrols since 2025 (Baltic Sentry).
- By now: n/a.
- p = 0.65 (medium).

### Q-0101 — EU formally opens cluster 2 or 3 with Ukraine by 31.12
- Reference class: once a veto is lifted, clusters are usually opened at the next intergovernmental conference (often December), but conditions can delay; here the next step depends on Ukraine's minority-rights law.
- YES: Hungary lifted its veto 07.10 (G4-028); Commission enlargement roadmap (G4-082).
- NO: common position pending the Rada law; Hungarian conditionality.
- By now: Rada scheduling the law — not reported.
- p = 0.50 (low).

Batch 6 log: questions 14; searches 0; consistency check done.

---

## Batch 7 — US_EUROPE, US_ELECTIONS, foreign elections, IRAN_LEADERSHIP, VENEZUELA, SAHEL, CAUCASUS, GREENLAND, PANAMA (15 questions)

### Q-0003 — Official decision to cut US troops in Europe by ≥ 10,000 by 31.03.2027
- Reference class: this administration has signalled large cuts for over a year, while announced decisions so far were smaller (brigade-level); review end now XII, options 25–40k (G1-038).
- YES: Hegseth: shift to the Western Hemisphere (G1-038); FY2026 floor funds expired (G1-041).
- NO: NDAA FY2027 may add a floor (Q-0109); new rotations to Lithuania and a Polish base (G1-037, G1-039).
- By now: review end on schedule — moved later.
- p = 0.28 (low).

### Q-0109 — FY2027 NDAA with a EUCOM floor enacted by 31.12
- Reference class: NDAAs were signed by 31.12 in most recent years (XII 2019, 2021, 2023, 2024, 2025; I 2021 by override) ≈ 0.8; the FY2026 law had a 76k floor and the SASC draft adds a check (G1-041) ≈ 0.85 conditional.
- YES: annual must-pass record; bipartisan support for European posture.
- NO: lame-duck session after a wave election; final text not confirmed.
- By now: conference progress — not observable in the facts.
- p = 0.66 (low).

### Q-0114 — Official naming of a new permanent US Army base location in Poland by 31.03.2027
- Reference class: "Fort Trump" proposals since 2018 have not produced a named base; current guidance: decision not before XII (G1-037).
- YES: Trump "I think so"; special law drafted; candidates shortlisted (G4-050).
- NO: domestic political dispute in Poland (G4-049); posture review may cut overall presence.
- By now: a US statement naming a site — not seen.
- p = 0.22 (low).

### Q-0031 — Republicans win ≥ 218 House seats on 03.11
- Reference class: the president's party loses House seats in nearly every midterm; with approval near 32% (G4-045) and a narrow GOP majority, holding is rare (2002 under a popular president is the exception).
- YES: mid-decade redistricting gains; payment promises (G4-046).
- NO: approval 32%, generic ballot D+7 (C/3), fuel and rate pain.
- By now: n/a.
- p = 0.07 (medium).

### Q-0095 — Republicans hold ≥ 50 Senate seats
- Reference class: from 53 seats the GOP must lose four; in wave years with presidential approval below 40% (2006) the out-party gained six, but the 2026 map favours Republicans.
- YES: favourable map; 50–50 counts as YES.
- NO: record-low approval, energy shock.
- By now: n/a.
- p = 0.50 (low).

### Q-0033 — Lula wins the presidency (runoff 25.10)
- Reference class: first-round leaders win runoffs in about 70–75% of cases; Bolsonaro led by 1.9 pp and gained endorsements from eliminated right-wing candidates (G4-029, G4-030); polls underestimated him.
- YES: incumbency; Lula's 2022 comeback.
- NO: endorsements; Trump's support (G4-031).
- By now: post-round poll — not available before cutoff.
- p = 0.25 (medium).

### Q-0093 — Iotova > 50% of valid votes in round one (25.10)
- Polls among intending voters 41.4% and 44.5%; with ≈ 10% undecided redistributed proportionally ≈ 46–50%; Radev in 2021 fell just short (49.4%). GERB fielding no candidate helps.
- YES: rising trend; fragmented opposition.
- NO: 27 tickets; Gyurov 26%; "I support no one" option counts against the share.
- By now: n/a.
- p = 0.38 (low).

### Q-0094 — Likud wins strictly the most Knesset seats (27.10)
- Five-poll average Likud 23 vs Yashar 22.2, latest Channel 12 Yashar 23 vs Likud 21 (G4-034); seat ties count NO.
- YES: Likud has usually matched or beaten final polls.
- NO: latest poll behind; ties.
- By now: n/a.
- p = 0.42 (low).

### Q-0032 — New video/audio of Mojtaba Khamenei by 31.12
- Reference class: no audio or video since he took office; only written messages (G4-012); persistence suggests a low hazard.
- YES: legitimacy needs during the mandate dispute.
- NO: security or health reasons behind the absence are unchanged.
- By now: any appearance — not seen.
- p = 0.12 (medium).

### Q-0096 — Araghchi ceases to be foreign minister by 31.12
- Reference class: Majlis impeachments of ministers do succeed (e.g. economy minister 2025), but most motions stall in the presidium; ≈ 0.15–0.2 over 12 weeks given an open dispute.
- YES: impeachment motion registered, hardliners active (G4-009, G4-011).
- NO: not on the agenda; senior officials say the mission was authorised (G4-010).
- By now: referral to the floor — not seen.
- p = 0.17 (low).

### Q-0034 — Venezuela announces a presidential election date by 31.03.2027
- Reference class: transitional authorities set dates after institutional renewal; opposition targets TSJ XI and CNE XII, civil society proposes July 2027 (G4-066).
- YES: US-backed dialogue; promise at the UN (G4-065).
- NO: no calendar after a year of promises; renewal can slip.
- By now: CNE renewal on track — partly (AN commission named).
- p = 0.35 (low).

### Q-0035 — Goïta ceases to hold power by 31.03.2027
- Reference class: Sahel junta leaders face an annual removal hazard ≈ 10%; Kidal retaken strengthens him (G4-060).
- YES: JNIM pressure on Bamako.
- NO: recent military gain; Russian support.
- By now: n/a.
- p = 0.05 (medium).

### Q-0072 — Armenia and Azerbaijan sign a peace treaty by 30.06.2027
- Reference class: text initialled in 2025; Azerbaijan conditions signature on Armenian constitutional change, which needs a referendum; such sequences take years.
- YES: TRIPP diplomacy (G4-071).
- NO: detained-soldier dispute (G4-072); no referendum date.
- By now: referendum scheduling — not seen.
- p = 0.15 (low).

### Q-0111 — Greenland defence agreement in force by 30.06.2027
- Reference class: US defence agreements with Denmark have taken 1–1.5 years from signature to entry into force; this one needs both parliaments and has no timetable (G4-054).
- YES: governments in Nuuk and Copenhagen support it; US presents it as a model (G4-056).
- NO: Naleraq opposition (G4-055); no vote scheduled.
- By now: committee timetable — not seen.
- p = 0.38 (low).

### Q-0039 — Panama Canal limit above 32 in force by 31.10
- ACP advisory of 28.09: 33 slots from 15.10 (G1-061); advisories are occasionally revised for water levels.
- YES: advisory issued.
- NO: drought revision before 15.10.
- By now: advisory in place — seen.
- p = 0.88 (high).

Batch 7 log: questions 15; searches 0; consistency check done.

---

## Summary

- Questions forecast: 88 of 88. Searches: 0 (no web in replay). Post-cutoff facts seen in the inputs: 6 (not used).
- p range 0.02–0.92, mean 0.324 over 88 questions. The prompt warns of under-forecasting (editions 01–02: mean forecast 0.42 vs YES rate 0.58); each p here was set from the base rate and the listed evidence, not moved toward the status quo by default. The low mean reflects many questions about specific events in short windows. A reviewer should still compare it with the realised YES rate.
- Lens B kept base rates explicit and adjusted cautiously; where the base rate is a market barrier probability, the volatility assumption is stated.
- Provenance: `stage-start R` was not recorded when the run began; it was recorded at the end with a note saying so, followed by `stage-end R` (reviews/learning/provenance.jsonl).
- Possibly contaminated questions: none (training cutoff June 2026, before every event in scope).
