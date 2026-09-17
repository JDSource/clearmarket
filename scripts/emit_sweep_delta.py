#!/usr/bin/env python3
"""
emit_sweep_delta.py — publish what the daily sweep changed, so the Worker can apply it to D1.

sweep_past_due.py fixes statuses in the R2 bundle the website renders from; until 2026-09-17 the API
database (D1) only learned about those fixes at the monthly reload. This script diffs the pre-sweep
and post-sweep bundle and writes a small JSON file of open->terminal transitions; the Worker fetches
it from R2 at 09:00 UTC (applySweep) and applies it idempotently to still-open rows.

Usage: emit_sweep_delta.py PRE_BUNDLE POST_BUNDLE OUT_JSON
       emit_sweep_delta.py --terminal-open OPEN_IDS_JSON POST_BUNDLE OUT_JSON   (one-off backfill:
         every bundle-terminal market whose id appears in OPEN_IDS_JSON, a list of market_ids D1 says are open)
"""
import json
import sys
from datetime import datetime, timezone

FIELDS = ("market_id", "event_id", "platform", "status", "last_price", "settled_at", "close_at", "resolve_at")
TERMINAL = ("resolved", "closed")


def rec(m):
    return {k: m.get(k) for k in FIELDS}


def main(argv):
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    if argv[0] == "--terminal-open":
        open_ids = set(json.load(open(argv[1])))
        post = json.load(open(argv[2]))
        changes = [rec(m) for m in post["markets"] if m.get("status") in TERMINAL and m.get("market_id") in open_ids]
        mode = "backfill"
        out_path = argv[3]
    else:
        pre = json.load(open(argv[0]))
        post = json.load(open(argv[1]))
        before = {m["market_id"]: m.get("status") for m in pre["markets"]}
        changes = [rec(m) for m in post["markets"]
                   if m.get("status") in TERMINAL and before.get(m.get("market_id")) == "open"]
        mode = "daily"
        out_path = argv[2]
    out = {"generated_at": now, "mode": mode, "bundle_generated_at": (post.get("_meta") or {}).get("generated_at"),
           "count": len(changes), "changes": changes}
    with open(out_path, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"sweep delta ({mode}): {len(changes)} open->terminal changes -> {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
