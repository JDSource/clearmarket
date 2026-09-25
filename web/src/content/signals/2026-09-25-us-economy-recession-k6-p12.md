---
signal_id: "CMSIG20260925DV02"
signal_slug: "us-economy-recession-k6-p12"
headline: "US recession in 2026: Kalshi 6% vs Polymarket 12%"
semantic_title: "2026 recession call splits across venues with Polymarket twice as high"
telemetry: "Polymarket 12% vs Kalshi 6%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-25T07:48:58+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.12
  volume_cumulative_usd: 2128444.6025940003
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.06
bullets:
  - "Kalshi prices recession at 6% vs Polymarket at 12%, a 6pp gap, with Polymarket double the level"
  - "Polymarket holds the dominant book; Kalshi's volume is roughly one-tenth the size"
  - "Kalshi's lower print may reflect a stricter resolution standard or different user base expectations on defining 'recession'"
  - "Resolution likely hinges on an official NBER declaration or two consecutive negative GDP quarters before year-end 2026"
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-2FB03D51D4); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 287.5
      poly_vol_24h_usd: 61680.627436999996
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-09-25T07:48:58+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The definition of 'recession' is the most likely wedge here, if the two contracts resolve on different criteria, the spread is structural rather than a tradeable arb, and a desk should confirm resolution language on each venue before acting.
