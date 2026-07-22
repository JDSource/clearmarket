---
signal_id: "CMSIG20260722DV03"
signal_slug: "anduril-ipo-k5-p10"
headline: "Anduril IPO before 2027: Kalshi 5% vs Polymarket 10%"
semantic_title: "Anduril IPO odds split across venues with prices reversed"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-22T10:23:07+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.1
  volume_cumulative_usd: 355803.1660839991
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.05
bullets:
  - "Polymarket prices Anduril IPO at 10%, Kalshi at 5%, a 5pp gap, with direction reversed from typical Kalshi-high pattern."
  - "Polymarket is higher and holds roughly 29x the cumulative volume."
  - "Anduril's defense-sector profile may draw a more informed Polymarket crowd; Kalshi's sparse book amplifies small-sample noise."
  - "Resolves YES if Anduril completes an IPO before Jan 1 2027."
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
      kalshi_vol_24h_usd: 0.7
      poly_vol_24h_usd: 75.0
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-07-22T10:23:07+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket's deeper book pricing twice Kalshi's level, the divergence likely reflects Kalshi's thin liquidity rather than a genuine belief split, though a desk may also consider whether defense-IPO-aware traders concentrate on one platform.
