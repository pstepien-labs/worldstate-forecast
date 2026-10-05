"""Local harvester for the Calibrated Balance-of-Power Forecast.

Collects news feeds, official pages, public Telegram previews, GDELT article
lists and primary numeric datasets into a local, resumable corpus
(`data/harvest/`), then builds an edition digest for stage 02.

Python standard library only. Entry point: `python3 -m tools.harvester --help`.
"""
HARVESTER_VERSION = '1.3.0'
