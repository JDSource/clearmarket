---
signal_id: "CMSIG20260811VS06"
signal_slug: "will-russia-capture-lyman-by-september-3-vol-27901"
headline: "Russia captures Lyman by Sep 30: 6% on $28K"
semantic_title: "Odds on Russia taking Lyman by September 30 stay near zero at 6%"
telemetry: "6% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-GM6XLL63G6"
event_slug: "will-russia-capture-lyman-in-2025"
event_question: "Will Russia capture Lyman by...?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x25e4d8c492f2b24d8f720c9bd7480e541613405d6d13598c51f36f214ec5112a"
  question_raw: "Will Russia capture Lyman by September 30, 2026?"
  current_price: 0.06
  volume_24h_usd: 27901.579999999998
  volume_cumulative_usd: 71781.73658099998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T23:55:00Z"
bullets:
  - "Market prices Russia capturing Lyman by September 30, 2026 at just 6%, deep discount."
  - "$28K in 24h, 39% of all-time volume, shows a sharp revival of interest in this front-line contract."
  - "Volume likely reflects new battlefield reporting or shifting front-line assessments near Lyman."
  - "Resolves YES only if Russian forces control Lyman before October 1, 2026."
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
      poly_vol_24h_usd: 27901.579999999998
sources:
  - label: "ClearMarket market record: Will Russia capture Lyman by...?"
    url: "https://clearmarket.fyi/events/will-russia-capture-lyman-in-2025"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 39% all-time volume draw at 6% indicates active re-examination of Lyman battlefield probabilities without a consensus shift, desks monitoring Ukraine front-line risk should flag this as a potential leading indicator of updated military intelligence.
