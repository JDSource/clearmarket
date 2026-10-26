---
signal_id: "CMSIG20261026VS02"
signal_slug: "will-the-democratic-party-win-the-nc-09-vol-44586"
headline: "Dem NC-09 House seat: 30% on $44K surge"
semantic_title: "Fresh volume returns to Democrats' chances in NC-09 House contest"
telemetry: "30% · $45K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T07:48:41+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdc23b5a54616abf57d7f89f57a29dbacc0d836ab6f3994f5533c8c41ba929ebb"
  question_raw: "Will the Democratic Party win the NC-09 House seat?"
  current_price: 0.3
  volume_24h_usd: 44586.85713899999
  volume_cumulative_usd: 89211.424491
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Democrats priced at 30% in NC-09, competitive but still the underdog position."
  - "24h volume equals 50% of all-time, meaning half of all trading arrived in one session."
  - "Sudden attention in a mid-cycle House race often precedes a polling release or candidate news."
  - "Resolves on the NC-09 general election result."
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
      poly_vol_24h_usd: 44586.85713899999
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-26T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of lifetime volume in a single day on a 30% underdog contract is a strong attention signal, a desk should monitor for a NC-09 poll drop or opposition research event driving the imbalance.
