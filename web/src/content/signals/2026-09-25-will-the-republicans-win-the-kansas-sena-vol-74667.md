---
signal_id: "CMSIG20260925VS00"
signal_slug: "will-the-republicans-win-the-kansas-sena-vol-74667"
headline: "Kansas Senate GOP: 70% on $74K spike"
semantic_title: "Kansas Senate odds hold at 70% through a volume surge"
telemetry: "70% · $75K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T07:48:30+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb8b5349814450b8bba2ecdda2eeb9f48bd3c795bfb858bedf7a383712b877743"
  question_raw: "Will the Republicans win the Kansas Senate race in 2026?"
  current_price: 0.7
  volume_24h_usd: 74667.323783
  volume_cumulative_usd: 148013.91227000003
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at 70%, a solid but not certain Senate hold in Kansas."
  - "$74K traded in 24h equals 50% of all-time volume, signaling a sharp burst of fresh attention."
  - "With 2026 midterms approaching, traders are reassessing competitive Senate exposure across the map."
  - "Contract resolves on Kansas Senate race outcome in November 2026."
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
      poly_vol_24h_usd: 74667.323783
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-25T07:48:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half the contract's lifetime volume arriving in one session flags this race as newly live for desks running Senate control scenarios.
