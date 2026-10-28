---
signal_id: "CMSIG20261028VS00"
signal_slug: "will-benjamin-netanyahu-be-the-next-prim-vol-11556838"
headline: "Netanyahu next Israel PM: 50% on $11.6M spike"
semantic_title: "Netanyahu PM odds sit at 50% through a massive volume surge"
telemetry: "50% · $11.6M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T07:50:03+00:00"
event_id: "CM-EVT-05G08PPSM2"
event_slug: "who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
event_question: "Who will be the next Prime Minister of Israel after the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7586a96520578acaaaa4ea84a2582f197f84255da1f3392a7aa300386c187b37"
  question_raw: "Will Benjamin Netanyahu be the next Prime Minister of Israel?"
  current_price: 0.5
  volume_24h_usd: 11556838.061037004
  volume_cumulative_usd: 25566025.056456003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Even-money pricing signals maximum market uncertainty over Netanyahu's return to power."
  - "Polymarket logged $11.6M in 24h, 45% of all-time volume flooding in at once."
  - "Israeli political landscape in flux; fresh capital is forcing the contract toward resolution."
  - "Resolves on formation of next Israeli government following 2026 elections."
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
      poly_vol_24h_usd: 11556838.061037004
sources:
  - label: "ClearMarket market record: Who will be the next Prime Minister of Israel after the"
    url: "https://clearmarket.fyi/events/who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
    retrieved_at: "2026-10-28T07:50:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $11.6M single-session surge at dead-even odds signals that desks are treating Netanyahu's premiership as a binary live risk, not a settled outcome, position accordingly ahead of coalition talks.
