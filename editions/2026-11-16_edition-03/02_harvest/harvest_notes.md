# Harvest notes — edition 03 (window 07.10.2026–16.11.2026)

Written in stage H (mode digest), 16.11.2026, from `coverage.md`, `indicators.md`, `sources_health.md`, `manifest.json`, the harvester status and the harvester logs. No headlines or snippets are reproduced here.

## 1. Window actually covered

- **Full window, no late start.** The harvester ran in watch mode on every day of the window (event logs exist for each day 07.10–16.11.2026, 575–1,571 log lines a day; the lowest day is 09.10). Items by publication date range from about 3,200 to about 6,000 a day across the whole window (lowest 09.10: 3,160; highest 15.10: 5,983); no day is missing.
- The window is about 6 weeks long (41 days) — about three times a normal edition window, because edition 03 started 26 days later than planned (due 21.10.2026).
- Totals: 188,978 items in the window, 83,759 matched to at least one concept; 53 languages (largest: en 78,856, ru 47,314, pt 17,206, pl 9,534, ar 6,352, tr 5,611, fa 5,046, uk 4,766, fr 3,256, de 2,515); 125–126 countries of publication; Western share of items 26%.
- Sources at the state date (`python3 -m tools.harvester status`, 16.11.2026 21:58 UTC): 202 enabled — 159 ok, 31 throttled (rate-limited, waiting), 1 retrying (PortWatch, ArcGIS quota HTTP 429), 3 failing (ISW, PressTV, Saba), 8 skipped (missing API key or robots.txt). 143 sources had items in the window.
- Volume is not weight: the Russian state/loyal cell (43,108 items) and Brazil (17,189) dominate counts. Stage 02 balances perspectives per event.
- **GDELT gap.** 30 GDELT queries are throttled (host paused after rate limiting); 15 of them have produced no items at all (among them Polish-, Japanese-, Korean-, Turkish-, Spanish- and Hebrew-language queries, sanctions, tariffs, talks, chips, Sahel, Sudan/Horn), and several others have not succeeded since 05.10. Coverage of those topics rests on RSS/page sources and web search.

## 2. Flagged concepts — mandatory targeted searches in stage 02

| Group | Concept | Flag | Items | What to search |
|---|---|---|---|---|
| G2 | Fuel prices and energy policy in Poland | ⚠W>80% (99% Western; 3 languages, 6 countries) | 197 | Non-Polish and actor-side coverage (regional, Lithuanian/Czech/German or industry sources, Orlen counterparties); primary price data (e-petrol, Orlen wholesale) |

No other concept is flagged. Thin but unflagged concepts (fewer than about 350 items over 41 days): US forces in Europe and Poland 91 (G1, G4; 74% Western, 3 languages); rare earths and critical minerals 233, food and fertilisers 288, uranium and nuclear fuel 330 (G2); Arctic and Greenland 320 (G4). Poland security (G1, G4) sits at 79% Western, just under the flag. Treat these as low-volume and search actively.

## 3. Silent required cells of the source universe

| Cell (actor:role) | Group(s) concerned | Note |
|---|---|---|
| PL:official | G1, G3, G4 | Polish government source configured but silent — MON, DO RSZ, KPRM, NBP communiqués need direct checks |
| SA:official | G1, G2 | No Saudi official source — Houthi attacks on Saudi territory, OPEC+ decisions |
| TR:western | G1, G4 | No Western outlet configured for Turkey |
| IN:official | G2, G4 | Indian government source silent (oil purchases, sanctions compliance) |
| TW:official | G1 | Taiwan MND source silent — PLA activity reports must be read on mnd.gov.tw |
| JP:official | G1, G4 | No Japanese official source |
| YE:state_loyal | G1, G2 | Saba failing (HTTP 403) — Houthi A-perspective via other channels |
| GL:independent_exile | G4 | Greenland outlet configured but silent |

Near-silent: NATO official 1 item, China official 1 item, Iran official 6 items, EU independent 0 items. Official statements of these actors must be checked directly on their sites in stage 02.

## 4. Failing or missing sources that matter for registry resolution

| Source | Status | Relevance |
|---|---|---|
| GIE AGSI+ (agsi_eu, agsi_de, agsi_pl) | skipped — API key not set | EU and Polish gas-storage questions — stage 01 must read agsi.gie.eu directly |
| EIA Brent / US crude stocks | skipped — API key not set | Brent only from FRED spot (not the ICE front-month settlement named in oil-price questions) |
| TTF front-month, e-petrol diesel | no dataset configured | TTF and Polish fuel-price questions |
| IMF PortWatch | retrying (ArcGIS quota, HTTP 429); only 13 daily rows in the window (10–11.10, 16–18.10, 25.10, 29.10–01.11, 06–08.11); latest 08.11 | Hormuz and Red Sea transit questions — read missing days on portwatch.imf.org |
| ECB deposit rate | ok, but the series was last fetched on 05.10 — no harvested value after the 29.10 Governing Council | ECB questions — read ecb.europa.eu |
| ISW | failing — HTTP 403 (last success 23.10) | Front-line context |
| PressTV | failing since 10.11 — TLS certificate hostname mismatch | Iranian state perspective (other Iranian state sources work) |
| Saba (Yemen) | failing — HTTP 403 since 05.10 | Houthi A-perspective |
| Tasnim (EN, FA) | no items parsed in recent sweeps | Iranian loyal perspective |
| NASA FIRMS | skipped — API key not set | Strike and fire context |
| teleSUR (EN) | robots.txt now disallows | Venezuelan state perspective |

## 5. Primary-data values for block L (from `indicators.md` and raw snapshots)

| Indicator | Value | Date | Source |
|---|---|---|---|
| EUR/PLN (NBP table A) | 4.4048 | 16.11.2026 | api.nbp.pl |
| USD/PLN (NBP table A) | 4.0007 | 16.11.2026 | api.nbp.pl |
| EUR/USD (ECB reference) | 1.1014 | 16.11.2026 | ECB |
| USD/RUB, EUR/RUB, CNY/RUB (Bank of Russia official) | 82.1516 / 91.0322 / 12.3149 | 14.11.2026 | cbr.ru |
| Bank of Russia key rate | 14.00% | 16.11.2026 (raw snapshot of cbr.ru key-rate table) | cbr.ru |
| Fed funds target range | 3.75–4.00% | 16.11.2026 | FRED DFEDTARL/DFEDTARU |
| US 10-year Treasury yield | 5.15% | 13.11.2026 | FRED DGS10 |
| Broad US dollar index | 122.65 | 13.11.2026 | FRED DTWEXBGS |
| Brent spot (not ICE settlement) | 92.14 USD/bbl | 11.11.2026 | FRED DCOILBRENTEU |
| WTI spot | 89.62 USD/bbl | 11.11.2026 | FRED DCOILWTICO |
| Hormuz transits (all / tankers) | 3 / 1 | 08.11.2026 | IMF PortWatch |
| Bab el-Mandeb transits (all / tankers) | 24 / 6 | 08.11.2026 | IMF PortWatch |
| Suez Canal transits (all / tankers) | 43 / 17 | 08.11.2026 | IMF PortWatch |
| Bosporus transits (all / tankers) | 58 / 15 | 08.11.2026 | IMF PortWatch |
| Taiwan Strait transits (all) | 237 | 08.11.2026 | IMF PortWatch |
| Panama Canal transits (all) | 22 | 08.11.2026 | IMF PortWatch |
| OFAC SDN list change | 0 rows added, 0 removed | 15.11.2026 (vs previous snapshot) | OFAC SDN list |

Harvested Hormuz daily totals in the window, where available: 10.10: 4; 11.10: 2; 16.10: 7; 17.10: 0; 18.10: 4; 25.10: 2; 29.10: 3; 30.10: 7; 31.10: 8; 01.11: 1; 06.11: 6; 07.11: 2; 08.11: 3.

Not available from the harvest: TTF, EU and Polish gas storage, Polish fuel prices, NBP reference rate, ECB decisions after 05.10, ISW front assessments. These remain web-search items for stages 01 and 02.
