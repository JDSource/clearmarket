---
signal_id: "CMSIG20260918VS05"
signal_slug: "will-republicans-win-the-senate-race-in-vol-20928"
headline: "GOP Idaho Senate: 94% on $21K inflow"
semantic_title: "Republican Idaho Senate hold priced near certainty"
telemetry: "94% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-18T12:39:43+00:00"
event_id: "CM-EVT-TRRJX6C1D5"
event_slug: "senateid-26"
event_question: "Idaho Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEID-26-R"
  question_raw: "Will Republicans win the Senate race in Idaho?"
  current_price: 0.935
  volume_24h_usd: 20928.66
  volume_cumulative_usd: 53388.9
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "94% price leaves almost no market probability of a Democratic pickup in Idaho's Senate race."
  - "39% of all-time volume in 24 hours is notable for a race with almost no perceived competitiveness."
  - "Volume at this price level likely reflects hedging or arbitrage activity rather than directional conviction."
  - "Resolves on the certified outcome of the Idaho Senate general election."
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
      kalshi_vol_24h_usd: 20928.66
sources:
  - label: "ClearMarket market record: Idaho Senate winner?"
    url: "https://clearmarket.fyi/events/senateid-26"
    retrieved_at: "2026-09-18T12:39:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Elevated volume on a 94%-priced contract in a non-competitive state race warrants a desk check for arbitrage mispricing across correlated Senate outcome markets.
