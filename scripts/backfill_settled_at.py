#!/usr/bin/env python3
"""
backfill_settled_at.py — one-time backfill of venue settlement timestamps.

The resolution-history surface displayed each market's DEADLINE (resolve_at) in its
RESOLVED column because the pipeline never stored when the venue actually settled the
market — Polymarket's closedTime and Kalshi's settlement_ts were dropped on the floor
(found 2026-07-23: early-resolved "by Dec 31" markets displayed future resolution dates).

This queries the venue for every terminal (resolved/closed) market in the served bundle
that lacks `settled_at` and stamps it. Going forward the field is captured live by
settle_status_sweep.py / sweep_past_due.py; this script exists to correct history and
should rarely be needed again. Zero LLM calls — venue metadata GETs only.

Coverage is honest, not total: markets the venue no longer serves (delisted) have no
retrievable settlement time and keep only their deadline; build_resolution_log.py marks
those rows occurred_basis='deadline'.

Usage:
  python3 scripts/backfill_settled_at.py            # dry run (report only)
  python3 scripts/backfill_settled_at.py --write    # apply to the bundle
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import settle_status_sweep as S  # reuse _get, HEADERS, endpoints, poly_closed_time

WRITE = "--write" in sys.argv
KALSHI_BATCH = 50
POLY_BATCH = 50


def backfill_kalshi(markets, stats):
    by_ticker = {m["platform_market_id"]: m for m in markets if m.get("platform_market_id")}
    tickers = sorted(by_ticker)
    for i in range(0, len(tickers), KALSHI_BATCH):
        batch = tickers[i:i + KALSHI_BATCH]
        data = S._get(f"{S.KALSHI}/markets", params={"tickers": ",".join(batch), "limit": len(batch)})
        rows = (data or {}).get("markets") if isinstance(data, dict) else None
        if data == "ERR" or rows is None:
            stats["errors"] += len(batch)
            continue
        seen = set()
        for k in rows:
            t = k.get("ticker")
            m = by_ticker.get(t)
            if not m or t in seen:
                continue
            seen.add(t)
            st = k.get("settlement_ts") or k.get("close_time")
            if st and (k.get("status") or "").lower() in ("finalized", "settled", "closed"):
                m["settled_at"] = st
                stats["stamped"] += 1
            else:
                stats["no_ts"] += 1
        stats["gone"] += len([t for t in batch if t not in seen])
        time.sleep(0.12)


def backfill_poly(markets, stats):
    by_cid = {m["platform_market_id"]: m for m in markets if m.get("platform_market_id")}
    cids = sorted(by_cid)
    for i in range(0, len(cids), POLY_BATCH):
        batch = cids[i:i + POLY_BATCH]
        rows = []
        for closed in (None, "true"):
            got = {r.get("conditionId") for r in rows}
            missing = [c for c in batch if c not in got]
            if not missing:
                break
            params = [("condition_ids", c) for c in missing] + [("limit", "100")]
            if closed:
                params.append(("closed", "true"))
            res = S._get(S.GAMMA, params)
            if res in (None, "ERR"):
                stats["errors"] += len(missing)
                continue
            rows += res
        seen = set()
        for row in rows:
            cid = row.get("conditionId")
            m = by_cid.get(cid)
            if not m or cid in seen:
                continue
            seen.add(cid)
            ct = S.poly_closed_time(row)
            if ct and row.get("closed"):
                m["settled_at"] = ct
                stats["stamped"] += 1
            else:
                stats["no_ts"] += 1
        stats["gone"] += len([c for c in batch if c not in seen])
        time.sleep(0.2)


def main():
    bundle = json.loads(S.BUNDLE.read_text())
    target = [m for m in bundle["markets"]
              if (m.get("status") in ("resolved", "closed")) and not m.get("settled_at")]
    kal = [m for m in target if m.get("platform") == "kalshi"]
    pol = [m for m in target if m.get("platform") == "polymarket"]
    print(f"terminal markets missing settled_at: {len(target)} (kalshi {len(kal)} / polymarket {len(pol)})")

    stats = {"stamped": 0, "no_ts": 0, "gone": 0, "errors": 0}
    backfill_kalshi(kal, stats)
    print(f"  kalshi done: {stats}")
    backfill_poly(pol, stats)
    print(f"  total: {stats}")
    covered = sum(1 for m in bundle["markets"]
                  if m.get("status") in ("resolved", "closed") and m.get("settled_at"))
    terminal = sum(1 for m in bundle["markets"] if m.get("status") in ("resolved", "closed"))
    print(f"settled_at coverage: {covered}/{terminal} terminal markets ({covered / max(terminal, 1):.0%})")

    if WRITE:
        S.BUNDLE.write_text(json.dumps(bundle, ensure_ascii=False, separators=(",", ":")))
        print(f"wrote {S.BUNDLE}")
    else:
        print("(dry run — no write; pass --write to apply)")


if __name__ == "__main__":
    main()
