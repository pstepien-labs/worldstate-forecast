# Harvest notes — edition 02 (window 23.09.2026–07.10.2026)

Written in stage H (mode digest), 08.10.2026, from `coverage.md`, `indicators.md`, `sources_health.md` and `manifest.json`. No headlines or snippets are reproduced here.

## 1. Window actually covered

- **Late start (gap).** The harvester first ran on 05.10.2026 at 10:52 UTC (source check after the stage H repair) and has run continuously in watch mode since then. Live feed collection therefore covers only about 2.5 of the 14 days of the window (05.10–07.10). Feeds that keep a backlog and GDELT article lists (back-fill up to 14 days) supply the earlier days; primary datasets were fetched with their history.
- **Distribution of items by publication date:** 23.09–01.10: 1,531 items (about 8%); 02.10–04.10: 4,258 (about 22%); 05.10–07.10: 13,288 (about 70%). The first nine days of the window are thinly covered — stage 02 must treat the digest as a lead source mainly for 02–07.10 and rely on web search for 23.09–01.10.
- Totals: 19,077 items in the window, 8,336 matched to at least one concept; 47 languages (largest: en 8,461, ru 4,129, pt 1,615, pl 834, zh 582, uk 514, fa 444, tr 439, ar 437); 102–103 countries of publication; Western share of items 30%.
- Sources at the state date (`python3 -m tools.harvester status`, 07.10.2026 22:25 UTC): 202 enabled — 157 ok, 31 throttled (rate-limited, waiting; normal), 3 retrying, 2 failing, 9 skipped (missing API key or robots.txt). 154 sources had items in the window.
- The Russian state/loyal cell dominates volume (3,227 items); Brazil is large (1,356) because of the 04.10 elections. Volume is not weight: stage 02 balances perspectives per event.

## 2. Flagged concepts — mandatory targeted searches in stage 02

| Group | Concept | Flag | Items | What to search |
|---|---|---|---|---|
| G1 and G4 | Poland: security, defence, politics | ⚠<3 lang (pl, en only) | 113 | Actor-side (RU, BY) and third-party (Baltic, German, Ukrainian) coverage of events in and around Poland |
| G2 | Fuel prices and energy policy in Poland | ⚠W>80%, ⚠<3 lang (1 country) | 36 | Non-Polish coverage (e.g. regional or industry sources, Orlen counterparties); primary price data (e-petrol, Orlen wholesale) |
| G4 | Arctic and Greenland | ⚠<3 lang | 22 | Danish/Greenlandic (da, kl) and Russian coverage |

G3 has no flagged concept. Thin but unflagged concepts (fewer than 40 items): US forces in Europe and Poland 18 (G1); rare earths and critical minerals 19, uranium 25, semiconductors 34, food and fertilisers 36 (G2); China domestic 28 (G4). Treat these as low-volume and search actively.

## 3. Silent required cells of the source universe

| Cell (actor:role) | Group(s) concerned | Note |
|---|---|---|
| NATO:official | G1, G4 | nato.int not producing items — Article 4, flank incidents and summit statements need direct checks |
| SA:official | G1, G2 | No Saudi official source (SPA) — Houthi attacks on Saudi territory, OPEC+ decisions |
| TR:western | G1, G4 | No Western outlet configured for Turkey (Bosporus, Black Sea) |
| JP:official | G1, G4 | No Japanese official source (DPRK launches via mod.go.jp) |
| GL:independent_exile | G4 | Greenland outlet configured but silent |

Also near-silent: China official 2 items (MOFCOM intermittent connection resets), Iran official 2 items, Poland official 1 item, EU independent 0 items. Official statements of these actors must be checked directly on their sites in stage 02.

## 4. Failing or missing sources that matter for registry resolution

| Source | Status | Questions affected |
|---|---|---|
| GIE AGSI+ (agsi_eu, agsi_de, agsi_pl) | skipped — API key not set | Q-0010, Q-0049, Q-0067 (EU storage) — stage 01 must read agsi.gie.eu directly |
| EIA Brent / US crude stocks | skipped — API key not set | Brent comes only from FRED (DCOILBRENTEU, a spot series with about a one-week lag; latest value 29.09). It is not the ICE front-month settlement named in Q-0006, Q-0007, Q-0008 |
| TTF front-month | no dataset configured | Q-0009, Q-0048 |
| e-petrol weekly diesel | no dataset configured | Q-0050 |
| IMF PortWatch | ok, but no daily rows for 28.09–02.10 in the harvested series | Q-0036, Q-0037 — confirm the missing days on portwatch.imf.org |
| OFAC SDN list | ok, but diffs exist only from the first snapshot (05.10) | Q-0060, Q-0061, Q-0018 — additions 24.09–05.10 must be read from ofac.treasury.gov/recent-actions |
| ISW (understandingwar.org) | failing — HTTP 403 since 06.10 | Q-0073, front line context for Q-0004 |
| NASA FIRMS (Gulf, western Russia) | skipped — API key not set | Strike and fire context (G1) |
| Saba (Yemen, Houthi state agency) | failing — HTTP 403 | A-perspective for Bab el-Mandeb events (Q-0043, Q-0062, Q-0068) |
| Tasnim (EN) | no items parsed | Iranian loyal perspective (other Iranian state sources work) |

Transient errors on 07.10 (connection resets or timeouts: mid_ru, mofcom_en, presstv, chinadaily_world) — sources otherwise ok.

## 5. Primary-data values for block L (from `indicators.md`)

| Indicator | Value | Date | Source |
|---|---|---|---|
| EUR/PLN (NBP table A) | 4.3797 | 07.10.2026 | api.nbp.pl |
| USD/PLN (NBP table A) | 3.9111 | 07.10.2026 | api.nbp.pl |
| EUR/USD (ECB reference) | 1.1269 | 06.10.2026 | ECB |
| USD/RUB, EUR/RUB, CNY/RUB (Bank of Russia official) | 85.7116 / 96.0313 / 12.7984 | 07.10.2026 | cbr.ru |
| Bank of Russia key rate | 14.00% | 07.10.2026 (raw snapshot) | cbr.ru |
| ECB deposit facility rate | 2.50% | in force since 16.09.2026 | ECB data portal |
| Fed funds target range | 3.75–4.00% | 06.10.2026 | FRED DFEDTARL/DFEDTARU |
| US 10-year Treasury yield | 5.31% | 05.10.2026 | FRED DGS10 |
| Broad US dollar index | 121.385 | 02.10.2026 | FRED DTWEXBGS |
| Brent spot (not ICE settlement) | 113.96 USD/bbl | 29.09.2026 | FRED DCOILBRENTEU |
| WTI spot | 96.16 USD/bbl | 29.09.2026 | FRED DCOILWTICO |
| Hormuz transits (all / tankers) | 4 / 0 | 04.10.2026 | IMF PortWatch |
| Bab el-Mandeb transits (all / tankers) | 34 / 11 | 04.10.2026 | IMF PortWatch |
| Suez Canal transits (all / tankers) | 46 / 15 | 04.10.2026 | IMF PortWatch |
| Bosporus transits (all / tankers) | 72 / 19 | 04.10.2026 | IMF PortWatch |
| Taiwan Strait transits (all) | 233 | 04.10.2026 | IMF PortWatch |
| Panama Canal transits (all) | 29 | 04.10.2026 | IMF PortWatch |
| OFAC SDN list change | 19 rows added, 144 removed | 06.10.2026 (vs 05.10 snapshot) | OFAC SDN list |

Not available from the harvest: TTF, EU and Polish gas storage, Polish fuel prices, NBP reference rate, ISW front assessments. These remain web-search items for stage 02.
