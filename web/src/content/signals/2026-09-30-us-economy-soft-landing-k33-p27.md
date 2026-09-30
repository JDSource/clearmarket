---
signal_id: "CMSIG20260930DV00"
signal_slug: "us-economy-soft-landing-k33-p27"
headline: "U.S. economy in recession by end-2026: Kalshi 33% vs Polymarket 27%"
semantic_title: "2026 recession call prices higher on one major desk"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-30T14:34:12+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.27
  volume_cumulative_usd: 47038.800713000004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.33
bullets:
  - "Kalshi prices recession at 33%, Polymarket at 27%, a 6pp spread on the same claim"
  - "Kalshi is the higher-priced venue; Polymarket carries roughly five times the cumulative liquidity"
  - "Deeper Polymarket liquidity may reflect broader crowd input, making its lower read arguably more price-discovered"
  - "Resolution hinges on official recession definition, NBER call or GDP criteria ambiguity could explain venue disagreement"
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
      kalshi_vol_24h_usd: 16.38
      poly_vol_24h_usd: 63.81780700000001
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-30T14:34:12+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp gap with a 5-to-1 liquidity imbalance favoring Polymarket suggests the higher Kalshi price may reflect a thinner, less-tested market rather than genuine informational edge, a desk leaning on the claim should weight the deeper pool accordingly.
