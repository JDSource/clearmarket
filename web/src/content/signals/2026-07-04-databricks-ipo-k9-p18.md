---
signal_id: "CMSIG20260704DV02"
signal_slug: "databricks-ipo-k9-p18"
headline: "Databricks IPO before 2027: Kalshi 9% vs Polymarket 18%"
semantic_title: "Databricks IPO isolates a reversed spread on the major desks"
telemetry: "Polymarket 18% vs Kalshi 9%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-07-04T10:06:13+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Databricks IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfa0166f81f49ec29802bec6eabd71bd73aa24e65f0681b0071f5d1055ef44776"
  question_raw: "Databricks IPO before 2027?"
  current_price: 0.18
  volume_cumulative_usd: 480447.443778
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DATABRICKS"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.09
bullets:
  - "Polymarket prices Databricks IPO at 18%, Kalshi at 9%, a 9pp gap, with Polymarket the higher venue."
  - "Polymarket holds the dominant book; Kalshi volume is thin by comparison."
  - "Polymarket's crowd may be pricing Databricks' well-publicized late-stage fundraising as a near-term IPO signal."
  - "Claim resolves YES if Databricks lists on a public exchange before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 53.21
      poly_vol_24h_usd: 441.645554
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-07-04T10:06:13+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Polymarket pricing Databricks at double Kalshi's level, backed by substantially more volume, suggests the deeper market sees meaningfully higher IPO probability, a desk should treat the 18% as the better-informed reference.
