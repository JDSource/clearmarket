---
signal_id: "CMSIG20261106VS00"
signal_slug: "will-marco-rubio-leave-the-trump-adminis-vol-147052"
headline: "Rubio exit before 2027: 15% on $147K surge"
semantic_title: "Rubio stays put: long-shot exit odds hold through a volume surge"
telemetry: "15% · $147K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T15:37:54+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48a3e95c0bc1b9305e56445a7affcb857fd61e0ae0d78a4778310a1108ceb08a"
  question_raw: "Will Marco Rubio leave the Trump administration before 2027?"
  current_price: 0.15
  volume_24h_usd: 147052.89801899996
  volume_cumulative_usd: 179836.174245
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "At 15%, Polymarket sees Rubio departure before year-end as a tail risk, not a base case."
  - "$147K traded in 24h, 82% of all-time volume, signaling near-total fresh engagement today."
  - "Surge implies a catalyst rumor or news cycle driving urgent position-taking on his tenure."
  - "Resolves before Jan 1, 2027; proximity to deadline compresses the window and lifts urgency."
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
      poly_vol_24h_usd: 147052.89801899996
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-06T15:37:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 82% single-day share of all-time volume on a 15% contract is a strong signal that a specific rumor or report is driving hedged positioning on Rubio's near-term departure, a desk should monitor State Department coverage closely.
