---
signal_id: "CMSIG20260925VS00"
signal_slug: "will-the-republicans-win-the-kansas-sena-vol-72476"
headline: "Kansas Senate GOP: 70% on $72K volume surge"
semantic_title: "Kansas Senate stays Republican-favored at 70%"
telemetry: "70% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T13:13:41+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8b5349814450b8bba2ecdda2eeb9f48bd3c795bfb858bedf7a383712b877743"
  question_raw: "Will the Republicans win the Kansas Senate race in 2026?"
  current_price: 0.7
  volume_24h_usd: 72476.72092100001
  volume_cumulative_usd: 148078.19797799998
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republican win at 70%, a solid but not certain lead with a competitive margin implied."
  - "24h volume of $72K equals 49% of all-time handle, signaling a near-halving of total contract history in one session."
  - "Late-cycle attention spike suggests a catalyst, poll, candidate news, or money filing, is driving fresh positioning."
  - "Contract resolves on 2026 Kansas Senate race outcome; elevated volume may precede public disclosure of new race data."
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
      poly_vol_24h_usd: 72476.72092100001
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-25T13:13:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should watch for an imminent Kansas polling release or campaign finance filing that triggered this outsized single-session volume.
