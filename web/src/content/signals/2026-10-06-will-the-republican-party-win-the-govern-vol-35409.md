---
signal_id: "CMSIG20261006VS01"
signal_slug: "will-the-republican-party-win-the-govern-vol-35409"
headline: "GOP Iowa governor: 13% on $35K volume jump"
semantic_title: "Iowa governor odds slip to 13% as GOP betting picks up"
telemetry: "13% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-06T14:43:21+00:00"
event_id: "CM-EVT-8D7ZTR8991"
event_slug: "govpartyia-26"
event_question: "Will the Iowa gubernatorial election result be determined by January 14, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYIA-26-R"
  question_raw: "Will the Republican party win the governorship in Iowa"
  current_price: 0.13
  volume_24h_usd: 35409.92
  volume_cumulative_usd: 89877.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Republican win at 13%, a steep underdog read in a state trending competitive."
  - "39% of all-time volume arrived in 24h, indicating a meaningful spike in trader attention."
  - "Fresh activity may reflect a recent poll, candidate announcement, or early-cycle positioning."
  - "Gubernatorial race resolution tied to 2026 election cycle results."
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
      kalshi_vol_24h_usd: 35409.92
sources:
  - label: "ClearMarket market record: Will the Iowa gubernatorial election result be determin"
    url: "https://clearmarket.fyi/events/govpartyia-26"
    retrieved_at: "2026-10-06T14:43:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 13% price pulling 39% of lifetime volume in one day signals desks are reassessing the Iowa governor race, likely on new polling or candidate news worth tracking.
