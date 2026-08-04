#!/usr/bin/env python3
"""
Kalshi verified-source layer — fetch series settlement_sources for the universe.

Builds the Kalshi half of the verified-source layer AND measures coverage/quality.
`settlement_sources` is platform-stated (direct tier) but VARIABLE quality:
  - authoritative  : real agency/source (Fed, BLS, NWS, ...)
  - loose          : placeholder ("For example, Google Finance") — real URL, weak source;
                     the LLM `underlying_reference` (editorial tier) upgrades these.
  - missing        : no settlement_sources; resolution_source stays editorial-only.

Output: series-sources.json (series_ticker -> {sources, quality, important_info}) in the
universe dir, which enrich_universe.py reads to populate Kalshi resolution_source/
source_citation as `direct` (with a quality flag), instead of leaving it null.

`important_info` (product_metadata.important_info) is Kalshi's page-banner channel for
resolution-mechanics notices (source transitions, reading instructions). Sparse (~2% of
series) but resolution-relevant when present — captured since 2026-08-04 (Burke gold case:
banner announced a settlement-feed change the settlement_sources field didn't reflect).

Snapshots: every run also writes series-sources-snapshots/YYYY-MM-DD.json (sources +
important_info only) so mid-series source changes are diffable after the fact.

--refresh bypasses the per-series cache (the cache otherwise never refetches, which is
exactly how a mid-series change stays invisible).
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import requests

UNIV  = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-07-23"
CACHE = Path(__file__).parent / ".kalshi-series-cache"
BASE  = "https://api.elections.kalshi.com/trade-api/v2"
H     = {"User-Agent": "clearmarket/0.1"}
REFRESH = "--refresh" in sys.argv


def fetch_series(st: str) -> dict:
    cp = CACHE / f"{st}.json"
    if cp.exists() and not REFRESH:
        return json.loads(cp.read_text())
    try:
        r = requests.get(f"{BASE}/series/{st}", headers=H, timeout=20)
        r.raise_for_status()
        s = r.json().get("series", {}) or {}
    except Exception as e:
        print(f"   {st} ERR {e}", file=sys.stderr)
        if cp.exists():  # refresh failed — keep the cached copy rather than blanking it
            return json.loads(cp.read_text())
        s = {}
    CACHE.mkdir(exist_ok=True)
    cp.write_text(json.dumps(s))
    return s


def important_info(series: dict) -> dict | None:
    """Normalized banner notice, or None. Kept whole — the text is the payload."""
    ii = (series.get("product_metadata") or {}).get("important_info") or {}
    text = ii.get("markdown") or ii.get("message") or ""
    if not text.strip():
        return None
    return {"id": ii.get("id"), "title": ii.get("title") or None, "text": text.strip(),
            "scope": (series.get("product_metadata") or {}).get("scope")}


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
    series = {e.get("series_ticker") for e in evs if e.get("series_ticker")}
    # ALSO cover series that live only in the shipped bundle (resolved/legacy markets are
    # retained there for the backtest but drop out of the current raw event list — found
    # 2026-08-04: 232 series / 82 open markets missing). Ticker's first segment IS the
    # series ticker.
    bundle_path = Path(__file__).parent / "web/data/universe-enriched-linked.json"
    if bundle_path.exists():
        b = json.loads(bundle_path.read_text())
        series |= {(m.get("platform_market_id") or "").split("-")[0].upper()
                   for m in b.get("markets", [])
                   if m.get("platform") == "kalshi" and m.get("platform_market_id")}
        series.discard("")
    series = sorted(series)
    out, tally, examples = {}, {"authoritative": 0, "loose": 0, "missing": 0}, \
        {"authoritative": [], "loose": [], "missing": []}
    notices = []
    for i, st in enumerate(series, 1):
        s = fetch_series(st)
        ss = s.get("settlement_sources") or []
        q = quality(ss)
        ii = important_info(s)
        tally[q] += 1
        out[st] = {"sources": ss, "quality": q, "important_info": ii}
        if ii:
            notices.append((st, ii))
        if len(examples[q]) < 6:
            examples[q].append((st, ss[0] if ss else None))
        if i % 50 == 0:
            print(f"  {i}/{len(series)}", flush=True)
    (UNIV / "series-sources.json").write_text(json.dumps(out, indent=2))

    # dated snapshot — the diffable history of what Kalshi said settles each series
    snapdir = UNIV / "series-sources-snapshots"
    snapdir.mkdir(exist_ok=True)
    snap = {st: {"sources": v["sources"], "important_info": v["important_info"]}
            for st, v in out.items()}
    (snapdir / f"{date.today().isoformat()}.json").write_text(json.dumps(snap, indent=2))

    if notices:
        print(f"\nimportant_info notices ({len(notices)}):")
        for st, ii in notices:
            print(f"   {st} [{ii.get('id')}]: {ii['text'][:120]}")

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
