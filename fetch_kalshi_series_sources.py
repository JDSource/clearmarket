#!/usr/bin/env python3
"""
Kalshi verified-source layer — fetch series settlement_sources for the universe.

Builds the Kalshi half of the verified-source layer AND measures coverage/quality.
`settlement_sources` is platform-stated (direct tier) but VARIABLE quality:
  - authoritative  : real agency/source (Fed, BLS, NWS, ...)
  - loose          : placeholder ("For example, Google Finance") — real URL, weak source;
                     the LLM `underlying_reference` (editorial tier) upgrades these.
  - missing        : no settlement_sources; resolution_source stays editorial-only.

Output: series-sources.json (series_ticker -> {sources, quality}) in the universe dir,
which enrich_universe.py reads to populate Kalshi resolution_source/source_citation
as `direct` (with a quality flag), instead of leaving it null.
"""
import json
import sys
from pathlib import Path

import requests

UNIV  = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-05-27"
CACHE = Path(__file__).parent / ".kalshi-series-cache"
BASE  = "https://api.elections.kalshi.com/trade-api/v2"
H     = {"User-Agent": "clearmarket/0.1"}


def fetch_series(st: str) -> dict:
    cp = CACHE / f"{st}.json"
    if cp.exists():
        return json.loads(cp.read_text())
    try:
        r = requests.get(f"{BASE}/series/{st}", headers=H, timeout=20)
        r.raise_for_status()
        s = r.json().get("series", {}) or {}
    except Exception as e:
        print(f"   {st} ERR {e}", file=sys.stderr)
        s = {}
    CACHE.mkdir(exist_ok=True)
    cp.write_text(json.dumps(s))
    return s


def quality(ss: list) -> str:
    if not ss:
        return "missing"
    p = ss[0]
    name = (p.get("name") or "").lower()
    url  = (p.get("url") or "").lower()
    if name.startswith("for example") or "google finance" in name or "google.com/finance" in url:
        return "loose"
    return "authoritative"


def main() -> None:
    evs = json.loads((UNIV / "kalshi-institutional.json").read_text())
    series = sorted({e.get("series_ticker") for e in evs if e.get("series_ticker")})
    out, tally, examples = {}, {"authoritative": 0, "loose": 0, "missing": 0}, \
        {"authoritative": [], "loose": [], "missing": []}
    for i, st in enumerate(series, 1):
        ss = fetch_series(st).get("settlement_sources") or []
        q = quality(ss)
        tally[q] += 1
        out[st] = {"sources": ss, "quality": q}
        if len(examples[q]) < 6:
            examples[q].append((st, ss[0] if ss else None))
        if i % 50 == 0:
            print(f"  {i}/{len(series)}", flush=True)
    (UNIV / "series-sources.json").write_text(json.dumps(out, indent=2))

    n = len(series)
    print("\n" + "=" * 64)
    print(f"Kalshi series settlement_sources — {n} unique series (covering {len(evs)} events)")
    for q in ("authoritative", "loose", "missing"):
        print(f"  {q:14}: {tally[q]:>4}  ({100*tally[q]/n:.0f}%)")
    print()
    for q in ("authoritative", "loose", "missing"):
        print(f"{q} examples:")
        for st, s0 in examples[q]:
            print(f"   {st}: {s0}")
    print("=" * 64)


if __name__ == "__main__":
    main()
