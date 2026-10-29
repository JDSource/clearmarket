---
signal_id: "CMSIG20261029VS02"
signal_slug: "will-the-republicans-win-the-montana-sen-vol-60657"
headline: "MT Senate GOP: 90% on $60K Polymarket surge"
semantic_title: "Heavy trading tests the Montana Senate GOP lock at 90%"
telemetry: "90% · $61K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T14:56:22+00:00"
event_id: "CM-EVT-QLN52WYLT6"
event_slug: "montana-senate-election-winner"
event_question: "Montana Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd103195d48bf6183e28c4140bd374dd3e907e8f8d411374cb4d2d124ec4c216d"
  question_raw: "Will the Republicans win the Montana Senate race in 2026?"
  current_price: 0.9
  volume_24h_usd: 60657.370807
  volume_cumulative_usd: 181299.702199
  arbitration_model: "uma_oracle"
bullets:
  - "Market prices Republican Montana Senate victory as near-certain at 90%."
  - "Polymarket records $60.7K in 24h, 33% of all-time volume in one session."
  - "A 90% price with renewed volume implies traders are stress-testing, not challenging, the consensus."
  - "Resolves on the 2026 Montana Senate general election outcome."
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
      poly_vol_24h_usd: 60657.370807
sources:
  - label: "ClearMarket market record: Montana Senate Election Winner"
    url: "https://clearmarket.fyi/events/montana-senate-election-winner"
    retrieved_at: "2026-10-29T14:56:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at 90% suggests traders are either topping up conviction positions or testing whether any new information can move the price off a high-confidence consensus, worth monitoring for any late candidate or polling news.
