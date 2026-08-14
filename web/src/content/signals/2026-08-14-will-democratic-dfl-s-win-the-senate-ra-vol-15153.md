---
signal_id: "CMSIG20260814VS07"
signal_slug: "will-democratic-dfl-s-win-the-senate-ra-vol-15153"
headline: "Minnesota Senate (DFL): 89% on $15K volume"
semantic_title: "DFL holds strong Minnesota Senate lead at 89%"
telemetry: "89% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-M1PTCWQCS1"
event_slug: "senatemn-26"
event_question: "Minnesota Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMN-26-D"
  question_raw: "Will Democratic (DFL)s win the Senate race in Minnesota?"
  current_price: 0.89
  volume_24h_usd: 15153.41
  volume_cumulative_usd: 56047.47
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "89% reflects heavy DFL favoritism, this race is not competitively priced."
  - "$15K in 24h is 27% of all-time volume, a meaningful relative surge for a low-liquidity contract."
  - "Volume at a high price may reflect hedgers covering short positions or late entrants seeking safe yield."
  - "Resolves on November 2026 Minnesota Senate general election result."
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
      kalshi_vol_24h_usd: 15153.41
sources:
  - label: "ClearMarket market record: Minnesota Senate winner?"
    url: "https://clearmarket.fyi/events/senatemn-26"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume rushing into an 89% contract suggests traders are either closing shorts or locking in high-confidence longs, the underlying race itself is not in question, but position management is active.
