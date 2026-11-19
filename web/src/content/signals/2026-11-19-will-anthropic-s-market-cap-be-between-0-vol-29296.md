---
signal_id: "CMSIG20261119VS04"
signal_slug: "will-anthropic-s-market-cap-be-between-0-vol-29296"
headline: "Anthropic $0.6T, $0.9T band: 1% on $29K flow"
semantic_title: "Buyers pass on the $0.6T, $0.9T Anthropic floor band"
telemetry: "1% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-19T07:48:32+00:00"
event_id: "CM-EVT-RLJK2B5DD5"
event_slug: "anthropic-ipo-closing-market-cap-979"
event_question: "Will Anthropic's closing market capitalization at IPO be between $50 billion and $100 billion?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdebea2ab47315c433eaaa36d005e1063a59dc9119ceacfe1c1545407732e25bf"
  question_raw: "Will Anthropic’s market cap be between 0.6T and 0.9T at market close on IPO day by December 31 2027?"
  current_price: 0.008
  volume_24h_usd: 29296.042251000003
  volume_cumulative_usd: 90165.96626700001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "1% odds make a sub-$0.9T Anthropic IPO close a near-consensus impossibility at current pricing."
  - "$29K in 24h is 32% of all-time volume, modest in dollar terms but proportionally in line with the suite."
  - "Negligible probability at the floor band reinforces market confidence that Anthropic prices well above its last private round."
  - "Resolves at IPO-day close; the downside floor contract in Polymarket's full valuation ladder."
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
      poly_vol_24h_usd: 29296.042251000003
sources:
  - label: "ClearMarket market record: Will Anthropic's closing market capitalization at IPO b"
    url: "https://clearmarket.fyi/events/anthropic-ipo-closing-market-cap-979"
    retrieved_at: "2026-11-19T07:48:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Minimal flow and near-zero pricing on the floor band confirm desks see no credible catastrophic-debut scenario, attention and capital are concentrated in the $1.0T, $1.75T range of the suite.
