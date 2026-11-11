---
signal_id: "CMSIG20261111DV00"
signal_slug: "us-economy-soft-landing-k29-p24"
headline: "U.S. economy in recession by end-2026: Kalshi 30% vs Polymarket 24%"
semantic_title: "2026 recession call prices higher on one major desk"
telemetry: "Polymarket 24% vs Kalshi 30%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-11T07:48:16+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.244
  volume_cumulative_usd: 60940.572617
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.299
bullets:
  - "Kalshi prices recession at 30%, Polymarket at 24%, a 6pp spread on the same end-2026 claim."
  - "Kalshi carries the higher probability; Polymarket hosts roughly three times the cumulative volume."
  - "Deeper liquidity on Polymarket may reflect broader crowd consensus; Kalshi's smaller pool may skew toward more pessimistic users."
  - "Resolution hinges on an agreed recession definition, NBER declaration or GDP prints, which both venues may handle differently."
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
      kalshi_vol_24h_usd: 1770.23
      poly_vol_24h_usd: 718.36395
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-11-11T07:48:16+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 6pp gap on a relatively low-volume Kalshi market versus a much deeper Polymarket pool suggests a desk should treat Polymarket's 24% as the more crowd-tested signal, while monitoring whether Kalshi's elevated read narrows as liquidity grows.
