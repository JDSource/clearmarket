---
signal_id: "CMSIG20261119VS00"
signal_slug: "will-anthropic-s-market-cap-be-less-than-vol-1198191"
headline: "Anthropic IPO sub-$1.25T: 27% on $1.2M surge"
semantic_title: "Traders back a sub-$1.25T Anthropic IPO open"
telemetry: "27% · $1.2M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-19T07:48:32+00:00"
event_id: "CM-EVT-JCL1Q35R76"
event_slug: "anthropic-ipo-closing-market-cap-higher-strikes"
event_question: "Will Anthropic's IPO closing market cap exceed $100 billion?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x800376dc64e4e2376a495ed0df4a789192256c821bb4d1452acdd5931bca2fa5"
  question_raw: "Will Anthropic's market cap be less than $1.25T at market close on IPO day?"
  current_price: 0.27
  volume_24h_usd: 1198191.4967150001
  volume_cumulative_usd: 3093956.431844
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T23:55:00Z"
bullets:
  - "27% odds say Anthropic closes IPO day below $1.25T, a modest debut relative to its last private valuation."
  - "39% of all-time volume hit in 24h ($1.2M), the heaviest single-day flow on this contract by a wide margin."
  - "Fresh positioning across the full IPO valuation ladder suggests a market event is imminent or newly confirmed."
  - "Resolves at IPO-day close; contract is the anchor of a multi-band suite covering $0.6T through $3.0T+."
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
      poly_vol_24h_usd: 1198191.4967150001
sources:
  - label: "ClearMarket market record: Will Anthropic's IPO closing market cap exceed $100 bil"
    url: "https://clearmarket.fyi/events/anthropic-ipo-closing-market-cap-higher-strikes"
    retrieved_at: "2026-11-19T07:48:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The heaviest flow on the sub-$1.25T band signals desks are actively hedging downside IPO pricing risk and treating a conservative open as a live scenario worth pricing in size.
