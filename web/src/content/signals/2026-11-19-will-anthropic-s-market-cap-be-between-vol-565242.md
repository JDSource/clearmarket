---
signal_id: "CMSIG20261119VS02"
signal_slug: "will-anthropic-s-market-cap-be-between-vol-565242"
headline: "Anthropic $1.75T, $2.0T band: 5% on $565K"
semantic_title: "Odds stay low on a $1.75T, $2.0T Anthropic close"
telemetry: "5% · $565K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-19T07:48:32+00:00"
event_id: "CM-EVT-JCL1Q35R76"
event_slug: "anthropic-ipo-closing-market-cap-higher-strikes"
event_question: "Will Anthropic's IPO closing market cap exceed $100 billion?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdded1086ea6aca11f88b997328ff3b0f5bb9374e5ecb450422c862f67c9f3cbe"
  question_raw: "Will Anthropic's market cap be between $1.75T and $2.0T at market close on IPO day?"
  current_price: 0.047
  volume_24h_usd: 565242.5132380001
  volume_cumulative_usd: 1820811.96737
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T23:55:00Z"
bullets:
  - "5% odds place a $1.75T, $2.0T IPO-day close firmly in long-shot territory despite substantial fresh flow."
  - "$565K in 24h equals 31% of all-time volume, elevated activity despite the low headline probability."
  - "High volume at a low price implies traders are either laying the band or hedging tail scenarios in a broader spread."
  - "Resolution is IPO-day close; contract sits in the upper-middle of Polymarket's Anthropic valuation ladder."
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
      poly_vol_24h_usd: 565242.5132380001
sources:
  - label: "ClearMarket market record: Will Anthropic's IPO closing market cap exceed $100 bil"
    url: "https://clearmarket.fyi/events/anthropic-ipo-closing-market-cap-higher-strikes"
    retrieved_at: "2026-11-19T07:48:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Large volume into a 5% contract suggests spread construction rather than directional conviction, desks buying unlikely bands cheaply as part of a full-valuation-range hedge.
