#!/usr/bin/env python3
"""
ClearMarket — universe fetcher.

Pulls the full Kalshi + Polymarket universe from their PUBLIC read APIs
(no key, no spend), runs every event through the institutional filter +
category classifier in `classify.py`, and writes the filtered institutional
set to disk for enhance.py to enrich.

Build item #1 in `now.md`; feeds checklist items #2-3 + the prompt gate (#11)
in `schema-source-of-truth-decision.md`.

Outputs (under raw/clearmarket-universe-<date>/):
  kalshi-institutional.json     — kept Kalshi events (raw + cm_* annotations)
  poly-institutional.json       — kept Poly events
  poly-needs-classification.json— Poly events whose tags didn't map (Haiku gate)
  manifest.json                 — run stats: counts, drop reasons, category mix

Usage:
  python3 fetch_universe.py --smoke      # one page each, write to a _smoke dir, print summary
  python3 fetch_universe.py --limit 500  # cap total events per venue (testing)
  python3 fetch_universe.py              # full universe pull
"""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

from classify import (
    classify_kalshi, classify_poly, classify_poly_llm_fallback,
    passes_institutional_filter, CATEGORIES_IN,
)

# -----------------------------------------------------------------
# API endpoints (public read; no auth)
# -----------------------------------------------------------------
# If Kalshi 404s, the legacy base is https://trading-api.kalshi.com/trade-api/v2
KALSHI_BASE = "https://api.elections.kalshi.com/trade-api/v2"
POLY_GAMMA  = "https://gamma-api.polymarket.com"

PAGE_KALSHI = 200      # Kalshi /events page size (max 200)
PAGE_POLY   = 100      # Poly Gamma /events page size — Gamma CAPS at 100; requesting
                       # more returns 100 and would false-trip the "last page" check.
MAX_PAGES   = 1000     # safety stop
TIMEOUT     = 30

OUT_ROOT = Path.home() / "jeremy-os/raw"
RUN_DATE = datetime.now(timezone.utc).strftime("%Y-%m-%d")


RETRY_STATUSES = {429, 500, 502, 503, 504}


def _get(url: str, params: dict, tries: int = 4) -> dict:
    """Bounded retries with backoff for transient failures. 422 propagates immediately —
    it is Gamma's offset-cap signal and the pager's bisect trigger, never a retry case."""
    for attempt in range(tries):
        try:
            r = requests.get(url, params=params, timeout=TIMEOUT,
                             headers={"User-Agent": "clearmarket-fetcher/0.1"})
            r.raise_for_status()
            return r.json()
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as e:
            status = getattr(getattr(e, "response", None), "status_code", None)
            if status == 422 or attempt == tries - 1 or \
                    (status is not None and status not in RETRY_STATUSES):
                raise
            wait = 2.0 ** attempt
            if status == 429 and e.response is not None:
                wait = max(wait, float(e.response.headers.get("Retry-After", 0) or 0))
            time.sleep(wait)


# -----------------------------------------------------------------
# Kalshi: paginate /events with nested markets (events carry `category`)
# -----------------------------------------------------------------
def fetch_kalshi_events(max_events: int | None, max_pages: int = MAX_PAGES) -> list[dict]:
    events: list[dict] = []
    cursor = None
    for _ in range(max_pages):
        params = {"limit": PAGE_KALSHI, "status": "open", "with_nested_markets": "true"}
        if cursor:
            params["cursor"] = cursor
        data = _get(f"{KALSHI_BASE}/events", params)
        batch = data.get("events", [])
        events.extend(batch)
        cursor = data.get("cursor")
        if not batch or not cursor or (max_events and len(events) >= max_events):
            break
    return events[:max_events] if max_events else events


def kalshi_event_volume_usd(event: dict) -> float:
    """Coarse USD volume proxy = sum over nested markets of cumulative
    contracts (`volume_fp`) * `last_price_dollars`. Field names match the
    Kalshi nested-market payload (same suffixes enhance.py uses). Already in
    dollars — no /100. Threshold tuning is TODO (now.md)."""
    total = 0.0
    for m in event.get("markets", []) or []:
        vol = m.get("volume_fp") or 0              # cumulative contracts
        last = m.get("last_price_dollars")         # already in dollars
        if last is None:
            continue
        total += float(vol) * float(last)
    return total


def kalshi_event_resolve_at(event: dict) -> str | None:
    """Latest close_time across nested markets (or event strike_date)."""
    times = [m.get("close_time") for m in (event.get("markets") or []) if m.get("close_time")]
    if event.get("strike_date"):
        times.append(event["strike_date"])
    return max(times) if times else None


# -----------------------------------------------------------------
# Polymarket: paginate Gamma /events (events carry tags[] + volume + endDate)
# -----------------------------------------------------------------
def fetch_poly_events(max_events: int | None, max_pages: int = MAX_PAGES) -> list[dict]:
    # Gamma hard-caps offsets (~2000 as of 2026-07: deeper pages 422), so a single
    # offset walk can no longer cover the open set. Page inside end-date windows
    # instead — every window is DOUBLE-bounded (Gamma excludes null-endDate events
    # from any end_date-filtered query, and unbounded windows can't bisect) — with
    # recursive bisection on the offset cap and dedup on event id across boundaries.
    # First window catches past-due-but-open events; the last is capped at a far-future
    # constant so far-dated listings are never silently dropped. A final UNWINDOWED
    # offset walk (up to the cap) recovers null-endDate events, which no date-filtered
    # window can ever return (2026-07-24 swarm finding: 48+ live events, $10M+ volume).
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)
    events: list[dict] = []
    seen: set = set()

    def harvest(batch) -> None:
        if not isinstance(batch, list):  # Gamma returns a bare array
            batch = batch.get("events", []) if isinstance(batch, dict) else []
        for ev in batch:
            eid = ev.get("id")
            if eid is None or eid in seen:
                continue
            seen.add(eid)
            events.append(ev)

    def pull_window(lo, hi) -> None:
        """Offset-walk one end-date window; on the offset cap (422), bisect."""
        offset = 0
        for _ in range(max_pages):
            params = {
                "closed": "false", "limit": PAGE_POLY, "offset": offset,
                "end_date_min": lo.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "end_date_max": hi.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }
            try:
                batch = _get(f"{POLY_GAMMA}/events", params)
            except requests.HTTPError as e:
                if (e.response is not None and e.response.status_code == 422
                        and hi - lo > timedelta(hours=6)):
                    mid = lo + (hi - lo) / 2
                    pull_window(lo, mid)
                    pull_window(mid, hi)
                    return
                raise
            harvest(batch)
            offset += PAGE_POLY
            if not batch or (isinstance(batch, list) and len(batch) < PAGE_POLY):
                return

    # Past-due-but-open events back to Polymarket's launch era; far-future capped at 2099.
    pull_window(datetime(2020, 1, 1, tzinfo=timezone.utc), now)
    pull_window(now, datetime(2099, 1, 1, tzinfo=timezone.utc))

    # Unwindowed sweep for null-endDate events (invisible to every date-filtered window).
    # Highest-volume first so the most consequential ones land before Gamma's offset cap.
    offset = 0
    for _ in range(max_pages):
        try:
            batch = _get(f"{POLY_GAMMA}/events",
                         {"closed": "false", "limit": PAGE_POLY, "offset": offset,
                          "order": "volume", "ascending": "false"})
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code == 422:
                break  # hit the offset cap — took everything reachable
            raise
        harvest(batch)
        offset += PAGE_POLY
        if not batch or (isinstance(batch, list) and len(batch) < PAGE_POLY):
            break

    return events[:max_events] if max_events else events


def poly_event_volume_usd(event: dict) -> float:
    """Prefer 30-day volume (closest to the filter's intent), fall back to cumulative."""
    for k in ("volume1mo", "volume", "volume24hr"):
        v = event.get(k)
        if v:
            return float(v)
    return 0.0


# -----------------------------------------------------------------
# Filter pass
# -----------------------------------------------------------------
def run(smoke: bool, max_events: int | None) -> None:
    now = datetime.now(timezone.utc)
    suffix = "_smoke" if smoke else ""
    outdir = OUT_ROOT / f"clearmarket-universe-{RUN_DATE}{suffix}"
    outdir.mkdir(parents=True, exist_ok=True)
    cap = 1 * PAGE_KALSHI if smoke else max_events  # smoke = ~one page
    pages = 1 if smoke else MAX_PAGES

    stats = {"kalshi": {}, "polymarket": {}}

    # ---- Kalshi ----
    print(f"[kalshi] fetching events from {KALSHI_BASE} ...", flush=True)
    k_events = fetch_kalshi_events(cap, max_pages=pages)
    k_kept, k_drops, k_cat = [], {}, {}
    for ev in k_events:
        cm = classify_kalshi(ev)
        vol = kalshi_event_volume_usd(ev)
        res = kalshi_event_resolve_at(ev)
        ok, why = passes_institutional_filter(cm, vol, res, "kalshi", now=now)
        if ok:
            ev["_cm"] = {"category": cm, "volume_usd": round(vol, 2), "resolve_at": res, "venue": "kalshi"}
            k_kept.append(ev)
            k_cat[cm] = k_cat.get(cm, 0) + 1
        else:
            k_drops[why.split(":")[0]] = k_drops.get(why.split(":")[0], 0) + 1
    stats["kalshi"] = {"fetched": len(k_events), "kept": len(k_kept),
                       "dropped_by": k_drops, "category_mix": k_cat}
    (outdir / "kalshi-institutional.json").write_text(json.dumps(k_kept, indent=2, default=str))

    # ---- Polymarket ----
    print(f"[poly] fetching events from {POLY_GAMMA} ...", flush=True)
    p_events = fetch_poly_events(cap, max_pages=pages)
    p_kept, p_fallback, p_drops, p_cat = [], [], {}, {}
    for ev in p_events:
        cm, slugs = classify_poly(ev)
        if cm is None:
            cm = classify_poly_llm_fallback(ev)  # seam returns None today
        vol = poly_event_volume_usd(ev)
        res = ev.get("endDate")
        if cm is None:
            # tags didn't map — route to the Haiku gate instead of silently dropping
            ev["_cm"] = {"category": None, "volume_usd": round(vol, 2), "resolve_at": res,
                         "venue": "polymarket", "mapped_tags": slugs}
            p_fallback.append(ev)
            continue
        ok, why = passes_institutional_filter(cm, vol, res, "polymarket", now=now)
        if ok:
            ev["_cm"] = {"category": cm, "volume_usd": round(vol, 2), "resolve_at": res,
                         "venue": "polymarket", "mapped_tags": slugs}
            p_kept.append(ev)
            p_cat[cm] = p_cat.get(cm, 0) + 1
        else:
            p_drops[why.split(":")[0]] = p_drops.get(why.split(":")[0], 0) + 1
    stats["polymarket"] = {"fetched": len(p_events), "kept": len(p_kept),
                           "needs_classification": len(p_fallback),
                           "dropped_by": p_drops, "category_mix": p_cat}
    (outdir / "poly-institutional.json").write_text(json.dumps(p_kept, indent=2, default=str))
    (outdir / "poly-needs-classification.json").write_text(json.dumps(p_fallback, indent=2, default=str))

    manifest = {"run_at": now.isoformat(), "smoke": smoke, "max_events": max_events,
                "categories_in": list(CATEGORIES_IN), "stats": stats}
    (outdir / "manifest.json").write_text(json.dumps(manifest, indent=2))

    # ---- summary ----
    print("\n" + "=" * 60)
    print(f"Universe written to {outdir}")
    for venue in ("kalshi", "polymarket"):
        s = stats[venue]
        print(f"\n[{venue}] fetched={s['fetched']}  kept={s['kept']}"
              + (f"  needs_classification={s.get('needs_classification', 0)}" if venue == "polymarket" else ""))
        print(f"  category mix: {s['category_mix']}")
        print(f"  dropped by:   {s['dropped_by']}")
    print("=" * 60)


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    max_events = None
    if "--limit" in sys.argv:
        max_events = int(sys.argv[sys.argv.index("--limit") + 1])
    run(smoke=smoke, max_events=max_events)
