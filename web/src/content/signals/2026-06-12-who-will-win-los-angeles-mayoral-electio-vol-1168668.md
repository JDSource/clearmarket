---
signal_id: "CMSIG20260612VS03"
signal_slug: "who-will-win-los-angeles-mayoral-electio-vol-1168668"
headline: "LA mayoral race: 79% on $1.2M inflow"
semantic_title: "Heavy flows defend Bass as Los Angeles mayor favorite"
telemetry: "79% · $1.2M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-12T11:42:43+00:00"
event_id: "CM-EVT-X27NWLJN20"
event_slug: "kxmayorla-26"
event_question: "Will there be a Los Angeles Mayor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMAYORLA-26-KBAS"
  question_raw: "Who will win Los Angeles Mayoral Election?"
  current_price: 0.79
  volume_24h_usd: 1168668.91
  volume_cumulative_usd: 4455417.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-06-02T14:00:00Z"
bullets:
  - "79% on Bass signals strong but not conclusive market confidence heading into the election."
  - "$1.2M in 24h is 26% of all-time, sustained interest, not a one-off spike."
  - "Volume acceleration suggests new polling, endorsement, or opposition research in play."
  - "Resolves on official LA mayoral election result."
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
      kalshi_vol_24h_usd: 1168668.91
sources:
  - label: "ClearMarket market record: Will there be a Los Angeles Mayor winner?"
    url: "https://clearmarket.fyi/events/kxmayorla-26"
    retrieved_at: "2026-06-12T11:42:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should watch for complementary nominee contract movement, split flows between this market and the nominee confirmation contract would indicate traders hedging Bass's win probability against ballot uncertainty.
