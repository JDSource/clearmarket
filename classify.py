#!/usr/bin/env python3
"""
ClearMarket — institutional filter + venue→category classifier.

Net-new code per `schema-source-of-truth-decision.md` (2026-05-26) and the CM PRD
institutional filter (§4 / build item #2). Gates the full Kalshi + Polymarket
universe down to the institutional set before enhance.py enriches it.

Three filter inputs (PRD §4):
  1. category whitelist  — the 9 IN categories below (sports/entertainment/mentions OUT)
  2. volume threshold     — venue-specific (tune empirically; placeholders flagged TODO)
  3. resolution-date      — resolves within RESOLUTION_HORIZON_MONTHS

Category model (locked 2026-05-26):
  IN : economics, financials, crypto, companies, technology, health,
       politics, geopolitics, climate
  OUT: sports, entertainment, mentions

Kalshi ships a clean category field → direct map.
Polymarket has no category → derive from tags[] (deterministic map keyed on
top-level tags, weighting forceShow; Haiku fallback for unmapped). One primary
category + the rest kept as tags.

This module is pure logic (no network, no API key) so it's unit-testable. The
Haiku fallback is a seam (`classify_poly_llm_fallback`) — not invoked here.
Run `python3 classify.py` for the self-test against real specimen records.
"""

from __future__ import annotations

import calendar
import re
from datetime import datetime, timedelta, timezone

# -----------------------------------------------------------------
# Category model (locked 2026-05-26)
# -----------------------------------------------------------------
CATEGORIES_IN = (
    "economics", "financials", "crypto", "companies", "technology",
    "health", "politics", "geopolitics", "climate",
)

# -----------------------------------------------------------------
# Bundle-type classifier (2026-07-01) — routes a multi-outcome event to its
# resolution-inheritance shape so enrichment knows which fields are event-level
# shared vs per-child native. Pure logic; unit-testable. See
# outputs/clearmarket/event-child-resolution-fix-spec-2026-07-01.md.
# -----------------------------------------------------------------
_MONTH_RE = re.compile(
    r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w*\b|\bq[1-4]\b|\b20\d{2}\b", re.I
)
_THRESHOLD_RE = re.compile(r"[<>]=?|\$|\bbps\b|\b\d[\d,.]*\s*(k|m|b|bn|trillion|billion|million)?\b", re.I)


def _looks_like_date(title: str) -> bool:
    return bool(_MONTH_RE.search(title or ""))


def _looks_like_threshold(title: str) -> bool:
    t = (title or "").strip()
    if _looks_like_date(t):          # a year is a date, not a strike
        return False
    return bool(_THRESHOLD_RE.search(t))


def _ladder_kind(markets: list) -> str:
    titles = [(m.get("groupItemTitle") or m.get("yes_sub_title") or "") for m in markets]
    n = len(titles) or 1
    date_like = sum(1 for t in titles if _looks_like_date(t))
    num_like = sum(1 for t in titles if _looks_like_threshold(t))
    if date_like / n >= 0.6:
        return "date_ladder"
    if num_like / n >= 0.6:
        return "strike_ladder"
    return "categorical"


def classify_bundle_type(ev: dict, venue: str) -> str:
    """categorical | date_ladder | strike_ladder | augmented_negrisk | singleton.

    Determines resolution-field inheritance: for every non-singleton type the
    resolution RULE/SOURCE is event-level (one, generic, inherited); dates are
    per-child native for ladders, shared for categoricals; augmented_negrisk
    additionally needs a per-child grade override on its placeholder ("Other") leg.
    """
    markets = ev.get("markets") or []
    if len(markets) <= 1:
        return "singleton"
    if venue == "polymarket":
        if ev.get("negRiskAugmented"):
            return "augmented_negrisk"
        if ev.get("negRisk") or ev.get("enableNegRisk"):
            return "categorical"
        return _ladder_kind(markets)      # cumulativeMarkets or plain multi
    # kalshi
    if ev.get("mutually_exclusive"):
        return "categorical"
    return _ladder_kind(markets)


_MON = {m.lower(): i for i, m in enumerate(calendar.month_abbr) if m}
_MON.update({m.lower(): i for i, m in enumerate(calendar.month_name) if m})


def parse_ladder_deadline(title, year_hint=None):
    """Derive an ISO settlement date from a date-ladder rung's groupItemTitle when the
    venue ships a degenerate shared endDate across the ladder (the fed-rate B1 case).
    Handles 'June 2026', 'March 31, 2026', 'December 31', 'Q3 2026', bare '2027'.
    Returns 'YYYY-MM-DDT00:00:00Z' or None (None -> keep native, stay flagged)."""
    if not title:
        return None
    t = title.strip().lower()
    # Reject strike/threshold titles ('$2000', 'above 2050', '1.65 million') — a price digit-string
    # can look like a year (2000-2099) and must NEVER be parsed as a date. Callers also gate this to
    # date_ladder only, but defend here too.
    if "$" in t or _looks_like_threshold(t):
        return None
    # comparison words signal a strike/threshold rung ('above 2000', 'below 5%'), never a date
    if re.search(r"\b(above|below|over|under|at least|at most|more than|fewer than|less than|greater)\b", t):
        return None
    yr_m = re.search(r"\b(20\d{2})\b", t)
    year = int(yr_m.group(1)) if yr_m else year_hint
    if not year:
        return None
    # strip the year token so it can't be mistaken for a day number later
    t_noyear = re.sub(r"\b20\d{2}\b", " ", t)
    # Quarter / Half
    q = re.search(r"\bq([1-4])\b", t_noyear)
    if q:
        month = int(q.group(1)) * 3
        day = calendar.monthrange(year, month)[1]
        return f"{year:04d}-{month:02d}-{day:02d}T00:00:00Z"
    h = re.search(r"\bh([12])\b", t_noyear)
    if h:
        month = 6 if h.group(1) == "1" else 12
        day = calendar.monthrange(year, month)[1]
        return f"{year:04d}-{month:02d}-{day:02d}T00:00:00Z"
    # Month [day]
    mon = None
    for name, idx in _MON.items():
        if re.search(r"\b" + re.escape(name) + r"\b", t_noyear):
            mon = idx
            break
    if mon:
        day_m = re.search(r"\b(\d{1,2})\b", t_noyear)   # year already stripped -> safe
        day = int(day_m.group(1)) if day_m and 1 <= int(day_m.group(1)) <= 31 else calendar.monthrange(year, mon)[1]
        day = min(day, calendar.monthrange(year, mon)[1])
        return f"{year:04d}-{mon:02d}-{day:02d}T00:00:00Z"
    # bare year -> Dec 31
    if yr_m:
        return f"{year:04d}-12-31T00:00:00Z"
    return None
CATEGORIES_OUT = ("sports", "entertainment", "mentions")
ALL_CATEGORIES = CATEGORIES_IN + CATEGORIES_OUT

# -----------------------------------------------------------------
# Kalshi category (verbatim string) -> CM category
# Source values observed live 2026-05-26. None of these map to a dropped value;
# Sports/Entertainment/Mentions map to OUT categories so they're filtered, not lost.
# -----------------------------------------------------------------
KALSHI_CATEGORY_MAP = {
    "Economics":              "economics",
    "Financials":             "financials",
    "Companies":              "companies",
    "Science and Technology": "technology",
    "Health":                 "health",
    "Climate and Weather":    "climate",     # NOTE: pure-weather (hurricanes) lands here too;
                                             # catalyst layer routes weather->'none'. Revisit if
                                             # weather noise needs splitting out of the institutional set.
    "Politics":               "politics",
    "Elections":              "politics",    # folded; 'elections' survives as a tag
    "Geopolitics":            "geopolitics",
    "World":                  "geopolitics",
    "Crypto":                 "crypto",
    "Sports":                 "sports",       # OUT
    "Entertainment":          "entertainment",# OUT
    "Mentions":               "mentions",     # OUT
}

# -----------------------------------------------------------------
# Polymarket tag slug -> CM category. Keyed on Poly's top-level tags.
# Priority order matters for multi-tag events: first match in CATEGORIES_IN order wins.
# -----------------------------------------------------------------
POLY_TAG_MAP = {
    # economics
    "economy": "economics", "economic-policy": "economics", "fed-rates": "economics",
    "fed": "economics", "fomc": "economics", "inflation": "economics",
    "macro-single": "economics", "macro-graph": "economics", "fed-chair": "economics",
    # financials
    "finance": "financials", "spx": "financials", "sp-500": "financials",
    "nasdaq": "financials", "commodities": "financials", "etf": "financials",
    # crypto
    "crypto": "crypto", "bitcoin": "crypto", "ethereum": "crypto",
    "crypto-prices": "crypto", "altcoins": "crypto",
    # technology
    "tech": "technology", "ai": "technology", "openai": "technology", "claude": "technology",
    # health
    "health": "health", "fda": "health",
    # companies
    "business": "companies", "earnings": "companies",
    # politics
    "politics": "politics", "elections": "politics", "trump": "politics",
    "congress": "politics", "federal-government": "politics", "house-races": "politics",
    # geopolitics
    "geopolitics": "geopolitics", "international-affairs": "geopolitics", "war": "geopolitics",
    # climate
    "climate": "climate", "cop": "climate", "wildfire": "climate",
    # OUT
    "sports": "sports", "pop-culture": "entertainment", "mentions": "mentions",
}

# Structural / noise tags that never carry category signal.
POLY_NOISE_TAGS = {
    "parlays", "hit-first", "hide-from-new", "popularity", "tradition",
    "controversies", "season-finale", "new",
}

# -----------------------------------------------------------------
# Filter thresholds  (TODO: tune empirically once the full universe is pulled)
# -----------------------------------------------------------------
POLY_MIN_VOLUME_USD       = 10_000     # Poly ships USD volume
KALSHI_MIN_VOLUME_USD     = 5_000      # Kalshi volume imputed to USD upstream (volume_fp * last_price)
RESOLUTION_HORIZON_MONTHS = 24


# -----------------------------------------------------------------
# Category classification
# -----------------------------------------------------------------
def classify_kalshi(event: dict) -> str | None:
    """Map a Kalshi event/market's `category` string to a CM category.
    Returns a CM category (IN or OUT), or None if the venue category is unknown."""
    return KALSHI_CATEGORY_MAP.get(event.get("category"))


def classify_poly(event: dict) -> tuple[str | None, list[str]]:
    """Derive a CM category from a Polymarket event's tags[].

    Returns (category, mapped_tag_slugs). category is None when no top-level tag
    maps — that's the signal to call the Haiku fallback. Deterministic-first:
    prefer forceShow tags, then resolve multi-matches by CATEGORIES_IN order.
    """
    tags = event.get("tags") or []
    matches: list[tuple[str, bool]] = []  # (cm_category, forceShow)
    mapped_slugs: list[str] = []
    for t in tags:
        slug = (t.get("slug") or "").lower()
        if slug in POLY_NOISE_TAGS:
            continue
        cm = POLY_TAG_MAP.get(slug)
        if cm:
            matches.append((cm, bool(t.get("forceShow"))))
            mapped_slugs.append(slug)
    if not matches:
        return None, []
    # forceShow wins; then earliest in CATEGORIES_IN/OUT priority order
    order = {c: i for i, c in enumerate(ALL_CATEGORIES)}
    matches.sort(key=lambda m: (not m[1], order.get(m[0], 99)))
    return matches[0][0], mapped_slugs


def classify_poly_llm_fallback(event: dict) -> str | None:
    """Seam for the Haiku fallback (PRD: deterministic-first, LLM fallback).
    Intentionally NOT wired to the API here — returns None so the caller can
    decide. Wire to enhance.py's llm_call(model=HAIKU) when running at scale.
    """
    return None  # TODO: Haiku classify title+description into ALL_CATEGORIES


# -----------------------------------------------------------------
# Institutional filter
# -----------------------------------------------------------------
def _parse_iso(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def resolves_within_horizon(resolve_at: str | None, *, now: datetime | None = None,
                            months: int = RESOLUTION_HORIZON_MONTHS) -> bool:
    """True if resolution date is in the future and within `months` from now."""
    dt = _parse_iso(resolve_at)
    if dt is None:
        return False
    now = now or datetime.now(timezone.utc)
    horizon = now + timedelta(days=months * 30)
    return now <= dt <= horizon


def passes_institutional_filter(category: str | None, volume_usd: float | None,
                                resolve_at: str | None, venue: str,
                                *, now: datetime | None = None) -> tuple[bool, str]:
    """Apply the three filter inputs. Returns (passes, reason).
    `reason` names the first failing gate (or 'pass') for auditability."""
    if category not in CATEGORIES_IN:
        return False, f"category_out:{category}"
    threshold = POLY_MIN_VOLUME_USD if venue == "polymarket" else KALSHI_MIN_VOLUME_USD
    if volume_usd is None or volume_usd < threshold:
        return False, f"below_volume:{volume_usd}<{threshold}"
    if not resolves_within_horizon(resolve_at, now=now):
        return False, f"resolution_out_of_horizon:{resolve_at}"
    return True, "pass"


# -----------------------------------------------------------------
# Resolution Clarity Grade (RCG) — deterministic A/B/C from source signals
# Rolls the verified-source layer (deep-link URL, source quality, subjective
# boilerplate) into the named differentiator. No LLM.
#   A = authoritative named source + verifiable DEEP-LINK URL
#   B = source named but weak verifiability (no deep link / domain-root URL /
#       loose placeholder like Kalshi's "For example, Google Finance")
#   C = subjective resolution ("consensus of credible reporting") or no source
# -----------------------------------------------------------------
_SUBJECTIVE_RE = re.compile(
    r"consensus of (a )?credible|credible (public )?reporting|credible sources|"
    r"a consensus of|resolve[sd]?.{0,30}consensus", re.I)


def _is_deep_link(url: str | None) -> bool:
    """True if the URL has a path beyond the bare domain root."""
    if not url:
        return False
    m = re.match(r"https?://[^/]+(/.*)?$", url)
    path = m.group(1) if m else None
    return bool(path and path not in ("/", ""))


# RCG v2 model (locked 2026-05-26; detection split revised 2026-05-27). Weighted score,
# re-normalized over applicable factors, with hard caps (ceilings) for fatal defects.
# 5 LLM factors (trigger/contested/source_conflict/temporal/mutability — one per-event call),
# 1 deterministic (arbiter), 1 hybrid (source_clarity, read from the §2 verified-source layer).
# Spec: rcg-scoring-model.csv (repo root) + METHODOLOGY.md §3.
RCG_WEIGHTS = {
    "trigger_objectivity": 28,   # LLM; heaviest, saturation-resistant
    "contested_reality":   22,   # LLM; fact controlled/disputed by an interested party
    "source_clarity":      18,   # hybrid: reads verified-source layer (det. Kalshi / gated-LLM Poly)
    "arbiter_incentive":   12,   # deterministic (mechanism/proposer)
    "source_conflict":      8,   # LLM; situational — 2+ conflictable sources with no adjudication rule
    "temporal_precision":   7,   # LLM; always-on
    "source_mutability":    5,   # LLM; always-on
}
RCG_FRACTION = {"pass": 1.0, "partial": 0.5, "fail": 0.0}   # "na" => excluded from denominator
_RCG_RANK = {"A": 0, "B": 1, "C": 2}
_RANK_RCG = {0: "A", 1: "B", 2: "C"}


def _rcg_band(score: float) -> str:
    return "A" if score >= 80 else "B" if score >= 55 else "C"


def _rcg_caps(r: dict) -> list[tuple[str, str]]:
    """Hard caps (ceilings) derived from factor ratings: (name, ceiling_grade)."""
    caps = []
    if r.get("source_conflict") == "fail":
        caps.append(("multi_source_no_conflict_rule", "C"))
    # Deterministic, non-weighted pseudo-factor (methodology v3.7, 2026-08-04): the venue's
    # own notice channel (Kalshi product_metadata.important_info) names a settlement source
    # that differs from the committed settlement_sources entry — two venue documents disagree
    # about what settles the contract (Burke gold case: XAU/USD vs Metal.Index.GOLD/USD).
    # Cap-only: never contributes to score, so absence never inflates a grade.
    if r.get("exchange_notice_conflict") == "fail":
        caps.append(("exchange_notice_source_conflict", "C"))
    if r.get("trigger_objectivity") == "fail" and r.get("source_clarity") == "fail":
        caps.append(("discretionary_trigger_no_source", "C"))
    if r.get("arbiter_incentive") == "fail" and r.get("trigger_objectivity") == "fail":
        caps.append(("permissionless_oracle_discretionary_trigger", "C"))
    if r.get("contested_reality") == "fail":
        caps.append(("adversarial_ground_truth", "B"))   # ceiling, not floor
    return caps


# Engine per factor — stamped into the audit trail so any grade is reverse-engineerable.
_LLM_FACTORS_SET = {"trigger_objectivity", "contested_reality", "source_conflict",
                    "temporal_precision", "source_mutability"}
# Source-commitment cap ceilings — folded in from the retired patch_sources (subtype -> ceiling).
# committed_secondhand (ruled 2026-07-04, rubric v3.6): sole committed source is a concrete
# non-authority (data aggregator / single outlet — Fiscal.ai class). A real commitment, capped C
# because the source transcribes numbers whose authority lies elsewhere and no rule covers a
# disagreement (ESPN precedent; CF Benchmarks-style published-methodology providers stay named).
_COMMITMENT_CAP = {"committed_secondhand": "C", "uncommitted_illustrative": "B",
                   "uncommitted_placeholder": "C", "none": "C"}


def resolution_clarity_grade(ratings: dict, commitment_subtype: str | None = None) -> dict:
    """v2 engine. `ratings` maps each RCG_WEIGHTS factor to pass|partial|fail|na. Re-normalizes
    over applicable (non-na) factors, bands, applies factor cap ceilings + the source-commitment
    ceiling (from the LLM commitment classification). Returns the grade PLUS a per-factor audit
    breakdown (rating / engine / weight / points) so any grade re-derives from stamped values."""
    earned = possible = 0.0
    factors = {}
    for f, w in RCG_WEIGHTS.items():
        rating = ratings.get(f, "na")
        entry = {"rating": rating, "engine": "llm" if f in _LLM_FACTORS_SET else "deterministic",
                 "weight": w}
        if rating != "na":
            possible += w
            earned += w * RCG_FRACTION.get(rating, 0.0)
            entry["points"] = round(w * RCG_FRACTION.get(rating, 0.0), 1)
        factors[f] = entry
    score = round(100 * earned / possible) if possible else 0
    band = _rcg_band(score)
    caps = _rcg_caps(ratings)
    cc = _COMMITMENT_CAP.get(commitment_subtype)
    if cc:
        caps = caps + [(f"commitment_{commitment_subtype}", cc)]
    rank = max([_RCG_RANK[band]] + [_RCG_RANK[c[1]] for c in caps])
    applied = sum(1 for f in RCG_WEIGHTS if ratings.get(f, "na") != "na")
    return {"grade": _RANK_RCG[rank], "score": score, "band": band,
            "applied_factors": applied, "total_factors": len(RCG_WEIGHTS),
            "caps": [c[0] for c in caps], "factors": factors,
            "commitment_subtype": commitment_subtype}


# ---- deterministic factor raters (source_clarity, arbiter); the 5 LLM factors are supplied at enrichment ----
import re as _re

# Venue homepages / generic landing pages are NOT real source citations — a market that
# "cites" kalshi.com or polymarket.com has not named where the outcome is actually read.
_PLACEHOLDER_HOSTS = ("kalshi.com", "polymarket.com", "kalshi.co")

def _is_placeholder_citation(url: str) -> bool:
    """True if the citation is the venue's own homepage / a bare host with no real path."""
    if not url:
        return True
    u = url.strip().rstrip("/")
    host = _re.sub(r"^https?://(www\.)?", "", u).split("/")[0].lower()
    path = u[u.find(host) + len(host):] if host in u else ""
    if host in _PLACEHOLDER_HOSTS:
        return True
    # bare host with no meaningful path (e.g. "https://example.com") = not a real deep link
    if not path or path in ("", "/"):
        return True
    return False

def _is_placeholder_source_name(name: str) -> bool:
    """Single-token / acronym-only source names ('NYC') are placeholders, not named authorities."""
    return bool(name) and len(name.split()) <= 1

def rate_source_clarity(market: dict) -> str:
    # ONE source judgment: when the LLM commitment classification is stamped (enrichment), this
    # factor DERIVES from it instead of second-guessing with word-count heuristics — a factor
    # scoring "pass" while the commitment cap says "placeholder" was a self-contradicting audit
    # trail (the cl-hit oil misgrade class). Methodology: pass = named authority + usable link.
    sub = market.get("source_commitment_subtype")
    if sub:
        if sub == "named":
            cite = market.get("source_citation")
            return "pass" if (cite and not _is_placeholder_citation(cite)) else "partial"
        if sub in ("committed_secondhand", "uncommitted_illustrative"):
            # secondhand: the source IS named and checkable — the deficiency (authority
            # quality, no disagreement rule) is carried by the C cap, not double-counted here
            return "partial"
        return "fail"   # uncommitted_placeholder / none
    # Pre-commitment fallback (build-time only — the grade is 'pending' until the per-event
    # LLM ratings exist, so this path never reaches a shipped grade).
    if market.get("resolution_source_quality") == "loose":
        return "partial"
    cite = market.get("source_citation")
    name = market.get("resolution_source")
    real_cite = cite and not _is_placeholder_citation(cite)
    real_name = name and not _is_placeholder_source_name(name)
    if real_cite and real_name:
        return "pass"
    if real_cite or real_name or name:
        return "partial"
    return "fail"


def rate_arbiter(market: dict) -> str:
    mech = market.get("arbitration_model")
    if mech == "kalshi_staff":
        return "pass"
    if mech == "uma_oracle":
        return "partial" if market.get("resolution_proposer") == "managed_whitelist" else "fail"
    return "partial"


_RCG_LLM_FACTORS = ("trigger_objectivity", "contested_reality", "source_conflict",
                    "temporal_precision", "source_mutability")


def grade_market(market: dict, description: str = "", llm_ratings: dict | None = None) -> dict:
    """RCG for a market. Deterministic factors (source_clarity, arbiter) computed here; the
    five LLM factors (trigger/contested/source_conflict/temporal/mutability) come from the
    per-event rater at enrichment. Returns grade='pending' until trigger+contested are present.
    `description` is retained for call-site compatibility; deterministic raters no longer use it."""
    ratings = {
        "source_clarity":    rate_source_clarity(market),
        "arbiter_incentive": rate_arbiter(market),
    }
    # deterministic exchange-notice conflict flag, set at enrich/apply time (v3.7) —
    # cap-only input; read by _rcg_caps, never scored.
    if market.get("source_notice_conflict"):
        ratings["exchange_notice_conflict"] = "fail"
    if not llm_ratings or any(f not in llm_ratings for f in ("trigger_objectivity", "contested_reality")):
        return {"grade": "pending", "score": None, "applied_factors": None,
                "total_factors": len(RCG_WEIGHTS), "caps": [],
                "reason": "awaiting per-event LLM factor ratings"}
    ratings.update({f: llm_ratings.get(f, "na") for f in _RCG_LLM_FACTORS})
    # commitment cap comes from the LLM source-commitment classification (stored at enrich);
    # replaces the retired patch_sources deterministic re-cap.
    return resolution_clarity_grade(ratings, commitment_subtype=market.get("source_commitment_subtype"))


# -----------------------------------------------------------------
# Self-test — runs against real records pulled 2026-05-26
# -----------------------------------------------------------------
def _selftest() -> None:
    NOW = datetime(2026, 5, 26, tzinfo=timezone.utc)

    kalshi_samples = [
        {"category": "Economics", "title": "Fed funds rate after Jun 2026 meeting?", "v": 50000, "r": "2026-06-17T18:00:00Z"},
        {"category": "Financials", "title": "Nasdaq-100 close price end of 2026?", "v": 80000, "r": "2026-12-31T21:00:00Z"},
        {"category": "Companies", "title": "Sam Altman replaced as OpenAI CEO?", "v": 9000, "r": "2026-12-31T00:00:00Z"},
        {"category": "Science and Technology", "title": "FDA approve MDMA for PTSD?", "v": 12000, "r": "2026-09-01T00:00:00Z"},
        {"category": "Climate and Weather", "title": "First Atlantic hurricane name 2026", "v": 3000, "r": "2026-12-01T00:00:00Z"},
        {"category": "Sports", "title": "UNC Health Championship Winner", "v": 200000, "r": "2026-06-01T00:00:00Z"},
        {"category": "Mentions", "title": "What announcers say during NHL game", "v": 50000, "r": "2026-05-29T00:00:00Z"},
    ]
    print("KALSHI:")
    for s in kalshi_samples:
        cm = classify_kalshi(s)
        ok, why = passes_institutional_filter(cm, s["v"], s["r"], "kalshi", now=NOW)
        print(f"  {('IN ' if ok else 'OUT'):3} [{cm or '??':12}] {why:28} | {s['title'][:45]}")

    poly_samples = [
        {"title": "Fed decisions (Mar-Jun)", "volume": 1202252,
         "endDate": "2026-06-17T00:00:00Z",
         "tags": [{"slug": "fed"}, {"slug": "parlays"}, {"slug": "economy"},
                  {"slug": "fed-rates", "forceShow": True}, {"slug": "fomc"}]},
        {"title": "Bitcoin vs Gold vs S&P 500 in 2026", "volume": 804746,
         "endDate": "2026-12-31T00:00:00Z",
         "tags": [{"slug": "finance"}, {"slug": "crypto"}, {"slug": "bitcoin", "forceShow": True},
                  {"slug": "commodities"}, {"slug": "sp-500"}]},
        {"title": "Will Bitcoin hit $70k or $90k first?", "volume": 98383,
         "endDate": "2027-01-01T05:00:00Z",
         "tags": [{"slug": "bitcoin", "forceShow": True}, {"slug": "crypto-prices", "forceShow": True},
                  {"slug": "hit-first"}, {"slug": "crypto"}]},
        {"title": "Predicted Fed rate under each Fed Chair", "volume": 157841,
         "endDate": "2026-12-31T00:00:00Z",
         "tags": [{"slug": "parlays"}, {"slug": "hide-from-new"}, {"slug": "fed-chair"}]},
        {"title": "All-noise example (forces Haiku fallback)", "volume": 5000,
         "endDate": "2026-08-01T00:00:00Z",
         "tags": [{"slug": "parlays"}, {"slug": "hit-first"}]},
    ]
    print("\nPOLYMARKET:")
    for s in poly_samples:
        cm, slugs = classify_poly(s)
        if cm is None:
            cm = classify_poly_llm_fallback(s)
            tag = "(haiku-fallback needed)"
        else:
            tag = f"via {slugs}"
        ok, why = passes_institutional_filter(cm, s["volume"], s["endDate"], "polymarket", now=NOW)
        print(f"  {('IN ' if ok else 'OUT'):3} [{cm or '??':12}] {why:28} | {s['title'][:40]:40} {tag}")

    print("\nRCG v2 engine check (expect C / C / B / C):")
    rcg_cases = {
        "Venezuela": {"trigger_objectivity": "pass", "contested_reality": "fail", "source_clarity": "partial",
                      "arbiter_incentive": "fail", "source_conflict": "fail", "temporal_precision": "pass", "source_mutability": "partial"},
        "Zelensky":  {"trigger_objectivity": "fail", "contested_reality": "pass", "source_clarity": "fail",
                      "arbiter_incentive": "fail", "source_conflict": "na", "temporal_precision": "pass", "source_mutability": "na"},
        "OPM":       {"trigger_objectivity": "pass", "contested_reality": "pass", "source_clarity": "pass",
                      "arbiter_incentive": "fail", "source_conflict": "na", "temporal_precision": "fail", "source_mutability": "partial"},
        "Ukraine":   {"trigger_objectivity": "pass", "contested_reality": "fail", "source_clarity": "partial",
                      "arbiter_incentive": "fail", "source_conflict": "na", "temporal_precision": "pass", "source_mutability": "fail"},
    }
    for nm, r in rcg_cases.items():
        res = resolution_clarity_grade(r)
        print(f"  {nm:10} score={res['score']:>3}  applied={res['applied_factors']}/7  caps={res['caps']}  -> {res['grade']}")


if __name__ == "__main__":
    _selftest()
