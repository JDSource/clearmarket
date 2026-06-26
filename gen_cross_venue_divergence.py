"""
gen_cross_venue_divergence.py — CM Signal cross_venue_divergence wire generator.

Self-contained, NO external API. Reads the linked bundle's canonical cross-venue pairs
(canon-pairs.json + question_id), computes the Kalshi-vs-Polymarket price gap per CLEAN binary pair,
gates on a meaningful gap + two-sided liquidity (signal-not-noise), then ONE Claude call renders
each qualifying divergence into a wire. The prices are direct provenance from the bundle (venue
APIs); the wire cites the CM cross-venue record (CM is the layer that linked the two venues).

Usage: python3 gen_cross_venue_divergence.py [--dry] [--min-gap 0.08] [--min-vol 2000] [--max 12]
"""
import json, sys, re
from collections import defaultdict
from pathlib import Path
from gen_news_cycle import now_utc, yz, no_dash, claude_json, OUT_DIR, BUNDLE, pct, compact_usd, venue_label, live_refresh

ROOT = Path(__file__).parent
PAIRS = ROOT / "web/data/canon-pairs.json"
SITE = "https://clearmarket.fyi"

def _arg(flag, default, cast):
    return cast(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default
DRY = "--dry" in sys.argv
MIN_GAP = _arg("--min-gap", 0.05, float)
# A genuine cross-venue divergence is MODERATE. A huge gap on a "same claim" is almost always a
# horizon/polarity artifact in the link, not a real disagreement (e.g. SpaceX 95% vs 0% = a near-month
# Poly market glued into the 'before 2027' bucket). Cap it, and exclude near-0/near-1 prices (resolved /
# mismatched markets). Conservative by design — a wrong divergence wire is worse than a missing one.
MAX_GAP = _arg("--max-gap", 0.25, float)
PRICE_LO, PRICE_HI = 0.04, 0.96
MIN_VOL = _arg("--min-vol", 2000.0, float)
MAX = _arg("--max", 12, int)

def slugify(s):
    return (re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:72]) or "divergence"

def find_divergences():
    bundle = json.loads(BUNDLE.read_text())
    pairs = json.loads(PAIRS.read_text())
    evs = {e["event_id"]: e for e in bundle["events"]}
    by_sig = defaultdict(list)
    for m in bundle["markets"]:
        if m.get("question_id"):
            by_sig[m["question_id"]].append(m)
    out = []
    for p in pairs:
        if not p.get("clean"):
            continue  # 1:1 binary only — never a ladder
        grp = by_sig.get(p["question_id"], [])
        k = next((m for m in grp if m["platform"] == "kalshi"), None)
        po = next((m for m in grp if m["platform"] == "polymarket"), None)
        if not (k and po):
            continue
        k, po = live_refresh(k), live_refresh(po)
        if k is None or po is None:
            continue  # either leg not live (resolved/aged-out) — a divergence on a dead claim is a stale artifact; both legs now carry live prices, so the gap is real
        kp, pp = k.get("last_price"), po.get("last_price")
        if kp is None or pp is None:
            continue
        today = str(now_utc().date())
        if any(((m.get("resolve_at") or m.get("close_at") or "")[:10] or today) < today for m in (k, po)):
            continue  # expired/resolved on either venue — don't write about a dead claim
        gap = abs(kp - pp)
        if gap < MIN_GAP or gap > MAX_GAP:
            continue  # too small = not newsworthy; too big = almost certainly a link artifact
        if not (PRICE_LO <= kp <= PRICE_HI and PRICE_LO <= pp <= PRICE_HI):
            continue  # near-0/near-1 on a "same claim" signals a resolved or mismatched market
        kvol = k.get("volume_total_usd") or 0
        pvol = po.get("volume_total_usd") or 0
        if kvol < MIN_VOL or pvol < MIN_VOL:
            continue  # both sides must be liquid (signal, not noise)
        out.append({"p": p, "k": k, "po": po, "kp": kp, "pp": pp, "gap": gap,
                    "kvol": kvol, "pvol": pvol,
                    "k24": k.get("volume_24h_usd"), "p24": po.get("volume_24h_usd"),
                    "ev": evs.get(k.get("event_id")) or evs.get(po.get("event_id")) or {}})
    out.sort(key=lambda d: d["gap"], reverse=True)
    return out[:MAX]

SYS = (
    "You write CM Signal CROSS-VENUE DIVERGENCE wire items: the SAME prediction-market claim priced "
    "differently on Kalshi vs Polymarket. Newswire/terminal style. Return ONLY JSON.\n"
    "Per divergence return {div_index:int, semantic_title:str, headline:str, bullets:[str], interp:str}.\n"
    "- SEMANTIC_TITLE (durable, indexed title — the venue prices are added deterministically as telemetry, "
    "not by you): a MARKET-STANCE line, wire-service register, about the PRICING BEHAVIOR BETWEEN the venues "
    "tracking this claim. Do NOT predict the outcome and do NOT pose a question — report the structural "
    "dislocation / spread state. Register: arbitrage spread + fragmentation + platform friction. Palette "
    "(inspiration, NOT a lookup): splits sharply, decouples, mirrors, bridges, spreads, isolates, converges, "
    "tracks a premium. MAX 62 characters (hard limit — count them; the long stance tail is the usual cause, keep it 2-3 words). Refer to venues GENERICALLY ('across venues', 'on the major desks') — do "
    "NOT name Kalshi/Polymarket or print either price (those live in telemetry). NO probability, NO math "
    "symbols; claim-defining figures (the level/date in the claim) may be spelled out. NUMBER FORMAT: compact notation only — dollar PRICE LEVELS from the claim as $65K or $150K, non-dollar counts/index levels as 30K / 80K (the 24h trading VOLUME is telemetry — NEVER put a volume dollar figure in the title); NEVER spell out 'thousand' or 'million'. Snapshot only. Do NOT "
    "invent a date/horizon absent from the claim. VARIATION (whole batch in one call): alternate Subject-first "
    "and Market-first; do NOT reuse an opening verb/noun across items. GOOD: 'Anthropic IPO pricing splits "
    "sharply across venues'; 'Grok 5 timeline decouples on the major prediction desks'. BAD (predicts/asks/"
    "names venue+price): 'Anthropic to IPO before 2027'; 'Anthropic IPO: Kalshi 76% vs Polymarket 70%'.\n"
    "- HEADLINE: <=72 chars, NOUN PHRASE, lead with the claim then BOTH prices, e.g. "
    "'Anthropic IPO before 2027: Kalshi 76% vs Polymarket 70%'. Use '%'.\n"
    "- BULLETS: 3-4, each ONE tight line (<=20 words), fragments OK. bullet 1 = the gap (both venues + "
    "the pp gap). bullet 2 = which venue is higher + the liquidity on each side. bullet 3 = a plausible "
    "read (resolution-clarity difference, audience, or which venue is more credible). bullet 4 (optional) "
    "= resolution mechanic.\n"
    "- NAME both venues explicitly; these are PREDICTION-MARKET contracts, not equities. No 'fade'/'spike' "
    "jargon. Do NOT claim either price 'moved' (we have no price history) — state current levels + the gap.\n"
    "- interp: one plain sentence on what the divergence means for a desk."
)

def render(divs):
    blocks = []
    for i, d in enumerate(divs):
        blocks.append(
            f'DIVERGENCE {i}: claim="{d["p"]["claim"]}" | horizon={d["p"].get("horizon")} | '
            f'Kalshi {d["kp"]*100:.0f}% (cum vol ${d["kvol"]:,.0f}) | '
            f'Polymarket {d["pp"]*100:.0f}% (cum vol ${d["pvol"]:,.0f}) | gap {d["gap"]*100:.0f}pp')
    user = (f"Today: {now_utc().date()}. Render these {len(divs)} cross-venue divergences:\n\n"
            + "\n".join(blocks)
            + '\n\nReturn {"items":[{"div_index":int,"semantic_title":str,"headline":str,"bullets":[str],"interp":str}]}')
    res = claude_json(SYS, user)
    return {it["div_index"]: it for it in res.get("items", [])}

def build_md(d, it, sig_id, slug, date):
    now = now_utc().isoformat(timespec="seconds")
    k, po, ev, p = d["k"], d["po"], d["ev"], d["p"]
    # primary = the higher-cumulative-volume venue (the more liquid read)
    if d["kvol"] >= d["pvol"]:
        prim, primp, pv, rel, relp, pplat, rplat = k, d["kp"], d["kvol"], po, d["pp"], "kalshi", "polymarket"
    else:
        prim, primp, pv, rel, relp, pplat, rplat = po, d["pp"], d["pvol"], k, d["kp"], "polymarket", "kalshi"
    bullets = [no_dash(b) for b in it.get("bullets", []) if b][:5]
    while len(bullets) < 3:
        bullets.append(f"{pplat.title()} prices {primp*100:.0f}%; {rplat.title()} {relp*100:.0f}% — a {d['gap']*100:.0f}pp cross-venue gap.")
    fm = [
        f"signal_id: {yz(sig_id)}", f"signal_slug: {yz(slug)}",
        f"headline: {yz(no_dash(it['headline']))}",
    ]
    # Title split (2026-06-04): semantic_title (durable) + telemetry (both venue prices, as-of)
    if it.get("semantic_title"):
        fm.append(f"semantic_title: {yz(no_dash(it['semantic_title']))}")
    _cv_telemetry = f"{venue_label(pplat)} {pct(primp)} vs {venue_label(rplat)} {pct(relp)}"
    fm.append(f"telemetry: {yz(_cv_telemetry)}")
    fm += [
        'category_tag: "CROSS_VENUE_DIVERGENCE"', 'detection_path: "cross_venue_divergence"',
        'pre_news_classification: "concurrent"', f"published_at: {yz(now)}",
        f"event_id: {yz(ev.get('event_id') or prim.get('event_id'))}",
        f"event_slug: {yz(ev.get('slug') or p['slug'])}", f"event_question: {yz(p['claim'])}",
        "primary_market:", f"  platform: {yz(pplat)}",
        f"  platform_market_id: {yz(prim.get('platform_market_id') or prim.get('market_id'))}",
        f"  question_raw: {yz(prim.get('question_raw') or p['claim'])}", f"  current_price: {primp}",
        f"  volume_cumulative_usd: {pv}",
    ]
    if prim.get("arbitration_model"):
        fm.append(f"  arbitration_model: {yz(prim['arbitration_model'])}")
    if prim.get("resolve_at"):
        fm.append(f"  resolves_at: {yz(prim['resolve_at'])}")
    fm += [
        "related_markets:", f"  - platform: {yz(rplat)}",
        f"    platform_market_id: {yz(rel.get('platform_market_id') or rel.get('market_id'))}",
        f"    question_raw: {yz(rel.get('question_raw') or p['claim'])}", f"    current_price: {relp}",
        "bullets:",
    ]
    fm += [f"  - {yz(b)}" for b in bullets]
    fm += [
        "atomic_claims:", '  - type: "cross_venue_spread"',
        f"    provenance: {yz('CM cross-venue link (question_id ' + p['question_id'] + '); prices direct from venue APIs')}",
        "    field_provenance:",
        "      kalshi_price:", '        tier: "direct"', '        method: "kalshi_api"',
        "      poly_price:", '        tier: "direct"', '        method: "polymarket_clob_api"',
        "      divergence_pp:", '        tier: "derived"', '        method: "arithmetic"',
        '        inputs: ["kalshi_price", "poly_price"]',
        "    liquidity_context:",
    ]
    if d["k24"] is not None:
        fm.append(f"      kalshi_vol_24h_usd: {d['k24']}")
    if d["p24"] is not None:
        fm.append(f"      poly_vol_24h_usd: {d['p24']}")
    fm += [
        "sources:",
        f"  - label: {yz('ClearMarket cross-venue record: ' + p['claim'][:60])}",
        f"    url: {yz(SITE + '/compare/' + p['slug'])}", f"    retrieved_at: {yz(now)}",
        "field_provenance:", '  pm_data: "kalshi_api, polymarket_clob_api"',
        '  editorial_judgment: "cm_signal_llm_judge"',
    ]
    body = no_dash(it.get("interp") or
                   "Cross-venue divergence: the same claim priced differently on Kalshi and Polymarket, "
                   "linked by CM's question_id. The gap is each venue's current price; provenance is direct.")
    return "---\n" + "\n".join(fm) + "\n---\n\n" + body + "\n"

def main():
    divs = find_divergences()
    print(f"{len(divs)} qualifying divergences (gap>={MIN_GAP*100:.0f}pp, both cum-vol>=${MIN_VOL:,.0f})", flush=True)
    for d in divs:
        print(f"  {d['gap']*100:4.0f}pp  {d['p']['title'][:34]:34} K {d['kp']*100:.0f}% / P {d['pp']*100:.0f}%", flush=True)
    if not divs or DRY:
        if DRY: print("--dry: no Claude call, nothing written")
        return
    rendered = render(divs)
    date = str(now_utc().date())
    compact = date.replace("-", "")
    wrote = 0
    for i, d in enumerate(divs):
        it = rendered.get(i)
        if not it or not it.get("headline"):
            continue
        slug = slugify(f"{d['p']['title']}-k{int(d['kp']*100)}-p{int(d['pp']*100)}")
        sig_id = f"CMSIG{compact}DV{i:02d}"
        (OUT_DIR / f"{date}-{slug}.md").write_text(build_md(d, it, sig_id, slug, date))
        wrote += 1
    print(f"wrote {wrote} cross_venue_divergence wires", flush=True)

if __name__ == "__main__":
    main()
