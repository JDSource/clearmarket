---
signal_id: "CMSIG20261024VS00"
signal_slug: "2026-balance-of-power-d-senate-r-house-vol-2997975"
headline: "D Senate, R House sweep: 1% on $3M surge"
semantic_title: "Split-Congress sweep odds hold near zero on heavy trading"
telemetry: "1% · $3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-24T07:48:55+00:00"
event_id: "CM-EVT-420D9TG6H7"
event_slug: "balance-of-power-2026-midterms"
event_question: "Will the Republicans gain control of the U.S. House of Representatives in the 2026 midterm elections?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0808de4f0cfd47947f2d1be51f9a9c52ea0fec76f73a75cfbe79ddec98d8a908"
  question_raw: "2026 Balance of Power: D Senate, R House"
  current_price: 0.007
  volume_24h_usd: 2997975.606397
  volume_cumulative_usd: 7749291.788028001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic Senate / Republican House outcome at just 1%, near-total rejection."
  - "39% of all-time volume landed in 24h, making this one of the contract's highest-activity sessions."
  - "Week-before-election positioning drives fresh attention; traders are closing out or hedging tail scenarios."
  - "Resolves on certified 120th Congress composition."
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
      poly_vol_24h_usd: 2997975.606397
sources:
  - label: "ClearMarket market record: Will the Republicans gain control of the U.S. House of "
    url: "https://clearmarket.fyi/events/balance-of-power-2026-midterms"
    retrieved_at: "2026-10-24T07:48:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A massive late-cycle volume flush at 1% signals desks are either unwinding residual hedges or testing liquidity on a near-dead contract before Tuesday's results.
