---
signal_id: "CMSIG20261027VS07"
signal_slug: "will-benjamin-netanyahu-become-prime-min-vol-123045"
headline: "Netanyahu PM return: 16% on $123K surge"
semantic_title: "Netanyahu PM return stays a long shot at 16%"
telemetry: "16% · $123K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T13:54:51+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-BNET"
  question_raw: "Will Benjamin Netanyahu become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.16
  volume_24h_usd: 123045.17
  volume_cumulative_usd: 296494.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "Kalshi prices Netanyahu returning as Prime Minister at 16%, a meaningful but minority probability following the election."
  - "24h volume of $123K is 41% of all-time, signaling renewed attention on Netanyahu's political fate."
  - "The 16% price aligns with Likud's 21% lead-party odds, suggesting the market ties his PM prospects tightly to Likud's overall performance."
  - "Resolves on Netanyahu assuming the Prime Minister role post-2026 election."
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
      kalshi_vol_24h_usd: 123045.17
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-27T13:54:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Netanyahu's 16% PM odds tracking just below Likud's 21% seat-race price is a coherent signal, desks modeling Israeli coalition scenarios should treat his return as a tail scenario, not a base case.
