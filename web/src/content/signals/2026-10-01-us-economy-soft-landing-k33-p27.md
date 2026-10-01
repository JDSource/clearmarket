---
signal_id: "CMSIG20261001DV01"
signal_slug: "us-economy-soft-landing-k33-p27"
headline: "Economy rated 'good' end of 2026: Kalshi 33% vs Polymarket 27%"
semantic_title: "End-of-2026 economy outlook builds a gap across major desks"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-01T15:04:26+00:00"
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
  - "Kalshi prices a positive economy outcome at 33%, Polymarket at 27%, a 6pp spread heading into Q4 2026."
  - "Kalshi is the higher venue; Polymarket carries the larger book at roughly five times Kalshi's cumulative volume."
  - "Divergence likely reflects ambiguous resolution criteria, 'state of the economy' leaves room for interpretation, widening venue-to-venue disagreement."
  - "Resolution mechanic: outcome determined by a defined economic indicator or survey benchmark at year-end 2026."
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
    retrieved_at: "2026-10-01T15:04:26+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Soft resolution language on a macro claim is a known driver of cross-venue spreads, a desk should treat the 6pp gap as a signal to scrutinize the resolution rules before taking a position on either side.
