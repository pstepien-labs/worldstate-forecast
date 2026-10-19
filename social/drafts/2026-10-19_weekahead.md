# Social drafts — 19.10.2026 — weekahead

A 5-post thread for the week 19–25.10.2026. **Drafts only. Nothing has been posted.** Review, edit and post by hand. Character counts follow X's weighting: a link counts as 23, and most symbols outside Latin script count as 2 (so the bullets are hyphens).

Every value is an official AGG_RT value of edition 02 from `registry/forecasts.csv` (frozen 09.10.2026, commit f09a1d4), rounded to whole percent. No new probability is stated, no question is called likely beyond its official value, and nothing from `no_republish.txt` is quoted or linked (TASS and other Russian state reports of the Bank of Russia meeting were left out; cbr.ru is linked instead).

## 1. Opening post (attach the card)
Questions: the 15 with deadlines 20.10–23.10 (Q-0025, Q-0074, Q-0084; Q-0080, Q-0081, Q-0083, Q-0085, Q-0086, Q-0087, Q-0089, Q-0090, Q-0091, Q-0092; Q-0020, Q-0088), plus Q-0033 and Q-0093 (deadline 31.10, decided on 25.10) · edition 02 · frozen 09.10.2026
Card: `social/cards/edition-02/week-ahead.png` (window 19.10–26.10.2026; its 7 values match the registry)

Draft post (269 chars):
> Week ahead, 19–25.10: 15 of our frozen forecasts close by 23.10; two elections fall on 25.10.
> Values are the official ones from edition 02, frozen 09.10. We don't change them between editions; edition 03 scores them.
> AI-assisted, human-reviewed.
> https://pstepien-labs.github.io/worldstate-forecast/#forecasts

## 2. Tuesday 20.10
Question: Q-0074 · edition 02 · 0.633 · 20.10.2026 (ICE Futures Europe settlement) | Q-0084 · edition 02 · 0.437 · 20.10.2026 (ICE Endex settlement) | Q-0025 · edition 02 · 0.517 · 20.10.2026 (China customs data for September, expected about 20–21.10 per report K.6)

Draft post (279 chars):
> Tue 20.10, three close on one day:
> - Brent front month above 100 USD/bbl: 63% (Q-0074)
> - Dutch TTF front month above 80 EUR/MWh: 44% (Q-0084)
> - China's rare-earth magnet exports to the US in September above 512 t (customs data): 52% (Q-0025)
> Research questions, not market calls.

## 3. Wednesday 21.10
Question: Q-0083 · edition 02 · 0.90 · 21.10.2026 | Q-0080 · edition 02 · 0.787 · 21.10.2026 | Q-0092 · edition 02 · 0.233 · 21.10.2026 | Q-0081 · edition 02 · 0.103 · 21.10.2026
Evidence: Q-0083: Council Implementing Regulation (EU) 2026/2281 of 12.10.2026, OJ L 12.10.2026: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202602281 (checked for the 13.10 draft). It resolves formally in stage 01 of edition 03; the post says "adopted 12.10" and nothing more.

Draft post (260 chars):
> Wed 21.10, ten two-week windows close. Four:
> - EU adopts 1,500+ new Russia listings: 90% (Q-0083; adopted 12.10)
> - Saudi-reported death from a Yemen attack: 79% (Q-0080)
> - Ship hit in Red Sea/Gulf of Aden: 23% (Q-0092)
> - US–Iran meeting in person: 10% (Q-0081)

## 4. Friday 23.10 and Sunday 25.10
Question: Q-0020 · edition 02 · 0.143 · 23.10.2026 | Q-0088 · edition 02 · 0.083 · 23.10.2026 | Q-0033 · edition 02 · 0.29 · 31.10.2026 | Q-0093 · edition 02 · 0.267 · 31.10.2026
Evidence (checked 19.10.2026):
- Bank of Russia: next key-rate meeting 23.10.2026, rate held at 14% in September: The Star, 12.09.2026, https://www.thestar.com.my/news/world/2026/09/12/russian-central-bank-holds-key-rate-steady-at-14-pct ; meeting calendar: https://cbr.ru/eng/dkp/mp_dec/decision_key_rate/
- Brazil: runoff 25.10.2026 between Lula and Senator Flávio Bolsonaro after the 04.10 first round (TSE figures as reported): https://www.africanews.com/amp/2026/10/05/brazils-presidential-election-heads-to-runoff-between-bolsonara-and-lula/
- Bulgaria: first round of the presidential election 25.10.2026; a first-round win needs more than 50% of valid votes: https://en.wikipedia.org/wiki/2026_Bulgarian_presidential_election (secondary; the CEC is the deciding source)

Draft post (261 chars):
> Fri 23.10, Bank of Russia key-rate meeting: a cut 14% (Q-0020), a hike 8% (Q-0088).
> Sun 25.10, Brazil's runoff, Lula wins: 29% (Q-0033). Bulgaria's first round, Iotova above 50%: 27% (Q-0093).
> Decided by cbr.ru, Brazil's TSE and Bulgaria's electoral commission.

## 5. Full list and the brief
Links: the report annex lists all 88 AGG_RT forecasts of edition 02 by vector; the brief PDF is live (HTTP 200 on 19.10.2026).

Draft post (218 chars):
> All 88 forecasts of edition 02, including the other six closing on 21.10, with resolution criteria and sources:
> https://github.com/pstepien-labs/worldstate-forecast/blob/main/editions/2026-10-07_edition-02/07_report.md#annex-full-list-of-agg_rt-forecasts-by-vector
> The brief: https://pstepien-labs.github.io/worldstate-forecast/briefs/edition-02.pdf
> Hits and misses get the same space when scored.

## Notes for you

- **Q-0080 (79%)**: the edition 02 report (J.5, H.3) says two of three lenses missed "the 08.10 Saudi deaths", so the question may already be determined. I could not confirm the deaths in a Saudi official source today (searches found interceptions and one injury, no SPA casualty report). The post therefore states only the frozen value. Stage 01 of edition 03 decides it, and the `resolved` post will report the outcome.
- **Q-0090 (13%)**: the H.R. 5334 30-day deadline (about 18.10) has passed. I did not check whether an act was published; it is not in the posts, so nothing is claimed.
- **The card truncates three titles** (Q-0025, Q-0084, Q-0085) with an ellipsis. It is still readable; fixing the layout is a change to `tools/brief.py` (needs an approved proposal).
- The site's table shows 7 of the ten 21.10 questions (it shows 12 forecasts in all), so post 5 links the report annex for the full list.

Sources used: thestar.com.my, cbr.ru, africanews.com, en.wikipedia.org, eur-lex.europa.eu; other results read: interfax.com, gvwire.com, aa.com.tr, shafaq.com, khaleejtimes.com (no claims taken from them).
