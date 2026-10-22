---
signal_id: "CMSIG20261022VS00"
signal_slug: "will-the-republicans-win-the-ohio-govern-vol-139285"
headline: "Ohio GOP governor: 21% on $139K volume surge"
semantic_title: "Heavy trading tests Ohio GOP at long-shot 21%"
telemetry: "21% · $139K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T07:48:28+00:00"
event_id: "CM-EVT-KSRSHVHX02"
event_slug: "ohio-governor-winner-2026"
event_question: "Will a specific candidate win the Ohio gubernatorial election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x650e3ebc043ddbcfa1d1ffda0c5830f19da7389827889fb5db3474bde5b007fb"
  question_raw: "Will the Republicans win the Ohio governor race in 2026?"
  current_price: 0.21
  volume_24h_usd: 139285.59614699997
  volume_cumulative_usd: 390698.352266
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republicans at just 21%, deep underdog territory in a state trending competitive."
  - "24h volume hit $139K, equal to 36% of all-time handle, signaling a sharp spike in fresh attention."
  - "Ohio's 2026 governor race drawing capital as filing deadlines and candidate field clarify."
  - "Resolves on Ohio gubernatorial election night, November 2026."
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
      poly_vol_24h_usd: 139285.59614699997
sources:
  - label: "ClearMarket market record: Will a specific candidate win the Ohio gubernatorial el"
    url: "https://clearmarket.fyi/events/ohio-governor-winner-2026"
    retrieved_at: "2026-10-22T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-third-of-lifetime volume day in a state-level race flags that desks are reassessing the Ohio governor contest as a live Democratic pickup opportunity, not a formality.
