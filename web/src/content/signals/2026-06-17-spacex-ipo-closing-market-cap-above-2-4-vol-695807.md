---
signal_id: "CMSIG20260617VS05"
signal_slug: "spacex-ipo-closing-market-cap-above-2-4-vol-695807"
headline: "SpaceX IPO above $2.4T: 21% on $696K flow"
semantic_title: "Traders fade the $2.4T SpaceX IPO ceiling at 21%"
telemetry: "21% · $696K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-17T12:14:33+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf471786ca9608b18a61e1f555681428c80ad2a2695fdd2df69e796defff9f897"
  question_raw: "SpaceX IPO closing market cap above $2.4T?"
  current_price: 0.21
  volume_24h_usd: 695807.7482489998
  volume_cumulative_usd: 1650803.9406099995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket at 21%, market assigns long-shot odds to a $2.4T+ opening valuation."
  - "$696K in 24h is 42% of all-time, reflecting active positioning around the upper bound."
  - "Sharp drop from 67% at $2.2T to 21% at $2.4T marks the credible ceiling for debut pricing."
  - "Any bookbuilding news signaling anchor orders above $2.3T would reprice this rapidly."
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
      poly_vol_24h_usd: 695807.7482489998
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-17T12:14:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $2.2T, $2.4T band is where market conviction collapses, a desk should monitor for anchor investor disclosures or pre-IPO secondary prints that could shift this bracket materially.
