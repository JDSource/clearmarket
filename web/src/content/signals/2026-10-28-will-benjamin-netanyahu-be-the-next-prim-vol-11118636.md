---
signal_id: "CMSIG20261028VS00"
signal_slug: "will-benjamin-netanyahu-be-the-next-prim-vol-11118636"
headline: "Netanyahu next PM: 46% on $11M volume surge"
semantic_title: "Netanyahu's return to PM odds sit below 50%"
telemetry: "46% · $11.1M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T14:50:28+00:00"
event_id: "CM-EVT-05G08PPSM2"
event_slug: "who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
event_question: "Who will be the next Prime Minister of Israel after the next election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7586a96520578acaaaa4ea84a2582f197f84255da1f3392a7aa300386c187b37"
  question_raw: "Will Benjamin Netanyahu be the next Prime Minister of Israel?"
  current_price: 0.46
  volume_24h_usd: 11118636.021178002
  volume_cumulative_usd: 26875268.117406
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Netanyahu below 50%, a near-coin-flip on his political comeback."
  - "24h volume of $11.1M is 41% of all-time flow, signaling a concentrated burst of fresh attention."
  - "Israeli election cycle is drawing peak engagement; odds below even suggest the race is genuinely contested."
  - "Resolves on confirmation of next Israeli Prime Minister."
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
      poly_vol_24h_usd: 11118636.021178002
sources:
  - label: "ClearMarket market record: Who will be the next Prime Minister of Israel after the"
    url: "https://clearmarket.fyi/events/who-will-be-the-next-prime-minister-of-israel-after-the-next-election"
    retrieved_at: "2026-10-28T14:50:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-even split at massive volume signals desks are actively hedging Israeli political risk with no clear directional consensus.
