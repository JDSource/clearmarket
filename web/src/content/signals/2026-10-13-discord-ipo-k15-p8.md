---
signal_id: "CMSIG20261013DV01"
signal_slug: "discord-ipo-k15-p8"
headline: "Discord IPO before 2027: Kalshi 15% vs Polymarket 8%"
semantic_title: "Discord IPO odds split across venues heading into year-end"
telemetry: "Polymarket 8% vs Kalshi 15%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-13T15:33:55+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.082
  volume_cumulative_usd: 490666.33244799986
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.15
bullets:
  - "Kalshi sits at 15% and Polymarket at 8%, a 7pp gap on the same pre-2027 IPO claim."
  - "Kalshi is the higher-priced venue; Polymarket holds dominant liquidity at $490K+ vs Kalshi's $20K."
  - "The gap likely reflects audience differences and limited arbitrage incentive given Kalshi's small pool, not a genuine edge on IPO timing."
  - "Resolution requires a confirmed Discord public listing on a major exchange before January 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-26DA00133D); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 36.26
      poly_vol_24h_usd: 12.195122
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-13T15:33:55+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 7pp spread where one side holds 24x the liquidity points to structural fragmentation rather than informed disagreement, a desk tracking Discord IPO risk should anchor to Polymarket's 8% and monitor Kalshi only for a sudden volume surge.
