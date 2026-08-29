---
signal_id: "CMSIG20260829VS06"
signal_slug: "will-karishma-manzur-be-the-democratic-n-vol-12511"
headline: "Manzur NH Dem Senate nominee: 6% on $13K"
semantic_title: "Manzur NH Senate nomination trades as a long shot at 6%"
telemetry: "6% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-29T13:34:58+00:00"
event_id: "CM-EVT-HY8R70V952"
event_slug: "new-hampshire-democratic-senate-primary-winner"
event_question: "Will the Democratic Party winner of the New Hampshire Senate primary be determined by the 2026 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1cf96ff28b0fa76e23f12a0cf299fc3bced8b26e0addfc1ef11fb58347c0216e"
  question_raw: "Will Karishma Manzur be the Democratic nominee for Senate in New Hampshire?"
  current_price: 0.061
  volume_24h_usd: 12511.054092999999
  volume_cumulative_usd: 49133.826359999985
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "6% price signals the market sees Manzur as a heavy underdog in New Hampshire's Democratic Senate primary."
  - "Polymarket records $13K in 24h, 25% of all-time volume, a material liquidity event for a lower-profile race."
  - "Volume into a 6% candidate may reflect a speculative position ahead of a primary filing deadline or polling release."
  - "Resolves on the New Hampshire Democratic Senate primary result."
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
      poly_vol_24h_usd: 12511.054092999999
sources:
  - label: "ClearMarket market record: Will the Democratic Party winner of the New Hampshire S"
    url: "https://clearmarket.fyi/events/new-hampshire-democratic-senate-primary-winner"
    retrieved_at: "2026-08-29T13:34:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 25% all-time volume day on a 6% candidate contract suggests speculative interest rather than informed flow, a desk should treat this as noise unless accompanied by a concrete primary catalyst.
