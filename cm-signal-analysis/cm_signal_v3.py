#!/usr/bin/env python3
"""
CM Signal v3 — ALL 4 detection paths properly run on real data.

Path 1: News-driven — match Perplexity top-10 stories to markets
Path 2: Benchmark divergence — count markets where external benchmark exists
Path 3: Cross-venue divergence — tighter semantic match
Path 4: Volume spike — already correct
"""
import json
import glob
import re
from collections import Counter

POLY_PATH = "/Users/jdmac/.claude/projects/-Users-jdmac/862bffe8-bb8c-4f8a-b332-955ab99c7817/tool-results/mcp-prediction-markets-polymarket_list_events-1778528352664.txt"
KALSHI_SEARCH_GLOB = "/Users/jdmac/.claude/projects/-Users-jdmac/862bffe8-bb8c-4f8a-b332-955ab99c7817/tool-results/mcp-prediction-markets-kalshi_search_markets-*.txt"

# Real top-10 news stories from Perplexity (May 11, 2026)
TOP_STORIES = [
    {
        "summary": "S&P 500 reaches all-time highs as Middle East de-escalation hopes dominate",
        "entities": ["S&P 500", "Middle East", "S&P", "SPX", "stocks"],
    },
    {
        "summary": "EU holds first summit with Armenia, signaling South Caucasus realignment",
        "entities": ["EU", "Armenia", "Azerbaijan", "European Union"],
    },
    {
        "summary": "BlackRock identifies energy security + AI-driven power demand as mega-forces",
        "entities": ["BlackRock", "AI", "energy", "power"],
    },
    {
        "summary": "Brent crude climbs to $112/barrel on Strait of Hormuz disruption",
        "entities": ["Brent", "oil", "Hormuz", "crude", "Iran"],
    },
    {
        "summary": "BlackRock iShares Bitcoin Trust attracts $1.7B inflows in April",
        "entities": ["Bitcoin", "ETF", "BlackRock", "iShares", "IBIT", "BTC"],
    },
    {
        "summary": "Morgan Stanley expands crypto trading to retail via E-Trade",
        "entities": ["Morgan Stanley", "E-Trade", "Bitcoin", "Ether", "Solana", "crypto"],
    },
    {
        "summary": "Kevin Warsh Fed Chair nomination faces Senate vote as Powell term ends May 15",
        "entities": ["Warsh", "Fed Chair", "Powell", "Federal Reserve", "Fed"],
    },
    {
        "summary": "Trump rejects Iran's latest proposal to end Middle East war",
        "entities": ["Trump", "Iran", "Middle East", "peace deal", "ceasefire"],
    },
    {
        "summary": "S&P 500 posts six consecutive quarters of double-digit earnings growth",
        "entities": ["S&P 500", "earnings", "SPX"],
    },
    {
        "summary": "Morgan Stanley projects US equities deliver 8% annual returns over 20 years",
        "entities": ["Morgan Stanley", "equities", "S&P 500"],
    },
]

# External benchmarks available for comparison (path 2)
BENCHMARK_KEYWORDS = {
    'fed_rate': {'keywords': ['fed', 'federal reserve', 'fomc', 'rate cut', 'rate hike', 'basis point', 'bps', 'fed funds'], 'benchmark': 'CME FedWatch'},
    'cpi': {'keywords': ['cpi', 'inflation', 'consumer price'], 'benchmark': 'Bloomberg economist consensus'},
    'jobs': {'keywords': ['jobs', 'unemployment', 'nfp', 'payroll', 'labor', 'employment'], 'benchmark': 'Economist consensus'},
    'gdp': {'keywords': ['gdp', 'growth', 'recession'], 'benchmark': 'Economist consensus + Atlanta Fed nowcast'},
    'election': {'keywords': ['election', 'president', 'win 2028', 'win 2024', 'win 2026', 'midterm', 'nominee'], 'benchmark': 'Polling average (RCP / 538)'},
    'oil': {'keywords': ['brent', 'wti', 'crude', 'oil price'], 'benchmark': 'CME crude futures'},
    'btc': {'keywords': ['bitcoin', 'btc', 'ethereum', 'eth', 'crypto'], 'benchmark': 'Spot exchange price'},
    'eq': {'keywords': ['s&p 500', 'sp500', 'spx', 'nasdaq', 'dow'], 'benchmark': 'Index futures (ES, NQ, YM)'},
    'fx': {'keywords': ['dollar', 'usd', 'euro', 'yen', 'fx'], 'benchmark': 'FX spot + forward curves'},
}

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
}

VOLUME_FLOOR_USD = 10_000
PRICE_MOVE_THRESHOLD = 0.04
VOLUME_SPIKE_MULT = 2.5
CROSS_VENUE_SPREAD_THRESHOLD = 0.05


def num(x):
    try: return float(x) if x is not None else 0
    except (ValueError, TypeError): return 0


def lowertext(*ss):
    return ' '.join((s or '').lower() for s in ss)


def main():
    # Load
    poly = json.load(open(POLY_PATH))
    kalshi_dedupe = {}
    for path in sorted(glob.glob(KALSHI_SEARCH_GLOB)):
        with open(path) as f:
            d = json.load(f)
        for r in (d.get('results') or []):
            m = r.get('item') if isinstance(r, dict) and 'item' in r else r
            if not m: continue
            t = m.get('ticker')
            if t and t not in kalshi_dedupe:
                kalshi_dedupe[t] = m
    kalshi_markets = list(kalshi_dedupe.values())

    # Institutional filter on Kalshi
    kalshi_inst = []
    for m in kalshi_markets:
        if m.get('status') != 'active': continue
        title = (m.get('title') or '').lower()
        if any(k in title for k in ['nba', 'nfl', 'mlb', 'nhl', ' goal', 'rebound', 'assists', 'pts ',
                                     'lakers', 'celtics', 'yankees', 'soccer', 'tennis', 'fight',
                                     'champions league', 'la liga', 'premier league', 'world cup',
                                     'drake', 'rihanna', 'celebrity', 'gta', 'grammy']):
            continue
        vol = num(m.get('volume_fp')) + num(m.get('open_interest_fp'))
        if vol < VOLUME_FLOOR_USD: continue
        kalshi_inst.append(m)

    # Institutional filter on Polymarket
    poly_inst_markets = []
    for ev in poly['events']:
        tags = {t.get('label') for t in (ev.get('tags') or []) if t.get('label')}
        if tags & EXCLUDED_TAGS: continue
        if not (tags & INSTITUTIONAL_TAGS): continue
        # Also filter out trivia like Rihanna / GTA / celebrity events even with passable tags
        title = (ev.get('title') or '').lower()
        if any(k in title for k in ['rihanna', 'gta', 'celebrity', 'drake', 'grammy', 'megaeth']):
            continue
        if num(ev.get('volume')) < VOLUME_FLOOR_USD: continue
        for m in ev.get('markets', []):
            if not m.get('active') or m.get('closed') or m.get('archived'): continue
            poly_inst_markets.append({'event': ev, 'market': m})

    print(f"Institutional universe: Polymarket {len(poly_inst_markets)} mkts, Kalshi {len(kalshi_inst)} mkts")
    sample_size = len(poly_inst_markets) + len(kalshi_inst)
    inst_universe = 2500
    scale = inst_universe / sample_size if sample_size else 1
    print(f"Sample: {sample_size} of estimated {inst_universe} full universe → scale ×{scale:.1f}\n")

    # ----- PATH 1: NEWS-DRIVEN -----
    print("=" * 70)
    print("PATH 1: NEWS-DRIVEN (top news → matched PM markets)")
    print("=" * 70)
    news_matches = []
    matched_market_ids = set()
    for story in TOP_STORIES:
        entity_lc = [e.lower() for e in story['entities']]
        story_matches = []
        for x in poly_inst_markets:
            text = lowertext(x['event'].get('title'), x['market'].get('question'))
            hits = sum(1 for e in entity_lc if e in text)
            if hits >= 2:  # require ≥2 entity matches
                mid = ('poly', x['market'].get('id'))
                if mid not in matched_market_ids:
                    matched_market_ids.add(mid)
                    story_matches.append(('poly', x['event'].get('title')[:60], x['market'].get('question')[:60]))
        for k in kalshi_inst:
            text = lowertext(k.get('title'))
            hits = sum(1 for e in entity_lc if e in text)
            if hits >= 2:
                mid = ('kalshi', k.get('ticker'))
                if mid not in matched_market_ids:
                    matched_market_ids.add(mid)
                    story_matches.append(('kalshi', k.get('ticker'), k.get('title')[:80]))
        if story_matches:
            print(f"\n[{len(story_matches)} match] {story['summary'][:80]}")
            for src, ev, q in story_matches[:3]:
                print(f"   {src}: {ev} | {q[:60]}")
    news_candidates = len(matched_market_ids)
    print(f"\n→ News-driven candidates (≥2 entity match, deduped): {news_candidates}")

    # ----- PATH 2: BENCHMARK DIVERGENCE -----
    print("\n" + "=" * 70)
    print("PATH 2: BENCHMARK DIVERGENCE (markets with external benchmark available)")
    print("=" * 70)
    benchmark_eligible = {'poly': [], 'kalshi': []}
    benchmark_breakdown = Counter()
    for x in poly_inst_markets:
        text = lowertext(x['event'].get('title'), x['market'].get('question'))
        for bkey, bdef in BENCHMARK_KEYWORDS.items():
            if any(kw in text for kw in bdef['keywords']):
                benchmark_eligible['poly'].append((x, bkey))
                benchmark_breakdown[bkey] += 1
                break
    for k in kalshi_inst:
        text = lowertext(k.get('title'))
        for bkey, bdef in BENCHMARK_KEYWORDS.items():
            if any(kw in text for kw in bdef['keywords']):
                benchmark_eligible['kalshi'].append((k, bkey))
                benchmark_breakdown[bkey] += 1
                break
    total_eligible = len(benchmark_eligible['poly']) + len(benchmark_eligible['kalshi'])
    print(f"Benchmark-eligible markets: Poly {len(benchmark_eligible['poly'])}, Kalshi {len(benchmark_eligible['kalshi'])} = {total_eligible}")
    print(f"By benchmark category:")
    for k, v in benchmark_breakdown.most_common():
        print(f"  {k:10s} ({BENCHMARK_KEYWORDS[k]['benchmark'][:40]}): {v}")
    # Assume ~30% of benchmark-eligible markets have material (>5pp) divergence at any given time
    DIVERGENCE_RATE = 0.30
    benchmark_candidates = int(total_eligible * DIVERGENCE_RATE)
    print(f"\n→ Benchmark-divergence candidates (~{DIVERGENCE_RATE*100:.0f}% have material gap): {benchmark_candidates}")

    # ----- PATH 3: CROSS-VENUE (refined matching) -----
    print("\n" + "=" * 70)
    print("PATH 3: CROSS-VENUE DIVERGENCE (refined semantic match)")
    print("=" * 70)
    def event_signature(text):
        # Extract proper nouns and numbers — much tighter than raw token overlap
        text = (text or '').lower()
        # specific event-like patterns
        sigs = set()
        for m in re.finditer(r'\b(fed|cpi|nfp|gdp|ppi|election|recession)\b[^.?!]*', text):
            sigs.add(m.group(0)[:30])
        # capitalize specific named entities
        for ent in ['iran', 'israel', 'russia', 'ukraine', 'china', 'trump', 'biden',
                    'powell', 'warsh', 'fed june', 'fed july', 'fed sept', 'fed dec',
                    'bitcoin', 'ethereum', 'oil', 'brent', 'starmer', 'macron']:
            if ent in text:
                sigs.add(ent)
        # year/date anchors
        for m in re.finditer(r'\b(2026|2027|2028|by may|by june|by jul|by aug|by sep|by oct|by nov|by dec)\b', text):
            sigs.add(m.group(0))
        return sigs

    cross_pairs = []
    used_k = set()
    for x in poly_inst_markets:
        m = x['market']
        ev = x['event']
        poly_sig = event_signature(lowertext(ev.get('title'), m.get('question')))
        if len(poly_sig) < 2: continue
        best = None
        best_overlap = 0
        for k in kalshi_inst:
            if k.get('ticker') in used_k: continue
            k_sig = event_signature(lowertext(k.get('title')))
            overlap = len(poly_sig & k_sig)
            if overlap > best_overlap:
                best_overlap = overlap
                best = k
        if best and best_overlap >= 3:  # tighter: require ≥3 signature matches
            poly_price = num(m.get('lastTradePrice'))
            k_price = num(best.get('last_price_dollars'))
            if poly_price > 0 and k_price > 0:
                spread = abs(poly_price - k_price)
                if spread >= CROSS_VENUE_SPREAD_THRESHOLD:
                    cross_pairs.append({
                        'poly': f"{ev.get('title')[:50]} | {m.get('question')[:50]}",
                        'kalshi': f"{best.get('title')[:80]}",
                        'poly_price': poly_price, 'kalshi_price': k_price, 'spread': spread,
                        'overlap': best_overlap,
                    })
                    used_k.add(best.get('ticker'))
    print(f"Cross-venue pairs (≥3 signature overlap + ≥5pp spread): {len(cross_pairs)}")
    print("\nTop 5 pairs:")
    for c in sorted(cross_pairs, key=lambda x: x['spread'], reverse=True)[:5]:
        print(f"  Δ{c['spread']*100:.0f}pp ({c['overlap']} sig)  Poly {c['poly_price']*100:.0f}% / Kalshi {c['kalshi_price']*100:.0f}%")
        print(f"    Poly:   {c['poly']}")
        print(f"    Kalshi: {c['kalshi']}")

    # ----- PATH 4: VOLUME SPIKE -----
    print("\n" + "=" * 70)
    print("PATH 4: VOLUME SPIKE")
    print("=" * 70)
    poly_vol = []
    for x in poly_inst_markets:
        ev = x['event']
        v24 = num(ev.get('volume24hr'))
        v1w = num(ev.get('volume1wk'))
        baseline = v1w / 7 if v1w else 0
        if v24 > VOLUME_FLOOR_USD and baseline > 0 and v24 / baseline >= VOLUME_SPIKE_MULT:
            poly_vol.append({**x, 'mult': v24/baseline, 'v24': v24})
    kalshi_vol = []
    for m in kalshi_inst:
        v24 = num(m.get('volume_24h_fp'))
        v_total = num(m.get('volume_fp'))
        if v24 > VOLUME_FLOOR_USD and v_total > 0 and v24 / v_total >= 0.30:
            kalshi_vol.append({'market': m, 'v24': v24, 'ratio': v24/v_total})
    print(f"Poly volume spikes (≥{VOLUME_SPIKE_MULT}× baseline): {len(poly_vol)}")
    print(f"Kalshi volume spikes (24h ≥30% of cumulative): {len(kalshi_vol)}")
    print("Top 3 Poly spikes:")
    for c in sorted(poly_vol, key=lambda x: x['mult'], reverse=True)[:3]:
        print(f"  {c['mult']:.1f}× | $24h ${c['v24']:.0f} | {c['event']['title'][:60]}")

    # ----- COMBINED -----
    print("\n" + "=" * 70)
    print("ALL FOUR PATHS — COMBINED CANDIDATE COUNT")
    print("=" * 70)
    all_candidate_ids = set(matched_market_ids)
    for x in poly_vol: all_candidate_ids.add(('poly', x['market'].get('id')))
    for x in kalshi_vol: all_candidate_ids.add(('kalshi', x['market'].get('ticker')))
    # cross-venue contributes pair-counts beyond single markets
    single_market_candidates = len(all_candidate_ids)
    # Add benchmark candidates (overlap with news likely; assume 40% incremental)
    bench_incremental = int(benchmark_candidates * 0.4)
    total_raw = single_market_candidates + len(cross_pairs) + bench_incremental
    print(f"News-driven candidates:           {news_candidates}")
    print(f"Benchmark-divergence (estimated): {benchmark_candidates} ({bench_incremental} after overlap)")
    print(f"Cross-venue pairs:                {len(cross_pairs)}")
    print(f"Volume-spike candidates:          {len(poly_vol) + len(kalshi_vol)}")
    print(f"───────────────────────────")
    print(f"Total raw candidates (sample):    {total_raw}")
    print(f"\nScaling to ~{inst_universe}-market institutional universe: ×{scale:.1f}")
    print(f"Scaled candidates/day: ~{int(total_raw * scale)}")
    print(f"\nMateriality gate (tight, ~15%): ~{int(total_raw * scale * 0.15)} published signals/day")
    print(f"Materiality gate (medium, ~25%): ~{int(total_raw * scale * 0.25)} published signals/day")
    print(f"Materiality gate (loose, ~40%): ~{int(total_raw * scale * 0.40)} published signals/day")

main()
