---
signal_id: "CMSIG20260919VS00"
signal_slug: "trump-x-greenland-deal-signed-by-decembe-vol-139988"
headline: "Trump-Greenland deal: 95% on $140K surge"
semantic_title: "Greenland deal by Dec 31 stays a near-certainty"
telemetry: "95% · $140K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-M8SXSN1YS7"
event_slug: "trump-x-greenland-deal-signed-by-december-31"
event_question: "Will a Trump-Greenland deal be signed by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a7aed00fae37de19e0b789a6b50a7475ff1afa898c50b9da11ca733a23199fa"
  question_raw: "Trump x Greenland deal signed by December 31?"
  current_price: 0.954
  volume_24h_usd: 139988.76515099997
  volume_cumulative_usd: 240683.353165
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a signed Trump-Greenland deal by Dec 31 at 95%, near-full conviction."
  - "24h volume of $140K is 58% of all-time handle, making this the dominant session on record."
  - "Surge implies fresh attention tracking an imminent diplomatic or legislative milestone."
  - "Resolves Dec 31, 2026; any credible denial or delay could reprice sharply from these levels."
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
      poly_vol_24h_usd: 139988.76515099997
sources:
  - label: "ClearMarket market record: Will a Trump-Greenland deal be signed by December 31?"
    url: "https://clearmarket.fyi/events/trump-x-greenland-deal-signed-by-december-31"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The concentrated volume at 95% signals desks are treating a formal deal as largely priced in, with residual capital chasing the final 5% tail risk before year-end resolution.
