---
signal_id: "CMSIG20260814VS02"
signal_slug: "will-republican-win-the-house-race-for-t-vol-88384"
headline: "TX-15 House (R): 40% on $88K volume spike"
semantic_title: "TX-15 House race tightens with GOP at 40%"
telemetry: "40% · $88K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-F1CD0HM6W4"
event_slug: "housetx15-26"
event_question: "TX-15 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX15-26-R"
  question_raw: "Will Republican win the House race for TX-15?"
  current_price: 0.4
  volume_24h_usd: 88384.8
  volume_cumulative_usd: 282090.86
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "40% puts Republicans as underdogs in TX-15, a notable framing for a Texas seat."
  - "$88K in 24h represents 31% of all-time volume, a sharp single-session burst."
  - "Competitive House map attention; TX-15 pricing suggests district-level vulnerability."
  - "Resolves on November 2026 general election result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 88384.8
sources:
  - label: "ClearMarket market record: TX-15 House winner?"
    url: "https://clearmarket.fyi/events/housetx15-26"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 31% all-time volume day in TX-15 with GOP at underdog odds flags that desks are treating this as a genuine toss-up worth active positioning.
