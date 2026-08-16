---
signal_id: "CMSIG20260816DV02"
signal_slug: "us-economy-soft-landing-k59-p53"
headline: "State of economy end-2026 (positive): Kalshi 59% vs Polymarket 53%"
semantic_title: "Economy-condition odds diverge across venues heading into year-end"
telemetry: "Polymarket 53% vs Kalshi 59%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-16T08:24:18+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.53
  volume_cumulative_usd: 30768.274219
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.591
bullets:
  - "Kalshi prices 59%, Polymarket 53%, a 6pp gap on the same economic-state outcome"
  - "Kalshi is the higher venue; Polymarket has 2.4x more liquidity ($30,768 vs $12,644)"
  - "Outcome definition ambiguity, what counts as a 'good' economy, may be driving venue-specific interpretation differences"
  - "Resolution likely tied to a specific GDP, unemployment, or composite index reading at year-end 2026"
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-08-16T08:24:18+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp gap where the lower-liquidity venue prices more optimistically suggests Kalshi participants may be applying a narrower or more favorable resolution reading, worth monitoring as resolution criteria clarify.
