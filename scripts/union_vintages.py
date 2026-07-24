#!/usr/bin/env python3
"""
union_vintages.py — merge a fresh re-enrichment vintage with the live bundle's history.

Why: a fresh venue pull only serves active/recent events. Long-settled events fall out
of the pull, but locked decision #4 says resolved events STAY (reference product =
history; permalinks persist), and the resolution_log / dispute backtest need the
settled population. Replacement deletes history; union preserves it.

Rules (deterministic IDs make this safe — same venue-native id == same CM id):
  - events:  fresh wins on event_id overlap; live-only events appended (settled history).
  - markets: fresh wins on market_id overlap; live-only markets appended when their
             event survives in the union (it always does, by construction).
  - resolution log: union by market_id; the NEW log wins unless its outcome is PENDING
             and the old row carries a final outcome (never downgrade a settled row).

After this script: re-run regrade_rcg.py (one grading vintage across both populations)
then patch_sources.py --write (grade_market does NOT apply source-commitment caps —
patch_sources rebuilds them; it is idempotent), then build_resolution_log.py + export.

Usage:
  python3 scripts/union_vintages.py --fresh web/data/universe-enriched-linked.json \
      --live /tmp/live-r2-bundle.json \
      --fresh-log web/data/resolution-log.json --live-log /tmp/live-r2-resolution-log.json
  (writes the union back to --fresh and --fresh-log; prints a report)
"""
import argparse
import json
from pathlib import Path


def load(p):
    return json.loads(Path(p).read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresh", required=True)
    ap.add_argument("--live", required=True)
    ap.add_argument("--fresh-log", required=True)
    ap.add_argument("--live-log", required=True)
    args = ap.parse_args()

    fresh, live = load(args.fresh), load(args.live)

    # settled_at is written only by the sweeps/backfill, never by fetch/enrich — so a fresh
    # record for an already-settled market arrives WITHOUT it. "Fresh wins" must not wipe the
    # venue settlement timestamp or resolution dates regress to deadlines on every re-enrich.
    live_settled = {m["market_id"]: m["settled_at"]
                    for m in live["markets"] if m.get("settled_at")}
    restored = 0
    for m in fresh["markets"]:
        if not m.get("settled_at") and m["market_id"] in live_settled:
            m["settled_at"] = live_settled[m["market_id"]]
            restored += 1

    fe = {e["event_id"] for e in fresh["events"]}
    live_only_events = [e for e in live["events"] if e["event_id"] not in fe]
    fresh["events"] += live_only_events

    fm = {m["market_id"] for m in fresh["markets"]}
    union_events = fe | {e["event_id"] for e in live_only_events} \
        | {e["event_id"] for e in live["events"]}
    live_only_markets = [m for m in live["markets"]
                         if m["market_id"] not in fm and m.get("event_id") in union_events]
    fresh["markets"] += live_only_markets

    meta = fresh.setdefault("_meta", {})
    meta["vintage_union"] = {
        "live_only_events": len(live_only_events),
        "live_only_markets": len(live_only_markets),
        "settled_at_restored": restored,
    }
    Path(args.fresh).write_text(json.dumps(fresh, ensure_ascii=False, separators=(",", ":")))
    print(f"events: +{len(live_only_events)} live-only -> {len(fresh['events'])}")
    print(f"markets: +{len(live_only_markets)} live-only -> {len(fresh['markets'])}")

    def rows(log):
        return log if isinstance(log, list) else log.get("log") or log.get("rows") or []

    new_rows = {r["market_id"]: r for r in rows(load(args.fresh_log))}
    merged, kept_old, updated = [], 0, 0
    for r in rows(load(args.live_log)):
        n = new_rows.pop(r["market_id"], None)
        if n is None:
            merged.append(r); kept_old += 1
        elif n.get("to_value") == "PENDING" and r.get("to_value") not in (None, "PENDING"):
            merged.append(r); kept_old += 1
        else:
            merged.append(n); updated += 1
    merged += list(new_rows.values())
    Path(args.fresh_log).write_text(json.dumps(merged, ensure_ascii=False, indent=1))
    print(f"resolution log: {len(merged)} rows (kept {kept_old} live rows, "
          f"updated {updated}, +{len(new_rows)} new)")


if __name__ == "__main__":
    main()
