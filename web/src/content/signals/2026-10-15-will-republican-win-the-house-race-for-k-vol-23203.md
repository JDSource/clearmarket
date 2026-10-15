---
signal_id: "CMSIG20261015VS06"
signal_slug: "will-republican-win-the-house-race-for-k-vol-23203"
headline: "KY-06 GOP win: 69% on $23.2K Kalshi volume"
semantic_title: "KY-06 Republican lead draws renewed testing near 75%"
telemetry: "69% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T13:03:58+00:00"
event_id: "CM-EVT-9D5R8WC8R6"
event_slug: "kxhouserace-ky06-26"
event_question: "KY-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-KY06-26-R"
  question_raw: "Will Republican win the House race for KY-06?"
  current_price: 0.69
  volume_24h_usd: 23203.42
  volume_cumulative_usd: 49169.03
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Republicans at 69% in KY-06, a meaningful lead, but Democrats retain over 30% implied probability."
  - "$23.2K in 24h represents 47% of all-time volume, showing concentrated new interest."
  - "Nearly 50% of lifetime volume printing in a day on a sub-75% price signals genuine competitive uncertainty."
  - "Resolves on 2026 KY-06 House election result."
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
      kalshi_vol_24h_usd: 23203.42
sources:
  - label: "ClearMarket market record: KY-06 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-ky06-26"
    retrieved_at: "2026-10-15T13:03:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

KY-06 pricing below 75% with nearly half its all-time volume arriving in one session is a flag for desks tracking House margin, a competitive Kentucky district tightening is an incremental signal for Democratic pickup odds.
