---
signal_id: "CMSIG20261028VS02"
signal_slug: "will-benjamin-netanyahu-become-prime-min-vol-659343"
headline: "Netanyahu 2026 election PM: 26% on $659K"
semantic_title: "Netanyahu PM via 2026 election stays a long shot at 26%"
telemetry: "26% · $659K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T15:35:02+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-BNET"
  question_raw: "Will Benjamin Netanyahu become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.26
  volume_24h_usd: 659343.06
  volume_cumulative_usd: 1213715.23
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "Kalshi prices Netanyahu winning PM specifically via the 2026 Israeli election at 26%, a clear underdog read."
  - "24h volume of $659K is 54% of all-time, the majority of this contract's lifetime activity hit in one session."
  - "Surge mirrors the Polymarket Netanyahu spike, suggesting coordinated fresh attention across venues on the same underlying event."
  - "Resolves on Netanyahu being named PM as a direct result of the 2026 election outcome."
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
      kalshi_vol_24h_usd: 659343.06
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-28T15:35:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Over half of all-time volume arriving in one day on the election-specific Netanyahu contract flags that traders are arbitraging or hedging across the Polymarket and Kalshi Netanyahu positions simultaneously.
