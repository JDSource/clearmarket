---
signal_id: "CMSIG20260814VS05"
signal_slug: "will-eric-barlow-win-the-2026-wyoming-go-vol-29972"
headline: "Barlow WY GOP primary: 77% on $30K surge"
semantic_title: "Barlow leads Wyoming GOP governor primary at 77%"
telemetry: "77% · $30K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-ZZBTDSPX00"
event_slug: "wyoming-governor-republican-primary-winner"
event_question: "Will the Republican Party nominee win the Wyoming Governor primary by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfb481845055afdf15febad269fcb534be4c5e79d5789b72659a036660b46e11b"
  question_raw: "Will Eric Barlow win the 2026 Wyoming Governor Republican primary election?"
  current_price: 0.774
  volume_24h_usd: 29972.481055999997
  volume_cumulative_usd: 74609.58236099998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-18T00:00:00Z"
bullets:
  - "77% makes Barlow a strong but not certain primary favorite heading into the vote."
  - "$30K in 24h, 40% of all-time Polymarket volume, a decisive single-session share."
  - "Primary timing and local polling likely catalyzing final-stretch positioning."
  - "Resolves on Wyoming Republican gubernatorial primary result."
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
      poly_vol_24h_usd: 29972.481055999997
sources:
  - label: "ClearMarket market record: Will the Republican Party nominee win the Wyoming Gover"
    url: "https://clearmarket.fyi/events/wyoming-governor-republican-primary-winner"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty percent of all-time volume entering at 77% suggests traders are taking final directional positions ahead of a near-term primary resolution.
