---
signal_id: "CMSIG20260627DV00"
signal_slug: "tesla-and-spacex-m-a-k14-p28"
headline: "Tesla/SpaceX binding merger before Oct 2026: Kalshi 14% vs Polymarket 28%"
semantic_title: "Tesla-SpaceX merger claim splits sharply across venues"
telemetry: "Polymarket 28% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-27T10:03:41+00:00"
event_id: "CM-EVT-J2MX96G9X1"
event_slug: "kxcompanyactionmerger-27"
event_question: "Will Tesla or SpaceX announce a definitive, binding agreement for Tesla to acquire SpaceX, SpaceX to acquire Tesla, or the two entities to merge or combine in any structure that results in a transfer of controlling interest or consolidation of the two entities under common corporate ownership before Oct 1, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9e7056c4004056441b57f960460c5e4f6d3e6ab9e1633b15538eb909d0f34466"
  question_raw: "Tesla and SpaceX merger officially announced by September 30?"
  current_price: 0.28
  volume_cumulative_usd: 42986.20616200001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXCOMPANYACTIONMERGER-27-26OCT01"
    question_raw: "Will Tesla or SpaceX announce a definitive, binding agreement for Tesla to acquire SpaceX, SpaceX to acquire Tesla, or the two entities to merge or combine in any structure that results in a transfer of controlling interest or consolidation of the two entities under common corporate ownership before Oct 1, 2026?"
    current_price: 0.14
bullets:
  - "Polymarket prices the merger at 28%, Kalshi at 14%, a 14pp gap on the same claim."
  - "Polymarket is the higher-conviction side with cumulative volume dwarfing Kalshi's thin book."
  - "Kalshi's lower price likely reflects stricter reading of 'definitive, binding agreement' within a 3-month window; Polymarket crowd may be pricing Musk-consolidation speculation more loosely."
  - "Resolution requires a publicly announced, legally binding deal structure, a high bar that may anchor Kalshi traders lower."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 677.025204
sources:
  - label: "ClearMarket cross-venue record: Will Tesla or SpaceX announce a definitive, binding agreemen"
    url: "https://clearmarket.fyi/compare/tesla-and-spacex-mna-m-2026-09"
    retrieved_at: "2026-06-27T10:03:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 14pp spread on a binary with a hard legal resolution standard suggests audience composition and contract-reading discipline differ materially between the two venues, offering a potential arb for desks confident in the definitional threshold.
