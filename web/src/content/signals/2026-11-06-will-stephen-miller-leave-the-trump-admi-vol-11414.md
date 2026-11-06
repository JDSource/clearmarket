---
signal_id: "CMSIG20261106VS03"
signal_slug: "will-stephen-miller-leave-the-trump-admi-vol-11414"
headline: "Stephen Miller exits admin: 19% on $11K surge"
semantic_title: "Miller departure odds stay near 25% on fresh volume"
telemetry: "19% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T07:48:47+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8e2c840905e4089910b2797984e2331e23be0b0071ddcb67c466a120faf05b60"
  question_raw: "Will Stephen Miller leave the Trump administration before 2027?"
  current_price: 0.19
  volume_24h_usd: 11414.853499
  volume_cumulative_usd: 18737.001448
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market puts only a 19% probability on Stephen Miller leaving the Trump administration before 2027, near the Rubio read."
  - "24h volume of $11K is 61% of all-time, suggesting the contract was largely dormant until a specific trigger today."
  - "Likely traded in tandem with the Rubio contract, a broader market sweep on Trump inner-circle departure risk."
  - "Resolves if Miller departs any Trump administration role before January 1, 2027."
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
      poly_vol_24h_usd: 11414.853499
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-06T07:48:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired trading action with the Rubio contract tells a desk that someone is running a basket bet on Trump inner-circle stability, both prices held low, so the flow is stress-testing rather than pricing departures as likely.
