---
signal_id: "CMSIG20261030VS03"
signal_slug: "will-republican-win-the-house-race-for-v-vol-61501"
headline: "GOP VA-06: 92% on $62K Kalshi volume"
semantic_title: "Traders back the GOP to hold VA-06 at 92%"
telemetry: "92% · $62K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-DR4SW84W87"
event_slug: "kxhouserace-va06-26"
event_question: "VA-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA06-26-R"
  question_raw: "Will Republican win the House race for VA-06?"
  current_price: 0.925
  volume_24h_usd: 61501.05
  volume_cumulative_usd: 85111.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "92% prices Republican retention of Virginia's 6th district as a near-certainty."
  - "$61K in 24h is 72% of all-time volume, the contract is effectively being settled by this session."
  - "Late, lopsided volume on a high-conviction seat typically reflects closing of residual short positions."
  - "Resolves on certified VA-06 House election result."
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
      kalshi_vol_24h_usd: 61501.05
sources:
  - label: "ClearMarket market record: VA-06 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-va06-26"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

72% of lifetime volume in one day on a 92% contract signals the market is closing out, not opening; desks are likely locking in gains or covering small hedge legs before election day.
