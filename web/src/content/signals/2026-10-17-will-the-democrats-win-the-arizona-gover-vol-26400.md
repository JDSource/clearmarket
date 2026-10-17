---
signal_id: "CMSIG20261017VS04"
signal_slug: "will-the-democrats-win-the-arizona-gover-vol-26400"
headline: "AZ governor Democrat: 92% on $26K volume pop"
semantic_title: "Democrats stay strong favorite in Arizona governor race at 92%"
telemetry: "92% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
event_id: "CM-EVT-T8VRLGR9D8"
event_slug: "arizona-governor-winner-2026"
event_question: "Will the Arizona Governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaf874c80349379303164629c3962b1456f667ca1d44edf95e0474dd13483a4b3"
  question_raw: "Will the Democrats win the Arizona governor race in 2026?"
  current_price: 0.92
  volume_24h_usd: 26400.620298
  volume_cumulative_usd: 99661.90784200002
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 92% to win the 2026 Arizona governorship, leaving Republicans a slim 8% shot."
  - "24h volume of $26K is 26% of all-time, a meaningful but not extreme one-day share."
  - "Arizona's swing-state status makes any governor race a macro-relevant event; fresh volume may track candidate news."
  - "Resolves after November 2026 Arizona general election."
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
      poly_vol_24h_usd: 26400.620298
sources:
  - label: "ClearMarket market record: Will the Arizona Governor election be won by the Republ"
    url: "https://clearmarket.fyi/events/arizona-governor-winner-2026"
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained high pricing with a fresh volume tranche suggests the market is treating the Arizona governor race as effectively decided, useful context for downstream policy and Senate race modeling.
