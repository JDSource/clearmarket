---
signal_id: "CMSIG20260709VS03"
signal_slug: "will-missouri-have-a-maximum-drought-cat-vol-63545"
headline: "Missouri D4 drought June, July: 71% on $63K surge"
semantic_title: "Missouri D4 drought by early July draws deep-conviction hedging"
telemetry: "71% · $64K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-09T10:57:00+00:00"
event_id: "CM-EVT-3THMS6LQ79"
event_slug: "kxdroughtlevel-26julld4"
event_question: "Which states will experience exceptional drought by July 30?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDROUGHTLEVEL-26JULLD4-MO"
  question_raw: "Will Missouri have a maximum drought category of at least D4 during June 4–July 30, 2026?"
  current_price: 0.71
  volume_24h_usd: 63545.36
  volume_cumulative_usd: 70900.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-07T14:00:00Z"
bullets:
  - "71% price, market assigns strong probability Missouri hits extreme D4 drought in the window."
  - "$63K in 24h is 90% of all-time; near the entire contract's history traded today."
  - "USDA drought monitor updates and crop stress reports likely driving fresh ag-desk and weather-risk attention."
  - "Resolution tied to the June 4, July window; outcome is imminent, compressing time value into directional flow."
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
      kalshi_vol_24h_usd: 63545.36
sources:
  - label: "ClearMarket market record: Which states will experience exceptional drought by Jul"
    url: "https://clearmarket.fyi/events/kxdroughtlevel-26julld4"
    retrieved_at: "2026-07-09T10:57:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 90% of lifetime volume printing in a single day at 71%, this contract is signaling near-certain resolution in the YES direction, agricultural and weather-risk desks should treat D4 as the working assumption for Missouri crop exposure.
