#!/usr/bin/env python3
"""
apply_exchange_notices.py — fold Kalshi important_info banners into the live -linked bundle.

Kalshi runs page banners (series product_metadata.important_info) for resolution-mechanics
notices — source-feed transitions, source-reading instructions. Sparse (~3% of series),
resolution-relevant when present. Until 2026-08-04 the pipeline never read the field, so a
committed source contradicted by the venue's own notice graded clean (Burke gold case:
settlement_sources says Pyth Metal.XAU/USD; banner says resolution moves to
Metal.Index.GOLD/USD).

Three channels (agreed 2026-08-04, methodology v3.7; hardened same day after swarm review):
  1. corpus  — the notice is resolution text: a labeled EXCHANGE NOTICE block is PREPENDED
               to resolution_rules_raw (prepended, not appended: enhance.llm_rcg_factors
               truncates the corpus at 1800 chars, and an appended block fell past the cut
               on long-rules series — 18/111 events' Haiku calls never saw it).
  2. cap     — deterministic conflict check: notice names a source/feed identifier absent
               from the committed settlement source -> market.source_notice_conflict=True
               -> classify grade cap `exchange_notice_source_conflict` (ceiling C).
  3. record  — the notice is stored whole on each affected market as `exchange_notice`
               (INTERNAL bundle field by decision 2026-08-04: not served by D1/API/site
               until the amendment-history exposure decision, ~Sep 2026).

Lifecycle correctness (swarm findings, all fixed here):
  - a CHANGED notice replaces the old block (strip-and-replace on markers, never append-once);
  - a REMOVED notice clears exchange_notice/source_notice_conflict, strips the block, and
    regrades the event (previously a withdrawn notice capped a market C forever);
  - series lookup is longest-prefix against known series tickers (hyphenated series like
    KXNEWOUTBREAK-P break naive split('-')[0]);
  - the regrade rebuilds the m["rcg"] audit blob (grade/caps/factors) so the audit never
    contradicts the served grade.

Affected events are re-graded with the SAME code path regrade_rcg.py uses
(enhance.llm_rcg_factors + classify.grade_market).

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

ROOT   = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
UNIV   = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-07-23"
SRCS   = UNIV / "series-sources.json"
BACKUP = ROOT / f"web/data/universe-enriched-linked.pre-notices-{date.today().isoformat()}-bak.json"
DRY    = "--dry" in sys.argv

NOTICE_MARK = "EXCHANGE NOTICE (venue page banner"
NOTICE_END  = "[END EXCHANGE NOTICE]"

# feed-identifier shapes: Pyth-style dotted pairs (Metal.Index.GOLD/USD), bare slash pairs
# (XAU/USD), underscore stream ids (HYPEUSD_RTI, U_HYPEUSD_RTI — the CF Benchmarks shape the
# first regex missed on a REAL live transition notice), and URLs. Deliberately NO bare-numeric
# "ID 1234" shape: a numeric id never appears in the committed source string, so it would flag
# a conflict forever even after the committed source is updated to match the notice.
_ID_PAT = re.compile(
    r"(?:[A-Za-z][\w]*\.){1,3}[A-Z0-9]{2,}/[A-Z0-9]{2,}"   # Metal.Index.GOLD/USD
    r"|\b[A-Z]{3,5}/[A-Z]{3,5}\b"                            # XAU/USD
    r"|\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b"                    # HYPEUSD_RTI / U_HYPEUSD_RTI
    r"|https?://\S+"                                          # any URL
)
# 'resol' (not 'resolut') so 'resolve/resolves/resolving' pass the gate — real Kalshi banner
# language ("will resolve this market to 'Yes'"); 'determin' for "determined by".
_RESOLUTION_KEY = re.compile(r"resol|settle|source|feed|determin", re.I)
_JUNK = "*.,);:!?'\"`>]"   # markdown/punctuation tails on extracted identifiers


def _norm_committed(name: str, url: str) -> str:
    return f"{name or ''} {url or ''}".lower().replace("%2f", "/")


def notice_conflict(notice_text: str, committed_name: str, committed_url: str) -> bool:
    """True when the banner names a source/feed identifier not present in the committed
    settlement source. Deterministic by design — judgment cases go to the LLM corpus instead."""
    if not _RESOLUTION_KEY.search(notice_text):
        return False
    committed = _norm_committed(committed_name, committed_url)
    for ident in _ID_PAT.findall(notice_text):
        ident_n = ident.rstrip(_JUNK).lower().replace("%2f", "/")
        if ident_n.startswith("http"):
            # compare on the feed slug: last TWO path segments (Pyth slugs contain a literal
            # slash — last-one collapsed Metal.Index.GOLD/USD to a vacuous 'usd')
            segs = [s for s in ident_n.split("/") if s]
            ident_n = "/".join(segs[-2:]) if len(segs) >= 2 else ident_n
        if ident_n and ident_n not in committed:
            return True
    return False


def strip_notice(rules: str) -> str:
    """Remove any EXCHANGE NOTICE block — new marker-delimited form or the legacy
    appended-at-end form — leaving the venue rules text untouched."""
    if not rules or NOTICE_MARK not in rules:
        return rules or ""
    # marker-delimited (prepended) form
    pat_new = re.compile(r"EXCHANGE NOTICE \(venue page banner.*?\[END EXCHANGE NOTICE\]\s*",
                         re.S)
    rules = pat_new.sub("", rules)
    # legacy appended form: block ran from the mark to end-of-text
    idx = rules.find(NOTICE_MARK)
    if idx != -1:
        rules = rules[:idx]
    return rules.strip()


def notice_block(st: str, ii: dict) -> str:
    return (f"{NOTICE_MARK}, series {st}, notice id {ii.get('id')}):\n"
            f"{ii['text']}\n{NOTICE_END}\n\n")


def build_series_lookup(series_keys) -> dict:
    """first-segment -> [series tickers with that first segment], longest first —
    so KXNEWOUTBREAK-P wins over a bogus KXNEWOUTBREAK for market KXNEWOUTBREAK-P-26."""
    by_seg: dict[str, list[str]] = {}
    for k in series_keys:
        by_seg.setdefault(k.split("-")[0], []).append(k)
    for seg in by_seg:
        by_seg[seg].sort(key=len, reverse=True)
    return by_seg


def series_for(pmid: str, by_seg: dict) -> str | None:
    p = (pmid or "").upper()
    for k in by_seg.get(p.split("-")[0], []):
        if p == k or p.startswith(k + "-"):
            return k
    return None


def rebuild_audit(m: dict, rcg: dict) -> None:
    """Mirror enrich_universe.py's m['rcg'] audit blob so audit never contradicts grade."""
    commit_fp = (m.get("field_provenance") or {}).get("source_commitment", {}) or {}
    prev = m.get("rcg") or {}
    m["rcg"] = {"grade": rcg["grade"], "score": rcg["score"], "caps": rcg["caps"],
                "factors": rcg.get("factors"),
                "commitment": prev.get("commitment") or {
                    "class": m.get("source_commitment_subtype"),
                    "source_of_record": m.get("source_of_record"),
                    "mechanism": m.get("source_mechanism"),
                    "why": commit_fp.get("why"),
                    "fail_closed": bool(commit_fp.get("fail_closed"))}}


def main() -> None:
    import enhance as E
    from classify import grade_market

    srcs = json.loads(SRCS.read_text())
    noticed = {st: v for st, v in srcs.items() if v.get("important_info")}
    print(f"series with important_info: {len(noticed)} / {len(srcs)}")
    for st, v in sorted(noticed.items()):
        print(f"   {st} [{v['important_info'].get('id')}]: {v['important_info']['text'][:100]}")

    bundle = json.loads(BUNDLE.read_text())
    by_event: dict[str, list] = {}
    for m in bundle["markets"]:
        by_event.setdefault(m.get("event_id"), []).append(m)

    # known series = fetched series ∪ raw universe series (covers hyphenated tickers)
    raw_series = set(srcs.keys())
    raw_path = UNIV / "kalshi-institutional.json"
    if raw_path.exists():
        raw_series |= {e.get("series_ticker") for e in json.loads(raw_path.read_text())
                       if e.get("series_ticker")}
    by_seg = build_series_lookup(raw_series)

    touched: dict[str, str] = {}   # event_id -> reason
    n_marked = n_conflict = n_cleared = 0
    for m in bundle["markets"]:
        if m.get("platform") != "kalshi":
            continue
        st = series_for(m.get("platform_market_id"), by_seg)
        v = noticed.get(st) if st else None
        old_rules = m.get("resolution_rules_raw") or ""
        if v:
            ii = v["important_info"]
            committed = (v.get("sources") or [{}])[0]
            conflict = notice_conflict(ii["text"], committed.get("name"), committed.get("url"))
            new_rules = notice_block(st, ii) + strip_notice(old_rules)
            changed = (new_rules != old_rules
                       or bool(m.get("source_notice_conflict")) != conflict
                       or (m.get("exchange_notice") or {}).get("id") != ii.get("id"))
            m["exchange_notice"] = {**ii, "captured_at": date.today().isoformat(),
                                    "series_ticker": st}
            m["source_notice_conflict"] = conflict
            m["resolution_rules_raw"] = new_rules
            n_marked += 1
            n_conflict += bool(conflict)
            if changed and m.get("event_id"):
                touched[m["event_id"]] = "notice"
        elif m.get("exchange_notice") is not None or NOTICE_MARK in old_rules:
            # notice REMOVED (or series no longer carries one): clear everything and regrade —
            # otherwise a withdrawn notice caps the market C forever.
            m["exchange_notice"] = None
            m["source_notice_conflict"] = None
            m["resolution_rules_raw"] = strip_notice(old_rules) or None
            n_cleared += 1
            if m.get("event_id"):
                touched[m["event_id"]] = "cleared"

    print(f"\nmarkets annotated: {n_marked} (deterministic conflicts: {n_conflict}), "
          f"cleared: {n_cleared}; events to regrade: {len(touched)}")

    if DRY:
        print("--dry: nothing written")
        return

    if not BACKUP.exists():
        BACKUP.write_text(BUNDLE.read_text())
        print(f"backed up -> {BACKUP.name}")

    ev_by_id = {e["event_id"]: e for e in bundle["events"]}
    for eid, reason in touched.items():
        e = ev_by_id.get(eid)
        markets = by_event.get(eid, [])
        if not e or not markets:
            continue
        factors = E.llm_rcg_factors(e, markets)
        if not factors:
            print(f"   {eid}: no factors (skipped regrade)")
            continue
        e["rcg_factors"] = factors
        ratings = {k: v["rating"] for k, v in factors.items()}
        for m in markets:
            rcg = grade_market(m, m.get("resolution_rules_raw") or "", llm_ratings=ratings)
            old = m.get("resolution_clarity_grade")
            m["resolution_clarity_grade"] = rcg["grade"]
            m["rcg_score"], m["rcg_caps"] = rcg["score"], rcg["caps"]
            m["rcg_applied_factors"] = rcg.get("applied_factors")
            rebuild_audit(m, rcg)
            if old != rcg["grade"]:
                print(f"   {m['platform_market_id']}: {old} -> {rcg['grade']} caps={rcg['caps']}")

    BUNDLE.write_text(json.dumps(bundle))
    print(f"wrote {BUNDLE.name}")


if __name__ == "__main__":
    main()
