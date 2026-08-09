---
signal_id: "CMSIG20260809VS00"
signal_slug: "will-democratics-win-the-senate-race-in-vol-132968"
headline: "Ohio Senate: 49% as $133K floods in"
semantic_title: "Ohio Senate race sits at a coin-flip 49%"
telemetry: "49% · $133K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-09T08:37:25+00:00"
event_id: "CM-EVT-MJFDC6MPF0"
event_slug: "senateohs-26"
event_question: "Ohio Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEOHS-26-D"
  question_raw: "Will Democratics win the Senate race in Ohio?"
  current_price: 0.49
  volume_24h_usd: 132968.09
  volume_cumulative_usd: 269598.42
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic Senate win in Ohio at 49%, dead even with the field."
  - "24h volume of $133K is 49% of all-time handle, signaling a mass reassessment of the race."
  - "Knife-edge pricing suggests traders see no clear structural edge for either party in the state."
  - "Contract resolves on Ohio general election outcome; any polling shift could break the deadlock."
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
      kalshi_vol_24h_usd: 132968.09
sources:
  - label: "ClearMarket market record: Ohio Senate winner?"
    url: "https://clearmarket.fyi/events/senateohs-26"
    retrieved_at: "2026-08-09T08:37:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-50% contract drawing half its lifetime volume in one session tells a desk the Ohio Senate race has become a marquee swing-state hedge, worth pricing in campaign and macro scenario models.
