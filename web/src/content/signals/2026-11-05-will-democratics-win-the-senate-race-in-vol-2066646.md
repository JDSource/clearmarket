---
signal_id: "CMSIG20261105VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-2066646"
headline: "AK Senate Dem: 94% on $2.1M Election Day surge"
semantic_title: "Democrats hold Alaska Senate at 94%"
telemetry: "94% · $2.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T16:03:26+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-D"
  question_raw: "Will Democratics win the Senate race in Alaska?"
  current_price: 0.943
  volume_24h_usd: 2066646.41
  volume_cumulative_usd: 8063655.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Market prices Democrats as near-certain Alaska Senate winners at 94%."
  - "$2.1M in 24h volume is 26% of all-time, dominant single-day spike on Election Day."
  - "Election Day 2026 is today; live returns will resolve the contract within hours."
  - "Kalshi contract resolves on certified winner; 94% leaves little room for reversal."
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
      kalshi_vol_24h_usd: 2066646.41
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-11-05T16:03:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Massive Election Day flow into an already-high-conviction contract signals traders are locking in final positions as Alaska returns come in, treating Democratic victory as a near-certainty.
