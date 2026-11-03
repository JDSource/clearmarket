---
signal_id: "CMSIG20261103VS06"
signal_slug: "will-the-democrats-win-the-texas-governo-vol-417758"
headline: "Texas Dem governor (PM): 37% on $418K volume"
semantic_title: "Democratic Texas governor odds pick up fresh trading at 37%"
telemetry: "37% · $418K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T15:46:45+00:00"
event_id: "CM-EVT-HCY4NZ1SN4"
event_slug: "texas-governor-winner-2026"
event_question: "Will the Texas Governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x12b727031b38130d945b3e164386874360d9a32fdd7e3d00ed2adb13857e089b"
  question_raw: "Will the Democrats win the Texas governor race in 2026?"
  current_price: 0.37
  volume_24h_usd: 417758.86484899995
  volume_cumulative_usd: 1220810.932189
  arbitration_model: "uma_oracle"
bullets:
  - "At 37%, Polymarket prices a Democratic Texas governor win as a genuine minority but not negligible scenario."
  - "$418K in 24h is 34% of all-time, the contract is attracting sustained interest alongside its Republican counterpart."
  - "Simultaneous volume spikes on both sides of the Texas governor market imply active two-way positioning, not a one-directional bet."
  - "Resolves on the 2026 Texas gubernatorial election result."
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
      poly_vol_24h_usd: 417758.86484899995
sources:
  - label: "ClearMarket market record: Will the Texas Governor election be won by the Republic"
    url: "https://clearmarket.fyi/events/texas-governor-winner-2026"
    retrieved_at: "2026-11-03T15:46:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired volume surges on both the Democratic and Republican Texas governor contracts point to a contested race narrative taking hold; a desk should treat Texas as a live swing-state risk rather than a safe Republican assumption.
