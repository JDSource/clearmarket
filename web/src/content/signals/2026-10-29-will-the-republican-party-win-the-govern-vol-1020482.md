---
signal_id: "CMSIG20261029VS00"
signal_slug: "will-the-republican-party-win-the-govern-vol-1020482"
headline: "TX GOP governor: 64% on $1M surge"
semantic_title: "Buyers back the GOP Texas governorship at 64%"
telemetry: "64% · $1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T14:56:22+00:00"
event_id: "CM-EVT-B8XSR8GJT6"
event_slug: "govpartytx-26"
event_question: "Texas Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYTX-26-R"
  question_raw: "Will the Republican party win the governorship in Texas"
  current_price: 0.64
  volume_24h_usd: 1020482.36
  volume_cumulative_usd: 3650956.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-20T15:00:00Z"
bullets:
  - "Market prices Republicans as clear favorites at 64% to hold the Texas governorship."
  - "Kalshi logs $1.02M in 24h, 28% of all-time volume in a single session."
  - "Late-October surge suggests fresh attention ahead of candidate filing or polling drop."
  - "Resolves on Texas 2026 general election result."
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
      kalshi_vol_24h_usd: 1020482.36
sources:
  - label: "ClearMarket market record: Texas Governor winner?"
    url: "https://clearmarket.fyi/events/govpartytx-26"
    retrieved_at: "2026-10-29T14:56:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A single-session volume spike consuming over a quarter of all-time flow signals desks are actively repositioning on Texas gubernatorial risk, warranting a close watch on any polling or candidate news this week.
