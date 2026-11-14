---
signal_id: "CMSIG20261114VS03"
signal_slug: "will-united-airlines-holdings-inc-repor-vol-16261"
headline: "UAL >184M passengers: 97% on $16K volume"
semantic_title: "United Airlines above 184M passengers stays near certain at 97%"
telemetry: "97% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-14T07:48:40+00:00"
event_id: "CM-EVT-XL3H4QDNB2"
event_slug: "kxuala-28janpax"
event_question: "United Airlines passenger count, January 2028"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUALA-28JANPAX-184000000"
  question_raw: "Will United Airlines Holdings Inc. report Above 184 million passengers flown in 2026?"
  current_price: 0.97
  volume_24h_usd: 16261.08
  volume_cumulative_usd: 21663.95
  arbitration_model: "kalshi_staff"
  resolves_at: "2028-03-31T05:00:00Z"
bullets:
  - "Kalshi prices United Airlines reporting above 184 million passengers at 97%, market treats this as effectively resolved."
  - "24h volume of $16K is 75% of all-time, three-quarters of all activity concentrated in this session."
  - "Late-stage contract trading at this confidence level suggests positioning ahead of an imminent earnings or traffic data release."
  - "Resolution hinges on United's official passenger count report."
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
      kalshi_vol_24h_usd: 16261.08
sources:
  - label: "ClearMarket market record: United Airlines passenger count, January 2028"
    url: "https://clearmarket.fyi/events/kxuala-28janpax"
    retrieved_at: "2026-11-14T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing with the bulk of all-time volume arriving now suggests desks are closing positions or locking in known outcomes ahead of United's traffic figures, a low-risk, high-conviction settlement play.
