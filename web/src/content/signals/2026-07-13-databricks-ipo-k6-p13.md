---
signal_id: "CMSIG20260713DV02"
signal_slug: "databricks-ipo-k6-p13"
headline: "Databricks IPO before 2027: Kalshi 6% vs Polymarket 13%"
semantic_title: "Databricks listing odds bridge inversely across venues"
telemetry: "Polymarket 13% vs Kalshi 6%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-13T10:57:12+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.13
  volume_cumulative_usd: 482938.6004749999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.06
bullets:
  - "Kalshi prices Databricks IPO before 2027 at 6%; Polymarket at 13%, a 7pp gap."
  - "Polymarket is the higher side and carries roughly 37x Kalshi's cumulative volume."
  - "Kalshi's ultra-thin book likely understates true probability; Polymarket's market is far better price-discovered."
  - "Contract resolves YES if Databricks completes an IPO before January 1, 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-EBC7EEEA61); prices direct from venue APIs"
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
      poly_vol_24h_usd: 11.82
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-13T10:57:12+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket holding dominant liquidity and pricing Databricks roughly twice as likely as Kalshi, the inversion here is almost certainly a liquidity-depth artifact, desks should treat Polymarket's 13% as the operative reference.
