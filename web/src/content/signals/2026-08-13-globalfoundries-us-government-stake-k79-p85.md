---
signal_id: "CMSIG20260813DV03"
signal_slug: "globalfoundries-us-government-stake-k79-p85"
headline: "US gov stake in GlobalFoundries >0%: Kalshi 79% vs Polymarket 85%"
semantic_title: "GlobalFoundries stake odds build higher across venues"
telemetry: "Kalshi 79% vs Polymarket 85%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-13T09:09:18+00:00"
event_id: "CM-EVT-TDJHRGQTY1"
event_slug: "kxusacompanystake-27jan01"
event_question: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSACOMPANYSTAKE-27JAN01-GFS"
  question_raw: "Will any part of the United States federal government take a stake of above 0% in GlobalFoundries?"
  current_price: 0.79
  volume_cumulative_usd: 21774.56
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0x29de69eea09afcb0cde8301eca3e6fcabf826dcb8a8dafacc0d20f3404a735ff"
    question_raw: "Will the US federal government take a stake in GlobalFoundries Inc.?"
    current_price: 0.851
bullets:
  - "Polymarket prices a US government stake at 85%, Kalshi at 79%, a 6pp gap."
  - "Kalshi holds the higher liquidity here ($21.8K vs $5.9K), making this a rarer case where Kalshi is deeper."
  - "Polymarket's higher price on thinner volume may reflect resolution-criteria optimism or audience skew toward YES."
  - "Resolves YES if any federal entity acquires any equity stake above 0% in GlobalFoundries."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-64E6FFD2DB); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 6.32
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will any part of the United States federal government take a"
    url: "https://clearmarket.fyi/compare/globalfoundries-us-government-stake-y-2026"
    retrieved_at: "2026-08-13T09:09:18+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Both venues price this as a high-probability outcome; the 6pp gap is modest but notable given Kalshi's liquidity edge, a desk would treat 79, 85% as the credible range.
