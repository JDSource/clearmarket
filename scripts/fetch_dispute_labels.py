#!/usr/bin/env python3
"""
fetch_dispute_labels.py — build the dispute-label dataset for the grade-to-dispute backtest.

Replaces the session-temp /tmp/full_join.py from the 2026-06-10 validation run with a
committed, reproducible script (same posture as the CFTC pull scripts).

What it does
------------
1. Targeted sweep: collects the conditionIds of every Polymarket market in the CM
   universe (union of the current bundle + the freshest raw pull), queries Gamma
   /markets in batches of condition_ids (two passes per batch — default returns
   open markets only, closed=true recovers the rest; full-surface offset paging
   is NOT viable, Gamma 422s past offset 10,000). Records per conditionId:
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


BATCH = 50


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


def _universe_condition_ids():
    """Union of conditionIds: current bundle + freshest raw pull."""
    cids = set()
    if BUNDLE.exists():
        bundle = json.loads(BUNDLE.read_text())
        for m in bundle["markets"]:
            if m.get("platform") == "polymarket" and m.get("platform_market_id"):
                cids.add(m["platform_market_id"])
    pulls = sorted((Path.home() / "jeremy-os/raw").glob("clearmarket-universe-2*"))
    pulls = [p for p in pulls if "_smoke" not in p.name]
    if pulls:
        raw = json.loads((pulls[-1] / "poly-institutional.json").read_text())
        for ev in raw:
            for m in ev.get("markets", []):
                if m.get("conditionId"):
                    cids.add(m["conditionId"])
        print(f"id sources: bundle + {pulls[-1].name}")
    return sorted(cids)


def sweep(max_pages=None):
    """Batched condition_ids queries, two passes per batch (open default + closed)."""
    cids = _universe_condition_ids()
    if max_pages:
        cids = cids[: max_pages * BATCH]
    print(f"sweeping {len(cids)} conditionIds in batches of {BATCH}...")
    out = {}
    for i in range(0, len(cids), BATCH):
        batch = cids[i : i + BATCH]
        rows = _page([("condition_ids", c) for c in batch] + [("limit", "100")])
        got = set()
        for row in rows:
            cid = row.get("conditionId")
            if cid:
                out[cid] = {k: row.get(k) for k in KEEP}
                got.add(cid)
        missing = [c for c in batch if c not in got]
        if missing:
            rows = _page([("condition_ids", c) for c in missing]
                         + [("limit", "100"), ("closed", "true")])
            for row in rows:
                cid = row.get("conditionId")
                if cid:
                    out[cid] = {k: row.get(k) for k in KEEP}
        if (i // BATCH) % 25 == 0:
            print(f"  {i + len(batch)}/{len(cids)} ids, {len(out)} found")
        time.sleep(PAUSE)
    path = OUT_DIR / f"uma-statuses-{TODAY}.json"
    path.write_text(json.dumps(out, indent=1))
    print(f"wrote {path} ({len(out)} of {len(cids)} conditionIds resolved)")
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
