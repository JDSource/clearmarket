---
signal_id: "CMSIG20260623VS02"
signal_slug: "spacex-ipo-closing-market-cap-above-2-2-vol-722171"
headline: "SpaceX IPO above $2.2T: 67% on $722K flow"
semantic_title: "Traders stack exposure above the $2.2T SpaceX IPO level"
telemetry: "67% · $722K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-23T10:59:55+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x93f2e17cfd239c4667eb3d41ff04e2cd1ae6f3f663210cbc42ec1296ff880805"
  question_raw: "SpaceX IPO closing market cap above $2.2T?"
  current_price: 0.67
  volume_24h_usd: 722171.8124839996
  volume_cumulative_usd: 1298448.1545060014
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 67%, better-than-even odds the closing market cap clears $2.2T."
  - "56% of all-time volume in 24h signals fresh institutional attention as IPO pricing crystallizes."
  - "This strike sits as the key contested band between the 93% ($2T) and 21% ($2.4T) levels."
  - "Resolution ties to IPO closing price; spread across strikes reveals consensus range of $2T, $2.4T."
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
      poly_vol_24h_usd: 722171.8124839996
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-23T10:59:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $2.2T strike is absorbing the most price-discovery flow relative to its history, marking it as the market's contested clearing level for the SpaceX IPO valuation.
