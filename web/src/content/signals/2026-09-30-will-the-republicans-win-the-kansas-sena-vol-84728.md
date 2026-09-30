---
signal_id: "CMSIG20260930VS01"
signal_slug: "will-the-republicans-win-the-kansas-sena-vol-84728"
headline: "Kansas Senate GOP: 73% on $85K, 34% of all-time"
semantic_title: "Traders pile into Kansas Senate race with Republicans at 73%"
telemetry: "73% · $85K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T07:48:11+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8b5349814450b8bba2ecdda2eeb9f48bd3c795bfb858bedf7a383712b877743"
  question_raw: "Will the Republicans win the Kansas Senate race in 2026?"
  current_price: 0.73
  volume_24h_usd: 84728.267334
  volume_cumulative_usd: 252757.95014900004
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 73% to win the Kansas Senate seat, solid favorite but not a lock."
  - "$85K in 24h volume equals 34% of all-time contract volume, marking an outsized single-session surge."
  - "Spike likely follows a new poll, candidate filing deadline, or primary result sharpening the general-election picture."
  - "Contract resolves on the November 2026 Kansas Senate general election outcome."
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
      poly_vol_24h_usd: 84728.267334
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-30T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-day volume burst consuming one-third of all-time liquidity suggests fresh information, likely a poll or candidate development, is forcing repricing of the Kansas Senate race ahead of November.
