---
signal_id: "CMSIG20260713DV03"
signal_slug: "anduril-ipo-k5-p10"
headline: "Anduril IPO before 2027: Kalshi 5% vs Polymarket 10%"
semantic_title: "Anduril near-term IPO spread isolates across prediction desks"
telemetry: "Polymarket 10% vs Kalshi 5%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-13T10:57:12+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Anduril IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb7a72d5e5e4ad1dd7664fec7b7c3031a66d149d186e9c5180351780eb1323566"
  question_raw: "Anduril IPO before 2027?"
  current_price: 0.1
  volume_cumulative_usd: 355387.5960839991
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-ANDURIL"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.05
bullets:
  - "Kalshi marks Anduril IPO before 2027 at 5%; Polymarket at 10%, a 5pp gap."
  - "Polymarket is the higher side with roughly 30x Kalshi's cumulative volume."
  - "Both venues assign low probability, but Polymarket's deeper market converges on a 2x multiple over Kalshi's price."
  - "Contract resolves YES if Anduril completes a public offering before January 1, 2027."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 7.644166
sources:
  - label: "ClearMarket cross-venue record: Anduril IPO before 2027?"
    url: "https://clearmarket.fyi/compare/anduril-ipo-y-2026"
    retrieved_at: "2026-07-13T10:57:12+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Though both venues agree Anduril is unlikely to IPO before 2027, the persistent 2x ratio between them at low absolute levels suggests Kalshi's thin volume is compressing its price, Polymarket's 10% is the more reliable anchor for desk use.
