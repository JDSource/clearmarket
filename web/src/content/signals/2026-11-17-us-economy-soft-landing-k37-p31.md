---
signal_id: "CMSIG20261117DV00"
signal_slug: "us-economy-soft-landing-k37-p31"
headline: "U.S. economy 'good' by end-2026: Kalshi 37% vs Polymarket 31%"
semantic_title: "2026 economy outlook carries a premium across venues"
telemetry: "Polymarket 31% vs Kalshi 37%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-17T07:49:13+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.312
  volume_cumulative_usd: 65907.85691900001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.372
bullets:
  - "Kalshi prices the claim at 37%, Polymarket at 31%, a 6pp spread."
  - "Kalshi is the higher venue; Polymarket holds deeper liquidity at roughly 2.6x Kalshi's cumulative volume."
  - "Thinner Kalshi market may reflect a narrower, more optimistic user base; Polymarket's larger pool suggests the lower price is better tested."
  - "Resolution likely hinges on a designated economic-conditions index or adjudicator ruling near Dec 31, 2026."
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
      kalshi_vol_24h_usd: 364.35
      poly_vol_24h_usd: 188.53
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-11-17T07:49:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat the 6pp gap as a potential arb opportunity, but weigh Polymarket's larger liquidity base as the more reliable signal on current consensus.
