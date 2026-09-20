---
signal_id: "CMSIG20260920VS02"
signal_slug: "will-the-republican-party-win-the-govern-vol-13086"
headline: "GOP Kansas governor: 73% on $13K volume jump"
semantic_title: "Kansas governor bet stays tilted Republican at 73%"
telemetry: "73% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T12:50:42+00:00"
event_id: "CM-EVT-53XSJLYKW7"
event_slug: "govpartyks-27"
event_question: "Kansas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYKS-27-R"
  question_raw: "Will the Republican party win the governorship in Kansas"
  current_price: 0.73
  volume_24h_usd: 13086.36
  volume_cumulative_usd: 46831.11
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Kansas governorship win at 73%, a solid but not overwhelming favorite."
  - "24h volume of $13K is 28% of all-time handle, indicating concentrated renewed interest in the race."
  - "Spike may reflect a primary outcome, candidate shift, or spillover attention from the concurrent Kansas Senate contract."
  - "Resolves YES if the Republican candidate wins the Kansas gubernatorial general election."
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
      kalshi_vol_24h_usd: 13086.36
sources:
  - label: "ClearMarket market record: Kansas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyks-27"
    retrieved_at: "2026-09-20T12:50:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat the parallel volume spikes in both Kansas contracts as a linked signal, a single state-level development is likely driving simultaneous reassessment of the full Kansas ballot.
