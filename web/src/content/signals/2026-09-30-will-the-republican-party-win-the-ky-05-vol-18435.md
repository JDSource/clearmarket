---
signal_id: "CMSIG20260930VS06"
signal_slug: "will-the-republican-party-win-the-ky-05-vol-18435"
headline: "GOP KY-05: 97% on $18K volume surge"
semantic_title: "KY-05 Republican win priced as near-certain"
telemetry: "97% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-BL7L8MBY65"
event_slug: "ky-05-house-election-winner"
event_question: "KY-05 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7282c5b2ced91d830069f1dbb54feb75c3088b63035714a0b6d1ed35056e4745"
  question_raw: "Will the Republican Party win the KY-05 House seat?"
  current_price: 0.971
  volume_24h_usd: 18435.299666
  volume_cumulative_usd: 37867.503482
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Republican KY-05 House win at 97%, essentially a resolved outcome in market terms."
  - "24h volume of $18K is 49% of all-time; nearly half of all lifetime trading occurred in one session."
  - "Volume into a 97% contract likely reflects late entrants seeking near-riskless yield on a safe Republican seat."
  - "Resolves on the 2026 KY-05 House general election result."
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
      poly_vol_24h_usd: 18435.299666
sources:
  - label: "ClearMarket market record: KY-05 House Election Winner"
    url: "https://clearmarket.fyi/events/ky-05-house-election-winner"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total volume concentration in a single session on a 97% contract suggests this is yield-harvesting behavior; desks should treat it as a liquidity footnote rather than a signal of changed competitive dynamics.
