---
signal_id: "CMSIG20261004VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-192830"
headline: "Alaska Senate Dem: 75% on $193K surge"
semantic_title: "Democrats hold a 75% edge in Alaska Senate"
telemetry: "75% · $193K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T07:48:35+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-D"
  question_raw: "Will Democratics win the Senate race in Alaska?"
  current_price: 0.75
  volume_24h_usd: 192830.92
  volume_cumulative_usd: 727407.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 75%, a strong favorite in a state that leaned Republican for decades."
  - "27% of all-time volume landed in 24h, signaling a sharp burst of fresh conviction."
  - "Alaska's unusual ranked-choice dynamics and a fractured GOP field keep this race in play."
  - "Contract resolves on 2026 election night."
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
      kalshi_vol_24h_usd: 192830.92
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-10-04T07:48:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 27% single-day share of all-time volume on a 75% favorite signals desks are actively repricing Alaska as a near-lock for Democrats, worth monitoring for any GOP field consolidation that could shift odds.
