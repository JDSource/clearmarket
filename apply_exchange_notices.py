#!/usr/bin/env python3
"""
apply_exchange_notices.py — fold Kalshi important_info banners into the live -linked bundle.

Kalshi runs page banners (series product_metadata.important_info) for resolution-mechanics
notices — source-feed transitions, source-reading instructions. Sparse (~2% of series),
resolution-relevant when present. Until 2026-08-04 the pipeline never read the field, so a
committed source contradicted by the venue's own notice graded clean (Burke gold case:
settlement_sources says Pyth Metal.XAU/USD; banner says resolution moves to
Metal.Index.GOLD/USD).

Three channels (agreed 2026-08-04, methodology v3.7):
  1. corpus  — the notice is resolution text: append a labeled EXCHANGE NOTICE block to
               resolution_rules_raw so every LLM pass (source commitment, RCG factors) reads it.
  2. cap     — deterministic conflict check: notice names a source/feed identifier that is
               absent from the committed settlement source -> market.source_notice_conflict=True
               -> classify grade cap `exchange_notice_source_conflict` (ceiling C).
  3. record  — the notice is stored whole on each affected market as `exchange_notice`
               (payload-visible; nothing an LLM might miss is silently dropped).

Affected events are then re-graded with the SAME code path regrade_rcg.py uses
(enhance.llm_rcg_factors + classify.grade_market) — a handful of Haiku calls.

Usage:
  python3 apply_exchange_notices.py --dry    # show what would change, write nothing
  python3 apply_exchange_notices.py          # apply + regrade + write (dated backup first)
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

import enhance as E
from classify import grade_market

ROOT   = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
SRCS   = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-07-23/series-sources.json"
BACKUP = ROOT / f"web/data/universe-enriched-linked.pre-notices-{date.today().isoformat()}-bak.json"
DRY    = "--dry" in sys.argv

NOTICE_MARK = "EXCHANGE NOTICE (venue page banner"

# feed-identifier shapes: Pyth-style dotted pairs (Metal.Index.GOLD/USD), bare pairs
# (XAU/USD), URLs. Deliberately NO bare-numeric "ID 1234" shape: a numeric id never
# appears in the committed source string, so it would flag a conflict forever even after
# the committed source is updated to match the notice (permanent false positive).
_ID_PAT = re.compile(
    r"(?:[A-Za-z][\w]*\.){1,3}[A-Z0-9]{2,}/[A-Z0-9]{2,}"   # Metal.Index.GOLD/USD
    r"|\b[A-Z]{3,5}/[A-Z]{3,5}\b"                            # XAU/USD
    r"|https?://\S+"                                          # any URL
)
_RESOLUTION_KEY = re.compile(r"resolut|settle|source|feed", re.I)


def notice_conflict(notice_text: str, committed_name: str, committed_url: str) -> bool:
    """True when the banner names a source/feed identifier not present in the committed
    settlement source. Deterministic by design — judgment cases go to the LLM corpus instead."""
    if not _RESOLUTION_KEY.search(notice_text):
        return False
    committed = f"{committed_name or ''} {committed_url or ''}".lower()
    for ident in _ID_PAT.findall(notice_text):
        ident_n = ident.rstrip(".,)").lower()
        if ident_n.startswith("http"):
            # compare on path tail (the feed slug), not the whole URL
            ident_n = ident_n.split("/")[-1]
        if ident_n and ident_n.replace("%2f", "/") not in committed.replace("%2f", "/"):
            return True
    return False


def main() -> None:
    srcs = json.loads(SRCS.read_text())
    noticed = {st: v for st, v in srcs.items() if v.get("important_info")}
    print(f"series with important_info: {len(noticed)} / {len(srcs)}")
    for st, v in noticed.items():
        print(f"   {st} [{v['important_info'].get('id')}]: {v['important_info']['text'][:110]}")
    if not noticed:
        print("nothing to apply")
        return

    bundle = json.loads(BUNDLE.read_text())
    by_event: dict[str, list] = {}
    for m in bundle["markets"]:
        by_event.setdefault(m.get("event_id"), []).append(m)

    touched_events: dict[str, dict] = {}
    n_marked = n_conflict = 0
    for m in bundle["markets"]:
        if m.get("platform") != "kalshi":
            continue
        # -linked bundle drops platform_event_id; the market ticker's first segment IS the
        # series ticker (KXGOLDMON-26AUG3117-T4051.99 -> KXGOLDMON).
        st = (m.get("platform_market_id") or "").split("-")[0].upper()
        v = noticed.get(st)
        if not v:
            continue
        ii = v["important_info"]
        committed = (v.get("sources") or [{}])[0]
        conflict = notice_conflict(ii["text"], committed.get("name"), committed.get("url"))
        m["exchange_notice"] = {**ii, "captured_at": date.today().isoformat(),
                                "series_ticker": st}
        m["source_notice_conflict"] = conflict
        block = (f"\n\n{NOTICE_MARK}, series {st}, notice id {ii.get('id')}):\n{ii['text']}")
        if NOTICE_MARK not in (m.get("resolution_rules_raw") or ""):
            m["resolution_rules_raw"] = (m.get("resolution_rules_raw") or "") + block
        n_marked += 1
        n_conflict += bool(conflict)
        if m.get("event_id"):
            touched_events[m["event_id"]] = None

    for e in bundle["events"]:
        if e["event_id"] in touched_events:
            touched_events[e["event_id"]] = e
    work = [(e, by_event.get(eid, [])) for eid, e in touched_events.items() if e]
    print(f"\nmarkets annotated: {n_marked} (deterministic conflicts: {n_conflict}) "
          f"across {len(work)} events")

    if DRY:
        print("--dry: nothing written")
        return

    if not BACKUP.exists():
        BACKUP.write_text(BUNDLE.read_text())
        print(f"backed up -> {BACKUP.name}")

    for e, markets in work:
        factors = E.llm_rcg_factors(e, markets)
        if not factors:
            print(f"   {e['event_id']}: no factors (skipped regrade)")
            continue
        e["rcg_factors"] = factors
        ratings = {k: v["rating"] for k, v in factors.items()}
        for m in markets:
            rcg = grade_market(m, m.get("resolution_rules_raw") or "", llm_ratings=ratings)
            old = m.get("resolution_clarity_grade")
            m["resolution_clarity_grade"] = rcg["grade"]
            m["rcg_score"], m["rcg_caps"] = rcg["score"], rcg["caps"]
            m["rcg_applied_factors"] = rcg.get("applied_factors")
            if old != rcg["grade"]:
                print(f"   {m['platform_market_id']}: {old} -> {rcg['grade']} caps={rcg['caps']}")

    BUNDLE.write_text(json.dumps(bundle))
    print(f"wrote {BUNDLE.name}")


if __name__ == "__main__":
    main()
