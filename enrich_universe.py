#!/usr/bin/env python3
"""
ClearMarket — universe enrichment (adapts enhance.py to the fetched universe).

Consumes the institutional universe produced by fetch_universe.py and builds CM
event/market/mark records with:
  - the 9-category enum (from each event's _cm.category)
  - the renamed field `resolution_source_type` (was `source_type`)
  - PER-EVENT enrichment: underlying_reference is computed ONCE per event from a
    representative market and shared to all child markets (a 400-strike ladder
    costs one call, not 400). editorial_notes / tags / canonical question are
    per-event by nature.

Reuses enhance.py's prompts + LLM cache + cost tracking so cost is measured, not
guessed. Run with --sample to enrich a handful of events (cents) and read the
real per-event cost, then project to the full universe before any paid run.

Usage:
  python3 enrich_universe.py --sample 10            # 10 events/venue, measure cost
  python3 enrich_universe.py --sample 10 --no-llm   # structure only, $0
  python3 enrich_universe.py                         # full universe (the paid run)

Data-completeness TODOs (not cost-relevant, do in a later pass):
  - Kalshi resolution_source/source_citation come from SERIES settlement_sources,
    not fetched here → currently left null; needs a per-series fetch.
  - resolution_source_type classification (gov_stat_agency / central_bank /
    regulated_data_vendor / subjective ...) not yet derived → defaulted to null.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import enhance as E  # reuse llm_call, prompts, cache, cost stats, helpers
from classify import (CATEGORIES_IN, grade_market, classify_bundle_type,
                     parse_ladder_deadline)

UNIVERSE_DIR = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-06-12"
OUT_DIR      = Path.home() / "jeremy-os/outputs/clearmarket/samples-universe"
RUN_AT       = datetime.now(timezone.utc).isoformat()


def _load_map(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}

# Verified-source maps (direct tier). Built by fetch_kalshi_series_sources.py + fetch_poly_sources.py.
KALSHI_SRC = _load_map(UNIVERSE_DIR / "series-sources.json")  # series_ticker -> {sources, quality}
POLY_SRC   = _load_map(UNIVERSE_DIR / "poly-sources.json")    # event key -> {source_url, source, verified, method}


# -----------------------------------------------------------------
# Structure builders (lean; marks from nested fields, no CLOB calls)
# -----------------------------------------------------------------
def _kalshi_status(s: str) -> str:
    return {"active": "open", "open": "open", "closed": "closed",
            "settled": "resolved", "resolved": "resolved", "finalized": "resolved"}.get(s or "", "open")


def build_kalshi_market(m: dict, event_id: str, src: dict | None = None) -> dict:
    rules = "\n\n".join(filter(None, [m.get("rules_primary"), m.get("rules_secondary")]))
    ksrc = (src or {}).get("sources") or []
    mk = {
        "market_id":             E.generate_market_id("kalshi:" + (m.get("ticker") or m.get("title") or "")),
        "platform":              "kalshi",
        "platform_market_id":    m.get("ticker"),
        "event_id":              event_id,
        "question_raw":          m.get("title"),
        "description_raw":       m.get("yes_sub_title") or m.get("subtitle"),
        "group_item_title":      m.get("yes_sub_title") or m.get("subtitle"),   # per-child subject (compose)
        "contract_type":         "binary",
        "settlement_currency":   "USD",
        "underlying_reference":  E.EDITORIAL_STUB,   # filled per-event below (editorial gloss)
        "close_at":              m.get("close_time"),
        "resolve_at":            m.get("expected_expiration_time") or m.get("expiration_time"),
        "_expiration_time":          m.get("expiration_time"),           # native per-rung (ladder reconcile)
        "_expected_expiration_time": m.get("expected_expiration_time"),  # rollup estimate
        "status":                _kalshi_status(m.get("status")),
        "resolution_rules_raw":  rules or None,
        "arbitration_model":     "kalshi_staff",
        "resolution_proposer":   "platform_staff",
        # DIRECT tier — from series settlement_sources (series-sources.json).
        # DISPLAY stays the venue's verbatim field (first entry) per the "show the source in the
        # venue's own words" methodology. PRESERVE the full list ONLY for independent grading, so
        # a multi-outlet 'credible-reporting menu' can be classified as uncommitted without altering
        # what the reader sees.
        "resolution_source":     ksrc[0]["name"] if ksrc else None,   # verbatim venue field
        "source_citation":       ksrc[0]["url"] if ksrc else None,
        # per-entry provenance (PRD taxonomy): a venue-listed source = platform_api; LLM-surfaced
        # prose authorities are appended at enrichment as clearmarket_editorial (enrich_event)
        "resolution_source_list":       [{"name": s.get("name"), "url": s.get("url"),
                                          "provenance": "platform_api"} for s in ksrc] or None,
        "resolution_source_count":      len(ksrc) or None,
        "resolution_source_provenance": "kalshi_series_settlement_sources" if ksrc else None,
        "resolution_source_quality":    (src or {}).get("quality"),   # venue self-tag — NOT trusted for grading
        "resolution_source_type": None,             # RENAMED from source_type; TODO: classify
        "last_price":            E._to_float(m.get("last_price_dollars")),
        "volume_24h_usd":        E._mult(m.get("volume_24h_fp"), E._to_float(m.get("last_price_dollars"))),
        "volume_total_usd":      E._mult(m.get("volume_fp"), E._to_float(m.get("last_price_dollars"))),
    }
    rcg = grade_market(mk, rules)
    mk["resolution_clarity_grade"] = rcg["grade"]
    mk["rcg_score"], mk["rcg_caps"] = rcg["score"], rcg["caps"]
    return mk


def build_poly_market(m: dict, event_id: str, src: dict | None = None) -> dict:
    psrc = src or {}
    # Canonical full source list (source-layer refactor 2026-07-03). Previously Poly collapsed to
    # ONE extracted URL and resolution_source_list was never populated — the grading judge could
    # not tell a committed authority from a menu, and 92% of Poly (empty resolutionSource) was
    # force-capped "none". Entries: the venue's structured resolutionSource field (if any) + ALL
    # regex-extracted URL candidates. Prose-named authorities are appended at enrichment.
    rs_prose = (m.get("resolutionSource") or "").strip() or None
    src_list = ([{"name": rs_prose, "url": None, "provenance": "platform_api"}] if rs_prose else []) \
             + [{"name": None, "url": u, "provenance": "platform_api"}
                for u in (psrc.get("candidates") or [])]
    mk = {
        "market_id":             E.generate_market_id("polymarket:" + (m.get("conditionId") or m.get("id") or m.get("question") or "")),
        "platform":              "polymarket",
        "platform_market_id":    m.get("conditionId") or m.get("id"),
        "event_id":              event_id,
        "question_raw":          m.get("question"),
        "description_raw":       (m.get("description") or "")[:600] or None,
        "group_item_title":      m.get("groupItemTitle"),   # per-child subject (compose)
        "contract_type":         "binary",
        "settlement_currency":   "USDC",
        "underlying_reference":  E.EDITORIAL_STUB,   # filled per-event below (editorial gloss)
        "close_at":              m.get("endDate"),
        # child's OWN native settlement date (prefer umaEndDate); never the event rollup — Family-B fix
        "resolve_at":            m.get("umaEndDate") or m.get("endDate"),
        "status":                "open" if (m.get("active") and not m.get("closed")) else "closed",
        "resolution_rules_raw":  (m.get("description") or None),
        "arbitration_model":     "uma_oracle",
        "resolution_proposer":   "managed_whitelist",
        # DIRECT (verified) tier — URLs extracted verbatim from the market description (poly-sources.json)
        "resolution_source":     rs_prose,                    # verbatim venue field (display)
        "source_citation":       psrc.get("source_url"),      # single-URL case; multi-URL selected by the commitment call
        "resolution_source_list":       src_list or None,
        "resolution_source_count":      len(src_list) or None,
        "resolution_source_provenance": psrc.get("source"),   # polymarket_description | subjective_or_none
        "resolution_source_verified":   psrc.get("verified"),
        "resolution_source_method":     psrc.get("method"),
        "resolution_source_type": None,             # RENAMED from source_type; TODO: classify
        "last_price":            E._to_float(m.get("lastTradePrice")),
        "volume_24h_usd":        E._to_float(m.get("volume24hr")),
        "volume_total_usd":      E._to_float(m.get("volume")),
    }
    rcg = grade_market(mk, m.get("description") or "")
    mk["resolution_clarity_grade"] = rcg["grade"]
    mk["rcg_score"], mk["rcg_caps"] = rcg["score"], rcg["caps"]
    return mk


def build_cm_event(ev: dict, venue: str) -> tuple[dict, list[dict]]:
    cm = ev.get("_cm", {})
    if venue == "kalshi":
        seed = ev.get("event_ticker") or ev.get("title", "")
        slug = (ev.get("event_ticker") or "").lower()
        question = ev.get("title") or ev.get("sub_title") or seed
        src = KALSHI_SRC.get(ev.get("series_ticker"))
        markets = [build_kalshi_market(m, "", src) for m in (ev.get("markets") or [])]
    else:
        seed = ev.get("slug") or ev.get("id") or ev.get("title", "")
        slug = ev.get("slug") or ""
        question = ev.get("title") or seed
        src = POLY_SRC.get(str(ev.get("id") or ev.get("slug")))
        markets = [build_poly_market(m, "", src) for m in (ev.get("markets") or [])]

    event_id = E.generate_event_id(str(seed))
    for m in markets:
        m["event_id"] = event_id

    # representative market = highest cumulative volume (for the per-event underlying_reference)
    rep = max(markets, key=lambda x: (x.get("volume_total_usd") or 0), default=None) if markets else None
    primary_market_id = rep["market_id"] if rep else None

    event = {
        "event_id":          event_id,
        "slug":              slug,
        "question":          question,
        "category":          cm.get("category"),          # 9-enum
        "tags":              cm.get("mapped_tags") or [],
        "primary_market_id": primary_market_id,
        "bundle_type":       classify_bundle_type(ev, venue),   # categorical|date_ladder|strike_ladder|augmented_negrisk|singleton
        "catalyst_dates":    [],
        "published":         True,
        "venue":             venue,
        "editorial_notes":   E.EDITORIAL_STUB,
        "resolution_reference": E.EDITORIAL_STUB,   # generic subject-free event ontology (filled per-event below)
        "created_at":        RUN_AT,
        "updated_at":        RUN_AT,
        "field_provenance":  {"question": {"source": "platform_api"}},  # lets canonical-question rewrite fire
    }
    _reconcile_ladder_dates(event, markets)   # Family-B: per-rung dates (runs even with LLM off)
    return event, markets


def _reconcile_ladder_dates(event: dict, markets: list[dict]) -> None:
    """Family-B fix. For date ladders, make each rung carry its OWN deadline instead of
    the event rollup: (1) prefer Kalshi's native per-rung `expiration_time`; (2) if the
    ladder's dates are still degenerate (all identical — the Poly fed-rate case where the
    venue copies one endDate to every child), derive each rung's date from its title."""
    if event.get("bundle_type") not in ("date_ladder", "strike_ladder") or len(markets) < 2:
        return
    # (1) Kalshi: rollup estimate was preferred in the builder; swap to native per-rung
    for m in markets:
        if m.get("_expiration_time"):
            m["resolve_at"] = m["_expiration_time"]
            m.setdefault("field_provenance", {})["resolve_at"] = {"source": "native:expiration_time"}
    # (2) title-derive is DATE ladders ONLY — a strike rung title ('$2050', 'above 2000') looks
    #     like a year and must never be parsed as a date. Also: ignore None when testing degeneracy
    #     (a single null-date child must not mask a genuinely degenerate ladder).
    if event.get("bundle_type") != "date_ladder":
        return
    nonnull = {d for d in (m.get("resolve_at") for m in markets) if d}
    if len(nonnull) <= 1:
        yr = None
        for d in nonnull:
            mm = re.search(r"(20\d{2})", str(d))
            if mm:
                yr = int(mm.group(1)); break
        for m in markets:
            derived = parse_ladder_deadline(m.get("group_item_title"), year_hint=yr)
            if derived:
                m["resolve_at"] = derived
                m.setdefault("field_provenance", {})["resolve_at"] = {"source": "derived:group_item_title"}


# -----------------------------------------------------------------
# Per-event enrichment (the refactor: underlying_reference ONCE per event)
# -----------------------------------------------------------------
def _stamp_child_provenance(m: dict, source: str) -> None:
    fp = m.setdefault("field_provenance", {})
    fp["underlying_reference"] = {"source": source}


def _subject_leaks(ontology: str, subjects: list[str]) -> list[str]:
    """The event ontology must be SUBJECT-FREE, so ANY child subject appearing in it is a leak —
    INCLUDING the representative child's own subject (the ontology is generated from the rep's
    question, so its subject, e.g. 'SpaceX', is the single most likely thing to leak). Word-boundary
    match so 'Ripple' does not false-match inside 'Ripple Labs'."""
    onto_l = ontology or ""
    out = []
    for s in subjects:
        s = (s or "").strip()
        if not s or len(s) <= 3:
            continue
        if re.search(r"\b" + re.escape(s) + r"\b", onto_l, re.I):
            out.append(s)
    return out


def enrich_event(event: dict, markets: list[dict], enabled: bool) -> None:
    if not enabled or not markets:
        return
    rep = next((m for m in markets if m["market_id"] == event.get("primary_market_id")), markets[0])
    bundle_type = event.get("bundle_type", "singleton")

    # Family-A fix: settlement defined ONCE at the event (OCC class->series), inherited.
    try:
        if bundle_type == "singleton" or len(markets) == 1:
            # single outcome: the ref legitimately names its own (only) subject
            ref = E.llm_underlying_reference(rep)
            markets[0]["underlying_reference"] = ref
            _stamp_child_provenance(markets[0], "clearmarket_editorial")
        else:
            # multi-outcome: 1 call for a GENERIC subject-free ontology (the ladder saving,
            # kept), stored on the event; each child's ref composed from its OWN subject so
            # no sibling's identity ever leaks (kills the SpaceX/Anthropic broadcast bug).
            ontology = E.llm_event_resolution_ontology(rep)
            subjects = [(m.get("group_item_title") or "").strip() for m in markets]

            # Leak guard WITH ACTION: if the generic ontology contains ANY child subject (incl.
            # the rep's own), do not ship it — fall back to neutral phrasing + flag for review.
            leaked = _subject_leaks(ontology, subjects)
            if leaked:
                # keep the leaked draft inside provenance (not a new top-level field) for review
                event.setdefault("field_provenance", {})["subject_leak"] = {
                    "flag": True, "leaked": leaked, "raw_ontology": ontology}
                ontology = "Resolution per the event's stated source and mechanism (subject supplied per market)."
                print(f"    subject_leak in {event['event_id']}: {leaked!r} -> fell back to neutral ontology",
                      file=sys.stderr)

            event["resolution_reference"] = ontology
            src = "clearmarket_editorial_fallback" if leaked else "clearmarket_editorial"
            event.setdefault("field_provenance", {})["resolution_reference"] = {"source": src}
            for m in markets:
                m["underlying_reference"] = E.compose_child_reference(m.get("group_item_title"), ontology)
                _stamp_child_provenance(m, "composed:event+child")
    except Exception as e:
        print(f"    underlying_reference failed for {event['event_id']}: {e}", file=sys.stderr)

    try:
        event["editorial_notes"] = E.llm_editorial_notes(event, markets)
    except Exception as e:
        print(f"    editorial_notes failed for {event['event_id']}: {e}", file=sys.stderr)
    try:
        tags = E.llm_tags(event, markets)
        if tags:
            event["tags"] = tags
    except Exception as e:
        print(f"    tags failed for {event['event_id']}: {e}", file=sys.stderr)
    try:
        q = E.llm_canonical_question(event, markets)
        if q:
            event["question"] = q
    except Exception as e:
        print(f"    question failed for {event['event_id']}: {e}", file=sys.stderr)

    # Source commitment: one per-event LLM classification (the reading-comprehension judgment that
    # REPLACES the retired patch_sources deterministic regexes). MUST run before grading so the
    # commitment cap is on the market. rep carries the series/event source; commitment is a
    # property of the source, so it applies to every market in the event (per-event keying
    # verified safe 2026-07-03: 790/795 multi-market Poly events have uniform child sources).
    try:
        sc = E.llm_source_commitment(rep)
    except Exception as e:
        print(f"    source_commitment errored for {event['event_id']}: {e}", file=sys.stderr)
        sc = None
    if sc is None:
        # FAIL CLOSED (spec B1): never ship an uncapped grade on a failed judgment.
        sc = {"commitment": "uncommitted_placeholder", "source_of_record": None, "mechanism": None,
              "primary_url": None, "prose_sources": [],
              "why": "commitment judgment failed; capped fail-closed",
              "rubric_version": E.SOURCE_RUBRIC_VERSION, "_fail_closed": True}
        print(f"    source_commitment FAIL-CLOSED for {event['event_id']}", file=sys.stderr)
    top = ("named" if sc["commitment"] == "named"
           else "none" if sc["commitment"] == "none" else "uncommitted")
    # LLM-surfaced prose authorities (verbatim-gated in enhance) join the canonical source
    # list as editorial-tier entries — visible on every surface, not just baked into the grade.
    prose_entries = [{"name": p, "url": None, "provenance": "clearmarket_editorial"}
                     for p in sc.get("prose_sources") or []]
    for m in markets:
        if prose_entries:
            existing = m.get("resolution_source_list") or []
            have = {(e.get("name") or "").strip().lower() for e in existing}
            add = [e for e in prose_entries if e["name"].strip().lower() not in have]
            if add:
                m["resolution_source_list"] = existing + add
                m["resolution_source_count"] = len(m["resolution_source_list"])
        # multi-URL Poly case: the commitment call selected the controlling URL by index
        if not m.get("source_citation") and sc.get("primary_url"):
            m["source_citation"] = sc["primary_url"]
        m["source_commitment"] = top
        m["source_commitment_subtype"] = sc["commitment"]
        m["source_of_record"] = sc.get("source_of_record")   # the committed authority (also displayed in the source table)
        m["source_mechanism"] = sc.get("mechanism")          # single_authority | precedence | quorum
        # THE stamped judgment — every surface reads this; no consumer re-derives from raw
        # field presence (kills the platform_named-on-a-hedge display bug at the root).
        m["source_status"] = ("platform_named" if top == "named"
                              else "no_source_stated" if top == "none"
                              else "no_committed_source")
        m.setdefault("field_provenance", {})["source_commitment"] = {
            "source": "clearmarket_editorial", "ai_drafted": True, "why": sc.get("why"),
            "rubric_version": sc.get("rubric_version"),
            **({"fail_closed": True} if sc.get("_fail_closed") else {})}

    # RCG: one per-event Haiku rating of the LLM factors → grade every market (the commitment cap
    # from above folds into grade_market). Stores a self-contained audit object per market.
    try:
        factors = E.llm_rcg_factors(event, markets)
        if factors:
            event["rcg_factors"] = factors
            ratings = {f: d["rating"] for f, d in factors.items()}
            for m in markets:
                rcg = grade_market(m, m.get("resolution_rules_raw") or "", llm_ratings=ratings)
                m["resolution_clarity_grade"] = rcg["grade"]
                m["rcg_score"], m["rcg_caps"] = rcg["score"], rcg["caps"]
                m["rcg_applied_factors"] = rcg.get("applied_factors")
                # the full audit object — every value the grade derives from, incl. the
                # commitment's written why and whether it was a fail-closed default (so a
                # buyer-facing surface can distinguish "venue committed to nothing" from
                # "our judgment failed and we capped conservatively")
                commit_fp = (m.get("field_provenance") or {}).get("source_commitment", {})
                m["rcg"] = {"grade": rcg["grade"], "score": rcg["score"], "caps": rcg["caps"],
                            "factors": rcg.get("factors"),
                            "commitment": {"class": m.get("source_commitment_subtype"),
                                           "source_of_record": m.get("source_of_record"),
                                           "mechanism": m.get("source_mechanism"),
                                           "why": commit_fp.get("why"),
                                           "fail_closed": bool(commit_fp.get("fail_closed")),
                                           "rubric_version": E.SOURCE_RUBRIC_VERSION}}
    except Exception as e:
        print(f"    rcg_factors failed for {event['event_id']}: {e}", file=sys.stderr)


# -----------------------------------------------------------------
# Cost report + projection
# -----------------------------------------------------------------
def _cost_summary(events_done: int, universe_total: int) -> None:
    PRICING = {E.LLM_MODEL_HAIKU: {"in": 1.0, "out": 5.0},
               E.LLM_MODEL_SONNET: {"in": 3.0, "out": 15.0}}
    total = 0.0
    print("\n" + "=" * 60)
    for model, s in E._llm_stats.items():
        p = PRICING.get(model, {"in": 1.0, "out": 5.0})
        cost = s["input_tokens"] / 1e6 * p["in"] + s["output_tokens"] / 1e6 * p["out"]
        total += cost
        print(f"{model.split('-')[1]:7}: {s['calls']:3} new calls, {s['cache_hits']:3} cached  "
              f"in={s['input_tokens']:,} out={s['output_tokens']:,}  ${cost:.4f}")
    per_event = total / events_done if events_done else 0
    print(f"\nSample: {events_done} events  →  ${total:.4f}  (${per_event:.4f}/event)")
    print(f"PROJECTION @ ${per_event:.4f}/event:")
    for label, n in [("full broad universe", universe_total), ("~$50k threshold (~700)", 700),
                     ("~$250k threshold (~280)", 280)]:
        print(f"   {label:28}: {n:>5} events  ≈  ${per_event * n:6.2f}")
    print("=" * 60)


# -----------------------------------------------------------------
# Main
# -----------------------------------------------------------------
def main() -> None:
    from collections import defaultdict
    enabled = "--no-llm" not in sys.argv
    sample = per_cat = None
    if "--sample" in sys.argv:
        sample = int(sys.argv[sys.argv.index("--sample") + 1])
    if "--per-category" in sys.argv:
        per_cat = int(sys.argv[sys.argv.index("--per-category") + 1])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = {"kalshi": UNIVERSE_DIR / "kalshi-institutional.json",
             "polymarket": UNIVERSE_DIR / "poly-institutional.json"}

    tagged, universe_total = [], 0   # tagged = list of (venue, event)
    for venue, path in files.items():
        evs = json.loads(path.read_text())
        universe_total += len(evs)
        tagged += [(venue, ev) for ev in evs]

    if per_cat:
        by_cat = defaultdict(list)
        for venue, ev in tagged:
            by_cat[ev.get("_cm", {}).get("category")].append((venue, ev))
        todo = []
        for cat in CATEGORIES_IN:
            todo += by_cat.get(cat, [])[:per_cat]
        out_name = "per-category-sample.json"
        print(f"selecting {per_cat}/category across {len(CATEGORIES_IN)} categories -> {len(todo)} events", flush=True)
    elif sample:
        todo = [t for t in tagged if t[0] == "kalshi"][:sample] + \
               [t for t in tagged if t[0] == "polymarket"][:sample]
        out_name = "universe-enriched-sample.json"
    else:
        todo = tagged
        out_name = "universe-enriched-full.json"

    # Phase 1 — build sequentially (assigns CM-EVT-/CM-MKT- IDs race-free, no LLM)
    print(f"building {len(todo)} events...", flush=True)
    built = [build_cm_event(ev, venue) for venue, ev in todo]

    # Phase 2 — enrich concurrently (LLM calls are I/O-bound; ~6 workers, cache makes retries free)
    print(f"enriching {len(built)} events ({'LLM ON, 6 workers' if enabled else 'LLM OFF'})...", flush=True)
    if enabled:
        from concurrent.futures import ThreadPoolExecutor
        done = 0
        with ThreadPoolExecutor(max_workers=6) as ex:
            for _ in ex.map(lambda p: enrich_event(p[0], p[1], enabled), built):
                done += 1
                if done % 25 == 0:
                    print(f"   {done}/{len(built)}", flush=True)

    all_events = [ev for ev, mkts in built]
    all_markets = [mk for ev, mkts in built for mk in mkts]

    # Dedup by id: the venue pulls list the same event under multiple tags, so an
    # event (and its markets) can appear twice. Deterministic ids make these collide;
    # collapse by id (first wins) so ids stay unique (D1 primary key, citable ref).
    seen_ev, dedup_events = set(), []
    for ev in all_events:
        if ev["event_id"] in seen_ev:
            continue
        seen_ev.add(ev["event_id"]); dedup_events.append(ev)
    seen_mk, dedup_markets = set(), []
    for mk in all_markets:
        if mk["market_id"] in seen_mk:
            continue
        seen_mk.add(mk["market_id"]); dedup_markets.append(mk)
    if len(all_events) != len(dedup_events) or len(all_markets) != len(dedup_markets):
        print(f"dedup: dropped {len(all_events)-len(dedup_events)} duplicate events, "
              f"{len(all_markets)-len(dedup_markets)} duplicate markets", flush=True)
    all_events, all_markets = dedup_events, dedup_markets

    # strip pipeline-internal transient keys (leading underscore) before serialization
    for mk in all_markets:
        for k in [k for k in mk if k.startswith("_")]:
            mk.pop(k, None)

    # surface the new guard counts (subject leaks + date incoherence) — never silent
    n_leak = sum(1 for ev in all_events if ev.get("field_provenance", {}).get("subject_leak"))
    n_derived = sum(1 for mk in all_markets
                    if (mk.get("field_provenance", {}).get("resolve_at") or {}).get("source", "").startswith(("derived", "native:expiration")))
    print(f"guards: {n_leak} events with subject_leak fallback, "
          f"{n_derived} markets ladder-date reconciled "
          f"(run report_date_review.py for the date-review queue)", flush=True)

    bundle = {"_meta": {"generated_at": RUN_AT, "schema": "v0.2.0-universe",
                        "event_count": len(all_events), "market_count": len(all_markets)},
              "events": all_events, "markets": all_markets}
    (OUT_DIR / out_name).write_text(json.dumps(bundle, indent=2, default=str))
    print(f"\nwrote {OUT_DIR / out_name} ({len(all_events)} events, {len(all_markets)} markets)")

    if enabled:
        _cost_summary(len(all_events), universe_total)


if __name__ == "__main__":
    main()
