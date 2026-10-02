---
signal_id: "CMSIG20261002VS06"
signal_slug: "will-the-republican-party-win-the-va-01-vol-10087"
headline: "GOP wins VA-01: 54% on $10K surge"
semantic_title: "VA-01 House race too close to call as heavy trading tests 54%"
telemetry: "54% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T07:48:52+00:00"
event_id: "CM-EVT-RXRGN4SB51"
event_slug: "va-01-house-election-winner"
event_question: "Will the Virginia 1st Congressional District House election winner be determined by November 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb47f229515c8720ca5ab0bb536f6e6b3fc2041e587179551358503741a1820db"
  question_raw: "Will the Republican Party win the VA-01 House seat?"
  current_price: 0.54
  volume_24h_usd: 10087.899282
  volume_cumulative_usd: 19396.706943999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "54% price puts VA-01 in genuine toss-up territory, with Republicans holding the thinnest of edges."
  - "$10K in 24h is 52% of all-time volume, more than half the contract's lifetime activity arriving in a single session."
  - "A surge at near-50% on a House seat suggests new polling or campaign news is drawing fresh attention to this race."
  - "Resolves on the VA-01 House race result."
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
      poly_vol_24h_usd: 10087.899282
sources:
  - label: "ClearMarket market record: Will the Virginia 1st Congressional District House elec"
    url: "https://clearmarket.fyi/events/va-01-house-election-winner"
    retrieved_at: "2026-10-02T07:48:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

VA-01 sitting at 54% with over half its lifetime volume printing in a day makes this the most live swing-seat signal in the batch, a desk monitoring House control math should flag it as an active variable.
