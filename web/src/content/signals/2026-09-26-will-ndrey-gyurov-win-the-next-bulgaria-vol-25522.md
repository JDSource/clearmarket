---
signal_id: "CMSIG20260926VS03"
signal_slug: "will-ndrey-gyurov-win-the-next-bulgaria-vol-25522"
headline: "Gyurov Bulgaria president: 35% on $25K surge"
semantic_title: "Gyurov draws fresh bets in Bulgarian presidential field"
telemetry: "35% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T12:40:21+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd0590fb2d44c3b5deb053fde7072206ee9041441e3ee0e5fb022a41caf79b407"
  question_raw: "Will Аndrey Gyurov win the next Bulgarian presidential election?"
  current_price: 0.35
  volume_24h_usd: 25522.301139
  volume_cumulative_usd: 92262.20250700002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "Polymarket prices Andrey Gyurov at 35%, a meaningful but non-dominant share of probability in the Bulgarian presidential race."
  - "$25.5K in 24h equals 28% of all-time volume, indicating renewed market engagement with this Eastern European contest."
  - "At 35%, the market sees Gyurov as a credible frontrunner but not a clear winner, consistent with a fragmented candidate field."
  - "Contract resolves on the official Bulgarian presidential election outcome."
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
      poly_vol_24h_usd: 25522.301139
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-09-26T12:40:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume on a 35%-priced Balkan presidential candidate warrants attention from EM-political desks, particularly given parallel activity on the Kostadinov contract in the same session.
