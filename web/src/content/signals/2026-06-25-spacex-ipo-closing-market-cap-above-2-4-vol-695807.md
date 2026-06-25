---
signal_id: "CMSIG20260625VS05"
signal_slug: "spacex-ipo-closing-market-cap-above-2-4-vol-695807"
headline: "SpaceX IPO above $2.4T: 21% on $696K"
semantic_title: "Tail-risk capital targets SpaceX valuation above $2.4T"
telemetry: "21% · $696K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-25T10:39:33+00:00"
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
  - "Polymarket prices $2.4T at 21%, a meaningful tail, not dismissed, but firmly outside the base case."
  - "42% of all-time volume in 24h reflects active speculation on an upside IPO valuation surprise."
  - "A $2.4T print would require exceptional bookbuild demand or a strategic anchor investor at elevated terms."
  - "Resolves against closing market cap; the 21% price implies roughly 4-to-1 odds against this threshold."
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
    retrieved_at: "2026-06-25T10:39:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume here signals that a non-trivial subset of capital is positioned for an IPO blowout scenario, a desk tracking IPO risk should monitor this contract as a live sentiment gauge for bullish valuation drift.
