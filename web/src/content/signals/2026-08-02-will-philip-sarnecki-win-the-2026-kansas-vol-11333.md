---
signal_id: "CMSIG20260802VS07"
signal_slug: "will-philip-sarnecki-win-the-2026-kansas-vol-11333"
headline: "Sarnecki KS GOP primary: 12% on $11K"
semantic_title: "Sarnecki Kansas GOP governor primary stays a long shot at 12%"
telemetry: "12% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-02T09:53:38+00:00"
event_id: "CM-EVT-JJZDQB7K77"
event_slug: "kansas-governor-republican-primary-winner"
event_question: "Will a Republican candidate win the Kansas Governor primary?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd482f14b4a09d5d554589e8049d4c8eb367bd5caf01c9cb6d45e058b73cf1835"
  question_raw: "Will Philip Sarnecki win the 2026 Kansas Governor Republican primary election?"
  current_price: 0.118
  volume_24h_usd: 11333.876552
  volume_cumulative_usd: 28800.73307300001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "Polymarket prices Philip Sarnecki winning the 2026 Kansas Governor Republican primary at 12%, clear underdog against the field."
  - "39% of all-time volume in 24h points to a sharp and sudden burst of interest in an otherwise thin Kansas primary market."
  - "Spike may reflect a new Sarnecki campaign development, endorsement, or polling data reaching traders before wider coverage."
  - "Resolves on the Kansas Republican gubernatorial primary result; low base price limits upside for contract holders."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 11333.876552
sources:
  - label: "ClearMarket market record: Will a Republican candidate win the Kansas Governor pri"
    url: "https://clearmarket.fyi/events/kansas-governor-republican-primary-winner"
    retrieved_at: "2026-08-02T09:53:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 39%-of-all-time single-day volume spike into a 12% contract on a state primary signals information asymmetry, a local development may be circulating ahead of mainstream news pickup.
