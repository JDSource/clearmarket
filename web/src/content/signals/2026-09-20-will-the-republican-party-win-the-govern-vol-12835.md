---
signal_id: "CMSIG20260920VS04"
signal_slug: "will-the-republican-party-win-the-govern-vol-12835"
headline: "Kansas GOP governor: 72% on $13K Kalshi surge"
semantic_title: "Republicans favored to hold the Kansas governorship at 72%"
telemetry: "72% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T07:47:56+00:00"
event_id: "CM-EVT-53XSJLYKW7"
event_slug: "govpartyks-27"
event_question: "Kansas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYKS-27-R"
  question_raw: "Will the Republican party win the governorship in Kansas"
  current_price: 0.72
  volume_24h_usd: 12835.09
  volume_cumulative_usd: 46116.86
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "72% odds reflect solid but not decisive Republican advantage in the Kansas governor race."
  - "$13K in 24h is 28% of all-time volume on Kalshi, indicating fresh interest in the contest."
  - "Attention may follow candidate announcements, polling, or early filing deadlines."
  - "Resolves on Kansas gubernatorial election day."
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
      kalshi_vol_24h_usd: 12835.09
sources:
  - label: "ClearMarket market record: Kansas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyks-27"
    retrieved_at: "2026-09-20T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 72% price with a 28% lifetime-volume day on Kalshi signals the desk that the Kansas governor race is beginning to draw serious electoral positioning, worth tracking as a bellwether for GOP state-level strength.
