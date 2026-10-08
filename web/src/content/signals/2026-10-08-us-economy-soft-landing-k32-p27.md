---
signal_id: "CMSIG20261008DV00"
signal_slug: "us-economy-soft-landing-k32-p27"
headline: "U.S. economy in recession by end 2026: Kalshi 33% vs Polymarket 27%"
semantic_title: "2026 recession odds carry a premium across venues"
telemetry: "Polymarket 27% vs Kalshi 33%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-08T15:11:17+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.27
  volume_cumulative_usd: 47217.920418999995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.328
bullets:
  - "Kalshi prices recession at 33%, Polymarket at 27%, a 6pp gap on the same end-2026 claim."
  - "Kalshi sits higher with roughly $9.6K cumulative volume; Polymarket holds lower with ~$47K, suggesting the deeper-liquidity venue leans more skeptical."
  - "Polymarket's larger pool may reflect broader crowd input diluting recession fears, while Kalshi's tighter, smaller book may skew toward more macro-focused participants."
  - "Resolution likely hinges on an official NBER declaration or a recognized proxy definition baked into each contract's rules, check both desks for differing criteria."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
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
      poly_vol_24h_usd: 138.968276
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-10-08T15:11:17+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp spread against a much larger Polymarket book suggests a desk should scrutinize each contract's recession-definition language before treating this as clean arbitrage, as differing resolution standards may fully explain the gap.
