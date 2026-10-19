# Stage E — Executive brief and social cards

Runs after stage 08 of an edition (from `/edition`, or `/gE`). Output: `<DIRECTORY>/E_brief_body.html` (written by you), and from `tools/brief.py`: `docs/briefs/edition-NN.html`, `docs/briefs/edition-NN.pdf` and the cards in `social/cards/edition-NN/`. Commit: `edition-NN brief`.

Provenance: `python3 tools/pipeline.py stage-start E --model "<your model id>"` … `stage-end E`.

## What the brief is

An easier-to-read view of the edition report for readers outside the project, about 11 A4 pages, grouped by region. **The report stays the primary document and the only source.** The brief adds no facts, no assessments and no forecasts of its own (CLAUDE.md 3.1). Every number in it must appear in `07_report.md` or `01_scores.md`; every forecast value is injected from the registry by the tool, never typed. `tools/brief.py` refuses to publish if anything does not match.

## Inputs (read only these)

`editions/CURRENT.md`; `<DIRECTORY>/07_report.md`; `<DIRECTORY>/01_scores.md`; `registry/questions.csv` (question wording, deadlines); the previous edition's `E_brief_body.html` as the structural template; `site/brief_template.html` (styles only, do not edit). Do not use `07_annex_benchmarks.md` or any crowd or market value: the brief compares only with the baselines in `01_scores.md`.

## Steps

1. Copy the structure of the previous edition's `E_brief_body.html` into `<DIRECTORY>/E_brief_body.html` and rewrite every text from the current report. Keep the placeholders (`{{EDITION}}`, `{{PREV}}`, `{{STATE_DATE}}`, `{{FREEZE_DATE}}`, `{{FREEZE_COMMIT}}`, `{{NEXT_EDITION}}` and those in the provenance note); the tool fills them.
2. Run `python3 tools/brief.py check`. Fix what it reports by changing **the brief**, never the report or the registry: a number it cannot find in the report is reworded to the report's figure or removed.
3. Run `python3 tools/brief.py build` (writes the HTML, the PDF and the cards). Open the PDF's page count in the output if you can; each chapter should fit on one A4 page — shorten facts or forecast rows where one spills.
4. `stage-end E`, then `git add -A` and commit `edition-NN brief`.

## Structure (one `<section class="chapter">` per page)

1. **At a glance**: masthead, `<h1>The balance of power on {{STATE_DATE}}</h1>`, the meta block, the bottom line (the report's executive-summary conclusion, labelled ASSESSMENT with its confidence), six "what changed" boxes (FACT, from the executive summary and section I), and the 6–12-month scenario bars with the table of scenario names.
2. **Headline forecasts and track record**: `<table class="fct" data-card="headline">` with 8 rows that best discriminate between the scenarios (section H.2), the scenario rationale (ASSESSMENT, from H.1 "Rationale"), and the track-record tiles (`data-check="track"`, numbers from section 0 / `01_scores.md`), followed by the reading guide.
3. **Six region chapters**, kicker `Region N of 6`: Gulf and Iran; Red Sea, Yemen and Saudi Arabia; Russia, Ukraine and NATO's eastern flank; USA–China and the Indo-Pacific; Europe, energy and global markets; shifting alignments (elections and orientation). If the report's weight moves, regions may be renamed or merged; keep six. Each: bottom line (ASSESSMENT + confidence, from sections A–G), 6–9 key facts, at most one disputed box (both readings, one line each), 5–9 forecast rows, "what would change our view" (from the report's early-warning signals and K.7) and dates (from K.6).
4. **Cross-cutting view**: the section G table, then **"How the regions connect"**: `<ol class="chain" data-card="crosslink">` of 4–5 steps taken from one of the report's "Mechanism" paragraphs (each step a dated fact with its record ID; the chain labelled ASSESSMENT), followed by 1–2 inline values (`<b class="pv" data-q="…"></b>`) of questions that would register it; then the country lens (Poland, section K) with 3 forecast rows.
5. **Dates that could reset the picture** (K.6) and **what could prove us wrong** (K.7).
6. **Method, gaps and provenance** (section J for the gaps).

## Markup rules

- A fact: `<li><span class="d">DD.MM</span><span><span class="tag">FACT</span>text <span class="src">publisher [rating]</span> <span class="ref">record ID</span></span></li>`. Facts after the state date also get `<span class="tag after">AFTER STATE DATE</span>`.
- An assessment: `<span class="tag as">ASSESSMENT</span>` and its confidence. Disputed: `<span class="tag disp">DISPUTED</span>` with both readings.
- A forecast row: `<tr class="fc" data-q="Q-XXXX"><td>short label</td></tr>` — only the label; the tool adds the deadline, value, words, change, confidence and ID. An inline value: `<b class="pv" data-q="Q-XXXX"></b>`. Never write a probability as a number in the text.
- Scenario shares: copy the shares of section H.1 into the bars (`flex:NN` and the label) and the previous edition's shares into `ed. {{PREV}}: a · b · c` (order: favourable, base, crisis). The tool checks both against H.1.
- Outlets on `sources/harvest/no_republish.txt` are never quoted or named as a source; write "according to Russian state media" or the report's paraphrase.
- Plain English for readers outside the project: no stage numbers, no internal codes except record IDs and question IDs.
