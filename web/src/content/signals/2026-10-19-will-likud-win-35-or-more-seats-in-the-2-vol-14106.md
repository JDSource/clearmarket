---
signal_id: "CMSIG20261019VS03"
signal_slug: "will-likud-win-35-or-more-seats-in-the-2-vol-14106"
headline: "Likud 35+ seats: 2% on $14K Polymarket trade"
semantic_title: "Likud at 35 seats stays a long shot at 2%"
telemetry: "2% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-19T07:48:06+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x78b3aec55f914a149fc110ffd4dcfb008ff94e2df4a451b396f7c14a572d6aa7"
  question_raw: "Will Likud win 35 or more seats in the 2026 Israeli legislative election?"
  current_price: 0.018
  volume_24h_usd: 14106.734091
  volume_cumulative_usd: 45208.689031
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices Likud winning 35 or more Knesset seats in 2026 at just 2%, deep long-shot territory."
  - "$14K in 24h volume equals 31% of the contract's all-time value, an outsized single-session commitment for a low-probability line."
  - "Renewed trading at 2% may reflect speculative positioning on a poll shift or hedging against a Likud electoral recovery."
  - "Resolves on official 2026 Knesset results; current surveys place Likud well below the 35-seat threshold."
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
      poly_vol_24h_usd: 14106.734091
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-19T07:48:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital deploying against a 2% contract warrants monitoring for an undisclosed poll or coalition development that could reprice Likud's seat ceiling.
