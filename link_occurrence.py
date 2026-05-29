"""
Occurrence-event cross-venue linking (task #7).

Threshold-based linking (unify_events.py) is precise. Occurrence/binary markets
(threshold=None) can't link on subject alone — "republican party" spans 100s of distinct
races. This adds LLM adjudication on the SPECIFIC claim (predicate + object), not just the
entity, to recover those links precisely.

Claim-unit = (venue, event_native, subject) — baskets ("Who will IPO") split by entity.
Block by shared canonical subject (+ keyword overlap), then one Haiku call per Kalshi unit
adjudicates which Poly units are the SAME specific question. Matched units get a shared
CMX- claim_sig. Precision over recall.

Reads _unify_all.json. Writes _unify_occurrence_links.json.
"""
import json, re, hashlib
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from enhance import llm_call, LLM_MODEL_HAIKU

ROOT = Path(__file__).parent
markets = json.loads((ROOT / "_unify_all.json").read_text())["markets"]
occ = [m for m in markets if m.get("threshold") is None and m.get("subject")]

# ---- claim-units ----
units = {}
for m in occ:
    key = (m["venue"], m["event_native"], m["subject"])
    u = units.setdefault(key, {"venue": m["venue"], "event_native": m["event_native"],
                               "subject": m["subject"], "canonical_name": m["canonical_name"],
                               "qs": [], "mids": []})
    u["qs"].append(m["raw_q"]); u["mids"].append(m["native_id"])

kunits = [u for u in units.values() if u["venue"] == "kalshi"]
punits = [u for u in units.values() if u["venue"] == "polymarket"]
psubj = defaultdict(list)
for u in punits:
    psubj[u["subject"]].append(u)

def toks(s):
    return set(re.findall(r"[a-z0-9]+", (s or "").lower()))

SYS = ("You match prediction-market claims across two venues. Two claims link ONLY if they are "
       "the SAME SPECIFIC question — same actor AND same predicate AND same object/event. The same "
       "entity in DIFFERENT events does NOT match: 'Republicans win the House' != 'Republicans win "
       "Iowa governor'; 'X launches a token' != 'X testifies to Congress'; 'X IPOs' != 'X acquired'. "
       "Be strict. Output ONLY JSON.")

def adjudicate(ku):
    cands = psubj.get(ku["subject"], [])
    if not cands:
        return []
    kt = toks(ku["canonical_name"] + " " + " ".join(ku["qs"][:2]))
    cands = sorted(cands, key=lambda p: len(kt & toks(p["canonical_name"] + " " + (p["qs"][0] if p["qs"] else ""))),
                   reverse=True)[:12]
    lines = "\n".join(f'  {i} | {c["canonical_name"]} (e.g. "{(c["qs"][0] if c["qs"] else "")[:60]}")'
                      for i, c in enumerate(cands))
    prompt = (f'KALSHI CLAIM: {ku["canonical_name"]} (e.g. "{ku["qs"][0][:70]}")\n'
              f'POLYMARKET CANDIDATES:\n{lines}\n\n'
              'Return JSON {"matches":[{"i":int,"confidence":"high"|"medium"|"low"}]} — only SAME specific claim.')
    try:
        raw = llm_call(prompt, system=SYS, max_tokens=300, model=LLM_MODEL_HAIKU)
        ms = json.loads(re.search(r"\{.*\}", raw, re.S).group(0)).get("matches", [])
        return [(ku, cands[m["i"]]) for m in ms
                if m.get("confidence") in ("high", "medium") and isinstance(m.get("i"), int) and m["i"] < len(cands)]
    except Exception:
        return []

todo = [u for u in kunits if psubj.get(u["subject"])]
print(f"occurrence claim-units: {len(kunits)}K / {len(punits)}P  |  kalshi units with candidates: {len(todo)}")

with ThreadPoolExecutor(max_workers=24) as ex:
    results = list(ex.map(adjudicate, todo))

links = []
for r in results:
    if not r:
        continue
    ku = r[0][0]
    sig = "CMX-" + hashlib.sha256((ku["subject"] + "|" + ku["canonical_name"]).encode()).hexdigest()[:10].upper()
    links.append({"sig": sig, "subject": ku["subject"], "claim": ku["canonical_name"],
                  "kalshi_event": ku["event_native"], "kalshi_q": ku["qs"][0],
                  "poly": [{"event": p["event_native"], "name": p["canonical_name"],
                            "q": p["qs"][0] if p["qs"] else ""} for (_, p) in r]})

mx = max((len(L["poly"]) for L in links), default=0)
print(f"occurrence cross-venue links: {len(links)}  |  max poly-per-link (blob check): {mx}")
print("\n--- sample links (largest first) ---")
for L in sorted(links, key=lambda x: -len(x["poly"]))[:18]:
    print(f"\n  {L['claim'][:48]!r}  subj={L['subject']!r}  -> {len(L['poly'])}P")
    print(f"     K: {L['kalshi_q'][:58]!r}")
    for p in L["poly"][:3]:
        print(f"     P: {p['q'][:58]!r}")

# republican/democrat blob check
for s in ("republican party", "democratic party"):
    g = [L for L in links if L["subject"] == s]
    print(f"\n[{s}] links: {len(g)} (each should be a distinct race, not one blob)")
    for L in g[:6]:
        print(f"   {L['claim'][:46]!r} -> {len(L['poly'])}P  e.g. P:{(L['poly'][0]['q'][:46] if L['poly'] else '')!r}")

(ROOT / "_unify_occurrence_links.json").write_text(json.dumps(links, indent=2, default=str))
print("\nSaved -> _unify_occurrence_links.json")
