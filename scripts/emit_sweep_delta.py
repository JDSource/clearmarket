#!/usr/bin/env python3
"""
emit_sweep_delta.py — publish what the daily sweep changed, so the Worker can apply it to D1.

sweep_past_due.py fixes statuses in the R2 bundle the website renders from; until 2026-09-17 the API
database (D1) only learned about those fixes at the monthly reload. This script diffs the pre-sweep
and post-sweep bundle and writes a small JSON file of open->terminal transitions; the Worker fetches
it from R2 at 09:00 UTC (applySweep) and applies it idempotently to still-open rows.

Usage: emit_sweep_delta.py PRE_BUNDLE POST_BUNDLE OUT_JSON               (diff mode — one day's transitions only)
       emit_sweep_delta.py --terminal-open OPEN_IDS_JSON POST_BUNDLE OUT_JSON  (bundle-terminal ∩ a given open-id list)
       emit_sweep_delta.py --from-api POST_BUNDLE OUT_JSON                     (bundle-terminal ∩ what the API still
         serves as open/closed, pulled live from /v1/marks — SELF-HEALING: a day the Worker misses is covered the next day)
"""
import urllib.parse
import urllib.request

API = "https://api.clearmarket.fyi/v1/marks"
UA = "clearmarket-sweep/0.1 (+https://clearmarket.fyi)"


def api_status_by_id():
    """market_id -> status for every market the API serves as open or closed."""
    out = {}
    for status in ("open", "closed"):
        cursor = None
        while True:
            q = {"status": status, "limit": "1000"}
            if cursor:
                q["cursor"] = cursor
            req = urllib.request.Request(f"{API}?{urllib.parse.urlencode(q)}", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.load(r)
            for m in d.get("marks", []):
                out[m["market_id"]] = m["status"]
            cursor = d.get("next_cursor")
            if not cursor:
                break
    return out
import json
import sys
from datetime import datetime, timezone

FIELDS = ("market_id", "event_id", "platform", "status", "last_price", "settled_at", "close_at", "resolve_at")
TERMINAL = ("resolved", "closed")


def rec(m):
    return {k: m.get(k) for k in FIELDS}


def main(argv):
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    if argv[0] == "--from-api":
        api = api_status_by_id()
        post = json.load(open(argv[1]))
        # A transition is worth publishing when the bundle says resolved and the API still says open/closed, or the
        # bundle says closed and the API still says open. closed->closed is not a change.
        changes = [rec(m) for m in post["markets"]
                   if m.get("market_id") in api and (
                       m.get("status") == "resolved" or (m.get("status") == "closed" and api[m["market_id"]] == "open"))]
        mode = "from-api"
        out_path = argv[2]
        print(f"api reports {len(api)} open/closed markets")
    elif argv[0] == "--terminal-open":
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
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
