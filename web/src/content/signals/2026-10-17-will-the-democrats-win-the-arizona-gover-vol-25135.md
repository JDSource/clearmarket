---
signal_id: "CMSIG20261017VS07"
signal_slug: "will-the-democrats-win-the-arizona-gover-vol-25135"
headline: "AZ Dem governor 2026: 92% on $25K surge"
semantic_title: "Democrats stay heavy favorites in Arizona governor race on fresh money"
telemetry: "92% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T07:48:43+00:00"
event_id: "CM-EVT-T8VRLGR9D8"
event_slug: "arizona-governor-winner-2026"
event_question: "Will the Arizona Governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaf874c80349379303164629c3962b1456f667ca1d44edf95e0474dd13483a4b3"
  question_raw: "Will the Democrats win the Arizona governor race in 2026?"
  current_price: 0.92
  volume_24h_usd: 25135.988276
  volume_cumulative_usd: 98391.65784200003
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices a Democratic Arizona governor win in 2026 at 92%, strong favorite with limited tail risk priced in."
  - "$25.1K in 24h is 26% of all-time volume, the market is more seasoned, making today's activity still notable."
  - "Arizona remains a marquee Sun Belt battleground; volume at 92% may reflect early-cycle position-building or reaction to candidate news."
  - "Resolves on Arizona's 2026 general election result."
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
      poly_vol_24h_usd: 25135.988276
sources:
  - label: "ClearMarket market record: Will the Arizona Governor election be won by the Republ"
    url: "https://clearmarket.fyi/events/arizona-governor-winner-2026"
    retrieved_at: "2026-10-17T07:48:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A quarter of lifetime volume arriving at 92% odds on the Arizona governor race indicates traders are comfortable backing the Democratic favorite at scale, likely in response to candidate or recruitment developments.
