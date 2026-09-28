# Stage 03 — Changes to the question bank (edition 01, state 23.09.2026)

Edition 01 sets the standing panel (methodology §3.1) and adds the first open questions. Registry before the stage: 0 questions. After the stage: **73 ACTIVE questions** (Q-0001…Q-0073) — panel 40 (5 × 8 vectors), open 33. No forecasts.

## 1. Rules applied in this edition

**Creation date** of all questions: 23.09.2026. Every criterion concerns events after 23.09.2026 (usually "between 24.09 and …"), so the events of 23.09 (Rubio–Lavrov, UN speeches) and 24.09 (Xi–Trump summit) are either outside the questions or their subject.

**Deadline of short questions:** 07.10.2026 — the indicative date of edition 02 (00_plan §1, to be confirmed by the user). "Rolling" panel questions (Q-0006, Q-0013, Q-0014, Q-0025, Q-0037) are replaced after resolution with an analogous question from the same vector and cluster with a new date (§3.1).

**Application of §3.5 (p_status_quo) — mechanical rules applied consistently:**
1. YES requires a new action by an actor (decree, strike, attack, listing, announcement, signature, agreement, rate change) → **0.10**. This also applies to recurring events (e.g. DPRK launches): without a new decision they will not occur.
2. Thresholds for continuous quantities (prices, exchange rates, storage, indices): YES on the same side of the threshold as the last known value → 0.90; on the opposite side → **0.10**. All thresholds in this edition lie on the opposite side of the last value, hence 0.10. A trend (e.g. gas injection) is not a "state" — the level counts.
3. Elections: YES = the incumbent keeps office or majority → **0.90** (Q-0031, Q-0033); questions about a new configuration with no counterpart in the current state (largest group in the new Saeima, result > 50% in the first round) → **0.50**.
4. The current value lies exactly at the threshold or there are no data on the current state → **0.50** (Q-0047, Q-0053, Q-0054).
5. A pre-scheduled event without a direction (Q-0029 — Trump's attendance at APEC) → **0.50**.

Result: 65 × 0.10, 6 × 0.50, 2 × 0.90. The predominance of 0.10 follows from the construction of the questions ("will something change"), not from judgement.

**who_benefits (§3.6):** entered only where YES clearly strengthens an actor at another's expense; in case of doubt NONE. COMPROMISE — for questions in which YES means an agreement between opponents (truce, extension of a suspension, treaty). Distribution: NONE 58, COMPROMISE 7, RUSSIA 3, UKRAINE 2, EU 1, CHINA 1, US_WEST 1. In six proposals from 00, who_benefits was changed to NONE (P-002, P-003, P-005, P-013, P-021, P-027) — rationale in the question notes.

**Clusters (§3.4):** 43 labels. Interest rates were split into RATES_PL, RATES_ECB, RATES_FED and RATES_RU, because decisions of different central banks are not the same outcome. New labels outside the §3.4 examples (an illustrative list): PL_FUELS, PL_INFLATION, PL_FINANCE, PLN, FOOD, OPEC, US_EU_TRADE, US_CHINA_TECH, US_CHINA_SUMMITS, RU_SANCTIONS_US, RU_SANCTIONS_EU, RU_DOMESTIC, IRAN_WAR, IRAN_LEADERSHIP, KOREA, PANAMA, BALTIC_INFRA, BRAZIL_ELECTIONS, LATVIA_ELECTIONS, CAUCASUS, UA_USA, UA_FUNDING.

**Measuring Hormuz.** Questions Q-0036 and Q-0037 are resolved by IMF PortWatch (AIS). The series may not cover escorted traffic without transponders (contradiction G1-001 vs G2-006; 03_analysis §1.1 C). The criterion stays because it is unambiguous and public; the caveat is in the question notes.

**Oil — source.** The proposals from 00 and the G2 candidates pointed to the EIA RBRTE series (spot). Questions Q-0006–Q-0008 use the ICE Brent front-month contract, because the reference state (99.25 USD, 22.09) refers to futures, and spot Dated Brent deviated from them by more than ten USD (IEA: 113.48 USD on 09.09, G2-010) — with EIA the threshold would have no clear reference to the current state.

## 2. New questions

### 2.1 Standing panel (40)

| ID | Vector | Cluster | Question | Deadline | p_sq | who_benefits | PIR |
|---|---|---|---|---|---|---|---|
| Q-0001 | MIL | RU_MOBILIZATION | Will the president of Russia sign by 31.12.2026 a decree announcing mobilisation (general or partial)? | 31.12.2026 | 0.10 | NONE | PIR-1 |
| Q-0002 | MIL | EASTERN_FLANK | Will at least one person be killed on the territory of a NATO state by a Russian drone or missile strike by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-1; PIR-2 |
| Q-0003 | MIL | US_EUROPE | Will the Pentagon or the White House announce by 31.03.2027 a decision to reduce the number of US troops in Europe by at least 10,000? | 31.03.2027 | 0.10 | RUSSIA | PIR-2 |
| Q-0004 | MIL | UA_FRONT | Will the net gain of Ukrainian territory occupied by Russia in October 2026 exceed 200 km² according to DeepState? | 31.10.2026 | 0.10 | RUSSIA | PIR-1 |
| Q-0005 | MIL | TAIWAN | Will the PRC Eastern Theater Command announce named military exercises around Taiwan by 31.03.2027? | 31.03.2027 | 0.10 | NONE | PIR-4 |
| Q-0006 | ENE | OIL_PRICE | Will the settlement price of the ICE Brent front-month contract on 06.10.2026 exceed 100.00 USD/bbl? | 06.10.2026 | 0.10 | NONE | PIR-3; PIR-5 |
| Q-0007 | ENE | OIL_PRICE | Will the settlement price of the ICE Brent front-month contract exceed 120 USD/bbl on any trading day between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-3; PIR-5 |
| Q-0008 | ENE | OIL_PRICE | Will the settlement price of the ICE Brent front-month contract fall below 80 USD/bbl on any trading day between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-3; PIR-5 |
| Q-0009 | ENE | EU_ENERGY | Will the settlement price of the TTF front-month contract exceed 90 EUR/MWh on any trading day between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-3 |
| Q-0010 | ENE | EU_ENERGY | Will EU gas storage fill per GIE AGSI+ on gas day 01.01.2027 be below 55.0%? | 01.01.2027 | 0.10 | NONE | PIR-3 |
| Q-0011 | ECO | US_CHINA_TRADE | Will the governments of the USA and the PRC both announce by 10.11.2026 an extension of the trade (tariff) truce or a new trade agreement replacing it? | 10.11.2026 | 0.10 | COMPROMISE | PIR-4 |
| Q-0012 | ECO | RU_SANCTIONS_US | Will the US president impose a tariff under H.R. 5334 on goods from at least one country other than Russia by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-1; PIR-4; PIR-6 |
| Q-0013 | ECO | PL_INFLATION | Will the Statistics Poland (GUS) flash estimate of CPI inflation for September 2026 be at least 3.5% y/y? | 30.09.2026 | 0.10 | NONE | PIR-6; PIR-3 |
| Q-0014 | ECO | FOOD | Will the FAO Food Price Index (FFPI) for September 2026 be higher than 133.3 points? | 09.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0015 | ECO | US_EU_TRADE | Will the USA introduce a tariff on EU goods exceeding the 15% ceiling set in the 2026 agreement by 31.03.2027? | 31.03.2027 | 0.10 | NONE | PIR-6 |
| Q-0016 | FIN | RATES_PL | Will the Monetary Policy Council change the NBP reference rate at any meeting between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-6 |
| Q-0017 | FIN | RATES_ECB | Will the ECB raise the deposit rate at a meeting held between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-6 |
| Q-0018 | FIN | CN_SECONDARY_SANCTIONS | Will OFAC add to the SDN list by 31.03.2027 a bank registered in mainland PRC in connection with Iran or Russia? | 31.03.2027 | 0.10 | NONE | PIR-4; PIR-5; PIR-6 |
| Q-0019 | FIN | RU_SANCTIONS_EU | Will the EU Council adopt the 22nd package of sanctions against Russia by 31.12.2026? | 31.12.2026 | 0.10 | EU | PIR-1; PIR-6 |
| Q-0020 | FIN | RATES_RU | Will the Bank of Russia cut its key rate at the meeting scheduled for 23.10.2026? | 23.10.2026 | 0.10 | NONE | PIR-1; PIR-6 |
| Q-0021 | TEC | CN_RARE_EARTHS | Will the PRC announce by 10.11.2026 an extension or repeal of the suspension of the rare-earth export controls introduced on 09.10.2025? | 10.11.2026 | 0.10 | COMPROMISE | PIR-4 |
| Q-0022 | TEC | CN_RARE_EARTHS | Will the PRC announce by 27.11.2026 an extension or repeal of the suspension of the ban on exports of gallium, germanium, antimony and superhard materials to the USA? | 27.11.2026 | 0.10 | COMPROMISE | PIR-4 |
| Q-0023 | TEC | US_CHINA_TECH | Will MOFCOM add at least one US entity to the export control list or the unreliable entity list between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-4 |
| Q-0024 | TEC | US_CHINA_TECH | Will the US government permit exports to the PRC of Nvidia AI chips with the Blackwell architecture or newer by 31.12.2026? | 31.12.2026 | 0.10 | CHINA | PIR-4 |
| Q-0025 | TEC | CN_RARE_EARTHS | Will PRC exports of rare-earth permanent magnets to the USA in September 2026 exceed 512 t? | 20.10.2026 | 0.10 | NONE | PIR-4 |
| Q-0026 | DIP | UA_TALKS | Will a trilateral meeting of government delegations of the USA, Ukraine and Russia take place by 30.11.2026? | 30.11.2026 | 0.10 | NONE | PIR-1; PIR-7 |
| Q-0027 | DIP | EASTERN_FLANK | Will any NATO state submit a request for consultations under Article 4 of the North Atlantic Treaty between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-1; PIR-2 |
| Q-0028 | DIP | HORMUZ | Will the USA and Iran announce by 31.12.2026 the conclusion of an agreement (framework, interim or final) that includes the opening of the Strait of Hormuz? | 31.12.2026 | 0.10 | COMPROMISE | PIR-5; PIR-3 |
| Q-0029 | DIP | US_CHINA_SUMMITS | Will Donald Trump personally attend the APEC leaders' meeting in Shenzhen (18–19.11.2026)? | 19.11.2026 | 0.50 | NONE | PIR-4 |
| Q-0030 | DIP | UA_TALKS | Will Vladimir Putin and Donald Trump meet in person by 31.03.2027? | 31.03.2027 | 0.10 | NONE | PIR-1; PIR-2 |
| Q-0031 | DOM | US_ELECTIONS | Will the Republican Party win at least 218 seats in the House of Representatives in the 03.11.2026 elections? | 31.12.2026 | 0.90 | NONE | PIR-2; PIR-7 |
| Q-0032 | DOM | IRAN_LEADERSHIP | Will a new video or audio recording of Mojtaba Khamenei speaking be published by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-5; PIR-7 |
| Q-0033 | DOM | BRAZIL_ELECTIONS | Will Luiz Inácio Lula da Silva win the 2026 presidential election in Brazil (first round 04.10 or second round 25.10)? | 31.10.2026 | 0.90 | NONE | PIR-7 |
| Q-0034 | DOM | VENEZUELA | Will the CNE or the government of Venezuela announce a specific date for the presidential election by 31.03.2027? | 31.03.2027 | 0.10 | NONE | PIR-7 |
| Q-0035 | DOM | SAHEL | Will Assimi Goïta cease to hold power in Mali by 31.03.2027 (coup, resignation, death or capture of Bamako by JNIM or the FLA)? | 31.03.2027 | 0.10 | NONE | PIR-7 |
| Q-0036 | INF | HORMUZ | Will the 7-day average number of transits through the Strait of Hormuz per IMF PortWatch exceed 40 ships per day on any day between 24.09 and 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-5; PIR-3 |
| Q-0037 | INF | HORMUZ | Will IMF PortWatch record at least 20 transits through the Strait of Hormuz on any day between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-5; PIR-3 |
| Q-0038 | INF | HORMUZ | Will the USA officially lift or suspend the naval blockade of Iranian ports by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-5 |
| Q-0039 | INF | PANAMA | Will the Panama Canal Authority raise the daily transit limit above 32 by 31.10.2026? | 31.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0040 | INF | BALTIC_INFRA | Will the government or prosecutor of a Baltic Sea state announce by 31.03.2027 damage to a subsea cable or pipeline in the Baltic together with proceedings concerning external action? | 31.03.2027 | 0.10 | NONE | PIR-1; PIR-3 |

### 2.2 Open questions (33)

| ID | Vector | Cluster | Question | Deadline | p_sq | who_benefits | PIR |
|---|---|---|---|---|---|---|---|
| Q-0041 | MIL | IRAN_WAR | Will CENTCOM or the Pentagon announce a US strike on a target on Iranian land territory between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-5 |
| Q-0042 | DIP | HORMUZ | Will another round of talks between representatives of the US and Iranian governments (direct or indirect) take place between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-5 |
| Q-0043 | MIL | BAB_EL_MANDAB | Will Saudi Arabia confirm a missile or drone attack from Yemen aimed at Riyadh between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-5; PIR-3 |
| Q-0044 | MIL | US_EUROPE | Will the US or Polish government officially announce by 07.10.2026 the location of a new permanent US Army base in Poland? | 07.10.2026 | 0.10 | NONE | PIR-2 |
| Q-0045 | MIL | EASTERN_FLANK | Will the Polish Operational Command (DO RSZ) or the Ministry of National Defence confirm a violation of Polish airspace by an object from the direction of Russia or Belarus between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-1 |
| Q-0046 | MIL | KOREA | Will the DPRK launch a ballistic missile between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-4 |
| Q-0047 | MIL | TAIWAN | Will Taiwan's Ministry of National Defense report at least 20 PLA aircraft around Taiwan in a daily report between 24.09 and 07.10.2026? | 07.10.2026 | 0.50 | NONE | PIR-4 |
| Q-0048 | ENE | EU_ENERGY | Will the settlement price of the TTF front-month contract on 06.10.2026 exceed 75.00 EUR/MWh? | 06.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0049 | ENE | EU_ENERGY | Will EU gas storage fill per GIE AGSI+ on gas day 06.10.2026 exceed 73.0%? | 06.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0050 | ENE | PL_FUELS | Will the national average price of diesel in the e-petrol weekly quotation of 07.10.2026 exceed 9.00 PLN/l? | 07.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0051 | ENE | OPEC | Will the OPEC+ states with voluntary cuts announce at the 04.10.2026 meeting an increase in required production for November 2026? | 07.10.2026 | 0.10 | NONE | PIR-3 |
| Q-0052 | FIN | PLN | Will the NBP average EUR/PLN rate of 07.10.2026 be higher than 4.3500? | 07.10.2026 | 0.10 | NONE | PIR-6 |
| Q-0053 | FIN | RU_FINANCE | Does the draft Russian federal budget law for 2027 submitted to the Duma by 07.10.2026 provide for a deficit of at least 2.0% of GDP? | 07.10.2026 | 0.50 | NONE | PIR-1; PIR-6 |
| Q-0054 | DOM | RU_DOMESTIC | Will A Just Russia obtain at least 5.00% of the vote in the final results of the Duma elections announced by the Central Election Commission? | 30.09.2026 | 0.50 | NONE | PIR-7 |
| Q-0055 | DOM | LATVIA_ELECTIONS | Will the United List (Apvienotais saraksts) win the most seats in the elections to the Latvian Saeima on 03.10.2026? | 10.10.2026 | 0.50 | NONE | PIR-7 |
| Q-0056 | DOM | BRAZIL_ELECTIONS | Will Lula da Silva win more than 50% of valid votes in the first round of the presidential election on 04.10.2026? | 05.10.2026 | 0.50 | NONE | PIR-7 |
| Q-0057 | ECO | US_CHINA_TRADE | Will the USA publish between 24.09 and 07.10.2026 an overcapacity report recommending tariffs on the PRC, or announce a new tariff rate on PRC goods? | 07.10.2026 | 0.10 | NONE | PIR-4 |
| Q-0058 | ECO | US_CHINA_TRADE | Will the governments of the USA and the PRC both announce by 07.10.2026 an extension of the trade (tariff) truce or a new trade agreement? | 07.10.2026 | 0.10 | COMPROMISE | PIR-4 |
| Q-0059 | DIP | UA_TALKS | Will Russia and Ukraine both officially confirm by 07.10.2026 an agreement in force on a mutual halt to strikes on energy infrastructure? | 07.10.2026 | 0.10 | COMPROMISE | PIR-1; PIR-3 |
| Q-0060 | FIN | CN_SECONDARY_SANCTIONS | Will OFAC add to the SDN list an entity from the PRC or Hong Kong in connection with Iran between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-4; PIR-5 |
| Q-0061 | FIN | RU_SANCTIONS_US | Will OFAC add a new entity to the SDN list in connection with Russia between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-1; PIR-6 |
| Q-0062 | INF | BAB_EL_MANDAB | Will UKMTO or JMIC report an attack on a merchant ship in the Red Sea, Bab el-Mandeb or the Gulf of Aden between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-5; PIR-3 |
| Q-0063 | INF | HORMUZ | Will UKMTO or JMIC confirm a hit on a merchant ship in the Persian Gulf, the Strait of Hormuz or the Gulf of Oman between 24.09 and 07.10.2026? | 07.10.2026 | 0.10 | NONE | PIR-5 |
| Q-0064 | DIP | UA_USA | Will the USA and Ukraine sign an intergovernmental drone agreement by 07.10.2026? | 07.10.2026 | 0.10 | UKRAINE | PIR-1; PIR-2 |
| Q-0065 | MIL | IRAN_WAR | Will CENTCOM or the Pentagon announce a US strike on a target on Iranian land territory by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-5 |
| Q-0066 | FIN | RATES_FED | Will the FOMC raise the target range for the federal funds rate at the 27–28.10.2026 meeting? | 28.10.2026 | 0.10 | NONE | PIR-6 |
| Q-0067 | ENE | EU_ENERGY | Will EU gas storage fill per GIE AGSI+ on gas day 01.11.2026 be at least 80.0%? | 01.11.2026 | 0.10 | NONE | PIR-3 |
| Q-0068 | MIL | BAB_EL_MANDAB | Will US forces carry out a strike on Houthi targets in Yemen by 31.12.2026? | 31.12.2026 | 0.10 | NONE | PIR-5; PIR-2 |
| Q-0069 | MIL | TAIWAN | Will the DSCA notify Congress by 31.12.2026 of arms sales to Taiwan with a combined value of at least 1 bn USD? | 31.12.2026 | 0.10 | US_WEST | PIR-4 |
| Q-0070 | FIN | PL_FINANCE | Will Fitch or S&P downgrade Poland's long-term foreign-currency rating by 31.03.2027? | 31.03.2027 | 0.10 | NONE | PIR-6 |
| Q-0071 | FIN | UA_FUNDING | Will the EU Council adopt by 30.06.2027 a legal act allowing the frozen assets of the Bank of Russia themselves (not only windfall profits) to be used for Ukraine? | 30.06.2027 | 0.10 | UKRAINE | PIR-1; PIR-6 |
| Q-0072 | DIP | CAUCASUS | Will Armenia and Azerbaijan sign a peace treaty by 30.06.2027? | 30.06.2027 | 0.10 | COMPROMISE | PIR-7 |
| Q-0073 | MIL | UA_FRONT | Will ISW assess by 30.06.2027 that Russian forces have taken control of the whole of Kramatorsk or the whole of Sloviansk? | 30.06.2027 | 0.10 | RUSSIA | PIR-1 |

## 3. Replacements

None — this is the first edition with a registry; no panel question has been resolved yet.

## 4. Proposals from edition 00 — decisions (28)

| Proposal | Decision | Question | Reason / change |
|---|---|---|---|
| P-001 | Accepted with correction | Q-0021 | Merged with K-G2-06; "or repeal" added; MOFCOM announcements specified |
| P-002 | Accepted with correction | Q-0018 | "Majority state ownership by the PRC" hard to verify → "bank registered in mainland PRC"; Russia added (H.R. 5334); deadline 31.03.2027; who_benefits → NONE |
| P-003 | Accepted | Q-0036 | who_benefits COMPROMISE → NONE; AIS caveat |
| **P-004** | **Rejected** | → Q-0028, Q-0042 | **Resolved before the creation date:** the round of 22.09 confirmed by both sides (Witkoff — G4-006; Iranian MFA spokesman — G4-008). Replaced by a question about an agreement (panel) and about the next round (open) |
| P-005 | Accepted | Q-0026 | who_benefits COMPROMISE → NONE (a meeting is not an agreement) |
| P-006 | Accepted with correction | Q-0001 | Conscription in 2026 is year-round (00_plan §2) — narrowed to a decree announcing mobilisation; reserve formations excluded |
| P-007 | Accepted as open | Q-0069 | The MIL vector of the panel has five questions with higher PIR-1/PIR-2 priority |
| P-008 | Accepted with correction | Q-0010 | Threshold 45% → 55% (with a projection of approx. 78% on 01.11, the 45% threshold would require an extreme winter — risk of triviality, §3.8) |
| P-009 | Accepted with correction | Q-0009 | Threshold 100 → 90 EUR/MWh (state 71–74, IX peak 84); source specified |
| P-010 | Accepted with correction | Q-0007 | Source: ICE contract (consistency with Q-0006) |
| P-011 | Accepted with correction | Q-0008 | As P-010 |
| **P-012** | **Rejected** | — | **Resolved before the creation date:** the restart of the East–West pipeline on 22.09 was confirmed by at least two independent media (Reuters citing 3 sources; Al Arabiya, Al Khaleej — G2-008), which meets the proposal's criterion. The INF vector of the panel was filled with questions Q-0038–Q-0040 |
| P-013 | Accepted | Q-0002 | who_benefits RUSSIA → NONE |
| P-014 | Accepted | Q-0027 | No substantive changes |
| P-015 | Accepted | Q-0016 | Period from 24.09 |
| P-016 | Accepted with correction | Q-0017 | The hike of 10.09 happened before the creation date — the question concerns meetings after 23.09 |
| P-017 | Accepted | Q-0031 | Resolution specified for uncalled seats |
| **P-018** | **Rejected** | → Q-0003 | Ambiguous criterion: rotations change routinely, and "reduction of the rotational presence" has no public measure; signals point rather to an increase in PL. Replaced by a question about a decision to reduce by ≥ 10k in Europe |
| **P-019** | **Rejected** | → Q-0044 | Unverifiable criterion: no public record of US troop strength in PL, "additional under the announcement of 21.05" cannot be separated from rotations. Replaced by a question about the base location |
| P-020 | Accepted with correction | Q-0032 | Merged with K4-15; the recording must be new (after 23.09) |
| P-021 | Accepted | Q-0029 | who_benefits COMPROMISE → NONE; the case of a cancelled summit specified |
| P-022 | Accepted as open | Q-0073 | Deadline 31.12 → 30.06.2027 (a pace of approx. 150 km²/4 weeks makes the 31.12 deadline close to trivial); in the UA_FRONT panel it is replaced by Q-0004 (DeepState, monthly) |
| P-023 | Accepted | Q-0019 | No substantive changes |
| P-024 | Accepted with correction | Q-0034 | Deadline → 31.03.2027 (replacement of the TSJ and CNE in progress) |
| P-025 | Accepted with correction | Q-0035 | Deadline → 31.03.2027; the junta leader named |
| P-026 | Accepted as open, reworded | Q-0053 | The 2.0% threshold equals the announced "approx. 2%" (G3-019) → p_status_quo 0.50; threshold "≥ 2.0%"; deadline 07.10 (submission approx. 29.09–01.10) |
| P-027 | Accepted with correction | Q-0005 | Deadline → 31.03.2027; who_benefits CHINA → NONE |
| P-028 | Accepted with correction | Q-0011 | Merged with K3-03; deadline → 10.11 (truce expiry date); short version Q-0058 |

## 5. Unused candidates from stage 02 (with reason)

| Candidate | Reason |
|---|---|
| G1 K11 (USS George Washington in Yokosuka by 31.12) | Dependent on the IRAN_WAR cluster; weak link with decisions by the deadline |
| G1 K12 (DPRK ICBM by 31.12) | The MIL vector is already the most numerous (15); Korea covered by the short question Q-0046 |
| G1 K14 (shoot-down of an object over Poland by 31.12) | Strongly dependent on Q-0002 and Q-0045 (EASTERN_FLANK) |
| K-G2-01, K-G2-02 | Replaced by Q-0006, Q-0007 (ICE contract instead of EIA — §1) |
| K-G2-09 (full E-W capacity — official statement) | "Full capacity" criterion ambiguous; Aramco does not comment on flows |
| K-G2-10 (Qatar–Edison force majeure) | Dependent on HORMUZ; resolved by one company's statement |
| K-G2-11 (extension of the Russian diesel export ban) | Extensions are serial (precedents IX 2026) — risk of triviality (§3.8) |
| K-G2-13 (renewed VAT cut or maximum fuel price in PL) | No government signal (G2 §3: gap); to be considered in edition 02 |
| K3-02 (H.R. 5334 tariff on China) | Contained in Q-0012; would duplicate the cluster |
| K3-05 (Russian budget in third reading ≥ 2.0%) | Replaced by the short version Q-0053 (third reading after 30.11 would give NO regardless of the deficit) |
| K3-08 (ECB 29.10), K3-09 (MPC 07.10) | Contained in Q-0017 and Q-0016 |
| K4-06 (ratification of the Greenland agreement by the Inatsisartut) | No meeting date; weak link with PIRs within the horizon |
| K4-10 (Democratic majority in the House) | Complement of Q-0031 — duplicate |
| K4-12 (election date in Venezuela) | = P-024 → Q-0034 |
| K4-13 (new composition of the TSJ in Venezuela) | Dependent on the VENEZUELA cluster; PIR-7 covered |

## 6. Statistics

**Horizons (§3.3)** — deadline counted from the creation date 23.09.2026:

| Horizon | Panel | Open | Total | Share | §3.3 target |
|---|---|---|---|---|---|
| To the next edition (≤ 10.10.2026) | 4 | 24 | 28 | 38% | approx. 40% |
| To the end of the quarter (11.10–31.12.2026) | 27 | 5 | 32 | 44% | approx. 40% |
| Longer (after 31.12.2026) | 9 | 4 | 13 | 18% | approx. 20% |

Note: three short questions have deadlines on 09–10.10 (FAO, Latvia, CVK results) — in `scores.py` they will fall into the "≤ 100 days" bin, because the forecasts will be made around 24–25.09.

**Vectors:**

| Vector | Panel | Open | Total |
|---|---|---|---|
| MIL | 5 | 10 | 15 |
| ENE | 5 | 5 | 10 |
| ECO | 5 | 2 | 7 |
| FIN | 5 | 7 | 12 |
| TEC | 5 | 0 | 5 |
| DIP | 5 | 4 | 9 |
| DOM | 5 | 3 | 8 |
| INF | 5 | 2 | 7 |
| **Total** | **40** | **33** | **73** |

**PIR (questions may have several):** PIR-1 — 17, PIR-2 — 8, PIR-3 — 20, PIR-4 — 16, PIR-5 — 17, PIR-6 — 14, PIR-7 — 10. PIR-2 is the least covered — a candidate for supplementing in edition 02.

**Clusters with the most questions:** HORMUZ 6; EU_ENERGY 5; 3 each: EASTERN_FLANK, TAIWAN, OIL_PRICE, US_CHINA_TRADE, CN_RARE_EARTHS, UA_TALKS, BAB_EL_MANDAB. The weight of 1 per cluster (§8) limits the influence of these clusters on the score.

**Triviality (§3.8):** cannot be assessed before the forecasts. The risk of questions close to 0 or 1 was reduced by raising or lowering thresholds from the 00 proposals (P-008, P-009, P-022) and rejecting candidates with a serial pattern (K-G2-11). Check after stage 06.

## 7. Notes for later stages

- Stage 04: questions Q-0011, Q-0021, Q-0022, Q-0024, Q-0029, Q-0057, Q-0058, Q-0060 depend on the 24.09 summit, which takes place after the state date. The lenses forecast without knowing its outcome, unless stage 04 is run after 24.09 — then the summit outcome is a new fact (CLAUDE.md §1) that must be verified on the web.
- Stage 01 of edition 02: first resolutions — Q-0013 (30.09), Q-0054 (30.09), Q-0056 (05.10), Q-0006 and Q-0048/Q-0049 (06.10), the other short ones 07–10.10. PortWatch data (Q-0037) and FAO (Q-0014) may require postponing resolution until publication.
- The date of edition 02 (07.10) has not been confirmed by the user; if it changes, the deadlines of short questions stay unchanged (append-only registry).
