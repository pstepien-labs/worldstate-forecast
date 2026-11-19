#!/usr/bin/env bash
# One-time Mac settings for unattended running (framework 1.9.2). Needs your administrator password once.
#   sudo scripts/owner_setup.sh                 restart after a power cut; no automatic macOS update installs
#   sudo scripts/owner_setup.sh --backup DIR    also set BACKUP_DIR in autopilot.conf (an external or synced folder)
# Undo: sudo pmset -a autorestart 0; sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates -bool true
set -euo pipefail
cd "$(dirname "$0")/.."
[ "$(uname)" = Darwin ] || { echo "macOS only"; exit 1; }
[ "$(id -u)" = 0 ] || { echo "Run with sudo: sudo scripts/owner_setup.sh"; exit 1; }
pmset -a autorestart 1
# FileVault waits for a password after any restart; updates that restart the Mac would stop the autopilot until you are back.
defaults write /Library/Preferences/com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates -bool false
if [ "${1:-}" = --backup ] && [ -n "${2:-}" ]; then
  [ -d "$2" ] || { echo "Backup folder $2 does not exist"; exit 1; }
  owner=$(stat -f %Su .)
  sed -i '' "s|^BACKUP_DIR=.*|BACKUP_DIR=$2|" autopilot.conf
  chown "$owner" autopilot.conf
  echo "BACKUP_DIR=$2 (written to autopilot.conf; commit it or leave it local)"
fi
echo "--- check"
pmset -g | grep -E ' autorestart'
echo "AutomaticallyInstallMacOSUpdates = $(defaults read /Library/Preferences/com.apple.SoftwareUpdate AutomaticallyInstallMacOSUpdates)"
echo "Done. Security responses may still install; macOS updates now wait for you."
