#!/usr/bin/env python3
"""
lint_wire_voice.py — deterministic register lint for CM Signal wires.

Scans the reader-facing frontmatter fields (headline, semantic_title, bullets, interp)
of wire markdown files for banned vocabulary. The bar: a wire headline must read like
CNBC/terminal copy. Prompt-level bans have failed twice (2026-07-01, 2026-07-13 —
"Capital fades…"); this enforces the ban in CI, deterministically, before commit.

Usage:
  python3 lint_wire_voice.py <file.md> [...]        lint specific files
  python3 lint_wire_voice.py --staged               lint git-staged new/modified wires
  python3 lint_wire_voice.py --quarantine <files>   DELETE violating files instead of
                                                    failing (CI mode: a bad wire is
                                                    dropped, the rest of the run ships)

Exit 0 = clean (in --quarantine mode: always 0; violators removed + listed on stdout).
Exit 1 = violations found (non-quarantine mode).
"""
import re, sys, os, subprocess

# Banned in reader-facing copy. Tuple = (pattern, why). Keep patterns tight — every
# entry here was a real shipped violation or flagged by Jeremy; don't grow it casually.
BANNED = [
    # transitive "fade" with a market-actor subject — the one pattern shared by all 12
    # confirmed violations in the 2026-07-14 audit. Intransitive "fades to 3%" (price as
    # subject) is legitimate probability-decline language and must NOT match.
    (r"\b(capital|traders?|markets?|flows?|desks?|money)\s+fades?\b",
                                      "trader slang: market-actor fades X (2026-07-13/14)"),
    (r"\bdespite the live print\b",   "spot-vs-forward framing (banned 2026-07-01)"),
    (r"\balready (above|below)\b",    "spot-vs-forward framing (banned 2026-07-01)"),
    (r"\bclearing that bar\b",        "spot-vs-forward framing (banned 2026-07-01)"),
    # negation-aware: "reinforce rather than contradict" is legitimate — exempt "than contradict"
    (r"(?<!than )\bcontradict(s|ing|ion)?\b", "spot-vs-forward framing (banned 2026-07-01)"),
    # manufactured tension near a threshold comparison (confirmed live 2026-07-14)
    (r"\bdespite\b[^.\n]{0,50}\b(below|above|proximity to)\b",
                                      "despite-tension pattern near threshold (2026-07-14)"),
    # attribution: ClearMarket is the reference layer, never the venue that prices anything.
    # Shipped live 2026-07-18 ("The ClearMarket ladder prices Bitcoin…", headline "CM ladder 12%").
    (r"\b(CM|ClearMarket)\s+(ladder|price[sd]?|odds|probabilit\w*)\b",
                                      "attribution: ClearMarket is not a venue (2026-07-18)"),
    # '$' spelled out as the word 'dollar' next to a number — prompt ambiguity ("NO math
    # symbols" + "spell them out") shipped "dollar 100K" (07-18) and "100 to 150 dollar
    # range" (07-02). Digit-adjacent only: "dollar flow", "cents on the dollar", "digital
    # dollar", "firm dollar" are legitimate and must NOT match.
    (r"\bdollar\s+\d|\b\d[\d,.]*\s+dollar\b",
                                      "spelled-out '$' — write $100K (2026-07-18)"),
    # participant-type inference from anonymous flow — "institutional defense" shipped 2026-07-19
    # (Iowa Senate wire). Collocation-scoped: a market whose literal subject is an institution
    # ("institutional adoption of BTC ETFs") must not match.
    (r"\binstitutional\s+(defen[cs]e|conviction|bids?|buyers?|sellers?|flows?|capital|money|demand|support|accumulation)\b",
                                      "participant-type inference from anonymous flow (2026-07-19)"),
    (r"\bsmart money\b|\bwhales?\s+(buy|sell|bid|accumulate|defend|stack)\w*\b",
                                      "participant-type inference from anonymous flow (2026-07-19)"),
    # spelled-out large numbers — "above one and a half billion" shipped 2026-07-20 (crypto-hack
    # wire). '$1.5 billion' / '$1.5B' are fine; a spelled-out numeral before the unit is not.
    (r"\b(one|two|three|four|five|six|seven|eight|nine|ten|a)\s+(and\s+a\s+(half|quarter)\s+)?(thousand|million|billion|trillion)\b",
                                      "spelled-out numeral — write $1.5B (2026-07-20)"),
    # financial-poetry verbs flagged by Jeremy 2026-07-21 ("solidifies", "fractures below even
    # odds"). solidifies/crystallizes/calcifies have no legit reader-copy use; 'fractures' only
    # banned in the odds-collocation (a market about a coalition fracturing is a legit subject).
    (r"\b(solidif|crystalliz|calcif)\w*\b",
                                      "financial-poetry verb (2026-07-21)"),
    (r"\bfractures?\b[^.\n]{0,30}\bodds\b",
                                      "financial-poetry verb near odds (2026-07-21)"),
]
# NOT banned: "collapse" — audit 2026-07-14: ~15 false positives, ZERO true positives.
# Legitimate uses: the contract's literal subject (regime/ceasefire collapse) and
# probability-distribution shape ("tail collapses to 12%"). Left to the LLM prompt.

FIELD_RX = re.compile(
    r'^(?:headline|semantic_title|interp):\s*"?(.*?)"?\s*$|^  - "(.*)"$', re.M)

def reader_text(md_text):
    m = re.match(r"^---\n(.*?)\n---", md_text, re.S)
    if not m: return ""
    parts = []
    for a, b in FIELD_RX.findall(m.group(1)):
        parts.append(a or b)
    return " ".join(parts)

def lint(path):
    try:
        text = reader_text(open(path, encoding="utf-8").read())
    except OSError:
        return []
    hits = []
    for pat, why in BANNED:
        mt = re.search(pat, text, re.I)
        if mt: hits.append((mt.group(0), why))
    return hits

def staged_files():
    out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=AM"],
                         capture_output=True, text=True).stdout
    return [f for f in out.splitlines() if f.startswith("web/src/content/signals/") and f.endswith(".md")]

if __name__ == "__main__":
    args = sys.argv[1:]
    quarantine = "--quarantine" in args
    args = [a for a in args if a != "--quarantine"]
    files = staged_files() if args == ["--staged"] else args
    bad = 0
    for f in files:
        hits = lint(f)
        if not hits: continue
        bad += 1
        for word, why in hits:
            print(f"VOICE VIOLATION {f}: '{word}' — {why}")
        if quarantine and os.path.exists(f):
            os.remove(f)
            print(f"QUARANTINED (removed, will not publish): {f}")
    if bad and not quarantine:
        sys.exit(1)
    print(f"voice lint: {len(files)} file(s), {bad} violation(s)" + (" quarantined" if quarantine and bad else ""))
