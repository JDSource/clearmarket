---
signal_id: "CMSIG20261028VS00"
signal_slug: "will-benjamin-netanyahu-be-the-next-prim-vol-11041373"
headline: "Netanyahu next PM: 47% on $11M surge"
semantic_title: "Netanyahu PM odds split near 50% on massive volume"
telemetry: "47% · $11M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T15:35:02+00:00"
event_id: "CM-EVT-05G08PPSM2"
event_slug: "who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
event_question: "Who will be the next Prime Minister of Israel after the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7586a96520578acaaaa4ea84a2582f197f84255da1f3392a7aa300386c187b37"
  question_raw: "Will Benjamin Netanyahu be the next Prime Minister of Israel?"
  current_price: 0.47
  volume_24h_usd: 11041373.274643004
  volume_cumulative_usd: 26978407.301709
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Netanyahu's return to PM at 47%, a near-coin-flip with no clear lean."
  - "24h volume of $11M equals 41% of all-time handle, signaling an exceptional capital rush."
  - "Fresh attention likely tied to Israeli election developments or coalition-forming news breaking now."
  - "Contract resolves on whether Netanyahu holds the PM role after the next government is formed."
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
      poly_vol_24h_usd: 11041373.274643004
sources:
  - label: "ClearMarket market record: Who will be the next Prime Minister of Israel after the"
    url: "https://clearmarket.fyi/events/who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
    retrieved_at: "2026-10-28T15:35:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-even split on $11M in a single session flags acute uncertainty on Israeli government formation, desks should treat this as a live geopolitical event risk, not a settled call.
