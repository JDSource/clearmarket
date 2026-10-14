---
signal_id: "CMSIG20261014VS04"
signal_slug: "will-the-democratic-party-win-the-nh-02-vol-20324"
headline: "Dem NH-02 House win: 96% on $20K volume burst"
semantic_title: "NH-02 Democratic hold trades near certainty through a volume burst"
telemetry: "96% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T13:17:59+00:00"
event_id: "CM-EVT-4NDJ6QGJ77"
event_slug: "nh-02-house-election-winner"
event_question: "Who will win the New Hampshire 2nd Congressional District House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1790d20eab125a64b999fe78dd91eb8ed116a20d87dd782fad9f45a1f7b4dd58"
  question_raw: "Will the Democratic Party win the NH-02 House seat?"
  current_price: 0.959
  volume_24h_usd: 20324.184412
  volume_cumulative_usd: 30452.183085999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices 96%, market is near-unanimous on a Democratic hold in New Hampshire's second district."
  - "$20K in 24h covers 67% of all-time volume, a sharp spike in a historically quiet contract."
  - "Attention surge at extreme odds may reflect arbitrage or a news item touching the district."
  - "Resolves on 2026 midterm election night."
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
      poly_vol_24h_usd: 20324.184412
sources:
  - label: "ClearMarket market record: Who will win the New Hampshire 2nd Congressional Distri"
    url: "https://clearmarket.fyi/events/nh-02-house-election-winner"
    retrieved_at: "2026-10-14T13:17:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A two-thirds all-time volume spike at 96% warrants monitoring for any candidate or ballot news that could introduce tail risk into what the market treats as a locked seat.
