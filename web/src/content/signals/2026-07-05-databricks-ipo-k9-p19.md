---
signal_id: "CMSIG20260705DV03"
signal_slug: "databricks-ipo-k9-p19"
headline: "Databricks IPO before 2027: Kalshi 9% vs Polymarket 19%"
semantic_title: "Databricks IPO spread bridges two distinct crowd reads"
telemetry: "Polymarket 19% vs Kalshi 9%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-05T10:08:50+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.19
  volume_cumulative_usd: 480505.163778
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.09
bullets:
  - "Kalshi prices Databricks IPO at 9%, Polymarket at 19%, a 10pp gap"
  - "Polymarket is the higher-priced venue and holds more than twenty-five times Kalshi's volume"
  - "Polymarket's crowd appears to assign meaningful weight to a late-2026 filing window; Kalshi's sparse flow yields a more skeptical read"
  - "Resolution requires a confirmed Databricks public listing before Jan 1, 2027"
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
      poly_vol_24h_usd: 57.72
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-05T10:08:50+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket's deep book at nearly double Kalshi's price, a desk should treat the 19% as the more reliable anchor and flag the 9% as a thin-market artifact.
