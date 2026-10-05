---
signal_id: "CMSIG20261005VS00"
signal_slug: "will-the-democratic-party-win-the-govern-vol-152112"
headline: "NV governor: 54% on $152K surge"
semantic_title: "Nevada governor odds lean Democratic at 54%"
telemetry: "54% · $152K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-TNC2QWG2J9"
event_slug: "govpartynv-26"
event_question: "Nevada Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYNV-26-D"
  question_raw: "Will the Democratic party win the governorship in Nevada"
  current_price: 0.54
  volume_24h_usd: 152112.2
  volume_cumulative_usd: 476477.14
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices Democrats as slight favorites at 54%, a live race, not a runaway."
  - "24h volume of $152K is 32% of all-time handle, a significant single-day commitment."
  - "Nevada's competitive suburban mix draws fresh attention 13 months out from 2026 election day."
  - "Resolves on the Nevada gubernatorial election result."
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
      kalshi_vol_24h_usd: 152112.2
sources:
  - label: "ClearMarket market record: Nevada Governor winner?"
    url: "https://clearmarket.fyi/events/govpartynv-26"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy single-day flow on a near-50/50 market signals desks are actively positioning on Nevada as a marquee swing-state governor race, worth tracking for correlated Senate and presidential exposure.
