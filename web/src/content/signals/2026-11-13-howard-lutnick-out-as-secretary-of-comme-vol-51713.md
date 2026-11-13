---
signal_id: "CMSIG20261113VS00"
signal_slug: "howard-lutnick-out-as-secretary-of-comme-vol-51713"
headline: "Lutnick Commerce exit: 48% on $51K surge"
semantic_title: "Lutnick exit odds sit at 50% through year-end"
telemetry: "48% · $52K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-13T07:48:35+00:00"
event_id: "CM-EVT-H31QLM4JT3"
event_slug: "howard-lutnick-out-as-secretary-of-commerce-by-december-31"
event_question: "Will Howard Lutnick be out as Secretary of Commerce by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7978663d03b5c053dcea87b39e06fad5bcdd036b0c7febfa4309502c02f70c2c"
  question_raw: "Howard Lutnick out as Secretary of Commerce by December 31?"
  current_price: 0.48
  volume_24h_usd: 51713.010523
  volume_cumulative_usd: 94163.16225899999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices a near coin-flip, 48%, on Lutnick leaving Commerce by Dec 31."
  - "24h volume of $51K is 55% of all-time, signaling a sharp burst of fresh attention."
  - "Surge implies a catalyst is perceived imminent, resignation, dismissal, or public reporting."
  - "Resolves Dec 31, 2026; a binary with less than 7 weeks to run."
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
      poly_vol_24h_usd: 51713.010523
sources:
  - label: "ClearMarket market record: Will Howard Lutnick be out as Secretary of Commerce by "
    url: "https://clearmarket.fyi/events/howard-lutnick-out-as-secretary-of-commerce-by-december-31"
    retrieved_at: "2026-11-13T07:48:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of all-time volume printing in a single day on a near-50% price tells a desk this contract is live and that informed flow is undecided, worth monitoring for a price break.
