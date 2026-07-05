#!/usr/bin/env python3
"""
Source-layer regression suite (spec: source-layer-refactor-spec-2026-07-02 §5 + §8).

Three tiers:
  1. Deterministic unit tests — extraction, verbatim gates, fail-closed, status purity,
     factor derivation. No API key needed; always run.
  2. LLM ground-truth tests — the frozen 12-case commitment fixture set
     (tests/fixtures/source-commitment-ground-truth.json). Needs ANTHROPIC_API_KEY
     (results content-cached by enhance.llm_call, so re-runs are free).
  3. Bundle invariants — verbatim-gate / display-honesty / consistency / coverage scans
     over an enriched bundle. Skipped unless CM_BUNDLE points at one.

Run:  python3 -m pytest tests/test_source_layer.py -v
      CM_BUNDLE=path/to/universe-enriched-*.json python3 -m pytest tests/test_source_layer.py -v
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import enhance as E
import enrich_universe as EU
from classify import grade_market, rate_source_clarity
from fetch_poly_sources import extract_urls, resolve_source

FIXTURES = Path(__file__).parent / "fixtures"
HAS_KEY = bool(os.getenv("ANTHROPIC_API_KEY"))


# ---------------------------------------------------------------------------
# 1a. URL extraction (deterministic floor)
# ---------------------------------------------------------------------------
def test_extract_scheme_urls_and_paren_paths():
    t = "per https://www.bcb.gov.br/en/about/bcb-calendar?categoria=Monetary%20Policy%20Committee%20(Copom) page."
    assert extract_urls(t) == [
        "https://www.bcb.gov.br/en/about/bcb-calendar?categoria=Monetary%20Policy%20Committee%20(Copom)"
    ]


def test_extract_bare_domains_incl_sentence_end():
    t = "resolves based on information posted on tesla.com. Announcements on nato.int also qualify."
    assert extract_urls(t) == ["tesla.com", "nato.int"]


def test_extract_no_prose_false_positives():
    t = "Resolves to Yes. If unclear at 4 p.m. ET, e.g. due to delays, it resolves No. See rules vs. the U.S. announcement."
    assert extract_urls(t) == []


def test_extract_excludes_venue_hosts_and_dedupes():
    t = "See https://example.com/data, and https://example.com/data again. Not polymarket.com though."
    assert extract_urls(t) == ["https://example.com/data"]


def test_resolve_source_methods():
    assert resolve_source("no urls here")["method"] == "no_url"
    one = resolve_source("see https://example.com/x")
    assert one["method"] == "single_url_deterministic" and one["source_url"]
    multi = resolve_source("see https://a.com/x and https://b.com/y")
    assert multi["method"] == "multi_url_commitment_selects"
    assert multi["source_url"] is None and len(multi["candidates"]) == 2


# ---------------------------------------------------------------------------
# 1b. Verbatim gates — the LLM judges, it can never mint an identifier
# ---------------------------------------------------------------------------
MARKET_WITH_LIST = {
    "question_raw": "Will X happen?",
    "resolution_rules_raw": "Resolves per the Bureau of Labor Statistics release. See https://bls.gov/cpi.",
    "resolution_source_list": [
        {"name": None, "url": "https://bls.gov/cpi", "provenance": "platform_api"},
        {"name": "Reuters", "url": None, "provenance": "platform_api"},
    ],
}


def _mock_llm(monkeypatch, payload: dict):
    monkeypatch.setattr(E, "llm_call", lambda *a, **k: json.dumps(payload))


def test_gate_invented_source_of_record_nulled_and_demoted(monkeypatch):
    _mock_llm(monkeypatch, {"commitment": "named", "source_of_record": "Federal Reserve",
                            "mechanism": "single_authority", "primary_source_number": 1,
                            "prose_sources": [], "why": "x"})
    out = E.llm_source_commitment(dict(MARKET_WITH_LIST))
    assert out["source_of_record"] is None          # "Federal Reserve" appears nowhere in venue text
    # and a named claim with no gate-surviving evidence fails closed — no uncapped grade
    # rides on a hallucinated authority
    assert out["commitment"] == "uncommitted_placeholder"


def test_gate_paraphrased_prose_sources_dropped(monkeypatch):
    _mock_llm(monkeypatch, {"commitment": "named", "source_of_record": "Bureau of Labor Statistics",
                            "mechanism": "single_authority", "primary_source_number": 1,
                            "prose_sources": ["Bureau of Labor Statistics", "the US labor bureau"],
                            "why": "x"})
    out = E.llm_source_commitment(dict(MARKET_WITH_LIST))
    assert out["source_of_record"] == "Bureau of Labor Statistics"   # verbatim substring: kept
    assert out["prose_sources"] == ["Bureau of Labor Statistics"]    # paraphrase: dropped


def test_gate_primary_number_out_of_range(monkeypatch):
    _mock_llm(monkeypatch, {"commitment": "named", "source_of_record": None, "mechanism": None,
                            "primary_source_number": 9, "prose_sources": [], "why": "x"})
    assert E.llm_source_commitment(dict(MARKET_WITH_LIST))["primary_url"] is None


def test_gate_primary_number_valid_picks_url(monkeypatch):
    _mock_llm(monkeypatch, {"commitment": "named", "source_of_record": None, "mechanism": None,
                            "primary_source_number": 1, "prose_sources": [], "why": "x"})
    assert E.llm_source_commitment(dict(MARKET_WITH_LIST))["primary_url"] == "https://bls.gov/cpi"


def test_gate_word_boundary_blocks_minted_acronyms(monkeypatch):
    """Swarm-confirmed bypass (2026-07-03): 'SEC' must not pass via 'second/consecutive',
    'Fed' via 'federal'. The gate is a word-boundary match, not a substring check."""
    mkt = {"question_raw": "Will X happen?", "resolution_source_list": None,
           "resolution_rules_raw": "Resolves on the second consecutive monthly federal report."}
    _mock_llm(monkeypatch, {"commitment": "named", "source_of_record": "SEC",
                            "mechanism": "single_authority", "primary_source_number": 0,
                            "prose_sources": ["Fed", "SEC"], "why": "x"})
    out = E.llm_source_commitment(mkt)
    assert out["source_of_record"] is None
    assert out["prose_sources"] == []
    # and with no surviving evidence, the named claim itself fails closed
    assert out["commitment"] == "uncommitted_placeholder"


def test_gate_secondhand_claim_without_evidence_demoted(monkeypatch):
    """committed_secondhand rests entirely on 'one concrete checkable source' — if the verbatim
    gate nulls the source name, the claim fails closed to placeholder like a named claim would."""
    _mock_llm(monkeypatch, {"commitment": "committed_secondhand", "source_of_record": "Fiscal.ai",
                            "mechanism": None, "primary_source_number": 0,
                            "prose_sources": [], "why": "x"})
    out = E.llm_source_commitment(dict(MARKET_WITH_LIST))   # "Fiscal.ai" appears nowhere in venue text
    assert out["source_of_record"] is None
    assert out["commitment"] == "uncommitted_placeholder"


def test_gate_secondhand_verbatim_source_survives(monkeypatch):
    mkt = {"question_raw": "Will Tesla Inc. report Above 1.5 million total deliveries in 2026?",
           "resolution_rules_raw": "If Tesla Inc. reports Above 1500000.0 total deliveries in 2026, then the market resolves to Yes.",
           "resolution_source_list": None,
           "resolution_source": "Fiscal.ai", "source_citation": "https://fiscal.ai"}
    _mock_llm(monkeypatch, {"commitment": "committed_secondhand", "source_of_record": "Fiscal.ai",
                            "mechanism": None, "primary_source_number": 1,
                            "prose_sources": [], "authorities_in_list": [], "why": "x"})
    out = E.llm_source_commitment(mkt)
    assert out["commitment"] == "committed_secondhand"
    assert out["source_of_record"] == "Fiscal.ai"


def test_gate_invalid_class_returns_none(monkeypatch):
    _mock_llm(monkeypatch, {"commitment": "sort_of_named", "source_of_record": None,
                            "prose_sources": [], "why": "x"})
    assert E.llm_source_commitment(dict(MARKET_WITH_LIST)) is None


def test_deterministic_none_makes_no_llm_call(monkeypatch):
    def boom(*a, **k):
        raise AssertionError("LLM must not be called for empty market")
    monkeypatch.setattr(E, "llm_call", boom)
    out = E.llm_source_commitment({"question_raw": "?", "resolution_rules_raw": "",
                                   "resolution_source_list": None})
    assert out["commitment"] == "none"
    assert out["rubric_version"] == E.SOURCE_RUBRIC_VERSION


def test_prose_only_market_is_read_not_shortcircuited(monkeypatch):
    """The B2 fix: no structured sources but rules text present -> the LLM reads it."""
    called = {}
    def fake(*a, **k):
        called["yes"] = True
        return json.dumps({"commitment": "named", "source_of_record": "CME",
                           "mechanism": "single_authority", "primary_source_number": 0,
                           "prose_sources": ["CME"], "why": "x"})
    monkeypatch.setattr(E, "llm_call", fake)
    out = E.llm_source_commitment({"question_raw": "?", "resolution_source_list": None,
                                   "resolution_rules_raw": "Resolves per the official CME settlement price."})
    assert called.get("yes") and out["commitment"] == "named"
    assert out["source_of_record"] == "CME" and out["prose_sources"] == ["CME"]


# ---------------------------------------------------------------------------
# 1c. Fail-closed + source_status purity (enrich_event)
# ---------------------------------------------------------------------------
RATINGS = {"trigger_objectivity": {"rating": "pass", "why": ""},
           "contested_reality": {"rating": "pass", "why": ""},
           "source_conflict": {"rating": "na", "why": ""},
           "temporal_precision": {"rating": "pass", "why": ""},
           "source_mutability": {"rating": "pass", "why": ""}}


def _enrich_with(monkeypatch, commitment_result, raises=False):
    ev = {"event_id": "CM-EVT-TEST", "primary_market_id": "CM-MKT-TEST", "bundle_type": "singleton",
          "question": "Test?", "category": "economics", "field_provenance": {}}
    mk = {"market_id": "CM-MKT-TEST", "platform": "kalshi", "question_raw": "Test?",
          "resolution_rules_raw": "Some rules.", "arbitration_model": "kalshi_staff",
          "resolution_source": "Somebody", "source_citation": "https://x.gov/data",
          "resolution_source_list": [{"name": "Somebody", "url": "https://x.gov/data",
                                      "provenance": "platform_api"}]}
    monkeypatch.setattr(E, "llm_underlying_reference", lambda *a, **k: "ref")
    monkeypatch.setattr(E, "llm_editorial_notes", lambda *a, **k: "notes")
    monkeypatch.setattr(E, "llm_tags", lambda *a, **k: [])
    monkeypatch.setattr(E, "llm_canonical_question", lambda *a, **k: None)
    monkeypatch.setattr(E, "llm_rcg_factors", lambda *a, **k: RATINGS)
    if raises:
        def boom(*a, **k):
            raise RuntimeError("api down")
        monkeypatch.setattr(E, "llm_source_commitment", boom)
    else:
        monkeypatch.setattr(E, "llm_source_commitment", lambda *a, **k: commitment_result)
    EU.enrich_event(ev, [mk], enabled=True)
    return mk


def test_fail_closed_on_none(monkeypatch):
    mk = _enrich_with(monkeypatch, None)
    assert mk["source_commitment_subtype"] == "uncommitted_placeholder"
    assert mk["source_status"] == "no_committed_source"
    assert mk["field_provenance"]["source_commitment"]["fail_closed"] is True
    assert mk["resolution_clarity_grade"] == "C"     # capped, never uncapped


def test_fail_closed_on_exception(monkeypatch):
    mk = _enrich_with(monkeypatch, None, raises=True)
    assert mk["source_commitment_subtype"] == "uncommitted_placeholder"
    assert mk["resolution_clarity_grade"] == "C"


@pytest.mark.parametrize("subtype,expected_status,expected_grade", [
    ("named", "platform_named", "A"),
    # ruled 2026-07-04: a real commitment (status stays platform_named — the source table
    # tells the truth) but capped C for authority quality (the Fiscal.ai class)
    ("committed_secondhand", "platform_named", "C"),
    ("uncommitted_illustrative", "no_committed_source", "B"),
    ("uncommitted_placeholder", "no_committed_source", "C"),
    ("none", "no_source_stated", "C"),
])
def test_status_is_pure_function_of_commitment(monkeypatch, subtype, expected_status, expected_grade):
    committed = subtype in ("named", "committed_secondhand")
    sc = {"commitment": subtype, "source_of_record": "Somebody" if committed else None,
          "mechanism": "single_authority" if subtype == "named" else None,
          "primary_url": None, "prose_sources": [], "why": "t",
          "rubric_version": E.SOURCE_RUBRIC_VERSION}
    mk = _enrich_with(monkeypatch, sc)
    assert mk["source_status"] == expected_status
    assert mk["resolution_clarity_grade"] == expected_grade
    assert mk["rcg"]["commitment"]["rubric_version"] == E.SOURCE_RUBRIC_VERSION


def test_prose_sources_join_list_with_editorial_provenance(monkeypatch):
    sc = {"commitment": "named", "source_of_record": "Somebody", "mechanism": "single_authority",
          "primary_url": None, "prose_sources": ["The Registry"], "why": "t",
          "rubric_version": E.SOURCE_RUBRIC_VERSION}
    mk = _enrich_with(monkeypatch, sc)
    entries = mk["resolution_source_list"]
    added = [e for e in entries if e["provenance"] == "clearmarket_editorial"]
    assert added == [{"name": "The Registry", "url": None, "provenance": "clearmarket_editorial"}]


# ---------------------------------------------------------------------------
# 1d. rate_source_clarity derives from the stamped commitment
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("market,expected", [
    ({"source_commitment_subtype": "named", "source_citation": "https://bls.gov/cpi"}, "pass"),
    ({"source_commitment_subtype": "named", "source_citation": None}, "partial"),                  # prose authority, no link
    ({"source_commitment_subtype": "named", "source_citation": "https://kalshi.com"}, "partial"),  # venue homepage != citation
    ({"source_commitment_subtype": "committed_secondhand", "source_citation": "https://fiscal.ai"}, "partial"),  # named+checkable; cap carries the defect
    ({"source_commitment_subtype": "uncommitted_illustrative", "source_citation": "https://x.gov/d"}, "partial"),
    ({"source_commitment_subtype": "uncommitted_placeholder", "resolution_source": "A consensus of credible reporting", "source_citation": "https://x.gov/d"}, "fail"),
    ({"source_commitment_subtype": "none"}, "fail"),
])
def test_source_clarity_derivation(market, expected):
    assert rate_source_clarity(market) == expected


def test_source_clarity_legacy_path_without_stamp():
    # pre-commitment (build-time) markets fall back to presence heuristics; grade is pending anyway
    m = {"resolution_source": "Bureau of Labor Statistics", "source_citation": "https://bls.gov/cpi"}
    assert rate_source_clarity(m) == "pass"
    assert grade_market(m, "")["grade"] == "pending"


# ---------------------------------------------------------------------------
# 2. LLM ground truth — the frozen 12-case commitment set
# ---------------------------------------------------------------------------
GT = json.loads((FIXTURES / "source-commitment-ground-truth.json").read_text())["cases"]


@pytest.mark.skipif(not HAS_KEY, reason="ANTHROPIC_API_KEY not set")
@pytest.mark.parametrize("case", GT, ids=[c["id"] for c in GT])
def test_commitment_ground_truth(case):
    out = E.llm_source_commitment(case["market"])
    assert out is not None, f"{case['id']}: LLM judgment failed"
    exp = case["expect"]
    assert out["commitment"] in exp["commitment"], \
        f"{case['id']}: got {out['commitment']} (why: {out['why']}), expected {exp['commitment']}"
    if exp.get("source_of_record_contains"):
        assert out["source_of_record"] and exp["source_of_record_contains"].lower() in out["source_of_record"].lower(), \
            f"{case['id']}: source_of_record={out['source_of_record']!r}"
    if exp.get("mechanism"):
        assert out["mechanism"] in exp["mechanism"], \
            f"{case['id']}: mechanism={out['mechanism']!r}, expected {exp['mechanism']}"


# ---------------------------------------------------------------------------
# 3. Bundle invariants — run against an enriched bundle (CM_BUNDLE=path)
# ---------------------------------------------------------------------------
BUNDLE = os.getenv("CM_BUNDLE")


def _bundle_markets():
    b = json.loads(Path(BUNDLE).read_text())
    return b["markets"] if isinstance(b, dict) else b


@pytest.mark.skipif(not BUNDLE, reason="CM_BUNDLE not set")
def test_invariant_verbatim_gate_universe_wide():
    """Every non-null source_of_record traces to venue text or the source list — as a
    word-boundary token, not a bare substring ('SEC' must not count via 'second'). The
    predicate MUST stay stricter-or-equal to the gate in enhance.llm_source_commitment."""
    import re as _re
    bad = []
    for m in _bundle_markets():
        sor = (m.get("source_of_record") or "").strip()
        if not sor:
            continue
        hay = ((m.get("resolution_rules_raw") or "") + "\n" +
               json.dumps(m.get("resolution_source_list") or []))
        if not _re.search(r"(?<![A-Za-z0-9])" + _re.escape(sor) + r"(?![A-Za-z0-9])", hay, _re.I):
            bad.append((m["market_id"], sor))
    assert not bad, f"{len(bad)} invented source_of_record values: {bad[:5]}"


@pytest.mark.skipif(not BUNDLE, reason="CM_BUNDLE not set")
def test_invariant_display_honesty():
    """No uncommitted/none market carries source_status platform_named."""
    bad = [m["market_id"] for m in _bundle_markets()
           if m.get("source_commitment") in ("uncommitted", "none")
           and m.get("source_status") == "platform_named"]
    assert not bad, f"{len(bad)} uncommitted markets serving platform_named: {bad[:5]}"


@pytest.mark.skipif(not BUNDLE, reason="CM_BUNDLE not set")
def test_invariant_status_consistency():
    """source_status == pure function of source_commitment, every enriched market."""
    F = {"named": "platform_named", "none": "no_source_stated", "uncommitted": "no_committed_source"}
    bad = [(m["market_id"], m.get("source_commitment"), m.get("source_status"))
           for m in _bundle_markets()
           if m.get("source_commitment") and m.get("source_status") != F[m["source_commitment"]]]
    assert not bad, f"{len(bad)} status/commitment divergences: {bad[:5]}"


@pytest.mark.skipif(not BUNDLE, reason="CM_BUNDLE not set")
def test_invariant_coverage_lift():
    """Polymarket resolution_source_list coverage (was 0% pre-refactor). Reports, and
    requires the multi-URL menus at minimum."""
    poly = [m for m in _bundle_markets() if m.get("platform") == "polymarket"]
    if not poly:
        pytest.skip("no polymarket markets in bundle")
    with_list = sum(1 for m in poly if m.get("resolution_source_list"))
    print(f"\npoly source-list coverage: {with_list}/{len(poly)} ({100*with_list/len(poly):.0f}%)")
    assert with_list > 0, "Polymarket source lists still empty — the data fix did not land"
