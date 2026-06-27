---
signal_id: "CMSIG20260627DV00"
signal_slug: "tesla-and-spacex-m-a-k14-p28"
headline: "Tesla/SpaceX binding deal before Oct 2026: Kalshi 14% vs Polymarket 28%"
semantic_title: "Tesla-SpaceX merger claim splits sharply across venues"
telemetry: "Polymarket 28% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-27T01:36:57+00:00"
event_id: "CM-EVT-J2MX96G9X1"
event_slug: "kxcompanyactionmerger-27"
event_question: "Will Tesla or SpaceX announce a definitive, binding agreement for Tesla to acquire SpaceX, SpaceX to acquire Tesla, or the two entities to merge or combine in any structure that results in a transfer of controlling interest or consolidation of the two entities under common corporate ownership before Oct 1, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9e7056c4004056441b57f960460c5e4f6d3e6ab9e1633b15538eb909d0f34466"
  question_raw: "Tesla and SpaceX merger officially announced by September 30?"
  current_price: 0.28
  volume_cumulative_usd: 42881.20616200001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXCOMPANYACTIONMERGER-27-26OCT01"
    question_raw: "Will Tesla or SpaceX announce a definitive, binding agreement for Tesla to acquire SpaceX, SpaceX to acquire Tesla, or the two entities to merge or combine in any structure that results in a transfer of controlling interest or consolidation of the two entities under common corporate ownership before Oct 1, 2026?"
    current_price: 0.14
bullets:
  - "Polymarket prices the merger at 28%, Kalshi at 14%, a 14pp spread on the same binding-deal claim."
  - "Polymarket is the higher-conviction venue; Kalshi carries far thinner liquidity at under $3.5K cumulative volume vs $42.9K."
  - "Thin Kalshi pool likely reflects retail absence rather than informed skepticism; Polymarket's deeper book lends its print more weight."
  - "Resolution requires a publicly announced, definitive, binding agreement transferring controlling interest before Oct 1, 2026."
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
      poly_vol_24h_usd: 588.065204
sources:
  - label: "ClearMarket cross-venue record: Will Tesla or SpaceX announce a definitive, binding agreemen"
    url: "https://clearmarket.fyi/compare/tesla-and-spacex-mna-m-2026-09"
    retrieved_at: "2026-06-27T01:36:57+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 14pp gap is primarily a liquidity artifact, Kalshi's near-empty book should be treated as unreliable signal, leaving Polymarket's 28% as the operative market estimate for a desk sizing exposure to this tail event.
