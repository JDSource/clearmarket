---
signal_id: "CMSIG20261103VS02"
signal_slug: "will-the-republican-party-win-the-govern-vol-2486713"
headline: "Texas GOP governor: 67% on $2.5M volume push"
semantic_title: "Texas GOP governor odds hold at 67% through fresh trading"
telemetry: "67% · $2.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T15:46:45+00:00"
event_id: "CM-EVT-B8XSR8GJT6"
event_slug: "govpartytx-26"
event_question: "Texas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYTX-26-R"
  question_raw: "Will the Republican party win the governorship in Texas"
  current_price: 0.67
  volume_24h_usd: 2486713.37
  volume_cumulative_usd: 8542689.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-20T15:00:00Z"
bullets:
  - "At 67%, the market treats a Republican Texas governorship as the probable outcome but not a lock."
  - "$2.5M in 24h volume is 29% of all-time, significant but below Florida's session intensity."
  - "Texas has been reliably Republican at the governor level; pricing below 75% implies the race draws genuine contest odds."
  - "Resolves on the 2026 Texas gubernatorial election result."
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
      kalshi_vol_24h_usd: 2486713.37
sources:
  - label: "ClearMarket market record: Texas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartytx-26"
    retrieved_at: "2026-11-03T15:46:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel spikes in both Texas governor contracts (this and Spike 6) suggest traders are simultaneously testing both sides of the Texas race, pointing to a newly competitive dynamic worth tracking.
