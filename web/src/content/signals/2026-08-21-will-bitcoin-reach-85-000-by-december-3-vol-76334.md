---
signal_id: "CMSIG20260821VS06"
signal_slug: "will-bitcoin-reach-85-000-by-december-3-vol-76334"
headline: "Bitcoin $85K by Dec 31: 59% on $76K surge"
semantic_title: "Bitcoin reaching $85K by year-end stays the base case"
telemetry: "59% · $76K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-21T08:35:56+00:00"
event_id: "CM-EVT-2S263KKBP2"
event_slug: "what-price-will-bitcoin-hit-before-2027"
event_question: "What price will Bitcoin reach by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1239389645c8a73b170b78ef3a83d69b6cf1d2711d412829ea8836660b08fc93"
  question_raw: "Will Bitcoin reach $85,000 by December 31, 2026?"
  current_price: 0.59
  volume_24h_usd: 76334.71806900001
  volume_cumulative_usd: 290761.52845600003
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "At 59%, Polymarket prices a year-end $85K Bitcoin as the slight favorite, consensus leans bullish but not confidently."
  - "24h volume of $76K is 26% of all-time; less concentrated than the August strikes but meaningful for a longer-dated claim."
  - "With Bitcoin already near the $80K range, the $85K target requires only a modest additional rally through December."
  - "Resolves Dec 31, 2026; complements the August BTC ladder by extending the market's directional outlook four months."
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
      poly_vol_24h_usd: 76334.71806900001
sources:
  - label: "ClearMarket market record: What price will Bitcoin reach by the end of 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-before-2027"
    retrieved_at: "2026-08-21T08:35:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume holding 59% on a $85K year-end target tells desks the market sees current BTC levels as a platform for further gains, but conviction is moderate, not the strong lean seen on the August contracts.
