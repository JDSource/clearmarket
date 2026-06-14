---
signal_id: "CMSIG20260614VS05"
signal_slug: "spacex-ipo-closing-market-cap-above-2-4-vol-695807"
headline: "SpaceX IPO above $2.4T: 21% on $696K inflow"
semantic_title: "Flows fade SpaceX IPO cap reaching $2.4T on debut"
telemetry: "21% · $696K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-14T10:48:10+00:00"
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
  - "Polymarket marks SpaceX IPO cap exceeding $2.4T at 21%, clear minority probability."
  - "24h volume of $696K is 42% of all-time; capital actively pressing the upper-band dispute."
  - "The sharp drop from 67% at $2.2T to 21% here reveals where the market sees the valuation ceiling."
  - "Resolves at IPO close; breakout above $2.4T would imply exceptional first-day demand."
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
    retrieved_at: "2026-06-14T10:48:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 21% print at $2.4T anchors the high end of the SpaceX valuation distribution; a desk can use the $2.2T, $2.4T spread to price a covered upside scenario in IPO derivatives.
