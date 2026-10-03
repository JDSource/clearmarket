---
signal_id: "CMSIG20261003VS07"
signal_slug: "will-the-democrats-win-the-vermont-gover-vol-22077"
headline: "Vermont Dem governor: 20% on $22K volume spike"
semantic_title: "Democrats stay a long shot in Vermont governor at 20%"
telemetry: "20% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T13:00:25+00:00"
event_id: "CM-EVT-R85JKZZ4R6"
event_slug: "vermont-governor-winner-2026"
event_question: "Will the Vermont Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5dacb3919e3eb6372770cba85c42e0f980ddf18b1a767751de700ee272269233"
  question_raw: "Will the Democrats win the Vermont governor race in 2026?"
  current_price: 0.198
  volume_24h_usd: 22077.695570000003
  volume_cumulative_usd: 79183.50721100005
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 20% for Vermont governor, a clear underdog stance despite the state's blue federal lean."
  - "28% of all-time volume arrived in one session, paired with the Republican Vermont governor spike (Spike 4)."
  - "The 20/79 split across both contracts reflects Vermont's split political identity: blue federally, recently GOP at the state level."
  - "Resolves on the 2026 Vermont gubernatorial election outcome."
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
      poly_vol_24h_usd: 22077.695570000003
sources:
  - label: "ClearMarket market record: Will the Vermont Governor election be won by the Democr"
    url: "https://clearmarket.fyi/events/vermont-governor-winner-2026"
    retrieved_at: "2026-10-03T13:00:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 20% Democratic price with fresh two-sided volume in Vermont governor confirms the market treats this as a GOP-favored race, desks should monitor for candidate announcements or polling that could compress the spread.
