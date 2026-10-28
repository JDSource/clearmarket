---
signal_id: "CMSIG20261028VS01"
signal_slug: "will-benjamin-netanyahu-become-prime-min-vol-692501"
headline: "Netanyahu 2026 PM via election: 24% on $693K surge"
semantic_title: "Kalshi traders back Netanyahu at 24% in the 2026 election race"
telemetry: "24% · $693K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-BNET"
  question_raw: "Will Benjamin Netanyahu become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.24
  volume_24h_usd: 692501.81
  volume_cumulative_usd: 1083660.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "24% pricing puts Netanyahu as a clear underdog in the formal 2026 election contract."
  - "Kalshi saw $692K in 24h, 64% of all-time volume, a near-full book turnover."
  - "Divergence from Polymarket's 50% suggests contract-scope differences driving split pricing."
  - "Resolves on Netanyahu specifically winning PM role via 2026 Israeli legislative election."
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
      kalshi_vol_24h_usd: 692501.81
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 64% all-time volume share in one session on a 24% price tells desks there is active repositioning, the sharp discount to Polymarket's 50% is a structural arb worth examining before Israeli election results.
