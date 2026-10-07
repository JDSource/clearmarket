---
signal_id: "CMSIG20261007VS05"
signal_slug: "will-the-democratic-party-win-the-tx-26-vol-10415"
headline: "Dems TX-26 House seat: 1% on $10K volume day"
semantic_title: "Traders back Republican hold in TX-26 as Dem odds sit at 1%"
telemetry: "1% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-07T15:02:49+00:00"
event_id: "CM-EVT-Y7G5WKJ4X7"
event_slug: "tx-26-house-election-winner"
event_question: "Will the Republican candidate win the Texas 26th Congressional District House election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfec01e9fd6757ee5b2b9a0f13f0262fd92c5166041ab12333786b25f7d610434"
  question_raw: "Will the Democratic Party win the TX-26 House seat?"
  current_price: 0.014
  volume_24h_usd: 10415.590928000001
  volume_cumulative_usd: 22833.200373
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in Texas's 26th congressional district at 1%, the market assigns near-zero probability to a flip."
  - "46% of all-time volume, $10K, arrived in 24 hours, the most active single day since the contract opened."
  - "TX-26 is a deep-red district; volume at 1% odds mirrors the WI-05 pattern and likely reflects House-majority basket trading."
  - "Resolves on the certified House election result for Texas's 26th district."
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
      poly_vol_24h_usd: 10415.590928000001
sources:
  - label: "ClearMarket market record: Will the Republican candidate win the Texas 26th Congre"
    url: "https://clearmarket.fyi/events/tx-26-house-election-winner"
    retrieved_at: "2026-10-07T15:02:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel 1%-price volume spikes in TX-26 and WI-05 on the same day suggest coordinated House-majority position-building across safe Republican seats rather than any district-specific news.
