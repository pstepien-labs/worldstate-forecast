#!/usr/bin/env bash
# Autopilot (framework 1.9): the whole cycle without the user.
# Two launchd jobs (macOS):
#   com.worldstate-forecast.harvester   the harvester, kept alive by launchd (KeepAlive)
#   com.worldstate-forecast.autopilot   `tick` every hour
# Each tick asks tools/autopilot.py what to do (edition / learn / interim / repair / qprep / none), runs at most
# one headless Claude Code session for it, then publishes: push to GitHub (GitHub Pages serves docs/),
# a GitHub release per edition, and the heartbeat docs/data/autopilot.json read by the cloud watchdog.
# Agents never push: origin's push URL is DISABLED for them; only this script pushes, to the `publish` remote.
#
#   scripts/autopilot.sh install     install both launchd jobs and run one tick now
#   scripts/autopilot.sh uninstall   remove both jobs (the harvester stops)
#   scripts/autopilot.sh tick        one step now (what launchd runs)
#   scripts/autopilot.sh status      next action, jobs, last runs, inbox
#   scripts/autopilot.sh pause       stop acting (ticks exit at once) · resume: undo
#   scripts/autopilot.sh backup      archive the harvest data to BACKUP_DIR now
#   scripts/autopilot.sh tail        follow the autopilot log
# Settings: autopilot.conf (KEY=value); environment variables of the same name win.
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd)
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
PY="${PYTHON:-python3}"
AP="$PY $ROOT/tools/autopilot.py"
DATA="$ROOT/data/autopilot"
LOG="$DATA/autopilot.log"
LOCK="$DATA/lock"
LABEL="com.worldstate-forecast.autopilot"
HLABEL="com.worldstate-forecast.harvester"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
HPLIST="$HOME/Library/LaunchAgents/$HLABEL.plist"
mkdir -p "$DATA/runs"

conf() { $AP conf "$1" "${2:-}"; }
MODEL=$(conf AUTOPILOT_MODEL)
PERMISSION_MODE=$(conf AUTOPILOT_PERMISSION_MODE auto)
MAX_RUN_HOURS=$(conf AUTOPILOT_MAX_RUN_HOURS 12)
BACKUP_DIR=$(conf BACKUP_DIR "")

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $*" | tee -a "$LOG"; }
notify() {
  log "NOTIFY: $1"
  command -v osascript >/dev/null 2>&1 && osascript -e "display notification \"${1//\"/\'}\" with title \"Worldstate autopilot\"" >/dev/null 2>&1 || true
}
sset() { $AP state-set "$1" "$2"; }
sget() { $AP state-get "$1" "${2:-}"; }

take_lock() {
  if ! mkdir "$LOCK" 2>/dev/null; then
    local pid; pid=$(cat "$LOCK/pid" 2>/dev/null || echo 0)
    if [ "$pid" != 0 ] && kill -0 "$pid" 2>/dev/null; then exit 0; fi
    rm -rf "$LOCK"; mkdir "$LOCK" || exit 0
  fi
  echo $$ > "$LOCK/pid"
  trap 'rm -rf "$LOCK"' EXIT
}

status_json() { "$PY" tools/pipeline.py status --json > "$DATA/status.json.tmp" 2>>"$LOG" && mv "$DATA/status.json.tmp" "$DATA/status.json"; }
next_stage() { "$PY" -c "import json;print(json.dumps(json.load(open('$DATA/status.json')).get('next')))"; }

inbox_add() {  # inbox_add "<section>" "<line>"
  "$PY" - "$ROOT/AUTOPILOT_INBOX.md" "$1" "$2" <<'EOF'
import sys
p, sec, line = sys.argv[1:]
t = open(p, encoding='utf-8').read() if __import__('os').path.exists(p) else '# Autopilot inbox\n\n## Blockers\n\n## Waiting for the user\n\n## Decisions taken without the user\n'
h = f'## {sec}\n'
if h not in t:
    t = t.rstrip('\n') + f'\n\n{h}'
i = t.index(h) + len(h)
t = t[:i] + f'- {line}\n' + t[i:]
open(p, 'w', encoding='utf-8').write(t)
EOF
  git add AUTOPILOT_INBOX.md && git commit -q -m "autopilot: inbox" -- AUTOPILOT_INBOX.md >/dev/null 2>&1 || true
}

run_claude() {  # run_claude <label> <prompt>  → sets KIND (ok|limit|blocked|failed), RESULT, OUT
  local label="$1" prompt="$2" ts pid killer rc
  ts=$(date '+%Y%m%d-%H%M%S'); OUT="$DATA/runs/$ts-$label.log"
  log "RUN $label (model $MODEL) → $OUT"
  sset last_run_start "\"$(date '+%Y-%m-%dT%H:%M:%S')\""
  claude -p "$prompt" --model "$MODEL" --permission-mode "$PERMISSION_MODE" --output-format text < /dev/null > "$OUT" 2>&1 &
  pid=$!
  command -v caffeinate >/dev/null 2>&1 && { caffeinate -i -s -w "$pid" & }
  ( sleep $((MAX_RUN_HOURS * 3600)); kill "$pid" 2>/dev/null ) & killer=$!
  wait "$pid"; rc=$?
  kill "$killer" 2>/dev/null; wait "$killer" 2>/dev/null
  sset last_run_end "\"$(date '+%Y-%m-%dT%H:%M:%S')\""
  local cls; cls=$($AP result "$OUT")
  KIND=${cls%% *}
  RESULT=$(grep -E '^AUTOPILOT:' "$OUT" | tail -1)
  [ -z "$RESULT" ] && RESULT="exit $rc ($KIND)"
  if [ "$KIND" = limit ]; then
    sset wait_until "\"${cls#* }\""
    log "usage limit reached: next try after ${cls#* } (not counted as a failure)"
  fi
  log "END $label rc=$rc · $KIND · $RESULT"
  find "$DATA/runs" -name '*.log' -mtime +60 -delete 2>/dev/null || true
}

count_failure() {
  local n; n=$(( $(sget consecutive_failures 0) + 1 )); sset consecutive_failures "$n"
  [ "$n" -eq 2 ] && notify "Autopilot failed twice in a row: $1"
  return 0
}

publish() {
  git fetch -q origin 2>>"$LOG" || { log "fetch failed (offline?)"; return; }
  if [ "$(git rev-list --count HEAD..origin/main 2>/dev/null || echo 0)" != 0 ]; then
    git merge --ff-only -q origin/main 2>>"$LOG" || { notify "Local and GitHub history diverged: push skipped"; return; }
  fi
  local url; url=$(git remote get-url publish 2>/dev/null || git remote get-url origin)
  if [ "$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)" != 0 ]; then
    if git push -q "$url" main 2>>"$LOG" && git push -q "$url" --tags 2>>"$LOG"; then
      git fetch -q origin 2>>"$LOG"
      log "pushed to GitHub ($(git rev-parse --short HEAD))"
    else
      notify "git push failed; will retry next hour"
      return
    fi
  fi
  release_editions
}

release_editions() {  # WP-21: one GitHub release per published edition (Zenodo archives it if linked)
  command -v gh >/dev/null 2>&1 || return 0
  local tag nr dir
  for tag in $(git tag -l 'edition-*' | sort); do
    nr=${tag#edition-}
    [ "$nr" -ge 2 ] 2>/dev/null || continue
    [ -f "docs/briefs/edition-$nr.pdf" ] || continue
    "$PY" -c "import json,sys;d=json.load(open('$DATA/state.json')) if __import__('os').path.exists('$DATA/state.json') else {};sys.exit(0 if '$tag' in d.get('released',[]) else 1)" && continue
    dir=$(ls -d editions/*_edition-"$nr" 2>/dev/null | head -1)
    if gh release view "$tag" >/dev/null 2>&1 || gh release create "$tag" "$dir/07_report.md" "docs/briefs/edition-$nr.pdf" \
        --title "Edition $nr" --notes "Forecast edition $nr. Report and executive brief; forecasts frozen in this tag's history (registry/forecasts.csv)." >/dev/null 2>>"$LOG"; then
      "$PY" - "$DATA/state.json" "$tag" <<'EOF'
import json, os, sys
p, t = sys.argv[1:]
d = json.load(open(p)) if os.path.exists(p) else {}
d['released'] = sorted(set(d.get('released', [])) | {t})
json.dump(d, open(p, 'w'), indent=1)
EOF
      log "GitHub release $tag ready"
    fi
  done
}

backup() {  # WP-18: weekly archive of the harvest data (skipped if BACKUP_DIR is not set)
  [ -n "$BACKUP_DIR" ] || return 0
  [ -d "$BACKUP_DIR" ] || { log "backup: BACKUP_DIR $BACKUP_DIR not found"; return 0; }
  local out recent
  out="$BACKUP_DIR/worldstate-harvest-$(date '+%Y%m%d').tar.gz"
  recent=$(find data/harvest/items -mindepth 1 -maxdepth 1 -type d -newermt "$(date -v-60d '+%Y-%m-%d' 2>/dev/null || date -d '-60 days' '+%Y-%m-%d')" 2>/dev/null)
  if tar -czf "$out" data/harvest/datasets data/harvest/state $recent 2>>"$LOG"; then
    log "backup written: $out ($(du -h "$out" | cut -f1))"
    ls -1t "$BACKUP_DIR"/worldstate-harvest-*.tar.gz 2>/dev/null | tail -n +5 | xargs rm -f 2>/dev/null
    sset backup_week "\"$(date '+%G-W%V')\""
  else
    notify "backup failed"
  fi
}

metrics() {  # 1.9.2: plan §5 measures, mechanically, after each published edition and weekly (Sundays)
  local ed closed site
  read -r ed closed site < <("$PY" -c "import json;d=json.load(open('$DATA/status.json'));print(d.get('edition'),d.get('edition_closed'),d.get('site_done'))")
  local want=""
  [ "$closed" = True ] && [ "$site" = True ] && [ "$(sget metrics_done_for)" != "$ed" ] && want="$ed"
  [ "$(date '+%u')" = 7 ] && [ "$(sget metrics_week)" != "$(date '+%G-W%V')" ] && want="all"
  [ -n "$want" ] || return 0
  if "$PY" tools/pipeline.py edition-metrics --all --append >/dev/null 2>>"$LOG"; then
    git add reviews/edition_metrics.csv && git commit -q -m "autopilot: edition metrics" -- reviews/edition_metrics.csv >/dev/null 2>&1 && log "edition metrics updated"
    [ "$want" = all ] && sset metrics_week "\"$(date '+%G-W%V')\""
    [ "$closed" = True ] && [ "$site" = True ] && sset metrics_done_for "\"$ed\""
  fi
}

harvester_check() {
  "$PY" -m tools.harvester status 2>/dev/null | grep -q 'LIVENESS: running' && return
  if launchctl print "gui/$(id -u)/$HLABEL" >/dev/null 2>&1; then
    log "harvester not running although its launchd job exists: kickstart"
    launchctl kickstart -k "gui/$(id -u)/$HLABEL" 2>>"$LOG"
  else
    notify "Harvester not running and its launchd job is not installed: run scripts/autopilot.sh install"
  fi
}

PROMPT_EDITION="Read CLAUDE.md and prompts/RUN_edition.md and act as the orchestrator described there, in AUTO mode. Arguments: --auto"
PROMPT_LEARN="Read CLAUDE.md and prompts/RUN_learning.md and run the learning loop for the latest closed edition in AUTO mode (section 'AUTO mode' of that file). Arguments: latest --auto"
PROMPT_INTERIM="Read CLAUDE.md and prompts/I_interim.md and carry out the interim resolutions in AUTO mode."
PROMPT_REPAIR="Read CLAUDE.md and prompts/H_harvest.md and carry out MODE repair. Nobody is watching: do not ask questions; record anything that needs the user under '## Waiting for the user' in AUTOPILOT_INBOX.md. Never push. Last line of your final message: 'AUTOPILOT: complete repair' or 'AUTOPILOT: blocked repair <reason>'."
PROMPT_QPREP="Read CLAUDE.md and prompts/Q_evidence.md and write the evidence file for the quarterly review in AUTO mode."

tick() {
  [ -f "$DATA/PAUSED" ] && exit 0
  take_lock
  [ "$(git rev-parse --abbrev-ref HEAD)" = main ] || { notify "Repository not on branch main: autopilot idle"; exit 0; }
  harvester_check
  status_json || { notify "pipeline status failed"; exit 0; }
  [ "$(sget backup_week)" != "$(date '+%G-W%V')" ] && [ "$(date '+%u')" = 7 ] && backup
  local decision action reason before
  decision=$($AP decide); action=${decision%% *}; reason=${decision#* }
  case "$action" in
    edition)
      log "edition: $reason"
      before=$(next_stage)
      run_claude edition "$PROMPT_EDITION"
      status_json
      case "$KIND" in
        ok) sset consecutive_failures 0; sset wait_until null
            [[ "$RESULT" == "AUTOPILOT: complete"* ]] && notify "Edition published: $RESULT" ;;
        limit) [ "$before" != "$(next_stage)" ] && sset consecutive_failures 0 ;;
        blocked) notify "$RESULT"; count_failure "$RESULT" ;;
        *) if [ "$before" != "$(next_stage)" ]; then sset consecutive_failures 0; else count_failure "$RESULT"; fi ;;
      esac
      sset last_result "\"$(date '+%Y-%m-%d %H:%M') $KIND $RESULT\"" ;;
    learn|interim|qprep|repair)
      log "$action: $reason"
      local prompt
      case "$action" in learn) prompt=$PROMPT_LEARN;; interim) prompt=$PROMPT_INTERIM;; qprep) prompt=$PROMPT_QPREP;; repair) prompt=$PROMPT_REPAIR;; esac
      run_claude "$action" "$prompt"
      local ed; ed=$("$PY" -c "import json;print(json.load(open('$DATA/status.json')).get('edition'))")
      if [ "$KIND" != limit ]; then   # one attempt per edition/week; a failure goes to the inbox, never loops
        case "$action" in
          learn) sset learn_done_for "\"$ed\"" ;;
          interim) sset interim_done_for "\"$ed\"" ;;
          qprep) sset qprep_done true ;;
          repair) sset repair_week "\"$(date '+%G-W%V')\"" ;;
        esac
        sset wait_until null
        [ "$KIND" = ok ] || inbox_add "Waiting for the user" "$(date '+%d.%m.%Y') autopilot $action did not complete ($KIND): see data/autopilot/runs/$(basename "$OUT")"
      fi
      sset last_result "\"$(date '+%Y-%m-%d %H:%M') $action $KIND $RESULT\"" ;;
    skip-repair) sset repair_week "\"$(date '+%G-W%V')\""; log "repair: $reason" ;;
    *) case "$reason" in model\ mismatch*|publication*) [ "$(sget last_notice)" != "$reason" ] && { notify "$reason"; sset last_notice "\"$reason\""; } ;; esac ;;
  esac
  status_json
  metrics
  if $AP heartbeat; then
    git add docs/data/autopilot.json && git commit -q -m "autopilot: heartbeat" -- docs/data/autopilot.json >/dev/null 2>&1 && log "heartbeat committed"
  fi
  publish
}

write_plists() {
  mkdir -p "$(dirname "$PLIST")" "$ROOT/data/harvest/logs"
  cat > "$HPLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$HLABEL</string>
  <key>ProgramArguments</key><array><string>/usr/bin/caffeinate</string><string>-i</string><string>-s</string><string>$(command -v "$PY")</string><string>-m</string><string>tools.harvester</string><string>watch</string></array>
  <key>WorkingDirectory</key><string>$ROOT</string>
  <key>KeepAlive</key><true/>
  <key>RunAtLoad</key><true/>
  <key>ThrottleInterval</key><integer>60</integer>
  <key>StandardOutPath</key><string>$ROOT/data/harvest/logs/console.log</string>
  <key>StandardErrorPath</key><string>$ROOT/data/harvest/logs/console.log</string>
  <key>EnvironmentVariables</key><dict><key>HOME</key><string>$HOME</string><key>LANG</key><string>en_US.UTF-8</string></dict>
</dict></plist>
EOF
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
}

install() {
  [ "$(uname)" = Darwin ] || { echo "install is for macOS (launchd). Elsewhere run the harvester under systemd and 'scripts/autopilot.sh tick' hourly from cron."; exit 1; }
  write_plists
  # hand the harvester over to launchd: stop a copy started by hand (state is kept), then load the job
  if ! launchctl print "gui/$(id -u)/$HLABEL" >/dev/null 2>&1; then
    "$PY" -m tools.harvester status 2>/dev/null | grep -q 'LIVENESS: running' && "$PY" -m tools.harvester stop --wait >/dev/null 2>&1
  fi
  launchctl bootout "gui/$(id -u)/$HLABEL" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$HPLIST" && echo "Installed $HLABEL (harvester kept alive by launchd)."
  launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$PLIST" && echo "Installed $LABEL (hourly; first tick running now). Log: scripts/autopilot.sh tail"
}

case "${1:-status}" in
  tick) tick ;;
  install) install ;;
  uninstall)
    for l in "$LABEL" "$HLABEL"; do launchctl bootout "gui/$(id -u)/$l" 2>/dev/null; done
    rm -f "$PLIST" "$HPLIST"; echo "Removed $LABEL and $HLABEL (the harvester has stopped)." ;;
  pause) touch "$DATA/PAUSED"; echo "Paused (ticks exit at once; the harvester keeps running). Undo: scripts/autopilot.sh resume" ;;
  resume) rm -f "$DATA/PAUSED"; echo "Resumed." ;;
  backup) BACKUP_DIR=${2:-$BACKUP_DIR}; [ -n "$BACKUP_DIR" ] || { echo "Set BACKUP_DIR in autopilot.conf or pass a folder."; exit 1; }; backup ;;
  tail) tail -n 40 -f "$LOG" ;;
  status)
    status_json; echo "Next action: $($AP decide)"
    echo "Model: $MODEL · permission mode: $PERMISSION_MODE"
    [ -f "$DATA/PAUSED" ] && echo "PAUSED"
    [ -d "$LOCK" ] && echo "Running now: pid $(cat "$LOCK/pid" 2>/dev/null)"
    for l in "$LABEL" "$HLABEL"; do
      launchctl print "gui/$(id -u)/$l" >/dev/null 2>&1 && echo "launchd job $l: installed" || echo "launchd job $l: NOT installed (scripts/autopilot.sh install)"
    done
    echo "--- last log lines"; tail -n 8 "$LOG" 2>/dev/null
    [ -f AUTOPILOT_INBOX.md ] && { echo "--- AUTOPILOT_INBOX.md"; cat AUTOPILOT_INBOX.md; } ;;
  *) sed -n '2,19p' "$0"; exit 1 ;;
esac
