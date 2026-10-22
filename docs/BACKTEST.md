# Resolution Outcomes Study, Edition 1

**Does ClearMarket's Resolution Clarity Grade predict which prediction-market contracts end up in a settlement dispute?**

Data as of **2026-07-23**. Polymarket only (see "Why Polymarket" below). Every number on this page is reproduced by one command, with no API access and no key:

```bash
python3 scripts/backtest_stats.py data/backtest/dispute-labels-2026-07-23.csv
```

The dataset is committed at [`data/backtest/dispute-labels-2026-07-23.csv`](../data/backtest/dispute-labels-2026-07-23.csv): one row per matched, graded Polymarket market, with the grade assigned from the rules text, the market's full UMA resolution status trail, and its trading volume on the sweep date.

## Headline

Across **7,166** Polymarket contracts with a public dispute record, **52 of the 55** contracts that were formally challenged at resolution had been graded **C** (the lowest of three tiers) before they resolved. C-rated contracts were challenged at **1.59%**, about **20 times** the **0.08%** rate of A- and B-rated contracts combined.

| Grade | Challenged | Contracts | Rate | 95% CI (Wilson) |
|---|---|---|---|---|
| A | 3 | 2,587 | 0.12% | 0.04% to 0.34% |
| B | 0 | 1,302 | 0.00% | 0.00% to 0.29% |
| C | 52 | 3,277 | 1.59% | 1.21% to 2.07% |
| A + B | 3 | 3,889 | 0.08% | 0.03% to 0.23% |

Relative risk, C versus A+B: **20.6x**, 95% CI 6.4x to 65.8x. The interval is wide because the A+B numerator is three events; the separation is not in doubt, the multiple is approximate.

All three challenges to A-rated contracts **failed**: the challenged outcome was re-proposed and settled as originally proposed, against the named source (two silver settlement-price brackets, one Colombian election market). No A- or B-rated contract was overturned.

## The grade is computed from rules text only

The Resolution Clarity Grade is a weighted score over seven features of a contract's resolution rules (trigger objectivity, contested reality, source clarity, arbiter incentive, source conflict, temporal precision, source mutability), banded A/B/C, then capped by a short list of fatal defects (no source of record, conflicting sources with no tiebreak, subjective trigger, and so on). The full specification is on the [methodology page](https://clearmarket.fyi/methodology/). The grader never sees prices, volume, outcomes, or dispute history. The result is therefore a prediction made before resolution, tested against what happened after.

## Pre-registered dispute definition

Fixed before any counting, and encoded in [`scripts/fetch_dispute_labels.py`](../scripts/fetch_dispute_labels.py):

- **Challenged (tier 1, the headline):** the string `disputed` appears anywhere in the market's UMA resolution status trail. That is a formal on-chain challenge to a proposed outcome, whether or not it succeeds. Frivolous challenges are included and reported as-is.
- **Overturned (tier 2):** the final outcome differs from the first proposal. Not derivable from the Gamma API alone; left null in this edition. Do not infer it from tier 1.
- **Publicly contested (tier 3):** press, lawsuit, or regulator action. Hand-curated; Kalshi cases live only here. Not part of the rate above.

The target set in the spec before the first run was "C disputes at roughly four times the A rate." Edition 1 observed total separation (26 of 26 disputes graded C on the 2026-06-12 labels); this refresh observes 52 of 55.

## Is the grade just flagging big markets?

A dispute needs vague wording and enough money to make the fight worthwhile, so the grade could be volume in disguise. Comparing only within trading-volume quartiles (volume at the sweep date):

| Volume quartile | A | B | C |
|---|---|---|---|
| Lowest | 0 / 675 | 0 / 335 | 1 / 771 (0.13%) |
| Second | 0 / 546 | 0 / 484 | 0 / 751 (0.00%) |
| Third | 1 / 674 (0.15%) | 0 / 247 | 6 / 860 (0.70%) |
| Highest | 2 / 677 (0.30%) | 0 / 235 | 43 / 871 (4.94%) |

In the highest-volume quartile, 912 A- and B-rated contracts, as large and as watched as anything on the venue, were challenged at **0.22%** (95% CI 0.06% to 0.80%). C-rated contracts of the same size were challenged at **4.94%** (95% CI 3.69% to 6.58%). Money was present either way; the wording decided whether it turned into a fight. (The research page on clearmarket.fyi reports this control using bundle volumes rather than sweep-date volumes; cut points differ slightly, conclusions do not.)

## Where the disputes come from

By the venue's own resolution-source commitment, the input the grade caps on:

| Source commitment | Challenged | Contracts | Rate |
|---|---|---|---|
| Named source of record | 3 | 3,868 | 0.08% |
| Placeholder only ("a consensus of credible reporting") | 52 | 2,740 | 1.90% |
| Illustrative example only ("for example, Reuters") | 0 | 304 | 0.00% |
| Committed second-hand source | 0 | 210 | 0.00% |
| No source | 0 | 44 | 0.00% |

Every one of the 52 C-rated disputes was a contract whose rules named no source of record.

## Why Polymarket

Polymarket is the only venue with a complete, publicly auditable dispute record: every challenge is posted on-chain through UMA, whether it succeeds or fails. Kalshi publishes no dispute feed, so a Kalshi challenge rate cannot be independently computed by anyone, at any standard; its contested settlements reach the public record only through courts, regulators, and the press. The grade is applied identically to Kalshi contracts. The largest public Kalshi case to date, the February 2026 market on whether Iran's Supreme Leader would leave office (about $54M volume), settled at the last traded price under a death carve-out that appeared in the CFTC-filed terms but not on the trading page; Kalshi refunded about $2.2M and a class action followed. That is the failure mode this grade measures.

## Limits, stated plainly

- **Challenged, not overturned.** Tier 2 is null in this edition. The headline measures friction at settlement, not wrong payouts.
- **Grade-now, not grade-at-listing.** The grade is derived from rules text set at listing and is stable, but this edition uses the grade as stamped on 2026-07-23.
- **Rare events.** 55 disputes in 7,166 contracts. Levels are small; the separation between tiers is the result.
- **One venue.** See above.
- **Not a trading signal.** A C means the rules are unclear, not that the market is mispriced.

## Reproduce it

```bash
# 1. the committed dataset -> every table above
python3 scripts/backtest_stats.py data/backtest/dispute-labels-2026-07-23.csv

# 2. (optional) rebuild the dataset from the venue: fresh UMA sweep + join to the graded universe,
#    then export the flat CSV. Needs the enriched bundle (web/data/universe-enriched-linked.json).
python3 scripts/fetch_dispute_labels.py --sweep --join
python3 scripts/export_backtest_labels.py <date>
```

## Editions

| Edition | Labels date | Contracts | Challenged | A | B | C | C vs A+B |
|---|---|---|---|---|---|---|---|
| Private run | 2026-06-12 | 7,155 | 26 | 0 / 1,716 | 0 / 1,461 | 26 / 3,978 | separation (A+B = 0) |
| Refresh | 2026-07-05 | 7,253 | 54 | 3 / 2,590 | 0 / 1,299 | 51 / 3,364 | 19.7x |
| **Edition 1 (this page)** | **2026-07-23** | **7,166** | **55** | **3 / 2,587** | **0 / 1,302** | **52 / 3,277** | **20.6x** |

Next edition: re-run the sweep against the current universe (about 39,000 markets across both venues as of October 2026) and add tier 2 (overturned) from on-chain UMA history.
