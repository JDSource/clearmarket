"""
Non-destructive D1 push of events.catalyst_dates — generates SQL only (run via wrangler).

Clears catalyst_dates on all events, then sets the prior-mover set from the bundle. No drop/reseed
of events/markets — touches only the catalyst_dates column. Same mechanism the daily cron will use.

Usage: python3 push_catalysts.py  →  writes api/catalysts-update.sql
       (cd api && npx wrangler d1 execute clearmarket --remote --file=catalysts-update.sql)
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
bundle = json.loads((ROOT / "web/data/universe-enriched-linked.json").read_text())

def esc(s):
    return str(s).replace("'", "''")

lines = ["UPDATE events SET catalyst_dates='[]';"]  # clear stale catalysts first
n = 0
for e in bundle["events"]:
    cds = e.get("catalyst_dates") or []
    if cds:
        n += 1
        lines.append(f"UPDATE events SET catalyst_dates='{esc(json.dumps(cds))}' WHERE event_id='{esc(e['event_id'])}';")

out = ROOT / "api/catalysts-update.sql"
out.write_text("\n".join(lines) + "\n")
print(f"wrote {out} — clear-all + {n} events with prior-mover catalysts")
