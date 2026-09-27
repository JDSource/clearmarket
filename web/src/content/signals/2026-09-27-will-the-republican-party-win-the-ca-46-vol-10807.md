---
signal_id: "CMSIG20260927VS04"
signal_slug: "will-the-republican-party-win-the-ca-46-vol-10807"
headline: "GOP CA-46 House seat: 4% on $11K surge"
semantic_title: "CA-46 Republican odds hold at long-shot levels on rising volume"
telemetry: "4% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-27T07:47:43+00:00"
event_id: "CM-EVT-Q44D460T30"
event_slug: "ca-46-house-election-winner"
event_question: "Will the CA-46 House seat be won by a new representative in the 2026 general election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x544f00d1660aa786d5c535fb0c217246062d70274cbd8bcfddd64703206ab2eb"
  question_raw: "Will the Republican Party win the CA-46 House seat?"
  current_price: 0.04
  volume_24h_usd: 10807.0
  volume_cumulative_usd: 37284.633140000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 4%, Polymarket prices a Republican win in CA-46 as a deep underdog outcome, mirroring the CA-36 read."
  - "24h volume of $11K equals 29% of all-time contract liquidity, a notable single-session concentration."
  - "Simultaneous spikes in CA-36 and CA-46 suggest a shared California House catalyst, redistricting news, a candidate entry, or a broader 2026 map repricing."
  - "Contract resolves on the CA-46 general election result."
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
      poly_vol_24h_usd: 10807.0
sources:
  - label: "ClearMarket market record: Will the CA-46 House seat be won by a new representativ"
    url: "https://clearmarket.fyi/events/ca-46-house-election-winner"
    retrieved_at: "2026-09-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Back-to-back California House district volume spikes at identical 4% prices in one session point to a systematic map-level development rather than district-specific news, a 2026 California redistricting or recruit story deserves immediate desk attention.
