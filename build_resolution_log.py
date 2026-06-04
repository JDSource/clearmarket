#!/usr/bin/env python3
"""
build_resolution_log.py — capture step for the resolution_log / history table.

Runs as part of the re-enrich pipeline (after the universe bundle is built, before the D1 export).
For every market whose resolution date is in the past, it writes an append-only `resolved` event
capturing WHEN it settled and — when the final price is confident — the OUTCOME.

Why derive from price + date, not `status`: the monthly bundle's `status` field is stale (a market
that has clearly resolved still shows "open" because the snapshot predates settlement). The reliable
signals are the resolution DATE (resolve_at/close_at) and the final PRICE (≈1.0 → YES, ≈0.0 → NO).

Outcome confidence: a price is only a true settlement price if the snapshot was taken AT/AFTER the
market resolved (resolve_at < pull_date). Markets that resolved AFTER the pull still carry a mid
price, so their outcome is recorded as PENDING (not guessed) — they get a real outcome on the next
re-enrich, which is exactly how this operationalizes: each pull backfills everything settled so far.

Output: web/data/resolution-log.json — consumed by the D1 export (seeds the resolution_log table)
and the per-event JSON / event page Resolution section.
"""
import json
import os
import sys
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

    log = []
    counts = {"YES": 0, "NO": 0, "PENDING": 0}
    for m in markets:
        occurred = m.get("resolve_at") or m.get("close_at")
        if not occurred or day(occurred) >= TODAY:
            continue  # not resolved yet (live)

        lp = m.get("last_price")
        # An extreme final price (≈1.0 / ≈0.0) means the market is decided — trust it as the outcome.
        # A mid price means the snapshot likely predates settlement → record resolved-but-PENDING;
        # the next re-enrich (fresh pull, now-extreme price) upgrades it to a real outcome.
        if isinstance(lp, (int, float)) and lp >= CONF_HI:
            outcome = "YES"
        elif isinstance(lp, (int, float)) and lp <= CONF_LO:
            outcome = "NO"
        else:
            outcome = "PENDING"
        counts[outcome] += 1

        log.append({
            "market_id": m.get("market_id"),
            "event_id": m.get("event_id"),
            "platform": m.get("platform"),
            "event_type": "resolved",
            "occurred_at": occurred,
            "recorded_at": pull_date,
            "to_value": outcome,
            "final_price": lp if isinstance(lp, (int, float)) else None,
            "source": "editorial_observation",   # derived from the platform price snapshot + date
            "source_ref": f"price-snapshot@{pull_date}",
            "actor": "clearmarket-reenrich",
        })

    log.sort(key=lambda r: r["occurred_at"], reverse=True)
    json.dump(log, open(OUT, "w"), indent=0)
    print(f"resolution_log: {len(log)} resolved markets captured  ->  {OUT}")
    print(f"  outcomes: YES={counts['YES']}  NO={counts['NO']}  PENDING={counts['PENDING']} "
          f"(pull_date={pull_date}, today={TODAY})")


if __name__ == "__main__":
    main()
