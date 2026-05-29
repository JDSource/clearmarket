"""
Catalysts v2 — category-specific PRIOR-MOVER model (per Jeremy's mapping, 2026-05-28).

A catalyst = a scheduled event that moves a market BEFORE its resolution. Attach a catalyst only
if (a) it's relevant to the market's category/subject AND (b) it falls strictly BEFORE the event's
resolution date (max close_at across its markets). Resolution-coincident dates are NOT catalysts
(that's the venue's close date). Multiple prior movers per market are expected (a year-out market
lists the next several). Soonest ~5 kept.

Mapping (core, all sources wired):
  economics / rates  -> CPI, jobs, GDP, FOMC (FRED + curated)
  financials (index) -> Mag-7 earnings + CPI/jobs/FOMC (Finnhub + FRED)
  companies / tech    -> that company's earnings (Finnhub)
  geopolitics/politics-> Exa residual (separate: evolving_exa.py)  | crypto/climate/health -> none (FDA = fast-follow)

Reads/writes web/data/universe-enriched-linked.json. Shows the corrected set; HOLDS D1 push.
"""
import json, re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
TODAY = date.today().isoformat()

CPI_URL = "https://www.bls.gov/cpi/"; JOBS_URL = "https://www.bls.gov/ces/"
GDP_URL = "https://www.bea.gov/data/gdp/gross-domestic-product"
FOMC_URL = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
FH = lambda tk: f"https://finnhub.io/quote/{tk}"

MAG7 = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA"]
NAME_TICKER = {"tesla": "TSLA", "apple": "AAPL", "microsoft": "MSFT", "google": "GOOGL", "alphabet": "GOOGL",
               "amazon": "AMZN", "nvidia": "NVDA", "meta": "META", "uber": "UBER", "mercadolibre": "MELI",
               "snowflake": "SNOW", "dell": "DELL", "broadcom": "AVGO", "micron": "MU", "vail": "MTN",
               "robinhood": "HOOD", "futu": "FUTU"}
INDEX_RE = re.compile(r"\b(s&p|s and p|sp500|spx|s&p 500|nasdaq|dow jones|russell)\b")
# "S&P 500" used as a company qualifier ("an S&P 500 company buys BTC", "added to the S&P 500") is a
# membership/corporate-action market, NOT an index-level bet — index drivers (Mag-7 earnings, CPI/FOMC)
# don't move it. Matched against the QUESTION only (tags like "sp500 stock-market" create false adjacency).
INDEX_MEMBER_RE = re.compile(r"\b(s&p 500|sp500|nasdaq)\s+compan|"
                             r"(added to|join\w*|removed from|drop\w* from) the (s&p|nasdaq|dow)")
# Genuine macro subjects only (not the whole 'economics' category — that sweeps in IPO/tax/productivity markets
# that no CPI print moves). \bfed\b won't match "federal"; bare "rate" excluded (matches "approval rate" etc.).
MACRO_RE = re.compile(r"\b(fed|fomc|inflation|cpi|gdp|unemployment|recession|interest rate|rate cut|rate hike|jobs report|nonfarm|payroll)\b")
# Earnings is a catalyst only for FINANCIAL-METRIC company markets (deliveries/revenue/EPS…), not for
# product-release or corporate-action markets (foldable iPhone, Llama 5, merger, CEO-out) — those move on
# keynotes/M&A announcements we don't track, so they stay none.
FINANCIAL_RE = re.compile(r"\b(earnings|revenue|sales|profit|eps|deliver|production|produce|guidance|"
                          r"beat|subscribers|margin|income|quarter|q[1-4]|market cap|valuation)\b")
# Fed *personnel* markets (who chairs/fire/nominate/departure) match "fed/fomc" but aren't moved by CPI/jobs —
# the outcome is a political appointment. Suppress macro for these; rate/policy Fed markets keep it.
PERSONNEL_RE = re.compile(r"\b(chair|fire|fired|firing|nominat\w*|appoint\w*|resign\w*|depart\w*|replace\w*|"
                          r"oust\w*|step down|stepping down|successor)\b")
# Foreign central banks / economies match MACRO_RE via generic "interest rate"/"inflation" but are NOT
# moved by US CPI/jobs/FOMC. Per Jeremy 2026-05-29: leave these BLANK for MVP (no US pack; no foreign
# calendar wired yet). US Fed markets say "fed"/"federal reserve"/"fomc" and won't match this.
FOREIGN_RE = re.compile(r"\b(boj|bank of japan|ecb|european central bank|euro ?zone|euro area|"
                        r"boe|bank of england|bank of canada|bank of mexico|banxico|"
                        r"pboc|people'?s bank of china|rba|reserve bank of (australia|india)|rbi|"
                        r"swiss national bank|snb|argentin\w*|brazil\w*|turk(ey|ish)|japan\w*|"
                        r"mexic\w*|canad\w*|chin(a|ese)|india\b|indian\b|britain|british|"
                        r"united kingdom|australia\w*|russia\w*)\b")

# Read the cached calendar (refreshed monthly by refresh_calendar.py). ZERO live macro calls here.
_cal_path = ROOT / "data/catalyst-calendar.json"
if not _cal_path.exists():
    raise SystemExit("data/catalyst-calendar.json missing — run refresh_calendar.py first (the monthly job).")
CAL = json.loads(_cal_path.read_text())
CPI, JOBS, GDP, FOMC = CAL["cpi"], CAL["jobs"], CAL["gdp"], CAL["fomc"]
EARN = CAL["earnings"]
def earnings_dates(tk):
    return EARN.get(tk, [])
print(f"calendar cached {CAL['generated']} | CPI {len(CPI)} jobs {len(JOBS)} GDP {len(GDP)} FOMC {len(FOMC)} | "
      f"earnings tickers {sum(1 for v in EARN.values() if v)}/{len(EARN)}")

def parse_d(s):
    try: return date.fromisoformat((s or "")[:10]).isoformat()
    except (ValueError, AttributeError): return None

def ticker_for(t):
    for name, tk in NAME_TICKER.items():
        if re.search(rf"\b{re.escape(name)}\b", t):  # word-boundary: "gubernatorial" must not match "uber"
            return tk
    return None

def build():
    bundle = json.loads((ROOT / "web/data/universe-enriched-linked.json").read_text())
    by_ev = defaultdict(list)
    for m in bundle["markets"]:
        by_ev[m.get("event_id")].append(m)

    counts = defaultdict(int); samples = []; multi = 0
    for ev in bundle["events"]:
        mkts = by_ev.get(ev["event_id"], [])
        res = max((d for d in (parse_d(m.get("close_at")) for m in mkts) if d), default=None)
        cds = []
        if res:
            q = (ev.get("question") or "").lower()
            t = (q + " " + " ".join(ev.get("tags") or [])).lower()
            pool = []  # (date, type, label, url)
            # rate/policy Fed markets, not personnel, not foreign central banks
            if MACRO_RE.search(t) and not PERSONNEL_RE.search(t) and not FOREIGN_RE.search(t):
                pool += [(d, "cpi", "CPI release", CPI_URL) for d in CPI]
                pool += [(d, "jobs", "Employment Situation", JOBS_URL) for d in JOBS]
                pool += [(d, "gdp", "GDP release", GDP_URL) for d in GDP]
                pool += [(d, "fomc", "FOMC rate decision", FOMC_URL) for d in FOMC]
            if INDEX_RE.search(t) and not INDEX_MEMBER_RE.search(q):  # index markets → Mag-7 earnings + macro
                for tk in MAG7:
                    pool += [(d, "corporate_earnings", f"{tk} earnings (index driver)", FH(tk)) for d in earnings_dates(tk)]
                pool += [(d, "cpi", "CPI release", CPI_URL) for d in CPI]
                pool += [(d, "fomc", "FOMC rate decision", FOMC_URL) for d in FOMC]
            tk = ticker_for(t)  # single-stock markets → earnings, ONLY as prior movers (horizon markets)
            if tk and FINANCIAL_RE.search(t):
                before = [d for d in earnings_dates(tk) if d < res]
                if len(before) >= 2:  # ≥2 reports before resolution = genuine prior movers; a single report
                    pool += [(d, "corporate_earnings", f"{tk} earnings", FH(tk)) for d in before]  # IS the resolution
            # prior movers only: strictly before resolution; soonest 5, deduped
            pool = sorted({p for p in pool if p[0] < res})[:5]
            cds = [{"date": d, "type": ty, "label": lb, "source_url": u} for d, ty, lb, u in pool]
        ev["catalyst_dates"] = cds
        if cds:
            counts[ev.get("category")] += 1
            if len(cds) > 1:
                multi += 1
            if len(samples) < 10:
                samples.append((ev.get("question", "")[:46], res, [c["type"] + ":" + c["date"] for c in cds]))

    total = sum(counts.values())
    print(f"\nevents with TRUE (prior-mover) catalysts: {total}  (multi-catalyst events: {multi})")
    print("by category:", dict(counts))
    print("\nsamples (event | resolves | prior-mover catalysts):")
    for q, res, cs in samples:
        print(f"  {q!r:48} res={res}  {cs}")
    (ROOT / "web/data/universe-enriched-linked.json").write_text(json.dumps(bundle, default=str))
    print("\nwrote catalyst_dates (HELD from D1 — review the corrected set).")

if __name__ == "__main__":
    build()
