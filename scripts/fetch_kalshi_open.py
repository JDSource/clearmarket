#!/usr/bin/env python3
"""
fetch_kalshi_open.py — snapshot every OPEN Kalshi market's price + volume to one compact JSON file.

Why this exists: Kalshi rate-limits Cloudflare Workers' shared egress IPs at the first request (HTTP 429),
so the Worker's hourly refresh only reached Kalshi sporadically (cron_runs made this visible 2026-09-17).
GitHub runners are not throttled the same way. This job publishes kalshi-open-latest.json to R2 every hour;
the Worker's refreshMarks() reads it when its own direct fetch fails (or is fresher), and applies it to the
tracked markets exactly as it would a direct response. Fields mirror the venue: last_price_dollars,
volume_24h_fp (contracts), volume_fp (contracts).

Usage: fetch_kalshi_open.py OUT_JSON      (exit 1 on any non-200 after retries, so the workflow fails loudly)
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE = "https://api.elections.kalshi.com/trade-api/v2/markets"
UA = "clearmarket-marks/0.2 (+https://clearmarket.fyi)"


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
        except Exception as e:  # network blip
            last = e
    raise RuntimeError(f"giving up: {last}")


def main(out_path):
    markets, cursor, pages = [], None, 0
    while True:
        q = {"status": "open", "limit": "1000"}
        if cursor:
            q["cursor"] = cursor
        d = get(f"{BASE}?{urllib.parse.urlencode(q)}")
        batch = d.get("markets") or []
        for m in batch:
            markets.append({"t": m.get("ticker"), "p": m.get("last_price_dollars"),
                            "v24": m.get("volume_24h_fp"), "v": m.get("volume_fp")})
        pages += 1
        cursor = d.get("cursor")
        if not cursor or not batch or pages >= 300:
            break
        time.sleep(0.2)
    out = {"generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
           "source": BASE, "pages": pages, "count": len(markets), "markets": markets}
    with open(out_path, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"kalshi open snapshot: {len(markets)} markets over {pages} pages -> {out_path}")
    if len(markets) < 1000:
        print("suspiciously small snapshot — failing so the workflow shows red", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
