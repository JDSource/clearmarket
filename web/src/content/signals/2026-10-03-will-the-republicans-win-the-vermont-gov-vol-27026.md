---
signal_id: "CMSIG20261003VS04"
signal_slug: "will-the-republicans-win-the-vermont-gov-vol-27026"
headline: "Vermont GOP governor: 79% on $27K volume burst"
semantic_title: "Republicans stay heavy favorites in Vermont governor at 79%"
telemetry: "79% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T13:00:25+00:00"
event_id: "CM-EVT-R85JKZZ4R6"
event_slug: "vermont-governor-winner-2026"
event_question: "Will the Vermont Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6664de877892786b699c552ef88f25ff6e4828f9a847e4f40e4d6d9cd30b1485"
  question_raw: "Will the Republicans win the Vermont governor race in 2026?"
  current_price: 0.79
  volume_24h_usd: 27026.222769
  volume_cumulative_usd: 84731.654773
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 79%, a strong favorite read in a race Vermont's GOP has held in recent cycles."
  - "32% of all-time volume arrived in 24 hours, a meaningful single-session share for a state-level race."
  - "Paired activity with the Democratic Vermont governor contract (Spike 7) indicates fresh two-sided interest in this market."
  - "Resolves on the 2026 Vermont gubernatorial election."
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
      poly_vol_24h_usd: 27026.222769
sources:
  - label: "ClearMarket market record: Will the Vermont Governor election be won by the Democr"
    url: "https://clearmarket.fyi/events/vermont-governor-winner-2026"
    retrieved_at: "2026-10-03T13:00:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 79% GOP price with fresh two-sided volume in Vermont governor suggests the market is stress-testing whether the Republican incumbent advantage holds, worth tracking alongside the Democratic contract for any convergence.
