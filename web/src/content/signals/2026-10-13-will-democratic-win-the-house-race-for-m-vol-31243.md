---
signal_id: "CMSIG20261013VS00"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-31243"
headline: "MN-05 Democrat: 93% on $31K single-day surge"
semantic_title: "Democrats hold MN-05 as heavy volume backs the favorite"
telemetry: "93% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T07:49:07+00:00"
event_id: "CM-EVT-1F7LPV1P19"
event_slug: "kxhouserace-mn05-26"
event_question: "MN-05 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN05-26-D"
  question_raw: "Will Democratic win the House race for MN-05?"
  current_price: 0.927
  volume_24h_usd: 31243.1
  volume_cumulative_usd: 42865.51
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Democratic win at 93%, a near-certainty in a deep-blue Minneapolis seat."
  - "24h volume of $31K covers 73% of all-time handle, the bulk of lifetime liquidity in one session."
  - "Late-cycle concentration this close to Election Day suggests sharp attention on down-ballot locks."
  - "Resolves on MN-05 general election result."
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
      kalshi_vol_24h_usd: 31243.1
sources:
  - label: "ClearMarket market record: MN-05 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-mn05-26"
    retrieved_at: "2026-10-13T07:49:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A flood of volume into an apparent lock signals desks are sweeping up cheap yes-side exposure or hedging correlated House-wide positions before Election Day.
