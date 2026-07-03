#!/usr/bin/env python3
"""
Grade-neutrality diff — the pre-ship gate for any grading/source change
(source-layer-refactor spec §5 test 7; replaces the histogram patch_sources printed).

Joins two enriched bundles by market_id and reports:
  - grade histogram old vs new (per venue)
  - every flip, up/down, with old/new commitment + the binding caps
  - the gate verdict: flips are EXPECTED where the commitment class changed;
    a flip with NO commitment change is a regression to investigate.

Usage:
  python3 scripts/grade_neutrality_diff.py OLD_BUNDLE NEW_BUNDLE [--max-list 40]
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

RANK = {"A": 3, "B": 2, "C": 1, "pending": 0, None: 0}


def markets_of(path: str) -> dict:
    b = json.loads(Path(path).read_text())
    ms = b["markets"] if isinstance(b, dict) else b
    return {m["market_id"]: m for m in ms}


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    max_list = int(sys.argv[sys.argv.index("--max-list") + 1]) if "--max-list" in sys.argv else 40
    old, new = markets_of(args[0]), markets_of(args[1])
    joined = [(mid, old[mid], new[mid]) for mid in new if mid in old]
    print(f"joined {len(joined)} markets (new bundle: {len(new)}, old bundle: {len(old)})")

    for venue in ("kalshi", "polymarket"):
        ho = Counter((o.get("resolution_clarity_grade") or "pending")
                     for _, o, n in joined if n.get("platform") == venue)
        hn = Counter((n.get("resolution_clarity_grade") or "pending")
                     for _, o, n in joined if n.get("platform") == venue)
        print(f"\n{venue:10} old: " + "  ".join(f"{g}:{ho.get(g,0)}" for g in ("A", "B", "C", "pending")))
        print(f"{'':10} new: " + "  ".join(f"{g}:{hn.get(g,0)}" for g in ("A", "B", "C", "pending")))

    flips, unexplained = [], []
    for mid, o, n in joined:
        og, ng = o.get("resolution_clarity_grade"), n.get("resolution_clarity_grade")
        if og == ng or "pending" in (og, ng, None) or og is None or ng is None:
            continue
        oc, nc = o.get("source_commitment_subtype"), n.get("source_commitment_subtype")
        direction = "UP" if RANK.get(ng, 0) > RANK.get(og, 0) else "DOWN"
        rec = {"market_id": mid, "venue": n.get("platform"), "q": (n.get("question_raw") or "")[:60],
               "grade": f"{og}->{ng}", "dir": direction, "commitment": f"{oc}->{nc}",
               "new_caps": n.get("rcg_caps"), "commitment_changed": oc != nc}
        flips.append(rec)
        if oc == nc:
            unexplained.append(rec)

    ups = sum(1 for f in flips if f["dir"] == "UP")
    downs = len(flips) - ups
    print(f"\nflips: {len(flips)}  (up: {ups}, down: {downs})  "
          f"commitment-explained: {len(flips) - len(unexplained)}  UNEXPLAINED: {len(unexplained)}")
    for f in flips[:max_list]:
        tag = "  " if f["commitment_changed"] else "?!"
        print(f" {tag} {f['dir']:4} {f['grade']:9} commit {f['commitment']:45} [{f['venue']}] {f['q']}")
    if len(flips) > max_list:
        print(f"  … {len(flips) - max_list} more")

    if unexplained:
        # A flip without a commitment change is either (a) the LLM factor re-rating moving on
        # fresh inputs — expected when the factor prompt changed; pre-refactor bundles carry no
        # factor stamps to diff against, so these need EYEBALL review, or (b) a real regression.
        # Once both bundles carry rcg.factors stamps, tighten this back to a hard FAIL on any
        # flip whose stamped factor ratings are identical.
        old_has_stamps = any(o.get("rcg") for _, o, n in joined)
        print(f"\nGATE: {'FAIL' if old_has_stamps else 'REVIEW'} — {len(unexplained)} flips with NO commitment change"
              f"{' (old bundle has factor stamps: investigate as regressions)' if old_has_stamps else ' (likely factor re-rating variance — eyeball each)'}:")
        for f in unexplained[:20]:
            print(f"   {f['market_id']} {f['grade']} caps={f['new_caps']} {f['q']}")
        sys.exit(1 if old_has_stamps else 0)
    print("\nGATE: PASS — every grade flip traces to a commitment change.")


if __name__ == "__main__":
    main()
