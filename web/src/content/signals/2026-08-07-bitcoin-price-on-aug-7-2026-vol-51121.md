---
signal_id: "CMSIG20260807VS05"
signal_slug: "bitcoin-price-on-aug-7-2026-vol-51121"
headline: "BTC Aug 7 mid-range: 51% on $51K inflow"
semantic_title: "Bitcoin Aug 7 mid-range contract sits near 50% on fresh volume"
telemetry: "51% · $51K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-07T08:54:29+00:00"
event_id: "CM-EVT-PFHRR5PCZ2"
event_slug: "kxbtcd-26aug0717"
event_question: "Bitcoin price, August 7, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCD-26AUG0717-T64499.99"
  question_raw: "Bitcoin price on Aug 7, 2026?"
  current_price: 0.51
  volume_24h_usd: 51121.69
  volume_cumulative_usd: 104116.36
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-14T21:00:00Z"
bullets:
  - "51% price on the mid-range bracket shows a near-coin-flip on today's Bitcoin close level."
  - "$51K in 24h is 49% of all-time volume, almost the entire contract history trading today."
  - "Companion spike in the upper-range contract (Spike 4) suggests layered bracket positioning."
  - "Resolves on Bitcoin's official price at end of August 7, 2026."
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
      kalshi_vol_24h_usd: 51121.69
sources:
  - label: "ClearMarket market record: Bitcoin price, August 7, 2026"
    url: "https://clearmarket.fyi/events/kxbtcd-26aug0717"
    retrieved_at: "2026-08-07T08:54:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume printing at 51% on a same-day bracket suggests active spread trading across adjacent Bitcoin price tiers, a crypto desk should map all related brackets before acting.
