---
signal_id: "CMSIG20260812VS05"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-85468"
headline: "Democrat wins TX-15: 62% on $85K volume"
semantic_title: "Democrats hold a slim edge in the TX-15 House race"
telemetry: "62% · $85K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-F1CD0HM6W4"
event_slug: "housetx15-26"
event_question: "TX-15 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSETX15-26-D"
  question_raw: "Will Democratic win the House race for TX-15?"
  current_price: 0.62
  volume_24h_usd: 85468.47
  volume_cumulative_usd: 128853.19
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in TX-15 at 62%, a narrow lean in a competitive district."
  - "$85K in 24h is 66% of all-time volume, indicating this market is relatively thin but actively accumulating."
  - "TX-15 sits in the Rio Grande Valley; fresh attention here often precedes candidate or polling news."
  - "Resolves on the certified winner of the 2026 TX-15 House general election."
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
      kalshi_vol_24h_usd: 85468.47
sources:
  - label: "ClearMarket market record: TX-15 House winner?"
    url: "https://clearmarket.fyi/events/housetx15-26"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 62% price with 66% of all-time volume printing in one session means this market is being discovered by new participants, desks should monitor for an upcoming poll or candidate development driving the attention.
