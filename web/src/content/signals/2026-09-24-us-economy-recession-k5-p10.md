---
signal_id: "CMSIG20260924DV02"
signal_slug: "us-economy-recession-k5-p10"
headline: "U.S. recession in 2026: Kalshi 5% vs Polymarket 10%"
semantic_title: "U.S. recession call in 2026 trades far apart on the major desks"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-24T13:09:21+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.1
  volume_cumulative_usd: 2071076.6560339998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.05
bullets:
  - "Kalshi marks 2026 recession at 5%, Polymarket at 10%, a 5pp gap, with Polymarket twice as high."
  - "Polymarket sits higher and holds more than 11x Kalshi's cumulative volume, lending it greater price authority."
  - "Resolution-definition differences likely drive the gap; Kalshi's contract may use a stricter two-quarter GDP criterion vs. a broader Polymarket definition."
  - "Resolves on official NBER declaration or GDP data confirming contraction within calendar year 2026."
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
      kalshi_vol_24h_usd: 390.52
      poly_vol_24h_usd: 11999.835221
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-09-24T13:09:21+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The doubling of odds between venues on a macro claim with deep Polymarket liquidity points to a contract-definition divergence, a desk should scrutinize resolution rules before assuming either price reflects a purer recession probability.
