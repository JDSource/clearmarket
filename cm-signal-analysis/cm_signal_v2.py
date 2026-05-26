#!/usr/bin/env python3
"""
CM Signal v2 — proper Kalshi institutional universe via targeted search.
"""
import json
import glob
from collections import Counter

POLY_PATH = "/Users/jdmac/.claude/projects/-Users-jdmac/862bffe8-bb8c-4f8a-b332-955ab99c7817/tool-results/mcp-prediction-markets-polymarket_list_events-1778528352664.txt"
KALSHI_SEARCH_GLOB = "/Users/jdmac/.claude/projects/-Users-jdmac/862bffe8-bb8c-4f8a-b332-955ab99c7817/tool-results/mcp-prediction-markets-kalshi_search_markets-*.txt"

INSTITUTIONAL_TAGS = {
    'Finance', 'Economy', 'Business', 'Crypto', 'Stocks', 'Inflation',
    'Federal Reserve', 'Geopolitics', 'Foreign Policy', 'Middle East',
    'Russia', 'China', 'Ukraine', 'Iran', 'Israel', 'Politics',
    'Elections', 'Congress', 'Supreme Court', 'Regulation', 'Energy',
    'Oil', 'Commodities', 'Bitcoin', 'Ethereum', 'ETF', 'Recession',
    'Interest Rates', 'GDP', 'Unemployment', 'CPI', 'PPI',
    'Trump', 'Biden', 'White House', 'Treasury', 'SEC',
    'Tariffs', 'Trade', 'Sanctions', 'World', 'Israel-Hamas',
    'Russia-Ukraine', 'Climate', 'Hurricane', 'Earthquake',
    'Tech', 'AI', 'Inflation',
}
EXCLUDED_TAGS = {
    'Sports', 'NBA', 'NFL', 'MLB', 'NHL', 'Soccer', 'NCAA', 'UFC', 'Boxing',
    'Olympics', 'Tennis', 'Golf', 'Hockey', 'Football',
    'Entertainment', 'Music', 'Movies', 'TV', 'Celebrity', 'Awards',
    'Pop Culture', 'Memes', 'Streaming', 'Gaming', 'Esports',
    'Weather Predictions',
}

VOLUME_FLOOR_USD = 10_000
PRICE_MOVE_THRESHOLD = 0.04
VOLUME_SPIKE_MULT = 2.5
CROSS_VENUE_SPREAD_THRESHOLD = 0.05


def num(x):
    try: return float(x) if x is not None else 0
    except (ValueError, TypeError): return 0


def normalize_words(s):
    return set(w.lower().strip('.,?!:;()[]"\'') for w in (s or '').split() if len(w) > 3)


def main():
    poly = json.load(open(POLY_PATH))

    # Load + merge + dedupe Kalshi search results
    kalshi_files = sorted(glob.glob(KALSHI_SEARCH_GLOB))
    kalshi_dedupe = {}
    queries = []
    for path in kalshi_files:
        with open(path) as f:
            d = json.load(f)
        queries.append((d.get('query'), len(d.get('results') or [])))
        for r in (d.get('results') or []):
            m = r.get('item') if isinstance(r, dict) and 'item' in r else r
            if not m: continue
            t = m.get('ticker')
            if t and t not in kalshi_dedupe:
                kalshi_dedupe[t] = m
    kalshi_markets = list(kalshi_dedupe.values())

    print("=" * 70)
    print("KALSHI SEARCH RESULTS (targeted institutional pulls)")
    print("=" * 70)
    for q, n in queries:
        print(f"  '{q}': {n} markets")
    print(f"Deduped Kalshi institutional markets: {len(kalshi_markets)}")

    # Status / volume filter on Kalshi
    kalshi_inst = []
    for m in kalshi_markets:
        if m.get('status') != 'active':
            continue
        # Skip sports props (title-based filter)
        title = (m.get('title') or '').lower()
        if any(k in title for k in ['nba', 'nfl', 'mlb', 'nhl', ' goal', 'rebound',
                                     'assists', 'pts ', 'lakers', 'celtics', 'yankees',
                                     'soccer', 'tennis', 'fight', 'champions league',
                                     'la liga', 'premier league', 'world cup']):
            continue
        vol = num(m.get('volume_fp')) + num(m.get('open_interest_fp'))
        if vol < VOLUME_FLOOR_USD:
            continue
        kalshi_inst.append(m)
    print(f"After active + sports/volume filter: {len(kalshi_inst)}")

    # Polymarket institutional universe
    poly_events_inst = []
    for ev in poly['events']:
        tags = {t.get('label') for t in (ev.get('tags') or []) if t.get('label')}
        if tags & EXCLUDED_TAGS:
            continue
        if not (tags & INSTITUTIONAL_TAGS):
            continue
        if num(ev.get('volume')) < VOLUME_FLOOR_USD:
            continue
        poly_events_inst.append(ev)
    poly_inst_markets = []
    for ev in poly_events_inst:
        for m in ev.get('markets', []):
            if not m.get('active') or m.get('closed') or m.get('archived'):
                continue
            poly_inst_markets.append({'event': ev, 'market': m})
    print(f"Polymarket institutional markets: {len(poly_inst_markets)}")

    # ---- DETECTION ----
    print(f"\n=== DETECTION RESULTS ===")

    # Path 1: 24h momentum
    poly_movers = [x for x in poly_inst_markets if abs(num(x['market'].get('oneDayPriceChange'))) >= PRICE_MOVE_THRESHOLD]
    kalshi_movers = []
    for m in kalshi_inst:
        d1 = num(m.get('last_price_dollars')) - num(m.get('previous_price_dollars'))
        if abs(d1) >= PRICE_MOVE_THRESHOLD:
            kalshi_movers.append({'market': m, 'move': d1})
    print(f"Path 1 (24h momentum ≥{PRICE_MOVE_THRESHOLD*100:.0f}pp): Poly {len(poly_movers)}, Kalshi {len(kalshi_movers)}")

    # Path 4: volume spike
    poly_vol_spikes = []
    for x in poly_inst_markets:
        ev = x['event']
        v24 = num(ev.get('volume24hr'))
        v1w = num(ev.get('volume1wk'))
        baseline = v1w / 7 if v1w else 0
        if v24 > VOLUME_FLOOR_USD and baseline > 0 and v24 / baseline >= VOLUME_SPIKE_MULT:
            poly_vol_spikes.append({**x, 'v24': v24, 'mult': v24/baseline})
    # Kalshi: compare 24h vol to "average" baseline — without 7d data we estimate roughly
    kalshi_vol_spikes = []
    for m in kalshi_inst:
        v24 = num(m.get('volume_24h_fp'))
        v_total = num(m.get('volume_fp'))
        # rough proxy: if 24h vol > 30% of cumulative, that's a spike
        if v24 > VOLUME_FLOOR_USD and v_total > 0 and v24 / v_total >= 0.30:
            kalshi_vol_spikes.append({'market': m, 'v24': v24, 'ratio': v24/v_total})
    print(f"Path 4 (volume spike): Poly {len(poly_vol_spikes)}, Kalshi {len(kalshi_vol_spikes)}")

    # Path 3: cross-venue divergence — now with both sides populated
    cross_pairs = []
    used_kalshi = set()
    for x in poly_inst_markets:
        m = x['market']
        ev = x['event']
        poly_words = normalize_words(ev.get('title', '')) | normalize_words(m.get('question', ''))
        if len(poly_words) < 2: continue
        best_k = None
        best_overlap = 0
        for k in kalshi_inst:
            if k.get('ticker') in used_kalshi: continue
            k_words = normalize_words(k.get('title', ''))
            overlap = len(poly_words & k_words)
            if overlap > best_overlap:
                best_overlap = overlap
                best_k = k
        if best_k and best_overlap >= 2:
            poly_price = num(m.get('lastTradePrice'))
            k_price = num(best_k.get('last_price_dollars'))
            if poly_price > 0 and k_price > 0:
                spread = abs(poly_price - k_price)
                if spread >= CROSS_VENUE_SPREAD_THRESHOLD:
                    cross_pairs.append({
                        'poly_event': ev.get('title'),
                        'poly_market': m.get('question'),
                        'poly_price': poly_price,
                        'kalshi_title': best_k.get('title'),
                        'kalshi_ticker': best_k.get('ticker'),
                        'kalshi_price': k_price,
                        'spread': spread,
                        'overlap': best_overlap,
                    })
                    used_kalshi.add(best_k.get('ticker'))
    print(f"Path 3 (cross-venue spread ≥{CROSS_VENUE_SPREAD_THRESHOLD*100:.0f}pp, ≥2 token overlap): {len(cross_pairs)} pairs")

    # ---- DEDUPED CANDIDATES ----
    candidate_ids = set()
    for x in poly_movers: candidate_ids.add(('poly', x['market'].get('id')))
    for x in kalshi_movers: candidate_ids.add(('kalshi', x['market'].get('ticker')))
    for x in poly_vol_spikes: candidate_ids.add(('poly', x['market'].get('id')))
    for x in kalshi_vol_spikes: candidate_ids.add(('kalshi', x['market'].get('ticker')))
    deduped_single = len(candidate_ids)
    total_with_xv = deduped_single + len(cross_pairs)
    print(f"\nDeduped single-market candidates: {deduped_single}")
    print(f"Plus cross-venue pairs: {len(cross_pairs)}")
    print(f"Total raw candidates: {total_with_xv}")

    # Materiality gate
    GATE = 0.25
    published = int(total_with_xv * GATE)
    print(f"\nAfter materiality gate (~{GATE*100:.0f}%): ~{published} published signals from THIS sample")

    # Scaling
    sample_size = len(poly_inst_markets) + len(kalshi_inst)
    inst_universe = 2500
    scale = inst_universe / sample_size if sample_size else 1
    scaled = int(published * scale)
    print(f"\nSample inst universe: {sample_size}, target: {inst_universe}, scale: {scale:.1f}×")
    print(f"\n*** ESTIMATED PUBLISHED SIGNALS/DAY: ~{scaled} ***")
    print(f"With tighter materiality gate (10% pass rate, real Sonnet judge): ~{int(scaled*0.4)} signals/day")

    # Cost
    cand_per_day = int(total_with_xv * scale)
    haiku = cand_per_day * 0.0005
    perp = cand_per_day * 0.5 * 0.005
    sonnet = scaled * 0.008
    daily = haiku + perp + sonnet + 0.30
    print(f"\n=== COST AT SCALE ===")
    print(f"Candidates evaluated by judge: ~{cand_per_day}/day")
    print(f"  Haiku judge: ${haiku:.2f}/day")
    print(f"  Perplexity: ${perp:.2f}/day")
    print(f"  Sonnet brief render ({scaled} signals): ${sonnet:.2f}/day")
    print(f"  Hosting: $0.30/day")
    print(f"  TOTAL: ~${daily:.2f}/day = ${daily*30:.2f}/month")

    # SAMPLE CANDIDATES
    print(f"\n=== SAMPLE CROSS-VENUE PAIRS (real data, top 6 by spread) ===")
    for c in sorted(cross_pairs, key=lambda x: x['spread'], reverse=True)[:6]:
        print(f"  Δ{c['spread']*100:+.1f}pp  Poly {c['poly_price']*100:.0f}% / Kalshi {c['kalshi_price']*100:.0f}%")
        print(f"    Poly:   {c['poly_event'][:70]}")
        print(f"    Kalshi: {c['kalshi_title'][:80]} ({c['kalshi_ticker']})")
    print(f"\n=== TOP 5 KALSHI MOVERS ===")
    for x in sorted(kalshi_movers, key=lambda x: abs(x['move']), reverse=True)[:5]:
        print(f"  {x['move']*100:+.1f}pp  {x['market'].get('title')[:80]}")
    print(f"\n=== TOP 5 POLYMARKET MOVERS ===")
    for x in sorted(poly_movers, key=lambda x: abs(num(x['market'].get('oneDayPriceChange'))), reverse=True)[:5]:
        d = num(x['market'].get('oneDayPriceChange'))
        print(f"  {d*100:+.1f}pp  {x['event']['title'][:70]}")
        print(f"     → {x['market']['question'][:80]}")

main()
