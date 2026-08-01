---
signal_id: "CMSIG20260801VS06"
signal_slug: "us-recognizes-russian-sovereignty-over-u-vol-48928"
headline: "US recognizes Russian Ukraine sovereignty: 9% on $49K"
semantic_title: "Odds stay near zero as volume tests US recognition of Russian Ukraine claim"
telemetry: "9% · $49K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-T1H8NR4G99"
event_slug: "us-recognizes-russian-sovereignty-over-ukraine-before-2027"
event_question: "Will the US recognize Russian sovereignty over Ukraine before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4f192d856071c86b7a480c5b0bdd38318ec7be0bf2430784acacbe77bf12fcc9"
  question_raw: "US recognizes Russian sovereignty over Ukraine before 2027?"
  current_price: 0.09
  volume_24h_usd: 48928.86
  volume_cumulative_usd: 184692.16556300005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices only 9% odds the US formally recognizes Russian sovereignty over Ukraine before 2027."
  - "24h volume of $49K is 26% of all-time flow, a moderate but notable acceleration."
  - "Spike likely follows diplomatic reporting, a Trump-Putin contact, peace-framework leak, or Congressional signal, that prompted traders to test the upside."
  - "Resolves before January 1, 2027; five months remain on the contract."
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
      poly_vol_24h_usd: 48928.86
sources:
  - label: "ClearMarket market record: Will the US recognize Russian sovereignty over Ukraine "
    url: "https://clearmarket.fyi/events/us-recognizes-russian-sovereignty-over-ukraine-before-2027"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 9% price holding through a volume test tells a desk that while diplomatic noise is generating attention, the market still treats formal US recognition of Russian territorial gains as a tail risk, not a base case.
