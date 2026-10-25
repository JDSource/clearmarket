---
signal_id: "CMSIG20261025VS01"
signal_slug: "will-likud-win-the-most-seats-in-the-202-vol-269262"
headline: "Likud most seats: 32% on $269K inflow"
semantic_title: "Likud stays the frontrunner at 32% in Israeli election race"
telemetry: "32% · $269K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T12:57:02+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf77fa3e63014f1f76ea4433dac66b3860493ed7f1a9fee3dfbef9104d7f1eee3"
  question_raw: "Will Likud win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.32
  volume_24h_usd: 269262.59304700006
  volume_cumulative_usd: 1004030.2009109999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "32% makes Likud the implied leader in a fragmented field, no single party near majority territory."
  - "Polymarket recorded $269K in 24h, 27% of all-time $1M pool, meaningful but not panic-driven repositioning."
  - "Attention spike likely tied to Israeli coalition maneuvering and ongoing war-cabinet pressure on Netanyahu."
  - "Resolves on official 2026 Israeli legislative election results."
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
      poly_vol_24h_usd: 269262.59304700006
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-25T12:57:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A large single-day inflow into a mid-odds Likud contract points to desks actively hedging Israeli political risk as coalition dynamics and security conditions shift the electoral landscape.
