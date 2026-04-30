"""
Kalshi re-pull via events endpoint (with_nested_markets=true).

The /markets endpoint returns rules_primary/rules_secondary as empty strings.
The /events?with_nested_markets=true endpoint includes rules text on
each nested market. Re-running with this corrected source.
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
UA = {"User-Agent": "clearmarket-research/0.1 (CFTC ANPRM comment data pull)"}

URL_RE = re.compile(r"https?://[^\s)\]]+", re.IGNORECASE)
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
    r"for example",   # Kalshi-specific weak naming
]
PLACEHOLDER_RE = re.compile("|".join(PLACEHOLDER_PATTERNS), re.IGNORECASE)


# Kalshi categories normalized to the same buckets as the Polymarket script
KALSHI_CAT_MAP = {
    "politics": "politics",
    "elections": "politics",
    "economics": "macro",
    "financials": "macro",
    "companies": "macro",
    "world": "geopolitics",
    "sports": "sports",
    "crypto": "crypto",
    "climate and weather": "weather_science",
    "science and technology": "tech_ai",
    "entertainment": "culture",
    "health": "weather_science",
    "social": "culture",
    "transportation": "other",
}


def http_get(url: str, retries: int = 3, sleep: float = 1.0):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
            if i == retries - 1:
                raise
            time.sleep(sleep * (2**i))
    return None


def pull_kalshi_events(target_events: int = 1500) -> list[dict]:
    out: list[dict] = []
    cursor = ""
    base = (
        "https://api.elections.kalshi.com/trade-api/v2/events"
        "?status=open&limit=200&with_nested_markets=true"
    )
    while len(out) < target_events:
        url = base + (f"&cursor={cursor}" if cursor else "")
        page = http_get(url)
        if not page:
            break
        events = page.get("events") or []
        if not events:
            break
        out.extend(events)
        cursor = page.get("cursor") or ""
        if not cursor:
            break
        time.sleep(0.5)
    return out


def has_url(s: str | None) -> bool:
    if not s:
        return False
    return bool(URL_RE.search(s))


def has_placeholder(s: str | None) -> bool:
    if not s:
        return False
    return bool(PLACEHOLDER_RE.search(s))


def has_named_authoritative_source(s: str) -> bool:
    """Kalshi often names a source by name without a URL."""
    if not s:
        return False
    # Common Kalshi-cited sources
    named_sources = [
        r"\bBLS\b", r"Bureau of Labor Statistics",
        r"Federal Reserve", r"\bFOMC\b", r"\bFed\b",
        r"S&P Dow Jones", r"\bS&P\b 500", r"\bSPX\b",
        r"\bAP\b\b", r"Associated Press",
        r"Reuters", r"Bloomberg", r"FactSet", r"Refinitiv",
        r"NYSE", r"NASDAQ", r"\bSEC\b", r"\bDOJ\b", r"\bBEA\b",
        r"NCAA", r"\bNFL\b", r"\bNBA\b", r"\bMLB\b", r"\bNHL\b",
        r"Census Bureau", r"\bCBO\b", r"\bIRS\b",
        r"NOAA", r"National Weather Service", r"\bNWS\b",
        r"Coinbase", r"CoinMarketCap", r"CoinGecko",
        r"Box Office Mojo", r"Billboard",
    ]
    return any(re.search(p, s) for p in named_sources)


def analyze(events: list[dict]) -> dict:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    rows_all: list[dict] = []

    for ev in events:
        cat_raw = (ev.get("category") or "").strip().lower()
        cat = KALSHI_CAT_MAP.get(cat_raw, "other")
        markets = ev.get("markets") or []
        for m in markets:
            if m.get("status") != "active" and m.get("status") != "open":
                # Some events have non-active markets; only count actively-listed.
                pass  # Kalshi 'open' status is the relevant one; let's keep all
            rules_p = m.get("rules_primary") or ""
            rules_s = m.get("rules_secondary") or ""
            full_rules = f"{rules_p}\n{rules_s}"
            row = {
                "ticker": m.get("ticker"),
                "category": cat,
                "category_raw": cat_raw,
                "rules_has_url": has_url(full_rules),
                "rules_has_placeholder": has_placeholder(full_rules),
                "rules_has_named_source": has_named_authoritative_source(
                    full_rules
                ),
                "rules_length": len(full_rules),
                "rules_short": len(full_rules) < 200,
                "volume": float(m.get("volume_fp") or 0),
            }
            by_cat[cat].append(row)
            rows_all.append(row)

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
            "total_volume_contracts": int(total_vol),
            "pct_rules_has_url": pct("rules_has_url"),
            "pct_rules_has_named_source": pct("rules_has_named_source"),
            "pct_rules_has_url_or_named_source": round(
                100
                * sum(
                    1
                    for r in rows
                    if r["rules_has_url"] or r["rules_has_named_source"]
                )
                / n,
                1,
            ),
            "pct_rules_has_placeholder": pct("rules_has_placeholder"),
            "pct_rules_short": pct("rules_short"),
            "median_rules_length": int(
                sorted(r["rules_length"] for r in rows)[n // 2]
            ),
            "vw_pct_rules_has_url_or_named_source": round(
                100
                * sum(
                    r["volume"]
                    for r in rows
                    if r["rules_has_url"] or r["rules_has_named_source"]
                )
                / total_vol,
                1,
            ),
            "vw_pct_rules_has_placeholder": vw_pct("rules_has_placeholder"),
        }

    out = {"overall": summarize(rows_all), "by_category": {}}
    for cat in sorted(by_cat.keys()):
        out["by_category"][cat] = summarize(by_cat[cat])
    return out


def main():
    raw_path = OUT / "kalshi-events-raw.json"
    if raw_path.exists():
        print(f"Reusing existing pull: {raw_path}", flush=True)
        events = json.loads(raw_path.read_text())
        print(f"  loaded {len(events)} events", flush=True)
    else:
        print("Pulling Kalshi events with nested markets...", flush=True)
        events = pull_kalshi_events(target_events=1500)
        print(f"  fetched {len(events)} events", flush=True)
        raw_path.write_text(json.dumps(events))
    print("Analyzing Kalshi...", flush=True)
    summary = analyze(events)
    (OUT / "kalshi-summary-v2.json").write_text(json.dumps(summary, indent=2))
    print("Done.", flush=True)
    print(json.dumps(summary["overall"], indent=2))


if __name__ == "__main__":
    main()
