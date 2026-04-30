# CFTC ANPRM data pull — findings

**Pulled:** April 27, 2026 18:29 UTC
**Sources:** Polymarket Gamma API (events with nested markets), Kalshi public events API (`with_nested_markets=true`)
**Sample sizes:** 37,382 active Polymarket markets across 4,000 events ($6.0B cumulative volume); 10,165 active Kalshi markets across 1,600 events (593M contracts)

---

## Headline finding

The categories most relevant to the CFTC's public-interest determination framework — **politics, geopolitics, culture, and technology / AI** — are precisely the categories with the weakest documented resolution sources on both venues. The pattern is consistent across the regulated (Kalshi) and unregulated (Polymarket) perimeter.

| | Polymarket | Kalshi |
|---|---|---|
| Markets sampled | 37,382 | 10,165 |
| Cumulative volume | $6.0B (USDC) | 594M contracts (~$594M nominal) |
| Markets with a populated `resolutionSource` URL field | 25.1% | 0.0% (Kalshi does not use URLs in rules text) |
| Markets naming an authoritative source (URL or named entity) | 25.1% | 12.6% |
| **Volume-weighted** rate of populated source | **1.8%** | **15.2%** |
| Markets containing placeholder language ("consensus of credible reporting" or similar) | 64.1% | 3.7% |

The single sharpest data point: **on Polymarket, the volume-weighted rate of populated resolution-source URLs (1.8%) is one-fourteenth the market-count rate (25.1%)**. The highest-volume markets are systematically the ones with the worst disclosure. Kalshi inverts this — its volume-weighted rate is higher than its market-count rate (15.2% vs 12.6%), meaning higher-volume Kalshi markets do better. But both venues are weak at the count level on the categories CFTC asked about.

## Polymarket — segmented

Active markets only; `closed=false`. Total volume in millions USDC. "URL populated" = the platform's `resolutionSource` field contains an `http(s)://` URL. "Placeholder" = the market description contains language like "consensus of credible reporting" or "primary source."

| Category | n markets | Volume ($M) | URL populated | Placeholder language | Volume-weighted URL |
|---|---:|---:|---:|---:|---:|
| Politics | 15,220 | 3,320 | **2.6%** | 71.7% | 0.5% |
| Sports | 12,548 | 1,510 | 46.1% | 83.1% | 1.6% |
| Macro | 2,630 | 617 | 39.1% | 29.2% | 8.3% |
| Crypto | 1,861 | 207 | 2.3% | 14.2% | 0.2% |
| Culture | 1,933 | 147 | **0.8%** | 51.2% | 0.5% |
| Weather/Science | 1,719 | 21 | 82.0% | 3.0% | 17.4% |
| Tech/AI | 1,063 | 61 | **0.0%** | 22.2% | 0.0% |
| Geopolitics | 175 | 46 | **0.0%** | 77.7% | 0.0% |
| Other | 233 | 84 | 15.9% | 68.2% | 9.6% |

Notes:
- **Politics is the largest category by a wide margin** (15,220 markets, $3.32B — 55% of total Polymarket volume).
- **Sports markets often link to a sports-data URL** (e.g., atptour.com, espn.com), but the description language is itself placeholder ("based on official statistics") — explaining why both `URL populated = 46%` and `Placeholder = 83%` are high in the same segment.
- **Weather/Science is the only segment with strong source disclosure** (82% URL populated). These markets reference NWS/NOAA feeds and tend to have small dollar exposure.

## Kalshi — segmented

Active markets only. "Named source" = rules text contains a recognized authoritative source by name (BLS, Fed, S&P, Reuters, AP, NFL, CoinGecko, etc.). "Short" = rules under 200 characters. "Placeholder" = same patterns as Polymarket.

| Category | n markets | Volume (contracts) | Named source | Placeholder | VW named source | Short rules |
|---|---:|---:|---:|---:|---:|---:|
| Politics | 3,609 | 379M | **1.9%** | 7.8% | 8.3% | 34.2% |
| Sports | 2,706 | 40M | 21.8% | 0.0% | 13.4% | 66.1% |
| Culture | 2,142 | 32M | **0.7%** | 3.1% | 0.0% | 50.8% |
| Macro | 1,368 | 67M | 39.3% | 0.1% | 28.0% | 31.1% |
| Crypto | 125 | 53M | 52.0% | 0.0% | 65.9% | 0.8% |
| Tech/AI | 124 | 22M | **0.0%** | 0.0% | 0.0% | 63.7% |
| Geopolitics | 45 | 0.6M | **0.0%** | 68.9% | 0.0% | 31.1% |
| Weather/Science | 45 | 1.5M | 0.0% | 0.0% | 0.0% | 93.3% |
| Other | 1 | 0.005M | 0.0% | 0.0% | 0.0% | 100.0% |

Notes:
- **Kalshi politics markets (3,609) name an authoritative source in only 1.9% of cases.** This is the largest single category and it is essentially undocumented. Kalshi resolves these by exchange staff judgment without committing to a named source ex ante.
- **Crypto markets are the cleanest segment on either venue:** 52% name a source by name (CoinGecko, CMC, CF Benchmarks), 65.9% volume-weighted. Crypto pricing is structurally unambiguous and the market makers know their reference data must be specific.
- **Sports rules are short and source-skeletal** (66% under 200 characters, 22% name a source). Kalshi appears to rely on widely-known unambiguous game outcomes rather than written source citations.
- **Geopolitics — though tiny in count (45 markets) — is 69% placeholder language and 0% named source.** Same gap as Polymarket.

## Side-by-side comparison

The categories matter for the CFTC ANPRM because they map directly onto the "public-interest" activities listed in CEA section 5c(c)(5)(C) and the Commission's questions in II.B-E.

| Category | Poly URL% | Kalshi src% | Both ≥30%? | CFTC public-interest relevance |
|---|---:|---:|:---:|---|
| Politics | 2.6% | 1.9% | No | Q15-22, Q29-32 (election manipulation, federal-employee inside info) |
| Geopolitics | 0.0% | 0.0% | No | Q17-18 (terrorism, war) |
| Culture | 0.8% | 0.7% | No | Q19 (gaming — entertainment, awards, contests) |
| Tech/AI | 0.0% | 0.0% | No | Q15-22, Q33 (novel contract types) |
| **Sports** | 46.1% | 21.8% | No | Q19.b (sports vs gaming) |
| **Macro** | 39.1% | 39.3% | **Yes** | Q33 (swaps), Q5.a (SDR reporting) |
| **Crypto** | 2.3% | 52.0% | No | Q2.h (blockchain markets) |
| **Weather/Science** | 82.0% | 0.0% | No | n/a (low CFTC priority) |

The takeaway: where CFTC's regulatory framework is most concerned (politics, geopolitics, culture-as-gaming, novel tech contracts), **both** venues run essentially zero documented resolution sources. Where venues do well, the underlying data is structurally unambiguous (BLS releases, exchange-traded crypto pricing) and would not require regulatory intervention to clean up. The gap is the regulated sphere.

## What this changes vs. the README's prior 92% claim

The earlier ClearMarket README cited a survey of 746 "institutional-category" Polymarket markets where ~92% used placeholder language. That number was directionally right but lost the segmentation. The corrected picture:

- **The 92% headline understated the gap on the categories that matter.** Politics, geopolitics, culture, and tech/AI on Polymarket all run **0-3% URL populated**.
- **Sports and weather/science were inflating the previous "good" tail.** Excluding them, the Polymarket count rate drops materially.
- **The volume-weighted gap is the cleanest single number.** 25% by market vs 1.8% by volume on Polymarket — disclosure is worst where stakes are highest.

## Methodology limits

- Both venues are sampled, not exhaustive. Polymarket has thousands of low-volume markets in long-tail categories (sports props, micro-caps) that can shift category-level percentages.
- Polymarket's `resolutionSource` is a structured field; Kalshi's resolution information lives in `rules_primary` / `rules_secondary` free text. The two are not directly comparable as fields. The comparison framework is "does an external auditor know the named source ex ante?" — both URL-in-field and named-source-in-prose count as "yes."
- The "named source" detection on Kalshi uses a curated regex list of authoritative sources (BLS, Fed, S&P, Reuters, AP, league names, etc.). It will have false negatives where a less common but legitimate source is named.
- "Placeholder language" detection is conservative; some markets that *look* well-sourced may still contain placeholder phrasing because they hedge their named source.
- Volume-weighted rates use Polymarket's reported `volume` (cumulative USDC) and Kalshi's `volume_fp` (cumulative contract count). These are not directly comparable across venues but are comparable within each venue.

## Output files

- `polymarket-events-raw.json` — raw 4,000-event payload from Polymarket Gamma API
- `polymarket-summary.json` — segmented analysis
- `kalshi-events-raw.json` — raw 1,600-event payload from Kalshi public API
- `kalshi-summary-v2.json` — segmented analysis (v2 = corrected category mapping)
- `combined-summary.json` — earlier combined output (Kalshi piece in this file is the broken v1 — use v2 for Kalshi)

Reproducibility scripts at `scripts/cftc_data_pull.py` (Polymarket) and `scripts/cftc_kalshi_repull.py` (Kalshi).
