"""
Unified per-event pass — the hybrid (structured + LLM) cross-venue layer.

Per the decision doc (outputs/clearmarket/cross-venue-linking-and-tagging-decision.md):
  - Kalshi numeric fields (threshold/direction/window) read DETERMINISTICALLY from native
    fields (cap_strike/floor_strike, strike_type, close_time). NOT re-derived from text.
  - Polymarket numeric fields extracted by ONE Haiku call/event.
  - Naming (canonical), shape (ladder/independent_basket/categorical_winner), per-market
    entity TAGS, and settlement_style come from the same per-event LLM call (both venues).
  - Cross-venue MARKET-grain links: claim key = (subject + threshold + settlement_style),
    polarity (direction) is an attribute, terminal markets also key on window date.
  - Stable signatures so recurring runs are incremental.

Reads raw institutional files (native fields intact), NOT the mangled enriched bundle.
v1: produces venue-native events (named/shaped/tagged + structured fields) + cross-venue
market links. Does NOT force merged-event containers — that presentation choice is
surfaced for review (see decision doc). Writes _unify_<category>.json.

Usage: python3 unify_events.py [category]   (default: crypto)
"""
import json, re, sys, hashlib
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from enhance import llm_call, LLM_MODEL_HAIKU

RAW = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-05-27"
ROOT = Path(__file__).parent
CATEGORY = sys.argv[1] if len(sys.argv) > 1 else "crypto"

# ---------- subject canonicalization ----------
COIN_ALIAS = {"btc": "bitcoin", "eth": "ethereum", "sol": "solana", "ripple": "xrp",
              "doge": "dogecoin", "ada": "cardano"}
SUBJ_ALIAS = {"fed": "federal reserve", "the fed": "federal reserve",
              "ecb": "european central bank", "boj": "bank of japan",
              "boe": "bank of england", "scotus": "supreme court"}
GENERIC = set("the a an of will be by at on or to is in price prices value level reach above "
              "below specific end new market when how high low get go hit ___ before after "
              "2025 2026 2027 inc corp ltd".split())

def canon_subject(s):
    s = (s or "").strip().lower()
    s = re.sub(r"\.(family|fun|io|xyz|app|finance|fi)\b", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s).strip()
    if s in SUBJ_ALIAS: return SUBJ_ALIAS[s]
    for a, full in COIN_ALIAS.items():
        if re.search(rf"\b{a}\b", s): return full
    toks = [SUBJ_ALIAS.get(t, t) for t in s.split() if t not in GENERIC and len(t) > 1]
    return " ".join(toks[:3]) if toks else (s or None)

def round_thr(t):
    """Snap the venue .99/.01 strike convention to the round number (149999.99 -> 150000)
    while keeping genuinely distinct strikes distinct (1750 != 1800)."""
    if t in (None, ""): return None
    try: t = float(t)
    except (TypeError, ValueError): return None
    r = round(t, 2)
    if abs(r - round(r)) <= max(0.01, abs(r) * 0.005):
        r = float(round(r))
    return r

def _f(v):
    try: return float(v)
    except (TypeError, ValueError): return None

# ---------- Kalshi deterministic numeric fields ----------
DIR_MAP = {"less": "below", "greater": "above", "above": "above", "below": "below",
           "between": "between", "structured": "reach"}

def kalshi_settlement_style(text):
    t = (text or "").lower()
    if re.search(r"all[- ]time high|record high|new high|new low|new all-time", t): return "relative"
    if re.search(r"\b(launch|announce|airdrop|acqui|ipo|elected|win|approve|file)", t): return "occurrence"
    if re.search(r"\b(hit|reach|fall below|rise above|cross|hits|reaches)\b", t): return "touch"
    if re.search(r"\bon [a-z]+ \d|at the end of|\bat \d|close|by \d.*pm|by end of", t): return "terminal"
    return "touch"

def kalshi_fields(ev, m):
    thr = m.get("cap_strike") if m.get("cap_strike") is not None else m.get("floor_strike")
    return {
        "threshold": round_thr(thr),
        "direction": DIR_MAP.get(str(m.get("strike_type")), m.get("strike_type")),
        "settlement_style": kalshi_settlement_style((ev.get("title") or "") + " " + (m.get("title") or "")),
        "window": (m.get("close_time") or "")[:10],
        "price": _f(m.get("last_price_dollars")),
        "native_id": m.get("ticker"),
        "raw_q": m.get("title") or ev.get("title"),
    }

def poly_fields(m):
    # native_id must match the enriched bundle's platform_market_id (Poly conditionId, not market id)
    return {"window": (m.get("endDate") or "")[:10], "price": _f(m.get("lastTradePrice")),
            "native_id": m.get("conditionId") or m.get("id"), "raw_q": m.get("question")}

# ---------- per-event LLM pass ----------
SYS = ("You curate prediction-market reference data. For ONE venue event + its markets return JSON: "
       "canonical_name (concise, neutral, correct year, NO venue tickers/jargon); "
       "shape ('ladder'=one subject at many thresholds/dates=one event; 'independent_basket'=many "
       "DISTINCT subjects each its own question; 'categorical_winner'=mutually-exclusive outcomes, one "
       "winner); and per-market fields keyed by the integer index i. settlement_style: 'touch' (ever "
       "reached in a window), 'terminal' (level at a point in time), 'relative' (new high/low), "
       "'occurrence' (a discrete event happens). direction: above/below/reach/between/occurrence. "
       "subject = the underlying entity/asset only, lowercase. tags = short entity tags for search. "
       "Output ONLY JSON.")

def llm_pass(ev, venue, market_lines, want_numeric):
    fields = ('"subject": str, "tags": [str], "threshold": number|null, "direction": str, "settlement_style": str'
              if want_numeric else '"subject": str, "tags": [str]')
    prompt = (f"VENUE: {venue}\nEVENT TITLE: {json.dumps(ev.get('title'))}\nMARKETS (index | text):\n"
              + "\n".join(market_lines[:25]) +
              f'\n\nReturn JSON: {{"canonical_name": str, "shape": "ladder"|"independent_basket"|"categorical_winner", '
              f'"markets": [{{"i": int, {fields}}}]}}')
    try:
        raw = llm_call(prompt, system=SYS, max_tokens=1200, model=LLM_MODEL_HAIKU)
        j = json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
        by_i = {int(x["i"]): x for x in j.get("markets", []) if "i" in x}
        return j.get("canonical_name") or ev.get("title"), j.get("shape", "ladder"), by_i
    except Exception:
        return ev.get("title"), "ladder", {}

# ---------- build unified markets ----------
def _event_pass(ev, venue):
    mks = ev.get("markets", [])
    if venue == "kalshi":
        lines = [f"  {i} | {m.get('title','')} [{m.get('yes_sub_title','')}]" for i, m in enumerate(mks)]
        return llm_pass(ev, venue, lines, want_numeric=False)
    lines = [f"  {i} | {m.get('question','')} [{m.get('groupItemTitle','')}]" for i, m in enumerate(mks)]
    return llm_pass(ev, venue, lines, want_numeric=True)

def build(events, venue):
    with ThreadPoolExecutor(max_workers=24) as ex:
        passes = list(ex.map(lambda e: _event_pass(e, venue), events))
    out = []
    for ev, (name, shape, by_i) in zip(events, passes):
        mks = ev.get("markets", [])
        ev_subj = canon_subject(name)
        for i, m in enumerate(mks):
            llm = by_i.get(i, {})
            base = kalshi_fields(ev, m) if venue == "kalshi" else poly_fields(m)
            subj = canon_subject(llm.get("subject")) or ev_subj
            if venue == "kalshi":
                thr, direction, style = base["threshold"], base["direction"], base["settlement_style"]
            else:
                thr = round_thr(llm.get("threshold")); direction = llm.get("direction")
                style = llm.get("settlement_style") or "touch"
            if direction not in ("above", "below", "reach", "between", "occurrence"):
                direction = "occurrence" if style == "occurrence" else None
            out.append({
                "venue": venue, "native_id": base["native_id"], "raw_q": base["raw_q"],
                "event_native": ev.get("event_ticker") or ev.get("id"),
                "canonical_name": name, "shape": shape, "subject": subj,
                "tags": sorted(set(([subj] if subj else []) + [t.lower() for t in (llm.get("tags") or [])])),
                "threshold": thr, "direction": direction, "settlement_style": style,
                "window": base["window"], "price": base["price"],
            })
    return out

# ---------- cross-venue market links ----------
def claim_key(m):
    base = (m["subject"], m["threshold"], m["settlement_style"])
    return base + ((m["window"],) if m["settlement_style"] == "terminal" else ())

def stable_sig(key):
    return "CMX-" + hashlib.sha256("|".join(str(x) for x in key).encode()).hexdigest()[:10].upper()

def link(markets):
    # v1: link only THRESHOLD-bearing markets — precise (subject+threshold+style is a specific
    # claim). Occurrence/binary markets (threshold=None) over-merge on subject alone
    # ("republican party" spans 100s of distinct races) — deferred to the LLM-clustering
    # refinement (open item, see decision doc). Precision over recall.
    by_key = defaultdict(list)
    for m in markets:
        if m["subject"] and m["threshold"] is not None:
            by_key[claim_key(m)].append(m)
    links = []
    for key, ms in by_key.items():
        venues = {m["venue"] for m in ms}
        if len(venues) > 1:  # cross-venue link
            links.append({"sig": stable_sig(key), "subject": key[0], "threshold": key[1],
                          "settlement_style": key[2], "members": ms})
    return links

# ---------- run ----------
def main():
    def keep(e):
        return CATEGORY == "all" or (e.get("_cm") or {}).get("category") == CATEGORY
    kal = [e for e in json.loads((RAW / "kalshi-institutional.json").read_text()) if keep(e)]
    pol = [e for e in json.loads((RAW / "poly-institutional.json").read_text()) if keep(e)]
    print(f"CATEGORY={CATEGORY}: {len(kal)} Kalshi / {len(pol)} Poly events\n")

    mk = build(kal, "kalshi") + build(pol, "polymarket")

    # shape guard: a multi-threshold single-subject event is a ladder, not categorical_winner
    by_ev = defaultdict(list)
    for m in mk:
        by_ev[m["event_native"]].append(m)
    for ms in by_ev.values():
        thr = {m["threshold"] for m in ms if m["threshold"] is not None}
        subj = {m["subject"] for m in ms if m["subject"]}
        cur = ms[0]["shape"]
        new = cur
        if len(thr) > 1 and len(subj) <= 1:
            new = "ladder"                       # threshold/strike ladder of one subject
        elif cur == "categorical_winner" and len(subj) <= 1:
            new = "ladder"                       # single-subject binary mislabeled as winner-take-all
        if new != cur:
            for m in ms:
                m["shape"] = new

    links = link(mk)

    shapes = defaultdict(int)
    for m in mk:
        shapes[m["shape"]] += 1
    styled = sum(1 for m in mk if m["settlement_style"])
    threshed = sum(1 for m in mk if m["threshold"] is not None)
    tagged = sum(1 for m in mk if m["tags"])
    print(f"unified markets: {len(mk)} | settlement_style {styled} | threshold {threshed} | tagged {tagged}")
    print(f"shapes (market-weighted): {dict(shapes)}")

    print("\n--- canonical naming sample (raw event -> canonical) ---")
    seen = set()
    for m in mk:
        if m["event_native"] in seen: continue
        seen.add(m["event_native"])
        if len(seen) > 12: break
        print(f"  [{m['venue'][:4]}] {m['raw_q'][:40]!r:42} -> {m['canonical_name'][:46]!r} [{m['shape']}]")

    print("\n--- structured-field sample ---")
    for m in mk[:8]:
        print(f"  [{m['venue'][:4]}] thr={str(m['threshold'])[:10]:10} dir={str(m['direction'])[:8]:8} "
              f"style={str(m['settlement_style'])[:8]:8} tags={m['tags'][:4]}  {m['raw_q'][:38]!r}")

    print(f"\n=== CROSS-VENUE LINKS: {len(links)} ===")
    for L in sorted(links, key=lambda x: -len(x["members"]))[:20]:
        ks = [x for x in L["members"] if x["venue"] == "kalshi"]
        ps = [x for x in L["members"] if x["venue"] == "polymarket"]
        print(f"\n  {L['sig']}  {L['subject']!r} thr={L['threshold']} [{L['settlement_style']}]  ({len(ks)}K x {len(ps)}P)")
        if ks: print(f"     K: {ks[0]['raw_q'][:52]!r}")
        if ps: print(f"     P: {ps[0]['raw_q'][:52]!r}")

    (ROOT / f"_unify_{CATEGORY}.json").write_text(json.dumps({"markets": mk, "links": links}, indent=2, default=str))
    print(f"\nSaved -> _unify_{CATEGORY}.json")

if __name__ == "__main__":
    sys.exit(main())
