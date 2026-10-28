---
signal_id: "CMSIG20261028VS03"
signal_slug: "will-gadi-eizenkot-become-prime-minister-vol-89734"
headline: "Eizenkot Israel PM: 17% on $90K volume burst"
semantic_title: "Eizenkot PM bid draws fresh money at long odds"
telemetry: "17% · $90K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T14:50:28+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-GEIZ"
  question_raw: "Will Gadi Eizenkot become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.17
  volume_24h_usd: 89734.47
  volume_cumulative_usd: 191992.39
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "Kalshi prices Gadi Eizenkot at 17% for Prime Minister, a long-shot read on a credible opposition figure."
  - "47% of all-time contract volume hit in 24 hours, consistent with Israeli election news driving attention across the board."
  - "At 17%, the market assigns meaningful but minority odds, Eizenkot is a named alternative, not a fringe bet."
  - "Resolves on post-election PM confirmation."
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
      kalshi_vol_24h_usd: 89734.47
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-28T14:50:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume clustering on a secondary candidate alongside the Netanyahu contract suggests broad Israeli election repricing rather than a single-name catalyst.
