#!/usr/bin/env python3
"""Regulatory eligibility screen: stamp every market with pass/review/fail
against a named regime's distribution terms. Reads the served bundle; prints
the funnel by default; --write emits web/data/eligibility-<regime>.json for
the site/API build to join in.

Regimes are config, not code: each is a rule-set over fields the bundle
already carries. First regime: CIRO Administrative Bulletin 26-0076 (Canadian
dealers offering event contracts under IDPC Rule 2246(2)).

Three-state output, deliberately:
  pass   — clears every term mechanically (category, maturity, committed
           source whose class is government/official/institutional)
  review — clears the mechanical terms but the source class needs human
           judgment against the regime's language (media, party bodies,
           commercial data providers, unclassified names)
  fail   — misses a mechanical term (category, maturity, or no committed
           source)

The source-name -> class mapping below is the adjudication surface: every
entry is a judgment call to be reviewed, not an oracle. Unmatched named
sources NEVER silently pass — they land in review.

This is screening data to support a dealer's own determination. It is not a
compliance opinion.
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"

# ---------------------------------------------------------------------------
# Source classification.
# class -> tier:  pass-tier classes satisfy "verifiable through official
# government or institutional sources" mechanically; review-tier classes are
# named-and-credible but need judgment against the regime's literal language.
# Patterns are case-insensitive regex fragments matched against the named
# resolution_source string.
# ---------------------------------------------------------------------------
SOURCE_CLASSES = [
    # --- pass tier ---------------------------------------------------------
    ("gov_federal", "pass", [
        r"bureau of labor statistics", r"bureau of economic analysis",
        r"federal reserve", r"fred\.stlouisfed", r"u\.?s\.? treasury", r"department of the treasury",
        r"library of congress", r"united states congress", r"white house",
        r"supreme court", r"federal election commission", r"securities and exchange commission",
        r"\bcdc\b", r"centers for disease control",
        r"\bnoaa\b", r"national oceanic and atmospheric", r"national weather service",
        r"energy information administration", r"\beia\b",
        r"census bureau", r"internal revenue service", r"\bcbo\b", r"congressional budget office",
        r"department of (state|defense|justice|energy|commerce|agriculture)",
        r"usda(\.gov)?\b", r"usgs(\.gov)?\b", r"\bnasa\b", r"\bfda\b", r"\bfaa\b",
        r"office of personnel management", r"social security administration",
    ]),
    ("gov_state_local", "pass", [
        r"secretary of state", r"county clerk", r"board of elections",
        r"us state governments", r"state government", r"governor'?s office",
        r"rent guidelines board",
    ]),
    ("gov_foreign_official", "pass", [
        # National statistics agencies / official bodies outside the US
        r"ibge(\.gov\.br)?", r"statistics canada", r"statcan", r"eurostat",
        r"office for national statistics", r"\bons\b",
    ]),
    ("exchange_official", "pass", [
        # Exchange/venue official data — institutional sources
        r"theice\.com", r"intercontinental exchange", r"\bcme\b(?! group rumor)",
        r"new york stock exchange", r"\bnyse\b", r"nasdaq\.com",
    ]),
    ("official_authority_generic", "pass", [
        # Kalshi series rules that name the CLASS of official authority
        # ("the official election authority responsible for certifying
        # results in <geography>"). Points at a government source; instance
        # resolves per market. NOTE: 299 markets carry a literal unfilled
        # "<geography>" template — flagged in stats, kept pass-tier because
        # the committed class is governmental.
        r"official election authority", r"election authority responsible",
        r"official certifying authority",
    ]),
    ("intl_official", "pass", [
        r"united nations", r"\bimf\b", r"international monetary fund",
        r"world bank", r"european central bank", r"\becb\b", r"\bnato\b",
        r"world health organization", r"\bwho\b", r"\bopec\b",
        r"bank of (england|canada|japan)",
    ]),
    ("regulated_benchmark", "pass", [
        # FCA-regulated benchmark administrators et al.
        r"cf benchmarks",
    ]),
    ("institutional_data", "pass", [
        r"statistical review of world energy",  # Energy Institute
        r"energy institute",
        r"s ?& ?p\b", r"standard *& *poor", r"msci\b", r"nasdaq\b.*(index|official)",
    ]),
    # --- review tier -------------------------------------------------------
    ("media", "review", [
        r"\babc\b", r"abc news", r"new york times", r"washington post",
        r"fox news", r"the guardian", r"usa today", r"associated press",
        r"\breuters\b", r"\bcnn\b", r"\bnbc\b", r"\bcbs\b", r"\bbbc\b",
        r"bloomberg", r"wall street journal", r"axios", r"politico",
        r"consensus of credible reporting", r"credible (news )?reporting",
    ]),
    ("party_official", "review", [
        # Official body for its own nominations — defensible either way;
        # founder adjudicates.
        r"republican party", r"democratic party", r"\b[dr]nc\b",
    ]),
    ("commercial_data", "review", [
        r"fiscal\.ai", r"trading economics", r"polymarket", r"kalshi",
        r"google finance", r"yahoo finance", r"coinmarketcap", r"coingecko",
    ]),
    ("community", "review", [
        r"lm ?arena", r"leaderboard", r"wikipedia",
    ]),
]

REGIMES = {
    "ciro-26-0076": {
        "name": "CIRO Administrative Bulletin 26-0076 / IDPC Rule 2246(2)",
        "venues": ["kalshi"],          # venues a Canadian dealer could route to
        "categories": ["economics", "financials", "climate"],
        "min_days_to_resolution": 30,
        "source_terms": "outcomes verifiable through official government or institutional sources",
    },
}


def parse_dt(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


def classify_source(name):
    """Return (source_class, tier) for a named source; unmatched -> review."""
    if not name:
        return None, None
    low = str(name).lower()
    for cls, tier, patterns in SOURCE_CLASSES:
        for p in patterns:
            if re.search(p, low):
                return cls, tier
    return "unclassified", "review"


def screen_market(m, event, regime, now):
    """Return (status, reasons, source_class). Mechanical fails first."""
    reasons = []

    if m.get("platform") not in regime["venues"]:
        reasons.append("venue_out_of_scope")
    if (event or {}).get("category") not in regime["categories"]:
        reasons.append("category_not_permitted")

    resolve = parse_dt(m.get("resolve_at") or m.get("close_at"))
    if not resolve:
        reasons.append("no_resolution_date")
    elif resolve < now + timedelta(days=regime["min_days_to_resolution"]):
        reasons.append("under_min_maturity")

    committed = m.get("source_commitment") == "named"
    if not committed:
        reasons.append("no_committed_source")

    if reasons:
        return "fail", reasons, None

    cls, tier = classify_source(m.get("resolution_source"))
    if tier == "pass":
        return "pass", [], cls
    return "review", [f"source_class_{cls}"], cls


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--regime", default="ciro-26-0076", choices=REGIMES)
    ap.add_argument("--write", action="store_true",
                    help="emit web/data/eligibility-<regime>.json")
    ap.add_argument("--asof", default=None,
                    help="screen as of this ISO date (default: now UTC)")
    args = ap.parse_args()

    regime = REGIMES[args.regime]
    now = parse_dt(args.asof) or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    bundle = json.loads(BUNDLE.read_text())
    events = {e["event_id"]: e for e in bundle["events"]}

    out, stats = {}, Counter()
    review_sources = Counter()
    funnel = Counter()
    template_bug = 0

    in_scope = [m for m in bundle["markets"] if m.get("platform") in regime["venues"]]
    for m in in_scope:
        ev = events.get(m.get("event_id"))
        status, reasons, cls = screen_market(m, ev, regime, now)
        out[m["market_id"]] = {
            "regime": args.regime,
            "status": status,
            "reasons": reasons,
            "source_class": cls,
            "screened_at": now.date().isoformat(),
        }
        stats[status] += 1
        if status == "review":
            review_sources[m.get("resolution_source")] += 1
        if "<geography>" in str(m.get("resolution_source", "")):
            template_bug += 1

        # funnel (ordered, first-failure attribution)
        funnel["0_in_scope"] += 1
        if (ev or {}).get("category") not in regime["categories"]:
            continue
        funnel["1_category"] += 1
        r = parse_dt(m.get("resolve_at") or m.get("close_at"))
        if not r or r < now + timedelta(days=regime["min_days_to_resolution"]):
            continue
        funnel["2_maturity"] += 1
        if m.get("source_commitment") != "named":
            continue
        funnel["3_committed_source"] += 1
        if out[m["market_id"]]["status"] == "pass":
            funnel["4_pass"] += 1

    print(f"REGIME {args.regime} — {regime['name']}   (as of {now.date()})")
    print(f"  in-scope venue markets:        {funnel['0_in_scope']:>6}")
    print(f"  + permitted category:          {funnel['1_category']:>6}")
    print(f"  + >= {regime['min_days_to_resolution']}d maturity:             {funnel['2_maturity']:>6}")
    print(f"  + committed named source:      {funnel['3_committed_source']:>6}")
    print(f"  + source class pass-tier:      {funnel['4_pass']:>6}")
    print(f"\n  STATUS: pass {stats['pass']} / review {stats['review']} / fail {stats['fail']}")
    print(f"  '<geography>' template artifacts in source text: {template_bug}")
    print("\n  REVIEW QUEUE (distinct sources, by market count) — adjudicate these:")
    for src, n in review_sources.most_common(30):
        cls, _ = classify_source(src)
        print(f"   {n:>5}  [{cls}]  {str(src)[:70]}")

    if args.write:
        dest = ROOT / f"web/data/eligibility-{args.regime}.json"
        dest.write_text(json.dumps(out, indent=0, sort_keys=True))
        print(f"\n  wrote {dest} ({len(out)} markets)")


if __name__ == "__main__":
    main()
