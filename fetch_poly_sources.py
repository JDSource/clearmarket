#!/usr/bin/env python3
"""
Polymarket verified-source layer — deterministic URL extraction.

Regex extracts candidate URLs from the market description (the deterministic floor —
no model ever sees a URL it could invent). ALL candidates are kept and forwarded into
`resolution_source_list` (source-layer refactor 2026-07-03); collapsing the list to one
URL was the root cause of the menu-vs-committed-authority blindness. When there is
exactly one URL it doubles as the display citation; when there are several, the
per-event commitment judgment (enhance.llm_source_commitment) selects the controlling
one BY NUMBER among these candidates — the old standalone select-primary LLM call is
retired (one semantic source judgment, not two).

Also catches bare-domain citations ("as posted on tesla.com", "per nato.int") — 87
markets in the 2026-06-12 universe cite a source with no scheme and were invisible to
the scheme-required regex.

Output: poly-sources.json  { event_key -> {source_url, source, verified, candidates, method} }

Usage:
  python3 fetch_poly_sources.py --sample 30
  python3 fetch_poly_sources.py            # full (no LLM involved; free)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

UNIV   = Path.home() / "jeremy-os/raw/clearmarket-universe-2026-06-12"
URL_RE = re.compile(r'https?://[^\s\)\]\}"\'<>]+')

# Bare domains cited without a scheme. Tight TLD list to avoid prose false-positives;
# candidates are verbatim-gated + LLM-judged downstream, so a rare stray is inert.
_BARE_TLDS = "com|org|gov|net|edu|io|int|mil|fr|uk|de|br|ca|us|eu|ch|jp|au"
BARE_RE = re.compile(
    # trailing lookahead: block a word char ("tesla.community") and ".word" (mid-domain),
    # but ALLOW a sentence-ending period ("posted on tesla.com. Announcements…")
    r'(?<![/\w@.])((?:www\.)?[A-Za-z0-9][A-Za-z0-9-]*(?:\.[A-Za-z0-9-]+)*'
    r'\.(?:' + _BARE_TLDS + r'))(/[^\s\)\]\}"\'<>]*)?(?!\w)(?!\.\w)'
)
_VENUE_HOSTS = ("polymarket.com", "kalshi.com", "kalshi.co")


_TRAIL_PUNCT = '.,;:\'"!?*`“”‘’…'   # incl. typographic quotes, markdown *, ellipsis


def clean_url(u: str) -> str:
    """Strip trailing punctuation, but keep a closing ')' that has a matching '(' inside
    the URL (bcb.gov.br ...(Copom) class — the old rstrip ate the balanced paren)."""
    while u:
        if u[-1] in _TRAIL_PUNCT or u[-1] in ']}':
            u = u[:-1]
        elif u[-1] == ')' and u.count('(') < u.count(')'):
            u = u[:-1]
        else:
            break
    return u


def extract_urls(text: str) -> list[str]:
    text = text or ""
    out: list[str] = []
    for m in URL_RE.finditer(text):
        u, end = m.group(0), m.end()
        # the char class stops at ')': if the URL has an unclosed '(' and the next char
        # is ')', that ')' belongs to the URL (query params with parenthesised values)
        while end < len(text) and text[end] == ')' and u.count('(') > u.count(')'):
            u += ')'
            end += 1
        out.append(clean_url(u))
    # covered-check by HOST, case-insensitive — a bare "Tesla.com" mention must be suppressed
    # when https://tesla.com/x was already captured, and a distinct registry (tesla.com.br)
    # must NOT be suppressed just because its string appears inside another URL's path.
    def _host(u: str) -> str:
        h = re.sub(r'^https?://', '', u, flags=re.I).split('/')[0].lower()
        return h[4:] if h.startswith('www.') else h
    covered_hosts = {_host(u) for u in out}
    for m in BARE_RE.finditer(text):
        dom = clean_url(m.group(0))
        host = _host(dom)
        if any(host == v or host.endswith('.' + v) for v in _VENUE_HOSTS):
            continue
        if host in covered_hosts:  # same host already captured via a scheme-ful URL
            continue
        out.append(dom)
        covered_hosts.add(host)
    return list(dict.fromkeys(out))


def resolve_source(desc: str) -> dict:
    urls = extract_urls(desc)
    if not urls:
        # NOTE: no URL != no source — prose-named authorities ("per CME Group's daily
        # settlement price") are surfaced by the commitment judgment downstream.
        return {"source_url": None, "source": "subjective_or_none", "verified": False,
                "candidates": [], "method": "no_url"}
    if len(urls) == 1:
        return {"source_url": urls[0], "source": "polymarket_description", "verified": True,
                "candidates": urls, "method": "single_url_deterministic"}
    # multiple candidates: keep them ALL; the commitment call selects the controlling one
    return {"source_url": None, "source": "polymarket_description", "verified": False,
            "candidates": urls, "method": "multi_url_commitment_selects"}


def rep_description(ev: dict) -> str:
    mkts = ev.get("markets") or []
    if not mkts:
        return ev.get("description") or ""
    rep = max(mkts, key=lambda m: float(m.get("volume") or 0))
    return rep.get("description") or ev.get("description") or ""


def main() -> None:
    sample = int(sys.argv[sys.argv.index("--sample") + 1]) if "--sample" in sys.argv else None
    evs = json.loads((UNIV / "poly-institutional.json").read_text())
    todo = evs[:sample] if sample else evs

    out, methods = {}, {}
    for i, ev in enumerate(todo, 1):
        key = str(ev.get("id") or ev.get("slug"))
        r = resolve_source(rep_description(ev))
        out[key] = r
        methods[r["method"]] = methods.get(r["method"], 0) + 1
        if i % 200 == 0:
            print(f"  {i}/{len(todo)}", flush=True)

    (UNIV / "poly-sources.json").write_text(json.dumps(out, indent=2))
    n = len(todo)
    print(f"\nwrote poly-sources.json ({n} events)")
    print("methods:")
    for k, v in sorted(methods.items(), key=lambda x: -x[1]):
        print(f"   {k:28}: {v:>4} ({100*v/n:.0f}%)")


if __name__ == "__main__":
    main()
