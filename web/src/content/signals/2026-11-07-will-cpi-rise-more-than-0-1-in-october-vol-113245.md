---
signal_id: "CMSIG20261107VS03"
signal_slug: "will-cpi-rise-more-than-0-1-in-october-vol-113245"
headline: "CPI above 0.1% in Oct: 93% on $113K surge"
semantic_title: "Buyers back the October CPI beat as odds hold near certainty"
telemetry: "93% · $113K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T07:49:22+00:00"
event_id: "CM-EVT-N58KJP0K82"
event_slug: "kxcpi-26oct"
event_question: "Will CPI be released in October?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26OCT-T0.1"
  question_raw: "Will CPI rise more than 0.1% in October 2026?"
  current_price: 0.93
  volume_24h_usd: 113245.9
  volume_cumulative_usd: 339349.0
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-09T14:56:00Z"
bullets:
  - "93% pricing indicates strong consensus that October 2026 CPI will exceed 0.1% MoM."
  - "Kalshi records $113K in 24h, 33% of all-time, a meaningful single-session push."
  - "Fresh volume likely tied to pre-release positioning ahead of CPI print this week."
  - "Resolves upon BLS October 2026 CPI release."
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
      kalshi_vol_24h_usd: 113245.9
sources:
  - label: "ClearMarket market record: Will CPI be released in October?"
    url: "https://clearmarket.fyi/events/kxcpi-26oct"
    retrieved_at: "2026-11-07T07:49:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as the rates and macro community locking in a consensus before the print, 93% leaves little hedging room and signals broad agreement on a firmer inflation reading.
