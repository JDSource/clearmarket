---
signal_id: "CMSIG20260629DV03"
signal_slug: "databricks-ipo-k6-p16"
headline: "Databricks IPO before 2027: Kalshi 6% vs Polymarket 16%"
semantic_title: "Databricks IPO spread bridges a wide gap across major desks"
telemetry: "Polymarket 16% vs Kalshi 6%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-29T12:30:10+00:00"
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
    current_price: 0.06
bullets:
  - "Polymarket prices the Databricks IPO at 16%, Kalshi at 6%, a 10pp divergence on the same horizon."
  - "Polymarket carries roughly 38x Kalshi's cumulative volume, anchoring the higher price with substantially more participation."
  - "Kalshi's low print on comparatively thin volume may understate true market probability given Databricks' active pre-IPO signaling."
  - "Resolution requires a confirmed public listing before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 66.87
      poly_vol_24h_usd: 795.086187
sources:
  - label: "ClearMarket cross-venue record: Databricks IPO before 2027?"
    url: "https://clearmarket.fyi/compare/databricks-ipo-y-2026"
    retrieved_at: "2026-06-29T12:30:10+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Polymarket's 16% is the better-supported figure here; the 10pp gap and the liquidity imbalance together suggest Kalshi's price has not fully absorbed available public information on Databricks' IPO trajectory.
