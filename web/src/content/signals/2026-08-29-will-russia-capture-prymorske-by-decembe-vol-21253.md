---
signal_id: "CMSIG20260829VS05"
signal_slug: "will-russia-capture-prymorske-by-decembe-vol-21253"
headline: "Russia captures Prymorske by Dec 31: 7%"
semantic_title: "Prymorske capture by year-end stays a long shot at 7%"
telemetry: "7% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-29T13:34:58+00:00"
event_id: "CM-EVT-J63P6XRFL4"
event_slug: "will-russia-capture-prymorske-by"
event_question: "Will Russia capture Prymorske in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7dec9c618309c76d9772c3205ecf688828189c00d0485222be618e0a0011f00a"
  question_raw: "Will Russia capture Prymorske by December 31, 2026?"
  current_price: 0.07
  volume_24h_usd: 21253.2
  volume_cumulative_usd: 48283.856506
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "7% price reflects deep skepticism that Russian forces reach Prymorske before year-end despite ongoing front pressure."
  - "Polymarket logs $21K in 24h, 44% of all-time volume, a sharp attention spike for a geopolitical contract."
  - "Fresh volume on a low-probability war contract often precedes or follows a notable battlefield development or intelligence report."
  - "Resolves December 31, 2026."
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
      poly_vol_24h_usd: 21253.2
sources:
  - label: "ClearMarket market record: Will Russia capture Prymorske in 2026? (multi-deadline "
    url: "https://clearmarket.fyi/events/will-russia-capture-prymorske-by"
    retrieved_at: "2026-08-29T13:34:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 44% all-time volume day on a 7% geopolitical contract warrants monitoring, volume into low-odds war markets frequently leads news, and a desk tracking Ukraine exposure should watch for confirming ground reports.
