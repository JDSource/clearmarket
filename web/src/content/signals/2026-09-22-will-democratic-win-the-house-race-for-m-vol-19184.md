---
signal_id: "CMSIG20260922VS04"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-19184"
headline: "Democrat MT-1 House: 30% on $19K fresh inflow"
semantic_title: "Democratic odds in MT-1 stay under 25% despite fresh volume"
telemetry: "30% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T07:48:31+00:00"
event_id: "CM-EVT-QWGZDJ1DQ6"
event_slug: "housemt1-26"
event_question: "MT-01 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEMT1-26-D"
  question_raw: "Will Democratic win the House race for MT-1?"
  current_price: 0.3
  volume_24h_usd: 19184.37
  volume_cumulative_usd: 32123.37
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in MT-1 at 30%, an underdog but not a long shot, with real implied probability."
  - "$19.2K in 24h equals a striking 60% of all-time contract volume, the majority of all trading ever done here printed today."
  - "The companion Republican contract (69%) and this 30% price are arithmetically consistent; volume across both legs signals active two-sided repositioning."
  - "Resolves on 2026 MT-1 midterm outcome."
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
      kalshi_vol_24h_usd: 19184.37
sources:
  - label: "ClearMarket market record: MT-01 House winner?"
    url: "https://clearmarket.fyi/events/housemt1-26"
    retrieved_at: "2026-09-22T07:48:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sixty percent of all-time volume in one day means this contract is essentially being discovered or re-rated today, cross-reference with the Republican leg and any breaking MT-1 news.
