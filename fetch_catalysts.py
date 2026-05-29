"""
Catalyst pipeline — thin MVP (task #3). Populates events[].catalyst_dates.

Sources (all verified working 2026-05-28):
  - FRED  → macro release dates (CPI/jobs/GDP/PPI), keyed, shared-per-catalyst (1 call/release).
  - [next increments] API Ninjas → earnings (per-ticker, near-term); Exa → ad-hoc/evolving (cap 75/day);
    FOMC meeting dates → curated/Exa (FRED has no FOMC-meeting release).

Deterministic classifier routes each event to a catalyst type; most → `none` (no call, no date).
catalyst_dates shape: {date, type, label, source_url}. Reads/writes web/data/universe-enriched-linked.json.
"""
import json, os, re, requests
from collections import Counter
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
FRED_KEY = os.getenv("FRED_API_KEY")
FRED = "https://api.stlouisfed.org/fred"
TODAY = date.today().isoformat()

# release_id -> (catalyst type, label, source_url)
FRED_RELEASES = {
    10: ("cpi",  "CPI release",                        "https://www.bls.gov/cpi/"),
    50: ("jobs", "Employment Situation (jobs report)", "https://www.bls.gov/ces/"),
    53: ("gdp",  "GDP release",                        "https://www.bea.gov/data/gdp/gross-domestic-product"),
    46: ("ppi",  "PPI release",                        "https://www.bls.gov/ppi/"),
}
TYPE_RELEASE = {v[0]: rid for rid, v in FRED_RELEASES.items()}

# FOMC meeting dates aren't a FRED "release" — curated from the Fed's official calendar
# (federalreserve.gov FOMC calendar, fetched 2026-05-28). Date = decision day (2nd day).
FOMC_2026 = ["2026-01-28", "2026-03-18", "2026-04-29", "2026-06-17",
             "2026-07-29", "2026-09-16", "2026-10-28", "2026-12-09"]
FOMC_URL = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
NEXT_FOMC = next((d for d in FOMC_2026 if d >= TODAY), None)

_next = {}
def next_release_date(rid):
    """Soonest upcoming release date for a FRED release_id (cached — shared per catalyst)."""
    if rid in _next:
        return _next[rid]
    r = requests.get(f"{FRED}/release/dates", params={
        "release_id": rid, "api_key": FRED_KEY, "file_type": "json",
        "include_release_dates_with_no_data": "true", "sort_order": "asc", "limit": 2000}, timeout=25)
    dates = sorted(x["date"] for x in r.json().get("release_dates", []))
    upcoming = [d for d in dates if d >= TODAY]
    _next[rid] = upcoming[0] if upcoming else None
    return _next[rid]

def classify(ev):
    t = ((ev.get("question") or "") + " " + " ".join(ev.get("tags") or [])).lower()
    if re.search(r"\b(cpi|consumer price|inflation)\b", t):                         return "cpi"
    if re.search(r"\b(jobs report|nonfarm|unemployment|employment situation|payroll)\b", t): return "jobs"
    if re.search(r"\bgdp\b|gross domestic", t):                                     return "gdp"
    if re.search(r"\b(ppi|producer price)\b", t):                                   return "ppi"
    if re.search(r"\b(fomc|fed rate|federal reserve|rate cut|rate hike|interest rate)\b", t): return "fomc"
    if re.search(r"\b(earnings|revenue|eps)\b", t):                                 return "corporate_earnings"
    return "none"

def main():
    path = ROOT / "web/data/universe-enriched-linked.json"
    bundle = json.loads(path.read_text())
    events = bundle["events"]

    types = Counter()
    populated = 0
    samples = []
    earnings_events = []
    for ev in events:
        ct = classify(ev)
        types[ct] += 1
        cds = []
        if ct in TYPE_RELEASE:
            d = next_release_date(TYPE_RELEASE[ct])
            if d:
                typ, label, url = FRED_RELEASES[TYPE_RELEASE[ct]]
                cds.append({"date": d, "type": typ, "label": f"Next {label}", "source_url": url})
        elif ct == "fomc" and NEXT_FOMC:
            cds.append({"date": NEXT_FOMC, "type": "fomc", "label": "FOMC rate decision", "source_url": FOMC_URL})
        elif ct == "corporate_earnings":
            earnings_events.append(ev.get("question", "")[:70])  # collect for assessment (API Ninjas per-ticker = next)
        ev["catalyst_dates"] = cds  # [] for none/unpopulated
        if cds:
            populated += 1
            if len(samples) < 8:
                samples.append((ev.get("question", "")[:50], cds[0]["type"], cds[0]["date"]))

    print("classifier type distribution:", dict(types))
    print(f"events with catalyst_dates populated: {populated}  (FRED macro + FOMC)")
    print("FRED next dates:", {FRED_RELEASES[r][0]: d for r, d in _next.items()}, "| next FOMC:", NEXT_FOMC)
    print("\nsamples:")
    for q, typ, d in samples:
        print(f"  [{typ}] {d}  {q!r}")

    print(f"\nearnings events (need API Ninjas per-ticker — not yet populated): {len(earnings_events)}")
    for q in earnings_events[:14]:
        print(f"    {q!r}")

    path.write_text(json.dumps(bundle, default=str))
    print(f"\nwrote catalyst_dates back to {path.name}")

if __name__ == "__main__":
    main()
