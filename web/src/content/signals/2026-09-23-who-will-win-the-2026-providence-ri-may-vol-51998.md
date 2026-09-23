---
signal_id: "CMSIG20260923VS00"
signal_slug: "who-will-win-the-2026-providence-ri-may-vol-51998"
headline: "Providence mayor: 98% on $52K surge"
semantic_title: "Providence mayor race locked in at 98%"
telemetry: "98% · $52K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-2T4GQHNZN2"
event_slug: "kxprovidencemayor-26"
event_question: "Will there be a winner of the Providence mayoral election by November 3, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPROVIDENCEMAYOR-26-DMOR"
  question_raw: "Who will win the 2026 Providence, RI mayoral election?"
  current_price: 0.98
  volume_24h_usd: 51998.76
  volume_cumulative_usd: 155308.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices the Democratic candidate at 98%, effectively a foregone conclusion with weeks to go."
  - "24h volume of $52K equals 33% of all-time handle, a sharp concentration of fresh capital on a settled line."
  - "Volume spike on a near-certain outcome often signals late hedging or position squaring ahead of final weeks."
  - "Resolves on Providence, RI November 2026 mayoral election result."
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
      kalshi_vol_24h_usd: 51998.76
sources:
  - label: "ClearMarket market record: Will there be a winner of the Providence mayoral electi"
    url: "https://clearmarket.fyi/events/kxprovidencemayor-26"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-sided market drawing a third of its lifetime volume in a single day signals participants are either closing out positions or a small cohort is pressing the 98% ceiling, worth monitoring for any late entrant news.
