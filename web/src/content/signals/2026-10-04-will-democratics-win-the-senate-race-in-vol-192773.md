---
signal_id: "CMSIG20261004VS01"
signal_slug: "will-democratics-win-the-senate-race-in-vol-192773"
headline: "AK Senate Dem win: 75% on $193K volume"
semantic_title: "Democrats hold Alaska Senate odds above 75%"
telemetry: "75% · $193K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T13:40:01+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-D"
  question_raw: "Will Democratics win the Senate race in Alaska?"
  current_price: 0.75
  volume_24h_usd: 192773.24
  volume_cumulative_usd: 727418.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning Alaska's Senate seat at 75%, a strong favorite reading in a historically red state."
  - "$192,773 in 24h volume represents 27% of all-time activity, a notable single-day push for a state-level race."
  - "Surge likely reflects new polling, candidate news, or national environment shifts tightening the GOP's hold on Alaska."
  - "Contract resolves on the certified Alaska Senate election result."
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
      kalshi_vol_24h_usd: 192773.24
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-10-04T13:40:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 75% Democratic price in Alaska accompanied by a significant volume flush warrants attention, desks tracking Senate majority scenarios should note this as a potential leading indicator of broader map movement.
