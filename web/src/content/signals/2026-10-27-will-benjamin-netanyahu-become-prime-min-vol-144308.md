---
signal_id: "CMSIG20261027VS04"
signal_slug: "will-benjamin-netanyahu-become-prime-min-vol-144308"
headline: "Netanyahu PM Israel: 25% on $144K surge"
semantic_title: "Netanyahu PM return trades at 25% on fresh volume"
telemetry: "25% · $144K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T07:49:11+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-BNET"
  question_raw: "Will Benjamin Netanyahu become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.25
  volume_24h_usd: 144308.01
  volume_cumulative_usd: 408021.82
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "25% price places Netanyahu at the low end of live contention for a return as PM after the 2026 election."
  - "$144K in 24h is 35% of all-time Kalshi volume, meaningful re-engagement as the election approaches."
  - "Surge alongside the Eizenkot contract suggests traders are actively repricing the PM race across multiple candidates simultaneously."
  - "Resolves on who holds the PM office following the 2026 Israeli legislative result."
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
      kalshi_vol_24h_usd: 144308.01
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-27T07:49:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Correlated volume spikes on both Netanyahu and Eizenkot PM contracts in the same session indicate desks are rotating probability between candidates, a single catalyst is likely driving both moves.
