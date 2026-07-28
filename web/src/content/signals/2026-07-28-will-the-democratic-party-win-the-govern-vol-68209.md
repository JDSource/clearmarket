---
signal_id: "CMSIG20260728VS03"
signal_slug: "will-the-democratic-party-win-the-govern-vol-68209"
headline: "Ohio Dem governor: 50% on $68K volume"
semantic_title: "Democratic Ohio governorship odds hold near 50%"
telemetry: "50% · $68K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-28T10:31:13+00:00"
event_id: "CM-EVT-ZJYN286LR2"
event_slug: "govpartyoh-26"
event_question: "Ohio Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYOH-26-D"
  question_raw: "Will the Democratic party win the governorship in Ohio"
  current_price: 0.5
  volume_24h_usd: 68209.77
  volume_cumulative_usd: 180442.8
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices the Democrat at 50%, the market assigns zero edge to either party in this race."
  - "$68K in 24h is 38% of all-time volume, a meaningful but smaller surge than the Republican-side contract."
  - "Both Ohio contracts moving together points to correlated repricing, likely driven by a shared data input such as a poll."
  - "Resolves on election night Ohio; the 1-point spread between the two contracts (51/50) is within noise."
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
      kalshi_vol_24h_usd: 68209.77
sources:
  - label: "ClearMarket market record: Ohio Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyoh-26"
    retrieved_at: "2026-07-28T10:31:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The Ohio governor market is effectively pricing a toss-up in real time, a desk should treat both contracts as a paired position and watch for polling or candidate news that breaks the symmetry.
