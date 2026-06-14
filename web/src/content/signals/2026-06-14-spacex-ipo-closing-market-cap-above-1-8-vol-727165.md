---
signal_id: "CMSIG20260614VS04"
signal_slug: "spacex-ipo-closing-market-cap-above-1-8-vol-727165"
headline: "SpaceX IPO above $1.8T: 98% on $727K volume"
semantic_title: "Traders pile into SpaceX IPO cap above $1.8T as near-certainty"
telemetry: "98% · $727K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-14T10:48:10+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd4d841659e8b1fe050980ec9b7deae31accc10e529082fe9468ef9699d11aec2"
  question_raw: "SpaceX IPO closing market cap above $1.8T?"
  current_price: 0.982
  volume_24h_usd: 727165.1358640001
  volume_cumulative_usd: 1800066.6684309978
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket prices $1.8T-plus SpaceX IPO cap at 98%, effectively a resolved lower bound."
  - "24h volume of $727K is 40% of all-time; fresh capital locking in the floor with high conviction."
  - "At 98%, remaining activity is arbitrage and hedging against catastrophic IPO failure scenarios."
  - "Part of a five-contract ladder; this strike is the consensus anchor for the entire structure."
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
      poly_vol_24h_usd: 727165.1358640001
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-14T10:48:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sub-$1.8T is priced as near-impossible; a desk can use this contract as a near-cash equivalent within a SpaceX IPO hedging structure and focus risk budget on the $2.2T, $2.4T spread.
