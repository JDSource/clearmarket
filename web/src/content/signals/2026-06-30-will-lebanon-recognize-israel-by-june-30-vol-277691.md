---
signal_id: "CMSIG20260630VS03"
signal_slug: "will-lebanon-recognize-israel-by-june-30-vol-277691"
headline: "Lebanon recognizes Israel by June 30: 6% on $278K"
semantic_title: "Lebanon-Israel normalization sits deep in long-shot territory"
telemetry: "6% · $278K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-30T10:55:12+00:00"
event_id: "CM-EVT-C44TBGCDK8"
event_slug: "which-countries-will-recognize-israel-by-june-30"
event_question: "Will additional countries recognize Israel by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x274cec202608757e62a0cf64ec63a3a814a6cc23a1bff1819b437362c5c16732"
  question_raw: "Will Lebanon recognize Israel by June 30?"
  current_price: 0.059
  volume_24h_usd: 277691.2832450002
  volume_cumulative_usd: 915689.1760240004
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket at 6%, slim but non-trivial probability as the deadline expires today."
  - "24h volume $277K is 30% of all-time, suggesting a last-day attention spike."
  - "No diplomatic framework for formal recognition has emerged; flows likely reflect closing shorts."
  - "Resolves today; 6% residual price implies a small cohort still sees a surprise scenario."
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
      poly_vol_24h_usd: 277691.2832450002
sources:
  - label: "ClearMarket market record: Will additional countries recognize Israel by June 30?"
    url: "https://clearmarket.fyi/events/which-countries-will-recognize-israel-by-june-30"
    retrieved_at: "2026-06-30T10:55:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 6% price with elevated last-day volume on a geopolitical normalization contract signals a desk that a thin minority of participants refused to fully write off a surprise announcement right through the deadline.
