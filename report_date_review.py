#!/usr/bin/env python3
"""
Date-review queue reporter (periodic surfacing of temporally-suspect markets).

The enrichment pipeline auto-CORRECTS the two fixable date-mangle classes (ladder rungs via
_reconcile_ladder_dates; fabricated question years via the llm_canonical_question guard +
fix_questions.py). This reporter surfaces the RESIDUAL that neither auto-fix caught, so a human
can eyeball it. Low-noise by design (see classify.date_review_reason): it does NOT flag the
legitimate 'measured in year N, settles N+1/N+2' pattern.

Two signals:
  - per market : stale_year (user-visible question shows a year >=2yr behind settlement, not in
                 the raw source) | missing_resolve_at
  - per event  : degenerate_ladder_dates (a date/strike ladder whose children all still share one
                 resolve_at — a Family-B case reconciliation could not repair)

Usage:
  python3 report_date_review.py                       # reads web/data/universe-enriched-linked.json
  python3 report_date_review.py <bundle.json>         # or an explicit bundle
Writes data/date-review-queue.json and prints a digest. Exit code 1 if the queue is non-empty
(so a cron / CI wrapper can alert). Read-only against the bundle.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
DEFAULT_BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
OUT = ROOT / "data/date-review-queue.json"


def main():
    bundle_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BUNDLE
    if not bundle_path.exists():
        print(f"bundle not found: {bundle_path}", file=sys.stderr)
        return 2
    b = json.loads(bundle_path.read_text())
    events = {e["event_id"]: e for e in b.get("events", [])}
    mbye = defaultdict(list)
    for m in b.get("markets", []):
        mbye[m.get("event_id")].append(m)

    def years(s):
        return {int(y) for y in re.findall(r"\b(20\d{2})\b", str(s or ""))}

    queue = []
    for eid, ms in mbye.items():
        ev = events.get(eid, {})
        # (a) stale year in the USER-VISIBLE event question. Predicate held IDENTICAL to
        #     fix_questions.py Trigger 2 so the queue drains to 0 once that pass runs: a display
        #     year present in NEITHER the children's question_raw NOR any settlement year, and
        #     >=2yr behind the max settlement year. (group_item_title deliberately NOT in src.)
        settle_years = set().union(*[years(m.get("resolve_at")) for m in ms]) if ms else set()
        src_years = set().union(*[years(m.get("question_raw")) for m in ms]) if ms else set()
        settle = max(settle_years) if settle_years else None
        disp = years(ev.get("question"))
        if settle:
            stale = sorted(y for y in disp if y <= settle - 2 and y not in src_years and y not in settle_years)
            if stale:
                queue.append({"level": "event", "reason": f"stale_year:{stale}<settle:{settle}",
                              "event_slug": ev.get("slug"), "event_id": eid,
                              "question": ev.get("question"), "n_children": len(ms)})
        # (b) missing settlement date (per-market — a genuinely per-child gap)
        for m in ms:
            if not m.get("resolve_at"):
                queue.append({"level": "market", "reason": "missing_resolve_at",
                              "event_slug": ev.get("slug"), "event_id": eid,
                              "market_id": m.get("market_id"), "question": ev.get("question")})
        # (c) date/strike ladder whose non-null dates are all identical (reconcile couldn't repair).
        #     Ignore None so one null-date child doesn't mask a degenerate ladder.
        if ev.get("bundle_type") in ("date_ladder", "strike_ladder") and len(ms) > 1:
            nonnull = {m.get("resolve_at") for m in ms if m.get("resolve_at")}
            if len(nonnull) <= 1:
                queue.append({"level": "event", "reason": "degenerate_ladder_dates",
                              "event_slug": ev.get("slug"), "event_id": eid,
                              "question": ev.get("question"),
                              "resolve_at": next(iter(nonnull), None), "n_children": len(ms)})

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({"bundle": str(bundle_path), "count": len(queue), "items": queue},
                              indent=2, default=str))

    by_reason = defaultdict(int)
    for q in queue:
        by_reason[q["reason"].split(":")[0]] += 1
    print(f"date-review queue: {len(queue)} items  ({bundle_path.name})")
    for r, n in sorted(by_reason.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5}  {r}")
    print(f"\nfull list -> {OUT}")
    for q in queue[:15]:
        print(f"  [{q['level']:6}] {q['reason']:28} {q.get('event_slug')}  {str(q.get('question'))[:48]!r}")
    if len(queue) > 15:
        print(f"  ... +{len(queue)-15} more in the JSON")
    return 1 if queue else 0


if __name__ == "__main__":
    sys.exit(main())
