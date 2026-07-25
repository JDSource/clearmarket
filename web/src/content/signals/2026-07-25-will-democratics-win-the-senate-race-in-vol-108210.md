---
signal_id: "CMSIG20260725VS01"
signal_slug: "will-democratics-win-the-senate-race-in-vol-108210"
headline: "Iowa Senate Dems: 42% on $108K volume burst"
semantic_title: "Democratic Iowa Senate odds sit at 42% as fresh bets pile in"
telemetry: "42% · $108K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-R8V0583H75"
event_slug: "senateia-26"
event_question: "Iowa Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEIA-26-D"
  question_raw: "Will Democratics win the Senate race in Iowa?"
  current_price: 0.42
  volume_24h_usd: 108210.92
  volume_cumulative_usd: 180644.85
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 42%, trailing but within striking distance, well above a long-shot read."
  - "$108K in 24h represents 60% of all-time volume, the highest lifetime-share ratio across today's spikes."
  - "Mirror of Spike 0: simultaneous heavy trading on both sides points to contested new information entering the market."
  - "Implied Republican lead of roughly 18 percentage points is the current consensus gap."
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
      kalshi_vol_24h_usd: 108210.92
sources:
  - label: "ClearMarket market record: Iowa Senate winner?"
    url: "https://clearmarket.fyi/events/senateia-26"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When both sides of a binary draw dominant lifetime-share volume in the same session, it signals a genuine information event, not noise, and warrants monitoring for the underlying news catalyst.
