---
signal_id: "CMSIG20261113VS03"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-17150"
headline: "Fed Dec 2027 no-hike: 89% on $17K volume burst"
semantic_title: "Fed hold at December 2027 meeting priced in at 89%"
telemetry: "89% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-13T07:48:35+00:00"
event_id: "CM-EVT-D9GMMQLFR9"
event_slug: "kxfeddecision-27dec"
event_question: "Will the Federal Reserve make a decision in December 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-27DEC-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their December 2027 meeting?"
  current_price: 0.89
  volume_24h_usd: 17150.77
  volume_cumulative_usd: 27996.1
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-12-08T19:05:00Z"
bullets:
  - "Market prices an 89% chance the Fed holds rates at 0bps change at the December 2027 meeting."
  - "61% of all-time volume traded in 24h, the dominant session for this contract by a wide margin."
  - "Fresh flow into a long-dated rates contract may reflect a shift in forward guidance expectations or macro data."
  - "Resolves at the December 2027 FOMC decision; 13-month runway leaves room for significant repricing."
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
      kalshi_vol_24h_usd: 17150.77
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in December 20"
    url: "https://clearmarket.fyi/events/kxfeddecision-27dec"
    retrieved_at: "2026-11-13T07:48:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of all-time volume in one session on a 2027 rates contract signals that macro participants are actively expressing a rates view well into the forward curve, worth flagging alongside rates futures positioning.
