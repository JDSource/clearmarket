#!/usr/bin/env python3
"""
Filter untraded Polymarket ghost markets out of a universe bundle.

Polymarket pre-creates unnamed outcome slots inside multi-candidate (negRisk)
events before real candidates exist — "Person W", "Candidate E", "Party H (H)",
"Will A win the FL-18 House seat?", "Placeholder 2", etc. Template formats vary
too much for regex enumeration (a 2026-06-10 regex pass caught only 1,312 of
3,626). The reliable discriminator is VOLUME, per locked decision #7
(venue-specific volume threshold): ghosts have zero lifetime volume; real
markets trade. When a slot is renamed to a real candidate it starts trading and
re-enters naturally on the next ingest — so never filter by id blocklist.

RULE: drop a market iff platform == polymarket AND source volume == 0.
 - Run at ingest/merge time with gamma's own volumeNum (at-source volume has no
   capture gaps; D1-side volume can be stale/null — 2 real disputed markets
   showed $0 in D1 on 2026-06-10).
 - If NO volume field exists on the record, KEEP it (unknown != zero).
 - Kalshi is untouched (zero-volume Kalshi strikes are real listed ladders).
 - Never empty an event: if all of an event's markets would drop, keep them and
   report for human review.

Usage: python3 scripts/filter_placeholder_slots.py <bundle.json> [-o out.json]
"""
import json, sys, argparse

VOLUME_KEYS = ("volumeNum", "volume_total_usd", "volume")

def market_volume(m):
    for k in VOLUME_KEYS:
        if k in m and m[k] is not None:
            try: return float(m[k])
            except (TypeError, ValueError): continue
    return None  # unknown -> keep

def is_ghost(m):
    if m.get("platform") != "polymarket": return False
    vol = market_volume(m)
    return vol is not None and vol == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle"); ap.add_argument("-o", "--out", default=None)
    args = ap.parse_args()
    bundle = json.load(open(args.bundle))
    markets = bundle["markets"]
    keep = [m for m in markets if not is_ghost(m)]
    drop = [m for m in markets if is_ghost(m)]
    surviving_events = {m["event_id"] for m in keep}
    protected = [m for m in drop if m["event_id"] not in surviving_events]
    if protected:
        pids = {m["market_id"] for m in protected}
        keep += protected
        drop = [m for m in drop if m["market_id"] not in pids]
        print(f"KEPT {len(protected)} ghosts to avoid emptying events — review these events:")
        for m in protected[:10]: print("  ", m["event_id"], (m.get("question_raw") or "")[:60])
    bundle["markets"] = keep
    json.dump(bundle, open(args.out or args.bundle, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"markets: {len(markets)} -> {len(keep)} (removed {len(drop)} untraded polymarket ghosts)")

if __name__ == "__main__":
    main()
