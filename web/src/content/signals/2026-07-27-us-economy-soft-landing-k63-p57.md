---
signal_id: "CMSIG20260727DV01"
signal_slug: "us-economy-soft-landing-k63-p57"
headline: "Economy 'good/great' end-2026: Kalshi 64% vs Polymarket 58%"
semantic_title: "U.S. economy end-of-2026 outlook trades apart on the major desks"
telemetry: "Polymarket 58% vs Kalshi 64%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-27T11:16:57+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.58
  volume_cumulative_usd: 29466.300328000012
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.639
bullets:
  - "Kalshi prices a positive economy outcome at 64%, Polymarket at 58%, a 6pp gap"
  - "Kalshi is the higher venue; $12K cumulative volume vs $29K on Polymarket"
  - "Softer liquidity on Kalshi may reflect a narrower, more optimistic user base skewing the consensus"
  - "Resolves on prevailing economic-condition classification at end of calendar year 2026"
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
      kalshi_vol_24h_usd: 451.9
      poly_vol_24h_usd: 1241.367739
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-07-27T11:16:57+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6pp spread on a subjective macro claim is notable, differing resolution criteria interpretations across venues are the most likely driver, and a desk should audit both contracts' resolution rules before leaning on either price.
