---
signal_id: "CMSIG20261103VS00"
signal_slug: "2026-balance-of-power-r-senate-r-house-vol-5695090"
headline: "R House + R Senate sweep: 5% on $5.7M surge"
semantic_title: "Full GOP sweep odds stay near the floor on heavy volume"
telemetry: "5% · $5.7M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T15:46:45+00:00"
event_id: "CM-EVT-420D9TG6H7"
event_slug: "balance-of-power-2026-midterms"
event_question: "Will the Republicans gain control of the U.S. House of Representatives in the 2026 midterm elections?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"
  question_raw: "2026 Balance of Power: R Senate, R House"
  current_price: 0.05
  volume_24h_usd: 5695090.482119
  volume_cumulative_usd: 22079866.242172003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 5%, Polymarket sees a full Republican House-and-Senate sweep as a near-remote outcome heading into 2026 midterms."
  - "$5.7M traded in 24h, 26% of all-time volume, marks one of the contract's busiest single sessions."
  - "Elevated turnover at a low price suggests active selling of the sweep scenario, not a revival of GOP optimism."
  - "Resolves after 2026 midterm results confirm both chamber outcomes."
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
      poly_vol_24h_usd: 5695090.482119
sources:
  - label: "ClearMarket market record: Will the Republicans gain control of the U.S. House of "
    url: "https://clearmarket.fyi/events/balance-of-power-2026-midterms"
    retrieved_at: "2026-11-03T15:46:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as the market firmly pricing Democratic recovery in at least one chamber; the volume burst reflects conviction, not reassessment, of a sweep being off the table.
