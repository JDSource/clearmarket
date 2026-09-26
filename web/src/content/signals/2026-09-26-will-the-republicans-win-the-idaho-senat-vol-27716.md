---
signal_id: "CMSIG20260926VS00"
signal_slug: "will-the-republicans-win-the-idaho-senat-vol-27716"
headline: "Idaho Senate GOP: 90% on $27K volume surge"
semantic_title: "Republicans stay heavy favorites in Idaho Senate"
telemetry: "90% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T12:40:21+00:00"
event_id: "CM-EVT-HW8FT0L534"
event_slug: "idaho-senate-election-winner"
event_question: "Will the Republicans win the Idaho Senate race in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x22e986868fae24a9e7b6fff86e063cc90843c85c4a9dd65b2628bbf5663997c7"
  question_raw: "Will the Republicans win the Idaho Senate race in 2026?"
  current_price: 0.904
  volume_24h_usd: 27716.246757000004
  volume_cumulative_usd: 51489.474958000006
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 90%, near-certainty for the GOP to hold Idaho's Senate seat in 2026."
  - "$27.7K traded in 24h, representing 54% of all-time contract volume, majority of lifetime activity in a single session."
  - "Burst of fresh attention on a deep-red state race suggests either a ballot event or hedging against a long-shot upset scenario."
  - "Contract resolves on 2026 midterm result; at 90%, market sees minimal path for Democrats."
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
      poly_vol_24h_usd: 27716.246757000004
sources:
  - label: "ClearMarket market record: Will the Republicans win the Idaho Senate race in 2026?"
    url: "https://clearmarket.fyi/events/idaho-senate-election-winner"
    retrieved_at: "2026-09-26T12:40:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A single session accounting for more than half of all-time volume on a lopsided contract signals tactical positioning, desks should watch for any Idaho-specific news that might be repricing tail risk.
