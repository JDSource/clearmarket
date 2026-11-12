---
signal_id: "CMSIG20261112VS00"
signal_slug: "howard-lutnick-out-as-secretary-of-comme-vol-14072"
headline: "Lutnick out by Dec 31: 33% on $14K surge"
semantic_title: "Lutnick departure odds hold at a third by year-end"
telemetry: "33% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-12T07:48:29+00:00"
event_id: "CM-EVT-H31QLM4JT3"
event_slug: "howard-lutnick-out-as-secretary-of-commerce-by-december-31"
event_question: "Will Howard Lutnick be out as Secretary of Commerce by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7978663d03b5c053dcea87b39e06fad5bcdd036b0c7febfa4309502c02f70c2c"
  question_raw: "Howard Lutnick out as Secretary of Commerce by December 31?"
  current_price: 0.33
  volume_24h_usd: 14072.866143
  volume_cumulative_usd: 42450.15173599999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices a one-in-three chance Commerce Secretary Lutnick exits before year-end."
  - "24h volume of $14K is 33% of all-time liquidity, fresh capital is piling in fast."
  - "Surge implies renewed attention on cabinet turnover risk heading into late-cycle policy windows."
  - "Contract resolves Dec 31; any resignation, firing, or confirmed departure counts."
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
      poly_vol_24h_usd: 14072.866143
sources:
  - label: "ClearMarket market record: Will Howard Lutnick be out as Secretary of Commerce by "
    url: "https://clearmarket.fyi/events/howard-lutnick-out-as-secretary-of-commerce-by-december-31"
    retrieved_at: "2026-11-12T07:48:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A third of all-time volume arriving in a single day signals that a desk-relevant cabinet disruption narrative is gaining traction and warrants monitoring for Commerce-linked regulatory or trade policy positioning.
