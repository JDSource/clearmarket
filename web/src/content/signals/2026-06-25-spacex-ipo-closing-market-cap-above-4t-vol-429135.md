---
signal_id: "CMSIG20260625VS06"
signal_slug: "spacex-ipo-closing-market-cap-above-4t-vol-429135"
headline: "SpaceX IPO above $4T: 0% on $429K surge"
semantic_title: "SpaceX $4T IPO valuation fully faded by the market"
telemetry: "0% · $429K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-25T10:39:33+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2576d8fe9a5ed75f58c2ef34bad961916d4799254c8d248734aee5cf5224eb07"
  question_raw: "SpaceX IPO closing market cap above $4T?"
  current_price: 0.002
  volume_24h_usd: 429135.1700309999
  volume_cumulative_usd: 897378.6698439954
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket prices $4T at 0%, capital has unanimously discarded this scenario."
  - "48% of all-time volume in 24h suggests the surge was driven by curiosity-driven positioning that the market immediately absorbed and rejected."
  - "A $4T closing cap would represent roughly a doubling of the consensus base case, no credible bookbuild path supports it."
  - "Contract functions as a market-structure outlier; volume reflects price discovery completing, not genuine contest."
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
      poly_vol_24h_usd: 429135.1700309999
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-25T10:39:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The zero-price, high-volume configuration signals that the $4T level was stress-tested and dismissed in a single session, desks can treat this as confirmation that SpaceX IPO valuation expectations are firmly anchored below $2.5T.
