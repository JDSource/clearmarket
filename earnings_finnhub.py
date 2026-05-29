"""
Earnings catalyst dates via Finnhub (free /calendar/earnings) — vendor-of-record provenance.
Replaces the Exa-scraping approach (mixed-authority sources). ONE call returns the upcoming
earnings calendar; we filter to our tickers + take the soonest per ticker. Needs FINNHUB_API_KEY.

Dry-run (no key): prints the event→ticker mapping so it's verifiable now. With key: populates
catalyst_dates + writes back to the bundle. Reads/writes web/data/universe-enriched-linked.json.
"""
import json, os, re, requests
from datetime import date, timedelta
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
KEY = os.getenv("FINNHUB_API_KEY")

# company name (lowercase substring) -> ticker, for the earnings-classified events
NAME_TICKER = {
    "tesla": "TSLA", "uber": "UBER", "mercadolibre": "MELI", "snowflake": "SNOW",
    "dell": "DELL", "broadcom": "AVGO", "micron": "MU", "vail": "MTN",
    "robinhood": "HOOD", "futu": "FUTU",
}

def ticker_for(q):
    ql = (q or "").lower()
    for name, tk in NAME_TICKER.items():
        if name in ql:
            return tk
    return None

def is_earnings(ev):
    t = ((ev.get("question") or "") + " " + " ".join(ev.get("tags") or [])).lower()
    if re.search(r"\b(cpi|inflation|jobs report|nonfarm|unemployment|gdp|gross domestic|ppi|producer price|fomc|fed rate|federal reserve|rate cut|rate hike|interest rate)\b", t):
        return False
    return bool(re.search(r"\b(earnings|revenue|eps|deliver|production|trip volume|skier visits|funded accounts|customers)\b", t))

def main():
    path = ROOT / "web/data/universe-enriched-linked.json"
    bundle = json.loads(path.read_text())
    targets = [(e, ticker_for(e.get("question", ""))) for e in bundle["events"] if is_earnings(e)]
    mapped = [(e, tk) for e, tk in targets if tk]
    print(f"earnings-classified events: {len(targets)} | mapped to a ticker: {len(mapped)}")
    for e, tk in targets:
        print(f"  {tk or '—(no ticker)':6}  {e.get('question','')[:55]!r}")

    if not KEY:
        print("\nFINNHUB_API_KEY not set — DRY RUN (mapping above). Add the key + re-run to populate.")
        return

    # per-ticker (symbol-filtered) avoids the free-tier 1,500-row cap that truncated near-term dates
    frm = date.today().isoformat()
    to = (date.today() + timedelta(days=365)).isoformat()
    next_date = {}
    for tk in sorted({t for _, t in mapped}):
        r = requests.get("https://finnhub.io/api/v1/calendar/earnings",
                         params={"symbol": tk, "from": frm, "to": to, "token": KEY}, timeout=20)
        up = sorted(x["date"] for x in r.json().get("earningsCalendar", []) if x.get("date") and x["date"] >= frm)
        if up:
            next_date[tk] = up[0]

    pop = 0
    for e, tk in mapped:
        d = next_date.get(tk)
        if d:
            e["catalyst_dates"] = [{"date": d, "type": "corporate_earnings",
                                    "label": f"{tk} earnings (Finnhub)", "source_url": f"https://finnhub.io/quote/{tk}"}]
            pop += 1
            print(f"  {tk} -> {d}")
    path.write_text(json.dumps(bundle, default=str))
    print(f"\npopulated {pop}/{len(mapped)} earnings events (Finnhub vendor-of-record).")

if __name__ == "__main__":
    main()
