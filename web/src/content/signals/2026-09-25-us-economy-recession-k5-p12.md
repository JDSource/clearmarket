---
signal_id: "CMSIG20260925DV01"
signal_slug: "us-economy-recession-k5-p12"
headline: "US recession in 2026: Kalshi 5% vs Polymarket 12%"
semantic_title: "2026 recession odds carry a premium on the major prediction desks"
telemetry: "Polymarket 12% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-25T13:14:13+00:00"
event_id: "CM-EVT-L7017DJDX1"
event_slug: "kxrecssnber-26"
event_question: "Will there be a recession in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.12
  volume_cumulative_usd: 2132252.7726060003
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXRECSSNBER-26"
    question_raw: "Will there be a recession in 2026?"
    current_price: 0.05
bullets:
  - "Kalshi prices a 2026 recession at 5%, Polymarket at 12%, a 7pp spread with the year nearly complete."
  - "Polymarket sits higher at 12% with $2.13M in cumulative volume; Kalshi sits at 5% on $179K volume."
  - "Resolution-definition differences may explain part of the gap, recession triggers vary by adjudicator, making contract language the key credibility variable."
  - "Both contracts resolve on whether a recognized recession is declared or confirmed as occurring within calendar year 2026."
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
      kalshi_vol_24h_usd: 137.46
      poly_vol_24h_usd: 61176.116572
sources:
  - label: "ClearMarket cross-venue record: Will there be a recession in 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-recession-y-2026"
    retrieved_at: "2026-09-25T13:14:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With both books liquid enough to take seriously, the 7pp gap likely reflects differing resolution criteria or adjudicator definitions of 'recession' rather than pure mispricing, a desk should read the fine print on both contracts before leaning on either price.
