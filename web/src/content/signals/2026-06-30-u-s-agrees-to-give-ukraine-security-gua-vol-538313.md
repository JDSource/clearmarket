---
signal_id: "CMSIG20260630VS01"
signal_slug: "u-s-agrees-to-give-ukraine-security-gua-vol-538313"
headline: "Ukraine security guarantee: 0% on $538K final surge"
semantic_title: "Capital writes off a U.S.-Ukraine security deal by June 30"
telemetry: "0% · $538K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-30T10:55:12+00:00"
event_id: "CM-EVT-XJ07DRZ1S1"
event_slug: "us-agrees-to-give-ukraine-security-guarantee-by-june-30"
event_question: "Will the U.S. agree to give Ukraine a security guarantee by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2a991c78fc614786691a47c0ac0321dd60a0fa4b475c91cbf7c2ec14bb5e6823"
  question_raw: "U.S. agrees to give Ukraine security guarantee by June 30? "
  current_price: 0.003
  volume_24h_usd: 538313.652701
  volume_cumulative_usd: 709549.1212510002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket at 0%, market has fully abandoned any chance of a deal by today."
  - "24h volume $538K is 76% of all-time, the heaviest single-day flush on record."
  - "Contract expires today; late volume is pure settlement redemption, not new positioning."
  - "Resolves June 30; zero price confirms no formal guarantee materialized."
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
      poly_vol_24h_usd: 538313.652701
sources:
  - label: "ClearMarket market record: Will the U.S. agree to give Ukraine a security guarante"
    url: "https://clearmarket.fyi/events/us-agrees-to-give-ukraine-security-guarantee-by-june-30"
    retrieved_at: "2026-06-30T10:55:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 76% all-time volume share at 0% on expiry day tells a desk this is clean settlement flow, a geopolitical milestone the market priced out months ago is now officially closed.
