#!/usr/bin/env python3
"""
ClearMarket Enhancement Script — v0.1.0

Transforms raw Kalshi + Polymarket API JSON into the ClearMarket 4-table
specimen shape (events / markets / marks / resolution_log), matching the
JSON Schema contracts in outputs/clearmarket/schema/.

Input:  ~/jeremy-os/raw/clearmarket-api-pulls-apr22/
Output: ~/jeremy-os/outputs/clearmarket/samples/<specimen>/specimen.json

Run:    python3 enhance.py
"""

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load .env from the script's directory
SCRIPT_DIR = Path(__file__).parent
load_dotenv(dotenv_path=SCRIPT_DIR / ".env")

# -----------------------------------------------------------------
# Paths
# -----------------------------------------------------------------
RAW_DIR     = Path.home() / "jeremy-os/raw/clearmarket-api-pulls-apr22"
OUTPUT_DIR  = Path.home() / "jeremy-os/outputs/clearmarket/samples"
CACHE_DIR   = SCRIPT_DIR / ".enhance-cache"
LLM_CACHE   = CACHE_DIR / "llm"
CLOB_CACHE  = CACHE_DIR / "clob"
RUN_AT      = datetime.now(timezone.utc).isoformat()
SNAPSHOT_DATE_STR = "2026-04-22"  # raw pulls were on Apr 22

# -----------------------------------------------------------------
# LLM client (Anthropic Haiku 4.5) with file-based cache
# -----------------------------------------------------------------
_llm_client = None
# Stats tracked per-model for accurate cost reporting
_llm_stats  = {}  # model -> {"calls", "cache_hits", "input_tokens", "output_tokens"}
LLM_MODEL_HAIKU  = "claude-haiku-4-5-20251001"  # fast + cheap, for mechanical fields
LLM_MODEL_SONNET = "claude-sonnet-4-6"          # better constraint-following, for editorial_notes


def _get_llm_client():
    global _llm_client
    if _llm_client is None:
        from anthropic import Anthropic
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY not set; load from .env or export it")
        _llm_client = Anthropic(api_key=api_key)
    return _llm_client


def _stats(model: str) -> dict:
    if model not in _llm_stats:
        _llm_stats[model] = {"calls": 0, "cache_hits": 0, "input_tokens": 0, "output_tokens": 0}
    return _llm_stats[model]


def llm_call(prompt: str, system: str = "", max_tokens: int = 300,
             model: str = LLM_MODEL_HAIKU) -> str:
    """Cached Anthropic call. Returns generated text. Model selectable per-call."""
    cache_key = hashlib.sha256(
        f"{model}|{max_tokens}|{system}|{prompt}".encode()
    ).hexdigest()[:24]
    cache_path = LLM_CACHE / f"{cache_key}.txt"
    if cache_path.exists():
        _stats(model)["cache_hits"] += 1
        return cache_path.read_text().strip()

    client = _get_llm_client()
    msg_kwargs = {
        "model":      model,
        "max_tokens": max_tokens,
        "messages":   [{"role": "user", "content": prompt}],
    }
    if system:
        msg_kwargs["system"] = system
    resp = client.messages.create(**msg_kwargs)
    text = resp.content[0].text.strip()

    s = _stats(model)
    s["calls"] += 1
    s["input_tokens"]  += resp.usage.input_tokens
    s["output_tokens"] += resp.usage.output_tokens

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(text)
    return text


# -----------------------------------------------------------------
# Polymarket CLOB order book fetcher with file cache
# -----------------------------------------------------------------
_clob_stats = {"fetches": 0, "cache_hits": 0, "failures": 0}
CLOB_BASE   = "https://clob.polymarket.com"


def fetch_clob_orderbook(token_id: str) -> dict:
    """GET /book?token_id=X. Returns {bids: [{price, size}, ...], asks: [...]}.
    Cached to disk; subsequent runs are offline.
    """
    cache_path = CLOB_CACHE / f"{token_id}.json"
    if cache_path.exists():
        _clob_stats["cache_hits"] += 1
        return json.loads(cache_path.read_text())
    try:
        r = requests.get(f"{CLOB_BASE}/book", params={"token_id": token_id}, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        _clob_stats["failures"] += 1
        print(f"  [clob] fetch failed for {token_id[:12]}...: {e}", file=sys.stderr)
        return {"bids": [], "asks": []}
    _clob_stats["fetches"] += 1
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(data))
    return data


def _best_price(book_side: list, side: str) -> tuple:
    """Return (best_price, best_size_in_usd) or (None, None). side = 'bid' or 'ask'."""
    if not book_side:
        return (None, None)
    entries = [(float(e["price"]), float(e["size"])) for e in book_side
               if e.get("price") is not None and e.get("size") is not None]
    if not entries:
        return (None, None)
    best = max(entries, key=lambda x: x[0]) if side == "bid" else min(entries, key=lambda x: x[0])
    price, size_shares = best
    # Poly CLOB size is in shares. USD notional = shares * price.
    size_usd = round(size_shares * price, 2)
    return (price, size_usd)

# -----------------------------------------------------------------
# Specimen configs — one per shipping specimen
# -----------------------------------------------------------------
SPECIMENS = [
    {
        "id":       "iran",
        "sources":  ["poly-iran.json"],
        "pattern":  "poly_per_market_event",    # each child market = distinct canonical question
        "category": "geopolitics",
        "tags":     ["iran-conflict", "uma-subjective"],
        "res_source_type_default": "subjective",
        "editorial_autofill": {
            "poly_underlying_reference":    "No single structured data feed — resolution by consensus of credible news reporting (UMA Optimistic Oracle, subjective mechanism).",
            "poly_resolution_source_name":  "Credible news reporting (subjective — no specific feed cited in market description).",
            "editorial_notes":              "One of 9 sub-questions in the iran-conflict family. Polymarket lists as distinct deadline/scenario variants; all resolve via UMA optimistic oracle with subjective 'consensus of credible reporting' language. No named data source. Dispute risk is non-trivial given the interpretive latitude on what counts as 'qualifying military action' and 'consensus.' Pull the full family with /events?tag=iran-conflict.",
        },
    },
    {
        "id":       "fed-apr-2026",
        "sources":  ["poly-event-fed.json", "kalshi-fed-apr-markets.json", "kalshi-fed-series.json"],
        "pattern":  "shared_event_cross_platform",  # all markets slice ONE canonical question
        "category": "macro",
        "tags":     ["fed-rate-decisions", "fomc", "cross-platform", "macro"],
        "res_source_type_default": "central_bank",
        "kalshi_event_ticker":     "KXFED-26APR",  # filter Kalshi raw to just this series
        "canonical_question": "What will the Federal Reserve announce at the April 2026 FOMC meeting?",
        "canonical_slug": "fed-april-2026-rate-decision",
        "editorial_autofill": {
            "poly_underlying_reference":    "Federal Reserve FOMC statement (federalreserve.gov/monetarypolicy). Named in Polymarket description prose; mechanism is UMA optimistic oracle.",
            "poly_resolution_source_name":  "Federal Reserve (per market description; UMA arbitrates).",
            "poly_res_source_type_override":"central_bank",  # Fed Poly markets cite federalreserve.gov — NOT subjective
            "kalshi_underlying_reference":  "Upper bound of federal funds target rate per Federal Reserve Board of Governors (federalreserve.gov/monetarypolicy/fomccalendars.htm). Settled by Kalshi staff from Fed statement.",
            "editorial_notes":              "Cross-platform single event. 4 Polymarket directional markets (YES/NO on Fed actions) resolve via UMA optimistic oracle; 11 Kalshi strike markets (KXFED-26APR series) resolve via Kalshi staff against Federal Reserve Board of Governors releases. Both platforms point to the same real-world data source (Fed FOMC statement), but mechanism + arbiter differ. Primary market is a Kalshi strike for source clarity. Institutional buyers comparing across venues see uniform underlying + divergent mechanism — the canonical cross-venue normalization use case.",
        },
    },
    {
        "id":       "netanyahu",
        "sources":  ["poly-bibi.json"],
        "pattern":  "poly_per_market_event",
        "category": "geopolitics",
        "tags":     ["netanyahu", "israel", "uma-subjective"],
        "res_source_type_default": "subjective",
        "editorial_autofill": {
            "poly_underlying_reference":    "No single structured data feed — resolution by consensus of credible news reporting (UMA Optimistic Oracle, subjective mechanism).",
            "poly_resolution_source_name":  "Credible news reporting (subjective — no specific feed cited in market description).",
            "editorial_notes":              "One of 4 sub-questions in the netanyahu family. Polymarket lists as deadline variants on Netanyahu's tenure as Israeli PM; all resolve via UMA optimistic oracle with subjective source language. No named data feed. Dispute risk concentrated in resolution-timing edge cases (caretaker PM, coalition collapse, etc.). Pull the full family with /events?tag=netanyahu.",
        },
    },
    {
        "id":       "sp500-2026",
        "sources":  ["kalshi-inxy-markets.json", "kalshi-inxy-series.json"],
        "pattern":  "kalshi_shared_event",          # 30 strikes slice ONE canonical question
        "category": "macro",
        "tags":     ["sp500", "equities", "yearly", "strike-ladder"],
        "res_source_type_default": "regulated_data_vendor",
        "kalshi_event_ticker":     "KXINXY-26DEC31H1600",  # filter out legacy 2025 series contamination
        "canonical_question": "Where will the S&P 500 close on December 31, 2026?",
        "canonical_slug": "sp-500-close-end-of-2026",
        "editorial_autofill": {
            "kalshi_underlying_reference":  "S&P 500 index closing value on December 31, 2026, per S&P Dow Jones Indices (editorial clarification — Kalshi series metadata references 'for example, Google Finance' loosely; the authoritative index calculator is SPDJI).",
            "editorial_notes":              "Single event, 30-market strike ladder (Kalshi KXINXY-26DEC31H1600). Each binary strike resolves on the S&P 500 closing value at year-end 2026. Kalshi series settlement source is named loosely ('for example, Google Finance'); ClearMarket classifies as regulated_data_vendor because the authoritative index is calculated by S&P Dow Jones Indices. Primary market is a mid-ladder strike. This specimen demonstrates editorial refinement on top of weak platform source-naming — the Markit move.",
        },
    },
]

# -----------------------------------------------------------------
# Canonical ID generation — deterministic from slug
# Format: CM + 9 vowel-free base36 + 1 mod-10 check = 12 chars
# -----------------------------------------------------------------
VOWEL_FREE_ALPHABET = "0123456789BCDFGHJKLMNPQRSTVWXYZ"  # 31 chars


def generate_event_id(seed: str) -> str:
    h = hashlib.blake2s(seed.encode(), digest_size=16).hexdigest()
    num = int(h, 16)
    body = ""
    for _ in range(9):
        body = VOWEL_FREE_ALPHABET[num % len(VOWEL_FREE_ALPHABET)] + body
        num //= len(VOWEL_FREE_ALPHABET)
    check_val = sum(VOWEL_FREE_ALPHABET.index(c) for c in body) % 10
    return f"CM{body}{check_val}"


def load_json(filename: str):
    return json.loads((RAW_DIR / filename).read_text())


# Global market_id counter (BIGSERIAL analog)
_market_id_counter = 1000


def next_market_id() -> int:
    global _market_id_counter
    mid = _market_id_counter
    _market_id_counter += 1
    return mid


# -----------------------------------------------------------------
# Enhancement helpers — CM structures
# -----------------------------------------------------------------

EDITORIAL_STUB = "TO_BE_FILLED_BY_EDITOR"


def empty_field_provenance(stored_fields: dict, api_fields: set, editorial_fields: set) -> dict:
    """Flag each populated field with its source."""
    fp = {}
    for field, value in stored_fields.items():
        if value in (None, [], {}, EDITORIAL_STUB):
            continue
        if field in api_fields:
            fp[field] = {"source": "platform_api"}
        elif field in editorial_fields:
            fp[field] = {"source": "clearmarket_editorial"}
    return fp


def build_event(event_id: str, slug: str, question: str, category: str,
                tags: list, primary_market_id, catalyst_dates: list,
                editorial_notes, question_source: str = "clearmarket_editorial") -> dict:
    """Build an events-table row (stored shape, no derived fields)."""
    ev = {
        "event_id":              event_id,
        "slug":                  slug,
        "question":              question,
        "category":              category,
        "tags":                  tags,
        "primary_market_id":     primary_market_id,
        "primary_market_locked": False,
        "catalyst_dates":        catalyst_dates,
        "published":             True,
        "editorial_notes":       editorial_notes,
        "created_at":            RUN_AT,
        "updated_at":            RUN_AT,
    }
    # Provenance
    ev["field_provenance"] = {
        "slug":            {"source": "platform_api"},
        "question":        {"source": question_source},
        "category":        {"source": "clearmarket_editorial"},
        "tags":            {"source": "clearmarket_editorial"},
    }
    if editorial_notes:
        ev["field_provenance"]["editorial_notes"] = {"source": "clearmarket_editorial"}
    return ev


def poly_market_to_cm(poly_market: dict, event_id: str, res_source_type_default: str,
                      autofill: dict = None) -> dict:
    """Transform one Polymarket child market → CM markets row.

    `autofill` (per-specimen editorial defaults) can supply:
      - poly_underlying_reference       → str
      - poly_resolution_source_name     → str (used only when Poly ships empty)
      - poly_res_source_type_override   → str (overrides res_source_type_default)
    """
    autofill = autofill or {}
    res_source_type = autofill.get("poly_res_source_type_override") or res_source_type_default

    desc = poly_market.get("description") or ""
    poly_resolution_source = poly_market.get("resolutionSource") or None
    # Polymarket uma_resolution_status tells us the resolution state
    status = "open" if poly_market.get("active") and not poly_market.get("closed") else (
        "resolved" if poly_market.get("automaticallyResolved") or poly_market.get("umaResolutionStatus") == "resolved"
        else "closed"
    )

    # Resolved timestamp — use Poly's closedTime when the market actually resolved;
    # falls back to scheduled umaEndDate only if closedTime is absent.
    if status == "resolved":
        resolved_at = poly_market.get("closedTime") or poly_market.get("umaEndDate") or poly_market.get("endDate")
    else:
        resolved_at = None

    # underlying_reference: autofill wins if provided, else stub
    underlying_ref = autofill.get("poly_underlying_reference", EDITORIAL_STUB)

    # resolution_source_name: platform-shipped wins, else autofill, else stub
    if poly_resolution_source:
        resolution_source_name = poly_resolution_source
        resolution_source_name_src = "platform_api"
    elif "poly_resolution_source_name" in autofill:
        resolution_source_name = autofill["poly_resolution_source_name"]
        resolution_source_name_src = "clearmarket_editorial"
    else:
        resolution_source_name = EDITORIAL_STUB
        resolution_source_name_src = None

    m = {
        "market_id":                next_market_id(),
        "platform":                 "polymarket",
        "platform_market_id":       poly_market["conditionId"],
        "event_id":                 event_id,
        "platform_event_id":        None,  # Poly ships flat; parent event slug lives separately
        "question_raw":             poly_market.get("question"),
        "description_raw":          desc,
        "category_raw":             None,
        "contract_type":            "binary",
        "settlement_currency":      "USDC",
        "tick_size":                float(poly_market["orderPriceMinTickSize"]) if poly_market.get("orderPriceMinTickSize") else None,
        "contract_multiplier":      1.0,
        "underlying_reference":     underlying_ref,
        "close_at":                 poly_market.get("endDate"),
        "last_trading_date":        poly_market.get("endDate"),
        "resolve_at":               poly_market.get("umaEndDate") or poly_market.get("endDate"),
        "status":                   status,
        "resolution_rules_raw":     desc,  # Poly ships rules inline in description
        "resolution_triggers":      None,  # editor parses from description
        "resolution_mechanism":     "uma_oracle",
        "proposer_model":           "managed_whitelist",  # MOOV2 default Aug 2025+
        "resolution_source_name":   resolution_source_name,
        "resolution_source_url":    None,
        "resolution_source_type":   res_source_type,
        "contract_terms_url":       None,
        "resolution_outcome":       None,
        "resolution_value":         None,
        "resolved_at":              resolved_at,
        "first_seen_at":            RUN_AT,
        "last_updated_at":          RUN_AT,
    }
    m["field_provenance"] = {
        "platform":                {"source": "platform_api"},
        "platform_market_id":      {"source": "platform_api"},
        "question_raw":            {"source": "platform_api"},
        "description_raw":         {"source": "platform_api"},
        "contract_type":           {"source": "platform_api"},
        "settlement_currency":     {"source": "platform_api"},
        "tick_size":               {"source": "platform_api"},
        "close_at":                {"source": "platform_api"},
        "resolve_at":              {"source": "platform_api"},
        "status":                  {"source": "platform_api"},
        "resolution_rules_raw":    {"source": "platform_api"},
        "resolution_mechanism":    {"source": "clearmarket_editorial"},
        "proposer_model":          {"source": "clearmarket_editorial"},
        "resolution_source_type":  {"source": "clearmarket_editorial"},
        "event_id":                {"source": "clearmarket_editorial"},
    }
    if resolved_at:
        m["field_provenance"]["resolved_at"] = {"source": "platform_api"}
    if underlying_ref != EDITORIAL_STUB:
        m["field_provenance"]["underlying_reference"] = {"source": "clearmarket_editorial"}
    if resolution_source_name_src:
        m["field_provenance"]["resolution_source_name"] = {"source": resolution_source_name_src}
    return m


def kalshi_market_to_cm(kalshi_market: dict, event_id: str, series_meta: dict,
                        res_source_type: str, autofill: dict = None) -> dict:
    """Transform one Kalshi market → CM markets row.

    `autofill` can supply:
      - kalshi_underlying_reference → str

    Kalshi NEVER falls back to UMA-style subjective defaults. If series metadata
    lacks settlement_sources, resolution_source_name stays as EDITORIAL_STUB for
    human review — do not paper over with Poly-style phrasing.
    """
    autofill = autofill or {}

    # settlement_sources from the series — authoritative for Kalshi
    settlement_sources = series_meta.get("settlement_sources") or []
    source_name = settlement_sources[0]["name"] if settlement_sources else None
    source_url  = settlement_sources[0]["url"]  if settlement_sources else None

    # underlying_reference: autofill wins if provided, else stub
    underlying_ref = autofill.get("kalshi_underlying_reference", EDITORIAL_STUB)

    # status mapping
    status_raw = kalshi_market.get("status", "")
    status = {
        "active":   "open",
        "open":     "open",
        "closed":   "closed",
        "settled":  "resolved",
        "resolved": "resolved",
        "finalized":"resolved",
    }.get(status_raw, "open")

    # Kalshi ships rules split across rules_primary + rules_secondary
    rules_combined = "\n\n".join(filter(None, [
        kalshi_market.get("rules_primary"),
        kalshi_market.get("rules_secondary"),
    ]))

    m = {
        "market_id":                next_market_id(),
        "platform":                 "kalshi",
        "platform_market_id":       kalshi_market["ticker"],
        "event_id":                 event_id,
        "platform_event_id":        kalshi_market.get("event_ticker"),
        "question_raw":             kalshi_market.get("title"),
        "description_raw":          kalshi_market.get("subtitle") or kalshi_market.get("yes_sub_title"),
        "category_raw":             series_meta.get("category"),
        "contract_type":            "binary",
        "settlement_currency":      "USD",
        "tick_size":                0.01,  # Kalshi standard cent-tick
        "contract_multiplier":      float(kalshi_market.get("notional_value_dollars", 1.0)) if kalshi_market.get("notional_value_dollars") else 1.0,
        "underlying_reference":     underlying_ref,
        "close_at":                 kalshi_market.get("close_time"),
        "last_trading_date":        kalshi_market.get("close_time"),
        "resolve_at":               kalshi_market.get("expected_expiration_time") or kalshi_market.get("expiration_time"),
        "status":                   status,
        "resolution_rules_raw":     rules_combined or None,
        "resolution_triggers":      None,
        "resolution_mechanism":     "kalshi_staff",
        "proposer_model":           "platform_staff",
        "resolution_source_name":   source_name or EDITORIAL_STUB,
        "resolution_source_url":    source_url,
        "resolution_source_type":   res_source_type,
        "contract_terms_url":       series_meta.get("contract_terms_url"),
        "resolution_outcome":       kalshi_market.get("result") or None,
        "resolution_value":         float(kalshi_market["expiration_value"]) if kalshi_market.get("expiration_value") not in (None, "") else None,
        "resolved_at":              kalshi_market.get("expiration_time") if status == "resolved" else None,
        "first_seen_at":            RUN_AT,
        "last_updated_at":          RUN_AT,
    }
    m["field_provenance"] = {
        "platform":                {"source": "platform_api"},
        "platform_market_id":      {"source": "platform_api"},
        "platform_event_id":       {"source": "platform_api"},
        "question_raw":            {"source": "platform_api"},
        "description_raw":         {"source": "platform_api"},
        "category_raw":            {"source": "platform_api"},
        "contract_type":           {"source": "platform_api"},
        "settlement_currency":     {"source": "platform_api"},
        "tick_size":               {"source": "platform_api"},
        "contract_multiplier":     {"source": "platform_api"},
        "close_at":                {"source": "platform_api"},
        "resolve_at":              {"source": "platform_api"},
        "status":                  {"source": "platform_api"},
        "resolution_rules_raw":    {"source": "platform_api"},
        "contract_terms_url":      {"source": "platform_api"},
        "resolution_mechanism":    {"source": "clearmarket_editorial"},
        "proposer_model":          {"source": "clearmarket_editorial"},
        "resolution_source_type":  {"source": "clearmarket_editorial"},
        "event_id":                {"source": "clearmarket_editorial"},
    }
    if source_name:
        m["field_provenance"]["resolution_source_name"] = {"source": "platform_api"}
        m["field_provenance"]["resolution_source_url"]  = {"source": "platform_api"}
    if underlying_ref != EDITORIAL_STUB:
        m["field_provenance"]["underlying_reference"] = {"source": "clearmarket_editorial"}
    return m


def poly_mark_from_market(cm_market: dict, poly_market: dict) -> dict:
    """Build a marks row from a Polymarket market payload.

    v0.1: fetches full 4-side order book from Poly CLOB API per market.
    clobTokenIds is a 2-element JSON array [YES_token, NO_token].
    """
    # Fallback values from the Gamma event payload
    last_px       = _to_float(poly_market.get("lastTradePrice"))
    gamma_best_ask = _to_float(poly_market.get("bestAsk"))
    gamma_spread   = _to_float(poly_market.get("spread"))
    gamma_yes_bid  = (gamma_best_ask - gamma_spread) if (gamma_best_ask is not None and gamma_spread is not None) else None

    # CLOB: parse clobTokenIds (Poly ships as JSON string)
    token_ids_raw = poly_market.get("clobTokenIds")
    if isinstance(token_ids_raw, str):
        try:
            token_ids = json.loads(token_ids_raw)
        except json.JSONDecodeError:
            token_ids = []
    else:
        token_ids = token_ids_raw or []

    yes_bid = yes_ask = no_bid = no_ask = None
    yes_bid_size = yes_ask_size = no_bid_size = no_ask_size = None

    if len(token_ids) >= 2:
        yes_book = fetch_clob_orderbook(token_ids[0])
        no_book  = fetch_clob_orderbook(token_ids[1])
        yes_bid, yes_bid_size = _best_price(yes_book.get("bids", []), "bid")
        yes_ask, yes_ask_size = _best_price(yes_book.get("asks", []), "ask")
        no_bid,  no_bid_size  = _best_price(no_book.get("bids", []),  "bid")
        no_ask,  no_ask_size  = _best_price(no_book.get("asks", []),  "ask")

    # Fall back to Gamma-derived yes_bid/yes_ask if CLOB was unavailable
    if yes_bid is None:
        yes_bid = gamma_yes_bid
    if yes_ask is None:
        yes_ask = gamma_best_ask

    return _build_mark(
        market_id=cm_market["market_id"],
        yes_bid=yes_bid, yes_ask=yes_ask,
        no_bid=no_bid,   no_ask=no_ask,
        yes_bid_size_usd=yes_bid_size, yes_ask_size_usd=yes_ask_size,
        no_bid_size_usd=no_bid_size,   no_ask_size_usd=no_ask_size,
        yes_last=last_px,
        volume_24h=_to_float(poly_market.get("volume24hr")),
        volume_total=_to_float(poly_market.get("volume")),
        open_interest=None,  # Poly: requires on-chain subgraph, v0.2+
        source="platform_api",
        venue_updated_at=poly_market.get("updatedAt"),
        imputed_marker_fields=[],
    )


def kalshi_mark_from_market(cm_market: dict, kalshi_market: dict) -> dict:
    """Build a marks row from a Kalshi market payload."""
    yes_bid  = _to_float(kalshi_market.get("yes_bid_dollars"))
    yes_ask  = _to_float(kalshi_market.get("yes_ask_dollars"))
    no_bid   = _to_float(kalshi_market.get("no_bid_dollars"))
    no_ask   = _to_float(kalshi_market.get("no_ask_dollars"))
    last     = _to_float(kalshi_market.get("last_price_dollars"))

    # Sizes: Kalshi returns size in contracts (yes_bid_size_fp). USD-normalize = contracts * price.
    yes_bid_size_usd = _mult(kalshi_market.get("yes_bid_size_fp"), yes_bid)
    yes_ask_size_usd = _mult(kalshi_market.get("yes_ask_size_fp"), yes_ask)
    # Kalshi doesn't ship no_*_size directly — can be computed from YES side in binary markets (symmetric book). Leave null in v0.1.
    no_bid_size_usd  = None
    no_ask_size_usd  = None

    # Volume: Kalshi volume_fp is in contracts. Impute USD via last_price.
    volume_24h_usd   = _mult(kalshi_market.get("volume_24h_fp"), last)
    volume_total_usd = _mult(kalshi_market.get("volume_fp"),     last)
    oi_usd           = _mult(kalshi_market.get("open_interest_fp"), last)

    return _build_mark(
        market_id=cm_market["market_id"],
        yes_bid=yes_bid, yes_ask=yes_ask, no_bid=no_bid, no_ask=no_ask,
        yes_bid_size_usd=yes_bid_size_usd, yes_ask_size_usd=yes_ask_size_usd,
        no_bid_size_usd=no_bid_size_usd, no_ask_size_usd=no_ask_size_usd,
        yes_last=last,
        volume_24h=volume_24h_usd, volume_total=volume_total_usd,
        open_interest=oi_usd,
        source="platform_api",
        venue_updated_at=kalshi_market.get("updated_time"),
        imputed_marker_fields=["volume_24h_usd", "volume_total_usd", "open_interest_usd"],
    )


def _to_float(v):
    if v is None or v == "":
        return None
    return float(v)


def _mult(a, b):
    fa, fb = _to_float(a), _to_float(b)
    if fa is None or fb is None:
        return None
    return round(fa * fb, 2)


_mark_id_counter = 1


def _next_mark_id():
    global _mark_id_counter
    mid = _mark_id_counter
    _mark_id_counter += 1
    return mid


def _build_mark(market_id, yes_bid, yes_ask, yes_last, volume_24h, volume_total,
                open_interest, source, venue_updated_at,
                no_bid=None, no_ask=None,
                yes_bid_size_usd=None, yes_ask_size_usd=None,
                no_bid_size_usd=None, no_ask_size_usd=None,
                imputed_marker_fields=None) -> dict:

    mark = {
        "mark_id":              _next_mark_id(),
        "market_id":             market_id,
        "snapshot_date":         SNAPSHOT_DATE_STR,
        "snapshot_at":           RUN_AT,
        "source_updated_at":     venue_updated_at or RUN_AT,
        "yes_bid":               yes_bid,
        "yes_ask":               yes_ask,
        "no_bid":                no_bid,
        "no_ask":                no_ask,
        "yes_bid_size_usd":      yes_bid_size_usd,
        "yes_ask_size_usd":      yes_ask_size_usd,
        "no_bid_size_usd":       no_bid_size_usd,
        "no_ask_size_usd":       no_ask_size_usd,
        "yes_last_price":        yes_last,
        "implied_probability":   yes_last,   # binary: = last_price
        "volume_24h_usd":        volume_24h,
        "volume_total_usd":      volume_total,
        "open_interest_usd":     open_interest,
        "mark_method":           "venue_snapshot",
        "stale_flag":            False,
        "source_count":          1,
        "raw_payload":           None,  # Not committing the full blob in v0.1; API keeps raw elsewhere
    }

    fp = {}
    for f in ["yes_bid","yes_ask","no_bid","no_ask",
              "yes_bid_size_usd","yes_ask_size_usd","no_bid_size_usd","no_ask_size_usd",
              "yes_last_price","volume_24h_usd","volume_total_usd","open_interest_usd",
              "snapshot_at","source_updated_at"]:
        if mark.get(f) is not None:
            fp[f] = {"source": "platform_api"}
    if mark.get("implied_probability") is not None:
        fp["implied_probability"] = {"source": "derived"}
    for f in (imputed_marker_fields or []):
        if mark.get(f) is not None:
            fp[f] = {"source": "imputed"}
    # Venue-limited nulls
    for f, mark_f in [("no_bid","no_bid"),("no_ask","no_ask"),
                      ("no_bid_size_usd","no_bid_size_usd"),
                      ("no_ask_size_usd","no_ask_size_usd"),
                      ("open_interest_usd","open_interest_usd")]:
        if mark.get(mark_f) is None:
            fp[f] = {"source": "null_by_venue_limitation"}
    mark["field_provenance"] = fp
    return mark


# -----------------------------------------------------------------
# Specimen builders (per pattern)
# -----------------------------------------------------------------

def build_poly_per_market_event(spec, poly_data):
    """Iran / Netanyahu pattern: each Poly child market = distinct canonical question.

    Produces: N events, N markets, N marks.
    """
    autofill = spec.get("editorial_autofill", {})
    event_notes = autofill.get("editorial_notes", EDITORIAL_STUB)

    events, markets, marks = [], [], []
    for pm in poly_data["markets"]:
        slug = pm["slug"]
        event_id = generate_event_id(slug)

        cm_m = poly_market_to_cm(pm, event_id, spec["res_source_type_default"], autofill=autofill)
        markets.append(cm_m)

        ev = build_event(
            event_id=event_id,
            slug=slug,
            question=pm["question"],  # seed; editor refines
            category=spec["category"],
            tags=list(spec["tags"]),
            primary_market_id=cm_m["market_id"],
            catalyst_dates=[],  # editor fills per-event if desired
            editorial_notes=event_notes,
            question_source="platform_api",  # seeded from Poly; editor may rewrite
        )
        events.append(ev)

        marks.append(poly_mark_from_market(cm_m, pm))
    return events, markets, marks


def build_fed_cross_platform(spec):
    """Fed pattern: 1 canonical event, 4 Poly markets + 11 Kalshi markets, all → same event."""
    autofill = spec.get("editorial_autofill", {})
    kalshi_ticker_filter = spec.get("kalshi_event_ticker")

    poly_event = load_json("poly-event-fed.json")[0]
    kalshi_markets_response = load_json("kalshi-fed-apr-markets.json")
    kalshi_series = load_json("kalshi-fed-series.json")["series"]

    event_id = generate_event_id(spec["canonical_slug"])

    markets, marks = [], []
    # Poly markets — use autofill (which may override res_source_type_default to central_bank)
    for pm in poly_event.get("markets", []):
        cm_m = poly_market_to_cm(pm, event_id, spec["res_source_type_default"], autofill=autofill)
        markets.append(cm_m)
        marks.append(poly_mark_from_market(cm_m, pm))

    # Kalshi markets — filter to the configured event_ticker to avoid cross-series contamination
    for km in kalshi_markets_response["markets"]:
        if kalshi_ticker_filter and km.get("event_ticker") != kalshi_ticker_filter:
            continue
        cm_m = kalshi_market_to_cm(km, event_id, kalshi_series, "central_bank", autofill=autofill)
        markets.append(cm_m)
        marks.append(kalshi_mark_from_market(cm_m, km))

    # Primary = first Kalshi market (named source beats Poly UMA for headline clarity)
    kalshi_ms = [m for m in markets if m["platform"] == "kalshi"]
    primary = kalshi_ms[0] if kalshi_ms else markets[0]

    ev = build_event(
        event_id=event_id,
        slug=spec["canonical_slug"],
        question=spec["canonical_question"],
        category=spec["category"],
        tags=list(spec["tags"]),
        primary_market_id=primary["market_id"],
        catalyst_dates=[
            {"date": "2026-04-29", "event": "FOMC meeting Day 1"},
            {"date": "2026-04-30", "event": "FOMC statement + press conference"},
        ],
        editorial_notes=autofill.get("editorial_notes", EDITORIAL_STUB),
    )
    ev["primary_market_locked"] = True
    ev["field_provenance"]["primary_market_locked"] = {"source": "clearmarket_editorial"}
    ev["field_provenance"]["primary_market_id"] = {"source": "clearmarket_editorial"}
    ev["field_provenance"]["catalyst_dates"] = {"source": "clearmarket_editorial"}

    return [ev], markets, marks


def build_kalshi_shared_event(spec):
    """S&P 500 yearly pattern: 1 canonical event, Kalshi strike markets → same event."""
    autofill = spec.get("editorial_autofill", {})
    kalshi_ticker_filter = spec.get("kalshi_event_ticker")

    kalshi_markets_response = load_json("kalshi-inxy-markets.json")
    kalshi_series = load_json("kalshi-inxy-series.json")["series"]

    event_id = generate_event_id(spec["canonical_slug"])

    markets, marks = [], []
    for km in kalshi_markets_response["markets"]:
        # Filter to configured event_ticker to avoid cross-series contamination
        if kalshi_ticker_filter and km.get("event_ticker") != kalshi_ticker_filter:
            continue
        cm_m = kalshi_market_to_cm(km, event_id, kalshi_series, spec["res_source_type_default"], autofill=autofill)
        markets.append(cm_m)
        marks.append(kalshi_mark_from_market(cm_m, km))

    primary_idx = len(markets) // 2
    primary = markets[primary_idx]

    ev = build_event(
        event_id=event_id,
        slug=spec["canonical_slug"],
        question=spec["canonical_question"],
        category=spec["category"],
        tags=list(spec["tags"]),
        primary_market_id=primary["market_id"],
        catalyst_dates=[
            {"date": "2026-12-15", "event": "December FOMC meeting (last meaningful catalyst)"},
            {"date": "2026-12-31", "event": "S&P 500 final close of year"},
        ],
        editorial_notes=autofill.get("editorial_notes", EDITORIAL_STUB),
    )
    ev["primary_market_locked"] = True
    ev["field_provenance"]["primary_market_locked"] = {"source": "clearmarket_editorial"}
    ev["field_provenance"]["primary_market_id"] = {"source": "clearmarket_editorial"}
    ev["field_provenance"]["catalyst_dates"] = {"source": "clearmarket_editorial"}

    return [ev], markets, marks


# -----------------------------------------------------------------
# Derived-field population for denormalized specimen
# -----------------------------------------------------------------

def populate_derived(events, markets, marks):
    """Compute derived API fields and attach to each event / market / mark."""
    # Index helpers
    markets_by_event = {}
    for m in markets:
        markets_by_event.setdefault(m["event_id"], []).append(m)
    latest_mark_by_market = {m["market_id"]: m for m in marks}  # one mark per market in v0.1

    # Event-level derived
    for ev in events:
        ev_markets = markets_by_event.get(ev["event_id"], [])
        ev["venues_covered"] = sorted({m["platform"] for m in ev_markets})
        pmid = ev.get("primary_market_id")
        ev["current_primary_mark"] = latest_mark_by_market.get(pmid) if pmid else None
        ev["field_provenance"]["venues_covered"] = {"source": "derived"}
        if ev["current_primary_mark"] is not None:
            ev["field_provenance"]["current_primary_mark"] = {"source": "derived"}

    # Market-level derived
    # Group by event_id for cross-platform link
    for m in markets:
        sib_markets = markets_by_event.get(m["event_id"], [])
        by_platform = {}
        for sm in sib_markets:
            by_platform.setdefault(sm["platform"], 0)
            by_platform[sm["platform"]] += 1
        m["cross_platform_link"] = {
            "kalshi":     {"market_count": by_platform.get("kalshi", 0)},
            "polymarket": {"market_count": by_platform.get("polymarket", 0)},
        }
        m["field_provenance"]["cross_platform_link"] = {"source": "derived"}

    # Mark-level derived
    for mk in marks:
        if mk.get("yes_bid") is not None and mk.get("yes_ask") is not None:
            mk["spread"] = round(mk["yes_ask"] - mk["yes_bid"], 4)
            mk["mid"]    = round((mk["yes_bid"] + mk["yes_ask"]) / 2.0, 4)
        else:
            mk["spread"] = None
            mk["mid"]    = None
        mk["divergence_from_primary"] = None  # computed v0.2+ when multi-mark history exists
        mk["hours_since_source_update"] = 0.0 # fresh pull
        mk["field_provenance"]["spread"] = {"source": "derived"}
        mk["field_provenance"]["mid"]    = {"source": "derived"}
        mk["field_provenance"]["hours_since_source_update"] = {"source": "derived"}


# -----------------------------------------------------------------
# LLM enrichment pass (runs after deterministic build + populate_derived)
# -----------------------------------------------------------------

_EDITORIAL_PROSE_RULES = (
    "Today's date is April 23, 2026. When referring to market dates, use the year from the provided question or description; do not drift to earlier years. "
    "Do NOT use internal enum values in prose (e.g., write 'UMA Optimistic Oracle' not 'uma_oracle'; 'Kalshi staff determination' not 'kalshi_staff'). "
    "For index or data-product markets, name the authoritative calculator or publisher as the real source (e.g., 'S&P Dow Jones Indices' for the S&P 500; 'Federal Reserve Board of Governors' for fed funds), not platform-shorthand references (e.g., 'Google Finance'). "
    "Platform-named shorthand is a secondary distribution channel, not the authoritative source."
)


def llm_underlying_reference(market: dict) -> str:
    system = (
        "You are ClearMarket's editorial engine, identifying the real-world data source "
        "that determines a prediction market's resolution. Respond with ONE factual sentence, "
        "max 40 words. No em-dashes. No marketing language. No preamble. "
        + _EDITORIAL_PROSE_RULES
    )
    user = (
        f"Platform: {market['platform']}\n"
        f"Question: {market.get('question_raw', '')}\n"
        f"Description (trimmed): {(market.get('description_raw') or '')[:600]}\n"
        f"Resolution mechanism: {market.get('resolution_mechanism')}\n"
        f"Platform-named source: {market.get('resolution_source_name') or '(none)'}\n"
        f"Source URL: {market.get('resolution_source_url') or '(none)'}\n"
        f"Market close_at (authoritative): {market.get('close_at')}\n"
        f"Market resolve_at (authoritative): {market.get('resolve_at')}\n"
        f"Market status: {market.get('status')}\n\n"
        f"Write the one-sentence underlying_reference. IMPORTANT: take any date/year from close_at or resolve_at as authoritative; never infer a later year."
    )
    return llm_call(user, system=system, max_tokens=100)


def llm_editorial_notes(event: dict, event_markets: list) -> str:
    system = (
        "You are ClearMarket's editorial engine. Write institutional-grade notes about a "
        "prediction market event for a hedge fund / data distributor / swap desk reader. "
        "Cover in order: (a) what the event tracks, (b) how the markets relate to each other, "
        "(c) one notable source or resolution caveat. "
        "\n\nCROSS-PLATFORM INSIGHT RULE: "
        "When markets from two platforms structure the same event differently (direction vs. rate level, "
        "binary outcome vs. continuous range, discrete tiers vs. strike thresholds, directional vs. magnitude), "
        "name the structural difference as the cross-platform insight. Use parallel sentence structure to make "
        "the contrast visible. For Fed-like events: Polymarket prices direction, Kalshi prices the rate level. "
        "For election-like events: one platform asks outcome, the other asks margin. Name what each platform "
        "is actually pricing, not the raw market count or shape. "
        "\n\nVOCABULARY RULE: "
        "Use standard industry terminology. For Fed/rates events: 'target rate', 'upper bound', 'policy rate', "
        "'rate level' are correct; do NOT use 'landing rate' (colloquial, non-standard). For election events: "
        "'margin of victory', 'outcome', 'vote share' are correct. Default to the term a derivatives-trading "
        "reader would use, not a retail-news term. "
        "\n\nMECHANISM NAMING RULE: "
        "When citing UMA (the Optimistic Oracle resolution protocol), always contextualize it as Polymarket's "
        "resolution mechanism. Use phrases like 'Polymarket's UMA Optimistic Oracle' or 'the UMA protocol "
        "Polymarket uses for resolution'. Never reference UMA standalone — institutional readers may not know "
        "what UMA is. For Kalshi's mechanism, 'Kalshi staff determination' is self-explanatory. "
        "\n\nRESOLVED MARKET RULE: "
        "For markets with status=resolved (past deadline, already settled), describe resolution state factually "
        "using only the resolved_at timestamp. Do NOT speculate about outcome causes, 'historical clarity', "
        "'settlement patterns', escalation trajectories, or why markets resolved the way they did. You have no "
        "ground truth about outcome determination; never invent interpretation or commentary. "
        "\n\nCRITICAL STYLE CONSTRAINTS (Bloomberg-density prose): "
        "Write 3–4 SHORT sentences as PLAIN PROSE. Each sentence MAX 15 words. One claim per sentence. "
        "Match the density of a Bloomberg company-description field: terse, factual, no filler. "
        "Target total length: 40–50 words. Do not pad to fill space. "
        "Prefer short declarative sentences. No comma-chained subordinate clauses. "
        "If a sentence runs over 15 words, split it. "
        "\n\nFORMATTING RULES (strict): "
        "Do NOT use any markdown formatting. "
        "No **bold**. No # headers. No bullet lists. No numbered lists. "
        "No section labels like 'What it tracks:' or 'Resolution note:'. "
        "Write continuous prose only. Output is stored inside a JSON string field. "
        "\n\nNo em-dashes. No marketing language. No academic prose. "
        + _EDITORIAL_PROSE_RULES
    )
    mkt_rows = event_markets[:20]
    # Pass underlying_reference (our editorial authoritative source) to the LLM,
    # NOT resolution_source_name (raw platform text) — prevents e.g. "Google Finance"
    # from displacing "S&P Dow Jones Indices" in generated prose.
    markets_summary = "\n".join(
        f"  - [{m['platform']}] {(m.get('question_raw') or '')[:100]} | "
        f"mechanism={m.get('resolution_mechanism')}, "
        f"authoritative source={(m.get('underlying_reference') or 'unknown')[:120]}"
        for m in mkt_rows
    )
    if len(event_markets) > 20:
        markets_summary += f"\n  - ... and {len(event_markets)-20} more markets"
    # Authoritative date anchor from the first market
    anchor_close = event_markets[0].get("close_at") if event_markets else None
    anchor_resolve = event_markets[0].get("resolve_at") if event_markets else None
    user = (
        f"Canonical question: {event['question']}\n"
        f"Category: {event['category']}\n"
        f"Seed tags: {event.get('tags', [])}\n"
        f"Representative market close_at (authoritative): {anchor_close}\n"
        f"Representative market resolve_at (authoritative): {anchor_resolve}\n"
        f"Markets under this event ({len(event_markets)}):\n"
        f"{markets_summary}\n\n"
        f"Write the editorial_notes paragraph (3-4 sentences). "
        f"IMPORTANT: derive dates/years from close_at or resolve_at; never infer a later year."
    )
    # Use Sonnet for editorial_notes — better constraint-following on the 15-word-sentence cap
    return llm_call(user, system=system, max_tokens=250, model=LLM_MODEL_SONNET)


def llm_tags(event: dict, event_markets: list) -> list:
    system = (
        "You generate 4-6 tags for a prediction market event. Format: lowercase-hyphenated strings. "
        "Mix thematic family tags, attribute tags (mechanism/structure), and entity-specific tags. "
        "Return ONLY a JSON array of strings. No preamble, no prose. "
        "Today's date is April 23, 2026. Year tags should reflect the market's actual resolution year, not an earlier year. "
        "Avoid tags that restate an enum value (e.g., 'uma-subjective' is fine as a characterizing tag; 'uma_oracle' is not)."
    )
    example = (event_markets[0].get("question_raw") if event_markets else "") or ""
    anchor_close = event_markets[0].get("close_at") if event_markets else None
    # Extract just the year from close_at for explicit injection
    anchor_year = str(anchor_close)[:4] if anchor_close else None
    user = (
        f"Event question: {event['question']}\n"
        f"Category: {event['category']}\n"
        f"Seed tags (include if still relevant): {event.get('tags', [])}\n"
        f"Example market: {example[:100]}\n"
        f"Market count: {len(event_markets)}\n"
        f"Market close_at (authoritative): {anchor_close}\n"
        f"Resolution year (authoritative, derived from close_at): {anchor_year}\n\n"
        f"Return JSON array of 4-6 tags. If you include a year tag, use the authoritative year above — do not drift."
    )
    raw = llm_call(user, system=system, max_tokens=120)
    # Strip ``` fencing if present
    if raw.startswith("```"):
        raw = raw.strip("`").lstrip("json").strip()
    try:
        tags = json.loads(raw)
        if isinstance(tags, list) and all(isinstance(t, str) for t in tags):
            tags = tags[:6]
            # Guarantee the event's category enum appears as a tag (deterministic, not LLM-dependent)
            category = event.get("category")
            if category and category not in tags:
                tags.insert(0, category)
                tags = tags[:6]
            return tags
    except Exception:
        pass
    return None


def llm_canonical_question(event: dict) -> str:
    # Only rewrite when the current question is still raw platform text
    src = event.get("field_provenance", {}).get("question", {}).get("source")
    if src != "platform_api":
        return event["question"]
    system = (
        "Rewrite a prediction market question in clean grammatical English, "
        "preserving exact meaning, entities, and dates. Use 'Will X by DATE?' or equivalent. "
        "Return ONLY the rewritten question. No preamble, no quotes."
    )
    return llm_call(event["question"], system=system, max_tokens=80)


def enrich_with_llm(events: list, markets: list, enabled: bool = True):
    """Overwrite rule-based autofill with per-market/per-event LLM output.

    If LLM call fails for a field, the rule-based value is retained.
    """
    if not enabled:
        return
    markets_by_event = {}
    for m in markets:
        markets_by_event.setdefault(m["event_id"], []).append(m)

    # 1. Per-market: underlying_reference
    print(f"  [llm] enriching {len(markets)} markets (underlying_reference)... ", end="", flush=True)
    ok = 0
    for m in markets:
        try:
            m["underlying_reference"] = llm_underlying_reference(m)
            m["field_provenance"]["underlying_reference"] = {"source": "clearmarket_editorial", "ai_drafted": True}
            ok += 1
        except Exception as e:
            print(f"\n    market {m['market_id']}: {e}", file=sys.stderr)
    print(f"{ok}/{len(markets)} ok")

    # 2. Per-event: editorial_notes, tags, canonical question
    print(f"  [llm] enriching {len(events)} events (editorial_notes, tags, canonical question)... ", end="", flush=True)
    for ev in events:
        ev_markets = markets_by_event.get(ev["event_id"], [])
        try:
            ev["editorial_notes"] = llm_editorial_notes(ev, ev_markets)
            ev["field_provenance"]["editorial_notes"] = {"source": "clearmarket_editorial", "ai_drafted": True}
        except Exception as e:
            print(f"\n    event {ev['event_id']} editorial_notes: {e}", file=sys.stderr)
        try:
            new_tags = llm_tags(ev, ev_markets)
            if new_tags:
                ev["tags"] = new_tags
                ev["field_provenance"]["tags"] = {"source": "clearmarket_editorial", "ai_drafted": True}
        except Exception as e:
            print(f"\n    event {ev['event_id']} tags: {e}", file=sys.stderr)
        try:
            new_q = llm_canonical_question(ev)
            if new_q and new_q != ev["question"]:
                ev["question"] = new_q
                ev["field_provenance"]["question"] = {"source": "clearmarket_editorial", "ai_drafted": True}
        except Exception as e:
            print(f"\n    event {ev['event_id']} question: {e}", file=sys.stderr)
    print("done")


# -----------------------------------------------------------------
# Write specimen bundle
# -----------------------------------------------------------------

def count_ai_drafted(events, markets):
    """Count fields that carry the ai_drafted=True marker in field_provenance.

    Matches what Jeremy will actually see when grepping specimen files.
    """
    counts = {
        "markets.underlying_reference":    0,
        "markets.resolution_source_name":  0,
        "events.editorial_notes":          0,
        "events.tags":                     0,
        "events.question":                 0,
    }

    def is_ai(fp: dict, field: str) -> bool:
        return bool(fp.get(field, {}).get("ai_drafted"))

    for m in markets:
        fp = m.get("field_provenance", {})
        if is_ai(fp, "underlying_reference"):
            counts["markets.underlying_reference"] += 1
        if is_ai(fp, "resolution_source_name"):
            counts["markets.resolution_source_name"] += 1
    for e in events:
        fp = e.get("field_provenance", {})
        if is_ai(fp, "editorial_notes"):
            counts["events.editorial_notes"] += 1
        if is_ai(fp, "tags"):
            counts["events.tags"] += 1
        if is_ai(fp, "question"):
            counts["events.question"] += 1
    return counts


def build_review_note(counts: dict, stubs_remaining: int) -> str:
    lines = [
        "This specimen was generated by the Enhancement Script.",
        "AI-drafted fields are populated by Haiku 4.5 with per-event / per-market prompts.",
        "Scan the fields listed below; edit anything off-voice or factually wrong in place. No flags to clear.",
        "",
        "AI-drafted field counts in this specimen:",
    ]
    for k, v in counts.items():
        if v:
            lines.append(f"  - {v} × {k}")
    lines.append("")
    lines.append("Where AI draws the line (rules in enhance.py):")
    lines.append("  - Kalshi `resolution_source_name` / `resolution_source_url` ALWAYS pulled from series `settlement_sources`. No UMA fallback ever.")
    lines.append("  - Polymarket `resolution_source_name` uses editorial default ('Credible news reporting — subjective') ONLY when the Poly API ships empty.")
    lines.append("  - `underlying_reference`: per-market Haiku draft, anchored on market close_at for authoritative dates.")
    lines.append("  - `editorial_notes`: per-event Haiku draft, 2-3 sentences of institutional framing.")
    lines.append("  - `tags`: 4-6 per event, mix of thematic/attribute/entity, anchored on authoritative year from close_at.")
    lines.append("  - `question`: Haiku rewrites raw platform prose into canonical 'Will X by DATE?' grammar when needed.")
    if stubs_remaining:
        lines.append("")
        lines.append(f"WARNING: {stubs_remaining} fields still contain the literal TO_BE_FILLED_BY_EDITOR stub. Fill manually.")
    return "\n".join(lines)


def write_specimen(spec_id, events, markets, marks, resolution_log):
    outdir = OUTPUT_DIR / spec_id
    outdir.mkdir(parents=True, exist_ok=True)

    stubs_remaining = sum(
        1 for obj in [*events, *markets]
        for v in obj.values()
        if v == EDITORIAL_STUB
    )
    ai_drafted = count_ai_drafted(events, markets)

    bundle = {
        "_meta": {
            "specimen_id":    spec_id,
            "generated_at":   RUN_AT,
            "schema_version": "v0.1.0",
            "event_count":    len(events),
            "market_count":   len(markets),
            "mark_count":     len(marks),
            "resolution_log_count":    len(resolution_log),
            "editor_stubs_remaining":  stubs_remaining,
            "ai_drafted_counts":       ai_drafted,
            "editorial_review_notes":  build_review_note(ai_drafted, stubs_remaining),
        },
        "events":         events,
        "markets":        markets,
        "marks":          marks,
        "resolution_log": resolution_log,
    }
    (outdir / "specimen.json").write_text(json.dumps(bundle, indent=2, default=str))
    total_ai = sum(ai_drafted.values())
    print(f"  → wrote {outdir / 'specimen.json'}")
    print(f"    events={len(events)}  markets={len(markets)}  marks={len(marks)}  stubs={stubs_remaining}  ai_drafted={total_ai}")


# -----------------------------------------------------------------
# Main
# -----------------------------------------------------------------

def main():
    llm_enabled = "--no-llm" not in sys.argv
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"ClearMarket Enhancement Script — run at {RUN_AT}")
    print(f"Raw:    {RAW_DIR}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"LLM enrichment: {'ON (Haiku 4.5)' if llm_enabled else 'OFF (--no-llm)'}\n")

    for spec in SPECIMENS:
        print(f"[{spec['id']}]  pattern={spec['pattern']}")

        if spec["pattern"] == "poly_per_market_event":
            poly_data = load_json(spec["sources"][0])
            events, markets, marks = build_poly_per_market_event(spec, poly_data)
        elif spec["pattern"] == "shared_event_cross_platform":
            events, markets, marks = build_fed_cross_platform(spec)
        elif spec["pattern"] == "kalshi_shared_event":
            events, markets, marks = build_kalshi_shared_event(spec)
        else:
            raise ValueError(f"unknown pattern: {spec['pattern']}")

        populate_derived(events, markets, marks)
        enrich_with_llm(events, markets, enabled=llm_enabled)
        # re-populate derived after LLM enrichment (editorial_notes might flow into current_primary_mark display, tags into venues_covered, etc. — defensive)
        populate_derived(events, markets, marks)
        write_specimen(spec["id"], events, markets, marks, resolution_log=[])
        print()

    # Summary
    print("=" * 60)
    print("Run complete.")
    print(f"CLOB fetches: {_clob_stats['fetches']} new, {_clob_stats['cache_hits']} cache hits, {_clob_stats['failures']} failures")
    # LLM stats per model
    PRICING = {
        LLM_MODEL_HAIKU:  {"in": 1.0,  "out": 5.0},
        LLM_MODEL_SONNET: {"in": 3.0,  "out": 15.0},
    }
    total_cost = 0.0
    for model, s in _llm_stats.items():
        tok_in, tok_out = s['input_tokens'], s['output_tokens']
        p = PRICING.get(model, {"in": 1.0, "out": 5.0})
        cost = (tok_in / 1_000_000) * p["in"] + (tok_out / 1_000_000) * p["out"]
        total_cost += cost
        short_name = model.split("-")[1]  # "haiku" or "sonnet"
        print(f"{short_name:7s}: {s['calls']:3d} new, {s['cache_hits']:3d} cache hits  "
              f"in={tok_in:,}  out={tok_out:,}  ≈${cost:.4f}")
    print(f"Total LLM cost: ${total_cost:.4f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
