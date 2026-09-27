---
signal_id: "CMSIG20260927VS01"
signal_slug: "will-the-republicans-win-the-south-carol-vol-38921"
headline: "SC Senate GOP win: 87% on $39K volume pop"
semantic_title: "Buyers back Republicans heavily in the South Carolina Senate race"
telemetry: "87% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-27T07:47:43+00:00"
event_id: "CM-EVT-44DJH0XML6"
event_slug: "south-carolina-senate-election-winner"
event_question: "Will a winner be declared in the South Carolina Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1c017cbb38a9d0ab233ebb265b25c78290317e6a2470657ca18a73a112397b55"
  question_raw: "Will the Republicans win the South Carolina Senate race in 2026?"
  current_price: 0.87
  volume_24h_usd: 38921.74266
  volume_cumulative_usd: 146133.79163399996
  arbitration_model: "uma_oracle"
bullets:
  - "At 87%, Polymarket prices a Republican hold in South Carolina's 2026 Senate race as a near-certainty."
  - "24h volume of $39K represents 27% of all-time contract liquidity, indicating a meaningful fresh-money session."
  - "Renewed trading at high odds may reflect a candidate announcement, filing deadline, or Democratic challenger dropping out."
  - "Contract resolves on the 2026 South Carolina Senate race result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 38921.74266
sources:
  - label: "ClearMarket market record: Will a winner be declared in the South Carolina Senate "
    url: "https://clearmarket.fyi/events/south-carolina-senate-election-winner"
    retrieved_at: "2026-09-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume reaffirming an 87% Republican price in a reliably red state suggests the session is either locking in a resolved catalyst, such as an uncontested field, or hedging a longer 2026 Senate map position.
