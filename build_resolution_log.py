#!/usr/bin/env python3
"""
build_resolution_log.py — capture step for the resolution_log / history table.

Runs in the re-enrich pipeline AFTER settle_status_sweep.py (which sets venue-authoritative
`status`) and before the D1 export. HARD ORDERING DEPENDENCY: the sweep must run first, or terminal
markets still read status='open' here and get no history row.

Status-driven (not price+date). For every market the sweep marked terminal it writes an append-only
row capturing the transition out of 'open':
  - status='resolved' -> event_type 'resolved',      to_value = YES/NO (from the settlement price) or
                         PENDING when the price isn't extreme; final_price = last_price.
  - status='closed'   -> event_type 'status_change',  to_value = 'closed' (no determinable outcome).

Provenance: rows derived from venue-confirmed status are source='platform_api'. (Pre-rewrite this file
inferred resolution from price+date and tagged everything 'editorial_observation'; that heuristic is
gone — the sweep is now the authority.)

Honest detection-lag: merges with the prior resolution-log.json. recorded_at is preserved for rows we
have already seen and only stamped (= pull_date) on genuinely new rows, so occurred_at -> recorded_at
stays a true first-observation lag across monthly runs instead of being re-stamped every rebuild.

Output: web/data/resolution-log.json — consumed by the D1 export (seeds resolution_log) and the
per-event JSON / event-page Resolution section.
"""
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.join(ROOT, "web/data/universe-enriched-linked.json")
OUT = os.path.join(ROOT, "web/data/resolution-log.json")

TODAY = date.today().isoformat()
CONF_HI, CONF_LO = 0.95, 0.05


def day(s):
    return (s or "")[:10]


def main():
    bundle = json.load(open(BUNDLE))
    pull_date = day(bundle.get("_meta", {}).get("generated_at")) or TODAY
    markets = bundle["markets"]

    # Prior log -> carry forward recorded_at (first-observation), keyed by (market_id, occurred_at).
    # Fallback keyed by market_id alone: occurred_at moved from deadline to venue settlement time
    # (settled_at, 2026-07-23), so exact keys break once per market — without the fallback every
    # row would re-stamp recorded_at and destroy the detection-lag history.
    prior = {}
    prior_by_mid = {}  # keyed (market_id, event_type): a closed->resolved transition is a NEW
    # observation and must not inherit the closed row's earlier recorded_at (that would print
    # a negative detection lag: recorded before the settlement occurred).
    if os.path.exists(OUT):
        try:
            for r in json.load(open(OUT)):
                prior[(r.get("market_id"), day(r.get("occurred_at")))] = r.get("recorded_at")
                k2 = (r.get("market_id"), r.get("event_type"))
                ra = r.get("recorded_at")
                if r.get("market_id") and ra and (k2 not in prior_by_mid or ra < prior_by_mid[k2]):
                    prior_by_mid[k2] = ra
        except (ValueError, OSError):
            pass

    log = []
    counts = {"YES": 0, "NO": 0, "PENDING": 0, "closed": 0}
    open_past = 0  # safety counter: terminal-by-date but still status='open' (did the sweep run?)

    for m in markets:
        status = (m.get("status") or "").lower()
        # Venue settlement time is the truth; the deadline is only a fallback (and is
        # labeled as such via occurred_basis so no surface prints a deadline as a settlement).
        settled = m.get("settled_at")
        deadline = m.get("resolve_at") or m.get("close_at")
        occurred = settled or deadline or pull_date
        basis = ("venue_settlement" if settled
                 else "deadline" if deadline
                 else "first_observed")
        lp = m.get("last_price")

        if status == "resolved":
            if isinstance(lp, (int, float)) and lp >= CONF_HI:
                outcome = "YES"
            elif isinstance(lp, (int, float)) and lp <= CONF_LO:
                outcome = "NO"
            else:
                outcome = "PENDING"
            counts[outcome] += 1
            event_type, to_value = "resolved", outcome
            final_price = lp if isinstance(lp, (int, float)) else None
        elif status == "closed":
            counts["closed"] += 1
            event_type, to_value = "status_change", "closed"
            final_price = None
        else:
            # still 'open' (or amended/unknown). Flag the case the old price+date heuristic used to catch.
            if status == "open" and occurred and day(occurred) < TODAY:
                open_past += 1
            continue

        key = (m.get("market_id"), day(occurred))
        log.append({
            "market_id": m.get("market_id"),
            "event_id": m.get("event_id"),
            "platform": m.get("platform"),
            "event_type": event_type,
            "occurred_at": occurred,
            "occurred_basis": basis,
            "recorded_at": prior.get(key) or prior_by_mid.get((m.get("market_id"), event_type)) or pull_date,
            "from_value": "open",
            "to_value": to_value,
            "final_price": final_price,
            "source": "platform_api",
            "source_ref": None,
            "actor": "clearmarket-reenrich",
        })

    log.sort(key=lambda r: r["occurred_at"], reverse=True)
    json.dump(log, open(OUT, "w"), indent=0)
    print(f"resolution_log: {len(log)} terminal markets captured  ->  {OUT}")
    print(f"  outcomes: YES={counts['YES']}  NO={counts['NO']}  PENDING={counts['PENDING']}  "
          f"closed={counts['closed']} (pull_date={pull_date}, today={TODAY})")
    if open_past:
        print(f"  WARNING: {open_past} markets are status='open' but past their resolve date — "
              f"did settle_status_sweep.py run before this? Those get NO history row.")


if __name__ == "__main__":
    main()
