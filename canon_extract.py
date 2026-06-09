"""
Canonicalization — LLM EXTRACTOR (layer 1, pinned) + deterministic RESOLVER (layer 2, free).

Layer 1 (costs $, run once per market, cached): one Haiku call per market pulls the
canonical claim out of the raw text -> {entity, event, horizon, polarity, threshold, settlement}.
Pinned to canon-registry.json keyed by market_id; re-runs are free cache hits.

Layer 2 (free, re-runnable anytime): normalize entity via the alias map, build a claim_sig
from (entity, event, horizon, polarity, threshold, settlement), regroup, report cross-venue links.

Usage:
  python3 canon_extract.py validate     # extract a small known set, print it (cheap sanity check)
  python3 canon_extract.py slice         # extract the companies/crypto/macro slice (the real run)
  python3 canon_extract.py resolve       # free: re-resolve whatever is in the registry + report
"""
import json, re, sys, hashlib
from collections import defaultdict, Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from enhance import llm_call, LLM_MODEL_HAIKU

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
REGISTRY = ROOT / "canon-registry.json"
SLICE_CATEGORIES = {"companies", "crypto", "economics", "financials", "technology"}

# ---------- LLM extractor (layer 1) ----------
SYS = (
  "You extract the canonical CLAIM from a prediction market so that identical claims listed on "
  "different venues match exactly. Return ONLY a JSON object, no prose.\n"
  "Fields:\n"
  "- entity: the single underlying subject, lowercase, canonical, no venue tickers/jargon "
  "(e.g. 'spacex', 'bitcoin', 'federal funds rate', 'anthropic'). A market about SpaceX's "
  "valuation still has entity 'spacex'. Use the company/asset/rate/person itself.\n"
  "- event: 1-4 words for what is being predicted ('ipo', 'valuation level', 'merger with tesla', "
  "'launch count', 'rate decision', 'all-time high', 'price level').\n"
  "- horizon: the resolution DEADLINE, normalized. Prefer the deadline stated in the text; else use "
  "the close date given. Format EXACTLY one of: 'YYYY-MM-DD' (a specific day) | 'EOY-YYYY' (end of "
  "year / 'before YYYY+1') | 'EOQn-YYYY' (n=1..4) | 'EOM-YYYY-MM' (end of a month). "
  "'before 2027' -> 'EOY-2026'. 'by June 30, 2026' -> '2026-06-30'.\n"
  "- polarity: 'yes' normally; 'no' if the market resolves YES when the thing FAILS / does NOT happen.\n"
  "- threshold: the numeric level if the claim is crossing a number (price/valuation/count/rate), as a "
  "plain number ($1.6T -> 1600000000000, 4.0% -> 4.0); else null.\n"
  "- settlement: one of touch | terminal | relative | occurrence."
)

def extract_one(m):
    q = m.get("question_raw") or ""
    desc = (m.get("description_raw") or "")[:300]
    close = (m.get("resolve_at") or m.get("close_at") or "")[:10]
    user = f"QUESTION: {q}\nDESCRIPTION: {desc}\nCLOSE DATE: {close}"
    try:
        raw = llm_call(user, system=SYS, max_tokens=200, model=LLM_MODEL_HAIKU)
        j = json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
        return {k: j.get(k) for k in ("entity", "event", "horizon", "polarity", "threshold", "settlement")}
    except Exception as e:
        return {"_error": str(e)[:80]}

def load_registry():
    return json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {}

def extract_markets(markets, label):
    reg = load_registry()
    todo = [m for m in markets if m["market_id"] not in reg]
    print(f"[{label}] {len(markets)} markets, {len(todo)} need extraction ({len(markets)-len(todo)} cached)")
    if todo:
        with ThreadPoolExecutor(max_workers=12) as ex:
            results = list(ex.map(extract_one, todo))
        for m, r in zip(todo, results):
            reg[m["market_id"]] = r
        REGISTRY.write_text(json.dumps(reg, indent=0))
        errs = sum(1 for r in results if "_error" in r)
        print(f"[{label}] extracted {len(todo)} ({errs} errors); registry now {len(reg)}")
    return reg

# ---------- deterministic resolver (layer 2) ----------
ALIAS = {
  "space exploration technologies": "spacex", "space exploration technologies corp": "spacex",
  "anysphere": "cursor", "btc": "bitcoin", "eth": "ethereum", "sol": "solana",
  "the federal reserve": "federal funds rate", "fed funds rate": "federal funds rate",
}
def canon_entity(e):
    if not e: return None
    e = re.sub(r"\b(inc|corp|corporation|llc|ltd|plc|labs|the|co)\b\.?", "", e.lower())
    e = re.sub(r"[^a-z0-9 ]", " ", e); e = re.sub(r"\s+", " ", e).strip()
    return ALIAS.get(e, e)

def canon_event(s):
    """Collapse the LLM's free-text event phrasing into a small canonical set so true
    twins match. Order matters — most specific first."""
    s = (s or "").lower()
    if "ipo" in s and any(w in s for w in ("market cap", "valuation", "mcap", "cap ")): return "ipo_valuation"
    if "ipo" in s: return "ipo"
    if any(w in s for w in ("all-time high", "all time high", "ath", "record high")): return "ath"
    if any(w in s for w in ("airdrop", "token launch", "token")): return "token_event"
    if any(w in s for w in ("merger", "acqui", "buyout", "takeover")): return "mna"
    if any(w in s for w in ("rate decision", "rate cut", "rate hike", "fed funds", "interest rate")): return "rate"
    if any(w in s for w in ("largest company", "biggest company", "market cap", "marketcap")): return "marketcap"
    if "valuation" in s: return "valuation"
    if any(w in s for w in ("price", "hit $", "reach", "above", "below", "dip", "threshold", "level", "high", "low")): return "price"
    return re.sub(r"[^a-z0-9 ]", "", s).strip()[:24] or "other"

def canon_horizon(h):
    """Snap a raw horizon to a cross-venue rung bucket. Returns (bucket, snapped).
    Month-end and the adjacent month-start collapse to the same monthly rung — that
    closes the venues' end-of-month (Kalshi) vs start-of-month (Polymarket) convention
    gap (04-30 == 05-01). December rolls up to the year bucket so 'before 2027' / Dec-31 /
    Jan-1 all match. A mid-month date stays exact — a distinct deadline, not a convention
    artifact. `snapped` flags the derived (medium-confidence) collapses for provenance."""
    if not h: return None, False
    s = str(h).strip().upper()
    m = re.match(r"EOY-(\d{4})$", s)
    if m: return f"Y-{m.group(1)}", False
    m = re.match(r"EOQ([1-4])-(\d{4})$", s)
    if m: return f"Q{m.group(1)}-{m.group(2)}", False
    m = re.match(r"EOM-(\d{4})-(\d{2})$", s)
    if m:
        y, mo = int(m.group(1)), int(m.group(2))
        return (f"Y-{y}" if mo == 12 else f"M-{y}-{mo:02d}"), False
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if d >= 28:
            return (f"Y-{y}" if mo == 12 else f"M-{y}-{mo:02d}"), True
        if d <= 2:  # "by the 1st" == "by end of the previous month"
            pm, py = (12, y - 1) if mo == 1 else (mo - 1, y)
            return (f"Y-{py}" if pm == 12 else f"M-{py}-{pm:02d}"), True
        return f"D-{y}-{mo:02d}-{d:02d}", False  # mid-month exact deadline
    return s, False

def claim_sig(rec):
    e = canon_entity(rec.get("entity"))
    if not e: return None
    hb, _ = canon_horizon(rec.get("horizon"))
    key = (e, canon_event(rec.get("event")), hb,
           rec.get("polarity"), rec.get("threshold"), rec.get("settlement"))
    return "CMX-" + hashlib.sha256("|".join(str(x) for x in key).encode()).hexdigest()[:10].upper(), e

def resolve_and_report(markets):
    reg = load_registry()
    by_sig = defaultdict(list)
    for m in markets:
        rec = reg.get(m["market_id"])
        if not rec or "_error" in rec: continue
        cs = claim_sig(rec)
        if cs: by_sig[cs[0]].append((m, rec))
    xv = {s: g for s, g in by_sig.items() if len({m["platform"] for m, _ in g}) >= 2}
    clean_pairs = [g for g in xv.values()
                   if len(g) == 2 and {m["platform"] for m, _ in g} == {"kalshi", "polymarket"}]
    print(f"\nRESOLVE: {len(markets)} markets -> {len(by_sig)} claims; "
          f"{len(xv)} cross-venue; {len(clean_pairs)} clean 1:1 K+P pairs")
    # validations
    def ent_keys(name):
        return sorted({(canon_entity(r.get('entity')), r.get('horizon'), r.get('polarity'),
                        r.get('threshold')) for m, r in [(m, reg[m['market_id']]) for m in markets
                       if reg.get(m['market_id']) and '_error' not in reg[m['market_id']]]
                      if canon_entity(r.get('entity')) == name},
                      key=lambda t: tuple('' if v is None else str(v) for v in t))
    for name in ("spacex", "starlink"):
        ks = ent_keys(name)
        print(f"\n  {name}: {len(ks)} distinct claims")
        for k in ks[:8]: print(f"     {k}")
    print("\n  sample clean cross-venue pairs:")
    for g in clean_pairs[:12]:
        m, r = g[0]
        print(f"     {canon_entity(r['entity']):16} {r.get('event','')[:18]:18} {r.get('horizon')}")

# ---------- main ----------
def slice_markets(bundle):
    evs = {e["event_id"]: e for e in bundle["events"]}
    return [m for m in bundle["markets"]
            if (evs.get(m["event_id"], {}).get("category") in SLICE_CATEGORIES)]

VALIDATE_PATTERNS = [
    r"\bspacex\b.*\bipo\b", r"\bspacex\b.*valuation", r"\bspacex\b.*fail", r"\bstarlink\b",
    r"\banthropic\b.*ipo", r"\bstripe\b.*ipo", r"bitcoin.*150", r"\bopenai\b.*ipo",
]
def validate_set(bundle):
    out, seen = [], set()
    for m in bundle["markets"]:
        q = (m.get("question_raw") or "").lower()
        for p in VALIDATE_PATTERNS:
            if re.search(p, q) and m["market_id"] not in seen:
                out.append(m); seen.add(m["market_id"]); break
        if len(out) >= 40: break
    return out

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    bundle = json.loads(BUNDLE.read_text())
    if mode == "validate":
        ms = validate_set(bundle)
        reg = extract_markets(ms, "validate")
        print("\n--- extractions (eyeball these) ---")
        for m in ms:
            r = reg[m["market_id"]]
            print(f"[{m['platform'][:4]}] {(m.get('question_raw') or '')[:50]!r}")
            print(f"      -> {json.dumps(r)}")
    elif mode == "slice":
        ms = slice_markets(bundle)
        extract_markets(ms, "slice")
        resolve_and_report(ms)
    elif mode == "resolve":
        resolve_and_report(slice_markets(bundle))
