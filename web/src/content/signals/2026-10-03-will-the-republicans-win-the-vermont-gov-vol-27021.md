---
signal_id: "CMSIG20261003VS01"
signal_slug: "will-the-republicans-win-the-vermont-gov-vol-27021"
headline: "GOP VT governor: 77% on $27K volume surge"
semantic_title: "Republicans betting picks up on Vermont governor upset"
telemetry: "77% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T07:48:19+00:00"
event_id: "CM-EVT-R85JKZZ4R6"
event_slug: "vermont-governor-winner-2026"
event_question: "Will the Vermont Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6664de877892786b699c552ef88f25ff6e4828f9a847e4f40e4d6d9cd30b1485"
  question_raw: "Will the Republicans win the Vermont governor race in 2026?"
  current_price: 0.77
  volume_24h_usd: 27021.070121
  volume_cumulative_usd: 84725.32565900001
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Vermont Republican gubernatorial win at 77%, a strong favorite in a state that has backed GOP governors recently."
  - "24h volume of $27K is 32% of all-time contract activity, marking a meaningful single-day spike."
  - "Vermont's Republican incumbent history makes 77% defensible, but fresh volume suggests traders are re-evaluating the Democratic challenger's viability."
  - "Resolves on 2026 Vermont general election result."
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
      poly_vol_24h_usd: 27021.070121
sources:
  - label: "ClearMarket market record: Will the Vermont Governor election be won by the Democr"
    url: "https://clearmarket.fyi/events/vermont-governor-winner-2026"
    retrieved_at: "2026-10-03T07:48:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this volume spike as a signal that new polling or candidate news may be circulating ahead of a formal release, Vermont's gubernatorial race is drawing disproportionate attention.
