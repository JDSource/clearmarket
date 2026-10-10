---
signal_id: "CMSIG20261010VS01"
signal_slug: "will-republican-win-the-house-race-for-k-vol-19298"
headline: "KY-06 GOP House: 72% on $19K surge"
semantic_title: "Republicans' KY-06 House hold backed by heavy trading"
telemetry: "72% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T14:12:44+00:00"
event_id: "CM-EVT-9D5R8WC8R6"
event_slug: "kxhouserace-ky06-26"
event_question: "KY-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-KY06-26-R"
  question_raw: "Will Republican win the House race for KY-06?"
  current_price: 0.72
  volume_24h_usd: 19298.17
  volume_cumulative_usd: 26462.25
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republican at 72%, a meaningful but not overwhelming lead in this House race."
  - "$19K in 24h represents 73% of all-time volume, the vast majority of lifetime activity landed today."
  - "That concentration implies the contract is newly relevant, likely triggered by polling or candidate news."
  - "Resolves on KY-06 general election result."
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
      kalshi_vol_24h_usd: 19298.17
sources:
  - label: "ClearMarket market record: KY-06 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-ky06-26"
    retrieved_at: "2026-10-10T14:12:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When 73% of a contract's lifetime volume trades in a single session, a desk should treat it as a newly liquid signal rather than an established price, this race just got put on the map.
