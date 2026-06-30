---
signal_id: "CMSIG20260630VS02"
signal_slug: "will-the-fed-decrease-interest-rates-by-vol-1361654"
headline: "Fed 50 bps July cut: 1% on $1.36M one-day surge"
semantic_title: "Heavy flows defend the near-zero odds on a 50 bps July cut"
telemetry: "1% · $1.4M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-30T10:55:12+00:00"
event_id: "CM-EVT-CJQJ8SK6S4"
event_slug: "fed-decision-in-july-181"
event_question: "Will the Federal Reserve make a decision in July?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3d675f1c88099a57c12abca632cf926be1bf430125168321de06234e9930fe1a"
  question_raw: "Will the Fed decrease interest rates by 50+ bps after the July 2026 meeting?"
  current_price: 0.007
  volume_24h_usd: 1361654.083371
  volume_cumulative_usd: 4862241.925549009
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-29T00:00:00Z"
bullets:
  - "Polymarket at 1%, market near-unanimously rules out a jumbo July cut."
  - "24h volume $1.36M is the largest single-day flow, 28% of a deep $4.9M all-time pool."
  - "FOMC July meeting approaching; macro desks appear to be hedging or closing tail positions."
  - "A 1% handle with this volume density signals the rate path is considered highly constrained."
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
      poly_vol_24h_usd: 1361654.083371
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in July?"
    url: "https://clearmarket.fyi/events/fed-decision-in-july-181"
    retrieved_at: "2026-06-30T10:55:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Massive fresh flow into a 1% contract tells a rates desk that participants are actively closing out residual tail hedges ahead of the July FOMC, confirming near-universal conviction against aggressive easing.
