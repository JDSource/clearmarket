# ClearMarket — Methodology

How ClearMarket selects, sources, and grades prediction-market data. This document is the
source for the public `/methodology` page and the canonical internal record. Last updated
2026-05-26.

---

## 1. Universe & institutional filter

ClearMarket ingests the full Kalshi + Polymarket universe and filters to the institutionally
relevant set. As of the 2026-05-26 pull: **2,077 events / 17,585 markets** (Kalshi 942 / 6,999;
Polymarket 1,135 / 10,586) from ~16,000 raw events.

Three filter inputs:
1. **Category whitelist** — 9 institutional categories IN: `economics`, `financials`, `crypto`,
   `companies`, `technology`, `health`, `politics`, `geopolitics`, `climate`. OUT: `sports`,
   `entertainment`, `mentions`.
2. **Volume threshold** — venue-specific minimum (tuned empirically).
3. **Resolution horizon** — resolves within 24 months.

**Category derivation differs by venue.** Kalshi ships a clean category field → direct map.
Polymarket has no category field → derived from `tags[]`: a deterministic map keyed on top-level
tags (weighting Polymarket's `forceShow` flag), with a constrained LLM fallback for events whose
tags carry no category signal.

---

## 2. Verified-source layer

Every market's resolution source is captured from **platform-provided data**, never invented by a
model. The mechanism differs by venue.

### Kalshi — structured (direct)
The resolution source + URL live in a structured API field (`series.settlement_sources`). We read
it directly; no extraction. Coverage across 703 unique series:
- **98% authoritative** (Federal Reserve, BLS, BEA, NWS, Library of Congress, ICE, CF Benchmarks…)
- **2% loose** — a placeholder ("For example, Google Finance"), all in the equity-index family
- **0% missing**

### Polymarket — deterministic capture, gated judgment
The sources are embedded in the market description free-text. We capture them **without ever
letting a model mint an identifier**:
1. **Regex** extracts every candidate URL in the description — including bare-domain citations
   ("as posted on tesla.com") — and ALL candidates are kept in `resolution_source_list`
   (the deterministic floor; nothing is collapsed away).
2. **One per-event commitment judgment** (an LLM read of the full source list + rules prose,
   against the versioned rubric) surfaces authorities the venue names *in words* with no URL
   ("the official CME settlement price") and selects the controlling URL *by number among the
   extracted candidates*.
3. **Verbatim gate:** every identifier the judgment emits must appear in the venue's own text as
   a whole token (word-boundary match), or it is discarded; a "named" classification whose
   evidence does not survive the gate is demoted to uncommitted, never shipped uncapped.

**Zero hallucinated URLs remains structural:** URLs enter the dataset only via regex extraction,
and the judgment can only pick among them by index. Prose-surfaced names are tagged
`clearmarket_editorial`. Extraction-mix statistics will be republished with the first enrichment
under this pipeline.

### Provenance tiers
Every value carries its origin: **`direct`** (platform API / structured field / verbatim-extracted
URL), **`editorial`** (LLM-drafted interpretation, e.g. `underlying_reference`), **`subjective`**
(resolution by consensus, no named data source). The LLM is confined to the `editorial` tier; any
verifiable identifier (source name, URL) traces to platform data.

### Source commitment

Capturing a source is not the same as the venue *committing* to one. We classify every market's
resolution source on a **commitment axis**, because a hedge or a placeholder is not a definitive
source:

- **named** — a concrete, resolvable authority (Federal Reserve, BLS, the NYC Rent Guidelines Board,
  a deep-link `.gov` / official-electoral citation). No grade cap.
- **uncommitted** — a source is *gestured at* but not committed to. Two sub-cases:
  *illustrative* ("For example, Google Finance" — a candidate, not a commitment) and
  *placeholder* ("a consensus of credible reporting" — names no concrete authority).
- **none** — no source language at all.

The principle: **"for example" means the venue did not commit to a definitive source.** Source
commitment is a *separate axis* from outcome objectivity — an objective outcome resolved against an
uncommitted source still carries resolution risk, because *which* report decides is left unspecified.
This is the gap the CFTC comment documents: regulated venues commit to a named authority; unregulated
markets frequently do not. The commitment classification feeds a grade ceiling (see §3), and the
**venue's literal source field is shown verbatim** on each event page — including when it does not
match the resolution rules — so the reader judges the source in the venue's own words, not ours.

---

## 3. Resolution Clarity Grade (RCG) — v2

A per-**market** A/B/C grade of how unambiguously a market will resolve. (Per market, not per event:
one event can hold a Kalshi market that resolves clearly and a Polymarket market on the same question
that resolves subjectively.) The grade is a **weighted score (0–100) banded into A/B/C, then capped**
— not a single rule. It rolls seven factors grounded in the documented resolution failures (Hall's
a16z analysis + the CFTC ANPRM comment): the failures were not absent sources but specific structural
defects, so the grade scores those defects directly.

**Seven factors (weights sum to 100):**

| Factor | Weight | What it measures |
|---|---:|---|
| Trigger objectivity | 28 | Objective measurable trigger vs. discretionary criterion (the Zelensky-"suit" defect). Heaviest because it stays hard after venues clean up citations. |
| Contested reality | 22 | Whether the underlying fact is controlled or disputed by an interested party (Venezuela, Ukraine). Most saturation-resistant. |
| Source clarity | 18 | Authoritative named source + usable link. Necessary but commoditizes fastest. |
| Arbiter incentive | 12 | Dispute resolver's capture risk: regulated/automated vs. permissionless oracle (the UMA flip). |
| Source-conflict rule | 8 | If 2+ **genuinely competing** sources (independent authorities that could give contradictory answers) are named, is there an explicit precedence/fallback rule? A named *primary with an informal fallback* is **not** a conflict (Venezuela). *Situational — the only one.* |
| Temporal precision | 7 | Controlling timestamp vs. source-update lag (OPM shutdown). |
| Source mutability | 5 | Editable/tamperable source without a snapshot rule (Ukraine map, Météo-France sensor). |

**Scoring rules:**
- **Always-on** factors (trigger, contested, source clarity, arbiter, temporal, mutability — 92 of 100)
  score every market. The **one situational** factor (source-conflict rule) scores only when 2+ distinct
  sources are named and is **excluded from the denominator** otherwise (score re-normalized over applicable factors).
- Score = `100 × earned / applicable`, banded **A ≥ 80, B 55–79, C ≤ 54**.
- **Hard caps (ceilings, applied after banding):** **source uncommitted-illustrative → B; uncommitted-placeholder
  or none → C** (§2 — a hedge is not a committed source; the binding constraint on most unregulated markets);
  2+ *genuinely competing* sources with no precedence rule → C; discretionary trigger with no named source → C;
  permissionless oracle + discretionary trigger → C; **adversarial ground truth (contested reality) → B**.
  Caps only ever *lower* a grade, never raise it.
- The **applicable-factor count is surfaced with the grade** ("B — scored on 6 of 7 factors") for
  comparability across markets of different complexity.

Five LLM-judged factors — trigger objectivity, contested reality, source-conflict rule, temporal precision,
and source mutability — are scored in **one per-event call** (`enhance.llm_rcg_factors`). Source clarity is
hybrid: it reads the §2 verified-source layer (deterministic for Kalshi, gated-LLM for Polymarket). Only
arbiter incentive is purely deterministic (it reads the venue's arbitration model). Adding factors adds
tokens, not calls. The full weighted model, scoring rules, and caps are in `rcg-scoring-model.csv` (repo
root) — the canonical spec for this section.

The source-conflict rule was deterministic (URL-count + regex) through 2026-05-26; it moved to the LLM on
2026-05-27 because URL counting mis-read one source across multiple pages as "multiple sources" (false C)
and missed prose-named sources entirely (false `na`). It is now a reading-comprehension judgment.

**Validation:** the model reproduces the four documented failures as **C / C / B / C** (Venezuela,
Zelensky, OPM, Ukraine). Full-universe distribution is pending the per-event LLM rater's calibration
run against a sample of *ordinary* markets — four tail failures are not a calibration set.

The cross-venue resolution-governance contrast (objective, named-authority Kalshi markets vs. the
subjective-consensus share on Polymarket) is the signal the venues themselves do not surface.

---

## 4. Editorial enrichment

On top of the verified-source layer, ClearMarket adds editorial fields (`editorial_notes`,
`underlying_reference`, `tags`, canonical question) drafted by an LLM and tagged `editorial`. These
*interpret and gloss* the verified data — e.g. naming the authoritative publisher (S&P Dow Jones
Indices) where a venue cites only a placeholder (Google Finance) — but never serve as the source of
record. Enrichment is per-event (shared across a market's strike ladder), not per-strike.
