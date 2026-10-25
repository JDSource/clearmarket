---
signal_id: "CMSIG20261025VS04"
signal_slug: "will-republican-win-the-house-race-for-t-vol-22172"
headline: "GOP wins TX-09: 76% on $22K Kalshi surge"
semantic_title: "Republican hold in TX-09 trades as heavy favorite at 76%"
telemetry: "76% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T12:57:02+00:00"
event_id: "CM-EVT-D0QN4YG685"
event_slug: "kxhousetx9-26"
event_question: "TX-09 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSETX9-26-R"
  question_raw: "Will Republican win the House race for TX-09?"
  current_price: 0.76
  volume_24h_usd: 22172.24
  volume_cumulative_usd: 35310.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "76% reflects a confident Republican lean, market treats TX-09 as likely but not certain GOP retention."
  - "Kalshi logged $22K in 24h, 63% of all-time volume, the bulk of lifetime activity concentrated in one day."
  - "TX-09 is majority-minority Houston district historically held by Democrats; GOP pricing at 76% implies a notable shift."
  - "Resolves on official 2026 midterm TX-09 House race result."
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
      kalshi_vol_24h_usd: 22172.24
sources:
  - label: "ClearMarket market record: TX-09 House winner?"
    url: "https://clearmarket.fyi/events/kxhousetx9-26"
    retrieved_at: "2026-10-25T12:57:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Over three-fifths of lifetime volume landing in one session on a historically Democratic Houston seat priced as a GOP favorite demands desk attention, either redistricting data or candidate dynamics are driving a sharp conviction trade.
