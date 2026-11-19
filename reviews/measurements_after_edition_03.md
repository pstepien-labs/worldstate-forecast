# Re-measurement of the review findings after edition 03 (WP-06)

Date: 19.11.2026, after the edition 03 resolutions. Source: `python3 tools/scores.py` at framework 1.9.1.
66 questions scored (13 auto-verified by stage V), 1 awaiting verification, 0 overdue.
The review of 16.11.2026 had N = 26.

| # | Finding (review 16.11) | Now | Verdict |
|---|---|---|---|
| Q1 | Lenses get almost no time (0.2 h per lens) | Edition 03: lens A 0.16 h, B 0.20 h. The 8 h of lens C is a usage-limit wait, see `stage_time_audit.md` | **holds** (addressed by WP-09 from edition 04) |
| Q2 | The three lenses are one forecast repeated | Correlation 0.91–0.96 in edition 03, median spread 0.05. No lens differs from AGG_RT: every paired 90% interval contains 0 | **holds** |
| Q3 | Forecasts too low on events that happened | All resolved: mean p 0.38 against YES rate 0.49 (−0.12). Closed cohort: −0.07. Horizons ≤100 days: −0.20. MIL −0.22, TEC −0.28 | **holds, smaller** |
| Q4 | Part of Q3 is a selection effect (early YES) | Closed cohort YES rate 0.44 against 0.49 for all resolved; the bias falls from −0.12 to −0.07 | **holds** |
| Q5 | The status-quo baseline is too easy | p_status_quo 0.10: N = 54, YES rate 0.44. BSS vs SQ 0.54; vs constant 0.50 only 0.31; vs the earlier YES rate 0.40 | **holds** (for P-0007 at the quarterly review) |
| Q6 | The red team has not shown value | AGG − AGG_RT paired difference −0.001, interval [−0.005, 0.002]; 3 closer / 7 further | **holds** (no evidence either way) |
| Q7 | Extremizing does not help | Log-odds mean with exponent 1.5: +0.004 [−0.007, 0.015] against AGG_RT | **holds** |
| Q8 | Numeric questions could be computed | Back-test (`quant_backtest.md`): QNT Brier 0.058 against AGG_RT 0.214 on the same 4 questions | **holds, N = 4** (shadow run QNT from edition 04) |
| Q9 | Crowd comparison empty | Not re-measured here; see `01_scores.md` of edition 03 | **unclear** |
| Q10 | No uncertainty reported | Intervals and paired differences are now in every `01_scores.md` | **fixed** |

All packages built on these findings stay in place; none is skipped.
Official measure (unchanged): AGG_RT Brier 0.173 [0.139, 0.206], BSS vs status quo 0.538 [0.433, 0.629].
