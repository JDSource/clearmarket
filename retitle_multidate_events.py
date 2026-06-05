#!/usr/bin/env python3
"""
retitle_multidate_events.py — generalize the title of multi-date "series" events.

Problem: a venue event that bundles several deadline/date legs of the SAME question (e.g. Bitcoin
ATH by Mar 31 / Jun 30 / Sep 30 / Dec 31) gets titled after its FIRST leg ("...by March 31, 2026?").
So the H1 asserts one date while the markets span several, and the resolves-tag + representative
question contradict the title.

Fix = deterministic DETECTION + LLM GENERATION + deterministic VALIDATION:
  - detect (deterministic): event whose markets span >1 distinct resolution date AND whose question
    names a specific calendar day -> mis-title candidate. (A date invariant — no LLM needed to find.)
  - generate (LLM, one batched call): a generalized title per MULTIDATE_TITLE_RULE — never a single
    leg's day; reflect the span; keep the subject + a "(... series)" qualifier.
  - validate (deterministic): reject any output that still names a specific day, drops the subject,
    or is empty; those keep their ORIGINAL question and are FLAGGED for review (never silently mangled).

Idempotent: an event whose question no longer carries a specific day is already general -> skipped
(unless --force). Writes web/data/_retitle-report.json (before/after + flagged) for review.

Build chain: runs in build-data.sh AFTER fix_questions (raw fallback) and BEFORE patch_ladders
(strike-ladder metric labels). Also runnable standalone for a one-off backfill against any bundle:
    python3 retitle_multidate_events.py            # write
    python3 retitle_multidate_events.py --dry-run  # preview, no writes
    python3 retitle_multidate_events.py --force    # re-title even already-general events
"""
import sys, json, re
from pathlib import Path
from collections import defaultdict

from gen_news_cycle import claude_json  # loads .env, Anthropic client, strict-JSON helper

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
REPORT = ROOT / "web/data/_retitle-report.json"
DRY = "--dry-run" in sys.argv
FORCE = "--force" in sys.argv

# A SPECIFIC calendar day in the title = "Month DD" (optionally ", YYYY") or M/D. Year-only
# ("in 2026") and quarter ("Q1 2026") do NOT match — those are already general, leave them.
DAY_RE = re.compile(
    r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+\d{1,2}\b"
    r"|\b\d{1,2}/\d{1,2}\b",
    re.I,
)

MULTIDATE_TITLE_RULE = (
    "You are titling a prediction-market EVENT that bundles several deadline/date legs of the SAME "
    "underlying question (a 'series'). The current title names ONE leg's specific day, which is WRONG "
    "because the legs span multiple dates. Rewrite it as a GENERAL title for the whole series:\n"
    "- NEVER name a single leg's specific calendar day (no 'March 31', no 'by Jun 30').\n"
    "- Keep the exact subject/claim wording; generalize ONLY the time horizon.\n"
    "- Convey that it is a multi-deadline series and its span. Prefer 'in <year>?' when every leg "
    "falls in one calendar year; use '<startyear>-<endyear>?' when they cross years. Append a cadence "
    "qualifier when obvious: '(quarterly series)', '(monthly series)', otherwise '(multi-deadline series)'.\n"
    "- Concise (<= 80 chars). Keep a leading 'Will' only if the original had one.\n"
    "Examples:\n"
    "  'Bitcoin all time high by March 31, 2026?' (legs Mar/Jun/Sep/Dec 2026) -> "
    "'Bitcoin all-time high in 2026? (quarterly series)'\n"
    "  'MicroStrategy sells any Bitcoin by May 31, 2026?' (legs through Jan 2027) -> "
    "'MicroStrategy sells any Bitcoin? (deadline series, 2026-2027)'\n"
    "  'Will any country leave NATO by June 30, 2026?' (legs through Dec 2026) -> "
    "'Will any country leave NATO in 2026? (deadline series)'"
)


def day(s):
    return (s or "")[:10]


def main():
    bundle = json.loads(BUNDLE.read_text())
    by_ev = defaultdict(list)
    for m in bundle["markets"]:
        if m.get("event_id"):
            by_ev[m["event_id"]].append(m)

    todo = []
    for e in bundle["events"]:
        mk = by_ev.get(e["event_id"], [])
        dates = sorted({day(m.get("resolve_at") or m.get("close_at"))
                        for m in mk if (m.get("resolve_at") or m.get("close_at"))})
        if len(dates) <= 1:
            continue                                  # single-date event — not a series
        q = e.get("question") or ""
        if not DAY_RE.search(q) and not FORCE:
            continue                                  # already general (no specific day) — skip
        legs = sorted({(m.get("question_raw") or "").strip() for m in mk if m.get("question_raw")})
        todo.append({
            "event_id": e["event_id"],
            "question": q,
            "leg_questions": legs[:12],
            "leg_span": [dates[0], dates[-1]],
            "n_dates": len(dates),
        })

    print(f"{len(todo)} multi-date events to re-title", flush=True)
    if not todo:
        REPORT.write_text(json.dumps({"updated": [], "flagged": []}, indent=2))
        return

    system = ("You generalize mis-titled multi-date prediction-market event titles. "
              + MULTIDATE_TITLE_RULE
              + ' Return STRICT JSON only: {"titles":[{"event_id":"<id>","title":"<general title>"}]} '
                "with exactly one entry per input event_id.")
    user = ("Generalize each event title. leg_questions shows the individual legs; leg_span is the "
            "earliest->latest resolution date.\n\n" + json.dumps(todo, indent=2))
    result = claude_json(system, user, max_tokens=min(90 * len(todo) + 1200, 16000))
    new = {t["event_id"]: (t.get("title") or "").strip()
           for t in result.get("titles", []) if t.get("event_id")}

    ev_by_id = {e["event_id"]: e for e in bundle["events"]}
    report = {"updated": [], "flagged": []}
    for t in todo:
        eid, orig = t["event_id"], t["question"]
        title = new.get(eid, "")
        # VALIDATION (deterministic): non-empty, no specific day survived, plausibly long enough.
        if not title or DAY_RE.search(title) or len(title) < 8:
            report["flagged"].append({"event_id": eid, "question": orig,
                                      "proposed": title, "reason": "failed validation (empty / day survived)"})
            continue
        report["updated"].append({"event_id": eid, "old": orig, "new": title})
        if not DRY:
            ev_by_id[eid]["question"] = title

    if not DRY:
        BUNDLE.write_text(json.dumps(bundle, separators=(",", ":")))
    REPORT.write_text(json.dumps(report, indent=2))
    print(f"  re-titled {len(report['updated'])}; flagged {len(report['flagged'])} for review -> {REPORT.name}"
          + ("  [DRY-RUN, no write]" if DRY else ""))
    for u in report["updated"][:10]:
        print(f"   {u['old']!r}\n     -> {u['new']!r}")
    for f in report["flagged"][:5]:
        print(f"   FLAGGED {f['question']!r} -> {f['proposed']!r}")


if __name__ == "__main__":
    main()
