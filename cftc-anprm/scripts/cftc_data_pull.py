"""
CFTC ANPRM data pull (April 2026).

Two analyses:
  1. Polymarket resolution-source population, segmented by category.
     Verifies the v0.1.0 README's headline claim and breaks it apart by
     event type (sports vs. non-sports vs. macro etc.).
  2. Kalshi resolution-rule source-naming quality on a comparable sample.

Outputs JSON + a markdown summary to outputs/clearmarket/cftc-data-pull/.
"""
from __future__ import annotations

import json
import re
import time
import urllib.request
import urllib.error
from collections import defaultdict
from pathlib import Path

OUT = Path.home() / "jeremy-os/outputs/clearmarket/cftc-data-pull"
OUT.mkdir(parents=True, exist_ok=True)

UA = {"User-Agent": "clearmarket-research/0.1 (CFTC ANPRM comment data pull)"}

# ---------- Polymarket ----------
POLY_EVENTS = "https://gamma-api.polymarket.com/events"


def http_get(url: str, retries: int = 3, sleep: float = 1.0):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            if i == retries - 1:
                raise
            time.sleep(sleep * (2**i))
    return None


def pull_polymarket_events(target: int = 4000) -> list[dict]:
    """Pull active, non-closed Polymarket events with their nested markets."""
    out: list[dict] = []
    offset = 0
    page = 500
    while len(out) < target:
        url = (
            f"{POLY_EVENTS}?active=true&closed=false&limit={page}&offset={offset}"
            "&order=volume&ascending=false"
        )
        batch = http_get(url)
        if not batch:
            break
        out.extend(batch)
        if len(batch) < page:
            break
        offset += page
        time.sleep(0.4)
    return out


CATEGORY_KEYWORDS = {
    "sports": [
        "sports", "soccer", "football", "basketball", "baseball", "hockey",
        "tennis", "golf", "boxing", "mma", "ufc", "nba", "nfl", "mlb", "nhl",
        "epl", "premier league", "la liga", "champions league", "world cup",
        "olympics", "f1", "formula 1", "racing", "cricket", "rugby", "esports",
        "wnba", "atp", "wta", "ncaa", "march madness", "super bowl",
    ],
    "politics": [
        "politics", "election", "elections", "congress", "senate", "house",
        "white house", "presidency", "presidential", "primary", "midterms",
        "supreme court", "scotus", "cabinet", "governor", "mayor", "speaker",
        "trump", "biden", "harris", "republican", "democrat", "gop",
    ],
    "geopolitics": [
        "geopolitics", "war", "conflict", "ukraine", "russia", "china",
        "israel", "gaza", "iran", "north korea", "taiwan", "nato", "ceasefire",
        "hostage", "putin", "zelensky", "netanyahu", "khamenei", "diplomacy",
        "foreign", "international", "middle east",
    ],
    "macro": [
        "fed", "federal reserve", "fomc", "interest rate", "rate decision",
        "inflation", "cpi", "ppi", "unemployment", "jobs", "payroll",
        "gdp", "recession", "economy", "economic", "treasury", "yield",
        "ecb", "boe", "boj", "central bank", "macro", "finance", "stocks",
        "s&p", "nasdaq", "dow", "vix", "earnings",
    ],
    "crypto": [
        "crypto", "bitcoin", "btc", "ethereum", "eth", "solana", "sol",
        "xrp", "doge", "memecoin", "stablecoin", "blockchain", "defi",
        "nft", "altcoin", "microstrategy", "mstr", "coinbase",
    ],
    "culture": [
        "entertainment", "celebrity", "music", "movies", "film", "tv",
        "oscars", "grammys", "emmys", "golden globes", "awards", "billboard",
        "spotify", "netflix", "kardashian", "taylor swift", "kanye", "drake",
        "beyonce", "podcast", "youtube", "twitch", "tiktok",
    ],
    "tech_ai": [
        "ai", "artificial intelligence", "openai", "gpt", "anthropic",
        "claude", "google", "meta", "tesla", "spacex", "elon", "tech",
        "technology", "apple", "nvidia", "microsoft", "amazon",
    ],
    "weather_science": [
        "weather", "hurricane", "tornado", "earthquake", "climate",
        "temperature", "snow", "rain", "science", "space", "nasa",
    ],
}

# Order matters — sports/crypto are most specific so we check them first.
CATEGORY_ORDER = [
    "sports", "crypto", "macro", "politics", "geopolitics", "tech_ai",
    "culture", "weather_science",
]


def classify_event(event: dict) -> str:
    """Return a single primary category label."""
    tags = event.get("tags") or []
    title = (event.get("title") or "").lower()
    slug = (event.get("slug") or "").lower()
    label_blob = " ".join(
        ((t.get("label") or "") + " " + (t.get("slug") or "")).lower()
        for t in tags
    )
    blob = f"{title} {slug} {label_blob}"

    for cat in CATEGORY_ORDER:
        for kw in CATEGORY_KEYWORDS[cat]:
            # Word-boundary so "ai" doesn't match "main"
            if re.search(rf"\b{re.escape(kw)}\b", blob):
                return cat
    return "other"


PLACEHOLDER_PATTERNS = [
    r"consensus of (?:credible|verifiable|public|primary)",
    r"credible report(?:ing|s)",
    r"credible source",
    r"credible news",
    r"public report(?:ing|s)",
    r"primary source",
    r"reputable source",
    r"verifiable source",
    r"official source",
    r"authoritative source",
    r"reliable source",
    r"a consensus among",
    r"news reports",
    r"published reporting",
    r"primary reporting",
]
PLACEHOLDER_RE = re.compile("|".join(PLACEHOLDER_PATTERNS), re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s)\]]+", re.IGNORECASE)


def is_url(s: str | None) -> bool:
    if not s:
        return False
    return bool(URL_RE.search(s.strip()))


def has_placeholder(text: str | None) -> bool:
    if not text:
        return False
    return bool(PLACEHOLDER_RE.search(text))


def market_volume(m: dict) -> float:
    try:
        return float(m.get("volume") or m.get("volumeNum") or 0)
    except (TypeError, ValueError):
        return 0.0


def analyze_polymarket(events: list[dict]) -> dict:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    overall_markets = []

    for ev in events:
        cat = classify_event(ev)
        ev_resolution_source = (ev.get("resolutionSource") or "").strip()
        markets = ev.get("markets") or []
        for m in markets:
            if m.get("closed"):
                continue
            res_src = (m.get("resolutionSource") or "").strip()
            desc = m.get("description") or ""
            # An event-level resolution source counts toward population
            # only if the market itself doesn't override it.
            effective_src = res_src or ev_resolution_source
            row = {
                "question": m.get("question"),
                "category": cat,
                "resolutionSource_field_populated": bool(res_src),
                "resolutionSource_field_is_url": is_url(res_src),
                "event_resolutionSource_populated": bool(ev_resolution_source),
                "event_resolutionSource_is_url": is_url(ev_resolution_source),
                "effective_source_present": bool(effective_src),
                "effective_source_is_url": is_url(effective_src),
                "description_has_url": bool(URL_RE.search(desc)),
                "description_has_placeholder": has_placeholder(desc),
                "volume": market_volume(m),
            }
            by_cat[cat].append(row)
            overall_markets.append(row)

    def summarize(rows: list[dict]) -> dict:
        n = len(rows)
        if n == 0:
            return {"n": 0}
        total_vol = sum(r["volume"] for r in rows) or 1.0

        def pct(key):
            return round(100 * sum(1 for r in rows if r[key]) / n, 1)

        def vw_pct(key):
            return round(
                100 * sum(r["volume"] for r in rows if r[key]) / total_vol, 1
            )

        return {
            "n_markets": n,
            "total_volume_usd": round(total_vol, 0),
            "pct_market_resolutionSource_populated": pct(
                "resolutionSource_field_populated"
            ),
            "pct_market_resolutionSource_is_url": pct(
                "resolutionSource_field_is_url"
            ),
            "pct_event_resolutionSource_populated": pct(
                "event_resolutionSource_populated"
            ),
            "pct_effective_source_present": pct("effective_source_present"),
            "pct_effective_source_is_url": pct("effective_source_is_url"),
            "pct_description_has_url": pct("description_has_url"),
            "pct_description_has_placeholder": pct(
                "description_has_placeholder"
            ),
            "vw_pct_effective_source_is_url": vw_pct("effective_source_is_url"),
            "vw_pct_description_has_placeholder": vw_pct(
                "description_has_placeholder"
            ),
        }

    out = {"overall": summarize(overall_markets), "by_category": {}}
    for cat in sorted(by_cat.keys()):
        out["by_category"][cat] = summarize(by_cat[cat])
    return out


# ---------- Kalshi ----------
KALSHI_URL = "https://api.elections.kalshi.com/trade-api/v2/markets"


def pull_kalshi_markets(target: int = 3000) -> list[dict]:
    out: list[dict] = []
    cursor = ""
    while len(out) < target:
        url = f"{KALSHI_URL}?status=open&limit=1000"
        if cursor:
            url += f"&cursor={cursor}"
        page = http_get(url)
        if not page:
            break
        markets = page.get("markets") or []
        out.extend(markets)
        cursor = page.get("cursor") or ""
        if not cursor or not markets:
            break
        time.sleep(0.4)
    return out


def kalshi_classify(market: dict) -> str:
    """Classify a Kalshi market by its event_ticker prefix conventions."""
    ticker = (market.get("event_ticker") or market.get("ticker") or "").upper()
    sub = (market.get("sub_title") or "").lower()
    cat = (market.get("category") or "").lower()
    blob = f"{ticker} {sub} {cat}"

    if any(
        s in ticker
        for s in (
            "KX",
        )
    ):
        # Kalshi uses KX- prefixes on most product lines; look at sub_title.
        pass

    # Heuristic: rely on category field if present
    cat_map = {
        "economics": "macro", "financials": "macro",
        "politics": "politics", "world": "geopolitics",
        "sports": "sports", "crypto": "crypto",
        "climate and weather": "weather_science",
        "science and technology": "tech_ai",
        "entertainment": "culture",
    }
    if cat in cat_map:
        return cat_map[cat]

    # Fallback to keyword scan on sub_title
    for c in CATEGORY_ORDER:
        for kw in CATEGORY_KEYWORDS[c]:
            if re.search(rf"\b{re.escape(kw)}\b", blob):
                return c
    return "other"


def analyze_kalshi(markets: list[dict]) -> dict:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    rows_all = []

    for m in markets:
        cat = kalshi_classify(m)
        rules_primary = m.get("rules_primary") or ""
        rules_secondary = m.get("rules_secondary") or ""
        full_rules = f"{rules_primary}\n{rules_secondary}"
        row = {
            "ticker": m.get("ticker"),
            "category": cat,
            "rules_has_url": bool(URL_RE.search(full_rules)),
            "rules_has_placeholder": has_placeholder(full_rules),
            "rules_length": len(full_rules),
            "rules_short": len(full_rules) < 200,
        }
        by_cat[cat].append(row)
        rows_all.append(row)

    def summarize(rows):
        n = len(rows)
        if n == 0:
            return {"n": 0}

        def pct(key):
            return round(100 * sum(1 for r in rows if r[key]) / n, 1)

        return {
            "n_markets": n,
            "pct_rules_has_url": pct("rules_has_url"),
            "pct_rules_has_placeholder": pct("rules_has_placeholder"),
            "pct_rules_short": pct("rules_short"),
            "median_rules_length": int(
                sorted(r["rules_length"] for r in rows)[n // 2]
            ),
        }

    out = {"overall": summarize(rows_all), "by_category": {}}
    for cat in sorted(by_cat.keys()):
        out["by_category"][cat] = summarize(by_cat[cat])
    return out


# ---------- Driver ----------
def main():
    print("Pulling Polymarket events...", flush=True)
    poly_events = pull_polymarket_events(target=4000)
    print(f"  fetched {len(poly_events)} events", flush=True)
    (OUT / "polymarket-events-raw.json").write_text(json.dumps(poly_events))
    print("Analyzing Polymarket...", flush=True)
    poly_summary = analyze_polymarket(poly_events)
    (OUT / "polymarket-summary.json").write_text(
        json.dumps(poly_summary, indent=2)
    )

    print("Pulling Kalshi markets...", flush=True)
    kalshi_markets = pull_kalshi_markets(target=3000)
    print(f"  fetched {len(kalshi_markets)} markets", flush=True)
    (OUT / "kalshi-markets-raw.json").write_text(json.dumps(kalshi_markets))
    print("Analyzing Kalshi...", flush=True)
    kalshi_summary = analyze_kalshi(kalshi_markets)
    (OUT / "kalshi-summary.json").write_text(json.dumps(kalshi_summary, indent=2))

    summary = {
        "polymarket": poly_summary,
        "kalshi": kalshi_summary,
        "metadata": {
            "pulled_at": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
            "poly_events_pulled": len(poly_events),
            "kalshi_markets_pulled": len(kalshi_markets),
        },
    }
    (OUT / "combined-summary.json").write_text(json.dumps(summary, indent=2))
    print("Done. Output written to:", OUT, flush=True)


if __name__ == "__main__":
    main()
