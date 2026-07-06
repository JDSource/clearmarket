---
signal_id: "CMSIG20260706VS02"
signal_slug: "will-mahmoud-ahmadinejad-be-head-of-stat-vol-199902"
headline: "Ahmadinejad Iran head of state EOY: 0% on $200K"
semantic_title: "Traders stack against Ahmadinejad Iran return by year-end"
telemetry: "0% · $200K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-06T12:00:42+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb174c3e769e52b51681b154172468f89c685b9fe24c4b0ef3ef5f8c3b511c3a0"
  question_raw: "Will Mahmoud Ahmadinejad be head of state in Iran end of 2026?"
  current_price: 0.003
  volume_24h_usd: 199902.27999999997
  volume_cumulative_usd: 746299.4609739996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket holds Ahmadinejad's probability at zero for heading Iran by December 31, 2026, dismissing any comeback scenario."
  - "$200K in 24h is 27% of all-time volume, notable accumulation but spread across a larger historical base than the Mousavian contract."
  - "Parallel volume across Iran leadership contracts points to a shared geopolitical trigger driving desk-level scenario sweeps."
  - "Contract resolves on Ahmadinejad confirmed as head of state on December 31, 2026."
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
      poly_vol_24h_usd: 199902.27999999997
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-06T12:00:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Coordinated zero-price reinforcement across multiple Iran succession contracts in the same session tells a desk that a geopolitical development, likely around Iran's leadership transition, is driving systematic probability-clearing rather than isolated retail speculation.
