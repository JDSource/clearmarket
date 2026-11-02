---
signal_id: "CMSIG20261102VS01"
signal_slug: "will-democratics-win-the-senate-race-in-vol-724905"
headline: "Iowa Senate Dem: 49% on $725K inflow"
semantic_title: "Iowa Senate race sits at a coin-flip close to 50%"
telemetry: "49% · $725K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-R8V0583H75"
event_slug: "senateia-26"
event_question: "Iowa Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEIA-26-D"
  question_raw: "Will Democratics win the Senate race in Iowa?"
  current_price: 0.49
  volume_24h_usd: 724905.95
  volume_cumulative_usd: 2549865.96
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "At 49%, Kalshi prices the Iowa Senate seat as a pure toss-up with no party favored."
  - "$725K in 24h is 28% of all-time volume, significant pre-election repositioning on an undecided race."
  - "A near-50% price the day before voting signals genuine uncertainty and likely tight polling."
  - "Resolves on Iowa Senate general election result."
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
      kalshi_vol_24h_usd: 724905.95
sources:
  - label: "ClearMarket market record: Iowa Senate winner?"
    url: "https://clearmarket.fyi/events/senateia-26"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 49% price combined with a near-record single-day volume surge tells a desk this race is genuinely binary and unresolved, maximum hedging value remains.
