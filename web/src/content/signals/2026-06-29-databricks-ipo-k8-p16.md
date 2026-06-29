---
signal_id: "CMSIG20260629DV03"
signal_slug: "databricks-ipo-k8-p16"
headline: "Databricks IPO before 2027: Kalshi 8% vs Polymarket 16%"
semantic_title: "Databricks IPO spread bridges two distinct market reads"
telemetry: "Polymarket 16% vs Kalshi 8%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-29T01:47:46+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.16
  volume_cumulative_usd: 479676.466797
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.08
bullets:
  - "Polymarket marks Databricks IPO at 16%, Kalshi at 8%, an 8pp gap on the same pre-2027 horizon."
  - "Polymarket is the higher venue with roughly 29x Kalshi's cumulative volume, reflecting deeper informed flow."
  - "Kalshi's lower price likely reflects thin order books rather than a fundamentally different view on Databricks readiness."
  - "Resolves YES on Databricks completing a public listing before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 32.72
      poly_vol_24h_usd: 1664.486187
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-06-29T01:47:46+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 8pp spread on a well-followed name with significant volume asymmetry suggests Kalshi is underpriced relative to consensus, Polymarket's 16% is the more defensible desk anchor.
