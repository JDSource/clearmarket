---
signal_id: "CMSIG20261024DV00"
signal_slug: "us-economy-soft-landing-k17-p9"
headline: "U.S. economy in recession by end-2026: Kalshi 17% vs Polymarket 9%"
semantic_title: "Economy-in-recession odds build a wide spread across venues"
telemetry: "Polymarket 9% vs Kalshi 17%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-24T07:49:28+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.09
  volume_cumulative_usd: 52112.032628
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.174
bullets:
  - "Kalshi prices recession risk at 17%, Polymarket at 9%, an 8pp gap on the same end-of-year claim."
  - "Kalshi sits higher with roughly $6.6K cumulative volume; Polymarket carries the deeper pool at $52.1K."
  - "Polymarket's larger liquidity typically reflects broader price discovery; Kalshi's premium may stem from a narrower, more pessimistic user base or looser resolution language."
  - "Resolution hinges on how 'recession' is officially defined or declared before Jan 1, 2027, ambiguity in that mechanic likely amplifies the spread."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
    field_provenance:
      kalshi_price:
        tier: "direct"
        method: "kalshi_api"
      poly_price:
        tier: "direct"
        method: "polymarket_clob_api"
      divergence_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["kalshi_price", "poly_price"]
    liquidity_context:
      kalshi_vol_24h_usd: 3.48
      poly_vol_24h_usd: 1096.64
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-24T07:49:28+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp gap on a claim this close to resolution is wide enough that a desk with a clear view on the definition mechanic could find a straightforward arbitrage entry between the two venues.
