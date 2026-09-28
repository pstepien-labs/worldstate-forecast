# Edition 01 — plan (stage 00)

## 1. Edition parameters

| Parameter | Value |
|---|---|
| NR | 01 |
| STATE_DATE | 23.09.2026 |
| PERIOD_FROM | 21.09.2026 (state date of edition 00) |
| DIRECTORY | `editions/2026-09-23_edition-01` |
| PREVIOUS | `editions/2026-09-21_edition-00` (starting point, not scored) |
| Methodology | v1.0 (frozen) |
| Next edition (indicative, +14 days) | approx. 07.10.2026 — to be confirmed by the user |

**Note on the period.** The README planned edition 01 for 05.10.2026; the edition was started with STATE_DATE 23.09.2026, so the period covered is only 2 days (21–23.09). Stage 02 should therefore (a) verify the picture from edition 00, all of which "requires verification" (state_00.md), and (b) capture changes from 21–23.09. The horizon "to the next edition" (methodology §3.3) is counted from STATE_DATE: at a 14-day rhythm the deadline of those questions is approx. 07.10.2026.

## 2. Questions to resolve in stage 01

**None.** `registry/questions.csv` contains only the header (0 questions), so there are no ACTIVE questions with a deadline ≤ 23.09.2026 nor any in which the event may already have occurred. Stage 01 creates `01_resolutions.md` and `01_scores.md` with the note "no resolutions in this edition".

The proposals from edition 00 (`registry/question_proposals_edition_00.csv`, 28 rows, status PROPOSAL) are not registry questions and are not subject to resolution. Signals relevant to stage 03 (admission of proposals to the panel):

- **P-026** (deficit in Russia's draft 2027 budget > 2.0% of GDP, deadline 31.10.2026). On 21.09.2026 Siluanov at the Moscow Financial Forum gave a deficit of "about 2% of GDP" (Vedomosti, 21.09.2026, https://www.vedomosti.ru/economics/news/2026/09/21/1230540-federalnii-byudzhet-2027). The 2.0% threshold sits exactly on the announced value, and the draft will probably reach the Duma before 01.10. ASSESSMENT: if the draft is submitted before stage 03, the question will not meet the §3.2 requirement ("event can still occur after the creation date") — stage 03 must check this and reword if necessary (e.g. to the law adopted in third reading).
- **P-005** (trilateral US–UA–RU meeting by 30.11). Witkoff spoke of "movement on setting further trilateral talks" (The Hill, IX 2026); no date found.
- **P-006** (decree on mobilisation / reservists). Conscription in 2026 is year-round (decree no. 998 of 29.12.2025, 261k people; dispatch to units 01.10–31.12 — Garant.ru). A separate "autumn conscription decree" is therefore not expected; the assumption in K.6 of edition 00 ("autumn conscription … possible decree") needs correcting in stage 03.
- **P-018/P-019** (US troops in Poland). On 18.09.2026 Trump announced a near agreement on a new permanent base in Poland, and the Pentagon is considering withdrawing approx. 25k troops from other European states; the additional 5k for Poland not yet implemented (Stars and Stripes, 18.09.2026).

## 3. Calendar 23.09–04.11.2026 (6 weeks)

Status: **C** = confirmed on the web in stage 00; **U** = unconfirmed (check in stage 02).

| Date | Event | PIR | Status | Source |
|---|---|---|---|---|
| 23–25.09 | State visit of Xi Jinping to the USA; ceremony and summit at the White House on 24.09. On the table: tariffs, rare earths (deadline 10.11), Taiwan (14 bn USD package), Iran, AI | PIR-4, PIR-5 | C | whitehouse.gov (First Lady statement, IX 2026); SCMP (Beijing confirmation); Bloomberg 22.09.2026 |
| week of 22.09 | UN General Assembly general debate in New York; Iranian delegation "with a mandate" to resume diplomacy | PIR-5 | C | US News/Reuters 22.09.2026 |
| by approx. 25.09 | Final results of the Duma elections (CEC) | PIR-7 | C (approximate date) | Al Jazeera 21.09.2026 |
| 30.09 / 01.10 | End of the US fiscal year — **no** shutdown threat: CR to 11.12.2026 adopted (Senate 90–6, House 370–48) | PIR-6 | C | NPR 01.09.2026; NBC News |
| by 01.10 | Submission to the Duma of Russia's 2027–2029 draft budget (Siluanov: 2027 deficit approx. 2% of GDP) | PIR-1, PIR-6 | U (submission date) | Vedomosti 21.09.2026 |
| 01.10 | Start of autumn dispatch of conscripts in Russia (year-round conscription, 261k in 2026) | PIR-1 | C | Garant.ru (decree no. 998 of 29.12.2025); kremlin.ru/acts/news/78905 |
| 03.10 | Parliamentary elections in Latvia | PIR-7 | C | Wikipedia (index) — confirm with Latvia's CVK |
| 04.10 | General elections in Brazil (second round 25.10) | PIR-7 | C | AS/COA |
| 04.10 | General elections in Bosnia and Herzegovina | PIR-7 | C | Model Diplomat — confirm with the BiH CEC |
| 06–07.10 | MPC meeting (decision 07.10, inflation projection) | PIR-6 | C | PAP Biznes (NBP schedule for 2026) |
| to 08.10 | Exercise "Namejs 26" in Latvia (approx. 12k troops, since 02.09) | PIR-1, PIR-2 | C | grosswald.org (single source — confirm) |
| X (no date) | Trilateral US–UA–RU talks (edition 00: UAE, "in principle") | PIR-1, PIR-7 | U | The Hill (no date) |
| X (no date) | OPEC+ JMMC meeting | PIR-3 | U | tradingnewsterminal (no date) |
| X (approx. mid-month) | IEA monthly report (Oil Market Report) | PIR-3 | U | — |
| 12–18.10 | IMF and World Bank annual meetings, Bangkok (plenary 16.10) | PIR-6 | C | imf.org |
| 15–16.10 | European Council, Brussels | PIR-2, PIR-3, PIR-6 | C | consilium.europa.eu; brussels.be |
| 23.10 | Bank of Russia meeting (key rate currently 14.00%) | PIR-6 | C | cbr.ru (decision calendar) |
| 25.10 | Second round of elections in Brazil (if needed) | PIR-7 | C | AS/COA |
| 27–28.10 | FOMC (decision 28.10, SEP) | PIR-6 | C | federalreserve.gov; FedRateCalc |
| 29.10 | ECB monetary policy meeting | PIR-6 | C | ECB (meeting calendar) via Young Platform/IG |
| 03.11 | US midterm elections | PIR-2, PIR-7 | C (edition 00) | state_00.md; confirm in G4 |
| 03–04.11 | MPC meeting (decision 04.11) | PIR-6 | C | PAP Biznes |
| early XI | Expiry of the extended force majeure in Qatar (Ras Laffan) | PIR-3 | U | edition 00, section J (single source) |

Just beyond the window: 10.11 — the suspension of Chinese rare-earth controls expires; 18–19.11 — APEC in Shenzhen; 11.12 — the US CR expires; XII — G20 in Florida.

Not found: a meeting of NATO defence ministers in X 2026 (in 2026 so far 12.02 and 18.06 — nato.int). Check in G1.

## 4. PIRs (unchanged, methodology v1.0 §2)

- **PIR-1** Russia's capability and will to escalate against NATO and the eastern flank.
- **PIR-2** US/NATO capability and will to respond; US presence in Europe and in Poland.
- **PIR-3** Prices and availability of energy (oil, gas, fuels) in Europe and in Poland.
- **PIR-4** US–China rivalry: trade, technology, raw materials, Taiwan.
- **PIR-5** The war with Iran and sea lanes (Hormuz, Bab el-Mandeb, Suez).
- **PIR-6** Financial condition of the great powers and capital-market conditions, including PLN.
- **PIR-7** Shifts in the orientation of states (elections, alliances, changes of government).

## 5. Headline scan (15 queries) — what moved

Signals from headlines, not fact records. Each requires verification and three perspectives in stage 02.

| Vector / region | Signal (date, source) | Change vs edition 00 |
|---|---|---|
| MIL/DIP — Iran, Hormuz | 20–21.09: Iran's central armed forces command claims that the USA "with the support of regional states" is preparing to resume strikes; threatens retaliation on US bases (Al Jazeera 21.09; Al Arabiya 20.09; Times of Israel). 22.09: a senior Iranian official (Reuters via US News, CNBC): Hormuz could be opened within 7 days if the USA lifts the blockade and announces a diplomatic path; Ghalibaf — Hormuz closed until US commitments are met. Mediators: Qatar, Pakistan | **Large.** Two-track signal: risk of the war resuming and at the same time an offer to open Hormuz. This was not in edition 00 |
| DIP/ECO/FIN — USA–China | Summit 24.09. On 18.09 Trump signed the "Sanctioning Russia and Iran Act": tariffs of up to 100% on the largest importers of Russian oil and gas (including China), extension of the Iran Sanctions Act by 5 years (via CFR/Bloomberg, 21–22.09 — primary source to be established) | **Large.** A new sanctions tool just before the summit; edition 00 did not know it |
| ENE — oil | Brent approx. 99–100 USD on 22.09 (Fortune; Investing, day range 99.58–102.29) | Down from ~104 USD (19.09) — possibly a reaction to signals from Iran; verify closes |
| ENE — gas | TTF approx. 78–81 EUR/MWh (16.09), peak ~84 in early IX; EU storage 68.49% (15.09) vs 5-year average 84% (IndexBox; EnergyRiskIQ) | Unchanged — confirmation of the picture from 00; no data after 16.09 |
| INF — Bab el-Mandeb | The Houthis control the whole Red Sea coast, Perim (11.09) and the Hanish islands; blockade of Saudi ships; >300 killed in fighting (Al Jazeera 11.09; Washington Post 10.09; Times of Israel — Saudi strike on a prison) | Confirmation with deepening: "restricted" in block L may be too weak — check flows |
| DOM — Russia | Duma elections 18–20.09: United Russia 57.83% (95% of protocols), approx. 355/450 seats, turnout 56.7%; A Just Russia below 5% (Al Jazeera, Moscow Times 21.09) | **Gap closed** from section J of edition 00 (partial results) |
| FIN — Russia | Siluanov 21.09: 2027 deficit "about 2% of GDP", "without risks" (Vedomosti) | New; key for P-026 |
| MIL — Ukraine/Russia | 19/20.09 the largest Ukrainian package of missiles and drones on Moscow oblast; Russia is building underground drone plants in Alabuga (ISW 21.09 via Kyiv Post) | Change of emphasis: Ukrainian pressure on Russia's depth; front — no new data |
| DIP — Ukraine | Witkoff–Kushner talks with Putin (05.09) and Zelensky (06–07.09); "movement on further trilateral talks" (The Hill), no date | Unchanged vs 00 |
| MIL — USA in Europe and PL | 18.09: Trump — near agreement on a new permanent US Army base in Poland; the Pentagon is considering withdrawing approx. 25k from Europe (NBC: "almost a third"); currently approx. 80k; NDAA 2026 §1249 — 76k threshold on FY2026 funds (Stars and Stripes 18.09; The National 18.09; NBC) | **Large.** New numbers of the force posture review; divergence "less in Europe / more in PL" |
| MIL — flank | A search result contained a sentence about "almost two dozen drones over Poland on 10.09" — most likely refers to 10.09.2025, not 2026. Not accepted | No new incident 21–23.09 in headlines — check in G1 |
| MIL — Sahel | 14.09 JNIM attack on the air base in Sévaré; 19.09 attack on a checkpoint near Bamako; 20.09 crisis meeting at Goïta's; fuel blockade of the capital (Al Jazeera 22.09; Rio Times) | Deterioration relative to 00 |
| MIL — Taiwan | No named PLA exercises around Taiwan in IX 2026 in the results; since VII regular PRC coast guard patrols east of Taiwan (The Diplomat, IX 2026) | No major change; data gap |

## 6. Collection priorities (stage 02)

General principle: the period 21–23.09 is short, so each group **first verifies the block L values from edition 00** (each with a date and source), then looks for changes. Events marked ★ are key (three perspectives W/A/T).

**G1 — MIL + INF**
1. ★ Iran: threat of resumed US strikes (20–21.09) and the offer to open Hormuz (22.09) — perspectives: USA (CENTCOM, Pentagon), Iran (FA: IRNA, Tasnim, Khatam al-Anbiya statement), third party (Qatar, Pakistan, Oman; AR). Transits through Hormuz per IMF PortWatch after 13.09.
2. ★ Bab el-Mandeb: scale of the Houthi blockade, Saudi strikes, flows through the strait and Suez; status "restricted" vs "closed to some flags".
3. ★ USA in Europe and PL: force posture review numbers, permanent base in PL, implementation of the +5k; §1249 NDAA after 30.09 (CR to 11.12 — does it extend the restriction?).
4. Flank: incidents 21.09–23.09, most recent Art. 4 (gap from 00), Namejs 26.
5. Ukraine: front line (ISW; quantitatively km²), strikes on Russia's depth.
6. Taiwan/SCS: PLA activity, US carriers in the Indo-Pacific (status in IX — unconfirmed in 00).

**G2 — ENE + TEC**
1. ★ Brent (closes 19–23.09) and the reaction to signals from Iran; IEA report from IX.
2. ★ TTF and EU/PL storage after 15.09; Qatar (Ras Laffan, force majeure until early XI — single source in 00).
3. Saudi East–West pipeline (shut on 11.09) — status.
4. Fuels in PL: diesel price, maximum price mechanism (contradiction with 00).
5. ★ Rare earths: outcome of the 24.09 summit for the 10.11 deadline (MOFCOM, Xinhua; T perspective — Japan/EU).

**G3 — ECO + FIN**
1. ★ "Sanctioning Russia and Iran Act" (18.09): text, legal basis, dates of entry into force of tariffs; reaction of the PRC MFA/MOFCOM and India.
2. ★ US–China summit 24.09: tariffs, extension of the tariff truce (deadline 10.11).
3. Russia's 2027–2029 budget: date of submission to the Duma, deficit, defence spending; Bank of Russia rate (14.00%).
4. Rates: ECB 2.50%, NBP 3.75%, Fed — confirm; EUR/PLN (gap from 00); Poland's 2026 deficit (gap from 00).
5. EU sanctions against Russia — state of work on the next package; Ukraine funding and SAFE.

**G4 — DIP + DOM**
1. ★ Iran–US diplomacy in UN General Assembly week (mediators Qatar, Pakistan); status of Mojtaba Khamenei.
2. ★ Talks on Ukraine: date of trilateral talks; positions of the Kremlin (Ushakov, Peskov) and Kyiv.
3. Russia after the Duma elections: final CEC results, composition, personnel changes.
4. Elections 03–04.10: Latvia, Brazil, BiH; US midterms — state of the campaign.
5. Sahel (Mali — siege of Bamako), Venezuela (election date), Caucasus, Greenland — one status check each.

## 7. Registry problems (integrity check)

| Check | Result |
|---|---|
| Encoding and BOM | All 6 CSV files in `registry/`: UTF-8 with BOM, separator `;` — OK |
| Headers vs template | Headers of `questions.csv`, `forecasts.csv`, `benchmarks.csv`, `resolutions.csv`, `sources.csv` match the starter kit and the columns read by `tools/scores.py` — OK |
| Number of rows | `questions`, `forecasts`, `benchmarks`, `resolutions`, `sources`: header only (0 data rows) |
| Unique question IDs | Not applicable (0 questions). In the proposals file: 28 IDs (P-001…P-028), all unique, 17 fields in each row |
| Forecasts for non-existent questions | None (0 forecasts) |
| Changes to history | No previous git tag — repository initialised in this stage (commit "initial state"). Comparison possible from edition 02 |
| Notes | (1) `registry/sources.csv` is empty — stage 02 must append sources. (2) The proposals from 00 have `p_status_quo` set before methodology v1.0 — stage 03 should check them per §3.5. |

## 8. Gaps of stage 00

- Dates not confirmed: submission of Russia's budget to the Duma, OPEC+ JMMC, IEA report for X, trilateral talks, force majeure in Qatar, NATO defence ministers' meeting in X.
- Elections in Latvia confirmed only via the index (Wikipedia) — a primary source (CVK) is required.
- The primary source of the "Sanctioning Russia and Iran Act" (Congress.gov / whitehouse.gov) was not opened.
