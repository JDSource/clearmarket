"""
Non-destructive D1 migration for the ladder data fix (2026-05-29). Reads the patched bundle
(run patch_ladders.py first) and emits api/ladders-migration.sql: sets every event's event_type,
and for the 142 LADDER events writes ladder_distribution + the clean question + the corrected
primary_market_id. Touches only the events table (no markets/catalyst/marks reseed).

The two ALTER TABLE ADD COLUMN statements run ONCE separately (D1 has no IF NOT EXISTS for ADD COLUMN).
Usage: python3 migrate_d1_ladders.py  ->  api/ladders-migration.sql
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
b = json.loads((ROOT / "web/data/universe-enriched-linked.json").read_text())

def esc(s):
    return str(s).replace("'", "''")

lines = ["UPDATE events SET event_type='BINARY';"]
n = 0
for e in b["events"]:
    if e.get("event_type") == "LADDER" and e.get("ladder_distribution"):
        n += 1
        ld = esc(json.dumps(e["ladder_distribution"]))
        lines.append(
            "UPDATE events SET event_type='LADDER', "
            f"ladder_distribution='{ld}', question='{esc(e.get('question',''))}', "
            f"primary_market_id='{esc(e.get('primary_market_id') or '')}' "
            f"WHERE event_id='{esc(e['event_id'])}';"
        )

out = ROOT / "api/ladders-migration.sql"
out.write_text("\n".join(lines) + "\n")
print(f"wrote {out}: BINARY default + {n} LADDER updates")
print("NB: run ONCE first: ALTER TABLE events ADD COLUMN event_type TEXT; ALTER TABLE events ADD COLUMN ladder_distribution TEXT;")
