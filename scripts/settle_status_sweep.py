#!/usr/bin/env python3
"""
settle_status_sweep.py — reconcile carried-over markets with their venue's actual state.

Audit 2026-06-12: the vintage union carried live-only markets verbatim, so ~2,768 of
2,876 served status='open' with prices frozen at the prior vintage even though the
venue had finalized them. This sweep queries each carried market's venue and:

  - venue finalized/settled with a result  -> status 'resolved', last_price = settlement
    value (1.0 YES / 0.0 NO), resolve_at/close_at = venue close time
  - venue closed, outcome not determined   -> status 'closed' (price left as last seen)
  - venue still ACTIVE (the fresh pull dropped it on volume/category, not settlement)
    -> stays 'open', last_price refreshed from the venue
  - venue no longer serves it at all       -> close_at past => 'closed', else left alone
    (reported either way)

Target set = markets present in the -linked bundle but absent from the fresh enrichment
output (universe-enriched-full.json) — i.e. exactly the union's carried records.

Dry-run by default; --write applies to web/data/universe-enriched-linked.json.
After --write: rerun patch has no role here, but build_resolution_log.py MUST rerun
(settlement prices now true), then the log re-union, D1 export, R2 upload, deploys.
"""
import json
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
FRESH = ROOT / "web/data/universe-enriched-full.json"

KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
GAMMA = "https://gamma-api.polymarket.com/markets"
HEADERS = {"User-Agent": "clearmarket-fetcher/0.1"}
TIMEOUT = 30
WRITE = "--write" in sys.argv


def _get(url, params=None):
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, timeout=TIMEOUT, headers=HEADERS)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.json()
        except Exception:
            if attempt == 2:
                return "ERR"
            time.sleep(2 ** attempt)


def sweep_kalshi(markets, stats):
    for m in markets:
        data = _get(f"{KALSHI}/markets/{m['platform_market_id']}")
        if data == "ERR":
            stats["errors"] += 1
            continue
        if data is None:
            # venue no longer serves it — close it iff its close date has passed
            if (m.get("close_at") or "9999")[:10] < TODAY:
                m["status"] = "closed"
                stats["gone_closed"] += 1
            else:
                stats["gone_left"] += 1
            continue
        k = data.get("market") or data
        vstatus = (k.get("status") or "").lower()
        result = (k.get("result") or "").lower()
        if vstatus in ("finalized", "settled") and result in ("yes", "no"):
            m["status"] = "resolved"
            m["last_price"] = 1.0 if result == "yes" else 0.0
            ct = k.get("close_time") or k.get("expiration_time")
            if ct:
                m["close_at"] = ct
                m["resolve_at"] = ct
            stats["resolved"] += 1
        elif vstatus in ("finalized", "settled", "closed"):
            m["status"] = "closed"
            stats["closed"] += 1
        else:  # active — fresh pull dropped it on volume/category, keep it live
            lp = k.get("last_price")
            if lp is not None:
                m["last_price"] = lp / 100.0
            stats["still_active"] += 1
        time.sleep(0.08)


def sweep_poly(markets, stats):
    by_cid = {m["platform_market_id"]: m for m in markets if m.get("platform_market_id")}
    cids = sorted(by_cid)
    for i in range(0, len(cids), 50):
        batch = cids[i:i + 50]
        rows = []
        for closed in (None, "true"):
            params = [("condition_ids", c) for c in batch] + [("limit", "100")]
            if closed:
                got = {r.get("conditionId") for r in rows}
                missing = [c for c in batch if c not in got]
                if not missing:
                    break
                params = [("condition_ids", c) for c in missing] + [("limit", "100"), ("closed", "true")]
            res = _get(GAMMA, params)
            if res in (None, "ERR"):
                stats["errors"] += 1
                continue
            rows += res
        seen = set()
        for row in rows:
            cid = row.get("conditionId")
            m = by_cid.get(cid)
            if not m or cid in seen:
                continue
            seen.add(cid)
            if row.get("closed"):
                final = (row.get("umaResolutionStatus") or "").lower() == "resolved"
                m["status"] = "resolved" if final else "closed"
                prices = row.get("outcomePrices")
                try:
                    p = json.loads(prices) if isinstance(prices, str) else prices
                    if final and p:
                        m["last_price"] = float(p[0])
                except (ValueError, TypeError):
                    pass
                ed = row.get("endDate")
                if ed:
                    m["resolve_at"] = ed
                stats["resolved" if final else "closed"] += 1
            else:
                lp = row.get("lastTradePrice")
                if lp is not None:
                    m["last_price"] = float(lp)
                stats["still_active"] += 1
        for cid in batch:
            if cid not in seen:
                m = by_cid[cid]
                if (m.get("close_at") or "9999")[:10] < TODAY:
                    m["status"] = "closed"
                    stats["gone_closed"] += 1
                else:
                    stats["gone_left"] += 1
        time.sleep(0.2)


from datetime import date
TODAY = date.today().isoformat()


def main():
    bundle = json.loads(BUNDLE.read_text())
    fresh_ids = {m["market_id"] for m in json.loads(FRESH.read_text())["markets"]}
    carried = [m for m in bundle["markets"] if m["market_id"] not in fresh_ids]
    kal = [m for m in carried if m.get("platform") == "kalshi"]
    pol = [m for m in carried if m.get("platform") == "polymarket"]
    print(f"carried markets: {len(carried)} (kalshi {len(kal)} / polymarket {len(pol)})")

    stats = {"resolved": 0, "closed": 0, "still_active": 0,
             "gone_closed": 0, "gone_left": 0, "errors": 0}
    sweep_kalshi(kal, stats)
    print(f"  kalshi done: {stats}")
    sweep_poly(pol, stats)
    print(f"  total: {stats}")

    if WRITE:
        BUNDLE.write_text(json.dumps(bundle, ensure_ascii=False, separators=(",", ":")))
        print(f"wrote {BUNDLE}")
    else:
        print("(dry run — no write; pass --write to apply)")


if __name__ == "__main__":
    main()
