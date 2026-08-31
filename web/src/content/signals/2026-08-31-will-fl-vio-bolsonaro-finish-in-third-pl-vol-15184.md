---
signal_id: "CMSIG20260831VS05"
signal_slug: "will-fl-vio-bolsonaro-finish-in-third-pl-vol-15184"
headline: "Bolsonaro F. 3rd place R1 Brazil: 1% on $15K"
semantic_title: "Flávio Bolsonaro third-place finish stays a long shot at 1%"
telemetry: "1% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-31T15:48:06+00:00"
event_id: "CM-EVT-MQHJWNSWH5"
event_slug: "brazil-presidential-election-first-round-3rd-place"
event_question: "Will the third-place finisher in the first round of the Brazil presidential election receive more than 10% of the vote?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6be36f266340255dd19e09482da15b256ec51bd478309d667495645fde253a22"
  question_raw: "Will Flávio Bolsonaro finish in third place in the first round of the 2026 Brazilian presidential election?"
  current_price: 0.011
  volume_24h_usd: 15184.190637
  volume_cumulative_usd: 58826.06623699998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Flávio Bolsonaro finishing third in Brazil's first round at just 1%, near-zero probability."
  - "24h volume of $15.2K is 26% of all-time, a notable but not dominant share of the contract's history."
  - "Volume at 1% suggests traders are either hedging a tail or closing out speculative long positions."
  - "Resolves on official Brazilian first-round vote counts in October 2026."
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
      poly_vol_24h_usd: 15184.190637
sources:
  - label: "ClearMarket market record: Will the third-place finisher in the first round of the"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-3rd-place"
    retrieved_at: "2026-08-31T15:48:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 1% contract is a tail-risk signal, a desk tracking Brazilian political risk should assess whether new polling or a coalition shift is prompting the activity, even at these extreme odds.
