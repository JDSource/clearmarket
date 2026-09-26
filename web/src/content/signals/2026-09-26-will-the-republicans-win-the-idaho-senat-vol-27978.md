---
signal_id: "CMSIG20260926VS00"
signal_slug: "will-the-republicans-win-the-idaho-senat-vol-27978"
headline: "Idaho Senate GOP: 90% on $28K volume surge"
semantic_title: "Betting backs Republicans deep in Idaho Senate at 90%"
telemetry: "90% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T07:47:58+00:00"
event_id: "CM-EVT-HW8FT0L534"
event_slug: "idaho-senate-election-winner"
event_question: "Will the Republicans win the Idaho Senate race in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x22e986868fae24a9e7b6fff86e063cc90843c85c4a9dd65b2628bbf5663997c7"
  question_raw: "Will the Republicans win the Idaho Senate race in 2026?"
  current_price: 0.903
  volume_24h_usd: 27978.278940000004
  volume_cumulative_usd: 51410.10495800002
  arbitration_model: "uma_oracle"
bullets:
  - "90% odds on Polymarket price the Idaho Senate seat as a near-certain Republican hold."
  - "24h volume of $28K equals 54% of all-time, more than half the contract's lifetime activity in one day."
  - "Fresh capital deployment into a lopsided line signals positioning ahead of a filing deadline or poll release."
  - "Resolves on 2026 Idaho Senate election outcome."
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
      poly_vol_24h_usd: 27978.278940000004
sources:
  - label: "ClearMarket market record: Will the Republicans win the Idaho Senate race in 2026?"
    url: "https://clearmarket.fyi/events/idaho-senate-election-winner"
    retrieved_at: "2026-09-26T07:47:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of lifetime volume hitting in a single session on a 90% contract suggests traders are locking in carry on a perceived sure thing, watch for any late Democratic entry or polling shock that could reprice.
