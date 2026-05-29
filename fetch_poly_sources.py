#!/usr/bin/env python3
"""
Polymarket verified-source layer — hybrid extraction with a verbatim gate.

Regex extracts candidate URLs from the market description (the deterministic floor —
the LLM never sees a URL it could invent). If there's exactly one, it's used directly
(no LLM). If there are several, a cheap Haiku call SELECTS the primary among them, and a
verbatim gate REJECTS any URL not present in the description. The LLM can never mint or
mistype a URL; worst case it picks a real secondary URL (flagged for review).

Output: poly-sources.json  { event_key -> {source_url, source, verified, candidates, method} }

Usage:
  python3 fetch_poly_sources.py --no-llm   # free: just report URL-candidate distribution
  python3 fetch_poly_sources.py --sample 30
  python3 fetch_poly_sources.py            # full
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import enhance as E

UNIV   = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-05-27"
URL_RE = re.compile(r'https?://[^\s\)\]\}"\'<>]+')


def clean_url(u: str) -> str:
    return u.rstrip('.,;:)]}\'"')


def extract_urls(text: str) -> list[str]:
    return list(dict.fromkeys(clean_url(u) for u in URL_RE.findall(text or "")))


def select_primary(desc: str, candidates: list[str]) -> str | None:
    """Haiku picks the primary resolution-source URL by NUMBER among candidates."""
    system = (
        "You identify the PRIMARY resolution-source URL for a prediction market from its "
        "description. You are given the description and a numbered list of URLs found in it. "
        "Reply with ONLY the number of the URL that is the market's authoritative resolution "
        "source. If none qualifies, reply 0. Never output a URL or any other text — only a number."
    )
    lst = "\n".join(f"{i+1}. {u}" for i, u in enumerate(candidates))
    user = f"Description:\n{(desc or '')[:1500]}\n\nURLs:\n{lst}\n\nNumber:"
    raw = E.llm_call(user, system=system, max_tokens=5)
    m = re.search(r"\d+", raw or "")
    if not m:
        return None
    idx = int(m.group())
    return candidates[idx - 1] if 1 <= idx <= len(candidates) else None


def resolve_source(desc: str, enabled: bool) -> dict:
    urls = extract_urls(desc)
    if not urls:
        return {"source_url": None, "source": "subjective_or_none", "verified": False,
                "candidates": [], "method": "no_url"}
    if len(urls) == 1:
        return {"source_url": urls[0], "source": "polymarket_description", "verified": True,
                "candidates": urls, "method": "single_url_deterministic"}
    if not enabled:
        return {"source_url": None, "source": "polymarket_description", "verified": False,
                "candidates": urls, "method": "multi_url_needs_llm"}
    pick = select_primary(desc, urls)
    if pick and pick in urls and pick in (desc or ""):          # verbatim gate
        return {"source_url": pick, "source": "polymarket_description", "verified": True,
                "candidates": urls, "method": "llm_select_gated"}
    return {"source_url": urls[0], "source": "polymarket_description", "verified": True,
            "candidates": urls, "method": "fallback_first", "review": True}


def rep_description(ev: dict) -> str:
    mkts = ev.get("markets") or []
    if not mkts:
        return ev.get("description") or ""
    rep = max(mkts, key=lambda m: float(m.get("volume") or 0))
    return rep.get("description") or ev.get("description") or ""


def main() -> None:
    enabled = "--no-llm" not in sys.argv
    sample = int(sys.argv[sys.argv.index("--sample") + 1]) if "--sample" in sys.argv else None
    evs = json.loads((UNIV / "poly-institutional.json").read_text())
    todo = evs[:sample] if sample else evs

    out, methods = {}, {}
    for i, ev in enumerate(todo, 1):
        key = str(ev.get("id") or ev.get("slug"))
        r = resolve_source(rep_description(ev), enabled)
        out[key] = r
        methods[r["method"]] = methods.get(r["method"], 0) + 1
        if i % 25 == 0:
            print(f"  {i}/{len(todo)}", flush=True)

    (UNIV / "poly-sources.json").write_text(json.dumps(out, indent=2))
    n = len(todo)
    print(f"\nwrote poly-sources.json ({n} events)")
    print("methods:")
    for k, v in sorted(methods.items(), key=lambda x: -x[1]):
        print(f"   {k:26}: {v:>4} ({100*v/n:.0f}%)")


if __name__ == "__main__":
    main()
