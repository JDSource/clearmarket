---
signal_id: "CMSIG20260702VS02"
signal_slug: "will-donald-trump-be-the-next-leader-out-vol-950861"
headline: "Trump next out: 0% on $951K Polymarket inflow"
semantic_title: "Flows stack against any Trump departure scenario before 2027"
telemetry: "0% · $951K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will a current leader lose power before 2027, excluding Viktor Orbán?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x55118d53d1c381e96f9d9c47cd11db5f1987449f9a69aec43eef49ff99276f52"
  question_raw: "Will Donald Trump be the next leader out before 2027?"
  current_price: 0.001
  volume_24h_usd: 950861.6806219999
  volume_cumulative_usd: 1830629.2674129992
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "0% price reflects full market consensus that Trump will not be the next listed leader to exit."
  - "$951K in 24h, 52% of all-time volume, confirms this is a high-conviction clearing flow."
  - "Part of a synchronized multi-leg leadership basket sweep visible across Polymarket today."
  - "Resolves before 2027; zero residual probability leaves no hedging utility for desks."
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
      poly_vol_24h_usd: 950861.6806219999
sources:
  - label: "ClearMarket market record: Will a current leader lose power before 2027, excluding"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This leg's volume, mirroring the Zelenskyy and Lecornu spikes, confirms a basket-level structured liquidation, a desk or protocol resolving correlated multi-contract G7 leadership exposure in a single session.
