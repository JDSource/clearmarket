---
signal_id: "CMSIG20261026VS00"
signal_slug: "will-likud-win-the-most-seats-in-the-202-vol-395965"
headline: "Likud most seats: 28% on $396K volume spike"
semantic_title: "Likud keeps long-shot odds through a heavy Knesset surge"
telemetry: "28% · $396K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T14:48:56+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf77fa3e63014f1f76ea4433dac66b3860493ed7f1a9fee3dfbef9104d7f1eee3"
  question_raw: "Will Likud win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.28
  volume_24h_usd: 395965.682722
  volume_cumulative_usd: 1481086.8040449999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "At 28%, the market prices Likud as unlikely but alive to lead the 2026 Knesset."
  - "24h volume hit $396K, 27% of all-time flow, signaling sharp fresh attention."
  - "Israeli election positioning is live; capital is stress-testing the Likud plurality path."
  - "Resolves on official 2026 Israeli legislative election seat totals."
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
      poly_vol_24h_usd: 395965.682722
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-26T14:48:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-30% price drawing a quarter of all-time volume suggests desks are actively re-underwriting Likud's plurality odds ahead of a near-term polling or coalition development.
