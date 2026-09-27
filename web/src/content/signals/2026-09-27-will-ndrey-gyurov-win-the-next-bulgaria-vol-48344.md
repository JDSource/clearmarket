---
signal_id: "CMSIG20260927VS00"
signal_slug: "will-ndrey-gyurov-win-the-next-bulgaria-vol-48344"
headline: "Gyurov Bulgaria president: 18% on $48K surge"
semantic_title: "Fresh volume backs Gyurov as a long shot in Bulgaria's presidential race"
telemetry: "18% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-27T07:47:43+00:00"
event_id: "CM-EVT-C541X65QT7"
event_slug: "bulgaria-presidential-election"
event_question: "Will Bulgaria hold a presidential election by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd0590fb2d44c3b5deb053fde7072206ee9041441e3ee0e5fb022a41caf79b407"
  question_raw: "Will Аndrey Gyurov win the next Bulgarian presidential election?"
  current_price: 0.18
  volume_24h_usd: 48344.886817
  volume_cumulative_usd: 120130.334336
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "At 18%, Polymarket rates Gyurov a distant underdog but not a fringe contender in Bulgaria's next presidential vote."
  - "24h volume of $48K equals 40% of all-time contract volume, a concentrated, single-session attention spike."
  - "Burst of fresh activity suggests a domestic political development or candidacy news is driving outside attention to this market."
  - "Contract resolves on the Bulgarian presidential election outcome; no fixed date currently embedded in the question."
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
      poly_vol_24h_usd: 48344.886817
sources:
  - label: "ClearMarket market record: Will Bulgaria hold a presidential election by 2026?"
    url: "https://clearmarket.fyi/events/bulgaria-presidential-election"
    retrieved_at: "2026-09-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 40% all-time volume share landing in one session on a niche Eastern European election contract signals a specific catalyst, likely a candidacy announcement or polling shift, that desks covering EM political risk should investigate immediately.
