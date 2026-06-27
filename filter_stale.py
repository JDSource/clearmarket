#!/usr/bin/env python3
"""Pre-share data filter: drop stale / past / impossible / out-of-horizon events
from the served bundle. Dry-run by default (reports only); pass --write to apply.

Drop rules (today = 2026-06-03):
  (a) event's latest market resolve/close date is in the PAST (resolved/expired)
  (b) event resolves > 24 months out (> 2028-06-03)
  (c) question text references a clearly-past year (2023 or 2024) as its subject
      — catches mis-dated specimens like "Llama 5 by Dec 31, 2024" that resolve 2027
"""
import json, re, sys
from datetime import date, datetime
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
TODAY = date.today()
HORIZON = date(TODAY.year + 2, TODAY.month, TODAY.day) if (TODAY.month, TODAY.day) != (2, 29) \
    else date(TODAY.year + 2, 3, 1)  # today + 24 months (leap-day guard)
WRITE = "--write" in sys.argv

def parse_d(s):
    if not s: return None
    try: return datetime.fromisoformat(str(s).replace("Z", "+00:00")).date()
    except Exception: return None

bundle = json.loads(BUNDLE.read_text())
by_ev = defaultdict(list)
for m in bundle["markets"]:
    by_ev[m.get("event_id")].append(m)

PAST_YEAR = re.compile(r"\b(2023|2024)\b")
drop_ids, reasons = set(), defaultdict(list)
for ev in bundle["events"]:
    eid = ev["event_id"]
    mkts = by_ev.get(eid, [])
    dates = [d for d in (parse_d(m.get("resolve_at") or m.get("close_at")) for m in mkts) if d]
    resolve = max(dates) if dates else None
    q = ev.get("question") or ""
    reason = None
    if resolve and resolve < TODAY:
        reason = "past_resolve"
    elif resolve and resolve > HORIZON:
        reason = "beyond_24mo"
    elif PAST_YEAR.search(q) and (resolve is None or resolve.year >= 2027):
        # glaring mis-date: question's subject year is 2023/2024 but it "resolves" 2027+
        reason = "misdated_past_year"
    if reason:
        drop_ids.add(eid)
        reasons[reason].append((ev.get("slug"), q[:64], str(resolve)))

total_ev = len(bundle["events"])
print(f"events: {total_ev} | would drop: {len(drop_ids)} | keep: {total_ev - len(drop_ids)}")
for r, items in reasons.items():
    print(f"\n--- {r}: {len(items)} ---")
    for slug, q, res in items[:12]:
        print(f"   [{res}] {slug}: {q!r}")
    if len(items) > 12: print(f"   ... +{len(items)-12} more")

if WRITE:
    keep_ev = [e for e in bundle["events"] if e["event_id"] not in drop_ids]
    keep_mk = [m for m in bundle["markets"] if m.get("event_id") not in drop_ids]
    bundle["events"] = keep_ev
    bundle["markets"] = keep_mk
    BUNDLE.write_text(json.dumps(bundle, default=str))
    print(f"\nWROTE filtered bundle: {len(keep_ev)} events / {len(keep_mk)} markets")
else:
    print("\n(dry run — pass --write to apply)")
