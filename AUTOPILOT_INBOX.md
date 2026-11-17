# Autopilot inbox

What the unattended cycle (`scripts/autopilot.sh`, framework 1.8) could not settle alone. Nothing here blocks the cycle except items under **Blockers**. Remove an item once it is dealt with.

- To approve a disputed resolution, append a row to `registry/resolutions.csv`: copy the latest row with `version` + 1, `user_approved` = `Y` and a note. Or correct the outcome in that row.
- To stop the autopilot: `scripts/autopilot.sh pause`. To restart it: `scripts/autopilot.sh resume`.

## Blockers

## Waiting for the user

- 17.11.2026 · Q-0079 · stage V (edition 03) could not re-read IMF PortWatch (HTTP 429 quota exceeded), so the stage 01 YES (13.10.2026 = 17 transits) is unconfirmed for 08, 09 and 12–15.10; re-check the PortWatch series and approve or correct (see `editions/2026-11-16_edition-03/V_autoverify.md`).

## Decisions taken without the user

- 17.11.2026 · stage 03 (edition 03) · Q-0143 (US shutdown 12–31.12): p_status_quo set to 0.90, because with no new decision the continuing resolution expires on 11.12 and appropriations lapse (literal §3.5); a first use of this reading. Review in `editions/2026-11-16_edition-03/03_question_bank_changes.md` §1.
- 17.11.2026 · stage 03 (edition 03) · Panel replacements outside the original cluster, whose outcome was exhausted: Q-0033 (BRAZIL_ELECTIONS) → Q-0123 (DOM, RS_GOVERNMENT, Serbian government); Q-0031 (US_ELECTIONS) → Q-0122 (Hegseth leaving office, cluster kept as the midterms' consequences); Q-0004 (DeepState territory, no readable source) → Q-0116 (Russian MoD drone count, UA_FRONT). Review in §3 of the same file.
- 17.11.2026 · stage 04 A (edition 03) · Blindness incident: a format check (`tail` on `registry/forecasts.csv`) displayed the last two registry rows — edition-02 AGG/AGG_RT for one question, with that edition's lens values. It happened after all 83 lens-A forecasts were written; none was changed afterwards. Autopilot continued (lens A kept as written; later stages told to read only the CSV header). Judge whether to accept — details in `editions/2026-11-16_edition-03/log.md`.
- 17.11.2026 · stage 03 (edition 03) · Note for Q-0079: the PortWatch ArcGIS API was readable on 17.11.2026 (rows to 15.11), so the October rows may now be checkable.
