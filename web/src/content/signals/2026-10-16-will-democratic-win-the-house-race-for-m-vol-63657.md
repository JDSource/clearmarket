---
signal_id: "CMSIG20261016VS00"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-63657"
headline: "MN-05 Democrat: 93% on $63K Kalshi surge"
semantic_title: "Buyers back the Democratic hold of MN-05 at 93%"
telemetry: "93% · $64K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-16T07:48:37+00:00"
event_id: "CM-EVT-1F7LPV1P19"
event_slug: "kxhouserace-mn05-26"
event_question: "MN-05 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN05-26-D"
  question_raw: "Will Democratic win the House race for MN-05?"
  current_price: 0.932
  volume_24h_usd: 63657.68
  volume_cumulative_usd: 198136.1
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Democratic hold of MN-05 at 93%, implying near-certainty with three weeks to election day."
  - "24h volume of $63K is 32% of the contract's all-time total, a sharp concentration of fresh activity."
  - "MN-05 is a deep-blue Minneapolis seat; surge likely reflects late positioning or hedging against a long-shot upset scenario."
  - "Contract resolves on November 2026 House election results."
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
      kalshi_vol_24h_usd: 63657.68
sources:
  - label: "ClearMarket market record: MN-05 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-mn05-26"
    retrieved_at: "2026-10-16T07:48:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge into a 93% contract signals a desk-relevant liquidity test, traders are locking in near-final pricing on a safe Democratic seat, possibly as part of broader House-control basket positioning.
