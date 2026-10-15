---
signal_id: "CMSIG20261015VS00"
signal_slug: "will-the-democratic-party-win-the-govern-vol-137416"
headline: "Georgia governor (D): 47% on $137K surge"
semantic_title: "Georgia governor race stays a toss-up under heavy trading"
telemetry: "47% · $137K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T07:48:38+00:00"
event_id: "CM-EVT-RHX55RJPT1"
event_slug: "govpartyga-26"
event_question: "Georgia Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYGA-26-D"
  question_raw: "Will the Democratic party win the governorship in Georgia"
  current_price: 0.47
  volume_24h_usd: 137416.22
  volume_cumulative_usd: 435818.39
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "At 47%, Kalshi traders see the Democratic candidate as a narrow underdog in the Georgia governor race."
  - "$137K traded in 24h, 32% of all-time volume, marks a major liquidity event for this contract."
  - "October surge likely tracks early-vote data, poll drops, or candidate news tightening the outlook."
  - "Contract resolves on Georgia governor election result."
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
      kalshi_vol_24h_usd: 137416.22
sources:
  - label: "ClearMarket market record: Georgia Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyga-26"
    retrieved_at: "2026-10-15T07:48:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-coin-flip price drawing a third of all-time volume in one session signals desks should treat Georgia's governorship as a live swing risk, not a lean.
