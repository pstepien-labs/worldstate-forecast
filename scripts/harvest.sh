#!/usr/bin/env bash
# Harvester launcher for macOS / Linux (on Windows use WSL, or run
# `python -m tools.harvester watch` in a terminal that stays open).
#
#   scripts/harvest.sh start    start (or resume) continuous harvesting in the background
#   scripts/harvest.sh stop     stop after the current source (state is kept; start resumes)
#   scripts/harvest.sh status   progress, source health, errors, liveness
#   scripts/harvest.sh tail     follow the live event log (Ctrl+C to leave; harvesting continues)
#   scripts/harvest.sh check    fetch every source once now and write data/harvest/CHECK.md
#   scripts/harvest.sh digest   build the edition digest into editions/<DIR>/02_harvest/
#   scripts/harvest.sh doctor   environment check
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
DATA="${HARVEST_DATA:-data/harvest}"
mkdir -p "$DATA/logs"

running_pid() {
  local lock="$DATA/state/harvester.lock"
  [ -f "$lock" ] || return 1
  local pid
  pid=$("$PY" -c "import json,sys; print(json.load(open(sys.argv[1]))['pid'])" "$lock" 2>/dev/null) || return 1
  kill -0 "$pid" 2>/dev/null && echo "$pid"
}

case "${1:-status}" in
  start)
    if pid=$(running_pid); then
      echo "Harvester already running (pid $pid)."; "$PY" -m tools.harvester status | tail -3; exit 0
    fi
    "$PY" -m tools.harvester doctor || { echo "Fix the problems above first."; exit 1; }
    # Keep a laptop awake while harvesting (macOS: caffeinate; Linux: systemd-inhibit if available).
    WRAP=()
    if command -v caffeinate >/dev/null 2>&1; then WRAP=(caffeinate -i -s)
    elif command -v systemd-inhibit >/dev/null 2>&1 && systemd-inhibit --what=idle:sleep --why=test true >/dev/null 2>&1; then
      WRAP=(systemd-inhibit --what=idle:sleep --why=harvester)
    fi
    nohup ${WRAP[@]+"${WRAP[@]}"} "$PY" -m tools.harvester watch >> "$DATA/logs/console.log" 2>&1 &
    sleep 3
    if pid=$(running_pid); then
      echo "Harvester started (pid $pid). Progress: scripts/harvest.sh status · live log: scripts/harvest.sh tail"
    else
      echo "Harvester did not start; last lines of $DATA/logs/console.log:"; tail -20 "$DATA/logs/console.log"; exit 1
    fi
    ;;
  stop)   "$PY" -m tools.harvester stop --wait ;;
  status) "$PY" -m tools.harvester status ;;
  tail)   tail -n 30 -f "$DATA/logs/console.log" ;;
  check)  "$PY" -m tools.harvester check "${@:2}" ;;
  digest) "$PY" -m tools.harvester digest "${@:2}" ;;
  doctor) "$PY" -m tools.harvester doctor ;;
  *) sed -n '2,12p' "$0"; exit 1 ;;
esac
