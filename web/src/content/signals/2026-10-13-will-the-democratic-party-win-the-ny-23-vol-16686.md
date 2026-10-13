---
signal_id: "CMSIG20261013VS04"
signal_slug: "will-the-democratic-party-win-the-ny-23-vol-16686"
headline: "NY-23 Democrat: 3% on $17K Polymarket flow"
semantic_title: "NY-23 Democratic odds hold at 3% through a volume surge"
telemetry: "3% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-K34TZHDVH7"
event_slug: "ny-23-house-election-winner"
event_question: "NY-23 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6098d023d47306dbb9d9b41675038f09b47718e4e833e46599bef3ae338dbb35"
  question_raw: "Will the Democratic Party win the NY-23 House seat?"
  current_price: 0.027
  volume_24h_usd: 16686.195715
  volume_cumulative_usd: 32291.367899000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats at 3% in NY-23, a heavy Republican lean with marginal upset probability."
  - "$16.7K in 24h equals 52% of all-time contract volume, a sharp single-session concentration."
  - "NY-23 flipped Republican in recent cycles; any Democratic path requires significant candidate or environmental shift."
  - "Resolves on November 2026 House election."
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
      poly_vol_24h_usd: 16686.195715
sources:
  - label: "ClearMarket market record: NY-23 House Election Winner"
    url: "https://clearmarket.fyi/events/ny-23-house-election-winner"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half the contract's lifetime volume in one day at 3% suggests traders are either stress-testing the House majority math or closing out stale positions as Election Day approaches.
