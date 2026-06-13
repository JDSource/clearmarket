"""
regrade_rcg.py — re-run ONLY the RCG factor rating + grade on the existing -linked bundle, to apply
the source_conflict prompt fix WITHOUT a full re-enrichment. Preserves canon claim_sigs + source/ladder
patches (they live in -linked and we only touch grade fields). Reuses the SAME tested code enrich_event
runs: enhance.llm_rcg_factors (one Haiku call/event, cached) + classify.grade_market.

Usage:
  python3 regrade_rcg.py --sample 8 --dry   # verify it runs, show grade dist, write nothing
  python3 regrade_rcg.py                     # full run, 6 workers, writes -linked (backup once)
"""
import json, sys
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
import enhance as E
from classify import grade_market

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
# Dated backup: the old static name + "backup once" guard meant a second run on the
# same checkout silently took NO backup (the only rollback artifact was a stale one).
BACKUP = ROOT / f"web/data/universe-enriched-linked.pre-regrade-{date.today().isoformat()}-bak.json"
DRY = "--dry" in sys.argv
SAMPLE = int(sys.argv[sys.argv.index("--sample") + 1]) if "--sample" in sys.argv else None

def regrade_event(args):
    event, markets = args
    try:
        factors = E.llm_rcg_factors(event, markets)
        if not factors:
            return (event["event_id"], 0, "no factors")
        event["rcg_factors"] = factors
        ratings = {k: v["rating"] for k, v in factors.items()}
        n = 0
        for m in markets:
            rcg = grade_market(m, m.get("resolution_rules_raw") or "", llm_ratings=ratings)
            m["resolution_clarity_grade"] = rcg["grade"]
            m["rcg_score"], m["rcg_caps"] = rcg["score"], rcg["caps"]
            m["rcg_applied_factors"] = rcg.get("applied_factors")
            n += 1
        return (event["event_id"], n, None)
    except Exception as e:
        return (event["event_id"], 0, str(e)[:80])

def main():
    bundle = json.loads(BUNDLE.read_text())
    by_event = defaultdict(list)
    for m in bundle["markets"]:
        if m.get("event_id"):
            by_event[m["event_id"]].append(m)
    events = bundle["events"][:SAMPLE] if SAMPLE else bundle["events"]
    work = [(e, by_event[e["event_id"]]) for e in events if by_event.get(e["event_id"])]
    print(f"re-grading {len(work)} events ({sum(len(m) for _, m in work)} markets), 6 workers...", flush=True)
    if not DRY and not BACKUP.exists():
        BACKUP.write_text(BUNDLE.read_text()); print(f"backed up -> {BACKUP.name}", flush=True)
    done = errs = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for eid, n, err in ex.map(regrade_event, work):
            done += 1
            if err: errs += 1
            if done % 100 == 0:
                print(f"  {done}/{len(work)} events ({errs} errs)", flush=True)
    graded_ids = {e["event_id"] for e, _ in work}
    graded = [m for m in bundle["markets"] if m.get("event_id") in graded_ids]
    dist = Counter(m.get("resolution_clarity_grade") for m in graded)
    print(f"\ndone: {done} events, {errs} errors. grade dist: {dict(dist)}", flush=True)
    for plat in ("kalshi", "polymarket"):
        ms = [m for m in graded if m["platform"] == plat]
        ab = sum(1 for m in ms if m.get("resolution_clarity_grade") in ("A", "B"))
        print(f"  {plat}: {ab}/{len(ms)} A+B ({100 * ab // max(1, len(ms))}%)", flush=True)
    if DRY:
        print("--dry: nothing written"); return
    BUNDLE.write_text(json.dumps(bundle))
    print(f"wrote {BUNDLE.name}", flush=True)

if __name__ == "__main__":
    main()
