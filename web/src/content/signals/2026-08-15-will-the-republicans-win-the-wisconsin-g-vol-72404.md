---
signal_id: "CMSIG20260815VS01"
signal_slug: "will-the-republicans-win-the-wisconsin-g-vol-72404"
headline: "WI GOP governor: 23% on $72K volume spike"
semantic_title: "Republicans stay long shots in Wisconsin governor race at 23%"
telemetry: "23% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-15T08:22:27+00:00"
event_id: "CM-EVT-QYSXP23XP8"
event_slug: "wisconsin-governor-winner-2026"
event_question: "Will the Wisconsin gubernatorial election be won by the incumbent or a challenger?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd66eadbd64b3e815e31c7994470b44fe15c7ef1146f78937d0cfaa4c04fcfda7"
  question_raw: "Will the Republicans win the Wisconsin governor race in 2026?"
  current_price: 0.23
  volume_24h_usd: 72404.654763
  volume_cumulative_usd: 165815.50002299997
  arbitration_model: "uma_oracle"
bullets:
  - "23% price tags Republicans as clear underdogs, with the market heavily favoring a Democratic hold of the Wisconsin governorship."
  - "44% of all-time Polymarket volume landed in the last 24 hours, the single largest daily share in this contract's life."
  - "Concentrated volume against a lopsided price suggests traders are either testing the floor or hedging event-driven tail risk."
  - "Contract resolves on the 2026 Wisconsin gubernatorial election outcome."
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
      poly_vol_24h_usd: 72404.654763
sources:
  - label: "ClearMarket market record: Will the Wisconsin gubernatorial election be won by the"
    url: "https://clearmarket.fyi/events/wisconsin-governor-winner-2026"
    retrieved_at: "2026-08-15T08:22:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-half of lifetime volume arriving in one session at a 23% price is an outlier flow event, desks should watch for a news trigger that could shift the Democratic incumbency narrative in Wisconsin.
