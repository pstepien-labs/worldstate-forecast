# Edition 02 — plan (stage 00)

Stage 00 run on 08.10.2026 (00:29–) for the state date 07.10.2026. Facts below carry date and source; items marked ASSESSMENT are judgements. This file contains no probabilities.

## 1. Edition parameters and versions

| Parameter | Value |
|---|---|
| NR | 02 |
| STATE_DATE | 07.10.2026 |
| PERIOD_FROM | 23.09.2026 (state date of edition 01) |
| DIRECTORY | `editions/2026-10-07_edition-02` |
| PREVIOUS | `editions/2026-09-23_edition-01` |
| PREV_TAG | `wydanie-01` (commit f43c370, "wydanie-01 etap-08") |
| REGISTRY_BASELINE | `5669790f9de6fed150b2d8ae2bb7023d911c8f9c` (English migration 2/3 — the baseline named for edition 02 in `methodology/methodology_changes.md`, code-mapping section) |
| Methodology | v1.0 (frozen) |
| Next edition (earliest, +14 days) | 21.10.2026 |

Output of `python3 tools/pipeline.py versions` at the start of the stage (before the stage H commit):

```
framework_version 1.4.0 · methodology_version v1.0 · harvester_version 1.4.0
commit ba3a61d4ced1 · branch main · dirty_files 2 (CURRENT.md and the new edition directory)
edition 02 · claude_cli 2.1.293 (Claude Code)
```

Model: claude-opus-5-5. After the stage H commit the same command reports commit 85a4f7fc8656, dirty_files 0; versions unchanged.

**Previous edition closed — manual verification.** `python3 tools/pipeline.py status` reported edition 01 as not closed. Verified by hand on 08.10.2026: tag `wydanie-01` exists and points to f43c370 ("wydanie-01 etap-08"); `editions/2026-09-23_edition-01/08_quality_control.md` exists; `registry/editions.csv` holds the edition 01 row (report_commit f43c370, tag wydanie-01). The status output is caused by a detection bug in `tools/pipeline.py` (see §8 and `log.md`). The user approved continuing without changing the tool.

## 2. Harvest window actually covered and its gaps

Stage H (mode digest) was run inside this stage; details in `02_harvest/harvest_notes.md`.

- Window 23.09–07.10.2026: 19,077 items (8,336 matched to concepts), 47 languages, 102–103 countries, Western share 30%.
- **Gap — late start.** Live collection began on 05.10.2026 10:52 UTC. About 70% of items are dated 05–07.10, about 22% 02–04.10 and only about 8% 23.09–01.10 (GDELT and feed back-fill). Stage 02 must cover 23.09–01.10 mainly with web search.
- Sources at the state date: 202 enabled — 157 ok, 31 throttled, 3 retrying, 2 failing (ISW HTTP 403; Saba HTTP 403), 9 skipped (AGSI, EIA and FIRMS API keys not set; 2 robots.txt).
- Flagged concepts (mandatory targeted searches): Poland security ⚠<3 lang (G1, G4); Poland fuels ⚠W>80% ⚠<3 lang (G2); Arctic and Greenland ⚠<3 lang (G4).
- Silent required cells: NATO official, Saudi Arabia official, Japan official, Turkey Western, Greenland independent.
- Not covered by harvested primary data: TTF, EU/PL gas storage, Polish fuel prices, NBP rate, ISW assessments; PortWatch series has no rows for 28.09–02.10; OFAC diffs start only on 05.10.

## 3. Questions to resolve in stage 01

Registry: 73 questions, all ACTIVE. Values from the harvest are taken from `02_harvest/indicators.md`; values from web searches in this stage are leads for stage 01, which must open the named resolution source.

### 3.1 Deadline ≤ 07.10.2026 (26 questions)

| ID | Deadline | Resolution source | Harvested value / lead found in stage 00 |
|---|---|---|---|
| Q-0006 | 06.10 | ICE Brent settlement | No ICE settlement in the harvest. FRED Brent spot ends 29.09. Lead: Trading Economics shows the prior session near 100.6 USD and Fortune about 101.4 USD intraday on 06.10, so the value sits close to the threshold — the ICE settlement is needed |
| Q-0013 | 30.09 | stat.gov.pl flash CPI IX | Lead: MPC statement of 07.10 (via Polish media) cites CPI IX 2026 at 4.0% y/y — confirm on stat.gov.pl |
| Q-0037 | 07.10 | PortWatch daily Hormuz | Harvested daily totals 24.09–27.09: 5, 3, 4, 1; 03.10: 2; 04.10: 4. **No rows for 28.09–02.10 and 05–07.10** — check on portwatch.imf.org |
| Q-0041 | 07.10 | CENTCOM / Pentagon | Lead: reports (CBS, Fox, 03–04.10) of Pentagon military options for "after the elections"; no strike announcement found — check centcom.mil |
| Q-0042 | 07.10 | state.gov, mfa.ir, Qatar MFA | Leads: US News/Reuters 24.09 (discussion of a phased deal); Iran says replies go through mediators (Al Jazeera 04.10); Trump expected talks to resume (CBS) — establish whether a round took place 24.09–07.10 |
| Q-0043 | 07.10 | SPA, coalition | Leads: Houthi claims of strikes on Riyadh airport and Aramco facilities (CFR tracker, 05.10); Saudi authorities did not confirm — check spa.gov.sa |
| Q-0044 | 07.10 | US/PL governments | No announcement of a location found (Trump 17.09: "will be announced very soon" if it happens) |
| Q-0045 | 07.10 | DO RSZ, MON | Mi-8 helicopter violated Polish airspace near Braniewo on **23.09.2026** (Notes from Poland, 23.09) — one day before the window 24.09–07.10; check DO RSZ for incidents in the window |
| Q-0046 | 07.10 | JCS, mod.go.jp | Not checked (JP official cell silent in harvest) |
| Q-0047 | 07.10 | mnd.gov.tw | Not checked; MND daily reports available to 05.10 |
| Q-0048 | 06.10 | ICE Endex TTF | Leads disagree: Investing.com 75.49 EUR/MWh close 06.10; EnergyRiskIQ 73.70 (05.10?) — ICE Endex settlement needed (threshold 75.00) |
| Q-0049 | 06.10 | agsi.gie.eu | AGSI not harvested (no key). Lead: EnergyRiskIQ 72.7% (date unclear) vs threshold 73.0% — read AGSI+ directly |
| Q-0050 | 07.10 | e-petrol weekly | Not harvested |
| Q-0051 | 07.10 | opec.org | The seven countries met on 04.10.2026 and kept September required production for November (opec.org press release 04.10; CNBC 04.10) |
| Q-0052 | 07.10 | api.nbp.pl | **Harvested: EUR/PLN 4.3797 (NBP table A, 07.10.2026)** |
| Q-0053 | 07.10 | sozd.duma.gov.ru, minfin.gov.ru | Draft 2027–2029 budget submitted to the Duma on 30.09.2026 (Rossiyskaya Gazeta 30.09); spending 48.8 trn RUB, revenue 43.3 trn RUB (RG/Interfax 01.10) — deficit as % of GDP to be read from the explanatory note |
| Q-0054 | 30.09 | cikrf.ru | Final CEC result for A Just Russia — check (edition 01: disputed 5.00% vs 5.13% partial counts) |
| Q-0056 | 05.10 | tse.jus.br | First round 04.10: Lula 45.16% of valid votes, Flávio Bolsonaro 47.03%; runoff 25.10 (TSE final figures via Al Jazeera, AS/COA, NPR) |
| Q-0057 | 07.10 | ustr.gov, whitehouse.gov | Not checked |
| Q-0058 | 07.10 | whitehouse.gov, mofcom.gov.cn | Lead: Bessent announced on **23.09.2026** an extension of the trade truce to 10.01.2027 (NBC News); summit 24.09 — dates of each government's announcement matter (window and creation date 23.09) |
| Q-0059 | 07.10 | kremlin.ru, president.gov.ua | No agreement found; US pushing an energy ceasefire (Axios 24.09; Kyiv Independent 04.10) |
| Q-0060 | 07.10 | OFAC recent actions | Harvest: 19 SDN rows added on 06.10 (diff vs 05.10 snapshot); additions 24.09–05.10 not captured — read OFAC recent actions |
| Q-0061 | 07.10 | OFAC recent actions | As Q-0060 |
| Q-0062 | 07.10 | UKMTO/JMIC | No ship attack in the window found in a headline search (last confirmed: Amzan, 24.08) — check UKMTO |
| Q-0063 | 07.10 | UKMTO/JMIC | Not checked |
| Q-0064 | 07.10 | president.gov.ua, defense.gov | Not checked |

### 3.2 Later deadline, but the event may already have occurred

| ID | Deadline | Signal found in stage 00 |
|---|---|---|
| Q-0014 | 09.10 | FAO released the September FFPI on 02.10.2026: 136.0 points (FAO via Global Agriculture, IndexBox) — threshold 133.3; confirm on fao.org |
| Q-0055 | 10.10 | Saeima election 03.10: United List first with 41 or 42 of 100 seats (CVK preliminary via Euronews, Kyiv Independent, BNN 04.10) — no other list close; confirm on cvk.lv |
| Q-0011 | 10.11 | Truce extended to 10.01.2027 (Bessent 23.09.2026, NBC; CalChamber 06.10: Federal Register notice still pending) — check the PRC announcement and the timing relative to the creation date 23.09 |
| Q-0021 | 10.11 | Suspension of the 09.10.2025 rare-earth controls reported as extended to 10.01.2027 together with the truce (Brookings, CSIS) — check MOFCOM |
| Q-0022 | 27.11 | Check whether the Ga/Ge/Sb suspension was extended at the same time |
| Q-0019 | 31.12 | EU ambassadors endorsed the 22nd package; Council adoption expected (TASS citing a European source, early X) — check consilium.europa.eu |
| Q-0007 | 31.12 | FRED Brent **spot** 120.92 USD on 24.09.2026 (harvested; spot ≠ ICE front-month settlement) — check ICE settlements 24.09–07.10 |
| Q-0012 | 31.12 | H.R. 5334: measures due within 30 days of enactment, i.e. by about 18.10 (Baker McKenzie); no tariff decision found |
| Q-0016 | 31.12 | MPC 07.10: rates unchanged, reference 3.75% (PAP, Interia, 07.10) — not resolved; next 03–04.11 |
| Q-0027, Q-0002, Q-0040, Q-0065, Q-0068, Q-0018, Q-0023, Q-0005, Q-0069, Q-0032, Q-0001, Q-0024 | various | No event found in the stage 00 searches; stage 01 should run its standard check |
| Q-0036 | 31.12 | Harvested daily Hormuz totals 1–5 per day in the available days — no sign of a 7-day average above 40 |

All other ACTIVE questions (Q-0003, Q-0004, Q-0008, Q-0009, Q-0010, Q-0015, Q-0017, Q-0020, Q-0025, Q-0026, Q-0028–Q-0031, Q-0033–Q-0035, Q-0038, Q-0039, Q-0066, Q-0067, Q-0070–Q-0073): deadline after the state date and no signal of occurrence found; Q-0033 remains open (runoff 25.10).

## 4. Calendar 08.10–18.11.2026 (6 weeks)

Status: **C** = confirmed on the web in this stage; **U** = unconfirmed or single non-official source.

| Date | Event | PIR | Status | Source |
|---|---|---|---|---|
| 10.10 | Taiwan National Day; President Lai's address (PLA reaction watch, Q-0005) | PIR-4 | C | Focus Taiwan 02.10.2026 |
| 12.10 | Duma budget committee reviews the 2027–2029 draft (Siluanov present) | PIR-1, PIR-6 | C | Interfax 01.10.2026 |
| 12–18.10 | IMF/World Bank annual meetings, Bangkok (plenary 16.10) | PIR-6 | C | imf.org |
| 13.10 | EU ministers for European affairs prepare EUCO conclusions (Luxembourg) | PIR-2 | C | consilium.europa.eu |
| 15–16.10 | European Council, Brussels (Ukraine, MFF, Middle East, defence) | PIR-2, PIR-3, PIR-6 | C | consilium.europa.eu (notice of 14.09.2026) |
| about 18.10 | H.R. 5334: 30-day deadline for the measures of the Act (tariff authority; 10-day prior notice to Congress) | PIR-4, PIR-6 | C (deadline); U (whether any tariff is set) | whitehouse.gov 18.09; Baker McKenzie |
| about 20.10 | PRC customs detailed trade data for IX (rare-earth magnets, Q-0025) | PIR-4 | U | — |
| by end X | US-proposed technical trilateral US–UA–RU meeting (no date, venue or Russian acceptance) | PIR-1, PIR-7 | U | Zelensky 04.10 via Kyiv Independent, Ukrainska Pravda |
| "coming weeks" | Saudi offensive against the Houthis | PIR-5 | U | Reuters via US News, Defense News 02.10.2026 |
| 23.10 | Bank of Russia key-rate decision, 13:30 MSK, with medium-term forecast (current 14.00%) | PIR-6 | C | cbr.ru (calendar, investor calendar) |
| 25.10 | Brazil presidential runoff (Lula vs Flávio Bolsonaro) | PIR-7 | C | TSE figures via Al Jazeera, NPR, AS/COA |
| 25.10 | Bulgaria presidential election, first round (runoff 01.11 if needed) | PIR-7 | C | Sofia Globe 31.07.2026 (parliament decision); Washington Post |
| 26–29.10 | Fifth Plenum of the 20th CPC Central Committee (Party self-governance) | PIR-4, PIR-7 | C (October, Xinhua 30.07); U (exact dates, SBS only) | Xinhua; SBS |
| 27.10 | Israeli Knesset election (official results 04.11) | PIR-5, PIR-7 | C | Al Jazeera 17.07.2026; BICOM |
| 27–28.10 | FOMC (decision 28.10, no projections) | PIR-6 | C (secondary calendars; federalreserve.gov not opened) | fedratecalc; CME Group |
| 28–29.10 | ECB Governing Council (decision 29.10) | PIR-6 | C | ecb.europa.eu |
| 29.10 | Planned Duma first reading of the 2027–2029 budget | PIR-1, PIR-6 | C (plan of the committee chair) | Interfax, RG 01.10.2026 |
| 31.10 | Deadlines Q-0004 (DeepState October), Q-0039 (Panama), Q-0033 | — | — | registry |
| 01.11 | Meeting of the seven OPEC+ countries (December production) | PIR-3 | C | opec.org 04.10.2026 |
| 01.11 | EU gas storage date (Q-0067); target level for 2026 reported as lowered from 90% to 80% | PIR-3 | U (target level) | aggregators only |
| 01.11 | Bulgaria presidential runoff (if needed) | PIR-7 | C | Sofia Globe |
| 03.11 | US midterm elections (435 House, 35 Senate seats) | PIR-2, PIR-7 | C | NBC News; election guides |
| 03–04.11 | MPC (decision 04.11, new NBP projection) | PIR-6 | C (secondary; nbp.pl schedule not opened) | ceo.com.pl, strefainwestorow.pl |
| 06.11 | Recommendation of the US force posture review for Europe to the Secretary of Defense (review end reported for XII) | PIR-2 | C (reported date) | NBC News, The National 18.09.2026 |
| 06.11 | FAO Food Price Index (October) | PIR-3 | C | FAO via search |
| 06.11 | S&P review of Poland's rating | PIR-6 | U (from edition 01) | edition 01, K.6 |
| 09.11 | End of the BIS suspension of the "affiliates rule" | PIR-4 | U (single analysis) | search summary of post-summit analyses |
| 09–20.11 | COP31, Antalya (leaders 11–12.11) | — | C | unfccc.int |
| 18.11 | FOMC minutes | PIR-6 | C (secondary) | fedratecalc |
| 18–19.11 | APEC leaders' meeting, Shenzhen; Trump stated intent to attend (no official itinerary) | PIR-4 | C (dates); U (attendance) | gov.cn 12.12.2025; SCMP |

Changes against edition 01's calendar: the **10.11 trade-truce deadline is superseded** — truce and rare-earth suspension reported extended to 10.01.2027 (NBC, Brookings); Duma first reading set for 29.10; Israel (27.10) and Bulgaria (25.10) elections added. Just beyond the window: 27.11 Ga/Ge/Sb suspension; 29.11 OPEC+ JMMC; 11.12 US CR expiry; 16–17.12 ECB; 17–18.12 European Council; 10.01.2027 truce expiry. Not found: a NATO defence ministers' meeting in X 2026 (last 18.06.2026, nato.int).

## 5. PIRs (unchanged, methodology v1.0 §2)

- **PIR-1** Russia's capability and will to escalate against NATO and the eastern flank.
- **PIR-2** US/NATO capability and will to respond; US presence in Europe and in Poland.
- **PIR-3** Prices and availability of energy (oil, gas, fuels) in Europe and in Poland.
- **PIR-4** US–China rivalry: trade, technology, raw materials, Taiwan.
- **PIR-5** The war with Iran and sea lanes (Hormuz, Bab el-Mandeb, Suez).
- **PIR-6** Financial condition of the great powers and capital-market conditions, including PLN.
- **PIR-7** Shifts in the orientation of states (elections, alliances, changes of government).

## 6. What moved since edition 01 (10 priority searches + harvest coverage)

Signals from search summaries and harvest volumes, not fact records. Each needs verification and three perspectives in stage 02.

| Vector / region | Signal (date, source) | Change vs edition 01 |
|---|---|---|
| DIP/MIL — Iran, Hormuz | Trump rejected Iran's 7-day plan (blockade lift, oil-sanctions waiver, ceasefire incl. Lebanon); Ghalibaf 04.10: strait closed until "seven conditions" are met; Iran and Oman agreed safe-transit routes; Pentagon options for strikes "after the elections"; Rubio: Iran "lost control" of the strait (Al Jazeera 04.10; CBS; Fox 04.10). Harvest: Hormuz 356 items, Iran–US talks 85 | **Large.** Talks contact of 22–24.09 did not produce a deal; the military option is again explicit, tied to 03.11 |
| ENE — oil, gas | Brent front-month near 100–101 USD on 06.10 (Fortune, Trading Economics); FRED spot 113.96 on 29.09 and 120.92 on 24.09; EIA STEO 06.10: Brent spot averaged 114 USD in IX. TTF about 74–76 EUR/MWh (06–07.10); EU storage about 72.7% (EnergyRiskIQ). OPEC+ seven kept quotas for XI (04.10). Qatar force majeure extended into late Q4 (search summary) | Prices volatile around the thresholds of several questions; storage still far below the seasonal norm |
| DIP/MIL — Ukraine | US proposes a technical trilateral meeting by end-X (Zelensky 04.10); Kremlin 24.09: conditions not ready; Russia announced intensified strikes on Kyiv after Ukraine's refinery campaign; Merz in Kyiv 04.10 (Kyiv Independent, CNBC 05.10). Harvest: Ukraine war 1,530 items, refinery strikes 77 | Diplomatic track re-opened on paper; escalation of strikes on energy and cities |
| MIL — flank, Poland | Russian Mi-8 entered Polish airspace near Braniewo for 42 s on 23.09 (Notes from Poland 23.09); no drone incursion found for 24.09–07.10 in headlines. Harvest flag: Poland security <3 languages | New incident type (helicopter) on the state date of edition 01 |
| MIL — US in Europe and PL | No base location announced; Hegseth 04.10 hinted at shifting forces from Europe to Latin America (Washington Times 04.10); posture review recommendation 06.11 | Pressure toward reductions in Europe more explicit |
| ECO/TEC — USA–China | Truce and rare-earth suspension extended to 10.01.2027; Board of Trade lists of 30 bn USD per side; China to buy ≥10 Mt US coal a year in 2027–28; no chip-control changes (Brookings, CSIS, NBC) | **Large.** The 10.11 cliff removed; new cliff 10.01.2027 |
| FIN — sanctions | EU 22nd package endorsed by ambassadors (TASS citing an EU source); H.R. 5334 30-day deadline about 18.10; OFAC: 19 SDN additions on 06.10 (harvest) | Sanctions decisions cluster in the next two weeks |
| INF/MIL — Red Sea | Houthi claims of strikes on Riyadh airport, Rabigh refinery (05.10) and Jazan/Najran airports (06.10, 3 injured) (CFR tracker); Saudi offensive planned "in coming weeks" (Reuters 02.10). PortWatch Bab el-Mandeb 34 transits on 04.10 (harvest) | Escalation on Saudi territory; Saudi ground offensive possible |
| DOM — elections | Brazil: Flávio Bolsonaro led round one (47.03% vs 45.16%), runoff 25.10; Latvia: United List first (41–42 seats), coalition talks; Venezuela: elections promised at the UN, no date (Al Jazeera 24.09) | Brazil a likely orientation shift (PIR-7) |
| FIN — Poland, rates | CPI IX 4.0% y/y (MPC statement 07.10); MPC held rates (3.75%); EUR/PLN 4.3797 (NBP 07.10); USD/RUB 85.71 (CBR 07.10); Fed 3.75–4.00%; UST10Y 5.31% (05.10) | Inflation up 0.6 pp m/m; rate-hike talk in the MPC |
| MIL — Taiwan | PLA air activity around Taiwan down about half in 2026 (MND data to 09.08); no named exercise found; National Day 10.10 | No change; watch 10.10 |
| Sahel | No October 2026 reporting found on Mali (latest dated items IV–VI) | Data gap — G4 must search in French and Bambara-language outlets |

## 7. Collection priorities for stage 02

General principle: the harvest is thin for 23.09–01.10 — every group first closes that period with web search, then uses the digest for 02–07.10. Events marked ★ are key (three perspectives W/A/T). Mandatory flagged searches from `02_harvest/harvest_notes.md` are listed per group.

**G1 — MIL + INF**
1. ★ Iran: US military options vs talks; any US strike or CENTCOM announcement 24.09–07.10; Iran–Oman safe-transit arrangement; PortWatch Hormuz for the missing days 28.09–02.10 and 05–07.10.
2. ★ Red Sea and Saudi Arabia: Houthi strikes on Riyadh, Rabigh, Jazan, Najran (A: Houthi media — Saba failing in harvest; Saudi official cell silent → spa.gov.sa directly); UKMTO incidents; planned Saudi offensive.
3. ★ Eastern flank and Poland: DO RSZ reports 24.09–07.10; Mi-8 incident 23.09 with RU/BY (A) and T perspectives (mandatory: Poland security <3 lang); any Article 4 request (NATO official cell silent → nato.int directly).
4. ★ US forces in Europe/Poland: posture review leaks, Hegseth 04.10, base location (only 18 harvested items).
5. Ukraine: DeepState and ISW (ISW 403 in harvest → web), Russian strikes on energy and Kyiv, Ukrainian refinery strikes.
6. Taiwan (MND daily reports, PLA around 10.10), DPRK launches (JP official cell silent → mod.go.jp, JCS via Yonhap), Bosporus (Turkey Western cell silent).

**G2 — ENE + TEC**
1. ★ Brent ICE settlements 24.09–07.10 and TTF ICE Endex settlements (no harvested series); EIA STEO 06.10; IEA OMR mid-October.
2. ★ EU and PL gas storage directly from AGSI+ (no key in harvest); Qatar force majeure extension; storage target for 01.11.
3. Fuels in Poland: e-petrol weekly 07.10; mandatory: non-Polish perspective on Polish fuel prices (⚠W>80%, <3 lang).
4. ★ Rare earths: status of the suspension after the 24.09 summit (MOFCOM directly — China official cell near-silent); Ga/Ge/Sb; magnet exports IX.
5. Semiconductors and export controls (BIS affiliates rule 09.11), uranium, food (FFPI 02.10) — low harvest volume.

**G3 — ECO + FIN**
1. ★ H.R. 5334: notices to Congress, any tariff determinations by about 18.10; reactions of India, China, Turkey.
2. ★ US–China truce extension: Federal Register notice, PRC statement, Board of Trade lists.
3. ★ Russia's 2027–2029 budget: deficit in % of GDP, defence spending, windfall tax; Bank of Russia 23.10 setup.
4. EU 22nd package: formal Council adoption; OFAC SDN additions 24.09–07.10 (PRC/HK, Russia).
5. Poland: CPI IX flash (GUS), MPC 07.10 statement, EUR/PLN, rating calendar; Fed, ECB, UST10Y.

**G4 — DIP + DOM**
1. ★ US–Iran diplomacy: mediators (Qatar, Pakistan, Oman), Iranian conditions, status of Mojtaba Khamenei; IRGC vs MFA.
2. ★ Ukraine talks: trilateral proposal; Kremlin (Peskov, Ushakov) response; energy ceasefire.
3. ★ Elections: Brazil runoff campaign (25.10), Israel (27.10), Bulgaria (25.10), Latvia coalition, US midterms (03.11) — polls only, no forecasting models.
4. Arctic and Greenland (mandatory: <3 lang → Danish, Greenlandic, Russian sources; Greenland independent cell silent); ratification of the 22.09 defence agreement.
5. Sahel (Mali — no recent reporting found), Venezuela (election date), Caucasus, CPC Fifth Plenum (26–29.10).

## 8. Registry problems (integrity check)

| Check | Result |
|---|---|
| Encoding and BOM | All 7 CSV files in `registry/`: UTF-8 with BOM, separator `;` — OK |
| Headers vs template | `questions`, `forecasts`, `benchmarks`, `resolutions`, `sources` headers unchanged against the baseline and match the columns read by `tools/scores.py`; `question_proposals_edition_00.csv` has the same 17 columns as `questions.csv` — OK |
| Field counts | Every row of every file has the header's field count — OK |
| Unique question IDs | 73 questions, 73 unique IDs (Q-0001…Q-0073), all ACTIVE; panel 40 = 5 per vector × 8 — OK |
| Forecasts for non-existent questions | None. 365 forecast rows = 73 × 5 runs (A, B, C, AGG, AGG_RT) of edition 01; no duplicate (question, edition, run) keys; all p within 0.01–0.99 — OK |
| Benchmarks for non-existent questions | None (43 rows) — OK |
| Changes to history vs REGISTRY_BASELINE (5669790) | `questions`, `forecasts`, `benchmarks`, `resolutions`, `sources`, `question_proposals_edition_00`: row counts identical to the baseline and every baseline row unchanged. Only `registry/editions.csv` changed — it did not exist at the baseline (created in framework 1.1.0, 2 data rows) — OK |
| Resolutions | 0 rows — stage 01 of this edition writes the first resolutions |
| Notes | (1) `registry/editions.csv` uses CRLF line endings and quotes every field including the header, while the other registry files use LF and quote only text fields — format inconsistency, not a history change; not repaired. (2) `tools/pipeline.py` detection bug: `edition_done_map` falls back to file existence only when an edition's `provenance.jsonl` is empty; edition 01's file holds only the off-sequence "H repair" record of 05.10.2026, so none of stages 00–08 of edition 01 (run before provenance existed) count as done and `status` reported edition 01 as open. User-approved workaround: proceed; no change to the tool (rule 13); no provenance records invented. Proposed for L5 or the quarterly review |

## 9. Gaps of stage 00

- Dates unconfirmed or single-source: exact days of the CPC Fifth Plenum; trilateral US–UA–RU meeting; Saudi offensive; EU storage target level for 01.11; S&P review of Poland 06.11; BIS affiliates rule 09.11; PRC customs data date; G20 Miami (December, outside the window).
- Primary calendars not opened: federalreserve.gov (FOMC), nbp.pl (MPC schedule) — dates taken from secondary calendars that agree with each other.
- No ICE settlement prices (Brent, TTF), no AGSI+ reading, no e-petrol quotation in this stage — these decide several questions due by 07.10 and sit near their thresholds.
- Mali: no reporting after VI 2026 found.
