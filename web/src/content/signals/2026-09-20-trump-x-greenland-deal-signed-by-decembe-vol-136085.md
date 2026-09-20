---
signal_id: "CMSIG20260920VS00"
signal_slug: "trump-x-greenland-deal-signed-by-decembe-vol-136085"
headline: "Trump-Greenland deal: 96% on $136K surge"
semantic_title: "Traders back a Greenland deal signed by Dec 31 at 96%"
telemetry: "96% · $136K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T07:47:56+00:00"
event_id: "CM-EVT-M8SXSN1YS7"
event_slug: "trump-x-greenland-deal-signed-by-december-31"
event_question: "Will a Trump-Greenland deal be signed by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a7aed00fae37de19e0b789a6b50a7475ff1afa898c50b9da11ca733a23199fa"
  question_raw: "Trump x Greenland deal signed by December 31?"
  current_price: 0.965
  volume_24h_usd: 136085.760389
  volume_cumulative_usd: 341642.1668580001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "96% odds imply the market treats a signed deal by year-end as near-certain."
  - "$136K traded in 24h, 40% of all-time volume, marks a decisive capital commitment."
  - "Fresh attention likely driven by late-stage diplomatic signals or a reported timeline."
  - "Resolves Dec 31; any credible delay would be a sharp repricing event from this level."
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
      poly_vol_24h_usd: 136085.760389
sources:
  - label: "ClearMarket market record: Will a Trump-Greenland deal be signed by December 31?"
    url: "https://clearmarket.fyi/events/trump-x-greenland-deal-signed-by-december-31"
    retrieved_at: "2026-09-20T07:47:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 96% print absorbing 40% of lifetime volume in a single session signals the desk that this contract is pricing completion as a consensus, making any contrary headline an outsized tail risk.
