---
signal_id: "CMSIG20260811VS03"
signal_slug: "will-darline-graham-finish-1st-in-the-fi-vol-53352"
headline: "Graham SC Rep 1st round: 61% on $53K surge"
semantic_title: "Graham leads SC Republican first round at 61%"
telemetry: "61% · $53K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-34WPGXDWQ8"
event_slug: "kxprimaryplace-scrsens26-1"
event_question: "Will the candidate receiving the most votes win first place in the first round of the South Carolina Republican Senate special primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SCRSENS26-1-DGRA"
  question_raw: "Will Darline Graham finish 1st in the first round of the 2026 South Carolina Republican Senate special primary?"
  current_price: 0.61
  volume_24h_usd: 53352.88
  volume_cumulative_usd: 151571.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-11T14:00:00Z"
bullets:
  - "Market places Graham as the 61% favorite to finish first in the SC Republican primary first round."
  - "$53K in 24h, 35% of all-time volume, reflects a meaningful surge in directional conviction."
  - "Fresh trading likely follows updated internal polling or rival candidate news shifting the field."
  - "Resolves YES if Graham finishes first in the first-round Republican primary count in South Carolina."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 53352.88
sources:
  - label: "ClearMarket market record: Will the candidate receiving the most votes win first p"
    url: "https://clearmarket.fyi/events/kxprimaryplace-scrsens26-1"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 35% all-time volume draw pushing Graham to 61% suggests the market is repricing field dynamics after new information, desks tracking South Carolina Republican primaries should treat this as a signal to revisit rival candidate exposure.
