---
signal_id: "CMSIG20260918DV02"
signal_slug: "us-economy-recession-k4-p10"
headline: "US recession in 2026: Kalshi 4% vs Polymarket 10%, 6pp gap"
semantic_title: "US 2026 recession odds trade far apart on the major prediction desks"
telemetry: "Polymarket 10% vs Kalshi 4%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-18T12:40:20+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.1
  volume_cumulative_usd: 1970094.58623
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.04
bullets:
  - "Kalshi prices a 2026 US recession at 4%; Polymarket at 10%, a 6pp spread."
  - "Polymarket is the higher side and holds the much deeper book by a wide margin."
  - "Kalshi's lower price may reflect stricter resolution criteria or a narrower participant base on this contract."
  - "Resolution typically hinges on an official NBER recession declaration covering calendar year 2026."
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
      kalshi_vol_24h_usd: 991.72
      poly_vol_24h_usd: 8287.162223
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-09-18T12:40:20+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The direction of the gap is notable, Polymarket's deeper, higher-volume book prices recession risk 2.5x higher than Kalshi, suggesting the two contracts may differ in resolution definition, and a desk should reconcile the rulebooks before taking a cross-venue position.
