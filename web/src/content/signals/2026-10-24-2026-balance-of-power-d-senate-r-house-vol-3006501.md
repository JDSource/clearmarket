---
signal_id: "CMSIG20261024VS00"
signal_slug: "2026-balance-of-power-d-senate-r-house-vol-3006501"
headline: "D Senate, R House split: 1% on $3M surge"
semantic_title: "Traders back D-Senate R-House split at long-shot odds"
telemetry: "1% · $3M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-24T12:26:49+00:00"
event_id: "CM-EVT-420D9TG6H7"
event_slug: "balance-of-power-2026-midterms"
event_question: "Will the Republicans gain control of the U.S. House of Representatives in the 2026 midterm elections?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0808de4f0cfd47947f2d1be51f9a9c52ea0fec76f73a75cfbe79ddec98d8a908"
  question_raw: "2026 Balance of Power: D Senate, R House"
  current_price: 0.008
  volume_24h_usd: 3006501.5252040005
  volume_cumulative_usd: 7778396.610871001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Market prices Democratic Senate / Republican House balance of power at just 1%, near-zero conviction."
  - "Polymarket logged $3.01M in 24h volume, equal to 39% of the contract's entire all-time handle."
  - "Seven days from Election Day, a concentrated burst of activity tests whether any residual split-Congress scenario retains value."
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
      poly_vol_24h_usd: 3006501.5252040005
sources:
  - label: "ClearMarket market record: Will the Republicans gain control of the U.S. House of "
    url: "https://clearmarket.fyi/events/balance-of-power-2026-midterms"
    retrieved_at: "2026-10-24T12:26:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $3M single-day surge into a 1% contract seven days out signals desks actively closing or hedging residual tail exposure on a Democratic Senate outcome rather than expressing fresh directional conviction.
