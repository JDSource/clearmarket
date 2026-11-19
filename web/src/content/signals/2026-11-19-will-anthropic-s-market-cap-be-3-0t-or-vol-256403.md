---
signal_id: "CMSIG20261119VS03"
signal_slug: "will-anthropic-s-market-cap-be-3-0t-or-vol-256403"
headline: "Anthropic $3.0T+ IPO close: 0% on $256K surge"
semantic_title: "A $3.0T-or-greater Anthropic debut is priced out"
telemetry: "0% · $256K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-19T07:48:32+00:00"
event_id: "CM-EVT-JCL1Q35R76"
event_slug: "anthropic-ipo-closing-market-cap-higher-strikes"
event_question: "Will Anthropic's IPO closing market cap exceed $100 billion?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb0d2fa1aacbf2e91248f2d69d9364e6ef644177de0141e23313c5b2a28f5cf60"
  question_raw: "Will Anthropic's market cap be $3.0T or greater at market close on IPO day?"
  current_price: 0.002
  volume_24h_usd: 256403.79520899997
  volume_cumulative_usd: 740603.3336159999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T23:55:00Z"
bullets:
  - "0% odds, the market has effectively ruled out Anthropic closing IPO day at $3.0T or above."
  - "$256K in 24h is 35% of all-time volume; fresh flow is confirming, not challenging, the near-zero price."
  - "Volume at zero likely reflects late traders closing residual positions or completing cross-band spread books."
  - "Resolves at IPO-day close; the extreme upside band of Polymarket's Anthropic suite."
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
      poly_vol_24h_usd: 256403.79520899997
sources:
  - label: "ClearMarket market record: Will Anthropic's IPO closing market cap exceed $100 bil"
    url: "https://clearmarket.fyi/events/anthropic-ipo-closing-market-cap-higher-strikes"
    retrieved_at: "2026-11-19T07:48:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Active volume into a zero-priced contract signals spread clean-up and position squaring rather than new directional bets, the $3T+ scenario is off the table as a live risk for allocation purposes.
