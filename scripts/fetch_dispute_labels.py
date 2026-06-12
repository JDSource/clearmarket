#!/usr/bin/env python3
"""
fetch_dispute_labels.py — build the dispute-label dataset for the grade-to-dispute backtest.

Replaces the session-temp /tmp/full_join.py from the 2026-06-10 validation run with a
committed, reproducible script (same posture as the CFTC pull scripts).

What it does
------------
1. Sweeps the FULL Polymarket Gamma /markets surface (two passes: closed=true and
   closed=false; Gamma caps pages at 100) and records, per conditionId:
   umaResolutionStatuses (the dispute trail), umaResolutionStatus (final),
   closed flag, volumeNum, question.
2. Joins the sweep against the CM bundle's Polymarket markets by platform_market_id
   (= conditionId) and stamps each with a dispute tier.

Dispute tiers — PRE-REGISTERED (grade-to-dispute-backtest-spec.md):
  tier1_challenged : "disputed" appears anywhere in umaResolutionStatuses.
                     Includes frivolous challenges — reported as-is, stated in methods.
  tier2_overturned : final outcome differs from first UMA proposal. NOT derivable from
                     Gamma alone (needs the UMA subgraph / on-chain history) — left null
                     here; populated by a future pass. Do not infer it from tier1.
  tier3_publicly_contested : hand-curated (press / lawsuits / regulator action) in
                     data/dispute-labels-curated.json. Kalshi cases live there too —
                     Kalshi has no public dispute feed, so recall is lower by design.

Outputs
-------
  data/uma-statuses-<date>.json    — raw sweep: conditionId -> uma fields (refetchable)
  data/dispute-labels-<date>.json  — joined labels keyed by CM market_id + conditionId

Usage
-----
  python3 scripts/fetch_dispute_labels.py --sweep            # run the Gamma sweep (slow)
  python3 scripts/fetch_dispute_labels.py --join             # join newest sweep vs bundle
  python3 scripts/fetch_dispute_labels.py --sweep --join     # both
  python3 scripts/fetch_dispute_labels.py --sweep --max-pages 2   # smoke test
"""
import json
import sys
import time
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
OUT_DIR = ROOT / "data"
TODAY = date.today().isoformat()

GAMMA = "https://gamma-api.polymarket.com/markets"
HEADERS = {"User-Agent": "clearmarket-fetcher/0.1"}
PAGE = 100          # Gamma hard cap
PAUSE = 0.25        # polite pacing
TIMEOUT = 30
RETRIES = 3

KEEP = ("umaResolutionStatuses", "umaResolutionStatus", "closed",
        "volumeNum", "question", "endDate")


def _page(params):
    for attempt in range(RETRIES):
        try:
            r = requests.get(GAMMA, params=params, timeout=TIMEOUT, headers=HEADERS)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            if attempt == RETRIES - 1:
                raise
            time.sleep(2 ** attempt)


def sweep(max_pages=None):
    """Two passes (closed / open) over the full Gamma markets surface."""
    out = {}
    for closed in ("true", "false"):
        offset, pages = 0, 0
        while True:
            rows = _page({"limit": PAGE, "offset": offset, "closed": closed})
            if not rows:
                break
            for row in rows:
                cid = row.get("conditionId")
                if not cid:
                    continue
                out[cid] = {k: row.get(k) for k in KEEP}
            offset += PAGE
            pages += 1
            if pages % 25 == 0:
                print(f"  [closed={closed}] {pages} pages, {len(out)} unique conditionIds")
            if max_pages and pages >= max_pages:
                break
            time.sleep(PAUSE)
        print(f"[closed={closed}] done: {pages} pages")
    path = OUT_DIR / f"uma-statuses-{TODAY}.json"
    path.write_text(json.dumps(out, indent=1))
    print(f"wrote {path} ({len(out)} conditionIds)")
    return out


def _statuses(raw):
    """umaResolutionStatuses arrives as a JSON-encoded string like '["disputed","proposed"]'."""
    if not raw:
        return []
    if isinstance(raw, list):
        return raw
    try:
        v = json.loads(raw)
        return v if isinstance(v, list) else []
    except (ValueError, TypeError):
        return []


def join():
    sweeps = sorted(OUT_DIR.glob("uma-statuses-*.json"))
    if not sweeps:
        sys.exit("no uma-statuses-*.json found — run --sweep first")
    uma = json.loads(sweeps[-1].read_text())
    bundle = json.loads(BUNDLE.read_text())
    polys = [m for m in bundle["markets"] if m.get("platform") == "polymarket"]

    labels, matched, disputed = [], 0, 0
    for m in polys:
        cid = m.get("platform_market_id")
        hit = uma.get(cid)
        sts = _statuses(hit and hit.get("umaResolutionStatuses"))
        is_matched = hit is not None
        t1 = "disputed" in sts
        matched += is_matched
        disputed += t1
        labels.append({
            "market_id": m.get("market_id"),
            "condition_id": cid,
            "venue": "polymarket",
            "matched": is_matched,
            "uma_statuses": sts,
            "uma_final_status": hit.get("umaResolutionStatus") if hit else None,
            "tier1_challenged": t1,
            "tier2_overturned": None,   # UMA subgraph pass — see docstring
            "grade": m.get("resolution_clarity_grade"),
            "source_commitment": m.get("source_commitment_subtype"),
        })

    path = OUT_DIR / f"dispute-labels-{TODAY}.json"
    path.write_text(json.dumps(
        {"_meta": {"generated_at": TODAY, "sweep_file": sweeps[-1].name,
                   "bundle_markets_poly": len(polys), "matched": matched,
                   "tier1_challenged": disputed,
                   "tier_definitions": "see script docstring — pre-registered"},
         "labels": labels}, indent=1))
    print(f"wrote {path}")
    print(f"polymarket markets in bundle: {len(polys)}  matched: {matched} "
          f"({matched / max(len(polys), 1):.0%})  tier1 disputed: {disputed}")
    by_grade = {}
    for l in labels:
        if not l["matched"]:
            continue
        g = l["grade"] or "?"
        a, b = by_grade.get(g, (0, 0))
        by_grade[g] = (a + l["tier1_challenged"], b + 1)
    for g in sorted(by_grade):
        a, b = by_grade[g]
        print(f"  grade {g}: {a}/{b} disputed ({a / max(b, 1):.2%})")


if __name__ == "__main__":
    mp = None
    if "--max-pages" in sys.argv:
        mp = int(sys.argv[sys.argv.index("--max-pages") + 1])
    if "--sweep" in sys.argv:
        sweep(max_pages=mp)
    if "--join" in sys.argv:
        join()
    if len(sys.argv) == 1:
        print(__doc__)
