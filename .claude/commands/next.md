---
description: Where am I? Shows the pipeline state, the harvester state and the exact next command
---
Run `python3 tools/pipeline.py status` and `python3 -m tools.harvester status`. Explain the result in at most 8 lines: which edition and stage we are in, whether the harvester is running (if not, offer to restart it with `scripts/harvest.sh start`), and the exact next command to type, including whether it needs a new session (/clear first). Do not start the next stage yourself.
