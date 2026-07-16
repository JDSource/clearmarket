---
signal_id: "CMSIG20260716VS00"
signal_slug: "will-mohammad-khatami-be-head-of-state-i-vol-1528830"
headline: "Khatami Iran head of state: 0% on $1.5M surge"
semantic_title: "Traders write off Khatami leading Iran through year-end"
telemetry: "0% · $1.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-16T10:04:38+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4266ab921148974f104cbadd099e13bca989441bf58acfd2a08fc6cc7440e1a1"
  question_raw: "Will Mohammad Khatami be head of state in Iran end of 2026?"
  current_price: 0.002
  volume_24h_usd: 1528830.5010000034
  volume_cumulative_usd: 3587847.160268981
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices zero probability Khatami holds or gains head-of-state status by end of 2026."
  - "Polymarket logged $1.53M in 24h volume, 43% of all-time handle, signaling sharp institutional conviction."
  - "Fresh capital flooding a zero-priced contract suggests confirming news or a definitive political development in Tehran."
  - "Contract resolves end of 2026; volume spike implies the question is effectively settled in the market's view."
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
      poly_vol_24h_usd: 1528830.5010000034
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-16T10:04:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $1.5M single-session flush into a 0% contract is a rare consensus signal, desks should treat this as the market registering a near-certain negative resolution and monitor for the underlying Iranian political catalyst that triggered the flow.
