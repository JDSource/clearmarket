---
signal_id: "CMSIG20260714VS01"
signal_slug: "will-bitcoin-reach-85-000-by-december-3-vol-25725"
headline: "BTC $85K by Dec 31: 21% on $26K Polymarket flow"
semantic_title: "Bitcoin $85K by year-end sits deep in tail-risk territory"
telemetry: "21% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-14T09:55:02+00:00"
event_id: "CM-EVT-2S263KKBP2"
event_slug: "what-price-will-bitcoin-hit-before-2027"
event_question: "What price will Bitcoin reach by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1239389645c8a73b170b78ef3a83d69b6cf1d2711d412829ea8836660b08fc93"
  question_raw: "Will Bitcoin reach $85,000 by December 31, 2026?"
  current_price: 0.21
  volume_24h_usd: 25725.472724
  volume_cumulative_usd: 73676.41457800001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "21% price tags an $85K Bitcoin by December 31 as a low-probability, tail-risk scenario."
  - "Polymarket records $25,725 in 24h, 35% of all-time volume, marking acute fresh attention."
  - "With BTC well below $85K today, surge may reflect hedgers or speculators opening long-shot positions."
  - "Contract resolves December 31, 2026; ~5.5 months of runway for a major rally required."
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
      poly_vol_24h_usd: 25725.472724
sources:
  - label: "ClearMarket market record: What price will Bitcoin reach by the end of 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-before-2027"
    retrieved_at: "2026-07-14T09:55:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy single-session volume at a low probability level suggests desks are buying optionality rather than conviction, consistent with hedging a crypto rally scenario into year-end.
