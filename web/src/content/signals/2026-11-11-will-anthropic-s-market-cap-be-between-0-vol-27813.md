---
signal_id: "CMSIG20261111VS00"
signal_slug: "will-anthropic-s-market-cap-be-between-0-vol-27813"
headline: "Anthropic IPO band: 11% on $27K surge"
semantic_title: "Anthropic IPO day cap in $0.9T, $1.2T band stays a long shot"
telemetry: "11% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-11T07:47:49+00:00"
event_id: "CM-EVT-RLJK2B5DD5"
event_slug: "anthropic-ipo-closing-market-cap-979"
event_question: "Will Anthropic's closing market capitalization at IPO be between $50 billion and $100 billion?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x17459272717ce2de6d4d6aaff53b307381f03c07d44b56e839d38ac2f8b69b3c"
  question_raw: "Will Anthropic’s market cap be between 0.9T and 1.2T at market close on IPO day by December 31 2027?"
  current_price: 0.112
  volume_24h_usd: 27813.05604
  volume_cumulative_usd: 71455.06623799998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Market prices only 11% odds the IPO closes inside the $0.9T, $1.2T range, implying traders expect either a sharply higher or lower debut valuation."
  - "$27.8K in 24h volume equals 39% of all-time contract volume, a rare concentration of fresh attention on a single pricing band."
  - "Surge suggests active positioning ahead of an IPO timeline that remains unconfirmed, attention of this scale typically precedes a credible date signal."
  - "Contract resolves at market close on IPO day; no date is set, so resolution risk itself is part of the trade."
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
      poly_vol_24h_usd: 27813.05604
sources:
  - label: "ClearMarket market record: Will Anthropic's closing market capitalization at IPO b"
    url: "https://clearmarket.fyi/events/anthropic-ipo-closing-market-cap-979"
    retrieved_at: "2026-11-11T07:47:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this spike as a sentiment read on Anthropic's expected debut valuation, the market is aggressively fading the $0.9T, $1.2T band, with live IPO timing speculation driving the volume concentration.
