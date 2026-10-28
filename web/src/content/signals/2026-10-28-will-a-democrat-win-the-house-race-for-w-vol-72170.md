---
signal_id: "CMSIG20261028VS05"
signal_slug: "will-a-democrat-win-the-house-race-for-w-vol-72170"
headline: "Dem WI-3 House win: 86% on $72K surge"
semantic_title: "Heavy trading backs Democrats in WI-3 at 86%"
telemetry: "86% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T15:35:02+00:00"
event_id: "CM-EVT-6C7CNWJ6R7"
event_slug: "housewi3-26"
event_question: "WI-03 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWI3-26-D"
  question_raw: "Will a Democrat win the House race for WI-3?"
  current_price: 0.86
  volume_24h_usd: 72170.7
  volume_cumulative_usd: 176704.66
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democrat winning WI-3 at 86%, odds firmly favor the blue side in this Wisconsin district."
  - "41% of all-time contract volume moved in 24h, matching the elevated House-race activity seen across multiple districts today."
  - "High conviction pricing alongside a volume surge suggests new information, polling, fundraising, or endorsements, reinforcing the Democratic lean."
  - "Resolves on the certified winner of the WI-3 House race."
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
      kalshi_vol_24h_usd: 72170.7
sources:
  - label: "ClearMarket market record: WI-03 House winner?"
    url: "https://clearmarket.fyi/events/housewi3-26"
    retrieved_at: "2026-10-28T15:35:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 86% price holding through a volume surge in WI-3 suggests the market is absorbing fresh information that confirms rather than challenges the Democratic advantage, WI-3 looks effectively called by prediction market capital.
