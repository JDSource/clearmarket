---
signal_id: "CMSIG20260629DV04"
signal_slug: "anduril-ipo-k5-p10"
headline: "Anduril IPO before 2027: Kalshi 5% vs Polymarket 10%"
semantic_title: "Anduril IPO tracks a persistent premium on the deeper venue"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-29T12:30:10+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.1
  volume_cumulative_usd: 355238.2469409991
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.05
bullets:
  - "Polymarket prices Anduril's IPO at 10%, Kalshi at 5%, a 5pp gap with Polymarket consistently higher."
  - "Polymarket holds roughly 30x Kalshi's cumulative volume, giving its price substantially greater price-discovery weight."
  - "The 5pp spread is the narrowest in this batch, suggesting reasonable convergence but a residual liquidity-driven discount on Kalshi."
  - "Resolution requires a confirmed public Anduril listing before Jan 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-D39E0284B8); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 24.45
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-06-29T12:30:10+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The modest 5pp spread is consistent with partial convergence, but Polymarket's deeper book makes its 10% the more reliable reference, a desk treating Kalshi's 5% as equivalent overstates the degree of market agreement.
