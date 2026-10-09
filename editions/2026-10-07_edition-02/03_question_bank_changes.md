# Stage 03 — Changes to the question bank (edition 02, state 07.10.2026)

Registry before the stage: 73 questions — 46 ACTIVE (incl. Q-0037 and Q-0049, deadline passed but not resolved for lack of data) and 27 RESOLVED (stage 01). Added in this stage: **42 questions (Q-0074 – Q-0115)** — 4 panel replacements and 38 open questions. After the stage: **115 questions, 88 ACTIVE** (panel 40 = 5 per vector; open 48). No forecasts. Only appended rows; no existing row changed (checked with `git diff`: 42 insertions, 0 deletions).

## 1. Rules applied in this edition

**Creation date** of all new questions: 07.10.2026 (state date), `edition_created` = 02. Every criterion concerns events from 08.10.2026 onward ("between 08.10 and …"), or a value fixed on a later date. The stage itself ran on 09.10.2026, so for short questions the events of 08–09.10 were checked on the web (rule: an event that can still occur after the creation date, methodology §3.2); one candidate was rejected because its event may already have occurred (K4-04, §4).

**Deadline of short questions:** about 20–21.10.2026 (indicative date of edition 03, 00_plan §1); PortWatch questions end on 17.10 because the series is published with a lag of about 4 days (cf. Q-0037, still unresolved); Q-0088 (Bank of Russia) on 23.10 — counted in the short bucket (≤ 24.10).

**p_status_quo (§3.5)** — the mechanical rules of edition 01 (03_question_bank_changes.md of ed.01, §1) applied unchanged:
1. YES requires a new action by an actor (decree, strike, attack, listing, announcement, adoption, meeting) → 0.10. This includes recurring events (Saudi fatalities, tanker hits) and scheduled decisions (Council adoption on 12.10, Bank of Russia meeting).
2. Thresholds on continuous values: YES on the same side as the last known value → 0.90 (Q-0074: Brent 100.20 > 100.00); on the opposite side → 0.10. "Higher than the last value" counts as the opposite side (Q-0076, as Q-0014).
3. Elections: incumbent keeps majority → 0.90 (Q-0095); new configuration (outright first-round win, largest list in a new parliament) → 0.50 (Q-0093, Q-0094).
4. Scheduled event without a direction → 0.50 (Q-0100, as Q-0029).
Result: 37 × 0.10, 3 × 0.50, 2 × 0.90.

**who_benefits (§3.6):** NONE unless YES clearly strengthens one actor at another's expense. COMPROMISE for agreements and extensions of suspensions (Q-0077, Q-0089, Q-0102, Q-0108, Q-0110); EU for EU sanctions acts (Q-0083, Q-0104 — consistency with Q-0019); RUSSIA for a Russian territorial gain (Q-0113 — consistency with Q-0073). Distribution: NONE 34, COMPROMISE 5, EU 2, RUSSIA 1.

**Clusters (§3.4):** new labels BG_ELECTIONS, IL_ELECTIONS, BLACK_SEA, UA_EU, URANIUM, GREENLAND, US_CHINA_FIN. Existing labels reused wherever the outcome is the same (e.g. Q-0089 with Q-0021 in CN_RARE_EARTHS; Q-0082 with Q-0026 in UA_TALKS; Q-0081 with Q-0028/Q-0042 in HORMUZ).

**Measuring Hormuz and Bab el-Mandeb.** Q-0078 and Q-0079 use IMF PortWatch (AIS-visible transits only; contradiction between AIS counts and flow estimates, 03_analysis §1.1 C). The caveat is in the question notes.

**Oil — source.** Q-0074 and Q-0115 use the ICE Brent front-month settlement as Q-0006–Q-0008; ICE itself was not reachable in stage 01, so the fallback chain (Bloomberg/Reuters wire, then Investing.com) is written into the criterion.

## 2. New questions

### 2.1 Panel replacements (4)

| ID | Replaces | Vector | Cluster | Question | Deadline | p_sq | who_benefits | PIR |
|---|---|---|---|---|---|---|---|---|
| Q-0074 | Q-0006 | ENE | OIL_PRICE | Will the ICE Brent front-month settlement on 20.10.2026 exceed 100.00 USD/bbl? | 20.10.2026 | 0.90 | NONE | PIR-3; PIR-5 |
| Q-0075 | Q-0013 | ECO | PL_INFLATION | Will the GUS flash CPI for October 2026 be below 3.5% y/y? | 31.10.2026 | 0.10 | NONE | PIR-6; PIR-3 |
| Q-0076 | Q-0014 | ECO | FOOD | Will the FAO FFPI for October 2026 be higher than 136.0 points? | 09.11.2026 | 0.10 | NONE | PIR-3 |
| Q-0077 | Q-0011 | ECO | US_CHINA_TRADE | Will the USA and the PRC both announce by 10.01.2027 an extension of the trade truce beyond 10.01.2027 or a new agreement replacing it? | 10.01.2027 | 0.10 | COMPROMISE | PIR-4 |

Note on Q-0077: Q-0011 is flagged VERIFY (timing of the US announcement relative to the creation date). If the user adopts reading 2 and returns Q-0011 to ACTIVE, Q-0077 remains a separate outcome (extension beyond 10.01.2027), and the ECO panel would temporarily hold six questions until Q-0011 resolves — to be noted by the user's decision.

### 2.2 Open questions (38)

**Short horizon (deadline ≤ 24.10.2026) — 14**

| ID | Vector | Cluster | Question | Deadline | p_sq | who | PIR |
|---|---|---|---|---|---|---|---|
| Q-0078 | INF | HORMUZ | PortWatch ≥ 10 Hormuz transits on any day 08.10–17.10.2026? | 17.10.2026 | 0.10 | NONE | PIR-5 |
| Q-0079 | INF | BAB_EL_MANDAB | PortWatch < 20 Bab el-Mandeb transits on any day 08.10–17.10.2026? | 17.10.2026 | 0.10 | NONE | PIR-5 |
| Q-0080 | MIL | BAB_EL_MANDAB | Saudi authorities report ≥ 1 person killed on Saudi territory by an attack from Yemen, 08.10–21.10.2026? | 21.10.2026 | 0.10 | NONE | PIR-5 |
| Q-0081 | DIP | HORMUZ | In-person meeting of US and Iranian government representatives in the same room, 08.10–21.10.2026? | 21.10.2026 | 0.10 | NONE | PIR-5 |
| Q-0083 | FIN | RU_SANCTIONS_EU | EU Council adopts ≥ 1,500 new Russia listings by 21.10.2026? | 21.10.2026 | 0.10 | EU | PIR-1 |
| Q-0084 | ENE | EU_ENERGY | ICE Endex TTF front-month settlement on 20.10.2026 > 80.00 EUR/MWh? | 20.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0085 | ENE | PL_FUELS | e-petrol national average diesel on 21.10.2026 < 7.70 PLN/l? | 21.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0086 | FIN | PLN | NBP EUR/PLN on 21.10.2026 > 4.4000? | 21.10.2026 | 0.10 | NONE | PIR-6 |
| Q-0087 | MIL | TAIWAN | Taiwan MND daily report with ≥ 30 PLA aircraft, 08.10–21.10.2026? | 21.10.2026 | 0.10 | NONE | PIR-4 |
| Q-0088 | FIN | RATES_RU | Bank of Russia raises the key rate on 23.10.2026? | 23.10.2026 | 0.10 | NONE | PIR-1; PIR-6 |
| Q-0089 | TEC | CN_RARE_EARTHS | MOFCOM announcement extending beyond 10.11 or repealing the rare-earth suspension, 08.10–21.10.2026? | 21.10.2026 | 0.10 | COMPROMISE | PIR-4 |
| Q-0090 | ECO | RU_SANCTIONS_US | US act raising duties on Russian goods under Sec. 112 of H.R. 5334 published 08.10–21.10.2026? | 21.10.2026 | 0.10 | NONE | PIR-1; PIR-6 |
| Q-0091 | FIN | RU_SANCTIONS_US | OFAC SDN addition under a Russia programme, 08.10–21.10.2026? | 21.10.2026 | 0.10 | NONE | PIR-1; PIR-6 |
| Q-0092 | INF | BAB_EL_MANDAB | UKMTO/JMIC report a merchant ship hit in the Red Sea, Bab el-Mandeb or Gulf of Aden, 08.10–21.10.2026? | 21.10.2026 | 0.10 | NONE | PIR-5; PIR-3 |

**To the end of the quarter (25.10–31.12.2026) — 18**

| ID | Vector | Cluster | Question | Deadline | p_sq | who | PIR |
|---|---|---|---|---|---|---|---|
| Q-0082 | DIP | UA_TALKS | Trilateral US–UA–RU meeting of government delegations, 08.10–31.10.2026? | 31.10.2026 | 0.10 | NONE | PIR-1; PIR-7 |
| Q-0093 | DOM | BG_ELECTIONS | Iotova > 50% in the first round on 25.10.2026? | 31.10.2026 | 0.50 | NONE | PIR-7 |
| Q-0094 | DOM | IL_ELECTIONS | Likud the largest list in the Knesset election of 27.10.2026? | 06.11.2026 | 0.50 | NONE | PIR-5; PIR-7 |
| Q-0095 | DOM | US_ELECTIONS | Republicans hold ≥ 50 Senate seats after 03.11.2026? | 31.12.2026 | 0.90 | NONE | PIR-2; PIR-7 |
| Q-0096 | DOM | IRAN_LEADERSHIP | Araghchi ceases to be Iran's foreign minister by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-5; PIR-7 |
| Q-0097 | MIL | EASTERN_FLANK | DO RSZ/MoD confirm a violation of Polish airspace from RU or BY, 08.10–31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-1 |
| Q-0098 | INF | BLACK_SEA | RO, BG or TR authorities confirm a merchant ship hit by a drone/missile in their territorial sea or EEZ, 08.10–31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-1; PIR-2 |
| Q-0099 | MIL | IRAN_WAR | USNI tracker shows ≥ 3 US carriers simultaneously in CENTCOM waters by 30.11.2026? | 30.11.2026 | 0.10 | NONE | PIR-5 |
| Q-0100 | DIP | US_CHINA_SUMMITS | Putin attends the APEC leaders' meeting in Shenzhen in person? | 19.11.2026 | 0.50 | NONE | PIR-1; PIR-4 |
| Q-0101 | DIP | UA_EU | EU formally opens cluster 2 or 3 with Ukraine by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-7 |
| Q-0102 | TEC | US_CHINA_TECH | BIS Federal Register document extending (beyond 09.11) or rescinding the Affiliates rule, by 09.11.2026? | 09.11.2026 | 0.10 | COMPROMISE | PIR-4 |
| Q-0103 | TEC | URANIUM | Cameco month-end U3O8 spot > 95.00 USD/lb for X, XI or XII 2026? | 31.12.2026 | 0.10 | NONE | PIR-3 |
| Q-0104 | FIN | RU_SANCTIONS_EU | EU Council adopts a Russia act with a new import or export prohibition by 30.11.2026? | 30.11.2026 | 0.10 | EU | PIR-1; PIR-6 |
| Q-0105 | FIN | PL_FINANCE | S&P downgrades Poland or sets a negative outlook, decision dated by 06.11.2026? | 06.11.2026 | 0.10 | NONE | PIR-6 |
| Q-0106 | ENE | OIL_PRICE | US ban or mandatory quota on distillate exports in force by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-3 |
| Q-0107 | ENE | PL_FUELS | Commission letter of formal notice to Poland on reduced fuel VAT by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-3; PIR-6 |
| Q-0108 | ECO | US_CHINA_TRADE | Both USA and PRC put 30-for-30 tariff cuts into effect by 31.12.2026? | 31.12.2026 | 0.10 | COMPROMISE | PIR-4 |
| Q-0109 | DOM | US_EUROPE | FY2027 NDAA with a numerical EUCOM troop floor enacted by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-2 |

**Longer (after 31.12.2026) — 6**

| ID | Vector | Cluster | Question | Deadline | p_sq | who | PIR |
|---|---|---|---|---|---|---|---|
| Q-0110 | DIP | UA_TALKS | Russia and Ukraine both confirm a signed ceasefire covering the whole front by 30.06.2027? | 30.06.2027 | 0.10 | COMPROMISE | PIR-1; PIR-7 |
| Q-0111 | DIP | GREENLAND | The US–Denmark–Greenland agreement of 22.09.2026 enters into force by 30.06.2027? | 30.06.2027 | 0.10 | NONE | PIR-2; PIR-7 |
| Q-0112 | FIN | US_CHINA_FIN | Fed suspends, restricts or conditions HKMA's FIMA access by 31.03.2027? | 31.03.2027 | 0.10 | NONE | PIR-4; PIR-6 |
| Q-0113 | MIL | UA_FRONT | ISW assesses Russian control of the whole of Kostiantynivka by 31.03.2027? | 31.03.2027 | 0.10 | RUSSIA | PIR-1 |
| Q-0114 | MIL | US_EUROPE | US or Polish government names the location of a new permanent US Army base in Poland by 31.03.2027? | 31.03.2027 | 0.10 | NONE | PIR-2 |
| Q-0115 | ENE | OIL_PRICE | ICE Brent front-month settlement below 70.00 USD/bbl on any day 08.10.2026–30.06.2027? | 30.06.2027 | 0.10 | NONE | PIR-3; PIR-6 |

Full criteria, resolution sources, key indicators and notes are in `registry/questions.csv`.

## 3. Replacements

| Resolved panel question | Vector / cluster | Replaced by | Change |
|---|---|---|---|
| Q-0006 (Brent 06.10 > 100) | ENE / OIL_PRICE | Q-0074 | Same instrument and threshold, new date 20.10.2026 (rolling); fallback sources written in |
| Q-0013 (CPI IX ≥ 3.5%) | ECO / PL_INFLATION | Q-0075 | October flash; direction reversed ("below 3.5%") to test the pass-through of the fuel caps from 03.10 |
| Q-0014 (FFPI VIII → IX > 133.3) | ECO / FOOD | Q-0076 | October FFPI > 136.0 (rolling) |
| Q-0011 (truce extension by 10.11) | ECO / US_CHINA_TRADE | Q-0077 | Next cliff: extension beyond 10.01.2027 (see the note in §2.1) |

No other panel question was resolved. Q-0037 (INF, HORMUZ) and Q-0049 (open) remain ACTIVE past their deadlines pending data (01_resolutions §4); Q-0037 is not replaced until it resolves.

## 4. Candidates from stage 02 — decisions

| Candidate | Decision | Question | Reason / change |
|---|---|---|---|
| G1 K1 | Accepted with correction | Q-0078 | Window shortened to 08.10–17.10 (PortWatch lag) |
| G1 K2 | Accepted with correction | Q-0079 | Daily count below 20 in a short window instead of a 7-day average to 31.12 (the latter needs a sustained collapse; short window gives a resolvable test before edition 03) |
| G1 K3 | Accepted with correction | Q-0092 | Short window (to 21.10); "hit" defined as physical impact |
| G1 K4 | Accepted | Q-0080 | Sources specified; Houthi claims excluded |
| G1 K5 | Accepted | Q-0099 | CENTCOM waters listed |
| G1 K6 | Accepted with correction | Q-0098 | Cause must be stated as drone/missile/USV by the coastal state; attribution not required |
| **G1 K7** | **Rejected** | — | Government attribution to Russia is a rare, political act and depends on K6; kept as indicator I12 in 03_analysis |
| G1 K8 | Accepted with correction | Q-0097 | Balloons excluded |
| **G1 K9** | **Rejected** | — | Arrival of an already announced rotation, confirmed only by announcement; US_EUROPE covered by Q-0109 and Q-0114 |
| **G1 K10** | **Rejected** | — | "Independent confirmation" of control of Mocha is ambiguous |
| **G1 K11** | **Rejected** | — | MIL vector already the largest; KOREA lower PIR priority; deferred |
| G1 K12 | Accepted | Q-0087 | — |
| G1 K13 | Accepted with correction | Q-0113 | ISW assessment instead of a Russian MoD claim (consistency with Q-0073); deadline 31.03.2027 (long bucket) |
| **G1 K14** | **Rejected** | — | Overlaps Q-0028, Q-0036, Q-0038 (HORMUZ); "without route or clearance conditions" hard to verify from IRGC statements |
| K-G2-01 | Accepted | Q-0074 (panel) | Fallback sources added |
| K-G2-02 | Accepted | Q-0084 | — |
| **K-G2-03** | **Rejected (deferred)** | — | OPEC cluster just resolved (Q-0051); ENE already 6 new questions; to reconsider in edition 03 |
| **K-G2-04** | **Rejected** | — | "Beyond the 400 mn bbl programme" not verifiable — the 75 vs 100 mn bbl arithmetic dispute (G2 contradiction 5) |
| K-G2-05 | Accepted | Q-0106 | — |
| **K-G2-06** | **Rejected** | — | Serial extensions of the Russian diesel export ban — triviality risk (§3.8), as in edition 01 |
| K-G2-07 | Accepted | Q-0085 | — |
| K-G2-08 | Accepted | Q-0107 | — |
| K-G2-09 | Accepted with correction | Q-0102 | Rescission added as YES |
| K-G2-10 | Accepted | Q-0076 (panel) | Deadline 09.11 (3 days for a delayed release) |
| **K-G2-11** | **Rejected (deferred)** | — | No signal of a postponement in the window (Brussels holding to the date, G2-024); reconsider if one appears |
| **K-G2-12** | **Rejected** | — | Resolved by one company's statement; as in edition 01 |
| **K-G2-13** | **Rejected** | — | Aramco and SPA do not comment on flows — YES nearly unobservable |
| K-G2-14 | Accepted | Q-0103 | — |
| K3-01 | Accepted with correction | Q-0090 | Window to 21.10 (short bucket); legal act required |
| **K3-02** | **Rejected** | — | A Sec. 115 waiver may be sent to Congress without publication — observability; covered by ACH question 3 indicators |
| **K3-03** | **Rejected** | — | Same outcome family as Q-0102 (US formalisation of the truce); one question per family |
| K3-04 | Accepted | Q-0108 | — |
| K3-05 | Accepted with correction | Q-0083 | Several acts in the window may add up to 1,500 |
| K3-06 | Accepted with correction | Q-0104 | Adding goods to existing prohibition lists counts |
| **K3-07** | **Rejected** | — | Scheduled procedural step (first reading 29.10) with low information value |
| **K3-08** | **Rejected** | — | Third reading may fall after 30.11 → NO regardless of the defence figure (as ed.01 K3-05) |
| **K3-09** | **Rejected** | — | Contained in Q-0016 (any MPC change by 31.12) |
| K3-10 | Accepted with correction | Q-0075 (panel) | Direction and threshold changed (below 3.5%) |
| K3-11 | Accepted | Q-0086 | — |
| **K3-12** | **Rejected (deferred)** | — | FIN vector already the largest (7 new); RU_FINANCE kept as indicator I21 |
| **K3-13** | **Rejected (deferred)** | — | Same reason; UST10Y kept as indicator I18a |
| **K3-14** | **Rejected** | — | RATES_ECB covered by Q-0017; flash HICP after the edition-03 window |
| K3-15 | Accepted | Q-0105 | Partial overlap with Q-0070 noted |
| **K3-16** | **Rejected** | — | Depends on the format of the Bank of Russia forecast table; the decision itself is covered by Q-0020 and Q-0088 |
| K3-17 | Accepted | Q-0112 | — |
| **K3-18** | **Rejected** | — | Current NBP gold tonnage disputed (about 673 t vs 693.8 t, G3-079) — the threshold's position relative to the state is unknown |
| K4-01 | Accepted | Q-0081 | In-person, same room |
| K4-02 | Merged | Q-0096 | Impeachment vote merged into removal from office |
| K4-03 | Accepted | Q-0096 | — |
| **K4-04** | **Rejected** | — | **Possibly resolved before the forecasts:** Kremlin 08.10 — no call scheduled; a Russian state outlet (no_republish, not opened) reported on 09.10 that Ushakov announced a call had taken place. The window 08.10–21.10 may already be satisfied |
| K4-05 | Replaced | Q-0100 | Three-way meeting depends on Putin's APEC attendance and on Q-0030; the attendance question is the cleaner test |
| K4-06 | Accepted | Q-0101 | — |
| K4-07 | Accepted | Q-0093 | — |
| K4-08 | Accepted with correction | Q-0094 | Joint lists with Likud count; tie = NO |
| **K4-09** | **Rejected** | — | Composition of the "outgoing coalition" not verified for 2026 (parties' exits and re-entries) — ambiguous criterion |
| **K4-10** | **Rejected** | — | p_status_quo undeterminable (caretaker continuity vs new vote); weak PIR link |
| K4-11 | Replaced | Q-0111 | Unclear whether a formal Inatsisartut vote is required; entry into force is unambiguous |
| **K4-12** | **Rejected** | — | VENEZUELA covered by Q-0034; weak PIR link |
| **K4-13** | **Rejected** | — | p_status_quo undeterminable (scheduled election vs Israeli obstruction); weak PIR link |
| **K4-14** | **Rejected** | — | Weak PIR link (Horn of Africa); kept in section B |
| **K4-15** | **Rejected** | — | Non-binding regional resolution; low decision value |

New questions not from stage 02 candidates: Q-0077 (panel), Q-0082 (short version of Q-0026, from G4-021/G4-022), Q-0088 (Bank of Russia hike — complements Q-0020), Q-0091 (rolling successor of Q-0061), Q-0095 (Senate — PIR-2), Q-0109 (NDAA — PIR-2), Q-0110 (ceasefire, long), Q-0114 (base location, long successor of Q-0044), Q-0115 (Brent < 70, long; tests KA7).

## 5. Statistics

**Horizons of new questions (§3.3)** — deadline counted from the creation date 07.10.2026:

| Horizon | Panel | Open | Total | Share | §3.3 target |
|---|---|---|---|---|---|
| To the next edition (≤ 24.10.2026) | 1 | 14 | 15 | 36% | about 40% |
| To the end of the quarter (25.10–31.12.2026) | 2 | 18 | 20 | 48% | about 40% |
| Longer (after 31.12.2026) | 1 | 6 | 7 | 17% | about 20% |

Deviation: the quarter bucket is 8 pp above target, because several decision dates fall at the end of October and in November (Bulgaria, Israel, S&P, BIS, APEC, EU sectoral package). The short bucket is limited by the lag of resolution sources (PortWatch, GAC) and by the triviality risk of very short windows.

**Vectors:**

| Vector | New panel | New open | New total | ACTIVE after the stage (panel + open) |
|---|---|---|---|---|
| MIL | 0 | 6 | 6 | 15 (5 + 10) |
| ENE | 1 | 5 | 6 | 12 (5 + 7) |
| ECO | 3 | 2 | 5 | 7 (5 + 2) |
| FIN | 0 | 7 | 7 | 15 (5 + 10) |
| TEC | 0 | 3 | 3 | 8 (5 + 3) |
| DIP | 0 | 6 | 6 | 12 (5 + 7) |
| DOM | 0 | 5 | 5 | 10 (5 + 5) |
| INF | 0 | 4 | 4 | 9 (5 + 4) |
| **Total** | **4** | **38** | **42** | **88 (40 + 48)** |

ACTIVE includes Q-0037 and Q-0049 (deadline passed, awaiting data). TEC open questions: 0 in edition 01 → 3 now. ECO open remains the thinnest (2 open) — candidate for edition 03.

**PIR (new questions; a question may have several):** PIR-1 11, PIR-2 5, PIR-3 10, PIR-4 7, PIR-5 9, PIR-6 10, PIR-7 8. ACTIVE after the stage: PIR-1 23, PIR-2 11, PIR-3 21, PIR-4 17, PIR-5 19, PIR-6 20, PIR-7 15. PIR-2 (flagged as least covered in edition 01) rose from 8 to 11 but remains the least covered.

**p_status_quo:** 37 × 0.10, 3 × 0.50, 2 × 0.90. **who_benefits:** NONE 34, COMPROMISE 5, EU 2, RUSSIA 1.

**Clusters:** 44 labels among ACTIVE questions. Most populated: HORMUZ 6; OIL_PRICE 5; EU_ENERGY 5; CN_RARE_EARTHS, UA_TALKS, BAB_EL_MANDAB 4 each; EASTERN_FLANK, US_EUROPE 3 each. The weight of 1 per cluster (§8) limits their influence.

**Triviality (§3.8):** cannot be assessed before the forecasts. Risk controls in this stage: thresholds set near current values (Q-0074, Q-0084, Q-0085, Q-0086), candidates with a serial pattern rejected (K-G2-06), and a stricter "hit" definition in Q-0092. Check after stage 06.

## 6. Notes for later stages

- **Stage 04 (lenses run after 09.10):** events of 08–09.10 are new facts and must be verified on the web (CLAUDE.md §1) — in particular a Putin–Trump call reported on 09.10 (affects Q-0026, Q-0030, Q-0082), Iran's announced reply to the US proposal (Q-0028, Q-0081), the Council adoption of the listings on 12.10 (Q-0083, Q-0019).
- **Q-0019 vs Q-0083/Q-0104:** the label "22nd package" is disputed (TASS vs Euronews/Vlasiuk); Q-0083 and Q-0104 separate the listing track from the sectoral track; Q-0019's resolution wording remains as registered.
- **Q-0020 and Q-0088** are not complements: a hold on 23.10 resolves both NO.
- **Q-0077** depends on the user's decision on Q-0011 (VERIFY).
- **Stage 01 of edition 03:** PortWatch questions (Q-0078, Q-0079) need data to 17.10; Q-0103's December value is published in early January; Q-0095 may wait for runoffs.
- **Blocked domains for stages 03–05** used in this stage's searches: rule 3.9 list plus robinhood.com, poliwave.com, natesilver.net, racetothewh.com, wionews.com, betfair.com, oddschecker.com, 270towin.com, electionbettingodds.com. Search result lists in this stage included forecasting-style pages (vote-scope.com and uspollingdata.com, Senate projections) — not opened, not recorded, not used.
