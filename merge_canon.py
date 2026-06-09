"""
merge_canon.py — stamp the canonical claim_sig from canon-registry.json onto the live
bundle, replacing the old broken cross-venue links.

What it does (build-time intercept, no LLM, no re-enrich — same shape as patch_sources.py):
  1. Back up web/data/universe-enriched-linked.json once.
  2. Clear the OLD claim_sig on EVERY market (kills the broken 202 links; preserved as
     claim_sig_legacy for audit). Markets we haven't canonicalized end up with NO
     cross-venue link — the launch-safe interim (suppress low-confidence links).
  3. For every market in canon-registry.json (the slice), compute the canonical
     claim_sig via the layer-2 resolver (canon_entity + canon_event + canon_horizon +
     polarity + threshold + settlement) and stamp it on, with match_confidence +
     editorial/derived provenance (machine-layer rule: a link is an additive, auditable
     assertion, never a destructive merge).
  4. Emit web/data/canon-pairs.json — the cross-venue groups (both venues present) that
     /compare renders, with display metadata.

Run:  python3 merge_canon.py            # writes the bundle + pairs file
      python3 merge_canon.py --dry      # report only, write nothing
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path
from canon_extract import canon_entity, canon_event, canon_horizon, claim_sig

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
BACKUP = ROOT / "web/data/universe-enriched-linked.pre-canon-bak.json"
REGISTRY = ROOT / "canon-registry.json"
PAIRS = ROOT / "web/data/canon-pairs.json"

DRY = "--dry" in sys.argv

MONTHS = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def human_horizon(bucket):
    if not bucket: return ""
    m = re.match(r"Y-(\d{4})$", bucket)
    if m: return f"before {int(m.group(1)) + 1}"
    m = re.match(r"Q([1-4])-(\d{4})$", bucket)
    if m: return f"Q{m.group(1)} {m.group(2)}"
    m = re.match(r"M-(\d{4})-(\d{2})$", bucket)
    if m: return f"{MONTHS[int(m.group(2))]} {m.group(1)}"
    m = re.match(r"D-(\d{4})-(\d{2})-(\d{2})$", bucket)
    if m: return f"by {MONTHS[int(m.group(2))]} {int(m.group(3))}, {m.group(1)}"
    return bucket

def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s[:70] or "claim"

def is_umbrella(q):
    return bool(re.search(r"\bwho will\b|\bwhich (company|team|country)\b", q or "", re.I))

SPECIAL_CASE = {"spacex": "SpaceX", "openai": "OpenAI", "xai": "xAI", "gamestop": "GameStop",
                "blackrock": "BlackRock", "tiktok": "TikTok", "youtube": "YouTube",
                "jpmorgan": "JPMorgan", "bytedance": "ByteDance", "deepseek": "DeepSeek"}
UPPER_CASE = {"us", "ai", "gdp", "cpi", "etf", "sec", "eu", "uk", "btc", "eth", "sol",
              "nba", "nfl", "ufc", "fed", "ecb", "boj"}
def titlecase_entity(e):
    out = []
    for w in (e or "").split():
        lw = w.lower()
        out.append(SPECIAL_CASE.get(lw) or (lw.upper() if lw in UPPER_CASE else w.capitalize()))
    return " ".join(out)

def main():
    bundle = json.loads(BUNDLE.read_text())
    reg = json.loads(REGISTRY.read_text())
    evs = {e["event_id"]: e for e in bundle["events"]}

    # 1. back up once
    if not DRY and not BACKUP.exists():
        BACKUP.write_text(BUNDLE.read_text())
        print(f"backed up bundle -> {BACKUP.name}")

    # 2 + 3. clear old sigs everywhere, stamp canonical where we have a registry record
    stamped = 0
    for m in bundle["markets"]:
        old = m.get("claim_sig") if m.get("claim_sig") is not None else m.get("question_id")
        if old is not None and "question_id_legacy" not in m:
            m["question_id_legacy"] = old   # preserve the ORIGINAL only (don't clobber on re-run)
        m.pop("claim_sig", None)            # retire the old field name
        m.pop("cross_platform_link", None)  # retire the vestigial derived field (single-venue event_id; never worked)
        if isinstance(m.get("field_provenance"), dict):
            m["field_provenance"].pop("cross_platform_link", None)
        m["question_id"] = None
        m["also_on"] = None
        m["match_confidence"] = None
        rec = reg.get(m["market_id"])
        if not rec or "_error" in rec:
            continue
        # SELF-DEFENDING GATE: a "When will X happen?" market is a multinomial timing-ladder bucket,
        # not a clean binary — deny it a cross-venue claim_sig so it can't pollute a claim group or
        # form a false divergence (it stays a single-venue market). The clean binaries in the same
        # group keep their sig and still pair.
        if re.search(r"\bwhen (will|does|do|did)\b", (m.get("question_raw") or ""), re.I):
            continue
        cs = claim_sig(rec)
        if not cs:
            continue
        _, snapped = canon_horizon(rec.get("horizon"))
        m["question_id"] = cs[0]
        m["match_confidence"] = "medium" if snapped else "high"
        m["question_id_method"] = "canon_v1"
        m["question_id_provenance"] = "derived"   # editorial assertion, reversible
        stamped += 1

    # 3b. derive also_on: the SAME question (question_id) priced on OTHER venues.
    #     null when the question is unique to its venue. [{venue, market_id, price}]
    by_qid = defaultdict(list)
    for m in bundle["markets"]:
        if m.get("question_id"):
            by_qid[m["question_id"]].append(m)
    for group in by_qid.values():
        for m in group:
            others = [{"venue": o["platform"], "market_id": o["market_id"], "price": o.get("last_price")}
                      for o in group if o["platform"] != m["platform"]]
            m["also_on"] = others or None

    # 4. build cross-venue pair groups (both venues under one canonical question)
    pairs = []
    for sig, group in by_qid.items():
        venues = {m["platform"] for m in group}
        if venues != {"kalshi", "polymarket"}:
            continue   # cross-venue only
        rec = reg[group[0]["market_id"]]
        # /compare pages are for clean BINARY occurrence claims only. Price/rate ladders
        # (threshold set, touch/terminal settlement) stay single-venue on /priced — the
        # locked rule: venues' strike grids don't align, never stack them per strike.
        if rec.get("threshold") is not None or rec.get("settlement") != "occurrence":
            continue
        ent = canon_entity(rec.get("entity"))
        ev = canon_event(rec.get("event"))
        # Rate-decision markets ("cut" vs "hike" vs "maintain") share entity+horizon+settlement but are
        # DISTINCT outcomes the canon key can't separate, so they false-merge. Keep them OFF /compare —
        # central-bank decisions stay single-venue until a direction-aware key exists.
        if ev == "rate":
            continue
        hb, snapped = canon_horizon(rec.get("horizon"))
        # naming: prefer the kalshi row's question for the claim sentence (venue's own words)
        rep = next((m for m in group if m["platform"] == "kalshi"), group[0])
        cat = evs.get(rep.get("event_id"), {}).get("category", "other")
        EVENT_LABEL = {"ipo": "IPO", "ipo_valuation": "IPO valuation", "mna": "M&A",
                       "ath": "all-time high", "rate": "rate decision", "token_event": "token event",
                       "marketcap": "market cap"}
        el = EVENT_LABEL.get(ev, ev.replace("_", " "))
        ent_t = titlecase_entity(ent)
        title = ent_t if el.lower() in ent_t.lower() else f"{ent_t} {el}"
        # claim sentence: prefer a venue's SPECIFIC question (Poly "Stripe IPO before 2027?"),
        # never the basket umbrella ("Who will IPO before 2027?"); else construct from title+horizon
        claim_q = next((m.get("question_raw") for m in group
                        if m.get("question_raw") and not is_umbrella(m["question_raw"])), None)
        claim = claim_q or f"Will {title} {human_horizon(hb)}?"
        vol = sum((m.get("volume_total_usd") or 0) for m in group)
        clean = len(group) == 2  # 1:1 pair (vs ladder-on-each-venue)
        conf = "medium" if snapped else "high"
        pairs.append({
            "slug": slugify(f"{ent}-{ev}-{hb}"),
            "title": title,
            "claim": claim,
            "sector": cat,
            "horizon": human_horizon(hb),
            "question_id": sig,
            "markets": len(group),
            "clean": clean,
            "confidence": conf,
            "_vol": vol,
        })

    # dedupe slugs, sort by volume desc (best first)
    seen = {}
    for p in pairs:
        s, n = p["slug"], 1
        while p["slug"] in seen:
            n += 1; p["slug"] = f"{s}-{n}"
        seen[p["slug"]] = True
    pairs.sort(key=lambda p: p["_vol"], reverse=True)
    for p in pairs:
        p.pop("_vol", None)

    clean_n = sum(1 for p in pairs if p["clean"])
    print(f"stamped {stamped} markets with canonical claim_sig; "
          f"{len(pairs)} cross-venue groups ({clean_n} clean 1:1, {len(pairs)-clean_n} ladders)")
    print("  top 12 by volume:")
    for p in pairs[:12]:
        print(f"    [{p['confidence'][:3]}] {p['title'][:34]:34} {p['horizon'][:16]:16} {p['slug']}")

    if DRY:
        print("\n--dry: nothing written"); return
    BUNDLE.write_text(json.dumps(bundle))
    PAIRS.write_text(json.dumps(pairs, indent=1))
    print(f"\nwrote bundle + {PAIRS.name} ({len(pairs)} pairs)")

if __name__ == "__main__":
    main()
