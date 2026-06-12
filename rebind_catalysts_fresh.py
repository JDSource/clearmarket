#!/usr/bin/env python3
"""Surgical catalyst rebind for a fresh universe.

migrate_catalysts_to_types.py is a one-time migration that ALSO reshapes the
calendar (flat -> keyed). The calendar is already keyed, so we must NOT re-run
that. This script only re-binds events[].catalyst_types via catalyst_bind.bind_types
(the same logic), reading earnings dates from the preserved flat backup. Calendar
is left untouched.
"""
import json
from collections import defaultdict
import migrate_catalysts_to_types as M  # imports cb, parse_d, BUNDLE, ROOT (defs only)

cb, parse_d, ROOT, BUNDLE = M.cb, M.parse_d, M.ROOT, M.BUNDLE

flat = json.loads((ROOT / "data/catalyst-calendar.flat.bak.json").read_text())
earnings_flat = flat.get("earnings") or {}
def earnings_dates_fn(tk): return earnings_flat.get(tk, [])

bundle = json.loads(BUNDLE.read_text())
by_ev = defaultdict(list)
for m in bundle["markets"]:
    by_ev[m.get("event_id")].append(m)

n_typed, tickers = 0, set()
for ev in bundle["events"]:
    mkts = by_ev.get(ev["event_id"], [])
    resolve_at = max((d for d in (parse_d(m.get("close_at")) for m in mkts) if d), default=None)
    types = cb.bind_types(ev.get("question"), ev.get("tags"), resolve_at, earnings_dates_fn)
    ev["catalyst_types"] = types
    ev["catalyst_dates"] = []  # recurring derived at read-time; bespoke (Exa) deferred
    if types:
        n_typed += 1
        for t in types:
            if t.startswith("earnings:"):
                tickers.add(t.split(":", 1)[1])

(ROOT / "data/catalyst-tickers.json").write_text(json.dumps(sorted(tickers), indent=2))
BUNDLE.write_text(json.dumps(bundle, default=str))
print(f"events with catalyst_types: {n_typed} / {len(bundle['events'])}")
print(f"earnings tickers bound: {len(tickers)} -> {sorted(tickers)[:10]}")
