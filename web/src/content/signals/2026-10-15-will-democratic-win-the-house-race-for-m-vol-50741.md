---
signal_id: "CMSIG20261015VS04"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-50741"
headline: "MN-05 Dem win: 93% on $50.7K Kalshi volume"
semantic_title: "MN-05 Democratic hold draws fresh backing at strong odds"
telemetry: "93% · $51K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-1F7LPV1P19"
event_slug: "kxhouserace-mn05-26"
event_question: "MN-05 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN05-26-D"
  question_raw: "Will Democratic win the House race for MN-05?"
  current_price: 0.927
  volume_24h_usd: 50741.12
  volume_cumulative_usd: 156333.21
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Democrats priced at 93% in MN-05, a safe blue seat by market consensus."
  - "$50.7K in 24h is 32% of all-time, a meaningful single-day pulse for this contract."
  - "Volume on a strong-favorite race points to House-majority composition hedging rather than seat-level uncertainty."
  - "Resolves on 2026 MN-05 House election result."
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
      kalshi_vol_24h_usd: 50741.12
sources:
  - label: "ClearMarket market record: MN-05 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-mn05-26"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Renewed flow into a 93% Democratic hold suggests traders are using safe-seat contracts as legs in House-majority spread positions, worth cross-referencing against competitive swing-seat exposure.
