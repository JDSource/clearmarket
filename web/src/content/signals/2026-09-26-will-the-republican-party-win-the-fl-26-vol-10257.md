---
signal_id: "CMSIG20260926VS07"
signal_slug: "will-the-republican-party-win-the-fl-26-vol-10257"
headline: "GOP FL-26 House: 86% on $10K volume at 25% ATH"
semantic_title: "Republicans hold strong pricing on FL-26 House race"
telemetry: "86% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T12:40:21+00:00"
event_id: "CM-EVT-683BTN68V2"
event_slug: "fl-26-house-election-winner"
event_question: "Will the Republican candidate win Florida's 26th Congressional District House election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2d0d0159d0edd3511bf1aeef4ef53a74b0ef2dadcfc6b1019aa31ce74b664861"
  question_raw: "Will the Republican Party win the FL-26 House seat?"
  current_price: 0.86
  volume_24h_usd: 10257.949458000001
  volume_cumulative_usd: 40646.730638
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans at 86% in FL-26, a strong but not ironclad hold on this Florida House seat."
  - "$10.3K in 24h equals exactly 25% of all-time volume, hitting the quarter-lifetime threshold in a single session."
  - "Trading on an 86%-priced contract suggests either hedgers protecting against a slim upset or new entrants backing the consensus."
  - "Contract resolves on the 2026 midterm FL-26 House result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 10257.949458000001
sources:
  - label: "ClearMarket market record: Will the Republican candidate win Florida's 26th Congre"
    url: "https://clearmarket.fyi/events/fl-26-house-election-winner"
    retrieved_at: "2026-09-26T12:40:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 25%-of-lifetime volume day on an 86% Republican contract in FL-26 warrants a check for any local candidate news that could be nudging the small remaining uncertainty.
