"""
Catalyst calendar refresh — the MONTHLY job (per the approved cadence).

⚠️ STALE SHAPE — DO NOT RUN as-is (2026-05-29). This still emits the OLD FLAT shape
({cpi:[...], jobs:[...], earnings:{TICKER:[...]}}). The live architecture (see
outputs/clearmarket/catalyst-architecture-decision.md) uses the TYPE-KEYED shape
({types: {cpi: {label, source_url, dates}, "earnings:NVDA": {...}}}). Running this would
overwrite data/catalyst-calendar.json with the wrong shape and break the D1 calendar seed +
the Worker read-time join. POST-MVP TODO before re-enabling the monthly refresh:
  1. emit the type-keyed shape (reuse reshape logic in migrate_catalysts_to_types.py),
  2. pull Finnhub only for the demand-driven set in data/catalyst-tickers.json.
Until then the calendar is static (covers Jun–Dec 2026 — refresh before that runs out).

Fetches the dated scheduled-event calendar ONCE and caches it to data/catalyst-calendar.json:
  - FRED macro release dates (CPI / jobs / GDP)
  - curated FOMC decision days (Fed's official calendar)
  - Finnhub earnings dates for the tickers we map (Mag-7 + single names)
"""
import json, os, time
import requests
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
FRED_KEY, FINNHUB_KEY = os.getenv("FRED_API_KEY"), os.getenv("FINNHUB_API_KEY")
from datetime import date, timedelta
TODAY = date.today().isoformat()
HORIZON = (date.today() + timedelta(days=550)).isoformat()

FOMC = ["2026-06-17", "2026-07-29", "2026-09-16", "2026-10-28", "2026-12-09"]
MAG7 = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA"]
EXTRA_TICKERS = ["UBER", "MELI", "SNOW", "DELL", "AVGO", "MU", "MTN", "HOOD", "FUTU"]

# Authoritative published 2026 release schedules (BLS CPI/empsit, BEA GDP). Static for the year.
# Used as the fallback seed when FRED is unreachable (it's flaky) — FRED refresh only corrects reschedules.
SEED = {
    10: ["2026-06-10", "2026-07-14", "2026-08-12", "2026-09-11", "2026-10-14", "2026-11-10", "2026-12-10"],
    50: ["2026-06-05", "2026-07-02", "2026-08-07", "2026-09-04", "2026-10-02", "2026-11-06", "2026-12-04"],
    53: ["2026-06-25", "2026-07-30", "2026-08-26", "2026-09-30", "2026-10-29", "2026-11-25", "2026-12-23"],
}

def fred_dates(rid):
    last = None
    for _ in range(2):
        try:
            r = requests.get("https://api.stlouisfed.org/fred/release/dates",
                             params={"release_id": rid, "api_key": FRED_KEY, "file_type": "json",
                                     "include_release_dates_with_no_data": "true",  # future scheduled dates
                                     "sort_order": "desc", "limit": 40}, timeout=20)
            if r.status_code == 200:
                d = sorted(x["date"] for x in r.json().get("release_dates", []) if TODAY <= x["date"] <= HORIZON)
                if d:
                    return d
            last = f"HTTP {r.status_code}"
        except Exception as e:
            last = type(e).__name__
        time.sleep(4)
    print(f"  FRED release {rid} unreachable ({last}) — using published seed schedule")
    return [d for d in SEED[rid] if TODAY <= d <= HORIZON]

def earnings_dates(tk):
    r = requests.get("https://finnhub.io/api/v1/calendar/earnings",
                     params={"symbol": tk, "from": TODAY, "to": HORIZON, "token": FINNHUB_KEY}, timeout=30)
    return sorted(x["date"] for x in r.json().get("earningsCalendar", []) if x.get("date") and x["date"] >= TODAY) if r.ok else []

def main():
    cal = {"generated": TODAY, "horizon": HORIZON,
           "cpi": fred_dates(10), "jobs": fred_dates(50), "gdp": fred_dates(53),
           "fomc": [d for d in FOMC if d >= TODAY], "earnings": {}}
    for tk in MAG7 + EXTRA_TICKERS:
        cal["earnings"][tk] = earnings_dates(tk)
    out = ROOT / "data/catalyst-calendar.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(cal, indent=2))
    print(f"cached calendar → {out}")
    print(f"  CPI {len(cal['cpi'])} | jobs {len(cal['jobs'])} | GDP {len(cal['gdp'])} | FOMC {len(cal['fomc'])} | "
          f"earnings tickers {sum(1 for v in cal['earnings'].values() if v)}/{len(cal['earnings'])}")

if __name__ == "__main__":
    main()
