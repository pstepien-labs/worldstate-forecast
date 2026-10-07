# Edition 02 — resolutions (stage 01)

Stage 01 run on 08.10.2026 (00:38–) for the state date 07.10.2026. Input: `00_plan.md` §3, `registry/questions.csv`, methodology §3.7, §7–§8. Model: claude-opus-5-5. This file contains no probabilities.

## 1. Summary

| Item | Count |
|---|---|
| Questions on the stage 00 list with deadline ≤ 07.10.2026 | 26 |
| Resolved in this stage (rows appended to `registry/resolutions.csv`, version 1) | 27 (25 with a passed deadline + Q-0014 and Q-0055, whose event has already occurred) |
| Outcome YES / NO | 16 / 11 |
| VOID | 0 |
| Flagged VERIFY | 10 (6 ambiguous or disputed + 4 drawn at random) |
| Deadline passed but **not resolved** (resolution source not yet available) | 2 (Q-0037, Q-0049) — status stays ACTIVE |
| Later deadline, event not (yet) occurred — stays ACTIVE | all other questions (see §4) |

`registry/questions.csv`: `status` changed to RESOLVED for the 27 questions; `notes` extended for them and for Q-0021, Q-0037, Q-0039, Q-0049. No other field changed (checked against HEAD).

## 2. Resolutions

Outcome: 1 = YES, 0 = NO. Date = day the event occurred (YES) or deadline (NO). Conf. = resolution confidence.

| ID | Outcome | Date | Evidence (publisher, date) | Second source | Conf. | VERIFY |
|---|---|---|---|---|---|---|
| Q-0006 | 1 | 06.10.2026 | Investing.com, Brent historical data (LCOZ6), accessed 08.10 — [link](https://www.investing.com/commodities/brent-oil-historical-data) | Bloomberg via Rigzone, 07.10 — [link](https://rigzone.com/news/wire/oil_dips_as_middle_east_flows_recover-07-oct-2026-184796-article) | medium | Y (ambiguous) |
| Q-0011 | 1 | 28.09.2026 | Xinhua: MOFCOM reading of the 8th round, 28.09 — [link](https://www.news.cn/world/20260928/218d41a6ec924cf88bf3085936ef0c91/c.html) | NBC News, 23.09 (Bessent) — [link](https://www.nbcnews.com/business/economy/us-china-extend-trade-truce-trump-rcna599525) | low | Y (disputed) |
| Q-0013 | 1 | 30.09.2026 | GUS flash estimate, 30.09 — [link](https://publikacje.new.stat.gov.pl/en/publications-portal/flash-estimate-consumer-price-index-september-2026) | rp.pl, 30.09 — [link](https://www.rp.pl/dane-gospodarcze/art45213841-duzy-wzrost-inflacji-w-polsce-sa-nowe-dane-gus-tak-zle-nie-bylo-od-dawna) | high | N |
| Q-0014 | 1 | 02.10.2026 | FAO FFPI release, 02.10 — [link](https://www.fao.org/worldfoodsituation/foodpricesindex/en/) | Forbes, 02.10 — [link](https://www.forbes.com/sites/conormurray/2026/10/02/global-food-prices-approach-four-year-high-un-says/) | high | Y (random) |
| Q-0041 | 0 | 07.10.2026 | Wikipedia, "September 2026 United States strikes on Iran" (compilation) — [link](https://en.wikipedia.org/wiki/September_2026_United_States_strikes_on_Iran) | Washington Times, 04.10 — [link](https://washingtontimes.com/news/2026/oct/4/iranian-leaders-focus-diplomatic-talks-us-adds-military-muscle) | medium | Y (random) |
| Q-0042 | 0 | 07.10.2026 | Al Jazeera, 29.09 — [link](https://www.aljazeera.com/news/2026/9/29/irans-araghchi-meets-qatari-mediators-as-us-insists-on-nuclear-talks) | Iran International (citing Reuters), 28.09 — [link](https://www.iranintl.com/en/202609283428) | medium | Y (disputed) |
| Q-0043 | 1 | 26.09.2026 | SPA via GlobalSecurity, 26.09 — [link](https://www.globalsecurity.org/wmd/library/news/saudi/2026/saudi-260926-spa03.htm) | Times of Israel, 26.09 — [link](https://www.timesofisrael.com/saudi-coalition-says-intercepted-houthi-drones-headed-for-riyadh) | high | N |
| Q-0044 | 0 | 07.10.2026 | TVN24, 05.10 — [link](https://tvn24.pl/swiat/donald-trump-zapytany-o-stala-baze-wojsk-usa-w-polsce-tak-odpowiedzial-st9271157) | Defence24, 05.10 — [link](https://defence24.pl/polityka-obronna/stala-baza-usa-w-polsce-pozostaly-kwestie-techniczne) | high | N |
| Q-0045 | 0 | 07.10.2026 | Portal Obronny (DO RSZ statement), 07.10 — [link](https://portalobronny.se.pl/aktualnosci/dorsz-zakonczylo-operowanie-lotnictwa-wojskowego-polska-przestrzen-powietrzna-nie-zostala-naruszona-aa-dTA5-RBmQ-Qsae.html) | Defence24 (Mi-8, 23.09) — [link](https://defence24.pl/polityka-obronna/rosyjski-smiglowiec-naruszyl-polska-przestrzen-powietrzna) | medium | N |
| Q-0046 | 1 | 03.10.2026 | Bloomberg (JCS), 03.10 — [link](https://www.bloomberg.com/news/articles/2026-10-03/north-korea-fires-ballistic-missile-toward-east-coast-jcs-says) | Korea Herald — [link](https://www.koreaherald.com/article/10892386) | high | N |
| Q-0047 | 1 | 01.10.2026 | Taiwan MND daily report, 01.10 — [link](https://air.mnd.gov.tw/EN/News/News_Detail.aspx?CID=214&ID=59273) | The Defense Watch — [link](https://thedefensewatch.com/aerospace-aviation/taiwan-first-f16-block-70-fighters/) | high | N |
| Q-0048 | 1 | 06.10.2026 | Investing.com, Dutch TTF historical data, accessed 08.10 — [link](https://www.investing.com/commodities/dutch-ttf-gas-c1-futures-historical-data) | Trading Economics, EU natural gas — [link](https://tradingeconomics.com/commodity/eu-natural-gas) | medium | Y (ambiguous) |
| Q-0050 | 0 | 07.10.2026 | e-petrol.pl, quotation 07.10 — [link](https://www.e-petrol.pl/notowania/rynek-krajowy/ceny-stacje-paliw) | Gazeta Olsztyńska (PAP), 07.10 — [link](https://gazetaolsztynska.pl/artykul/paliwo-wyraznie-tansze-n2523670) | high | N |
| Q-0051 | 0 | 07.10.2026 | CNBC, 04.10 — [link](https://www.cnbc.com/2026/10/04/opec-agrees-to-keep-november-oil-output-targets-steady.html) | The National, 04.10 — [link](https://www.thenationalnews.com/business/energy/2026/10/04/opec-keeps-oil-output-targets-unchanged-for-november/) | high | N |
| Q-0052 | 1 | 07.10.2026 | NBP API, table A 195/A/NBP/2026 — [link](https://api.nbp.pl/api/exchangerates/rates/a/eur/2026-10-01/2026-10-07/?format=json) | nbp.pl table A — [link](https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/) | high | N |
| Q-0053 | 1 | 30.09.2026 | Kommersant, 01.10 — [link](https://www.kommersant.ru/doc/8991082) | Vedomosti, 24.09 — [link](https://www.vedomosti.ru/economics/news/2026/09/24/1231566-defitsit-federalnogo-byudzheta) | high | Y (random) |
| Q-0054 | 1 | 25.09.2026 | CEC resolution 53/356-9 of 25.09 (Garant) — [link](https://www.garant.ru/products/ipo/prime/doc/414878976/) | Life.ru, 25.09 — [link](https://life.ru/p/pamfilova-tsentrizbirkom-ofitsialno-utverdil-itogi-vyborov-v-gosdumu) | high | N |
| Q-0055 | 1 | 05.10.2026 | CVK provisional results, 05.10 12:23 — [link](https://www.cvk.lv/saeima-2026-rezultati) | LSM, 04.10 — [link](https://eng.lsm.lv/article/politics/election/04.10.2026-the-votes-are-in-united-list-handed-massive-mandate-by-latvian-voters.a666044/) | high | N |
| Q-0056 | 0 | 05.10.2026 | CartaCapital (TSE final count), 05.10 — [link](https://www.cartacapital.com.br/politica/tse-encerra-apuracao-do-1o-turno/) | Bloomberg results page — [link](https://www.bloomberg.com/graphics/2026-brazil-election/) | high | N |
| Q-0057 | 0 | 07.10.2026 | White House, presidential actions, accessed 08.10 — [link](https://www.whitehouse.gov/presidential-actions/) | Inside US Trade — [link](https://insidetrade.com/daily-news/sources-section-301-overcapacity-report-punted-after-trump-xi-summit) | medium | N |
| Q-0058 | 1 | 28.09.2026 | Xinhua: MOFCOM, 28.09 — [link](https://www.news.cn/world/20260928/218d41a6ec924cf88bf3085936ef0c91/c.html) | NBC News, 23.09 — [link](https://www.nbcnews.com/business/economy/us-china-extend-trade-truce-trump-rcna599525) | low | Y (disputed) |
| Q-0059 | 0 | 07.10.2026 | Axios, 24.09 — [link](https://www.axios.com/2026/09/24/zelensky-ukraine-russia-war-energy-ceasefire-grain) | Al Jazeera, 23.09 — [link](https://www.aljazeera.com/news/2026/9/23/zelenskyy-says-ukraine-ready-for-energy-truce-with-russia-after-trump-talks) | high | N |
| Q-0060 | 1 | 29.09.2026 | OFAC Recent Actions 29.09 — [link](https://ofac.treasury.gov/recent-actions/20260929) | OFAC Recent Actions 01.10 — [link](https://ofac.treasury.gov/recent-actions/20261001) | high | N |
| Q-0061 | 0 | 07.10.2026 | OFAC Recent Actions list, accessed 08.10 — [link](https://ofac.treasury.gov/recent-actions) | OFAC Recent Actions 01.10 — [link](https://ofac.treasury.gov/recent-actions/20261001) | high | N |
| Q-0062 | 1 | 04.10.2026 | The Maritime Executive (UKMTO), 04.10 — [link](https://maritime-executive.com/article/tanker-reports-attack-south-of-bab-el-mandeb) | Seatrade Maritime — [link](https://www.seatrade-maritime.com/security/product-tanker-attacked-in-red-sea-as-hostilities-escalate) | medium | Y (ambiguous) |
| Q-0063 | 1 | 01.10.2026 | Ship & Bunker (UKMTO), 02.10 — [link](https://shipandbunker.com/news/emea/780348-new-tanker-attack-reported-in-strait-of-hormuz-ukmto) | The Maritime Executive (UKMTO), 05.10 — [link](https://maritime-executive.com/article/ukmto-tanker-s-engine-room-on-fire-after-latest-hormuz-attack) | high | Y (random) |
| Q-0064 | 0 | 07.10.2026 | CBS News, IX 2026 — [link](https://www.cbsnews.com/news/ukraine-us-drone-defense-deal-kyiv-iran-war/) | Devdiscourse (Reuters), IX 2026 — [link](https://www.devdiscourse.com/article/international/3980244-ukraines-zelenskiy-says-new-drone-deal-ready-to-be-signed-as-he-lands-in-us) | medium | N |

## 3. Evidence notes (facts with date and publisher)

- **Q-0006 Brent 06.10.** Front month on 06.10.2026 was the December contract (November expired 30.09). Close 06.10: 100.58 USD/bbl (Investing.com table). Bloomberg via Rigzone (07.10.2026): December Brent "fell 0.4% to settle at $100.20" on 07.10, which puts the 06.10 settlement at about 100.6. The ICE settlement report was not reached. Threshold 100.00.
- **Q-0013 CPI IX.** GUS flash estimate 30.09.2026: 4.0% y/y, 0.7% m/m (threshold 3.5%).
- **Q-0014 FFPI IX.** FAO 02.10.2026: 136.0 points; threshold 133.3 (deadline 09.10, first publication already out).
- **Q-0041 US strike on Iranian land 24.09–07.10.** The last land strikes were on 30.08 (Larak) and 01.09.2026 (southern Iran). 05.09 and 08.09: tankers hit (these do not count). For 24.09–07.10 no statement by CENTCOM, the Pentagon or the White House was found. Reports of 03–04.10.2026 describe military options for after the US elections. centcom.mil returned HTTP 403, so its release list was not read directly. Wikipedia's section on the renewed hostilities (read 08.10) lists no US land strike in the window.
- **Q-0042 US–Iran round.** 22.09.2026: Araghchi met Witkoff and Kushner at the UN with Qatar's PM present, before the window. 28.09: Araghchi met Qatari mediators in New York. IRNA said no US representative would attend; Reuters reported "separate talks" with each side; a US official called the indirect talks "positive and constructive" (Al Jazeera 29.09). Washington's reply reached Iran through Qatari mediators in Doha (30.09). 06.10: the Qatari MFA said it is relaying messages.
- **Q-0043 Riyadh.** 26.09.2026: coalition spokesman al-Maliki (SPA) said two drones launched toward the Riyadh region were intercepted. 07.10.2026: the coalition (via dpa) said a ballistic missile was intercepted north of Riyadh. Houthi claims of hits on King Khalid airport and Aramco (05.10) were called "misleading" by the coalition.
- **Q-0044 base location.** Trump to TVN24, 05.10.2026: a base "could happen". Deputy defence minister Sobkowiak-Czarnecka: western Poland, about 5,000 soldiers, decision not expected before December. No official announcement named a town.
- **Q-0045 Polish airspace.** A Russian Mi-8 entered Polish airspace on 23.09.2026, north of Braniewo, for 42 s (DO RSZ via Defence24). That is outside the window, which starts 24.09. DO RSZ 07.10.2026: no violation during Russian strikes on Ukraine. The entries of 05.10 (three German fighters) and 07.10 (a Turkish air force aircraft) were not from RU or BY. No incursion from RU or BY found for 24.09–07.10. DO RSZ's X feed was not read item by item.
- **Q-0046 DPRK.** JCS: ballistic missile from Wonsan, about 06:30 on 03.10.2026, flight over 700 km.
- **Q-0047 PLA aircraft.** MND daily reports read directly for 25.09–07.10: 23 sorties in the report of 01.10.2026; other days 2–14.
- **Q-0048 TTF 06.10.** Front month = November. Investing.com close 75.485 EUR/MWh. Trading Economics "previous" 75.69 (read 08.10). ADVFN (06.10) 75.74 intraday. ICE Endex not reached. Threshold 75.00.
- **Q-0050 diesel.** e-petrol 07.10.2026: 7.78 PLN/l (30.09: 9.14). The drop follows the VAT cut (23%→8%) and the excise cut under the government fuel package (PAP 07.10).
- **Q-0051 OPEC+.** The seven countries met on 04.10.2026 and left November required production unchanged (CNBC, The National, 04.10). opec.org returned HTTP 402.
- **Q-0052 EUR/PLN.** NBP table A 195/A/NBP/2026 of 07.10.2026: 4.3797 (threshold 4.3500).
- **Q-0053 Russian budget.** The government submitted the draft on the evening of 30.09.2026 (Kommersant 01.10). MinFin puts the 2027 deficit at 5,443.2 bn RUB = 2.2% of GDP. Siluanov gave the same figure on 24.09 (Vedomosti). Threshold 2.0%.
- **Q-0054 A Just Russia.** CEC resolution 53/356-9 of 25.09.2026 sets the final federal-list result at 5.34%, giving 13 list seats plus 4 single-member seats.
- **Q-0055 Latvia.** CVK provisional results with all 1,059 stations counted (05.10.2026 12:23): United List 41 seats, Latvia First 17. Final confirmation is due by 19.10. A 24-seat lead cannot change first place.
- **Q-0056 Brazil.** TSE final count of the first round, 05.10.2026: Flávio Bolsonaro 47.03%, Lula 45.16% of valid votes.
- **Q-0057 US tariffs on the PRC.** The White House presidential actions for 24.09–07.10 contain no tariff act. The USTR overcapacity report was postponed until after the summit and was still unpublished in reporting to early October. ustr.gov press releases were not opened.
- **Q-0011 / Q-0058 truce.** US: Treasury Secretary Bessent on Fox News, 23.09.2026 (Washington time): the "Busan Agreement" would be "extended until Jan. 10" (NBC, 23.09, 18:20 EDT). PRC: on 28.09.2026 the MOFCOM Department of American and Oceanian Affairs said both sides agreed to extend the Kuala Lumpur joint arrangement to 10.01.2027 (Xinhua, Ming Pao). The White House fact sheet of 25.09 does not mention the extension. CalChamber (06.10) and Crowell report that the Federal Register notices are still pending.
- **Q-0059 energy truce.** Zelensky (23.09) said Ukraine is ready for an energy truce. Peskov (23.09) said no substantive talks are under way. No joint confirmation with a start date was found by 07.10.
- **Q-0060 / Q-0061 OFAC.** Read directly on ofac.treasury.gov: actions of 24.09, 28.09, 29.09 (two), 30.09, 01.10, 02.10 and 05.10; there are none on 06–07.10.
  - Q-0060: on 29.09 EC MOJO TECHNOLOGY CO LIMITED (Hong Kong) was added [NPWMD][IFSR], linked to Kavoshcom Asia (Iran). On 01.10, 12 China and Hong Kong entries were added under IRAN-EO13902/13871 (e.g. HEPCO Shanghai, Bonasol Group).
  - Q-0061: no new RUSSIA-EO14024 or H.R. 5334 entry in these actions. The A7 NETWORK (Russia and other countries) was designated on 01.10 under TCO, which the criterion excludes.
  - The harvested diff of 06.10 (19 rows added, 144 removed) matches the 05.10 action, which consisted of IRAQ2 deletions and updates.
- **Q-0062 Red Sea.** UKMTO, 04.10.2026 about 16:50 UTC: a tanker south of Mokha reported multiple explosions close to the vessel, the nearest about 100 m away, with no damage. The Maritime Executive called it an "attempted attack"; Seatrade named the vessel as Chrystal Sky.
- **Q-0063 Hormuz.** UKMTO: a tanker was struck by an unidentified projectile in the Strait of Hormuz at 17:50 UTC on 01.10.2026 and caught fire (Ship & Bunker 02.10). Further hits were reported on 02.10, 04.10 and 05.10 (engine-room fire off Musandam; The Maritime Executive 05.10).
- **Q-0064 drone agreement.** The deal was reported "ready to be signed" during UNGA week but was not signed. No official confirmation of a signing after 23.09 was found.

## 4. Not resolved in this stage

**Deadline passed, resolution source not yet available (status ACTIVE, note added):**

| ID | Why not resolved | What decides it |
|---|---|---|
| Q-0037 | PortWatch API (read 08.10) has daily Hormuz totals only up to 04.10: 24.09–04.10 = 5, 3, 4, 1, 4, 1, 4, 0, 4, 2, 4. Days 05–07.10 are not yet published | Rerun of stage 01 after PortWatch publishes 05–07.10 |
| Q-0049 | AGSI+ API needs a key, which is not set. Secondary readings: GIE homepage 72.84% (status 07.10 06:00, probably gas day 05.10); GEF 72.83% (gas day 05.10); EnergyRiskIQ 73.1% "07.10" with the gas day unclear. The value for gas day 06.10 sits at the 73.0 threshold | AGSI+ reading for gas day 06.10 (first publication), by hand or with a key |

**Later deadline: event signals checked, still ACTIVE.**

| ID | Finding (08.10.2026) |
|---|---|
| Q-0021 | MOFCOM on 28.09 extended the Kuala Lumpur arrangement to 10.01.2027. It named neither the rare-earth suspension nor announcements 55–58/61/62. No dedicated announcement has been issued; the current suspension runs to 10.11 |
| Q-0022 | No MOFCOM announcement on the Ga/Ge/Sb suspension (runs to 27.11) |
| Q-0039 | ACP advisory of 28.09.2026: 33 daily slots from 15.10.2026. YES once that limit is in force; it may still be withdrawn |
| Q-0007, Q-0008, Q-0009 | Brent front month stayed between about 95 and 108 USD in 21.09–07.10 (Investing.com); TTF stayed below 80 EUR/MWh |
| Q-0012, Q-0015 | No tariff act under H.R. 5334 or on EU goods (presidential actions to 07.10) |
| Q-0016 | MPC on 07.10.2026 left the reference rate at 3.75% (from 00_plan.md; nbp.pl not reopened) |
| Q-0019 | EU ambassadors endorsed the 22nd package around 07.10; formal Council adoption is still pending (ministers expected 12.10) |
| Q-0018, Q-0023, Q-0024, Q-0069 | Nothing found: no PRC bank in the OFAC actions of 29.09–01.10; the last MOFCOM listing of US entities was 22.06.2026; no Blackwell licence; no new DSCA notification for TECRO |
| Q-0036, Q-0038, Q-0065, Q-0068 | Hormuz daily transits 0–5; the blockade is being enforced (130th vessel redirected, 05.10); no US land strike in Iran or strike in Yemen since 23.09 (US not taking kinetic action in Yemen "for now", Axios 04.10) |
| Q-0001, Q-0002, Q-0003, Q-0005, Q-0026, Q-0027, Q-0028, Q-0030, Q-0032, Q-0034, Q-0035, Q-0040, Q-0070–Q-0073 | No occurrence found in standard searches (no Article 4 request, Baltic cable case, signed treaty, rating downgrade, new Mojtaba Khamenei recording, or decision on US troop cuts) |
| Q-0004, Q-0010, Q-0017, Q-0020, Q-0025, Q-0029, Q-0031, Q-0033, Q-0066, Q-0067 | Event date after the state date |

## 5. VERIFY flags

- **Ambiguous or disputed (6):** Q-0006, Q-0011, Q-0042, Q-0048, Q-0058, Q-0062.
- **Random 20% of the remaining 21 resolutions (4):** `random.Random(2).sample(sorted(rest), 4)` (seed = edition number 2), drawn from Q-0013, Q-0014, Q-0041, Q-0043–Q-0047, Q-0050–Q-0057, Q-0059–Q-0061, Q-0063, Q-0064. **Drawn: Q-0014, Q-0041, Q-0053, Q-0063.**
- `tools/scores.py` lists all 10 as "awaiting user verification" and leaves them out of the scores until the user approves them.

---

## FOR USER VERIFICATION

The user chose to continue the edition without pausing. Approve these after the edition. To approve, append a row with `version` 2, `user_approved = Y` and the same or a corrected outcome.

| ID | Proposed | Why flagged | What would change the outcome |
|---|---|---|---|
| Q-0006 | YES (06.10) | Near the threshold, no ICE source: Investing.com close 100.58; Bloomberg's 07.10 settlement 100.20 at −0.4% implies about 100.6 on 06.10 | An ICE settlement for LCOZ6 on 06.10 of 100.00 or less → NO |
| Q-0011 | YES (28.09) | Disputed timing. The PRC confirmed on 28.09. The US announcement (Bessent, Fox News) was on 23.09 US time, and the criterion says "after 23.09.2026". **Reading 1:** the announcement by both governments was completed on 28.09 → YES. **Reading 2:** the US statement predates the window → still ACTIVE until a US official announcement after 23.09 (e.g. the Federal Register notice) or 10.11 | If reading 2: the user decides how to record it (the registry is append-only — e.g. a version 2 row and status back to ACTIVE in questions.csv; VOID would not fit, since the criterion is clear) |
| Q-0058 | YES (28.09) | Same issue as Q-0011, short deadline. **Reading 1:** YES on 28.09. **Reading 2:** NO, because no US official announcement was found between 24.09 and 07.10 | Reading 2 → NO |
| Q-0042 | NO | Disputed format. On 28.09 in New York, Araghchi met Qatari mediators, and the mediators held separate talks with the US side; a US official called them "indirect talks". **Reading 1:** no meeting of both delegations in one place → NO. **Reading 2:** a mediated round with a shuttling mediator → YES (28.09) | Evidence that a US delegation was in New York and the Qatari mediator shuttled between the delegations on 28–29.09 → YES |
| Q-0048 | YES (06.10) | Near the threshold, no ICE Endex source: Investing.com 75.485, Trading Economics prior close 75.69 | An ICE Endex settlement for November TTF on 06.10 of 75.00 or less → NO |
| Q-0062 | YES (04.10) | UKMTO: multiple explosions near a tanker south of Mokha, no hit. **Reading 1:** an attempted hit → YES. **Reading 2:** not a confirmed attack → NO | UKMTO notice wording (attack vs incident) |
| Q-0014 | YES (02.10) | Random sample | — |
| Q-0041 | NO | Random sample; centcom.mil not readable (HTTP 403) | A CENTCOM release on a land strike in 24.09–07.10 → YES |
| Q-0053 | YES (30.09) | Random sample; MinFin and sozd not opened directly (press citing the explanatory note) | — |
| Q-0063 | YES (01.10) | Random sample; ukmto.org returned HTTP 403, so the notice was read via press | — |

Also to decide: **Q-0037** and **Q-0049** (deadline passed, data not available). Rerun stage 01 when PortWatch publishes 05–07.10, or check AGSI+ for gas day 06.10 by hand.

---

## 6. Gaps and incidents

- **Sites not readable:** ukmto.org, centcom.mil (HTTP 403); opec.org (HTTP 402); stat.gov.pl (404 on the guessed URL; the GUS publications portal was used); ICE and ICE Endex settlement pages (not reached); AGSI+ API (key required).
- **Prediction-market link in search results:** a search for the Brent settlement on 06.10 returned a robinhood.com "prediction market" page about the Brent price. It was not opened and nothing from it was used or recorded. Robinhood prediction-market pages should be added to the blocked domains of stages 03–05, as were poliwave.com and the others noted in stage 00.
- **Instructions in content:** none found in pages or search results.
- **Russian state media (no_republish):** no tass, ria or rg URL used as evidence. TASS and RIA appear only as harvested headlines consulted for leads.
- **Scores:** `01_scores.md` was generated by `tools/scores.py` and not edited. It covers the 17 resolutions without VERIFY; the 10 flagged ones are listed separately. No bug found in the script during this stage.
