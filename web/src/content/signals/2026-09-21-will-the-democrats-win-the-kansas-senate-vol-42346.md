---
signal_id: "CMSIG20260921VS02"
signal_slug: "will-the-democrats-win-the-kansas-senate-vol-42346"
headline: "Dems Kansas Senate: 26% on $42K volume spike"
semantic_title: "Democrats running above 25% in the Kansas Senate race"
telemetry: "26% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T07:48:00+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x460d3942d385cdeda20519c0c5ad804ae48dc18efc9a82e1f1be87a29e69adb3"
  question_raw: "Will the Democrats win the Kansas Senate race in 2026?"
  current_price: 0.26
  volume_24h_usd: 42346.147715
  volume_cumulative_usd: 90642.992441
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 26% to win Kansas Senate, slight outperformance vs. historical baseline for the state."
  - "47% of all-time volume hit in a single session, the heaviest single-day turnover on this contract."
  - "Fresh attention on a deep-red state race suggests a candidate development or polling surprise is in circulation."
  - "Resolves on 2026 Kansas Senate general election outcome."
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
      poly_vol_24h_usd: 42346.147715
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-21T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half the contract's lifetime volume in one day on a long-shot Democratic seat is an attention signal, a desk should watch for a Republican candidate stumble or a credible Democratic recruit emerging in Kansas.
