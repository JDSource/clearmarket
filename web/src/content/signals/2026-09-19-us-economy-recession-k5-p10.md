---
signal_id: "CMSIG20260919DV04"
signal_slug: "us-economy-recession-k5-p10"
headline: "Recession in 2026: Kalshi 5% vs Polymarket 10%"
semantic_title: "2026 recession odds back the higher read on the deeper book"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-19T07:48:36+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.1
  volume_cumulative_usd: 1972151.4149169999
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.05
bullets:
  - "Kalshi prices a 2026 U.S. recession at 5%, Polymarket at 10%, a 5pp gap, with Polymarket the higher venue."
  - "Polymarket dominates on volume at nearly $2M cumulative vs Kalshi's $177K, roughly 11x deeper."
  - "Here the more liquid venue holds the higher price, inverting the usual thin-market premium pattern and giving Polymarket's 10% stronger credibility."
  - "Resolves YES on a formally designated or widely recognized U.S. recession occurring within calendar year 2026."
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
      kalshi_vol_24h_usd: 103.04
      poly_vol_24h_usd: 2056.828687
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-09-19T07:48:36+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This is the only divergence in the batch where the deeper-liquidity venue is also the higher-priced one, that alignment makes Polymarket's 10% the more reliable signal, and Kalshi's 5% the outlier a desk should investigate before fading.
