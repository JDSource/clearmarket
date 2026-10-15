---
signal_id: "CMSIG20261015VS04"
signal_slug: "will-republican-win-the-house-race-for-k-vol-23191"
headline: "KY-06 (R): 69% on $23K, 47% of all-time vol"
semantic_title: "Betting picks up on a Republican hold in KY-06 at 69%"
telemetry: "69% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T07:48:38+00:00"
event_id: "CM-EVT-9D5R8WC8R6"
event_slug: "kxhouserace-ky06-26"
event_question: "KY-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-KY06-26-R"
  question_raw: "Will Republican win the House race for KY-06?"
  current_price: 0.69
  volume_24h_usd: 23191.69
  volume_cumulative_usd: 49157.3
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "At 69%, Kalshi sees the Republican candidate as a moderate favorite but not a lock in KY-06."
  - "$23K in 24h equals 47% of all-time volume, nearly half the contract's entire trading in one session."
  - "A competitive 69% price with this volume concentration suggests new information is reshaping expectations mid-cycle."
  - "Contract resolves on KY-06 House election result."
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
      kalshi_vol_24h_usd: 23191.69
sources:
  - label: "ClearMarket market record: KY-06 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-ky06-26"
    retrieved_at: "2026-10-15T07:48:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half the contract's lifetime volume arriving at 69% indicates KY-06 is being re-evaluated as a genuine competitive seat, desks should flag it as a potential Republican vulnerability.
