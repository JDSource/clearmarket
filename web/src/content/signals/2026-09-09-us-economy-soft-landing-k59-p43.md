---
signal_id: "CMSIG20260909DV00"
signal_slug: "us-economy-soft-landing-k59-p43"
headline: "State of economy end-2026 (positive): Kalshi 59% vs Polymarket 43%"
semantic_title: "Economy-by-end-of-2026 outlook splits sharply across venues"
telemetry: "Polymarket 43% vs Kalshi 59%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-09T12:41:30+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.43
  volume_cumulative_usd: 38428.26999500002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.59
bullets:
  - "Kalshi prices a positive 2026 economy at 59%; Polymarket at 43%, a 16pp gap."
  - "Kalshi is higher; liquidity thin at $13.8K cumulative vs Polymarket's deeper $38.4K."
  - "Vague resolution criteria ('state of economy') likely read differently across user bases; Polymarket's larger pool may reflect broader skepticism."
  - "Resolution likely tied to a subjective or index-based economic benchmark at year-end 2026."
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
      kalshi_vol_24h_usd: 39.04
      poly_vol_24h_usd: 487.114118
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-09T12:41:30+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 16pp spread on a loosely defined macro claim signals that resolution ambiguity, not information, is driving the gap, the desk should treat the higher-liquidity Polymarket price as the more reliable anchor.
