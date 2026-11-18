#!/usr/bin/env bash
# Replay a lens prompt on a closed edition, without web access (framework 1.9, WP-07).
#   scripts/replay.sh <edition NN> <LENS> <label> [prompt file, default prompts/04_forecasts.md]
# Writes reviews/replay/<date>_<label>/ (questions, forecasts, validity, run log) and scores it:
#   python3 tools/scores.py --add-forecasts reviews/replay/<date>_<label>/forecasts.csv
set -euo pipefail
cd "$(dirname "$0")/.."
NR=$(printf '%02d' "$((10#$1))"); LENS=$2; LABEL=$3; PROMPT=${4:-prompts/04_forecasts.md}
EDIR=$(ls -d editions/*_edition-"$NR" | head -1)
OUT="reviews/replay/$(date +%Y-%m-%d)_$LABEL"
MODEL=$(python3 tools/autopilot.py conf AUTOPILOT_MODEL)
mkdir -p "$OUT"
python3 - "$NR" "$OUT" <<'PY'
import csv, sys
nr, out = sys.argv[1:]
R = lambda f: list(csv.DictReader(open('registry/' + f, encoding='utf-8-sig'), delimiter=';'))
ids = {f['question_id'] for f in R('forecasts.csv') if f['edition'] == nr and f['run'] == 'AGG_RT'}
keep = ['id', 'created', 'type', 'vector', 'region', 'cluster', 'question', 'resolution_criterion', 'resolution_source', 'deadline', 'p_status_quo', 'who_benefits']
with open(out + '/questions.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    w.writerow(keep)
    for q in R('questions.csv'):
        if q['id'] in ids:
            w.writerow([q[k] for k in keep])
print(f'{len(ids)} questions of edition {nr} -> {out}/questions.csv')
PY
FIRST=$(head -1 "$EDIR/03_analysis.md")
if [ "$LENS" = B2 ]; then
  # base rates as they were at the edition's cutoff: only resolutions dated before it
  CUT=$(echo "$FIRST" | sed -E 's/.*([0-9]{2})\.([0-9]{2})\.([0-9]{4}).*/\3-\2-\1/')
  python3 tools/scores.py --base-rates "$OUT/base_rates.csv" --as-of "$CUT" >/dev/null
fi
export BLINDNESS_STAGE="R" BLINDNESS_REPLAY_DIR="$EDIR" BLINDNESS_REPLAY_OUT="$OUT"
claude -p "Read prompts/R_replay.md and carry out a replay. EDITION_DIR=$EDIR LENS=$LENS PROMPT=$PROMPT OUT=$OUT LABEL=$LABEL" \
  --model "$MODEL" --permission-mode "$(python3 tools/autopilot.py conf AUTOPILOT_PERMISSION_MODE auto)" \
  --disallowedTools WebSearch WebFetch --output-format text < /dev/null > "$OUT/run.log" 2>&1 || true
tail -1 "$OUT/run.log"
[ -f "$OUT/forecasts.csv" ] && python3 tools/scores.py --add-forecasts "$OUT/forecasts.csv" > "$OUT/scores.md" && echo "scores: $OUT/scores.md"
