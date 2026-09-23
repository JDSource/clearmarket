---
signal_id: "CMSIG20260923VS06"
signal_slug: "will-democratic-win-the-house-race-for-i-vol-10783"
headline: "IA-3 House Dem: 76% on $11K volume pop"
semantic_title: "Fresh volume returns to Democrats in IA-3 at 76%"
telemetry: "76% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-23T13:18:01+00:00"
event_id: "CM-EVT-2VB36981K2"
event_slug: "houseia3-26"
event_question: "IA-03 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEIA3-26-D"
  question_raw: "Will Democratic win the House race for IA-3?"
  current_price: 0.76
  volume_24h_usd: 10783.9
  volume_cumulative_usd: 28282.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats at 76% in IA-3, a solid but not overwhelming favorite in a historically competitive Iowa district."
  - "24h volume of $11K is 38% of all-time handle, the second-highest all-time share in this batch."
  - "IA-3 has flipped parties multiple cycles; 76% pricing with a fresh volume burst suggests new polling or opponent news is being priced."
  - "Resolves on the November 2026 IA-3 House general election result."
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
      kalshi_vol_24h_usd: 10783.9
sources:
  - label: "ClearMarket market record: IA-03 House winner?"
    url: "https://clearmarket.fyi/events/houseia3-26"
    retrieved_at: "2026-09-23T13:18:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 38% all-time daily volume share on a swing-district contract at 76% points to active repricing, potentially driven by local polling or candidate news that hasn't fully surfaced publicly yet.
