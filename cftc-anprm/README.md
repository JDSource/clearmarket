# CFTC ANPRM data pull (RIN 3038-AF65)

Source data and analysis scripts referenced in Jeremy Dietz's comment letter on the CFTC's Advance Notice of Proposed Rulemaking on Prediction Markets (91 FR 12516, March 16, 2026).

**Data pulled:** April 27, 2026 18:29 UTC.

## Layout

```
cftc-anprm/
├── findings.md              — analysis writeup (cross-venue placeholder language, sample sizes, segmented results)
├── scripts/
│   ├── cftc_data_pull.py    — Polymarket Gamma API pull (events with nested markets) + analysis
│   └── cftc_kalshi_repull.py — Kalshi public API pull (events with nested markets) + analysis
└── data/
    ├── polymarket-summary.json  — segmented placeholder/source rates by category
    ├── kalshi-summary-v2.json   — segmented placeholder/source rates by category
    └── combined-summary.json    — combined output (Kalshi piece superseded by v2)
```

## Reproducing

Both scripts pull from public APIs and require no authentication. Run:

```bash
python3 scripts/cftc_data_pull.py
python3 scripts/cftc_kalshi_repull.py
```

Both write to `~/jeremy-os/outputs/clearmarket/cftc-data-pull/` by default. Adjust the `OUT` path at the top of each script to redirect.

The methodology — placeholder language regex patterns, named-source detection, category mapping, volume-weighted aggregation — lives inline in each script. Reviewers wanting to test alternative regex patterns or category mappings can edit those constants directly.

## Headline figures (April 27, 2026)

- 37,382 active Polymarket markets, $6.0B cumulative volume
- 10,165 active Kalshi markets, ~$594M cumulative contract volume
- Per-market and volume-weighted placeholder-language rates by category in `data/*.json`

See `findings.md` for the full segmented breakdown.
