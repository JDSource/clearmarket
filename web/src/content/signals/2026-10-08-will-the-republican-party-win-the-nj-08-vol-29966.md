---
signal_id: "CMSIG20261008VS00"
signal_slug: "will-the-republican-party-win-the-nj-08-vol-29966"
headline: "NJ-08 GOP win: 1% on $30K surge"
semantic_title: "Heavy trading bets NJ-08 stays a Democratic lock"
telemetry: "1% · $30K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-08T15:10:56+00:00"
event_id: "CM-EVT-MGFVWYRY00"
event_slug: "nj-08-house-election-winner"
event_question: "Will the NJ-08 House seat be won by a Republican in the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0bb1b93d62a15087252b42e86b95f82f27232a590f2281da99e2e4cd623c2576"
  question_raw: "Will the Republican Party win the NJ-08 House seat?"
  current_price: 0.01
  volume_24h_usd: 29966.449917
  volume_cumulative_usd: 39377.83207700001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Market prices Republicans at 1%, near-zero chance of flipping this deep-blue seat."
  - "24h volume of $30K is 76% of all-time, the dominant single-session bet on this contract."
  - "Fresh attention likely tracks October House-race polling cycles with 29 days to Election Day."
  - "Resolves on November 2026 general election result for NJ-08."
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
      poly_vol_24h_usd: 29966.449917
sources:
  - label: "ClearMarket market record: Will the NJ-08 House seat be won by a Republican in the"
    url: "https://clearmarket.fyi/events/nj-08-house-election-winner"
    retrieved_at: "2026-10-08T15:10:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Lopsided volume against a 1% Republican price signals traders are locking in the Democratic hold, with almost no residual uncertainty left to price.
