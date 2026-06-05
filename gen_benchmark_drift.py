"""
gen_benchmark_drift.py — CM Signal benchmark_drift wire generator.

Compares prediction-market pricing to the external benchmark a market resolves against, where one
exists: macro -> FRED (rates/inflation/jobs/GDP/10yr), equity indices -> Finnhub (SPY/QQQ proxies),
crypto -> CoinGecko spot. Each benchmarkable market's PM price + the benchmark's current value + trend
goes to a Claude judge, which renders a wire ONLY when the market prices meaningfully away from where
the data sits (the judge is the gate — no forced wires). Benchmarks are fetched ONCE and shared across
all markets using them (~5-10 source calls/day, far under any limit). The benchmark source URL is a REAL
external citation, so these wires cite their source directly.

Usage: python3 gen_benchmark_drift.py [--dry] [--min-vol 5000] [--max 10]
"""
import os, json, sys, time, re
from pathlib import Path
import requests
from dotenv import load_dotenv
from gen_news_cycle import now_utc, yz, no_dash, claude_json, OUT_DIR, BUNDLE, pct, compact_usd, venue_label

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
FRED_KEY = os.getenv("FRED_API_KEY")
FINNHUB_KEY = os.getenv("FINNHUB_API_KEY")
SITE = "https://clearmarket.fyi"

def _arg(flag, default, cast):
    return cast(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default
DRY = "--dry" in sys.argv
MIN_VOL = _arg("--min-vol", 5000.0, float)
MAX = _arg("--max", 10, int)

# ---------- benchmark fetch (cached + shared, rate-limit friendly) ----------
_cache = {}
def fred_value(sid):
    k = ("fred", sid)
    if k in _cache: return _cache[k]
    val = None
    try:
        r = requests.get("https://api.stlouisfed.org/fred/series/observations",
                         params={"series_id": sid, "api_key": FRED_KEY, "file_type": "json",
                                 "sort_order": "desc", "limit": 14}, timeout=15)
        obs = [o for o in r.json().get("observations", []) if o.get("value") not in (".", None, "")]
        time.sleep(0.7)
        if obs:
            latest = float(obs[0]["value"])
            yago = float(obs[12]["value"]) if len(obs) > 12 else None
            val = {"value": latest, "date": obs[0]["date"], "yago": yago}
    except Exception:
        val = None
    _cache[k] = val; return val

def finnhub_quote(sym):
    k = ("fh", sym)
    if k in _cache: return _cache[k]
    val = None
    try:
        r = requests.get("https://finnhub.io/api/v1/quote", params={"symbol": sym, "token": FINNHUB_KEY}, timeout=12)
        j = r.json(); time.sleep(1.0)
        if j.get("c"):
            val = {"value": j["c"], "prev": j.get("pc")}
    except Exception:
        val = None
    _cache[k] = val; return val

def coingecko_spot(coin):
    k = ("cg", coin)
    if k in _cache: return _cache[k]
    val = None
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price",
                         params={"ids": coin, "vs_currencies": "usd", "include_24hr_change": "true"}, timeout=12)
        j = r.json().get(coin, {}); time.sleep(0.5)
        if j.get("usd"):
            val = {"value": j["usd"], "chg24h": j.get("usd_24h_change")}
    except Exception:
        val = None
    _cache[k] = val; return val

# ---------- shape gate: only LEVEL/THRESHOLD markets are benchmarkable against a spot value ----------
# A spot macro value (FRED rate/CPI) is a meaningful anchor ONLY for markets that name a numeric LEVEL
# of that metric ("CPI above 4%", "fed funds reach 5.25%"). Forward DECISION/COUNT markets ("will the
# Fed cut", "how many cuts in 2026") have no comparison to a spot level — pricing the *odds of an action*
# against the *current rate* is a unit mismatch, which is what produced the nonsense wires. The SYS
# prompt already says to skip these, but the LLM judge enforces it unreliably (skipped them one day,
# wired them the next), so enforce it deterministically here before anything reaches the judge.
_DECISION_RX = re.compile(
    r"\bhow many\b|\bnumber of\b|\brate (?:cut|cuts|hike|hikes)\b|\bcut rates\b|\bhike rates\b"
    r"|\braise rates\b|\blower rates\b|\b(?:no|zero|\d+)\s+(?:rate\s+)?(?:cut|cuts|hike|hikes)\b"
    r"|\bcut\s+\d+\s+times\b|\bwill the fed\s+(?:cut|hike|raise|lower)\b", re.I)
_LEVEL_RX = re.compile(r"\d+(?:\.\d+)?\s*(?:%|percent|bps|basis points)", re.I)

def is_levelthreshold_market(q):
    q = q or ""
    if _DECISION_RX.search(q):
        return False              # forward decision/count — no spot-level comparison exists
    return bool(_LEVEL_RX.search(q))  # must name a numeric level to anchor against the benchmark

# ---------- benchmark map: question keywords -> (label, current-value str, source url) ----------
def benchmark_for(q, entity):
    s = (q or "").lower() + " " + (entity or "").lower()
    # letter-boundary match so 'eth' doesn't fire on 'Hegseth', 'btc' not inside a word, etc.
    def has(*ws): return any(re.search(r"(?<![a-z])" + w + r"(?![a-z])", s) for w in ws)
    if has("federal funds", "fed funds", "fomc", "interest rate", "rate decision", "rate hike", "rate cut", "fed rate"):
        v = fred_value("DFEDTARU")
        if v: return ("Fed funds target rate, upper bound (FRED)", f"{v['value']:.2f}%", "https://fred.stlouisfed.org/series/DFEDTARU")
    if has("cpi", "inflation", "consumer price"):
        v = fred_value("CPIAUCSL")
        if v and v.get("yago"):
            yoy = (v["value"] / v["yago"] - 1) * 100
            return (f"CPI inflation, year-over-year (FRED)", f"{yoy:.1f}%", "https://fred.stlouisfed.org/series/CPIAUCSL")
    if has("unemployment", "jobless", "jobs report", "nonfarm", "payroll"):
        v = fred_value("UNRATE")
        if v: return ("Unemployment rate (FRED)", f"{v['value']:.1f}%", "https://fred.stlouisfed.org/series/UNRATE")
    if has("10-year", "10 year", "treasury yield", "10yr", "10-yr"):
        v = fred_value("DGS10")
        if v: return ("10-year Treasury yield (FRED)", f"{v['value']:.2f}%", "https://fred.stlouisfed.org/series/DGS10")
    if has("real gdp", "gdp growth", "recession"):
        v = fred_value("A191RL1Q225SBEA")
        if v: return ("Real GDP growth, annualized (FRED)", f"{v['value']:.1f}%", "https://fred.stlouisfed.org/series/A191RL1Q225SBEA")
    # MACRO-ONLY. Crypto/equity-index spot is the UNDERLYING, not an independent benchmark — "BTC hits
    # $150k vs $66k spot" is distance-from-spot, not a drift vs an external forward estimate. Those return
    # post-launch via proper forward benchmarks (futures / FedWatch-style), Perplexity-sourced.
    return None

def find_candidates():
    b = json.loads(BUNDLE.read_text())
    evs = {e["event_id"]: e for e in b["events"]}
    cands = []
    today = str(now_utc().date())
    for m in b["markets"]:
        if (m.get("status") or "").lower() not in ("", "active", "open"):
            continue
        ra = (m.get("resolve_at") or m.get("close_at") or "")[:10]
        if ra and ra < today:
            continue  # expired/resolved — never write about a dead market (the snapshot may be stale)
        if (m.get("volume_total_usd") or 0) < MIN_VOL or m.get("last_price") is None:
            continue
        ev = evs.get(m.get("event_id")) or {}
        q = m.get("question_raw") or ev.get("question") or ""
        if not is_levelthreshold_market(q):
            continue  # drop forward decision/count markets — they have no spot-level benchmark
        bench = benchmark_for(q, m.get("underlying_reference") or "")
        if not bench:
            continue
        cands.append({"m": m, "ev": ev, "q": q, "bench": bench})
    # cap the candidate set passed to the judge (highest-volume, dedup similar questions)
    cands.sort(key=lambda d: d["m"].get("volume_total_usd") or 0, reverse=True)
    seen, out = set(), []
    for d in cands:
        key = (d["bench"][0], d["q"][:30])
        if key in seen: continue
        seen.add(key); out.append(d)
        if len(out) >= 30: break
    return out

SYS = (
    "You write CM Signal BENCHMARK-DRIFT wire items: a prediction market pricing meaningfully away from "
    "the external benchmark it resolves against. Return ONLY JSON.\n"
    "Per candidate return {idx:int, drift:bool, semantic_title:str, headline:str, bullets:[str], interp:str}. "
    "Set drift=false and OMIT from items if the PM pricing is broadly consistent with where the benchmark sits.\n"
    "- SEMANTIC_TITLE (durable, indexed title — telemetry is added deterministically, not by you): a "
    "MARKET-STANCE line, wire-service register, framing the market's pricing RELATIVE TO the hard macro "
    "benchmark it resolves against. Do NOT predict the outcome and do NOT pose a question — report the "
    "divergence or tracking velocity vs the baseline data. Register: macro friction + deviation from FRED/BLS "
    "baselines. Palette (inspiration, NOT a lookup): outruns, paces ahead, gaps, lags, overshoots, tracks "
    "tight, challenges, detaches, nears full pricing. MAX 62 characters (hard limit — count them; the long stance tail is the usual cause, keep it 2-3 words). NO probability, NO venue names, NO math "
    "symbols (≥, ≤, ~, %); claim-defining figures (the level/threshold/date in the question) may be spelled "
    "out ('4 percent', 'by end-2026'); the PROBABILITY and the benchmark NUMBER are forbidden in the title. "
    "NUMBER FORMAT: compact notation only — dollar PRICE LEVELS from the claim as $65K or $150K, non-dollar counts/index levels as 30K / 80K (the 24h trading VOLUME is telemetry — NEVER put a volume dollar figure in the title); NEVER spell out 'thousand' or 'million'. Snapshot only — no permanence. Do NOT invent a date/horizon absent from the question. VARIATION (whole "
    "batch in one call): alternate Subject-first and Market-first; do NOT reuse an opening verb/noun across "
    "items. GOOD: 'CPI above 4 percent nears full pricing in inflation markets'; 'Rate expectations detach "
    "from historical target trend'; 'Jobs pricing outruns the baseline policy path'. BAD (predicts/asks/has "
    "metrics): 'Fed funds to exceed 4.5%'; 'Fed Funds ≥4.5%: 3%; rate at 3.75%'.\n"
    "- ONLY wire markets about a LEVEL or THRESHOLD of the metric the benchmark measures (e.g. 'CPI above "
    "3%', 'unemployment below 5%', 'fed funds above 4.5%') where the current actual gives real context vs "
    "the threshold. SKIP markets about a forward DECISION or COUNT (will the Fed hike/cut, how many cuts in "
    "2026) — the current level does not inform a forward policy decision; set drift=false for those.\n"
    "- HEADLINE: terse Bloomberg-wire style. <=60 chars, 6-9 words, immediately graspable. Format "
    "'Subject: X%' — a COLON before the probability, never the bare 'at X%' — then the benchmark anchor "
    "after a semicolon. e.g. 'Fed cut by July: 30%; rate at 3.75%'. Use '%'.\n"
    "- CRITICAL — NO INVENTED NUMBERS: use ONLY the benchmark value given in the candidate. You have NO "
    "current market data beyond what is provided. Never introduce another figure from your own knowledge "
    "(an all-time high, a prior level, a forecast). If the market references a level we did NOT provide, "
    "set drift=false and OMIT it — do not fabricate the number.\n"
    "- BULLETS: 3-4, each ONE tight line (<=20 words). bullet 1 = the PM read (price as %). bullet 2 = the "
    "benchmark's current value (name it). bullet 3 = the drift — what the market implies vs the data. "
    "bullet 4 (optional) = the catalyst/resolution. Plain language; no jargon.\n"
    "- These are PREDICTION-MARKET contracts vs an official benchmark; name the venue + the benchmark. Do NOT "
    "claim the price 'moved' (no history). interp: one plain sentence on the divergence for a desk."
)

def render(cands):
    blocks = []
    for i, d in enumerate(cands):
        m = d["m"]; label, cur, _ = d["bench"]
        blocks.append(f'CANDIDATE {i}: "{d["q"][:90]}" | venue={m["platform"]} | PM price={(m.get("last_price") or 0)*100:.0f}% | '
                      f'BENCHMARK: {label} currently {cur}')
    user = (f"Today: {now_utc().date()}. Assess these {len(cands)} markets for benchmark drift:\n\n"
            + "\n".join(blocks)
            + '\n\nReturn {"items":[{"idx":int,"drift":bool,"semantic_title":str,"headline":str,"bullets":[str],"interp":str}]} — '
            "include ONLY genuine divergences (drift=true).")
    # resilient for the unattended cron: retry once on a transient empty/malformed response, then skip
    for attempt in range(2):
        try:
            res = claude_json(SYS, user, max_tokens=3000)
            return {it["idx"]: it for it in res.get("items", []) if it.get("drift")}
        except Exception as e:
            if attempt == 0:
                time.sleep(2); continue
            print(f"  benchmark render failed after retry ({str(e)[:60]}); skipping this run", flush=True)
            return {}

def slugify(s):
    import re
    return (re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:70]) or "benchmark-drift"

def strip_bench_value(title, cur):
    """Remove the benchmark's OWN numeric value from the stance title — it belongs in the telemetry
    line, not the headline. Targets the exact benchmark value only (e.g. '3.75'), so the market's own
    claim level (e.g. 'above 4 percent') is preserved. Falls back to the original if stripping would
    gut the title, so we never ship a mangled headline."""
    if not title or not cur:
        return title
    num = re.escape(cur.rstrip("%").strip())
    pat = re.compile(
        r"\s*\b(?:against|at|vs\.?|versus|to|from|above|below|behind|near|over|under)?\s*"
        + num + r"\s*(?:%|percent)\b\s*(?:ceiling|baseline|reading|level|mark|rate|target|line)?",
        re.I)
    out = re.sub(r"\s{2,}", " ", pat.sub(" ", title)).strip(" ,;:-—")  # sub with a SPACE so 'the 3.9 percent FRED' -> 'the FRED', never 'theFRED'
    return out if len(out.split()) >= 4 else title

def build_md(d, it, sig_id, slug, date):
    now = now_utc().isoformat(timespec="seconds")
    m, ev = d["m"], d["ev"]
    label, cur, src_url = d["bench"]
    bullets = [no_dash(b) for b in it.get("bullets", []) if b][:5]
    while len(bullets) < 3:
        bullets.append(f"{m['platform'].title()} prices {(m.get('last_price') or 0)*100:.0f}%; benchmark ({label}) sits at {cur}.")
    fm = [
        f"signal_id: {yz(sig_id)}", f"signal_slug: {yz(slug)}",
        f"headline: {yz(no_dash(it['headline']))}",
    ]
    # Title split (2026-06-04): semantic_title (durable) + telemetry (as-of: price · benchmark anchor)
    if it.get("semantic_title"):
        fm.append(f"semantic_title: {yz(strip_bench_value(no_dash(it['semantic_title']), cur))}")
    _bench_telemetry = f"{pct(m.get('last_price'))} · {label} {cur}"
    fm.append(f"telemetry: {yz(_bench_telemetry)}")
    fm += [
        'category_tag: "VS_BENCHMARK_DRIFT"', 'detection_path: "benchmark_drift"',
        'pre_news_classification: "concurrent"', f"published_at: {yz(now)}",
        f"event_id: {yz(ev.get('event_id') or m.get('event_id'))}",
        f"event_slug: {yz(ev.get('slug',''))}", f"event_question: {yz(ev.get('question') or d['q'])}",
        "primary_market:", f"  platform: {yz(m['platform'])}",
        f"  platform_market_id: {yz(m.get('platform_market_id') or m.get('market_id'))}",
        f"  question_raw: {yz(m.get('question_raw') or d['q'])}",
        f"  current_price: {m.get('last_price') if m.get('last_price') is not None else 0}",
    ]
    if m.get("volume_total_usd") is not None:
        fm.append(f"  volume_cumulative_usd: {m['volume_total_usd']}")
    if m.get("resolve_at"):
        fm.append(f"  resolves_at: {yz(m['resolve_at'])}")
    fm.append("bullets:")
    fm += [f"  - {yz(b)}" for b in bullets]
    fm += [
        "atomic_claims:", '  - type: "benchmark_divergence"',
        f"    provenance: {yz('PM price direct from ' + m['platform'] + ' API; benchmark ' + label + ' = ' + cur)}",
        "    field_provenance:",
        "      pm_price:", '        tier: "direct"', f'        method: "{m["platform"]}_api"',
        "      benchmark_value:", '        tier: "mediated"', f"        method: {yz(label)}",
        f"        source_url: {yz(src_url)}", f"        retrieved_at: {yz(now)}",
        "sources:",
        f"  - label: {yz(label + ': ' + cur)}", f"    url: {yz(src_url)}", f"    retrieved_at: {yz(now)}",
        "field_provenance:", f'  pm_data: "{m["platform"]}_api"',
        '  news_context: "benchmark_api"', '  editorial_judgment: "cm_signal_llm_judge"',
    ]
    body = no_dash(it.get("interp") or
                   f"Benchmark drift: {m['platform'].title()} prices this market away from {label} ({cur}). "
                   "The PM read is set against the official current value, retrieved at publish time.")
    return "---\n" + "\n".join(fm) + "\n---\n\n" + body + "\n"

def main():
    cands = find_candidates()
    print(f"{len(cands)} benchmarkable candidates (vol>=${MIN_VOL:,.0f}); benchmarks fetched: "
          f"{sum(1 for v in _cache.values() if v)}/{len(_cache)}", flush=True)
    for d in cands[:12]:
        print(f"  [{d['m']['platform'][:4]}] PM {(d['m'].get('last_price') or 0)*100:3.0f}%  vs  {d['bench'][1]:>10}  | {d['q'][:46]}", flush=True)
    if not cands or DRY:
        if DRY: print("--dry: no Claude call, nothing written")
        return
    rendered = render(cands)
    print(f"judge kept {len(rendered)} genuine drifts", flush=True)
    date = str(now_utc().date()); compact = date.replace("-", "")
    wrote = 0
    for i, d in enumerate(cands):
        it = rendered.get(i)
        if not it or not it.get("headline"):
            continue
        if wrote >= MAX: break
        slug = slugify(f"{d['q'][:42]}-vs-bench")
        (OUT_DIR / f"{date}-{slug}.md").write_text(build_md(d, it, f"CMSIG{compact}BD{i:02d}", slug, date))
        wrote += 1
    print(f"wrote {wrote} benchmark_drift wires", flush=True)

if __name__ == "__main__":
    main()
