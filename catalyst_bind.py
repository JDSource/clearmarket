"""
Catalyst BINDING — which catalyst TYPES are prior movers for an event.

This is the semantic half of the catalyst layer (see
outputs/clearmarket/catalyst-architecture-decision.md, 2026-05-29). Binding emits a
list of catalyst TYPES; the Worker expands types -> dates from the shared calendar
and windows them at read-time. Types never carry dates — that keeps binding decoupled
from calendar refreshes.

Type vocabulary:
  macro:  "cpi" | "jobs" | "gdp" | "fomc"
  earnings: "earnings:<TICKER>"   (e.g. "earnings:NVDA")

This module is the regex BOOTSTRAP that reproduces catalysts_v2.py's binding 1:1
(including the 2026-05-29 foreign-CB + S&P-membership guards). On the next full
enrichment, the per-event Haiku call replaces bind_types() with LLM-quality binding
against the same vocabulary — drop-in, same output shape.
"""
import re

MAG7 = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA"]
NAME_TICKER = {"tesla": "TSLA", "apple": "AAPL", "microsoft": "MSFT", "google": "GOOGL", "alphabet": "GOOGL",
               "amazon": "AMZN", "nvidia": "NVDA", "meta": "META", "uber": "UBER", "mercadolibre": "MELI",
               "snowflake": "SNOW", "dell": "DELL", "broadcom": "AVGO", "micron": "MU", "vail": "MTN",
               "robinhood": "HOOD", "futu": "FUTU"}

INDEX_RE = re.compile(r"\b(s&p|s and p|sp500|spx|s&p 500|nasdaq|dow jones|russell)\b")
INDEX_MEMBER_RE = re.compile(r"\b(s&p 500|sp500|nasdaq)\s+compan|"
                             r"(added to|join\w*|removed from|drop\w* from) the (s&p|nasdaq|dow)")
MACRO_RE = re.compile(r"\b(fed|fomc|inflation|cpi|gdp|unemployment|recession|interest rate|rate cut|"
                      r"rate hike|jobs report|nonfarm|payroll)\b")
PERSONNEL_RE = re.compile(r"\b(chair|fire|fired|firing|nominat\w*|appoint\w*|resign\w*|depart\w*|replace\w*|"
                          r"oust\w*|step down|stepping down|successor)\b")
FOREIGN_RE = re.compile(r"\b(boj|bank of japan|ecb|european central bank|euro ?zone|euro area|"
                        r"boe|bank of england|bank of canada|bank of mexico|banxico|"
                        r"pboc|people'?s bank of china|rba|reserve bank of (australia|india)|rbi|"
                        r"swiss national bank|snb|argentin\w*|brazil\w*|turk(ey|ish)|japan\w*|"
                        r"mexic\w*|canad\w*|chin(a|ese)|india\b|indian\b|britain|british|"
                        r"united kingdom|australia\w*|russia\w*)\b")
FINANCIAL_RE = re.compile(r"\b(earnings|revenue|sales|profit|eps|deliver|production|produce|guidance|"
                          r"beat|subscribers|margin|income|quarter|q[1-4]|market cap|valuation)\b")


def ticker_for(t):
    for name, tk in NAME_TICKER.items():
        if re.search(rf"\b{re.escape(name)}\b", t):  # word-boundary: "gubernatorial" must not match "uber"
            return tk
    return None


def bind_types(question, tags=None, resolve_at=None, earnings_dates_fn=None):
    """Return the catalyst TYPES (prior movers) for an event. Reproduces catalysts_v2.

    question:          event question string
    tags:              list[str] (matched into the macro/index text, NOT into INDEX_MEMBER)
    resolve_at:        ISO date string (event resolution = max close_at). Needed only for the
                       single-stock >=2-reports rule; macro/index binding ignores it.
    earnings_dates_fn: optional fn(ticker) -> list[ISO date]. Needed only for the single-stock
                       rule. If None, the single-stock earnings branch is skipped (dormant => 0,
                       matching production reality).
    """
    q = (question or "").lower()
    t = (q + " " + " ".join(tags or [])).lower()
    types = []

    # macro / rate markets — not personnel, not foreign central banks
    if MACRO_RE.search(t) and not PERSONNEL_RE.search(t) and not FOREIGN_RE.search(t):
        types += ["cpi", "jobs", "gdp", "fomc"]

    # index-level markets — Mag-7 "index driver" earnings + macro (cpi/fomc). Not membership markets.
    if INDEX_RE.search(t) and not INDEX_MEMBER_RE.search(q):
        types += ["cpi", "fomc"]
        types += [f"earnings:{tk}" for tk in MAG7]

    # single-stock financial-metric markets — that ticker's earnings, ONLY if >=2 reports before
    # resolution (a single report that settles the market is the resolution, not a catalyst).
    tk = ticker_for(t)
    if tk and FINANCIAL_RE.search(t) and resolve_at and earnings_dates_fn:
        before = [d for d in earnings_dates_fn(tk) if d < resolve_at]
        if len(before) >= 2:
            types.append(f"earnings:{tk}")

    # dedupe, preserve order
    seen = set()
    return [x for x in types if not (x in seen or seen.add(x))]
