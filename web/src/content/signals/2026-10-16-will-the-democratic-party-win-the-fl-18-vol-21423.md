---
signal_id: "CMSIG20261016VS01"
signal_slug: "will-the-democratic-party-win-the-fl-18-vol-21423"
headline: "FL-18 Democrat: 4% on $21K Polymarket spike"
semantic_title: "FL-18 Democratic odds stay near zero through a volume surge"
telemetry: "4% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-16T07:48:37+00:00"
event_id: "CM-EVT-VDWZLZ0SR0"
event_slug: "fl-18-house-election-winner"
event_question: "Will the Republican candidate win Florida's 18th House District in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5d6f3fe42de792f93c9b3a5ed8d4913c8548b353a41ac43384132f1073bc6ac9"
  question_raw: "Will the Democratic Party win the FL-18 House seat?"
  current_price: 0.04
  volume_24h_usd: 21423.755478
  volume_cumulative_usd: 37066.101340999994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Democratic win in FL-18 at just 4%, marking the seat as a heavy Republican lock."
  - "At 58% of all-time contract volume in a single day, this is the sharpest liquidity event the market has seen."
  - "FL-18 (Treasure Coast) is a safe Republican district; fresh volume at near-zero odds points to speculative positioning or opposing-side hedges."
  - "Resolves on November 2026 House general election results."
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
      poly_vol_24h_usd: 21423.755478
sources:
  - label: "ClearMarket market record: Will the Republican candidate win Florida's 18th House "
    url: "https://clearmarket.fyi/events/fl-18-house-election-winner"
    retrieved_at: "2026-10-16T07:48:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of this contract's lifetime volume arriving in 24 hours at 4% odds warrants desk attention as a signal that traders are actively stress-testing the Republican assumption in FL-18, possibly linked to broader House-seat arbitrage.
