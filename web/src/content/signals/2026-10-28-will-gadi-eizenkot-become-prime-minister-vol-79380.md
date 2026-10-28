---
signal_id: "CMSIG20261028VS03"
signal_slug: "will-gadi-eizenkot-become-prime-minister-vol-79380"
headline: "Eizenkot Israel PM '26: 16% on $79K surge"
semantic_title: "Eizenkot PM odds draw fresh money at 16%"
telemetry: "16% · $79K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T15:35:02+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-GEIZ"
  question_raw: "Will Gadi Eizenkot become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.16
  volume_24h_usd: 79380.44
  volume_cumulative_usd: 181271.32
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "Kalshi prices Gadi Eizenkot becoming PM following the 2026 Israeli election at 16%, a long-shot alternative."
  - "44% of all-time volume arrived in the past 24h, consistent with the broader Israeli election event spike."
  - "Eizenkot contract activity tracks alongside Netanyahu and broader Israel election flow, attention is sweeping the full candidate set."
  - "Resolves on Eizenkot being named PM as a direct result of the 2026 Israeli election."
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
      kalshi_vol_24h_usd: 79380.44
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-28T15:35:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume spreading to a 16%-priced alternative candidate signals traders are mapping the full distribution of Israeli PM outcomes, not just the Netanyahu binary, useful for a desk building a portfolio hedge across scenarios.
