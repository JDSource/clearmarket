---
signal_id: "CMSIG20260724DV03"
signal_slug: "anduril-ipo-k4-p10"
headline: "Anduril IPO before 2027: Kalshi 4% vs Polymarket 10%"
semantic_title: "Anduril IPO long-shot prices diverge across venues"
telemetry: "Polymarket 10% vs Kalshi 4%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-24T10:14:49+00:00"
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
    current_price: 0.04
bullets:
  - "Kalshi prices Anduril IPO at 4%, Polymarket at 10%, a 6pp gap on an already low base"
  - "Polymarket is the higher venue; $355,803 vs Kalshi's $9,694 in cumulative volume"
  - "At these low probability levels, a 6pp gap is proportionally large; Polymarket's 37x deeper volume makes it the dominant price-discovery venue"
  - "Resolves YES only on a confirmed Anduril IPO pricing or first trading day before Jan 1, 2027"
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
      kalshi_vol_24h_usd: 0.12
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-07-24T10:14:49+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

On a tail event priced in single digits, Polymarket's deeply liquid 10% is the operative market, Kalshi's 4% on negligible volume is an outlier a desk should largely disregard.
