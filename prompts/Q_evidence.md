# Stage Q-prep — Evidence file for the quarterly review (autopilot)

Framework 1.9 (WP-14). The autopilot runs this once, from `AUTOPILOT_QPREP_FROM` in `autopilot.conf` (19.12.2026). It **prepares evidence, decides nothing and changes nothing** except writing one file and its commit. The quarterly review itself (`prompts/Q_quarterly_review.md`, `/gQ`) needs the user.

Provenance: `python3 tools/pipeline.py stage-start QE --model "<your model id>"` … `python3 tools/pipeline.py stage-end QE`. Output: `reviews/quarterly_2026Q4_evidence.md`. Commit: `quarterly review evidence 2026-Q4`.

## Sections

1. **Scores.** `python3 tools/scores.py` over all editions, plus the closed-cohort diagnostics (only questions whose deadline has passed). Quote N, Brier and BSS with their 90% intervals.
2. **P-0007, baselines.** BSS of `AGG_RT` against: the status quo, a constant 0.50, the family base rate (`registry/base_rates.csv`), and `QNT` on the numeric questions. Draft a recommendation, as text for the user, to make the family base rate the official first baseline.
3. **P-0008, lens diversity.**
   - Correlations by edition.
   - The paired comparison (`python3 tools/scores.py --bootstrap X AGG_RT`) for `B2`, `QNT`, the derived aggregates, and A, B and C.
   - Lens time and searches per edition, from provenance and the logs.
4. **Red team.** Brier with and without adjustments, by adjustment type; the coherence violations found per edition.
5. **A second model as a lens (Grok, xAI).** Design only, with no code:
   - the packet sent (public facts and questions only);
   - the run label `D`;
   - the cost per edition;
   - the change rule 3.13 would need;
   - the key, which goes in `.env`.
6. **Cadence.**
   - Agent hours per edition from provenance (editions 03 to the latest).
   - Usage-limit stops from `data/autopilot/autopilot.log`.
   - Whether weekly interim resolutions gave enough freshness.
   - Three options: stay at 14 days; a weekly re-forecast of questions due within 21 days; full weekly editions.
7. **Recalibration.** If the closed cohort has N ≥ 60: fit one log-odds shift with leave-one-cluster-out, and report the Brier it would have given. Otherwise write "not enough data".
8. **Shadow runs against the judging rule.** For each shadow run, give its paired N and interval against the run it would replace. The rule: 30 paired resolved questions, and an interval that excludes zero.

The last line of your final message is `AUTOPILOT: complete qprep` or `AUTOPILOT: blocked qprep <reason>`. Never push.
