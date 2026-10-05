---
description: Where am I? Pipeline state, harvester state, and what to type next
---
Run `python3 tools/pipeline.py status` and explain the result to the user in at most 6 plain lines: is the harvester running (if not, offer `scripts/harvest.sh start`), which edition exists and whether it is finished, and what to type next — normally just `/edition` (on or after the date the status gives). Do not start anything yourself.
