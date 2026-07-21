"""
gen_volume_spike.py — CM Signal volume_spike wire generator.

Self-contained, NO external API. Surfaces markets drawing a surge of fresh attention: high 24h
volume AND a high share of all-time volume concentrated in the last 24h (the no-history proxy for
"heating up"). When marks_daily accumulates a trailing baseline, swap the intensity denominator to
the trailing daily average; until then the cumulative-share proxy is honest and needs no history.
Volume-spike is the surveillance / pre-catalyst signal — often the spike precedes the news.

Usage: python3 gen_volume_spike.py [--dry] [--min-24h 10000] [--min-intensity 0.25] [--max 8]
"""
import json, sys, re
from pathlib import Path
from gen_news_cycle import now_utc, yz, no_dash, claude_json, OUT_DIR, BUNDLE, pct, compact_usd, venue_label, live_refresh

ROOT = Path(__file__).parent
SITE = "https://clearmarket.fyi"

def _arg(flag, default, cast):
    return cast(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default
DRY = "--dry" in sys.argv
MIN_24H = _arg("--min-24h", 10000.0, float)
MIN_INTENSITY = _arg("--min-intensity", 0.25, float)
# Above ~90% the market is essentially brand-new (all volume is today) — that's a NEW_LISTING, not a
# spike on an established market. Cap it so daily-churn novelty markets don't masquerade as spikes.
MAX_INTENSITY = _arg("--max-intensity", 0.90, float)
MAX = _arg("--max", 10, int)

def slugify(s):
    return (re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:72]) or "volume-spike"

def find_spikes():
    b = json.loads(BUNDLE.read_text())
    evs = {e["event_id"]: e for e in b["events"]}
    out = []
    today = str(now_utc().date())
    for m in b["markets"]:
        m = live_refresh(m)
        if m is None:
            continue  # live markets only — resolved/aged-out return None (kills settled-as-live + stale-volume spikes); price + volume now live, tier:direct honest
        ra = (m.get("resolve_at") or m.get("close_at") or "")[:10]
        if ra and ra < today:
            continue  # expired/resolved — never surface a dead market (the snapshot may be stale)
        v24 = m.get("volume_24h_usd") or 0
        vcum = m.get("volume_total_usd") or 0
        if v24 < MIN_24H or vcum <= 0:
            continue
        intensity = v24 / vcum          # share of all-time volume that is in the last 24h
        if not (MIN_INTENSITY <= intensity <= MAX_INTENSITY):
            continue
        ev = evs.get(m.get("event_id")) or {}
        # nearest upcoming catalyst (so the wire can say "ahead of <catalyst>")
        cats = [c for c in (ev.get("catalyst_dates") or []) if c.get("date")]
        out.append({"m": m, "ev": ev, "v24": v24, "vcum": vcum, "intensity": intensity,
                    "catalyst": (sorted(cats, key=lambda c: c["date"])[0] if cats else None)})
    # rank by absolute 24h volume × intensity (big AND concentrated)
    out.sort(key=lambda d: d["v24"] * d["intensity"], reverse=True)
    return out[:MAX]

SYS = (
    "You write CM Signal VOLUME-SPIKE wire items: a prediction market drawing a surge of fresh "
    "24h trading volume. Newswire/terminal style. Return ONLY JSON.\n"
    "Per spike return {idx:int, semantic_title:str, headline:str, bullets:[str], interp:str}.\n"
    "- SEMANTIC_TITLE (durable, indexed title — price + volume are added deterministically as telemetry, not "
    "by you): a MARKET-STANCE line, wire-service register, characterizing the HIGH CAPITAL DEPLOYMENT — what "
    "the money is attempting to defend, attack, or discount. Do NOT predict the outcome and do NOT pose a "
    "question. Register: liquidity conviction + capital deployment + risk absorption. Palette (inspiration, "
    "NOT a lookup): fresh volume returns to, betting picks up on, traders pile into, heavy trading tests, "
    "buyers back, odds hold through a volume surge. PLAIN-ENGLISH TEST (hard requirement): the title must be "
    "understandable in ONE read by someone who has never seen a prediction market — the bar is a CNBC/Bloomberg "
    "news headline an anchor could read on air unchanged. Everyday verbs only. BANNED financial-poetry verbs: "
    "solidifies, fractures, hardens, wavers, commands, absorbs, anchors, crystallizes, calcifies (and kin — if "
    "a verb wouldn't appear in a CNBC headline, don't use it). NEVER characterize WHO is trading — no "
    "'institutional', 'retail', 'whale', 'smart money', 'desks': order flow is anonymous; report what the "
    "ODDS/PRICING did, never who did it. MAX 62 "
    "characters (hard limit — count them; keep the stance tail to 2-3 words). NO probability, NO raw volume "
    "number, NO venue names, NO math symbols (≥, ≤, ~) — EXCEPTION: round landmark percentages 25% / 50% / 75% "
    "ARE allowed to state a threshold stance ('slips below 50%', 'stays under 25%'); never write 'even odds' / "
    "'quarter odds', a number is clearer; the exact current price stays in telemetry. Claim-defining figures (the "
    "level/date in the question) may be spelled out ('$150K', 'by June 30'). NUMBER FORMAT: compact notation only — dollar PRICE LEVELS from the claim as $65K or $150K, non-dollar counts/index levels as 30K / 80K (the 24h trading VOLUME is telemetry — NEVER put a volume dollar figure in the title); NEVER spell out 'thousand', 'million', or 'billion' (write $1.5B, never 'one and a half billion'); the '$' sign itself is REQUIRED notation, not a banned math symbol — write '$100K', never the word 'dollar' ('dollar 100K' / '100 dollar range' are wrong). Snapshot only. Do NOT invent a "
    "date/horizon absent from the question. VARIATION (whole batch in one call): alternate Subject-first and "
    "Market-first; do NOT reuse an opening verb/noun across items. GOOD: 'Betting picks up on the Paxton "
    "runoff'; 'A $150K Bitcoin by June stays a long shot'; 'Fresh volume returns to "
    "the Iowa Senate race'. BAD (predicts/asks/has metrics): 'Bitcoin to reach $150K by June 30'; "
    "'BTC $150K: 1% on $5.8M surge'.\n"
    "- HEADLINE: terse Bloomberg-wire style. <=58 chars, 6-9 words. Format 'Subject: X%' — a COLON before "
    "the probability, never the bare 'at X%' — then a SHORT volume hook. Drop articles and filler verbs "
    "('prices', 'holds', 'despite'). Use '%'. NOT 'Polymarket prices Culotti California governor at 0% "
    "despite $229K inflow'; YES 'Culotti CA governor: 0% on $229K surge' or 'Hormuz reopening: 14% on $222K'.\n"
    "- BULLETS: 3-4, each ONE tight line (<=20 words), fragments OK. bullet 1 = the market READ (price as % "
    "+ what it implies). bullet 2 = the volume surge (24h $ + share of all-time) as the 'why now'. bullet 3 = "
    "the nearest catalyst/context, or what fresh attention implies (attention precedes news). bullet 4 "
    "(optional) = resolution.\n"
    "- NAME the venue; these are PREDICTION-MARKET contracts, not equities. No 'fade'/'pump' jargon. "
    "State volume + current price as given; do NOT claim the PRICE moved (we have no price history).\n"
    "- QUALITY GATE: DROP novelty/entertainment candidates entirely — tweet-count bets, celebrity "
    "antics ('will X dance'), daily coin-flips ('SPX up or down today'). Return wire items ONLY for "
    "institutionally-relevant claims (macro/rates, company events/IPOs, crypto, geopolitics, elections). "
    "If a candidate is not institutionally serious, OMIT it from items — do not force a wire.\n"
    "- interp: one plain sentence on what the volume surge signals for a desk."
)

def render(spikes):
    blocks = []
    for i, d in enumerate(spikes):
        m = d["m"]
        cat = f" | nearest catalyst: {d['catalyst']['event']} {d['catalyst']['date']}" if d.get("catalyst") else ""
        blocks.append(
            f'SPIKE {i}: "{(m.get("question_raw") or "")[:80]}" | venue={m["platform"]} | '
            f'24h vol=${d["v24"]:,.0f} ({d["intensity"]*100:.0f}% of all-time ${d["vcum"]:,.0f}) | '
            f'price={(m.get("last_price") or 0)*100:.0f}%{cat}')
    user = (f"Today: {now_utc().date()}. Render these {len(spikes)} volume spikes:\n\n"
            + "\n".join(blocks)
            + '\n\nReturn {"items":[{"idx":int,"semantic_title":str,"headline":str,"bullets":[str],"interp":str}]}')
    res = claude_json(SYS, user)
    return {it["idx"]: it for it in res.get("items", [])}

def build_md(d, it, sig_id, slug, date):
    now = now_utc().isoformat(timespec="seconds")
    m, ev = d["m"], d["ev"]
    bullets = [no_dash(b) for b in it.get("bullets", []) if b][:5]
    while len(bullets) < 3:
        bullets.append(f"{m['platform'].title()} market drew ${d['v24']:,.0f} in 24h — {d['intensity']*100:.0f}% of its all-time volume.")
    fm = [
        f"signal_id: {yz(sig_id)}", f"signal_slug: {yz(slug)}",
        f"headline: {yz(no_dash(it['headline']))}",
    ]
    # Title split (2026-06-04): semantic_title (durable) + telemetry (price · 24h volume, as-of)
    if it.get("semantic_title"):
        fm.append(f"semantic_title: {yz(no_dash(it['semantic_title']))}")
    _vs_telemetry = f"{pct(m.get('last_price'))} · {compact_usd(d['v24'])} 24h"
    fm.append(f"telemetry: {yz(_vs_telemetry)}")
    fm += [
        'category_tag: "VOLUME_SPIKE"', 'detection_path: "volume_spike"',
        'pre_news_classification: "pre_news"', f"published_at: {yz(now)}",
        f"event_id: {yz(ev.get('event_id') or m.get('event_id'))}",
        f"event_slug: {yz(ev.get('slug',''))}", f"event_question: {yz(ev.get('question') or m.get('question_raw',''))}",
        "primary_market:", f"  platform: {yz(m['platform'])}",
        f"  platform_market_id: {yz(m.get('platform_market_id') or m.get('market_id'))}",
        f"  question_raw: {yz(m.get('question_raw') or ev.get('question',''))}",
        f"  current_price: {m.get('last_price') if m.get('last_price') is not None else 0}",
        f"  volume_24h_usd: {d['v24']}", f"  volume_cumulative_usd: {d['vcum']}",
    ]
    if m.get("arbitration_model"):
        fm.append(f"  arbitration_model: {yz(m['arbitration_model'])}")
    if m.get("resolve_at"):
        fm.append(f"  resolves_at: {yz(m['resolve_at'])}")
    fm.append("bullets:")
    fm += [f"  - {yz(b)}" for b in bullets]
    fm += [
        "atomic_claims:", '  - type: "volume_anomaly"',
        f"    provenance: {yz('24h + cumulative volume direct from ' + m['platform'] + ' API; intensity = 24h/cumulative (derived)')}",
        "    field_provenance:",
        "      volume_24h_usd:", '        tier: "direct"', f'        method: "{m["platform"]}_api"',
        "      intensity:", '        tier: "derived"', '        method: "arithmetic"',
        '        inputs: ["volume_24h_usd", "volume_cumulative_usd"]',
        "    liquidity_context:",
        f"      {'kalshi' if m['platform']=='kalshi' else 'poly'}_vol_24h_usd: {d['v24']}",
        "sources:",
        f"  - label: {yz('ClearMarket market record: ' + (ev.get('question') or m.get('question_raw',''))[:55])}",
        f"    url: {yz(SITE + '/events/' + (ev.get('slug') or ''))}", f"    retrieved_at: {yz(now)}",
        "field_provenance:", f'  pm_data: "{m["platform"]}_api"', '  editorial_judgment: "cm_signal_llm_judge"',
    ]
    body = no_dash(it.get("interp") or
                   "Volume spike: a market drawing a surge of fresh 24h trading relative to its all-time "
                   "volume. Surveillance signal — attention often precedes the news the other wires react to.")
    return "---\n" + "\n".join(fm) + "\n---\n\n" + body + "\n"

def main():
    spikes = find_spikes()
    print(f"{len(spikes)} volume spikes (24h>=${MIN_24H:,.0f}, intensity>={MIN_INTENSITY*100:.0f}%)", flush=True)
    for d in spikes:
        print(f"  ${d['v24']:>10,.0f}  {d['intensity']*100:3.0f}%  [{d['m']['platform'][:4]}] {(d['m'].get('question_raw') or '')[:48]}", flush=True)
    if not spikes or DRY:
        if DRY: print("--dry: no Claude call, nothing written")
        return
    rendered = render(spikes)
    date = str(now_utc().date()); compact = date.replace("-", "")
    wrote = 0
    for i, d in enumerate(spikes):
        it = rendered.get(i)
        if not it or not it.get("headline"):
            continue
        slug = slugify(f"{(d['m'].get('question_raw') or 'market')[:40]}-vol-{int(d['v24'])}")
        (OUT_DIR / f"{date}-{slug}.md").write_text(build_md(d, it, f"CMSIG{compact}VS{i:02d}", slug, date))
        wrote += 1
    print(f"wrote {wrote} volume_spike wires", flush=True)

if __name__ == "__main__":
    main()
