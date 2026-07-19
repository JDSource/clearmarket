"""
CM Signal — news_cycle wire generator (the feasible-now wire type).

Per outputs/cm-signal/prd.md §5.1 + retrieval-provenance-stack-decision.md (Exa+Claude locked):
  1. Exa retrieves recent news across the institutional domains (full text + publishedDate + deep link).
  2. Mechanical keyword prefilter narrows each story to candidate ClearMarket events.
  3. ONE Claude (Sonnet) call ranks the stories, keeps only genuine PM matches, and renders each
     wire item (headline + 3-5 bullets + news_event story text + classification).
  4. We assemble the markdown frontmatter DETERMINISTICALLY: event/market structured fields come
     from the bundle (direct provenance), prose from Claude (editorial), URLs ONLY from Exa results
     (never model-emitted — provenance rule #1).

Output: web/src/content/signals/<date>-<slug>.md, validated by the Astro content schema.
No marks-history table exists, so pm_response price-change/lead-lag fields are omitted (honest);
the wire carries the market's CURRENT price + the story + provenance.

Usage: python3 gen_news_cycle.py [--dry-run] [--max N]
"""
import os, re, json, sys, hashlib
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
EXA_KEY = os.getenv("EXA_API_KEY")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
OUT_DIR = ROOT / "web/src/content/signals"
SONNET = "claude-sonnet-4-6"
API_BASE = os.getenv("CM_API_BASE", "https://api.clearmarket.fyi")  # live marks_daily volume signal

DRY = "--dry-run" in sys.argv
MAX_ITEMS = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 5
# --exclude CM-EVT-..,CM-EVT-..  : skip these events in the prefilter (for net-new batches)
EXCLUDE = set(sys.argv[sys.argv.index("--exclude") + 1].split(",")) if "--exclude" in sys.argv else set()

# Institutional-domain news queries (Exa is relevance-search; Claude ranks/selects downstream).
QUERIES = [
    "major U.S. Federal Reserve, inflation, jobs, and economic-data news",
    "major U.S. political, election, and policy news",
    "major geopolitical, international conflict, and diplomacy news",
    "major cryptocurrency, bitcoin, and digital-asset news",
]
# Events whose question is templated/ambiguous (placeholder strikes, unspecified thresholds) make
# bad news-match targets and were a source of contradictory wires — drop them from candidates.
PLACEHOLDER_RE = re.compile(r"\[[^\]]*\]|\ba specific\b|\bspecified\b|"
                            r"\bspecific (price|level|threshold|amount|value|high|low|point)\b", re.I)
STOP = set("the a an and or of to in on for by with at from is are be will would may "
           "this that these those it its as into over under after before about new "
           "us u.s. percent more most than have has had said says report reports".split())


def now_utc():
    return datetime.now(timezone.utc)


# ---- live marks (fetch-on-publish) ----------------------------------------------------------
# CM Signal wires were shipping prices read from the monthly static bundle while stamping
# tier:direct / retrieved_at:now — a false-freshness claim and the root cause of ~73% stale wires.
# live_marks() pulls CURRENT prices for OPEN markets straight from the venue APIs at generation
# time, keyed by platform_market_id (same fetch as fetch_marks.py). A resolved/closed market is
# ABSENT from an open-only fetch, so absence == not-live: live_refresh() returns None and the caller
# MUST skip it — never narrate a settled market as live, never stamp tier:direct on a snapshot price.
# With a real live pull behind it, the existing tier:direct / retrieved_at:now provenance is TRUE.
_KALSHI_BASE = "https://api.elections.kalshi.com/trade-api/v2"
_POLY_GAMMA = "https://gamma-api.polymarket.com"
_LIVE_MARKS = None


def live_marks(force=False):
    """{platform_market_id -> {platform, price, vol24, vol_total}} for OPEN markets on both venues.
    Fetched once per process. Resolved/closed markets do not appear (open-only fetch)."""
    global _LIVE_MARKS
    if _LIVE_MARKS is not None and not force:
        return _LIVE_MARKS
    out, hdr = {}, {"User-Agent": "clearmarket-live/0.1"}
    cursor = None  # Kalshi: paginate OPEN events w/ nested markets (key = ticker)
    for _ in range(150):
        params = {"limit": 200, "status": "open", "with_nested_markets": "true"}
        if cursor:
            params["cursor"] = cursor
        try:
            data = requests.get(f"{_KALSHI_BASE}/events", params=params, timeout=30, headers=hdr).json()
        except Exception:
            break
        for ev in data.get("events", []):
            for m in ev.get("markets", []) or []:
                t, lp = m.get("ticker"), m.get("last_price_dollars")
                # An OPEN Kalshi event still nests SETTLED markets (status finalized/inactive) at
                # their settlement price — require the market's OWN status be active, else a market
                # resolved-since-snapshot would ship as "live" at a (genuinely fresh) terminal price.
                if t and lp is not None and m.get("status") == "active":
                    out[t] = {"platform": "kalshi", "price": float(lp),
                              "vol24": float(m.get("volume_24h_fp") or 0),
                              "vol_total": float(m.get("volume_fp") or 0)}
        cursor = data.get("cursor")
        if not cursor:
            break
    offset = 0  # Polymarket: paginate OPEN Gamma events w/ nested markets (key = conditionId)
    for _ in range(150):
        try:
            batch = requests.get(f"{_POLY_GAMMA}/events", params={"closed": "false", "limit": 100, "offset": offset},
                                 timeout=30, headers=hdr).json()
        except Exception:
            break
        if not isinstance(batch, list):
            batch = []
        for ev in batch:
            for m in ev.get("markets", []) or []:
                cid, ltp = m.get("conditionId"), m.get("lastTradePrice")
                # An OPEN Polymarket event still nests resolved markets (closed=true) at 1.0/0.001 —
                # require the market itself be not-closed, else a since-snapshot resolution ships live.
                if cid and ltp is not None and not m.get("closed"):
                    out[cid] = {"platform": "polymarket", "price": float(ltp),
                                "vol24": float(m.get("volume24hr") or 0),
                                "vol_total": float(m.get("volume") or 0)}
        offset += 100
        if len(batch) < 100:
            break
    _LIVE_MARKS = out
    return out


def live_refresh(m):
    """Copy of bundle market `m` with LIVE last_price + volumes if it is still OPEN on its venue;
    None if not live (resolved/closed/delisted/unfetched). Callers MUST skip None.

    Two gates, both required:
      (a) data-layer status: resolved/closed is monotonic and can LEAD the venue's open flag (the
          venue keeps a market open through its settlement timer), so trust a resolved snapshot.
      (b) venue open-feed presence: catches markets that resolved SINCE the snapshot, where the
          stale bundle still says open — this is the leak that put 4 settled markets on live wires."""
    if (m.get("status") or "").lower() not in ("", "active", "open"):
        return None
    nid = m.get("platform_market_id")
    d = live_marks().get(nid) if nid else None
    if d is None:
        return None
    if d["price"] <= 0.0 or d["price"] >= 1.0:
        return None  # pinned at the exact floor/ceiling = settled-but-status-lagging on the venue; never a live signal (0.99/0.01 near-certain markets still pass)
    r = dict(m)
    r["last_price"] = d["price"]
    # Polymarket volumes are USD-native; Kalshi volumes are contract counts -> approx USD via price.
    if d["platform"] == "polymarket":
        r["volume_24h_usd"] = d["vol24"]
        if d["vol_total"]:
            r["volume_total_usd"] = d["vol_total"]
    else:
        r["volume_24h_usd"] = round(d["vol24"] * d["price"], 2)
        if d["vol_total"]:
            r["volume_total_usd"] = round(d["vol_total"] * d["price"], 2)
    r["status"] = "open"  # verified live this run, not the stale snapshot value
    r["_live"] = True
    return r


def slugify(s, maxlen=60):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:maxlen].rstrip("-")


def tokens(text):
    toks = re.split(r"[^a-z0-9]+", (text or "").lower())
    return {t for t in toks if len(t) > 3 and t not in STOP}


# ---- Exa retrieval -----------------------------------------------------
def exa_news(query, days=3, n=10):
    start = (now_utc() - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    r = requests.post(
        "https://api.exa.ai/search",
        headers={"x-api-key": EXA_KEY, "content-type": "application/json"},
        json={
            "query": query, "type": "auto", "category": "news",
            "numResults": n, "startPublishedDate": start,
            "contents": {"text": {"maxCharacters": 1200}},
        }, timeout=40,
    )
    r.raise_for_status()
    out = []
    for x in r.json().get("results", []):
        if not x.get("url"):
            continue
        out.append({
            "title": x.get("title") or "",
            "url": x["url"],
            "published_at": x.get("publishedDate"),
            "publisher": (x.get("author") or "").strip() or _domain(x["url"]),
            "text": (x.get("text") or "")[:1200],
        })
    return out


def _domain(url):
    m = re.search(r"https?://(?:www\.)?([^/]+)", url or "")
    return m.group(1) if m else ""


def fetch_movers(min_mult=2.0):
    """Day-over-day 24h-volume movers from the live API (marks_daily), keyed by event slug.
    Fail-safe: returns {} on any error or when <2 daily snapshots exist, so the generator runs
    identically until the series accrues. This is the volume_spike content/ranking signal."""
    try:
        r = requests.get(f"{API_BASE}/v1/markets/movers",
                         params={"min_mult": min_mult, "limit": 100}, timeout=8)
        r.raise_for_status()
        out = {}
        for m in r.json().get("movers", []):
            sl = m.get("slug")
            if sl and (sl not in out or (m.get("volume_mult") or 0) > out[sl]["mult"]):
                out[sl] = {"mult": m.get("volume_mult"), "pct": m.get("volume_delta_pct")}
        if out:
            print(f"movers: {len(out)} events with >= {min_mult}x day/day volume")
        return out
    except Exception as ex:
        print(f"  movers fetch skipped ({ex}); volume_spike annotations off this run")
        return {}


def ladder_read(markets):
    """Reconstruct a monotonic strike ladder from the bundle's structured fields (threshold/direction/
    last_price) — deterministic, no LLM. Fixes the enrichment bug where a multinomial event got a
    mislabeled question + an arbitrary 'primary' strike. Returns the distribution read or None."""
    strikes = []
    for m in markets:
        thr, dr, p = m.get("threshold"), m.get("direction"), m.get("last_price")
        if thr is None or dr not in ("above", "below") or p is None:
            continue
        strikes.append({"thr": float(thr), "dir": dr, "prob": float(p), "m": m})
    if len(strikes) < 3 or len({s["dir"] for s in strikes}) != 1:
        return None
    direction = strikes[0]["dir"]
    strikes.sort(key=lambda s: s["thr"])
    # Monotonicity guard: a real "above X" ladder has non-increasing probability as the strike rises
    # (and "below X" non-decreasing). Allow only small bid/ask/staleness noise (<=5pp); any larger
    # INVERSION (e.g. 75% above 4.25% then 90% above 4.50%, or 6% above 3.9% then 82% above 4.0%) is
    # mathematically impossible = dirty data -> reject the ladder (event stays BINARY), never narrate it.
    TOL = 0.05
    probs = [s["prob"] for s in strikes]
    rises = [probs[k + 1] - probs[k] for k in range(len(probs) - 1)]
    if direction == "above" and max(rises, default=0) > TOL:
        return None
    if direction == "below" and min(rises, default=0) < -TOL:
        return None
    if direction == "above":
        above = [s for s in strikes if s["prob"] >= 0.5]
        below = [s for s in strikes if s["prob"] < 0.5]
        lo = above[-1]["thr"] if above else None
        hi = below[0]["thr"] if below else None
    else:
        below = [s for s in strikes if s["prob"] >= 0.5]
        above = [s for s in strikes if s["prob"] < 0.5]
        hi = below[-1]["thr"] if below else None
        lo = above[0]["thr"] if above else None
    anchor = next((s for s in strikes if s["prob"] < 0.5), strikes[-1])
    return {"direction": direction, "n": len(strikes),
            "strikes": [(s["thr"], round(s["prob"] * 100)) for s in strikes],
            "implied_band": (lo, hi), "anchor_market": anchor["m"], "anchor_prob": anchor["prob"],
            "sample_question": strikes[0]["m"].get("question_raw") or ""}


# ---- Anthropic ---------------------------------------------------------
def claude_json(system, user, max_tokens=4000):
    from anthropic import Anthropic
    client = Anthropic(api_key=ANTHROPIC_KEY)
    resp = client.messages.create(
        model=SONNET, max_tokens=max_tokens, system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    # strip code fences if present
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    return json.loads(text)


# ---- main --------------------------------------------------------------
def main():
    if not EXA_KEY or not ANTHROPIC_KEY:
        sys.exit("Missing EXA_API_KEY or ANTHROPIC_API_KEY in .env")

    bundle = json.loads(BUNDLE.read_text())
    # fetch-on-publish (news_cycle): replace snapshot prices with LIVE venue prices and DROP markets
    # that are not live, BEFORE any price reaches the LLM prompt, the ladder strike distribution, or
    # the emitted frontmatter — so the authored headline % and bullets are never the stale snapshot
    # value and tier:direct is honest. live_marks() is fetched once and cached. (Emit-time live_refresh
    # downstream is now idempotent defense.)
    bundle["markets"] = [lm for m in bundle["markets"] if (lm := live_refresh(m)) is not None]
    # freshness: drop fully-expired events (latest market resolve date already past) so a stale
    # snapshot never yields a wire about a dead market.
    _today = now_utc().date().isoformat()
    _ev_latest = {}
    for _m in bundle["markets"]:
        _eid, _ra = _m.get("event_id"), (_m.get("resolve_at") or _m.get("close_at") or "")[:10]
        if _eid and _ra:
            _ev_latest[_eid] = max(_ev_latest.get(_eid, ""), _ra)
    events = [e for e in bundle["events"] if e.get("published") is not False
              and _ev_latest.get(e["event_id"], _today) >= _today]
    mkt_by_id = {m["market_id"]: m for m in bundle["markets"]}
    # event token index for mechanical prefilter
    ev_tokens = {e["event_id"]: tokens(e.get("question", "") + " " + " ".join(e.get("tags") or [])) for e in events}
    ev_by_id = {e["event_id"]: e for e in events}
    # Market count per event. Multinomial strike-ladders (Fed-rate "above X%", CPI strikes) and
    # multi-candidate fields carry 5-26 markets; clean binary news events carry 1-4. The enrichment
    # mislabels the event question + picks a meaningless "primary" strike for ladders, so they produce
    # garbage wires (the 2026-05-29 Fed/CPI contradiction). News_cycle needs ONE clean probability ->
    # skip events with >4 markets. (Proper fix = re-enrich ladders from venue strike fields, data-layer.)
    mkt_count, mbye = {}, {}
    for m in bundle["markets"]:
        eid = m.get("event_id")
        mkt_count[eid] = mkt_count.get(eid, 0) + 1
        mbye.setdefault(eid, []).append(m)

    # live day-over-day volume signal (empty until >=2 daily snapshots exist; degrades silently)
    movers = fetch_movers()

    # 1. retrieve
    stories, seen = [], set()
    for q in QUERIES:
        try:
            for s in exa_news(q):
                if s["url"] in seen:
                    continue
                seen.add(s["url"]); stories.append(s)
        except Exception as ex:
            print(f"  exa query failed ({q[:30]}...): {ex}")
    print(f"exa: {len(stories)} unique recent stories")
    if not stories:
        sys.exit("no stories retrieved")

    # 2. mechanical prefilter — candidate events per story. Clean binaries (<=4 markets) pass directly;
    # multinomial events pass ONLY if they reconstruct as a coherent strike ladder (ladder_read), which
    # repairs the enrichment mislabel deterministically. Other multinomials (multi-candidate fields) drop.
    enriched, ladder_by_eid = [], {}
    for i, s in enumerate(stories):
        st = tokens(s["title"] + " " + s["text"])
        scored = sorted(
            ((len(st & ev_tokens[eid]), eid) for eid in ev_tokens),
            key=lambda x: -x[0],
        )[:6]
        cands = []
        for sc, eid in scored:
            if sc < 2 or eid in EXCLUDE:
                continue
            ev = ev_by_id[eid]
            if PLACEHOLDER_RE.search(ev.get("question", "")):
                continue
            lr = ladder_read(mbye.get(eid, [])) if mkt_count.get(eid, 0) > 4 else None
            if mkt_count.get(eid, 0) <= 4 or lr:
                cands.append(ev)
                if lr:
                    ladder_by_eid[eid] = lr
        if cands:
            enriched.append((i, s, cands))
    print(f"prefilter: {len(enriched)} stories have >=1 candidate CM event")
    if not enriched:
        sys.exit("no story matched any CM event")

    # 3. one Claude call: rank + keep genuine matches + render — PRICE-FIRST, not news-first.
    def mkt_info(c):
        pm = mkt_by_id.get(c.get("primary_market_id")) or {}
        p = pm.get("last_price")
        pct = f"{round(p * 100)}%" if isinstance(p, (int, float)) else "n/a"
        rs = (pm.get("resolution_source") or pm.get("arbitration_model") or "unspecified")
        return pm.get("platform", "?"), pct, str(rs)[:55]

    story_blocks, cand_index = [], {}
    for i, s, cands in enriched:
        cand_index[i] = {c["event_id"]: c for c in cands}
        rows = []
        for c in cands:
            eid = c["event_id"]
            mv = movers.get(c.get("slug"))
            vol = f' | VOLUME +{mv["pct"]:.0f}% day/day ({mv["mult"]:.1f}x)' if mv and mv.get("pct") is not None else ""
            lr = ladder_by_eid.get(eid)
            if lr:
                lo, hi = lr["implied_band"]
                band = f"~{lo}-{hi}" if lo is not None and hi is not None else (f">={lo}" if lo is not None else f"<{hi}")
                strikes_str = ", ".join(f"{t}:{p}%" for t, p in lr["strikes"])
                rows.append(f'    - event_id={eid} | LADDER ({lr["direction"]}), market-implied {band}: '
                            f'[{strikes_str}]{vol} | sample: "{lr["sample_question"][:70]}"')
            else:
                plat, pct, rs = mkt_info(c)
                rows.append(f'    - event_id={eid} | {plat} prediction market now at {pct} '
                            f'| resolves via: {rs}{vol} | "{c.get("question","")[:85]}"')
        clist = "\n".join(rows)
        story_blocks.append(
            f'STORY {i}: "{s["title"]}" ({s["publisher"]}, {s.get("published_at")})\n'
            f'  excerpt: {s["text"][:400]}\n  candidate CM events (with current market price):\n{clist}'
        )
    system = (
        "You are the CM Signal news-cycle editor. CM Signal does NOT report the news; it reports the "
        "PRICE. Prediction markets are truth machines: the capital-weighted probability is the quote-worthy "
        "data point, and THAT is the story. The real intelligence is the RELATIONSHIP between the news and "
        "the price: does the market AGREE with the news, or FADE it? (e.g. an official sounds hawkish but the "
        "market holds flat = the market is fading the posture.) You are given recent news stories, each with "
        "candidate ClearMarket PREDICTION-MARKET events, each event's current price, and its named resolution "
        "source. For the most significant genuine matches, produce a wire that leads with the market read. "
        "CRITICAL: use ONLY the data provided (price, resolution source, the news). Do NOT invent price moves, "
        "volumes, open interest, order-book depth, or any metric you were not given - fabricated numbers "
        "destroy the product. Skip non-matches. Return STRICT JSON only, no prose."
    )
    schema_hint = (
        '{"items":[{"story_index":int,"event_id":"<one of the candidates>",'
        '"semantic_title":"<see SEMANTIC_TITLE rule: market-stance line, NO probability/venue/symbols, MAX 62 chars>",'
        '"headline":"<<=90 chars; LEAD with the market+probability, news is the as/after clause>",'
        '"story_summary":"<one sentence: the news catalyst>",'
        '"classification":"pre_news|concurrent|lagging",'
        '"event_label":"<for LADDER events ONLY: a clean metric name, e.g. \'June 2026 Fed funds upper bound\'; omit for binary events>",'
        '"bullets":["3-4 SHORT wire bullets, each ONE tight line (<=20 words), fragments OK; '
        'bullet 1 = the market read (venue + probability/implied range), bullet 2 = the news catalyst, '
        'bullet 3 = implication or cross-market read, bullet 4 (optional) = resolution mechanic"],'
        '"pm_note":"<one sentence: venue coverage / market response>"}]}'
    )
    user = (
        f"Today: {now_utc().date()}. Up to {MAX_ITEMS} wire items.\n\n"
        + "\n\n".join(story_blocks)
        + f"\n\nReturn JSON matching: {schema_hint}\n\n"
        "RULES:\n"
        "- event_id MUST be one of THAT story's candidates.\n"
        "- HEADLINE: tight wire/terminal style (Bloomberg convention). A NOUN PHRASE, not a sentence. "
        "Put the event/claim first, then the venue + probability as a compact read after a COLON. Drop "
        "articles (a/the) and filler verbs (holds/prices/trades at/currently). NO catalyst clause in the "
        "headline (the news goes in the bullets). Use '%' (price 0.30 = '30%'). Keep UNDER 55 characters. "
        "GOOD: 'US-Iran nuclear deal by 2027: Polymarket 77%'; 'Fed funds above 4.5% after June: Kalshi 99%'; "
        "'May CPI below 3%: Kalshi 20%'; 'Strait of Hormuz reopens by year-end: Polymarket 62%'. "
        "BAD (too long / filler verb / catalyst clause): 'Polymarket holds 77% on US-Iran nuclear deal before "
        "2027 as ceasefire reports emerge'. BAD (news headline): 'Fed's Jefferson flags upside inflation risks'.\n"
        "- SEMANTIC_TITLE (durable, indexed title — telemetry is added deterministically, not by you): a "
        "MARKET-STANCE line, written like a wire-service desk editor, capturing the CURRENT consensus pricing "
        "stance on this event. Do NOT predict the real-world outcome and do NOT pose a question — report how "
        "the market is pricing/positioning the claim. Register: consensus shifts + narrative alignment. "
        "Palette (inspiration, NOT a lookup table): commands, hardens, solidifies, fractures, wavers, breaks "
        "away, absorbs, anchors, nears full pricing, holds. MAX 62 characters (hard limit — count them; the long stance tail is the usual cause, keep it 2-3 words). NO probability, NO volume, NO venue "
        "names, NO math symbols (≥, ≤, ~, %). Claim-defining figures that DEFINE the market (a strike, level, "
        "or date in the question) ARE allowed — spell them out ('4 percent', '$150K', 'by June 30'); only the "
        "PROBABILITY and VOLUME are forbidden. NUMBER FORMAT: compact notation only — dollar PRICE LEVELS from the claim as $65K or $150K, non-dollar counts/index levels as 30K / 80K (the 24h trading VOLUME is telemetry — NEVER put a volume dollar figure in the title); NEVER spell out 'thousand' or 'million'; the '$' sign itself is REQUIRED notation, not a banned math symbol — write '$100K', never the word 'dollar' ('dollar 100K' / '100 dollar range' are wrong). Snapshot only: frame the current pricing state, never a "
        "permanent/final real-world consequence. Do NOT invent a date/horizon absent from the question. "
        "VARIATION (you write the whole batch in one call): alternate Subject-first ('Bass commands...') and "
        "Market-first ('Consensus hardens...') constructions; do NOT reuse the same opening verb/noun across "
        "items; never stack three identical grammar orders in a row. "
        "GOOD: 'Bass commands the LA mayoral race in prediction pricing'; 'Fed pause consensus solidifies "
        "after macro commentary'; 'CPI above 4 percent nears full pricing'. BAD (predicts/asks/has metrics): "
        "'Karen Bass to win LA mayor race'; 'Will CPI exceed 4%?'; 'Kalshi 99% on Fed hold'.\n"
        "- Identify PEOPLE by full name and role on first reference, as the source gives them (e.g. 'Fed "
        "Governor Lisa Cook', 'Treasury Secretary Scott Bessent', 'Vice Chair Philip Jefferson'), never a bare "
        "surname like 'Cook'.\n"
        "- Always make clear these are PREDICTION MARKETS (Polymarket/Kalshi contracts), NOT equities or "
        "commodities. Name the venue; never write a bare 'the contract'/'the market' that a reader could "
        "mistake for a stock or an Iranian/commodity contract. First reference: 'the Polymarket contract' / "
        "'on Kalshi' / 'prediction markets'. The venue is ALWAYS Kalshi or Polymarket — NEVER 'CM' or "
        "'ClearMarket': ClearMarket is the reference layer carrying the data, not a market; 'CM ladder' / "
        "'the ClearMarket ladder prices' is a misattribution (shipped 2026-07-18, banned).\n"
        "- LADDER events (marked 'LADDER' with a strike list): do NOT pick one strike and report it as a "
        "single probability. Read the DISTRIBUTION. State the market-implied level/range and the sharp tail, "
        "using the strike probabilities provided. Set event_label to a clean metric name. GOOD headline: "
        "'June Fed funds upper bound seen at 3.50-3.75%: Kalshi'. GOOD bullet 1: 'Kalshi pins the June 2026 "
        "Fed funds upper bound in the 3.50-3.75% range, pricing 96% above 3.50% but only 2% above 3.75%.'\n"
        "- BREVITY (newswire, not research note): each bullet is ONE tight line, <=20 words, scannable. "
        "No multi-clause analytical sentences, no semicolon-chained reasoning. Punchy. 3-4 bullets max.\n"
        "- BULLET 1 (binary events): the pricing lede (venue + probability as a percent, from the provided price).\n"
        "- BULLET 2: connect the news to the price in PLAIN language - state whether the market is consistent "
        "with the news or at odds with it. BANNED words: 'fade'/'fading' (jargon). BANNED claims: that the "
        "market 'moved'/'spiked'/'repriced'/'jumped' in PRICE - we have NO intraday price history, so state the "
        "current price level only. VOLUME EXCEPTION: if and only if a candidate row carries a measured "
        "'VOLUME +X% day/day' figure, that is real day-over-day volume from our marks history - you MAY state "
        "that TRADING VOLUME rose by that figure (volume only, never price), and it is a strong signal the claim "
        "is drawing fresh attention. With no such figure, the no-moves rule stands fully. GOOD: 'Cook signaled "
        "readiness to hike, but the Polymarket contract still puts only 30% on an actual hike'; 'the Kalshi "
        "contract at 99% is consistent with the hold officials described, with volume up 180% day over day'.\n"
        "- BULLET 3: only substantive, concrete context. NO op-ed filler ('this confirms inflation is "
        "re-accelerating' is BANNED). If you have nothing concrete, fold it into bullet 2 and use 4 bullets.\n"
        "- BULLET 4 (highest value): a companion/related prediction market - a longer horizon, the other venue, "
        "or a correlated market - and what the spread reveals (term structure, timeline doubt, cross-venue gap).\n"
        "- BULLET 5: resolution MECHANICS, not a calendar date. Use the NAMED resolution source provided (who/"
        "what settles it) and any settlement edge case. Do NOT just say 'data is due in June'.\n"
        "- NO punditry. Explain a price ONLY via other market prices (spreads, term structure, companion "
        "markets) or resolution mechanics. Do NOT speculate on a candidate's 'legal baggage'/'polarizing "
        "profile' or anything similar. Do NOT invent liquidity, order-book depth, open interest, or "
        "'institutional positioning' - we don't have that data.\n"
        "- VERIFY each contract's DIRECTION (above/below, yes/no) matches your narrative before pricing it. "
        "These wires are read TOGETHER: do NOT output two wires whose probabilities are mutually contradictory "
        "(e.g. one market 99% ABOVE a rate level in June and another 93% BELOW a lower level weeks later). If a "
        "candidate's price implies an impossibility against another candidate, DROP the ambiguous one.\n"
        "- Use ONLY the provided price + resolution source. Do NOT invent prices or URLs.\n"
        "- If several wires reference the same macro print (e.g. April PCE 3.8%), state the full figure in ONE "
        "wire; in the others reference it briefly without re-explaining.\n"
        "- Plain news-wire prose, subject-verb-object, NO em dashes.\n"
        "- classification: pre_news if markets clearly led the news, concurrent if alongside, lagging if after."
    )
    result = claude_json(system, user, max_tokens=min(1300 * MAX_ITEMS + 1500, 16000))
    items = result.get("items", [])[:MAX_ITEMS]
    print(f"claude: {len(items)} wire items rendered")

    # 4. assemble markdown deterministically
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for n, it in enumerate(items, 1):
        si = it.get("story_index")
        eid = it.get("event_id")
        if si not in cand_index or eid not in cand_index[si]:
            print(f"  skip: bad event_id {eid} for story {si}")
            continue
        story = next(s for i, s, c in enriched if i == si)
        ev = cand_index[si][eid]
        lr = ladder_by_eid.get(eid)
        if lr:
            # ladder wire: anchor on the sharp-tail strike (a real market w/ a real price); the
            # mislabeled stored event question is replaced by Claude's clean event_label.
            pm = lr["anchor_market"]
            if not it.get("event_label"):
                it["event_label"] = "market-implied level"
        else:
            pm = mkt_by_id.get(ev.get("primary_market_id")) or {}
        pm = live_refresh(pm) if pm else None
        if not pm:
            print(f"  skip: market not live (resolved/closed/aged-out since snapshot) for {eid}")
            continue  # never narrate a settled/stale market as live; live_refresh also makes the wire's price + tier:direct honest
        date = (story.get("published_at") or now_utc().isoformat())[:10]
        slug = f'{slugify(it["headline"])}-{date}'
        sig_id = "CMSIG" + date.replace("-", "") + f"{n:02d}"
        md = build_md(it, story, ev, pm, sig_id, slug, date)
        path = OUT_DIR / f"{date}-{slug}.md"
        if DRY:
            print(f"\n--- {path.name} ---\n{md[:700]}")
        else:
            path.write_text(md)
            written.append(path.name)
    if not DRY:
        print(f"\nwrote {len(written)} wire items:")
        for w in written:
            print("  ", w)


def yz(v):  # YAML-safe double-quoted scalar
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def no_dash(s):
    # Site rule: zero em/en dashes. LLMs emit them by default, so scan post-draft.
    s = re.sub(r"\s*[—–]\s*", ", ", str(s))
    return re.sub(r",\s*,", ",", s).strip()


# ---- Telemetry composition (deterministic; NEVER LLM) ------------------
# The `telemetry` frontmatter field is the terse as-of read rendered as a muted track after
# the semantic_title. Composed in Python from the same structured values the wire already
# carries, so there is zero fabrication risk. Mirrors composeTelemetry() in
# web/src/lib/signal-display.ts so old (fallback) and new (authored) wires render identically.
def pct(p):
    try:
        return f"{round(float(p) * 100)}%"
    except (TypeError, ValueError):
        return "—"


def compact_usd(n):
    try:
        n = float(n)
    except (TypeError, ValueError):
        return ""
    if n >= 1e9:
        return f"${n / 1e9:.1f}".rstrip("0").rstrip(".") + "B"
    if n >= 1e6:
        return f"${n / 1e6:.1f}".rstrip("0").rstrip(".") + "M"
    if n >= 1e3:
        return f"${round(n / 1e3)}K"
    return f"${round(n)}"


def venue_label(v):
    return {"polymarket": "Polymarket", "kalshi": "Kalshi"}.get(v, v or "")


def build_md(it, story, ev, pm, sig_id, slug, date):
    now = now_utc().isoformat(timespec="seconds")
    venue = pm.get("platform") or "polymarket"
    it = {**it,
          "headline": no_dash(it.get("headline", "")),
          "semantic_title": no_dash(it.get("semantic_title", "")),
          "story_summary": no_dash(it.get("story_summary", "")),
          "pm_note": no_dash(it.get("pm_note", "")),
          "bullets": [no_dash(b) for b in it.get("bullets", [])]}
    bullets = it.get("bullets", [])[:5]
    src_url = story["url"]
    pub = story.get("publisher") or _domain(src_url)
    pub_at = story.get("published_at") or now
    fm = []
    fm.append(f"signal_id: {yz(sig_id)}")
    fm.append(f"signal_slug: {yz(slug)}")
    fm.append(f"headline: {yz(it['headline'])}")
    # Title split (2026-06-04): semantic_title = durable indexed anchor; telemetry = as-of read.
    is_ladder = bool(it.get("event_label")) or ev.get("event_type") == "LADDER"
    if it.get("semantic_title"):
        fm.append(f"semantic_title: {yz(it['semantic_title'])}")
    telemetry = (f"{venue_label(venue)} ladder" if is_ladder
                 else f"{venue_label(venue)} {pct(pm.get('last_price'))}")
    fm.append(f"telemetry: {yz(telemetry.strip())}")
    fm.append('category_tag: "PRE_EVENT_PRICING"' if it.get("classification") == "pre_news" else 'category_tag: "MOMENTUM_REPRICING"')
    fm.append('detection_path: "news_cycle"')
    cls = it.get("classification") if it.get("classification") in ("pre_news", "concurrent", "lagging") else "concurrent"
    fm.append(f"pre_news_classification: {yz(cls)}")
    fm.append(f"published_at: {yz(pub_at)}")
    fm.append(f"event_id: {yz(ev['event_id'])}")
    fm.append(f"event_slug: {yz(ev.get('slug',''))}")
    fm.append(f"event_question: {yz(it.get('event_label') or ev.get('question',''))}")
    # primary market (direct provenance from the bundle)
    fm.append("primary_market:")
    fm.append(f"  platform: {yz(venue)}")
    fm.append(f"  platform_market_id: {yz(pm.get('platform_market_id') or pm.get('market_id') or 'n/a')}")
    fm.append(f"  question_raw: {yz(pm.get('question_raw') or ev.get('question',''))}")
    fm.append(f"  current_price: {pm.get('last_price') if pm.get('last_price') is not None else 0}")
    if pm.get("volume_24h_usd") is not None:
        fm.append(f"  volume_24h_usd: {pm['volume_24h_usd']}")
    if pm.get("arbitration_model"):
        fm.append(f"  arbitration_model: {yz(pm['arbitration_model'])}")
    if pm.get("resolution_source"):
        fm.append(f"  resolution_source: {yz(pm['resolution_source'])}")
    if pm.get("resolve_at"):
        fm.append(f"  resolves_at: {yz(pm['resolve_at'])}")
    # bullets
    fm.append("bullets:")
    for b in bullets:
        fm.append(f"  - {yz(b)}")
    # atomic claims: news_event (mediated, Exa) + pm_response (editorial note; no history for price-change)
    fm.append("atomic_claims:")
    fm.append('  - type: "news_event"')
    fm.append("    significance:")
    fm.append("      threshold: 5")
    fm.append('      threshold_unit: "rank"')
    fm.append("      passed: true")
    fm.append(f"      reason: {yz('surfaced in the daily Exa news-cycle scan; mechanically matched to an active ' + venue + ' market')}")
    fm.append(f"    story: {yz(no_dash(it.get('story_summary') or story['title']))}")
    fm.append(f"    publisher: {yz(pub)}")
    fm.append(f"    published_at: {yz(pub_at)}")
    fm.append(f"    source_url: {yz(src_url)}")
    fm.append("    field_provenance:")
    fm.append("      story:")
    fm.append('        tier: "mediated"')
    fm.append('        method: "exa_search"')
    fm.append(f"        source: {yz(pub)}")
    fm.append(f"        source_url: {yz(src_url)}")
    fm.append(f"        retrieved_at: {yz(now)}")
    fm.append("  - type: \"pm_response\"")
    fm.append(f"    notes: {yz(it.get('pm_note') or 'Market is the liquid prediction-market read on this story.')}")
    fm.append("    field_provenance:")
    fm.append("      notes:")
    fm.append('        tier: "editorial"')
    fm.append('        method: "llm_judge_cm_signal_v1"')
    # sources (>=1, deep link, retrieved_at)
    fm.append("sources:")
    fm.append(f"  - label: {yz(no_dash(pub + ': ' + (story['title'][:70] or 'source article')))}")
    fm.append(f"    url: {yz(src_url)}")
    if story.get("published_at"):
        fm.append(f"    published_at: {yz(story['published_at'])}")
    fm.append(f"    retrieved_at: {yz(now)}")
    fm.append("field_provenance:")
    fm.append(f'  pm_data: "{venue}_api"')
    fm.append('  news_context: "exa_search"')
    fm.append('  editorial_judgment: "cm_signal_llm_judge"')
    body = (
        "Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's "
        "significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on "
        "coverage, not editorial selection."
    )
    return "---\n" + "\n".join(fm) + "\n---\n\n" + body + "\n"


if __name__ == "__main__":
    main()
