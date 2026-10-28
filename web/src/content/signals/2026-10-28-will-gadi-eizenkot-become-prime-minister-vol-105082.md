---
signal_id: "CMSIG20261028VS02"
signal_slug: "will-gadi-eizenkot-become-prime-minister-vol-105082"
headline: "Eizenkot Israel PM 2026: 15% on $105K volume burst"
semantic_title: "Eizenkot PM odds hold at 15% as fresh bets pile in on Kalshi"
telemetry: "15% · $105K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-GEIZ"
  question_raw: "Will Gadi Eizenkot become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.15
  volume_24h_usd: 105082.71
  volume_cumulative_usd: 166295.43
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "15% pricing marks Eizenkot as a long-shot challenger for PM following 2026 elections."
  - "Kalshi recorded $105K in 24h, 63% of all-time volume, matching the Netanyahu contract's surge pattern."
  - "Coordinated volume across Israeli leadership contracts suggests event-driven repositioning on election news."
  - "Resolves if Eizenkot forms or leads the next Israeli government post-2026 vote."
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
      kalshi_vol_24h_usd: 105082.71
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-simultaneous 60%+ all-time volume surges across multiple Israeli PM contracts points to a single catalyst driving broad Israeli political re-pricing, desks should treat this as a portfolio-level Israel election event, not isolated contract noise.
