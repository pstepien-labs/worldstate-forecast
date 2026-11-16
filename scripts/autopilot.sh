#!/usr/bin/env bash
# Autopilot (framework 1.8, P-0012): the whole cycle without the user.
# launchd runs `tick` every hour. Each tick does at most one thing:
#   - an edition is open, or its brief/site is missing  -> resume `/edition --auto` (Claude Code, headless)
#   - the next edition is due                            -> start it (Sunday from AUTOPILOT_START_HOUR,
#                                                           or at once if it is more than 7 days late)
#   - Sunday of an off-week with failing sources         -> harvest source repair (/gH repair)
# Then it publishes: `git push origin main` and tags (GitHub Pages serves docs/), and a
# heartbeat in docs/data/autopilot.json that the cloud watchdog reads.
# Agents never push (denied in .claude/settings.json); only this script does.
#
#   scripts/autopilot.sh install     install the hourly launchd job (macOS) and run one tick now
#   scripts/autopilot.sh uninstall   remove the launchd job
#   scripts/autopilot.sh tick        one step now (what launchd runs)
#   scripts/autopilot.sh status      next action, last runs, inbox
#   scripts/autopilot.sh pause       stop acting (ticks exit at once) · resume: undo
#   scripts/autopilot.sh tail        follow the autopilot log
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd)
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
PY="${PYTHON:-python3}"
DATA="$ROOT/data/autopilot"
LOG="$DATA/autopilot.log"
STATE="$DATA/state.json"
LOCK="$DATA/lock"
LABEL="com.worldstate-forecast.autopilot"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
START_DOW="${AUTOPILOT_START_DOW:-7}"         # day editions start: 1=Mon … 7=Sun (date +%u)
START_HOUR="${AUTOPILOT_START_HOUR:-20}"      # local hour from which they start that day
MAX_RUN_HOURS="${AUTOPILOT_MAX_RUN_HOURS:-12}"  # one headless run is stopped after this; the next tick resumes it
PERMISSION_MODE="${AUTOPILOT_PERMISSION_MODE:-auto}"
MODEL="${AUTOPILOT_MODEL:-}"                  # empty = Claude Code's default model
mkdir -p "$DATA/runs"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $*" | tee -a "$LOG"; }

notify() {  # local macOS notification + inbox line (the cloud watchdog reaches the phone)
  log "NOTIFY: $1"
  command -v osascript >/dev/null 2>&1 && osascript -e "display notification \"${1//\"/\'}\" with title \"Worldstate autopilot\"" >/dev/null 2>&1 || true
}

jget() {  # jget <file> <key> [default]
  "$PY" - "$1" "$2" "${3:-}" <<'EOF'
import json, sys
try:
    v = json.load(open(sys.argv[1])).get(sys.argv[2], sys.argv[3])
except Exception:
    v = sys.argv[3]
print(json.dumps(v) if isinstance(v, (list, dict, bool)) else v)
EOF
}

state_set() {  # state_set key value  (value as JSON or plain string)
  "$PY" - "$STATE" "$1" "$2" <<'EOF'
import json, os, sys
p, k, v = sys.argv[1:]
d = json.load(open(p)) if os.path.exists(p) else {}
try:
    d[k] = json.loads(v)
except ValueError:
    d[k] = v
json.dump(d, open(p, 'w'), indent=1)
EOF
}

take_lock() {
  if ! mkdir "$LOCK" 2>/dev/null; then
    local pid; pid=$(cat "$LOCK/pid" 2>/dev/null || echo 0)
    if [ "$pid" != 0 ] && kill -0 "$pid" 2>/dev/null; then exit 0; fi  # a run is in progress
    rm -rf "$LOCK"; mkdir "$LOCK" || exit 0
  fi
  echo $$ > "$LOCK/pid"
  trap 'rm -rf "$LOCK"' EXIT
}

status_json() { "$PY" tools/pipeline.py status --json > "$DATA/status.json" 2>>"$LOG"; }

decide() {  # prints: edition | repair | none, with a reason
  "$PY" - "$DATA/status.json" "$STATE" "$START_DOW" "$START_HOUR" <<'EOF'
import json, os, sys
from datetime import date, datetime
st = json.load(open(sys.argv[1]))
state = json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {}
dow, hour = int(sys.argv[3]), int(sys.argv[4])
now = datetime.now()
# back-off after failures: 1, 2, 4, 8, 16, 24 hours
fails = int(state.get('consecutive_failures', 0))
if fails:
    wait_h = min(24, 2 ** (fails - 1))
    last = datetime.fromisoformat(state.get('last_run_end', '2000-01-01T00:00:00'))
    if (now - last).total_seconds() < wait_h * 3600 - 300:
        print(f'none backing off {wait_h}h after {fails} failed run(s)'); sys.exit()
if not st.get('edition_closed'):
    print(f"edition resume edition {st.get('edition')} at stage {st['next']['stage']} {st['next'].get('arg') or ''}"); sys.exit()
if not st.get('brief_done') or not st.get('site_done'):
    print(f"edition finish brief/site of edition {st.get('edition')}"); sys.exit()
if st.get('can_start_next_edition'):
    late = (date.today() - date.fromisoformat(st['earliest_state_date'])).days
    if late >= 7 or (now.isoweekday() == dow and now.hour >= hour):
        print(f"edition start edition {st['next_edition']} ({late} day(s) after the earliest date)"); sys.exit()
week = now.strftime('%G-W%V')
if now.isoweekday() == dow and now.hour >= hour and state.get('repair_week') != week:
    print(f'repair weekly source check {week}'); sys.exit()
print('none nothing due')
EOF
}

run_claude() {  # run_claude <label> <prompt>
  local label="$1" prompt="$2" ts out pid killer rc
  ts=$(date '+%Y%m%d-%H%M%S'); out="$DATA/runs/$ts-$label.log"
  log "RUN $label → $out"
  state_set last_run_start "\"$(date '+%Y-%m-%dT%H:%M:%S')\""
  local args=(-p "$prompt" --permission-mode "$PERMISSION_MODE" --output-format text)
  [ -n "$MODEL" ] && args+=(--model "$MODEL")
  claude "${args[@]}" < /dev/null > "$out" 2>&1 &
  pid=$!
  command -v caffeinate >/dev/null 2>&1 && { caffeinate -i -s -w "$pid" & }   # keep the Mac awake while it runs
  ( sleep $((MAX_RUN_HOURS * 3600)); kill "$pid" 2>/dev/null ) & killer=$!
  wait "$pid"; rc=$?
  kill "$killer" 2>/dev/null; wait "$killer" 2>/dev/null
  state_set last_run_end "\"$(date '+%Y-%m-%dT%H:%M:%S')\""
  RESULT=$(grep -E '^AUTOPILOT:' "$out" | tail -1)
  [ -z "$RESULT" ] && RESULT="AUTOPILOT: exit $rc (no result line; see $out)"
  log "END $label rc=$rc · $RESULT"
  find "$DATA/runs" -name '*.log' -mtime +60 -delete 2>/dev/null || true
}

publish() {  # push committed work; GitHub Pages rebuilds from docs/
  git fetch -q origin 2>>"$LOG" || { log "fetch failed (offline?)"; return; }
  if [ "$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)" != 0 ]; then
    git merge --ff-only -q origin/main 2>>"$LOG" || { notify "Local and GitHub history diverged: push skipped (resolve by hand)"; return; }
  fi
  if [ "$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)" != 0 ]; then
    if git push -q origin main 2>>"$LOG" && git push -q origin --tags 2>>"$LOG"; then
      log "pushed to origin/main ($(git rev-parse --short HEAD))"
    else
      notify "git push failed; will retry next hour"
    fi
  fi
}

heartbeat() {  # docs/data/autopilot.json: committed when its content changes, or at least every 3 days
  "$PY" - "$DATA/status.json" "$STATE" "$ROOT/docs/data/autopilot.json" "$ROOT/AUTOPILOT_INBOX.md" <<'EOF'
import json, os, re, sys
from datetime import datetime, timezone
st = json.load(open(sys.argv[1])); state = json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {}
out, inbox = sys.argv[3], sys.argv[4]
blockers = 0
if os.path.exists(inbox):
    m = re.search(r'## Blockers\n(.*?)(\n## |\Z)', open(inbox, encoding='utf-8').read(), re.S)
    blockers = len([l for l in (m.group(1) if m else '').splitlines() if l.strip().startswith('-')])
hb = {'edition': st.get('edition'), 'state_date': st.get('state_date'), 'edition_closed': st.get('edition_closed'),
      'next_stage': None if st.get('edition_closed') else (st.get('next') or {}).get('cmd'),
      'earliest_next_edition': st.get('earliest_state_date'), 'last_result': state.get('last_result'),
      'consecutive_failures': state.get('consecutive_failures', 0), 'open_blockers': blockers,
      'resolutions_disputed': len(st.get('verification_disputed') or []),
      'harvester': st.get('harvester'), 'framework_version': st.get('framework_version')}
old = json.load(open(out)) if os.path.exists(out) else {}
age_h = 1e9
if old.get('updated'):
    age_h = (datetime.now(timezone.utc) - datetime.fromisoformat(old['updated'].replace('Z', '+00:00'))).total_seconds() / 3600
same = {k: v for k, v in old.items() if k not in ('updated', 'harvester')} == {k: v for k, v in hb.items() if k != 'harvester'}
if same and age_h < 72:
    sys.exit(1)
hb['updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(hb, open(out, 'w'), indent=1)
EOF
  [ $? -eq 0 ] && git add docs/data/autopilot.json && git commit -q -m "autopilot: heartbeat" -- docs/data/autopilot.json >/dev/null 2>&1 && log "heartbeat committed"
  return 0
}

tick() {
  [ -f "$DATA/PAUSED" ] && exit 0
  take_lock
  [ "$(git rev-parse --abbrev-ref HEAD)" = main ] || { notify "Repository not on branch main: autopilot idle"; exit 0; }
  "$PY" -m tools.harvester status 2>/dev/null | grep -q 'LIVENESS: running' || { log "harvester not running: starting"; scripts/harvest.sh start >>"$LOG" 2>&1; }
  status_json || { notify "pipeline status failed"; exit 0; }
  local decision action reason
  decision=$(decide); action=${decision%% *}; reason=${decision#* }
  RESULT=""
  case "$action" in
    edition)
      log "edition: $reason"
      local before; before=$(jget "$DATA/status.json" next)
      run_claude edition "Read CLAUDE.md and prompts/RUN_edition.md and act as the orchestrator described there, in AUTO mode. Arguments: --auto"
      status_json
      local after; after=$(jget "$DATA/status.json" next)
      if [[ "$RESULT" == "AUTOPILOT: complete"* ]] || [[ "$RESULT" == "AUTOPILOT: not-due"* ]] || [ "$before" != "$after" ]; then
        state_set consecutive_failures 0
      else
        local n; n=$(( $(jget "$STATE" consecutive_failures 0) + 1 )); state_set consecutive_failures "$n"
        [ "$n" -eq 2 ] && notify "Edition stuck at the same stage twice: $RESULT"
      fi
      [[ "$RESULT" == "AUTOPILOT: complete"* ]] && notify "Edition published: $RESULT"
      [[ "$RESULT" == "AUTOPILOT: blocked"* ]] && notify "$RESULT"
      state_set last_result "\"$(date '+%Y-%m-%d %H:%M') $RESULT\""
      ;;
    repair)
      state_set repair_week "\"$(date '+%G-W%V')\""
      local failing; failing=$("$PY" -m tools.harvester status 2>/dev/null | grep -oE 'failing [0-9]+' | head -1 | grep -oE '[0-9]+' || echo 0)
      if [ "${failing:-0}" -ge 3 ]; then
        log "repair: $failing failing sources"
        run_claude repair "Read CLAUDE.md and prompts/H_harvest.md and carry out MODE repair. Nobody is watching: do not ask questions; record anything that needs the user under '## Waiting for the user' in AUTOPILOT_INBOX.md. Never run git push. Last line of your final message: 'AUTOPILOT: complete repair' or 'AUTOPILOT: blocked repair <reason>'."
        state_set last_result "\"$(date '+%Y-%m-%d %H:%M') $RESULT\""
      else
        log "repair: not needed ($failing failing)"
      fi
      ;;
    *) : ;;
  esac
  status_json
  heartbeat
  publish
}

install() {
  [ "$(uname)" = Darwin ] || { echo "install is for macOS (launchd). Elsewhere run 'scripts/autopilot.sh tick' hourly from cron."; exit 1; }
  mkdir -p "$(dirname "$PLIST")"
  cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key><array><string>/bin/bash</string><string>$ROOT/scripts/autopilot.sh</string><string>tick</string></array>
  <key>WorkingDirectory</key><string>$ROOT</string>
  <key>StartInterval</key><integer>3600</integer>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>$DATA/launchd.out</string>
  <key>StandardErrorPath</key><string>$DATA/launchd.err</string>
  <key>EnvironmentVariables</key><dict><key>HOME</key><string>$HOME</string><key>LANG</key><string>en_US.UTF-8</string></dict>
</dict></plist>
EOF
  launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$PLIST" && echo "Installed $LABEL (hourly; first tick running now). Log: scripts/autopilot.sh tail"
}

case "${1:-status}" in
  tick) tick ;;
  install) install ;;
  uninstall) launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null; rm -f "$PLIST"; echo "Removed $LABEL." ;;
  pause) touch "$DATA/PAUSED"; echo "Paused (ticks exit at once). Undo: scripts/autopilot.sh resume" ;;
  resume) rm -f "$DATA/PAUSED"; echo "Resumed." ;;
  tail) tail -n 40 -f "$LOG" ;;
  status)
    status_json; echo "Next action: $(decide)"
    [ -f "$DATA/PAUSED" ] && echo "PAUSED"
    [ -d "$LOCK" ] && echo "Running now: pid $(cat "$LOCK/pid" 2>/dev/null)"
    launchctl print "gui/$(id -u)/$LABEL" >/dev/null 2>&1 && echo "launchd job: installed" || echo "launchd job: NOT installed (scripts/autopilot.sh install)"
    echo "--- last log lines"; tail -n 8 "$LOG" 2>/dev/null
    [ -f AUTOPILOT_INBOX.md ] && { echo "--- AUTOPILOT_INBOX.md"; cat AUTOPILOT_INBOX.md; }
    ;;
  *) sed -n '2,18p' "$0"; exit 1 ;;
esac
