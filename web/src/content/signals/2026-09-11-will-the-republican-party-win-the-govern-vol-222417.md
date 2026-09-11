---
signal_id: "CMSIG20260911VS01"
signal_slug: "will-the-republican-party-win-the-govern-vol-222417"
headline: "Florida GOP gov: 81% on $222K volume"
semantic_title: "Florida GOP governorship stays a heavy favorite"
telemetry: "81% · $222K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-11T12:33:13+00:00"
event_id: "CM-EVT-4HX1NKV2L1"
event_slug: "govpartyfl-26"
event_question: "Florida Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYFL-26-R"
  question_raw: "Will the Republican party win the governorship in Florida"
  current_price: 0.81
  volume_24h_usd: 222417.79
  volume_cumulative_usd: 647236.39
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 81% to hold the Florida governorship, a strong lean reflecting structural state-level advantage."
  - "$222K in 24h volume equals 34% of all-time, signaling a meaningful fresh-money commitment rather than routine churn."
  - "Surge likely tied to a candidate announcement, polling release, or filing deadline drawing capital to lock in current odds."
  - "Contract resolves on Florida gubernatorial election outcome."
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
      kalshi_vol_24h_usd: 222417.79
sources:
  - label: "ClearMarket market record: Florida Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyfl-26"
    retrieved_at: "2026-09-11T12:33:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy buying at 81% suggests traders are treating Florida as a near-certainty rather than a live contest; desks should monitor whether a competitive Democratic challenger emerges that could reprice this sharply.
