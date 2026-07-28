---
signal_id: "CMSIG20260728VS00"
signal_slug: "will-the-republican-party-win-the-govern-vol-133286"
headline: "Ohio GOP governor: 51% on $133K surge"
semantic_title: "Ohio GOP governorship race trades at a coin flip"
telemetry: "51% · $133K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-28T10:31:13+00:00"
event_id: "CM-EVT-ZJYN286LR2"
event_slug: "govpartyoh-26"
event_question: "Ohio Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYOH-26-R"
  question_raw: "Will the Republican party win the governorship in Ohio"
  current_price: 0.51
  volume_24h_usd: 133286.17
  volume_cumulative_usd: 276580.59
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices the Republican at 51%, dead even, implying no consensus on the outcome."
  - "$133K traded in 24h, nearly half (48%) of all-time volume, signaling a sudden concentration of fresh capital."
  - "Paired trading with Spike 3 (Dem side at 50%) suggests active two-sided positioning, not a directional bet."
  - "Resolves on Ohio gubernatorial election result; both sides are liquid enough to move quickly on any new polling."
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
      kalshi_vol_24h_usd: 133286.17
sources:
  - label: "ClearMarket market record: Ohio Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyoh-26"
    retrieved_at: "2026-07-28T10:31:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-simultaneous surge on both Republican and Democratic Ohio governor contracts points to a contested race repricing event, a desk should monitor for a new poll or candidate development as the trigger.
