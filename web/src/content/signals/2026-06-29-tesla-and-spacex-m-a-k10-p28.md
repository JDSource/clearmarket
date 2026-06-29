---
signal_id: "CMSIG20260629DV00"
signal_slug: "tesla-and-spacex-m-a-k10-p28"
headline: "Tesla/SpaceX binding merger before Oct 2026: Kalshi 10% vs Polymarket 28%"
semantic_title: "Tesla-SpaceX merger stance splits sharply across venues"
telemetry: "Polymarket 28% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-29T12:30:10+00:00"
event_id: "CM-EVT-J2MX96G9X1"
event_slug: "kxcompanyactionmerger-27"
event_question: "Will Tesla or SpaceX announce a definitive, binding agreement for Tesla to acquire SpaceX, SpaceX to acquire Tesla, or the two entities to merge or combine in any structure that results in a transfer of controlling interest or consolidation of the two entities under common corporate ownership before Oct 1, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9e7056c4004056441b57f960460c5e4f6d3e6ab9e1633b15538eb909d0f34466"
  question_raw: "Tesla and SpaceX merger officially announced by September 30?"
  current_price: 0.28
  volume_cumulative_usd: 44307.759073000016
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXCOMPANYACTIONMERGER-27-26OCT01"
    question_raw: "Will Tesla or SpaceX announce a definitive, binding agreement for Tesla to acquire SpaceX, SpaceX to acquire Tesla, or the two entities to merge or combine in any structure that results in a transfer of controlling interest or consolidation of the two entities under common corporate ownership before Oct 1, 2026?"
    current_price: 0.1
bullets:
  - "Polymarket prices the merger at 28%, Kalshi at 10%, an 18pp gap on a sub-90-day horizon."
  - "Polymarket is the higher-conviction side with substantially deeper liquidity; Kalshi volume is thin."
  - "Kalshi's tighter resolution wording ('definitive, binding agreement') may be driving its lower price vs Polymarket's crowd interpretation."
  - "Resolution requires a publicly confirmed binding corporate agreement before Oct 1, 2026, a high legal bar."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-948B650775); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 5.0
      poly_vol_24h_usd: 1281.703597
sources:
  - label: "ClearMarket cross-venue record: Will Tesla or SpaceX announce a definitive, binding agreemen"
    url: "https://clearmarket.fyi/compare/tesla-and-spacex-mna-m-2026-09"
    retrieved_at: "2026-06-29T12:30:10+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 18pp spread on a claim expiring in under 90 days signals a meaningful contract-wording or crowd-composition gap between venues, not just noise, a desk should check resolution criteria before treating either price as reliable.
