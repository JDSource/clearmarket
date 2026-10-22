#!/usr/bin/env python3
"""Export the grade-to-dispute backtest dataset as a flat CSV (one row per matched,
graded Polymarket market) from the dated raw files produced by
scripts/fetch_dispute_labels.py:

  data/dispute-labels-<date>.json   (grade + pre-registered dispute tier per market)
  data/uma-statuses-<date>.json     (raw Gamma sweep: UMA status trail + volume at sweep)

The raw files are large and gitignored; the CSV is committed under data/backtest/ so
the study in docs/BACKTEST.md can be re-run by anyone with scripts/backtest_stats.py
and no API access.

Usage: python3 scripts/export_backtest_labels.py 2026-07-23
"""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
date = sys.argv[1]
labels = json.load(open(ROOT / f"data/dispute-labels-{date}.json"))["labels"]
sweep = json.load(open(ROOT / f"data/uma-statuses-{date}.json"))

out = ROOT / f"data/backtest/dispute-labels-{date}.csv"
cols = ["market_id", "condition_id", "grade", "source_commitment", "tier1_challenged",
        "uma_statuses", "uma_final_status", "volume_usd_at_sweep", "question"]
n = 0
with open(out, "w", newline="") as f:
    w = csv.writer(f); w.writerow(cols)
    for r in labels:
        if not r.get("matched") or r.get("grade") not in ("A", "B", "C"):
            continue
        s = sweep.get(r["condition_id"]) or {}
        vol = s.get("volumeNum")
        w.writerow([r["market_id"], r["condition_id"], r["grade"], r.get("source_commitment") or "",
                    int(bool(r.get("tier1_challenged"))), "|".join(r.get("uma_statuses") or []),
                    r.get("uma_final_status") or "", f"{float(vol):.2f}" if vol is not None else "",
                    (s.get("question") or "").replace("\n", " ")])
        n += 1
print(f"wrote {out} ({n} rows)")
