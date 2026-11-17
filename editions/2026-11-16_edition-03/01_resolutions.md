# Edition 03 — resolutions (stage 01)

Stage 01 run on 16.11.2026 23:10 – 17.11.2026 01:31 (interrupted, resumed 17.11.2026 01:30) for the state date 16.11.2026, in AUTO mode (autopilot). Input: `00_plan.md` §3, `registry/questions.csv`, methodology §3.7, §7–§8. Model: claude-opus-5-5. This file contains no probabilities.

## 1. Summary

| Item | Count |
|---|---|
| Questions on the stage 00 list with deadline ≤ 16.11.2026 | 32 |
| Resolved in this stage (rows appended to `registry/resolutions.csv`, version 1) | 40 (all 32 with a passed deadline + 8 later-deadline questions whose event has occurred or whose outcome is fixed: Q-0009, Q-0026, Q-0031, Q-0065, Q-0095, Q-0098, Q-0099, Q-0101) |
| Outcome YES / NO | 18 / 22 |
| VOID | 0 |
| Flagged VERIFY | 13 new (6 ambiguous + 7 drawn at random) + Q-0042 (edition 02, still pending) |
| Deadline passed but not resolved | 0 |
| Later deadline, event not (yet) occurred — stays ACTIVE | 48 (see §4) |

`registry/questions.csv`: `status` changed to RESOLVED for the 40 questions, `notes` extended for them and for Q-0042. No other field changed (checked with a word diff against HEAD). Registry after the stage: 115 questions, 48 ACTIVE, 67 RESOLVED.

## 2. Resolutions

Outcome: 1 = YES, 0 = NO. Date = day the event occurred (YES) or deadline (NO), except where the criterion fixes another date (Q-0031) or the NO outcome became certain earlier (Q-0095, flagged). Conf. = resolution confidence.

| ID | Outcome | Date | Evidence (publisher, date) | Second source | Conf. | VERIFY |
|---|---|---|---|---|---|---|
| Q-0004 | 0 | 31.10.2026 | Russia Matters (DeepState data), 28.10 — [link](https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-oct-28-2026) | Fakty (Zelensky, ISW), 06.11 — [link](https://fakty.com.ua/ua/ukraine/20261106-skilky-terytoriyi-okupuvala-rosiya-u-zhovtni-2026-roku-shho-vidbuvalosya-na-fronti/) | medium | N |
| Q-0009 | 1 | 22.10.2026 | Investing.com, TTF historical data, read 16.11 — [link](https://www.investing.com/commodities/dutch-ttf-gas-c1-futures-historical-data) | Energy Planets — [link](https://www.energyplanets.org/european-natural-gas-prices-surge-to-highest/) | high | N |
| Q-0020 | 0 | 23.10.2026 | Bank of Russia, 23.10 — [link](https://cbr.ru/eng/press/event/?id=32930) | The Moscow Times, 23.10 — [link](https://www.themoscowtimes.com/2026/10/23/russian-central-bank-holds-key-interest-rate-steady-a94062) | high | N |
| Q-0021 | 1 | 09.11.2026 | SMM (MOFCOM/GAC Announcement No. 58 of 2026), 09.11 — [link](https://news.metal.com/newscontent/CNTOCBN4QTSC2L3BEOVBYILPAZVOOIHVV6INVPY-china-extends-suspension-of-rare-earth-export-controls-until-january-2027) | Benchmark Minerals — [link](https://source.benchmarkminerals.com/article/china-extends-pause-on-rare-earth-and-battery-export-controls-until-2027) | high | N |
| Q-0025 | 1 | 20.10.2026 | SCMP (GAC data) — [link](https://www.scmp.com/economy/global-economy/article/3371522/chinas-rare-earth-magnet-exports-eu-and-us-rebound-september) | SMM, 20.10 — [link](https://news.metal.com/newscontent/104168847-chinas-rare-earth-magnet-exports-hit-record-in-september-driven-by-backlog-release-and-regulatory-easingsmm-analysis) | medium | Y (ambiguous) |
| Q-0026 | 1 | 10.11.2026 | Kyiv Independent, 10.11 — [link](https://kyivindependent.com/ukraine-russia-us-resume-trilateral-peace-talks-in-abu-dhabi-after-9-month-pause/) | ABC News — [link](https://abcnews.com/International/russia-ukraine-us-meet-abu-dhabi-talks-trump/story?id=137970621) | high | N |
| Q-0031 | 0 | 04.11.2026 | PBS NewsHour (AP call) — [link](https://www.pbs.org/newshour/politics/democrats-win-control-of-the-u-s-house) | NPR — [link](https://www.npr.org/2026/11/03/g-s1-149526/2026-midterms-congress-balance-of-power) | high | N |
| Q-0033 | 1 | 25.10.2026 | NPR, 25.10 — [link](https://www.npr.org/2026/10/25/nx-s1-6016299/brazil-lula-bolsonaro-election) | Al Jazeera live blog, 25.10 — [link](https://www.aljazeera.com/amp/news/liveblog/2026/10/25/brazil-election-results-2026-live-polls-close-in-lula-bolsonaro-face-off) | high | N |
| Q-0037 | 0 | 07.10.2026 | IMF PortWatch API (Hormuz), read 16.11 — [link](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?where=portid%3D%27chokepoint6%27&outFields=date,portname,n_total&orderByFields=date+DESC&resultRecordCount=70&f=json) | portwatch.imf.org — [link](https://portwatch.imf.org/) | high | N |
| Q-0039 | 1 | 15.10.2026 | ACP advisory A-36-2026, 28.09 — [link](https://pancanal.com/en/panama-canal-announces-increase-in-draft-and-daily-transit/) | ad-hoc-news, 24.10 — [link](https://www.ad-hoc-news.de/unterhaltung/reisen/panama-canal-raised-daily-transit-capacity-on-15-october/70405358) | medium | Y (random) |
| Q-0049 | 0 | 06.10.2026 | GIE AGSI+ (not readable); value via TASS citing GIE (no_republish, link withheld) — [link](https://agsi.gie.eu/) | MKNews Hub (07.10 value) — [link](https://mknewshub.mk/article/1039/european-gas-near-a-four-year-high-while-storage-is-73-full-is-europe) | low | Y (ambiguous) |
| Q-0065 | 1 | 06.11.2026 | Al Jazeera, 07.11 — [link](https://www.aljazeera.com/news/2026/11/7/trump-confirms-new-us-strikes-on-irans-qeshm-island) | Voice of Emirates, 07.11 — [link](https://www.voiceofemirates.com/en/politics/2026/11/07/explosion-on-qeshm-island-trump-reveals-destruction-of-iranian-defenses-centcom-comments/) | medium | Y (ambiguous) |
| Q-0066 | 0 | 28.10.2026 | Federal Reserve, FOMC statement 28.10 — [link](https://www.federalreserve.gov/monetarypolicy/files/monetary20261028a1.pdf) | Advisor Perspectives, 28.10 — [link](https://www.advisorperspectives.com/dshort/updates/2026/10/28/feds-interest-rate-decision-october-28-2026) | high | N |
| Q-0067 | 0 | 01.11.2026 | ENGIE EnergyScan (AGSI+ data) — [link](https://energyscan.engie.com/trackers/europe-gas-storage-levels-weekly-fullness-rate-tracker-and-analysis/) | oenergetice.cz — [link](https://oenergetice.cz/en/natural-gas/eu-gas-storage-is-less-than-three-quarters-full-how-much-will-be-left-after-winter) | high | N |
| Q-0074 | 1 | 20.10.2026 | CNBC, 20.10 — [link](https://www.cnbc.com/2026/10/20/oil-price-wti-brent-crude.html) | SPA — [link](https://www.spa.gov.sa/en/N2706425) | high | N |
| Q-0075 | 0 | 31.10.2026 | Stockwatch (GUS flash 30.10) — [link](https://www.stockwatch.pl/wiadomosci/inflacja-pazdziernik-2026-szybki-szacunek-gus-paliwa-cpn-stopy-rpp,gospodarka,384226) | S.O.S. dla gospodarki — [link](https://gospodarka.sos.pl/gus-inflacja-wyniosla-3-5-r-r-w-pazdzierniku-konsensus-3-7-r-r-43503400) | high | N |
| Q-0076 | 0 | 09.11.2026 | World-Grain (FAO release 06.11) — [link](https://www.world-grain.com/articles/23426-fao-food-price-index-falls-in-october) | FAO FFPI page — [link](https://www.fao.org/worldfoodsituation/foodpricesindex/en/) | high | N |
| Q-0078 | 0 | 17.10.2026 | IMF PortWatch API (Hormuz), read 16.11 — [link](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?where=portid%3D%27chokepoint6%27&outFields=date,portname,n_total&orderByFields=date+DESC&resultRecordCount=70&f=json) | portwatch.imf.org — [link](https://portwatch.imf.org/) | high | N |
| Q-0079 | 1 | 13.10.2026 | IMF PortWatch API (Bab el-Mandeb), read 16.11 — [link](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query?where=portid%3D%27chokepoint4%27&outFields=date,portname,n_total&orderByFields=date+DESC&resultRecordCount=45&f=json) | portwatch.imf.org — [link](https://portwatch.imf.org/) | high | Y (random) |
| Q-0080 | 1 | 08.10.2026 | Arab News (GACA), 09.10 — [link](https://www.arabnews.com/saudi-arabia/saudia-pilot-killed-in-attack-on-riyadh-airport-3005428) | Al Arabiya, 09.10 — [link](https://english.alarabiya.net/News/saudi-arabia/2026/10/09/saudia-pilot-killed-in-attack-on-riyadh-airport-statement) | high | N |
| Q-0081 | 0 | 21.10.2026 | Al Jazeera, 31.10 — [link](https://www.aljazeera.com/news/2026/10/31/iran-fm-says-us-outreach-a-positive-step-as-delegation-in-qatar-for-talks) | Wikipedia (negotiations compilation) — [link](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations) | medium | N |
| Q-0082 | 0 | 31.10.2026 | Kyiv Independent, 10.11 — [link](https://kyivindependent.com/ukraine-russia-us-resume-trilateral-peace-talks-in-abu-dhabi-after-9-month-pause/) | ABC News — [link](https://abcnews.com/International/russia-ukraine-us-meet-abu-dhabi-talks-trump/story?id=137970621) | high | N |
| Q-0083 | 1 | 12.10.2026 | EEAS, 12.10 — [link](https://www.eeas.europa.eu/eeas/eu-adopts-its-largest-ever-package-sanctions-listings-targeting-industry-behind-russias-war_en) | US News (Reuters), 12.10 — [link](https://www.usnews.com/news/world/articles/2026-10-12/eu-adopts-nearly-1-600-new-sanctions-listings-targeting-russia) | high | Y (random) |
| Q-0084 | 1 | 20.10.2026 | Investing.com, TTF historical data — [link](https://www.investing.com/commodities/dutch-ttf-gas-c1-futures-historical-data) | Yahoo Finance TTF=F — [link](https://finance.yahoo.com/quote/TTF=F/history/) | medium | Y (random) |
| Q-0085 | 0 | 21.10.2026 | e-petrol.pl, 23.10 (data 21.10) — [link](https://www.e-petrol.pl/notowania-komentarz-rynek-paliw/124933/epetrolpl-tansze-tankowanie-pod-koniec-pazdziernika) | motoguru.pl — [link](https://motoguru.pl/na-czasie/srednie-ceny-paliw-21-pazdziernika-i-limity-cpn-na-22-pazdziernika/) | high | N |
| Q-0086 | 0 | 21.10.2026 | NBP API, table 205/A/NBP/2026 — [link](https://api.nbp.pl/api/exchangerates/rates/a/eur/2026-10-19/2026-10-23/?format=json) | nbp.pl table A — [link](https://nbp.pl/en/statistic-and-financial-reporting/rates/table-a/) | high | N |
| Q-0087 | 0 | 21.10.2026 | Taiwan Security Monitor (MND reports) — [link](https://taiwansecuritymonitor.substack.com/p/strait-snapshot-october-2026-update) | Peter's World tracker — [link](https://petersworld.org/pla-activity-tracker/) | medium | Y (ambiguous) |
| Q-0088 | 0 | 23.10.2026 | Bank of Russia, 23.10 — [link](https://cbr.ru/eng/press/event/?id=32930) | The Moscow Times, 23.10 — [link](https://www.themoscowtimes.com/2026/10/23/russian-central-bank-holds-key-interest-rate-steady-a94062) | high | Y (random) |
| Q-0089 | 0 | 21.10.2026 | SMM, 09.11 — [link](https://news.metal.com/newscontent/CNTOCBN4QTSC2L3BEOVBYILPAZVOOIHVV6INVPY-china-extends-suspension-of-rare-earth-export-controls-until-january-2027) | Benchmark Minerals — [link](https://source.benchmarkminerals.com/article/china-extends-pause-on-rare-earth-and-battery-export-controls-until-2027) | high | N |
| Q-0090 | 0 | 21.10.2026 | White House, EO of 16.10 — [link](https://www.whitehouse.gov/presidential-actions/2026/10/implementing-the-lindsey-o-graham-sanctioning-russia-and-iran-act-of-2026/) | CNN, 16.10 — [link](https://www.cnn.com/2026/10/16/europe/us-ukraine-russia-sanctions-intl-hnk) | high | N |
| Q-0091 | 0 | 21.10.2026 | OFAC Recent Actions, read 16.11 — [link](https://ofac.treasury.gov/recent-actions?page=1) | OFAC action 21.10 — [link](https://ofac.treasury.gov/recent-actions/20261021) | high | N |
| Q-0092 | 0 | 21.10.2026 | JMIC Update 108, 25.10 — [link](https://www.ukmto.org/-/media/ukmto/products/update-108-jmic-advisory-note-25-oct.pdf?rev=32a38b2b56f448f78f85fc33a48a1722) | JMIC Update 110, 01.11 — [link](https://www.ukmto.org/-/media/ukmto/products/jmic_advisory_update_110_01-nov-1.pdf?rev=d2be223caff04f09bbf58d94c9aa8e0a) | medium | N |
| Q-0093 | 0 | 31.10.2026 | BTA (CIK final results) — [link](https://www.bta.bg/en/news/bulgaria/1232658-final-results-iotova-valchev-win-first-round-of-presidential-election-with-34-7) | Radio Bulgaria — [link](https://bnrnews.bg/en/post/547988/bulgarian-presidential-election-results-with-9994percent-of-votes-counted) | high | N |
| Q-0094 | 1 | 30.10.2026 | Times of Israel (final count) — [link](https://www.timesofisrael.com/with-all-votes-counted-netanyahus-bloc-at-53-seats-eisenkots-48-arab-parties-19/) | israel.com — [link](https://www.israel.com/news/likud-tops-final-israeli-election-count-with-27-seats-as-shas-falls-to-6) | high | Y (random) |
| Q-0095 | 0 | 04.11.2026 | Spectrum News (AP) — [link](https://spectrumlocalnews.com/us/snplus/politics/2026/11/03/balance-of-power-congress-2026-midterm-elections) | NBC News, 15.11 — [link](https://nbcnews.com/news/us-news/weekend-rundown-november-15-rcna609191) | high | Y (ambiguous) |
| Q-0098 | 1 | 28.10.2026 | Novinite (Chief of Defence Eftimov) — [link](https://www.novinite.com/view_news.php?id=241330) | AP via News10 — [link](https://www.news10.com/news/international/ap-ship-sinks-off-bulgarias-black-sea-coast-after-being-hit-by-drones/amp/) | high | N |
| Q-0099 | 1 | 16.11.2026 | USNI News Fleet and Marine Tracker, 16.11 — [link](https://news.usni.org/2026/11/16/usni-news-fleet-and-marine-tracker-nov-16-2026) | USNI News, 16.11 — [link](https://news.usni.org/2026/11/16/uss-theodore-roosevelt-now-in-the-middle-east-lincolns-last-escorts-finally-home) | medium | N |
| Q-0101 | 1 | 13.10.2026 | Council of the EU, Ukraine policy page — [link](https://www.consilium.europa.eu/en/policies/ukraine/) | Ukrainska Pravda, 13.10 — [link](https://www.pravda.com.ua/eng/news/2026/10/13/8057865/) | high | N |
| Q-0102 | 1 | 09.11.2026 | Federal Register 2026-22793, 09.11 — [link](https://www.federalregister.gov/documents/2026/11/09/2026-22793/extension-of-the-suspension-of-expansion-of-end-user-controls-for-affiliates-of-certain-listed) | Skadden — [link](https://www.skadden.com/insights/publications/2026/11/bis-extends-suspension-of-affiliates-rule) | high | Y (random) |
| Q-0105 | 1 | 06.11.2026 | Notes from Poland, 07.11 — [link](https://notesfrompoland.com/2026/11/07/rating-agency-sp-shifts-polands-credit-outlook-to-negative-and-lowers-currency-rating/) | TVP World — [link](https://tvpworld.com/96358515/-sp-cuts-polands-credit-outlook-to-negative-over-debt) | medium | Y (ambiguous) |

## 3. Evidence notes (facts with date and publisher)

- **Q-0004 DeepState X.** DeepState data, four weeks to 26.10.2026: Russian net gain about 18 sq mi (about 47 km²) (Russia Matters 28.10). Zelensky (Telegram, 01.11): Russia occupied 85.8 km² in October, Ukraine liberated 96.2 km². ISW: net −27.29 km² for Russia. No DeepState calendar-month summary for October found (searched in Ukrainian and English, 16.11). Threshold 200 km².
- **Q-0009 TTF > 90 by 31.12.** Investing.com front-month closes: 20.10 85.062, 21.10 87.426, 22.10 90.043, 23.10 93.853, 28.10 100.720, 30.10 103.944 EUR/MWh. Reports of 22.10 say the contract ended trading above 90 for the first time since 12.2022. ICE Endex not reached. If the ICE settlement of 22.10 was at or below 90.00, the date moves to 23.10; the outcome stays YES.
- **Q-0020 / Q-0088 Bank of Russia.** 23.10.2026: key rate kept at 14.00%; 2026 inflation forecast raised to 7.1–7.6% (cbr.ru statement; Moscow Times). Harvested cbr.ru table: 14.00% on 27–28.10. Next meeting 18.12.
- **Q-0021 / Q-0089 rare earths.** MOFCOM and GAC Announcement No. 58 of 2026, 09.11.2026: suspension of six October-2025 export-control announcements (rare earths, equipment, the 0.1% rule, batteries, superhard materials) continues 11.11.2026–10.01.2027 (SMM, Benchmark, Rare Earth Exchanges, TechTimes 10.11). The announcement falls inside Q-0021 (by 10.11) and outside Q-0089 (08–21.10). No earlier announcement in 08–21.10 found. mofcom.gov.cn not opened.
- **Q-0025 magnets IX.** SCMP (GAC data): exports of rare-earth permanent magnets to the USA in IX 2026 604 t, +18% m/m, against 512 t in VIII. SMM 20.10.2026: total magnet exports in IX 6,165.12 t (record), driven by release of orders held at ports in VII–VIII. US figure from a single secondary source; GAC site not opened.
- **Q-0026 / Q-0082 trilateral.** Abu Dhabi, 10–11.11.2026: Russia's delegation named by Kremlin spokesman Peskov (Medinsky, Ushakov, Kostyukov, Ryabkov); Ukraine's led by Umerov; US by Witkoff and Kushner. Described as the first trilateral round since February (Kyiv Independent, ABC, Ukrinform). Agreement in principle on a large prisoner exchange; no breakthrough on territory reported. No trilateral meeting in 08–31.10.
- **Q-0031 / Q-0095 US Congress.** AP called the House for the Democrats at 01:33 ET on 04.11.2026 and the Senate overnight 03–04.11 (PBS, NPR, Spectrum/AP). AP count of 09.11: House D 254, R 162, 19 uncalled; Senate D 54 (with independents), R 44, Alaska and Mississippi uncalled. NBC 15.11: Mississippi projected for Colom (D); Alaska uncalled, Peltola (D) ahead 49.9–46.0. Republicans cannot reach 218 House seats or 50 Senate seats.
- **Q-0033 Brazil.** TSE confirmed Lula's runoff win on 25.10.2026 at 21:08 BRT (97% counted); final 51.79% vs 48.21%. Flávio Bolsonaro said he would seek annulment (Rio Times; no filing confirmed).
- **Q-0037 / Q-0078 Hormuz; Q-0079 Bab el-Mandeb (PortWatch read directly 16.11).**
  - Hormuz n_total 24.09–07.10: 5, 3, 4, 1, 4, 1, 4, 0, 4, 2, 4, 8, 2, 6 (max 8, threshold 20).
  - Hormuz n_total 08–17.10: 4, 3, 4, 2, 3, 7, 3, 2, 7, 0 (max 7, threshold 10).
  - Bab el-Mandeb n_total 08–17.10: 25, 24, 22, 31, 34, **17 (13.10)**, 24, 24, 25, 29 (threshold: below 20).
  - Harvested values for the days the harvester caught (10, 11, 16, 17.10) are identical.
- **Q-0039 Panama.** ACP advisory A-36-2026 (28.09.2026): Neopanamax 10 daily transits, 33 slots in total from 15.10.2026. A report of 24.10 confirms 33 slots from 15.10. A later rise to 34 slots is reported by DataPortuaria (date not confirmed). No withdrawal found.
- **Q-0049 EU storage 06.10.** TASS, citing GIE data: 72.97% on 06.10.2026 (Russian state media, no_republish: paraphrased, not linked). GIE homepage 72.84% for gas day 05.10 (edition 02); 73.1% on 07.10 (MKNews Hub citing AGSI+; Rio Times). AGSI+ API needs a key (HTTP "access denied"). Threshold 73.0.
- **Q-0065 US strike on Iranian land.** President Trump to reporters in West Palm Beach, 06.11.2026: US forces "knocked out" a newly built Iranian anti-aircraft system on Qeshm island in "about 15 minutes" ("minor strikes"). Iranian state media: two missile strikes in the Suza area of Qeshm; IRIB claimed an MQ-9 shot down (unverified). CENTCOM: situation "relatively calm", no further comment. No CENTCOM or Pentagon release found.
- **Q-0066 FOMC.** 28.10.2026: target range kept at 3.75–4.00%, vote 10–2 (Cook and Hammack dissented for a hike). Harvested FRED DFEDTARU 4.00 throughout 07.10–16.11.
- **Q-0067 EU storage 01.11.** ENGIE EnergyScan: 844.3 TWh = 74.6% on gas day 01.11.2026; oenergetice.cz 74.56%. Threshold 80.0.
- **Q-0074 Brent 20.10.** December contract settled at 108.79 USD/bbl on 20.10.2026, −0.76 (CNBC; SPA; Yahoo BZ=F). Session high 111.99.
- **Q-0075 CPI X.** GUS flash estimate 30.10.2026: 3.5% y/y, −0.4% m/m (fuels −9.7% m/m); PAP consensus 3.7%. The criterion requires less than 3.5%.
- **Q-0076 FFPI X.** FAO release 06.11.2026: 133.9 points, −1.2% m/m (World-Grain, Potato Pro). Threshold 136.0.
- **Q-0080 Saudi deaths.** GACA: two attacks on King Khalid International Airport on 08.10.2026 killed three Saudi nationals, including Saudia captain Hamoud Ali al-Kalthami (Arab News, Al Arabiya 09.10). 10.10: 12 killed, over 300 wounded at the same airport (Saudi civil aviation authorities via Arab News, AP). 11.10: 1 killed (GACA via Al Jazeera). 21.10: Dammam airport hit, 2 killed (Wikipedia compilation). The coalition attributes the attacks to the Houthis.
- **Q-0081 US–Iran meeting.** No in-person meeting of both governments' representatives in one room found for 08–21.10.2026. Al Jazeera 31.10: an Iranian delegation was in Doha; Araghchi said Iran saw no need to meet Americans at this stage. state.gov and mfa.ir not opened.
- **Q-0083 EU listings.** Council, 12.10.2026: 1,569 persons and entities (826 companies, 743 individuals) listed under the regime on Ukraine's territorial integrity; also 77 individuals over the Duma elections in occupied Ukraine (same regime) and 3 individuals and 4 entities under the DPRK regime (EEAS). No new sectoral measures (McDermott).
- **Q-0084 TTF 20.10.** Investing.com close 85.062 EUR/MWh (Yahoo TTF=F the same); intraday high about 90.2. Threshold 80.00.
- **Q-0085 diesel.** e-petrol: national average diesel 7.94 PLN/l on 21.10.2026 (−0.04). CPN maximum price 7.98. Threshold 7.70.
- **Q-0086 EUR/PLN.** NBP table 205/A/NBP/2026 of 21.10.2026: 4.3641 (20.10: 4.3716; 22.10: 4.3685). Threshold 4.4000.
- **Q-0087 PLA aircraft.** Highest count in the reports of 08–21.10.2026: 29 aircraft (TSM dates it 20.10; the second tracker dates the report 21.10). October total 232 sorties; first day with 30 or more: 31.10 (32). mnd.gov.tw timed out (60 s).
- **Q-0090 H.R. 5334 duty.** Executive order of 16.10.2026, "Implementing the Lindsey O. Graham Sanctioning Russia and Iran Act of 2026": certification to Congress under section 115(b) and waiver of the Act's duties; no 500% or 100% tariffs imposed (whitehouse.gov; ABC; CNN; The Hill).
- **Q-0091 OFAC.** Recent Actions read directly for 08–21.10.2026 (08.10; 09.10 two actions; 13.10 two; 14.10; 15.10; 16.10; 19.10; 21.10). Additions carry only IRAN-EO13846, IRAN-EO13902, CUBA-EO14404, ILLICIT-DRUGS-EO14059, SDGT, ICC and PAIPA tags. Russia-related items are general licences only (13S on 08.10; GL of 09.10; 128D, 130B on 15.10; 131K on 21.10).
- **Q-0092 Red Sea hits.** JMIC Update 106 (18.10) and 108 (25.10): no confirmed attack in the Red Sea, Bab el-Mandeb or Gulf of Aden; the only incident in the 25.10 update was an LPG tanker attacked on 22.10 northeast of Limah (Gulf of Oman area). JMIC Update 110 (01.11): no confirmed attack on shipping; the last confirmed Houthi attack on a merchant vessel was on 24.08.2026. PDFs returned HTTP 403; read through search excerpts.
- **Q-0093 Bulgaria.** CIK final first-round result (25.10.2026): Iotova–Valchev 34.76%, Gurov–Kandev 31.95%; turnout 22.98%. Iotova won the runoff of 01.11 (57.6% per one compilation).
- **Q-0094 Israel.** Knesset election 27.10.2026, final count: Likud 27 seats (20.51%), Yashar 21, Together 12, Joint List 11, Democrats 8, Ra'am 8. Netanyahu bloc 53, Eisenkot bloc 48, Arab-led parties 19. Formal announcement on 30.10 per one source, 04.11 per another.
- **Q-0098 Black Sea.** 28.10.2026: Contship Jet hit by three uncrewed surface drones about 16–21 nm off Cape Kaliakra / Shabla, inside Bulgaria's EEZ, per the Bulgarian Navy and Chief of Defence Adm. Eftimov (Novinite; AP); the ship sank on 29.10. Earlier: Wine Trader fire 15.10 (cause not confirmed by Romania); Khoryv sank on 23.10, 13 nm off Constanța, just outside Romanian territorial waters; Romania's president and PM condemned it as an attack, but no official statement naming a drone and the EEZ was found. Later: three ships hit near Sulina 14.11 (Romanian territorial waters), Betul 8 capsized 16.11 in Bulgaria's EEZ.
- **Q-0099 carriers.** USNI tracker 16.11.2026: George Washington (CVN-73), George H.W. Bush (CVN-77) and Theodore Roosevelt (CVN-71) all in the Arabian Sea; Roosevelt chopped into 5th Fleet on 15.11. USNI returned HTTP 403; read through search excerpts.
- **Q-0101 Ukraine clusters.** Fourth EU–Ukraine accession conference, Luxembourg, 13.10.2026: clusters 2 and 3 opened with all 27 member states in favour after Ukraine amended its minority education law (Council page; Ukrainska Pravda). Clusters 4 and 5 still closed.
- **Q-0102 BIS.** Federal Register document 2026-22793, published 09.11.2026: suspension of the Affiliates rule extended through 10.01.2027, effective on publication.
- **Q-0105 S&P Poland.** 06.11.2026: local-currency ratings lowered to A-/A-2 from A/A-1; foreign-currency ratings affirmed at A-/A-2; outlook revised from stable to negative ("outlooks for both ratings", per several reports). Deficit projected 7.1% of GDP in 2026 and 2027.
- **Q-0042 (edition 02, VERIFY pending).** Re-checked as the user's hold of 11.10.2026 requires. Searches on 16.11 found no evidence that a US delegation was in New York on 28.09.2026 or that the Qatari mediator shuttled between delegations. IRNA said no US representative would attend; Reuters said mediators were *expected* to hold separate talks with each side (not confirmed). The NO outcome of version 1 stands; no new row appended. Stage V re-checks it with the 13 new flags.

## 4. Not resolved in this stage (status ACTIVE)

**Deadline passed but not resolved:** none.

**Later deadline: event signals checked, still ACTIVE.**

| ID | Finding (16.11.2026) |
|---|---|
| Q-0029, Q-0100 | APEC leaders' meeting 18–19.11 is after the state date. White House confirmed Trump's attendance; Ushakov said Putin will meet Trump in Shenzhen (stage 00 leads) |
| Q-0030 | No Putin–Trump meeting by the state date; a meeting in Shenzhen is planned for 19.11 |
| Q-0022 | No MOFCOM extension of the Ga/Ge/Sb/superhard-materials suspension found; 09.11 announcement does not cover it per reports; expires 27.11 |
| Q-0007, Q-0008, Q-0115 | Highest Brent front-month settlement found in the window 116.72 (23.10); about 117.6 at the end of October per one report. Dated Brent and FRED spot above 120 do not count. Lowest settlement about 90; no settlement below 80 found |
| Q-0017 | ECB kept the deposit rate at 2.50% on 29.10.2026 (CNBC, euribor-rates.info); next meeting 17.12 |
| Q-0016 | MPC kept the reference rate at 3.75% on 04.11 (stage 00 lead); next decision 02.12 |
| Q-0019, Q-0104 | Listings of 12.10 (1,569) and 16.11 (113 under the Ukraine regime + 32 under the hybrid-threats regime; Council press release 16.11) contain no new import or export prohibition; 22nd package not yet proposed or adopted. The steel-slab quota step-down of 01.10 follows existing Art. 3g rules, not a new Council act |
| Q-0002 | Khoryv sailor killed 23.10 about 13 nm off Constanța, just outside Romanian territorial waters (EEZ is not "territory" under the criterion); no other death on NATO territory found |
| Q-0027, Q-0097 | No Article 4 request found. Polish airspace: DO RSZ did not confirm the 10–11.11 drone (Lithuania's report) nor the 18.10 alert |
| Q-0040 | Finnish court verdict of 05.11 concerns the December-2025 Fitburg case (announced before the creation date); no new damage announcement found |
| Q-0068 | No US strike on Houthi targets found |
| Q-0001 | No mobilisation decree found; Putin said none is planned (Russian-language reports, 15–16.11) |
| Q-0012 | Graham Act duties waived on 16.10; no tariff act on third countries |
| Q-0018 | No mainland PRC bank found in OFAC actions to 13.11 |
| Q-0023 | No new MOFCOM listing of US entities found after 22.06.2026 |
| Q-0024 | Blackwell still barred for China (TechCrunch 13.11); only H200 exports allowed |
| Q-0028, Q-0038 | No US–Iran agreement; blockade enforced (JMIC 016-26, 28.10) |
| Q-0032 | Latest Mojtaba Khamenei recording found dates from late August 2026 |
| Q-0036 | PortWatch Hormuz daily totals 0–8 through 08.11; 7-day average far below 40 |
| Q-0069 | No DSCA notification for TECRO after 23.09 found (DSCA site 403; Federal Register search only) |
| Q-0096 | Araghchi still foreign minister; impeachment motion not taken further |
| Q-0103 | Cameco month-end spot October 91.55 USD/lb (threshold 95.00) |
| Q-0106, Q-0107, Q-0108, Q-0109 | No diesel export restriction; no infringement decision on Polish fuel VAT found; no Federal Register act on the 30-for-30 lists; FY2027 NDAA not enacted |
| Q-0114 | Pentagon "green-lit" a permanent presence; White House decision expected in December; no location named |
| Q-0003, Q-0005, Q-0010, Q-0015, Q-0034, Q-0035, Q-0070–Q-0073, Q-0077, Q-0110–Q-0113 | Deadline in 2027 or event date after the state date; no occurrence found in stage 00 or this stage |

## 5. VERIFY flags

- **Ambiguous or disputed (6):** Q-0025 (single source for the US figure), Q-0049 (near threshold, no primary reading), Q-0065 (whether the President's remarks are an official statement), Q-0087 (one aircraft below the threshold, MND not read), Q-0095 (resolution date before the deadline, two races uncalled), Q-0105 (outlook scope).
- **Random 20% of the remaining 34 resolutions (7):** `random.Random(3).sample(sorted(rest), 7)` (seed = edition number 3; 0.2 × 34 = 6.8, rounded to 7), drawn from Q-0004, Q-0009, Q-0020, Q-0021, Q-0026, Q-0031, Q-0033, Q-0037, Q-0039, Q-0066, Q-0067, Q-0074–Q-0076, Q-0078–Q-0086, Q-0088–Q-0094, Q-0098, Q-0099, Q-0101, Q-0102. **Drawn: Q-0039, Q-0079, Q-0083, Q-0084, Q-0088, Q-0094, Q-0102.**
- `tools/scores.py` lists these 13 and Q-0042 as awaiting verification and leaves them out of the scores until stage V (AUTO mode) or the user approves them.

---

## FOR USER VERIFICATION

AUTO mode: these are re-checked independently by stage V (`prompts/V_autoverify.md`); a disagreement goes to `AUTOPILOT_INBOX.md`. To decide by hand, append a row with a higher `version`, `user_approved = Y` and the same or a corrected outcome.

| ID | Proposed | Why flagged | What would change the outcome |
|---|---|---|---|
| Q-0025 | YES (20.10) | US figure (604 t vs 512 t) from SCMP only; GAC not opened | GAC first publication for IX showing 512 t or less to the USA → NO |
| Q-0049 | NO (06.10) | 72.97% vs threshold 73.0, only via a TASS calculation on GIE data; AGSI+ needs a key | AGSI+ first publication for gas day 06.10 above 73.0 → YES |
| Q-0065 | YES (06.11) | **Reading 1:** the President's on-record confirmation of strikes on an air-defence site on Qeshm (Iranian island, land target) is a White House statement → YES. **Reading 2:** remarks to reporters are not an official statement; CENTCOM declined comment → still ACTIVE | A strict reading requiring a written CENTCOM/Pentagon/White House release → stays ACTIVE until such a release or 31.12 |
| Q-0087 | NO (21.10) | Maximum 29 aircraft vs threshold 30, from secondary trackers of MND data | An MND report published 08–21.10 with 30 or more → YES |
| Q-0095 | NO (04.11) | Outcome certain (Republicans at most 45–46 seats), but the date precedes the 31.12 deadline and Alaska is uncalled | Only the date could change (to 31.12); the outcome cannot |
| Q-0105 | YES (06.11) | spglobal.com not read; one report does not say explicitly that the negative outlook covers the foreign-currency rating | S&P release showing the FC outlook stable → NO |
| Q-0039 | YES (15.10) | Random sample; ACP advisory read, no later ACP confirmation that it took effect | An ACP advisory withdrawing the 33 slots before 15.10 → NO |
| Q-0079 | YES (13.10) | Random sample | — |
| Q-0083 | YES (12.10) | Random sample; Official Journal not opened | — |
| Q-0084 | YES (20.10) | Random sample; ICE Endex not reached (Investing.com fallback) | — |
| Q-0088 | NO (23.10) | Random sample | — |
| Q-0094 | YES (30.10) | Random sample; bechirot.gov.il not opened; date of formal announcement 30.10 or 04.11 | — |
| Q-0102 | YES (09.11) | Random sample | — |
| Q-0042 | NO (07.10, edition 02) | User hold of 11.10.2026; re-check found no new evidence | Evidence of a US delegation in New York on 28.09 with a shuttling Qatari mediator → YES |

---

## 6. Gaps and incidents

- **Sites not readable:** IMF PortWatch API (HTTP 429 quota on the first three tries, then read with a `portid` filter); AGSI+ API (key required); ukmto.org PDFs, news.usni.org, scmp.com, dsca.mil, intellinews.com (HTTP 403); mnd.gov.tw and an NPR page (timeout). ICE and ICE Endex settlement pages not reached. Not opened: stat.gov.pl, tse.jus.br, cik.bg, bechirot.gov.il, mofcom.gov.cn, spglobal.com, kremlin.ru, president.gov.ua, state.gov, mfa.ir.
- **Russian state media (no_republish):** the only reading for Q-0049 comes from TASS (citing GIE); it is paraphrased and its URL is withheld from the registry. No tass, ria or rg URL is used as evidence.
- **Forecasting sites:** forbidden domains of rule 3.9 were blocked in every search; none appeared. One search summary (Q-0022) mentioned a Substack author's "coin flip" guess about an extension; it is an opinion, not used.
- **Instructions in content:** none found in pages or search results.
- **Scores:** `01_scores.md` was generated by `tools/scores.py` and not edited. Observation (not a bug): the edition 02 forecasts of Q-0080 are left out because they are dated 08.10, the same day as the resolution event (08.10), in line with the framework 1.5 rule "on or after the resolution date".
