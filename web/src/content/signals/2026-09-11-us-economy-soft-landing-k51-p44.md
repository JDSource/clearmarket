---
signal_id: "CMSIG20260911DV02"
signal_slug: "us-economy-soft-landing-k51-p44"
headline: "U.S. economy strong at end of 2026: Kalshi 51% vs Polymarket 44%"
semantic_title: "U.S. economy end-of-2026 outlook trades apart on the major desks"
telemetry: "Polymarket 44% vs Kalshi 51%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-11T12:33:49+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.44
  volume_cumulative_usd: 38712.52999499999
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.51
bullets:
  - "Kalshi sits at 51%, Polymarket at 44%, a 7pp gap near the key 50% threshold"
  - "Kalshi is the higher venue; Polymarket holds roughly 3x greater volume at $38.7K vs $12.3K"
  - "Resolution ambiguity is the likely driver: 'state of the economy' may map to different benchmarks across venues, pulling crowds apart"
  - "Resolution criteria and adjudication source differ by platform, adding structural noise to this particular claim"
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
      kalshi_vol_24h_usd: 182.12
      poly_vol_24h_usd: 40.0
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-11T12:33:49+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp gap straddling 50% is consequential, Kalshi implies a coin-flip leaning positive while Polymarket leans negative, and the definitional looseness of 'state of economy' means a desk should scrutinize each platform's resolution rules before treating either price as actionable.
