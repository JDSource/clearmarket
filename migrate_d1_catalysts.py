"""
Non-destructive D1 migration for the catalyst re-architecture (2026-05-29).

Emits api/catalyst-migration.sql — does NOT touch events/markets rows beyond the catalyst columns:
  - clears events.catalyst_dates ('[]')        (recurring catalysts now derived at read-time)
  - sets events.catalyst_types per typed event (the binding pointers)
  - (re)builds the catalyst_calendar table from the reshaped data/catalyst-calendar.json

The ALTER TABLE events ADD COLUMN catalyst_types is run SEPARATELY (one-time; D1 has no
IF NOT EXISTS for ADD COLUMN). See the push step. catalyst_calendar uses DROP/CREATE so this
file is safely re-runnable.

Usage: python3 migrate_d1_catalysts.py  ->  api/catalyst-migration.sql
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
bundle = json.loads((ROOT / "web/data/universe-enriched-linked.json").read_text())
cal = json.loads((ROOT / "data/catalyst-calendar.json").read_text())

def esc(s):
    return str(s).replace("'", "''")

lines = []

# 1. clear all recurring catalyst_dates (bespoke Exa entries would be re-added by their own job)
lines.append("UPDATE events SET catalyst_dates='[]';")

# 2. set catalyst_types for events that have any
n_typed = 0
for e in bundle["events"]:
    types = e.get("catalyst_types") or []
    if types:
        n_typed += 1
        lines.append(f"UPDATE events SET catalyst_types='{esc(json.dumps(types))}' WHERE event_id='{esc(e['event_id'])}';")

# 3. rebuild the shared calendar table
lines.append("DROP TABLE IF EXISTS catalyst_calendar;")
lines.append("CREATE TABLE catalyst_calendar (type TEXT PRIMARY KEY, label TEXT NOT NULL, "
             "source_url TEXT NOT NULL, dates TEXT NOT NULL);")
n_cal = 0
for ty, c in (cal.get("types") or {}).items():
    n_cal += 1
    lines.append(
        "INSERT INTO catalyst_calendar (type,label,source_url,dates) VALUES "
        f"('{esc(ty)}','{esc(c['label'])}','{esc(c['source_url'])}','{esc(json.dumps(c['dates']))}');"
    )

out = ROOT / "api/catalyst-migration.sql"
out.write_text("\n".join(lines) + "\n")
print(f"wrote {out}")
print(f"  clear catalyst_dates + {n_typed} events typed + catalyst_calendar rebuilt ({n_cal} types)")
print("  NB: run `ALTER TABLE events ADD COLUMN catalyst_types TEXT;` ONCE before this file.")
