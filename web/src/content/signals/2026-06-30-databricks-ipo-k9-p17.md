---
signal_id: "CMSIG20260630DV01"
signal_slug: "databricks-ipo-k9-p17"
headline: "Databricks IPO before 2027: Kalshi 9% vs Polymarket 17%"
semantic_title: "Databricks IPO outlook decouples on the major prediction desks"
telemetry: "Polymarket 17% vs Kalshi 9%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-30T10:55:41+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.17
  volume_cumulative_usd: 479681.916797
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.09
bullets:
  - "Polymarket at 17% vs Kalshi at 9%, an 8pp spread with reversed directionality from most peers."
  - "Polymarket is the higher-pricing venue here and holds dramatically deeper liquidity."
  - "Kalshi's lower read may reflect a more conservative retail base or stale order book at thin volume."
  - "Claim resolves YES on a completed Databricks public market listing before Jan 1 2027."
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
      kalshi_vol_24h_usd: 36.54
      poly_vol_24h_usd: 5.45
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-06-30T10:55:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket pricing Databricks nearly twice as likely to IPO as Kalshi does, and holding 25x the volume, the Kalshi price looks stale, a desk running cross-venue positions should treat the 17% as the live consensus.
