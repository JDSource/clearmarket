---
signal_id: "CMSIG20260808VS06"
signal_slug: "will-cpi-rise-more-than-0-1-in-july-20-vol-27990"
headline: "July CPI above -0.1%: 89% on $28K volume"
semantic_title: "Heavy trading backs July CPI rising more than -0.1%"
telemetry: "89% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:36:03+00:00"
event_id: "CM-EVT-HVKDYMRT39"
event_slug: "kxcpi-26jul"
event_question: "CPI month-over-month change, July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUL-T-0.1"
  question_raw: "Will CPI rise more than -0.1% in July 2026?"
  current_price: 0.89
  volume_24h_usd: 27990.62
  volume_cumulative_usd: 62675.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-11T13:56:00Z"
bullets:
  - "Kalshi prices July CPI rising more than -0.1% at 89%, traders largely rule out a deeper deflation print."
  - "24h volume of $28K is 45% of all-time, nearly half of all lifetime trading in a single session."
  - "Fresh engagement ahead of the July CPI release indicates traders are locking in the consensus view."
  - "Resolves on the official July 2026 CPI release from the BLS."
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
      kalshi_vol_24h_usd: 27990.62
sources:
  - label: "ClearMarket market record: CPI month-over-month change, July 2026"
    url: "https://clearmarket.fyi/events/kxcpi-26jul"
    retrieved_at: "2026-08-08T08:36:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 89% pricing and 45% of all-time volume in one day, the market is signaling strong consensus that July CPI will not come in at or below -0.1%, directly informing the Fed hold narrative in Spikes 0 and 1.
