#!/usr/bin/env python3
"""Regulatory eligibility screen: stamp every market with pass/review/fail
against a named regime's distribution terms. Reads the served bundle; prints
the funnel by default; --write emits web/data/eligibility-<regime>.json for
the site/API build to join in.

Regimes are config, not code: each is a rule-set over fields the bundle
already carries. First regime: CIRO Administrative Bulletin 26-0076 (Canadian
dealers offering event contracts under IDPC Rule 2246(2)).

Three-state output, deliberately (public vocabulary — never pass/fail, so a
jurisdiction-scoping fact cannot be misread as market quality):
  eligible     — clears every Appendix A term mechanically (candidate
                 category, >=30d maturity, core subject-matter match)
  review       — clears mechanical terms; needs documented judgment
                 (S1 penumbra, S1 unenumerated category, S3 language flag)
  not_eligible — misses a mechanical term

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

# ---------------------------------------------------------------------------
# Subject-matter classification against Appendix A of bulletin 26-0076.
# The bulletin limits offerings to three buckets, each defined ILLUSTRATIVELY
# ("such as ..."), so there is a settled core and a penumbra:
#   §1 "Economic Forecasts: such as contracts based on economic statistics
#       related to the amount of sovereign debt, inflation rates, central bank
#       reserve rates, labor markets, and housing"
#   §1 "Environment Forecasts: such as contracts based on climate indicators
#       related to the average global temperature"
#   §1 "Financial indicators: such as US 500 Forecast Contracts that settle
#       based on the daily settlement price of the CME E-Mini S&P 500 Futures"
# Core matches -> pass. Candidates that match no core pattern -> review with
# reason category_interpretation (the penumbra; e.g. IPO-announcement markets).
# §3 prohibits "elections, political events, or other events of a political
# nature" — a flag that runs INSIDE permitted categories too (e.g. a Fed-chair
# nomination market filed under economics).
# Calibration: IBKR Canada (the first authorized dealer, live via ForecastEx)
# offers only economic + climate indicator contracts — the revealed perimeter
# matches the conservative core reading.
# ---------------------------------------------------------------------------
ECON_CORE = [
    r"inflation", r"\bcpi\b", r"consumer price", r"\bgdp\b", r"recession",
    r"unemployment", r"jobless", r"payroll", r"labor market", r"jobs report",
    r"nonfarm", r"employment situation",
    r"fed(eral)? funds", r"federal reserve", r"interest rate", r"\bfomc\b",
    r"central bank", r"overnight rate", r"rate (decision|cut|hike|change)",
    r"policy rate",
    r"housing (start|price|market)", r"home price", r"case-?shiller",
    r"sovereign debt", r"national debt", r"debt ceiling", r"deficit",
    r"productivity", r"trade (deficit|balance)", r"current account",
    r"retail sales", r"\bppi\b", r"producer price",
]
FIN_CORE = [
    r"s ?& ?p ?500", r"\bspx\b", r"nasdaq( ?100)?", r"dow jones", r"\bdjia\b",
    r"russell ?2000", r"treasury yield", r"10-?year yield", r"\bvix\b",
    r"mortgage rate", r"\bsofr\b",
]
CLIMATE_CORE = [
    r"global (average )?temperature", r"average global temperature",
    r"warmest", r"hottest year", r"climate indicator", r"sea level",
    r"carbon dioxide", r"\bco2\b", r"arctic sea ice",
]
POLITICAL_FLAG = [
    r"election", r"nominee", r"nomination", r"referendum", r"impeach",
    r"appointed?", r"confirmation", r"cabinet", r"president(ial)?",
    r"senate", r"congress(ional)?", r"parliament", r"prime minister",
    r"political party", r"\bmayor\b", r"governor race",
]

REGIMES = {
    "ciro-26-0076": {
        "name": "CIRO Administrative Bulletin 26-0076 / IDPC Rule 2246(2)",
        "venues": ["kalshi"],          # CFTC-regulated venue a dealer could route to
        # CM categories forming the CANDIDATE pool for the three Appendix A
        # buckets. crypto is included as REVIEW-ONLY (adjudicated 2026-06-10):
        # not enumerated in §1, but CF-Benchmarks-settled price contracts are
        # structurally identical to CIRO's own CME-settlement example — a
        # category-interpretation question, not a clear fail.
        "categories": ["economics", "financials", "climate"],
        "review_only_categories": ["crypto"],
        "min_days_to_resolution": 30,
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


def match_any(patterns, text):
    return any(re.search(p, text) for p in patterns)


def classify_subject(m, event):
    """Appendix A §1 bucket fit: ('core', bucket) | ('penumbra', None) | political flag."""
    text = " ".join([
        str((event or {}).get("question", "")),
        str(m.get("question_raw", "")),
        " ".join((event or {}).get("tags", []) or []),
    ]).lower()
    if match_any(POLITICAL_FLAG, text):
        return "political", None
    for bucket, pats in (("economic_forecasts", ECON_CORE),
                         ("financial_indicators", FIN_CORE),
                         ("environment_forecasts", CLIMATE_CORE)):
        if match_any(pats, text):
            return "core", bucket
    return "penumbra", None


def screen_market(m, event, regime, now):
    """Return (status, reasons, bucket). Mechanical fails first; then the
    Appendix A subject test sorts core (pass) from penumbra/political (review).
    Source class is diligence METADATA, not an eligibility gate — the bulletin
    contains no source-verifiability term."""
    reasons = []

    cat = (event or {}).get("category")
    review_only = cat in regime.get("review_only_categories", [])

    if m.get("platform") not in regime["venues"]:
        reasons.append("venue_out_of_scope")
    if cat not in regime["categories"] and not review_only:
        reasons.append("category_not_permitted")

    resolve = parse_dt(m.get("resolve_at") or m.get("close_at"))
    if not resolve:
        reasons.append("no_resolution_date")
    elif resolve < now + timedelta(days=regime["min_days_to_resolution"]):
        reasons.append("under_min_maturity")

    if reasons:
        return "not_eligible", reasons, None

    if review_only:
        # crypto: never pass mechanically — §1 doesn't enumerate it, even
        # where settlement structure mirrors the CME example
        return "review", ["category_not_enumerated_s1"], None

    kind, bucket = classify_subject(m, event)
    if kind == "political":
        return "review", ["political_nature_s3"], None
    if kind == "core":
        return "eligible", [], bucket
    return "review", ["category_interpretation_s1"], None


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
    review_reasons = Counter()
    penumbra_examples = Counter()
    pass_buckets = Counter()
    pass_diligence = Counter()
    funnel = Counter()

    in_scope = [m for m in bundle["markets"] if m.get("platform") in regime["venues"]]
    for m in in_scope:
        ev = events.get(m.get("event_id"))
        status, reasons, bucket = screen_market(m, ev, regime, now)
        src_cls, _ = classify_source(m.get("resolution_source"))
        out[m["market_id"]] = {
            "regime": args.regime,
            "status": status,
            "reasons": reasons,
            "permitted_category": bucket,
            # diligence metadata (NOT eligibility gates)
            "source_commitment": m.get("source_commitment"),
            "source_class": src_cls,
            "rcg_grade": m.get("resolution_clarity_grade"),
            "screened_at": now.date().isoformat(),
        }
        stats[status] += 1
        if status == "eligible":
            pass_buckets[bucket] += 1
            pass_diligence[(m.get("source_commitment"), src_cls)] += 1
        if status == "review":
            review_reasons[reasons[0]] += 1
            if reasons[0] == "category_interpretation_s1":
                penumbra_examples[str((ev or {}).get("question", ""))[:64]] += 1

        # funnel (ordered, first-failure attribution) — derived from the SAME
        # stamped reasons that produce the statuses, so the published cascade
        # composes exactly with the per-market records on every surface
        # (HTML/JSON/CSV). The old version re-tested event category directly,
        # which silently dropped crypto (review-only, not category-failed) at
        # the category gate and made the public numbers irreconcilable.
        rec = out[m["market_id"]]
        first = rec["reasons"][0] if rec["reasons"] else None
        funnel["0_in_scope"] += 1
        if first == "category_not_permitted":
            continue
        funnel["1_category"] += 1
        if first in ("under_min_maturity", "no_resolution_date"):
            continue
        funnel["2_maturity"] += 1
        if rec["status"] == "eligible":
            funnel["3_eligible"] += 1

    print(f"REGIME {args.regime} — {regime['name']}   (as of {now.date()})")
    print(f"  in-scope venue markets:               {funnel['0_in_scope']:>6}")
    print(f"  + candidate category (econ/fin/clim): {funnel['1_category']:>6}")
    print(f"  + >= {regime['min_days_to_resolution']}d maturity:                    {funnel['2_maturity']:>6}")
    print(f"  + Appendix A core subject -> PASS:    {funnel['3_eligible']:>6}")
    print(f"\n  STATUS: eligible {stats['eligible']} / review {stats['review']} / not_eligible {stats['not_eligible']}")
    print(f"\n  ELIGIBLE by bucket: {dict(pass_buckets)}")
    print(f"  REVIEW by reason: {dict(review_reasons)}")
    print("\n  DILIGENCE metadata on the ELIGIBLE set (source_commitment, class):")
    for (sc, cls), n in pass_diligence.most_common(10):
        print(f"   {n:>5}  commitment={sc}  class={cls}")
    print("\n  PENUMBRA sample (top distinct events in category_interpretation review):")
    for q, n in penumbra_examples.most_common(15):
        print(f"   {n:>4}  {q}")

    if args.write:
        # Page-ready summary: funnel + clustered review + eligible-set stats.
        # Clusters group the review set into the ~20 actual judgment units.
        CLUSTER_LABELS = [
            ("ipo_announcements", "IPO announcements", [r"\bipo\b"]),
            ("company_metrics", "Company performance metrics",
             [r"users\b", r"subscribers", r"active uniques", r"members\b", r"downloads"]),
            ("commodity_prices", "Commodity price levels",
             [r"crude", r"\boil\b", r"gas(oline)? price", r"natural gas", r"gold price"]),
            ("fx_levels", "FX rate levels", [r"usd/", r"/usd", r"exchange rate"]),
            ("wealth_rankings", "Wealth / rich-list rankings", [r"wealthiest", r"richest"]),
            ("weather_events", "Weather events (vs climate indicators)",
             [r"hurricane", r"storm", r"tornado", r"snow", r"rainfall", r"heat wave",
              r"high temp", r"temperature in "]),
        ]
        clusters = defaultdict(lambda: {"market_count": 0, "events": Counter()})
        for m in bundle["markets"]:
            rec = out.get(m["market_id"])
            if not rec or rec["status"] != "review":
                continue
            ev = events.get(m.get("event_id")) or {}
            q = str(ev.get("question", "?"))
            reason = rec["reasons"][0]
            if reason == "category_not_enumerated_s1":
                key, label = "crypto_prices", "Crypto price contracts (category not enumerated in Section 1)"
            elif reason == "political_nature_s3":
                key, label = "political_language", "Political-language flags (Section 3 echo, in-category)"
            else:
                key, label = "other_interpretation", "Other Section 1 interpretation questions"
                low = q.lower()
                for k, lbl, pats in CLUSTER_LABELS:
                    if any(re.search(p, low) for p in pats):
                        key, label = k, lbl
                        break
            rec["cluster"] = key  # per-market cluster key for the /screens/ page
            c = clusters[key]
            c["label"] = label
            c["reason"] = reason
            c["market_count"] += 1
            c["events"][q] += 1

        cluster_list = sorted(
            ({"key": k, "label": v["label"], "reason": v["reason"],
              "market_count": v["market_count"],
              "example_events": [q for q, _ in v["events"].most_common(5)],
              "event_count": len(v["events"])}
             for k, v in clusters.items()),
            key=lambda c: -c["market_count"])

        summary = {
            "regime": args.regime,
            "regime_name": regime["name"],
            "screen_version": "v1",
            "screened_at": now.date().isoformat(),
            "venue": regime["venues"][0],
            "funnel": {
                "in_scope": funnel["0_in_scope"],
                "candidate_category": funnel["1_category"],
                "min_maturity": funnel["2_maturity"],
                "eligible": stats["eligible"],
                "review": stats["review"],
                "not_eligible": stats["not_eligible"],
            },
            "eligible_categories": dict(pass_buckets),
            # Plain-English legend for the machine reason codes — mirrored in
            # web/src/lib/eligibility.ts REASON_COPY; keep the two in step.
            "reason_definitions": {
                "category_not_permitted": "Subject falls outside the categories Section 1 of Bulletin 26-0076 Appendix A permits (economic forecasts, financial indicators, environment forecasts) — e.g. sports, entertainment, elections.",
                "under_min_maturity": "Term to maturity is under the 30-day minimum (Section 2).",
                "no_resolution_date": "No parseable resolution date, so the Section 2 term test cannot be evidenced.",
                "category_interpretation_s1": "Fits a Section 1 permitted category only under interpretation — Section 1's 'such as' examples are macro statistics and this subject is adjacent rather than enumerated.",
                "category_not_enumerated_s1": "Subject category is not enumerated in Section 1 (currently crypto price contracts) — held for review rather than excluded.",
                "political_nature_s3": "Language suggests political character (Section 3) inside an otherwise permitted category.",
                "venue_out_of_scope": "Venue outside the regime's scope (CIRO terms require CFTC-regulated venues).",
            },
            "eligible_no_committed_source": sum(
                n for (sc, _), n in pass_diligence.items() if sc != "named"),
            "review_reasons": dict(review_reasons),
            "review_clusters": cluster_list,
        }
        dest = ROOT / f"web/data/eligibility-{args.regime}.json"
        dest.write_text(json.dumps(out, indent=0, sort_keys=True))
        print(f"\n  wrote {dest} ({len(out)} markets)")

        sdest = ROOT / f"web/data/eligibility-{args.regime}-summary.json"
        sdest.write_text(json.dumps(summary, indent=2))
        print(f"  wrote {sdest} ({len(cluster_list)} review clusters)")


if __name__ == "__main__":
    main()
