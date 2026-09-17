#!/usr/bin/env python3
"""
fetch_kalshi_open.py — hourly snapshot of the TRACKED Kalshi markets' status, price and volume.

Why: Kalshi rate-limits Cloudflare Workers' shared egress IPs at the first request (HTTP 429), so the
Worker's own hourly Kalshi scan only got through sporadically (cron_runs made it visible 2026-09-17).
GitHub runners are not throttled. Kalshi lists >300k open markets and ClearMarket tracks ~5k, so instead
of a full scan this asks for exactly the tracked tickers (GET /markets?tickers=…, 200 per request).

Flow: page api.clearmarket.fyi/v1/marks?platform=kalshi&status=open for the tracked tickers → query
Kalshi in batches → write one compact JSON the Worker's refreshMarks() applies (fields mirror the venue:
s=status, p=last_price_dollars, v24=volume_24h_fp, v=volume_fp, r=result, ct=close_time).

Usage: fetch_kalshi_open.py OUT_JSON   (non-zero exit on failure so the workflow shows red)
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

CM = "https://api.clearmarket.fyi/v1/marks"
KALSHI = "https://api.elections.kalshi.com/trade-api/v2/markets"
UA = "clearmarket-marks/0.2 (+https://clearmarket.fyi)"
BATCH = 200


def get(url, tries=5):
    last = None
    for i in range(tries):
        if i:
            time.sleep(min(2 * 2 ** (i - 1), 20))
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            last = e
            if e.code != 429 and e.code < 500:
                raise
        except Exception as e:
            last = e
    raise RuntimeError(f"giving up on {url[:80]}: {last}")


def tracked_tickers():
    tickers, cursor = [], None
    while True:
        q = {"platform": "kalshi", "status": "open", "limit": "1000"}
        if cursor:
            q["cursor"] = cursor
        d = get(f"{CM}?{urllib.parse.urlencode(q)}")
        tickers += [m["platform_market_id"] for m in d.get("marks", []) if m.get("platform_market_id")]
        cursor = d.get("next_cursor")
        if not cursor:
            break
    return tickers


def main(out_path):
    tickers = tracked_tickers()
    if len(tickers) < 500:
        print(f"only {len(tickers)} tracked Kalshi tickers from the API — refusing to publish", file=sys.stderr)
        sys.exit(1)
    markets, requests_made = [], 0
    for i in range(0, len(tickers), BATCH):
        chunk = tickers[i:i + BATCH]
        d = get(f"{KALSHI}?{urllib.parse.urlencode({'tickers': ','.join(chunk), 'limit': '1000'})}")
        requests_made += 1
        for m in d.get("markets") or []:
            markets.append({"t": m.get("ticker"), "s": m.get("status"), "p": m.get("last_price_dollars"),
                            "v24": m.get("volume_24h_fp"), "v": m.get("volume_fp"),
                            "r": m.get("result") or None, "ct": m.get("close_time")})
        time.sleep(0.2)
    by_status = {}
    for m in markets:
        by_status[m["s"]] = by_status.get(m["s"], 0) + 1
    out = {"generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
           "source": KALSHI + "?tickers=", "tracked": len(tickers), "returned": len(markets),
           "by_status": by_status, "markets": markets}
    with open(out_path, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"kalshi tracked snapshot: {len(markets)}/{len(tickers)} returned in {requests_made} requests; by_status={by_status} -> {out_path}")
    if len(markets) < 0.8 * len(tickers):
        print("returned far fewer markets than tracked — failing so the workflow shows red", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
