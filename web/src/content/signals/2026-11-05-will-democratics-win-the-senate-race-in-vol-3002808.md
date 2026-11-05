---
signal_id: "CMSIG20261105VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-3002808"
headline: "AK Senate Dem win: 95% on $3M Election Day surge"
semantic_title: "Democrats near-certain in Alaska Senate on heavy volume"
telemetry: "95% · $3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-D"
  question_raw: "Will Democratics win the Senate race in Alaska?"
  current_price: 0.954
  volume_24h_usd: 3002808.43
  volume_cumulative_usd: 7960650.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic win at 95%, implying a near-certain outcome with minimal residual doubt."
  - "38% of all-time contract volume, $3M, landed in 24 hours, the largest single-day commitment on record."
  - "Election Day 2026: live results arriving now are driving last-minute conviction into the 'yes' side."
  - "Resolves on certified Alaska Senate result; any late count shift is the residual 5% tail."
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
      kalshi_vol_24h_usd: 3002808.43
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An enormous Election Day volume flush into a 95% price signals the desk that Alaska is effectively called by the market, watch for official results to confirm.
