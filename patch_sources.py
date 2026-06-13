"""
Build-time SOURCE-COMMITMENT pass (CM DATA layer). v2.

The enrichment stores a venue's hedged/placeholder resolution language as if it were a
committed source ("For example, Google Finance" -> shown as the source, graded A), and leaves
the source NAME null for many Polymarket markets whose committed source is named only in prose
(Treasury, Rent Guidelines Board). Both are display + grade defects, NOT outcome-data defects.

Classifies every market's SOURCE COMMITMENT deterministically (no LLM, no re-enrich):
  named        - a concrete authority is committed to (named in field or recovered from prose,
                 a URL the venue itself names, or a deep-link official citation). No cap.
  uncommitted  - a source is gestured at but hedged ("for example" = illustrative -> B ceiling)
                 or pure placeholder ("consensus of credible reporting" = names nothing -> C ceiling)
  none         - no source named at all -> C ceiling

v2 fixes (2026-06-11, after the AAA gas-market false positive):
  - IDEMPOTENT: the candidate name is resolution_source OR source_hedge_text, so re-running
    on an already-patched bundle reclassifies from the original string instead of degrading
    to "none" (removes the build-data.sh re-run hazard).
  - URL-IN-NAME: a URL stored in the source field is a commitment to that URL (CME Group
    metals page, truthsocial.com/@realDonaldTrump) -> named, host shown as the source.
  - CITATION CORROBORATION: a single-token name whose own citation host contains the token
    ("AAA" + gasprices.aaa.com, "OpenAI" + openai.com) is a real org, not filler -> named.
  - GRADE RECOMPUTE: grade = band(rcg_score) re-capped by the surviving ceilings, so a
    market wrongly capped by a source false-positive recovers its earned grade. Source-cap
    reasons in rcg_caps are rebuilt from the new classification each run; factor caps
    (multi_source_no_conflict_rule, adversarial_ground_truth, ...) are preserved untouched.

Conservative by design: hedges stay hedges ("For example, Google Finance" remains
uncommitted_illustrative); genuine templates ("<polling organization>") remain placeholders.

Usage:  python3 patch_sources.py            # DRY RUN - report only, writes nothing
        python3 patch_sources.py --write     # back up bundle, patch in place, write report
"""
import json, re, sys, shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"
BACKUP = ROOT / "web/data/universe-enriched-linked.pre-sources-bak.json"
WRITE = "--write" in sys.argv

# ---- detectors -------------------------------------------------------------
# A hedge MARKER attached to a candidate => illustrative, non-committal.
HEDGE = re.compile(r"\bfor example\b|\be\.g\.|\bsuch as\b", re.I)
# Pure placeholder that names no concrete authority.
PLACEHOLDER = re.compile(
    r"consensus of (a )?credible|credible (public )?reporting|credible sources|"
    r"\ba consensus of\b|<[a-z_ ]+>|or equivalent|or similar", re.I)
# A concrete institutional authority named as definitive (no hedge on it).
AUTHORITY = re.compile(
    r"(rent guidelines board|department of the treasury|u\.?s\.? treasury|"
    r"bureau of labor statistics|federal reserve|securities and exchange commission|"
    r"\bBLS\b|\bSEC\b|\bFOMC\b|coingecko|cf benchmarks|"
    r"[a-z]+ secretary of state|board of elections|associated press|reuters|"
    r"official .{0,30}(board|department|bureau|agency|commission|authority))", re.I)
# Official / electoral citation domains => committed, even if prose hedges.
OFFICIAL_HOST = re.compile(
    r"\.gov$|\.gov/|\.gob\.|\.go\.kr|\.gouv\.|congress\.gov|un\.org|"
    r"electoral|\bnec\b|\bonpe\b|treasury\.gov|federalreserve\.gov|bls\.gov", re.I)
# Known real sources that show up as a single bare token => committed, not a placeholder.
KNOWN_TOKEN_AUTH = re.compile(
    r"^(reuters|bloomberg|ap|associated|abc|nbc|cbs|cnn|espn|bbc|politico|axios|"
    r"forbes|cnbc|coingecko|coinmarketcap|nasdaq|nyse|binance|coinbase|kraken|"
    r"fiscal\.ai|tradingview|fanduel|draftkings|opensecrets|ballotpedia)\b", re.I)
URL_RE = re.compile(r"^https?://\S+$", re.I)

RANK = {"A": 0, "B": 1, "C": 2}
UNRANK = {0: "A", 1: "B", 2: "C"}
# Source-commitment ceilings (this script's caps — rebuilt every run).
CAP = {"uncommitted_illustrative": "B", "uncommitted_placeholder": "C", "none": "C"}
SOURCE_CAPS = set(CAP)
# Factor-cap ceilings (classify.py's caps — preserved, never rebuilt here).
FACTOR_CAP_CEILING = {
    "multi_source_no_conflict_rule": "C",
    "discretionary_trigger_no_source": "C",
    "permissionless_oracle_discretionary_trigger": "C",
    "adversarial_ground_truth": "B",
}


def _band(score):
    # mirrors classify._rcg_band
    if not isinstance(score, (int, float)):
        return None
    return "A" if score >= 80 else "B" if score >= 55 else "C"


def _deeplink(u):
    if not u:
        return False
    if "polymarket.com" in u or "kalshi.com" in u:
        return False
    m = re.match(r"https?://[^/]+(/.*)?$", u)
    p = m.group(1) if m else None
    return bool(p and p not in ("/", ""))


def _host(u):
    return re.sub(r"^https?://(www\.)?", "", u or "").split("/")[0].lower()


def _tidy(s):
    return re.sub(r"\s+", " ", s).strip().title()


def classify(m):
    """-> (commitment, subtype, recovered_name_or_None, hedge_text_or_None)."""
    # Idempotence: a previous run nulls resolution_source for uncommitted rows and
    # preserves the original string in source_hedge_text — classify from either.
    name = (m.get("resolution_source") or m.get("source_hedge_text") or "").strip()
    cite = m.get("source_citation")
    rules = m.get("resolution_rules_raw") or ""

    # 0. Unfilled template token ("<geography>", "<polling organization>") -> placeholder.
    #    Audit 2026-06-12: 383 markets served a literal angle-bracket template as a
    #    "named" source and were graded A off it.
    if name and re.search(r"<[^>]{1,40}>", name):
        return "uncommitted", "uncommitted_placeholder", None, name
    # 1. Stored "source" is itself a hedge marker -> illustrative
    if name and HEDGE.search(name):
        return "uncommitted", "uncommitted_illustrative", None, name
    # 2. Stored "source" is a pure placeholder (names nothing) -> placeholder
    if name and PLACEHOLDER.search(name) and not AUTHORITY.search(name):
        return "uncommitted", "uncommitted_placeholder", None, name
    # 2b. Stored "source" is itself a URL -> the venue committed to that URL
    if name and URL_RE.match(name):
        return "named", "named", _host(name), None
    # 3. Clean multi-token stored name -> committed (keep as-is)
    if name and len(name.split()) > 1:
        return "named", "named", name, None
    # 3b. Single bare token that is a KNOWN real source -> committed
    if name and KNOWN_TOKEN_AUTH.match(name):
        return "named", "named", name, None
    # 3c. Single token corroborated by its own citation host ("AAA" + gasprices.aaa.com,
    #     "OpenAI" + openai.com) -> a real org the venue cited, not filler
    if name and cite and re.search(r"[a-z]", name, re.I):
        host = _host(cite)
        if name.lower() in host.replace("-", "").replace("_", ""):
            return "named", "named", name, None

    # ---- name empty or single-token truncation ("NYC"): read prose + citation ----
    auth = AUTHORITY.search(rules)
    placeholder_in_prose = PLACEHOLDER.search(rules)
    hedge_in_prose = HEDGE.search(rules)

    # 4. Prose names a definitive authority -> committed (Treasury / RGB / NYC-RGB)
    if auth:
        disp = _tidy(auth.group(0))
        if placeholder_in_prose:
            disp += " (consensus fallback)"
        return "named", "named", disp, None
    # 5. Deep-link to an official/electoral domain -> committed (recover host as name)
    if cite and _deeplink(cite) and OFFICIAL_HOST.search(cite):
        return "named", "named", _host(cite), None
    # 6. Prose hedges a candidate -> illustrative
    if hedge_in_prose:
        return "uncommitted", "uncommitted_illustrative", None, None
    # 7. Pure placeholder, no authority -> placeholder
    if placeholder_in_prose:
        return "uncommitted", "uncommitted_placeholder", None, None
    # 8. A real non-venue deep-link but no parseable name -> committed, name pending re-enrich
    if cite and _deeplink(cite):
        return "named", "named", _host(cite), None
    # 9. Single-token truncation we couldn't expand, no corroborating cite -> placeholder
    if name:
        return "uncommitted", "uncommitted_placeholder", None, name
    return "none", "none", None, None


def regrade(m, subtype):
    """Grade = band(rcg_score), re-capped by surviving factor caps + the new source cap.
    Returns (new_grade, new_caps). Falls back to the current grade when no score exists."""
    old_grade = m.get("resolution_clarity_grade")
    factor_caps = [c for c in (m.get("rcg_caps") or []) if c not in SOURCE_CAPS]
    source_cap = CAP.get(subtype)
    new_caps = factor_caps + ([subtype] if source_cap else [])

    base = _band(m.get("rcg_score"))
    if base is None:
        # no stored score: can only cap down from the current grade, never raise
        if old_grade in RANK and source_cap:
            return UNRANK[max(RANK[old_grade], RANK[source_cap])], new_caps
        return old_grade, new_caps

    ceilings = [FACTOR_CAP_CEILING.get(c) for c in factor_caps]
    ceilings = [c for c in ceilings if c] + ([source_cap] if source_cap else [])
    rank = max([RANK[base]] + [RANK[c] for c in ceilings])
    return UNRANK[rank], new_caps


def main():
    d = json.loads(BUNDLE.read_text())
    mkts = d["markets"]

    before_grade = Counter()
    after_grade = Counter()
    sub_ct = Counter()
    flips_down = flips_up = 0
    names_recovered = 0
    upgraded_to_named = Counter()
    by_venue = {"kalshi": [Counter(), Counter()], "polymarket": [Counter(), Counter()]}

    for m in mkts:
        old_subtype = m.get("source_commitment_subtype")
        commitment, subtype, recovered, hedge = classify(m)
        old_grade = m.get("resolution_clarity_grade")
        new_grade, new_caps = regrade(m, subtype)

        before_grade[old_grade] += 1
        after_grade[new_grade] += 1
        sub_ct[subtype] += 1
        v = by_venue.get(m["platform"])
        if v:
            v[0][old_grade] += 1
            v[1][new_grade] += 1
        if old_grade in RANK and new_grade in RANK:
            if RANK[new_grade] > RANK[old_grade]:
                flips_down += 1
            elif RANK[new_grade] < RANK[old_grade]:
                flips_up += 1
        if commitment == "named" and old_subtype in SOURCE_CAPS:
            upgraded_to_named[(recovered or "?")[:40]] += 1
        had_name = bool((m.get("resolution_source") or "").strip())
        if recovered and not had_name:
            names_recovered += 1

        if WRITE:
            m["source_commitment"] = commitment
            m["source_commitment_subtype"] = subtype
            m["source_hedge_text"] = hedge
            if commitment == "named":
                if recovered:
                    m["resolution_source"] = recovered
            else:
                # uncommitted/none: never show the hedge as a source
                m["resolution_source"] = None
            m["resolution_clarity_grade"] = new_grade
            m["rcg_caps"] = new_caps

    n = len(mkts)

    def pct(c, k, tot):
        return f"{c.get(k,0):6d} ({100*c.get(k,0)//tot:2d}%)"

    print(f"\n{'='*78}\nSOURCE-COMMITMENT PATCH v2 — {'WRITE' if WRITE else 'DRY RUN'} — {n} markets\n{'='*78}")
    print("\nCommitment subtypes:")
    for s, c in sub_ct.most_common():
        print(f"   {s:28s} {c:6d}")
    print(f"\nNames recovered from prose/citation (were null): {names_recovered}")
    print(f"Grade flips: {flips_down} capped down, {flips_up} recovered up")
    if upgraded_to_named:
        print("\nReclassified placeholder/illustrative -> named (top 15):")
        for name, c in upgraded_to_named.most_common(15):
            print(f"   {c:5d}  {name}")
    print(f"\n{'grade':8} {'BEFORE':>14} {'AFTER':>14}")
    for g in ["A", "B", "C", "pending"]:
        print(f"{g:8} {pct(before_grade,g,n):>14} {pct(after_grade,g,n):>14}")
    print("\nPer venue (A+B share):")
    for v, (b, a) in by_venue.items():
        tot = sum(b.values()) or 1
        ab_b = b.get("A", 0) + b.get("B", 0)
        ab_a = a.get("A", 0) + a.get("B", 0)
        print(f"   {v:11s} A+B  {100*ab_b//tot:2d}%  ->  {100*ab_a//tot:2d}%   (C {100*a.get('C',0)//tot:2d}%)")

    if WRITE:
        if not BACKUP.exists():
            shutil.copy(BUNDLE, BACKUP)
            print(f"\nbacked up -> {BACKUP.name}")
        BUNDLE.write_text(json.dumps(d))
        print(f"patched bundle written -> {BUNDLE.name}")
    else:
        print("\n(dry run — nothing written. re-run with --write to patch the bundle.)")


if __name__ == "__main__":
    main()
