---
signal_id: "CMSIG20261013VS04"
signal_slug: "will-republican-win-the-house-race-for-o-vol-17447"
headline: "OH-10 Republican: 84% on $17K Kalshi surge"
semantic_title: "Republican hold in OH-10 backed at 84% on rising volume"
telemetry: "84% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-13T07:49:07+00:00"
event_id: "CM-EVT-TY2DWD9XJ0"
event_slug: "kxhouserace-oh10-26"
event_question: "OH-10 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-OH10-26-R"
  question_raw: "Will Republican win the House race for OH-10?"
  current_price: 0.84
  volume_24h_usd: 17447.62
  volume_cumulative_usd: 51798.31
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in OH-10 at 84%, reflecting a solid but not guaranteed hold."
  - "34% of all-time volume traded in 24 hours, meaningful single-session share for a mid-tier district market."
  - "The 16% residual Democratic chance keeps this seat on the contested watchlist entering the final stretch."
  - "Resolves on the OH-10 general election result."
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
      kalshi_vol_24h_usd: 17447.62
sources:
  - label: "ClearMarket market record: OH-10 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-oh10-26"
    retrieved_at: "2026-10-13T07:49:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 84% price with a notable volume surge in OH-10 signals desks are treating this as a probable-but-not-certain Republican hold worth monitoring as a bellwether for Midwest swing-seat dynamics.
