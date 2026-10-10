---
signal_id: "CMSIG20261010VS00"
signal_slug: "will-the-democratic-party-win-the-govern-vol-238416"
headline: "Iowa governor (D): 88% on $238K volume surge"
semantic_title: "Democrats' Iowa governor bid holds strong at 88%"
telemetry: "88% · $238K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T14:12:44+00:00"
event_id: "CM-EVT-8D7ZTR8991"
event_slug: "govpartyia-26"
event_question: "Will the Iowa gubernatorial election result be determined by January 14, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYIA-26-D"
  question_raw: "Will the Democratic party win the governorship in Iowa"
  current_price: 0.88
  volume_24h_usd: 238416.52
  volume_cumulative_usd: 669027.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 88%, market treats a GOP upset as a distant tail risk."
  - "$238K traded in 24h, equal to 36% of all-time volume, signaling a sharp wave of fresh attention."
  - "Late-cycle Iowa engagement suggests polling or campaign news is pulling traders back to this race."
  - "Resolves on Iowa gubernatorial election outcome."
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
      kalshi_vol_24h_usd: 238416.52
sources:
  - label: "ClearMarket market record: Will the Iowa gubernatorial election result be determin"
    url: "https://clearmarket.fyi/events/govpartyia-26"
    retrieved_at: "2026-10-10T14:12:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A third of all-time volume hitting in one session on an 88% contract tells a desk this race just drew a hard look, either confirming comfort or stress-testing the near-certainty price.
