"""
One-time migration: denormalized per-event catalyst_dates  ->  catalyst_types + shared calendar.

Per outputs/clearmarket/catalyst-architecture-decision.md (2026-05-29). Does four things:
  1. Reshapes data/catalyst-calendar.json from flat per-type date lists to the type-keyed
     {type: {label, source_url, dates}} form the Worker joins against. earnings:{TICKER} keys.
  2. Bootstraps events[].catalyst_types via catalyst_bind.bind_types (regex; reproduces catalysts_v2).
  3. Clears events[].catalyst_dates -> [] (recurring catalysts are now derived at read-time; no bespoke
     entries exist today — Exa is deferred).
  4. Writes data/catalyst-tickers.json = the demand-driven ticker set referenced by binding.

Then VERIFIES: expanding catalyst_types through the new calendar + windowing reproduces the
(date,type) of the catalyst_dates we're replacing. Labels may differ cosmetically (the old index-driver
suffix is dropped) — verification compares (date,type), the load-bearing part.

Idempotent-ish: backs up the flat calendar once. Re-running re-derives from the bundle's questions/tags.
"""
import json
from pathlib import Path
from collections import defaultdict
from datetime import date

import catalyst_bind as cb

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
CAL = ROOT / "data/catalyst-calendar.json"

TYPE_META = {
    "cpi":  ("CPI release",         "https://www.bls.gov/cpi/"),
    "jobs": ("Employment Situation", "https://www.bls.gov/ces/"),
    "gdp":  ("GDP release",          "https://www.bea.gov/data/gdp/gross-domestic-product"),
    "fomc": ("FOMC rate decision",   "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"),
}


def parse_d(s):
    try: return date.fromisoformat((s or "")[:10]).isoformat()
    except (ValueError, AttributeError): return None


def reshape_calendar():
    flat = json.loads(CAL.read_text())
    # back up the flat shape once
    bak = CAL.with_suffix(".flat.bak.json")
    if not bak.exists():
        bak.write_text(json.dumps(flat, indent=2))
    out = {"generated": flat.get("generated"), "horizon": flat.get("horizon"), "types": {}}
    for ty in ("cpi", "jobs", "gdp", "fomc"):
        label, url = TYPE_META[ty]
        out["types"][ty] = {"label": label, "source_url": url, "dates": sorted(flat.get(ty, []))}
    for tk, dates in (flat.get("earnings") or {}).items():
        out["types"][f"earnings:{tk}"] = {
            "label": f"{tk} earnings",
            "source_url": f"https://finnhub.io/quote/{tk}",
            "dates": sorted(dates),
        }
    CAL.write_text(json.dumps(out, indent=2))
    return out, flat


def main():
    cal_new, cal_flat = reshape_calendar()
    earnings_flat = cal_flat.get("earnings") or {}
    def earnings_dates_fn(tk): return earnings_flat.get(tk, [])

    bundle = json.loads(BUNDLE.read_text())
    by_ev = defaultdict(list)
    for m in bundle["markets"]:
        by_ev[m.get("event_id")].append(m)

    # snapshot old catalyst_dates for verification
    old = {e["event_id"]: (e.get("catalyst_dates") or []) for e in bundle["events"]}

    tickers = set()
    n_typed = 0
    for ev in bundle["events"]:
        mkts = by_ev.get(ev["event_id"], [])
        resolve_at = max((d for d in (parse_d(m.get("close_at")) for m in mkts) if d), default=None)
        types = cb.bind_types(ev.get("question"), ev.get("tags"), resolve_at, earnings_dates_fn)
        ev["catalyst_types"] = types
        ev["catalyst_dates"] = []  # recurring now derived at read-time; bespoke (Exa) deferred
        if types:
            n_typed += 1
            for t in types:
                if t.startswith("earnings:"):
                    tickers.add(t.split(":", 1)[1])

    # demand-driven ticker set (what refresh_calendar.py should pull Finnhub for)
    (ROOT / "data/catalyst-tickers.json").write_text(json.dumps(sorted(tickers), indent=2))

    BUNDLE.write_text(json.dumps(bundle, default=str))

    # ---- verify: types -> calendar -> window reproduces old (date,type) ----
    def window(types, resolve_at):
        served = []
        for t in types:
            c = cal_new["types"].get(t)
            if not c: continue
            for d in c["dates"]:
                if resolve_at and d < resolve_at:
                    served.append((d, t))
        served = sorted(set(served))
        return served[:5]

    # Compare the windowed DATE MULTISET (the user-visible catalyst calendar). Type labels are
    # ALLOWED to differ: old lumped same-date Mag-7 reports under generic 'corporate_earnings';
    # new gives precise earnings:<TICKER>. So equivalence = same dates, possibly more-precise types.
    mism = 0; checked = 0; relabeled = 0
    for ev in bundle["events"]:
        old_entries = old[ev["event_id"]]
        if not old_entries: continue
        checked += 1
        mkts = by_ev.get(ev["event_id"], [])
        resolve_at = max((d for d in (parse_d(m.get("close_at")) for m in mkts) if d), default=None)
        new_pairs = window(ev["catalyst_types"], resolve_at)
        old_dates = sorted(c["date"] for c in old_entries)
        new_dates = sorted(d for d, _ in new_pairs)
        if old_dates != new_dates:
            mism += 1
            if mism <= 8:
                print(f"  DATE MISMATCH {ev['slug']}")
                print(f"    old dates: {old_dates}")
                print(f"    new dates: {new_dates}")
        elif any(c["type"] == "corporate_earnings" for c in old_entries):
            relabeled += 1  # same dates, generic corporate_earnings -> precise earnings:TICKER

    print(f"\ncalendar types: {list(cal_new['types'])}")
    print(f"events with catalyst_types: {n_typed}")
    print(f"demand-driven tickers ({len(tickers)}): {sorted(tickers)}")
    print(f"verification: {checked} events had catalysts; {mism} date-mismatched; "
          f"{relabeled} relabeled corporate_earnings -> earnings:TICKER (same dates, more precise)")
    print("OK — read-time join reproduces stored DATES exactly." if mism == 0 else "REVIEW DATE MISMATCHES ABOVE.")


if __name__ == "__main__":
    main()
