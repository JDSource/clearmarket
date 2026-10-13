---
signal_id: "CMSIG20261013VS00"
signal_slug: "will-republican-win-the-house-race-for-m-vol-74324"
headline: "MN-01 Republican: 76% on $74K surge"
semantic_title: "Buyers back the GOP hold in MN-01 at 76%"
telemetry: "76% · $74K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T15:33:23+00:00"
event_id: "CM-EVT-0HH4XXLY85"
event_slug: "kxhouserace-mn01-26"
event_question: "Will MN-01 House winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN01-26-R"
  question_raw: "Will Republican win the House race for MN-01?"
  current_price: 0.76
  volume_24h_usd: 74324.28
  volume_cumulative_usd: 132599.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices GOP at 76%, solid favorite but not a lock, leaving real upset risk."
  - "$74K traded in 24h, equal to 56% of all-time contract volume, flagging a sudden attention spike."
  - "Midterm House map focus intensifying; MN-01 is a competitive rural district drawing late-cycle capital."
  - "Contract resolves on November 2026 election result."
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
      kalshi_vol_24h_usd: 74324.28
sources:
  - label: "ClearMarket market record: Will MN-01 House winner be determined by January 4, 202"
    url: "https://clearmarket.fyi/events/kxhouserace-mn01-26"
    retrieved_at: "2026-10-13T15:33:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half the contract's lifetime volume printed in one day, signaling that MN-01 has moved from background to actively watched on the competitive-seat tracker.
