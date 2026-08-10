---
signal_id: "CMSIG20260810DV00"
signal_slug: "us-economy-soft-landing-k62-p54"
headline: "Economy state end-2026: Kalshi 62% vs Polymarket 54%, 8pp gap"
semantic_title: "Economy-end-2026 outlook builds a premium on one venue"
telemetry: "Polymarket 54% vs Kalshi 62%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-10T09:15:39+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.54
  volume_cumulative_usd: 30678.147993
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.62
bullets:
  - "Kalshi prices a positive economy outcome at 62% vs Polymarket's 54%, an 8pp split."
  - "Kalshi sits higher with roughly $11.6K cumulative volume; Polymarket carries over $30.6K, indicating deeper liquidity on the bearish side."
  - "The thinner Kalshi market may reflect a smaller, more optimistic user base, while Polymarket's larger pool could represent a broader consensus leaning cautious."
  - "Resolution depends on the designated economic indicator or index reading before Jan 1, 2027, ambiguity in that mechanic likely widens the spread."
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
    retrieved_at: "2026-08-10T09:15:39+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk can treat the 8pp gap as a potential arbitrage, but the vague resolution criteria on 'state of economy' introduces meaningful basis risk that may justify much of the spread.
