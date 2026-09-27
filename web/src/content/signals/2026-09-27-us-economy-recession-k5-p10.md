---
signal_id: "CMSIG20260927DV02"
signal_slug: "us-economy-recession-k5-p10"
headline: "US recession in 2026: Kalshi 5% vs Polymarket 10%"
semantic_title: "Recession odds in 2026 run higher on the deeper-volume desk"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-27T13:31:46+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.1
  volume_cumulative_usd: 2225578.0264029996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.05
bullets:
  - "Polymarket prices a 2026 recession at 10%, Kalshi at 5%, a 5pp gap, with Polymarket higher."
  - "Polymarket is both the higher and the far more liquid venue, with volume more than 12x Kalshi's."
  - "Polymarket's premium may reflect more active macro-focused participants or a stricter, cleaner resolution source on Kalshi depressing its price."
  - "Resolution hinges on the specific recession definition each platform applies, differing criteria can mechanically produce different prices."
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
      kalshi_vol_24h_usd: 75.39
      poly_vol_24h_usd: 3303.486925
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-09-27T13:31:46+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Here the higher price sits on the more liquid venue, which is the reverse of a typical thin-market artifact, a desk should scrutinize each platform's resolution criteria before assuming the gap is pure arbitrage.
