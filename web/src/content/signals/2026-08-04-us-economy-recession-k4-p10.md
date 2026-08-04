---
signal_id: "CMSIG20260804DV02"
signal_slug: "us-economy-recession-k4-p10"
headline: "U.S. recession in 2026: Kalshi 4% vs Polymarket 10%"
semantic_title: "Recession-in-2026 pricing diverges on the major prediction desks"
telemetry: "Polymarket 10% vs Kalshi 4%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-08-04T10:34:23+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.1
  volume_cumulative_usd: 1693903.2256180001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.04
bullets:
  - "Kalshi prices 4%, Polymarket 10%, a 6pp gap; both venues price this as a low-probability outcome."
  - "Polymarket is higher and holds the dominant liquidity position by a wide margin."
  - "Kalshi's 4% may reflect a stricter official-recession definition; Polymarket's 10% could use a broader or market-implied threshold."
  - "Resolves YES on a recognized U.S. recession call within calendar year 2026."
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
      kalshi_vol_24h_usd: 1450.25
      poly_vol_24h_usd: 3447.485375
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-08-04T10:34:23+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Even though both venues agree the probability is low, the 6pp gap at the bottom of the range is meaningful in relative terms and almost certainly traces to differing resolution definitions, making contract-spec comparison essential before any arb attempt.
