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
    events = [e for e in bundle["events"] if e.get("published") is not False]
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
            lr = ladder_by_eid.get(eid)
            if lr:
                lo, hi = lr["implied_band"]
                band = f"~{lo}-{hi}" if lo is not None and hi is not None else (f">={lo}" if lo is not None else f"<{hi}")
                strikes_str = ", ".join(f"{t}:{p}%" for t, p in lr["strikes"])
                rows.append(f'    - event_id={eid} | LADDER ({lr["direction"]}), market-implied {band}: '
                            f'[{strikes_str}] | sample: "{lr["sample_question"][:70]}"')
            else:
                plat, pct, rs = mkt_info(c)
                rows.append(f'    - event_id={eid} | {plat} prediction market now at {pct} '
                            f'| resolves via: {rs} | "{c.get("question","")[:85]}"')
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
        '"headline":"<<=90 chars; LEAD with the market+probability, news is the as/after clause>",'
        '"story_summary":"<one sentence: the news catalyst>",'
        '"classification":"pre_news|concurrent|lagging",'
        '"event_label":"<for LADDER events ONLY: a clean metric name, e.g. \'June 2026 Fed funds upper bound\'; omit for binary events>",'
        '"bullets":["3-5 sentences; bullet 1 = the market read (venue + probability/implied range), '
        'bullets 2-3 = the news catalyst, bullets 4-5 = implication/venue/resolution"],'
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
        "- Identify PEOPLE by full name and role on first reference, as the source gives them (e.g. 'Fed "
        "Governor Lisa Cook', 'Treasury Secretary Scott Bessent', 'Vice Chair Philip Jefferson'), never a bare "
        "surname like 'Cook'.\n"
        "- Always make clear these are PREDICTION MARKETS (Polymarket/Kalshi contracts), NOT equities or "
        "commodities. Name the venue; never write a bare 'the contract'/'the market' that a reader could "
        "mistake for a stock or an Iranian/commodity contract. First reference: 'the Polymarket contract' / "
        "'on Kalshi' / 'prediction markets'.\n"
        "- LADDER events (marked 'LADDER' with a strike list): do NOT pick one strike and report it as a "
        "single probability. Read the DISTRIBUTION. State the market-implied level/range and the sharp tail, "
        "using the strike probabilities provided. Set event_label to a clean metric name. GOOD headline: "
        "'June Fed funds upper bound seen at 3.50-3.75%: Kalshi'. GOOD bullet 1: 'Kalshi pins the June 2026 "
        "Fed funds upper bound in the 3.50-3.75% range, pricing 96% above 3.50% but only 2% above 3.75%.'\n"
        "- BULLET 1 (binary events): the pricing lede (venue + probability as a percent, from the provided price).\n"
        "- BULLET 2: connect the news to the price in PLAIN language - state whether the market is consistent "
        "with the news or at odds with it. BANNED words: 'fade'/'fading' (jargon). BANNED claims: that the "
        "market 'moved'/'spiked'/'repriced'/'jumped' - we have NO intraday history, so state the current level "
        "only. GOOD: 'Cook signaled readiness to hike, but the Polymarket contract still puts only 30% on an "
        "actual hike'; 'the Kalshi contract at 99% is consistent with the hold officials described'.\n"
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


def build_md(it, story, ev, pm, sig_id, slug, date):
    now = now_utc().isoformat(timespec="seconds")
    venue = pm.get("platform") or "polymarket"
    it = {**it,
          "headline": no_dash(it.get("headline", "")),
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
    fm.append('category_tag: "PRE_NEWS_PRICING"' if it.get("classification") == "pre_news" else 'category_tag: "MOMENTUM_REPRICING"')
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
