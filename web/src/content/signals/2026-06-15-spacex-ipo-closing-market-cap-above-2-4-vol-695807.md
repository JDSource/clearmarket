---
signal_id: "CMSIG20260615VS05"
signal_slug: "spacex-ipo-closing-market-cap-above-2-4-vol-695807"
headline: "SpaceX IPO above $2.4T: 21% on $696K volume"
semantic_title: "Market fades SpaceX reaching a $2.4T IPO close"
telemetry: "21% · $696K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-15T13:52:22+00:00"
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
  - "Polymarket prices 21%, majority capital rejects a $2.4T closing valuation."
  - "24h volume $696K is 42% of all-time, reflecting active two-sided positioning at this ceiling strike."
  - "The sharp step from $2.2T (67%) to $2.4T (21%) marks the market's conviction ceiling for the IPO."
  - "Upside surprise in book-building or anchor orders could reprice this level rapidly."
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
    retrieved_at: "2026-06-15T13:52:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $2.4T strike is where conviction breaks sharply, the 46-point gap from $2.2T to $2.4T is the most informative spread in the strip for desks modeling IPO valuation upside scenarios.
