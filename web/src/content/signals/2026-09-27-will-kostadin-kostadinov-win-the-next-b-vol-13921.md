---
signal_id: "CMSIG20260927VS03"
signal_slug: "will-kostadin-kostadinov-win-the-next-b-vol-13921"
headline: "Kostadinov Bulgaria president: 1% on $14K flow"
semantic_title: "Kostadinov priced out of Bulgaria's presidential race despite trading pick-up"
telemetry: "1% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-27T07:47:43+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa9e24f23e61265a798a2e484c0ead96255e6cd94034dfc0ab58343aa907cc390"
  question_raw: "Will Kostadin Kostadinov win the next  Bulgarian presidential election?"
  current_price: 0.011
  volume_24h_usd: 13921.767801000002
  volume_cumulative_usd: 52699.60707700001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "At 1%, Polymarket effectively rules out Kostadinov winning Bulgaria's next presidential election."
  - "24h volume of $14K is 26% of all-time contract volume, suggesting fresh but modest engagement."
  - "Trading alongside the Gyurov spike points to a broader Bulgarian presidential news cycle pulling capital across multiple candidate contracts simultaneously."
  - "Contract resolves on the Bulgarian presidential election result."
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
      poly_vol_24h_usd: 13921.767801000002
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-09-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel volume spikes on two Bulgarian presidential long shots in the same session, Gyurov at 18% and Kostadinov at 1%, indicate a single news event is rotating fresh money across the candidate slate, warranting a consolidated political-risk read on Bulgaria.
