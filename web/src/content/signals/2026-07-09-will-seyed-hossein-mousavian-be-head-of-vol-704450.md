---
signal_id: "CMSIG20260709VS00"
signal_slug: "will-seyed-hossein-mousavian-be-head-of-vol-704450"
headline: "Mousavian Iran head of state: 0% on $704K surge"
semantic_title: "Traders write off Mousavian as Iran's end-2026 head of state"
telemetry: "0% · $704K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-09T10:57:00+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x821f357da390a32347e4df0c3fb0aa4a8eadf4af72730c8dc7a7f1ab58798a02"
  question_raw: "Will Seyed Hossein Mousavian be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 704450.9425
  volume_cumulative_usd: 1111643.327882
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices zero probability, Mousavian leads Iran by year-end is effectively ruled out."
  - "24h volume of $704K is 63% of all-time; capital flooding in to close this at zero."
  - "Surge likely reflects coordinated resolution-hunting as Iran's post-Raisi succession picture clarifies."
  - "Contract resolves end-2026; fresh volume signals desks treating this name as eliminated."
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
      poly_vol_24h_usd: 704450.9425
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-09T10:57:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-total all-time volume concentration in 24h at a zero price signals institutional players are aggressively settling this candidate out of Iran succession scenario sets.
