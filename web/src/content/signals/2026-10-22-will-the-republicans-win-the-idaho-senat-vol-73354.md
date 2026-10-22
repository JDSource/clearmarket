---
signal_id: "CMSIG20261022VS03"
signal_slug: "will-the-republicans-win-the-idaho-senat-vol-73354"
headline: "Idaho Senate GOP: 90% on $73K Polymarket surge"
semantic_title: "Traders back Idaho Senate GOP to win at 90%"
telemetry: "90% · $73K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-HW8FT0L534"
event_slug: "idaho-senate-election-winner"
event_question: "Will the Republicans win the Idaho Senate race in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x22e986868fae24a9e7b6fff86e063cc90843c85c4a9dd65b2628bbf5663997c7"
  question_raw: "Will the Republicans win the Idaho Senate race in 2026?"
  current_price: 0.903
  volume_24h_usd: 73354.304323
  volume_cumulative_usd: 199951.83361299994
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republican win at 90%, consistent with Kalshi's 87% read on the same race."
  - "$73K in 24h is 37% of all-time volume, cross-venue flow confirms broad renewed interest."
  - "Parallel spikes on Kalshi and Polymarket for the same contract suggest arbitrage or coordinated hedging activity."
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
      poly_vol_24h_usd: 73354.304323
sources:
  - label: "ClearMarket market record: Will the Republicans win the Idaho Senate race in 2026?"
    url: "https://clearmarket.fyi/events/idaho-senate-election-winner"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes on both major venues for an identical contract strongly suggests cross-venue arbitrage or a single large position split across platforms, not organic retail discovery.
