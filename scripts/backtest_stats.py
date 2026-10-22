#!/usr/bin/env python3
"""Reproduce every number in docs/BACKTEST.md from the committed CSV. No API, no key.

  python3 scripts/backtest_stats.py data/backtest/dispute-labels-2026-07-23.csv

Dispute definition (pre-registered before counting, see scripts/fetch_dispute_labels.py):
  disputed = the string "disputed" appears anywhere in the market's UMA resolution
  status trail, i.e. a formal on-chain challenge was filed against a proposed outcome,
  whether or not the challenge succeeded.
Grades are ClearMarket Resolution Clarity Grades computed from rules text only; the
grader never sees dispute history.
"""
import csv, math, sys
from collections import Counter, defaultdict

path = sys.argv[1] if len(sys.argv) > 1 else "data/backtest/dispute-labels-2026-07-23.csv"
rows = list(csv.DictReader(open(path)))
for r in rows:
    r["disp"] = r["tier1_challenged"] == "1"
    r["vol"] = float(r["volume_usd_at_sweep"]) if r["volume_usd_at_sweep"] else None

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 0.0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)

def cell(k, n):
    lo, hi = wilson(k, n)
    return f"{k:>3} / {n:>5}  {100*k/n:5.2f}%   95% CI [{100*lo:.2f}%, {100*hi:.2f}%]"

N = len(rows); D = sum(r["disp"] for r in rows)
print(f"Sample: {N} matched, graded Polymarket markets; {D} disputed (file: {path})\n")

print("1. Dispute rate by Resolution Clarity Grade")
tab = {}
for g in "ABC":
    n = sum(1 for r in rows if r["grade"] == g); k = sum(1 for r in rows if r["grade"] == g and r["disp"])
    tab[g] = (k, n); print(f"   {g}: {cell(k, n)}")
kab = tab["A"][0] + tab["B"][0]; nab = tab["A"][1] + tab["B"][1]; kc, nc = tab["C"]
print(f"   A+B combined: {cell(kab, nab)}")
rr = (kc / nc) / (kab / nab); se = math.sqrt(1 / kc - 1 / nc + 1 / kab - 1 / nab)
print(f"   Relative risk, C vs A+B: {rr:.1f}x   95% CI [{rr*math.exp(-1.96*se):.1f}x, {rr*math.exp(1.96*se):.1f}x]")
print(f"   Share of all disputes that were graded C before resolution: {kc}/{D} = {100*kc/D:.1f}%\n")

print("2. Dispute rate by resolution-source commitment (the input the grade caps on)")
c = Counter(); d = Counter()
for r in rows: c[r["source_commitment"]] += 1; d[r["source_commitment"]] += r["disp"]
for s, n in c.most_common(): print(f"   {s:<26} {cell(d[s], n)}")
print()

print("3. Volume control: dispute rate by grade within trading-volume quartile (volume at sweep date)")
vr = sorted((r for r in rows if r["vol"] is not None), key=lambda r: r["vol"])
q = len(vr) // 4
bands = [("Q1 lowest", vr[:q]), ("Q2", vr[q:2*q]), ("Q3", vr[2*q:3*q]), ("Q4 highest", vr[3*q:])]
print(f"   ({len(vr)} markets with volume; {N-len(vr)} without, excluded here)")
for name, band in bands:
    parts = []
    for g in "ABC":
        n = sum(1 for r in band if r["grade"] == g); k = sum(1 for r in band if r["grade"] == g and r["disp"])
        parts.append(f"{g} {k}/{n} ({100*k/n:.2f}%)" if n else f"{g} 0/0")
    print(f"   {name:<11} " + "   ".join(parts))
top = bands[3][1]
nab = sum(1 for r in top if r["grade"] in "AB"); kab = sum(1 for r in top if r["grade"] in "AB" and r["disp"])
nc = sum(1 for r in top if r["grade"] == "C"); kc = sum(1 for r in top if r["grade"] == "C" and r["disp"])
print(f"   Top quartile, A+B: {cell(kab, nab)}")
print(f"   Top quartile, C:   {cell(kc, nc)}\n")

print("4. What happened to the challenged A-grade markets")
for r in rows:
    if r["grade"] == "A" and r["disp"]:
        print(f"   {r['market_id']}  trail={r['uma_statuses']}  final={r['uma_final_status']}  source={r['source_commitment']}  | {r['question'][:70]}")
