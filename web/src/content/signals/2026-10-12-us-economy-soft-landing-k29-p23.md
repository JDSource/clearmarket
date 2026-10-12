---
signal_id: "CMSIG20261012DV00"
signal_slug: "us-economy-soft-landing-k29-p23"
headline: "State of economy end-2026 (recession read): Kalshi 29% vs Polymarket 23%"
semantic_title: "Economy-at-year-end outlook carries a premium across venues"
telemetry: "Polymarket 23% vs Kalshi 29%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-12T17:18:52+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.23
  volume_cumulative_usd: 48203.800012
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.294
bullets:
  - "Kalshi prices the negative/recession outcome at 29%; Polymarket sits at 23%, a 6pp gap."
  - "Kalshi is higher on thin volume; Polymarket holds the lower read with roughly 5.6× more cumulative liquidity."
  - "Thinner Kalshi book may reflect a smaller, more pessimistic user base; deep Polymarket volume gives that 23% more weight."
  - "Resolution hinges on how Kalshi's economic-state rubric defines 'end of 2026', ambiguity in the scoring criteria may explain part of the spread."
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
      kalshi_vol_24h_usd: 19.71
      poly_vol_24h_usd: 828.498483
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-12T17:18:52+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap, wide relative to Polymarket's deep book, suggests a desk should treat the Polymarket 23% as the better-anchored price and view Kalshi as carrying an illiquidity premium on the bearish side.
