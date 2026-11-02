---
signal_id: "CMSIG20261102VS03"
signal_slug: "will-the-democrats-win-the-minnesota-sen-vol-129987"
headline: "Minnesota Senate Dems: 94% on $130K volume surge"
semantic_title: "Odds hold near certainty on Democrats keeping Minnesota Senate"
telemetry: "94% · $130K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:45:32+00:00"
event_id: "CM-EVT-3Z75P7P992"
event_slug: "minnesota-senate-election-winner"
event_question: "Will the Minnesota Senate election result in a winner by the scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x44b642636473fb07f0c2319a1d25729a36134969076ffdbb8979cbfdda612b14"
  question_raw: "Will the Democrats win the Minnesota Senate race in 2026?"
  current_price: 0.94
  volume_24h_usd: 129987.228612
  volume_cumulative_usd: 510295.257349
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 94%, the market treats a Republican flip of this Minnesota seat as a near-impossibility."
  - "24h volume of $130K equals 25% of all-time flow, suggesting a fresh wave of participants locking in the consensus."
  - "Minnesota has not elected a Republican senator in decades; the 94% price reflects both structural and polling reality."
  - "Resolves on 2026 general election results."
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
      poly_vol_24h_usd: 129987.228612
sources:
  - label: "ClearMarket market record: Will the Minnesota Senate election result in a winner b"
    url: "https://clearmarket.fyi/events/minnesota-senate-election-winner"
    retrieved_at: "2026-11-02T17:45:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-conviction volume at 94% indicates desks are using this contract as a near-risk-free anchor within diversified Senate portfolio positions rather than expressing directional doubt.
