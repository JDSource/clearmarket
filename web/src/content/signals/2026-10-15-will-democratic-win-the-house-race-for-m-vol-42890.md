---
signal_id: "CMSIG20261015VS02"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-42890"
headline: "MN-05 (D): 93% on $43K, 32% of all-time vol"
semantic_title: "Fresh volume backs Democratic hold in MN-05 at 93%"
telemetry: "93% · $43K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T07:48:38+00:00"
event_id: "CM-EVT-1F7LPV1P19"
event_slug: "kxhouserace-mn05-26"
event_question: "MN-05 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN05-26-D"
  question_raw: "Will Democratic win the House race for MN-05?"
  current_price: 0.932
  volume_24h_usd: 42890.27
  volume_cumulative_usd: 134478.42
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "At 93%, Kalshi traders see the Democratic candidate as a heavy favorite to retain MN-05."
  - "$43K in 24h accounts for 32% of all-time volume, pulling fresh attention to a seat rarely in play."
  - "A surge at this confidence level may reflect late positioning or hedging tied to broader House majority scenarios."
  - "Contract resolves on MN-05 House election result."
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
      kalshi_vol_24h_usd: 42890.27
sources:
  - label: "ClearMarket market record: MN-05 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-mn05-26"
    retrieved_at: "2026-10-15T07:48:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume at 93% on a safe Democratic seat implies desks are using MN-05 as a building block in House majority basket trades rather than a standalone competitive call.
