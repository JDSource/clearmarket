---
signal_id: "CMSIG20261119VS01"
signal_slug: "will-anthropic-s-market-cap-be-between-vol-581747"
headline: "Anthropic $1.5T, $1.75T band: 16% on $582K"
semantic_title: "Heavy trading tests the $1.5T, $1.75T Anthropic band"
telemetry: "16% · $582K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-19T07:48:32+00:00"
event_id: "CM-EVT-JCL1Q35R76"
event_slug: "anthropic-ipo-closing-market-cap-higher-strikes"
event_question: "Will Anthropic's IPO closing market cap exceed $100 billion?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe02dadd92c84112fce087b6f260d62c8df1648e071acaef35b0851c8dde64163"
  question_raw: "Will Anthropic's market cap be between $1.5T and $1.75T at market close on IPO day?"
  current_price: 0.158
  volume_24h_usd: 581747.8023060001
  volume_cumulative_usd: 1657821.434769
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T23:55:00Z"
bullets:
  - "16% implies the $1.5T, $1.75T close is plausible but not the central case, roughly one-in-six odds."
  - "$582K in 24h volume equals 35% of all-time flow, marking this as a high-conviction positioning session."
  - "Volume clustering across adjacent bands ($1.25T, $1.5T, $1.75T) points to active spread-trading around IPO pricing uncertainty."
  - "Resolves at IPO-day market close; part of Polymarket's Anthropic valuation suite."
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
      poly_vol_24h_usd: 581747.8023060001
sources:
  - label: "ClearMarket market record: Will Anthropic's IPO closing market cap exceed $100 bil"
    url: "https://clearmarket.fyi/events/anthropic-ipo-closing-market-cap-higher-strikes"
    retrieved_at: "2026-11-19T07:48:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concentrated flow in the mid-range band suggests the market is mapping probability mass across a wide valuation corridor rather than converging on a single outcome, useful input for IPO allocation sizing.
