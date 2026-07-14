---
signal_id: "CMSIG20260714DV02"
signal_slug: "anduril-ipo-k5-p10"
headline: "Anduril IPO before 2027: Kalshi 5% vs Polymarket 10%"
semantic_title: "Anduril IPO odds isolate sharply on the major prediction desks"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-14T09:55:35+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.1
  volume_cumulative_usd: 355401.2160839991
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.05
bullets:
  - "Polymarket prices Anduril IPO at 10%, Kalshi at 5%, a 5pp spread on a low-probability claim."
  - "Polymarket is the higher venue here; it also holds the dominant liquidity position on this contract."
  - "At these low absolute levels, 5pp represents a doubling of implied odds, likely driven by resolution-criteria interpretation differences."
  - "Resolves YES if Anduril completes a public market listing before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 0.5
      poly_vol_24h_usd: 13.62
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-07-14T09:55:35+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When base probabilities are this low, a 5pp gap is proportionally extreme, Polymarket's double-the-odds pricing versus Kalshi signals genuine disagreement on tail-event likelihood, and a desk should weight Polymarket's deeper-liquidity price as the primary reference.
