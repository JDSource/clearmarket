"""
Marks fetcher — the hourly cron's core (task #4 / marks).

Pulls CURRENT prices for the cross-venue-linked markets (question_id set) from the Kalshi +
Polymarket public APIs (open markets only — resolved/stale ones naturally drop out), appends a
timestamped marks snapshot, and recomputes cross_venue_spread on the FRESH prices so the
divergences are trustworthy (no stale 1.0s, no deadline-resolved artifacts).

MVP scope: linked markets only (~600) keeps D1 writes well inside free tier; full-universe
last_price refreshes on the daily scan. Schedule: hourly (0 * * * *) via GitHub Actions cron.

Appends marks.jsonl. No LLM.
"""
import json, requests
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
KALSHI_BASE = "https://api.elections.kalshi.com/trade-api/v2"
POLY_GAMMA = "https://gamma-api.polymarket.com"
TIMEOUT, MAX_PAGES = 30, 80

def _get(url, params):
    r = requests.get(url, params=params, timeout=TIMEOUT, headers={"User-Agent": "clearmarket-marks/0.1"})
    r.raise_for_status()
    return r.json()

# ---- which markets to snapshot ----
linked = [m for m in json.loads((ROOT / "_clearmarket_linked.json").read_text())["markets"] if m.get("question_id")]
want_k = {m["native_id"] for m in linked if m["venue"] == "kalshi"}
want_p = {m["native_id"] for m in linked if m["venue"] == "polymarket"}
dir_by = {m["native_id"]: m.get("direction") for m in linked}
sig_by = {m["native_id"]: m["question_id"] for m in linked}
print(f"linked markets to snapshot: {len(want_k)} kalshi / {len(want_p)} poly")

now = datetime.now(timezone.utc).isoformat()
fresh = {}  # native_id -> {price, vol}

# ---- Kalshi (paginate open events, nested markets) ----
cursor = None
for _ in range(MAX_PAGES):
    params = {"limit": 200, "status": "open", "with_nested_markets": "true"}
    if cursor: params["cursor"] = cursor
    data = _get(f"{KALSHI_BASE}/events", params)
    for ev in data.get("events", []):
        for m in ev.get("markets", []) or []:
            t = m.get("ticker")
            if t in want_k and m.get("last_price_dollars") is not None:
                fresh[t] = {"price": float(m["last_price_dollars"]), "vol": float(m.get("volume_fp") or 0)}
    cursor = data.get("cursor")
    if not cursor: break

# ---- Polymarket (paginate open Gamma events, nested markets) ----
offset = 0
for _ in range(MAX_PAGES):
    batch = _get(f"{POLY_GAMMA}/events", {"closed": "false", "limit": 100, "offset": offset})
    if not isinstance(batch, list): batch = []
    for ev in batch:
        for m in ev.get("markets", []) or []:
            cid = m.get("conditionId")
            ltp = m.get("lastTradePrice")
            if cid in want_p and ltp is not None:
                fresh[cid] = {"price": float(ltp), "vol": float(m.get("volume24hr") or 0)}
    offset += 100
    if len(batch) < 100: break

# ---- append marks snapshot ----
with (ROOT / "marks.jsonl").open("a") as f:
    for nid, d in fresh.items():
        f.write(json.dumps({"native_id": nid, "snapshot_at": now,
                            "last_price": d["price"], "volume_24h": d["vol"]}) + "\n")

cov_k = sum(1 for t in want_k if t in fresh)
cov_p = sum(1 for c in want_p if c in fresh)
print(f"fresh prices: {cov_k}/{len(want_k)} kalshi, {cov_p}/{len(want_p)} poly (open markets only)")

# ---- recompute spreads on FRESH prices ----
def norm(nid):
    d = fresh.get(nid)
    if not d: return None
    p = d["price"]
    return (1.0 - p) if dir_by.get(nid) == "below" else p

groups = defaultdict(lambda: {"kalshi": [], "polymarket": []})
for m in linked:
    if m["native_id"] in fresh:
        groups[m["question_id"]][m["venue"]].append(m["native_id"])

spreads = []
for sig, g in groups.items():
    kp = next((norm(n) for n in g["kalshi"] if norm(n) is not None), None)
    pp = next((norm(n) for n in g["polymarket"] if norm(n) is not None), None)
    if kp is None or pp is None: continue
    subj = next(m["subject"] for m in linked if m["question_id"] == sig)
    rq = {m["native_id"]: m["raw_q"] for m in linked}
    spreads.append({"sig": sig, "subject": subj, "k": round(kp, 3), "p": round(pp, 3),
                    "spread": round(abs(kp - pp), 3),
                    "kq": rq.get(g["kalshi"][0], ""), "pq": rq.get(g["polymarket"][0], "")})

both = len(spreads)
mat = [s for s in spreads if s["spread"] >= 0.05]
print(f"\nclaims with BOTH venues live: {both}  |  material divergences (>=5pp): {len(mat)}")
print("--- top 12 LIVE cross-venue divergences ---")
for s in sorted(spreads, key=lambda x: -x["spread"])[:12]:
    print(f"  Δ{s['spread']*100:4.0f}pp  K {s['k']*100:3.0f}% / P {s['p']*100:3.0f}%  {s['subject']!r}")
    print(f"        K:{s['kq'][:50]!r}  P:{s['pq'][:50]!r}")

(ROOT / "_clearmarket_spreads_live.json").write_text(json.dumps(spreads, indent=2, default=str))
print(f"\nappended {len(fresh)} marks to marks.jsonl  |  spreads -> _clearmarket_spreads_live.json")
