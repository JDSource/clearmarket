---
signal_id: "CMSIG20260724VS00"
signal_slug: "mitch-mcconnell-steps-down-from-senate-b-vol-229639"
headline: "McConnell Senate exit: 41% on $230K surge"
semantic_title: "Heavy trading backs McConnell Senate exit at 41%"
telemetry: "41% · $230K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-24T10:14:05+00:00"
event_id: "CM-EVT-9DBYNLBPG3"
event_slug: "will-mitch-mcconnell-resign-from-the-senate-before-his-term-ends"
event_question: "Will Mitch McConnell step down from the Senate before his term ends?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x15d2e66dcf1d63c5695d6d0e9e2f8e06dd246d00fd5dfc254f2b22baa33bfa1b"
  question_raw: "Mitch McConnell steps down from Senate before his term ends?"
  current_price: 0.41
  volume_24h_usd: 229639.04661000005
  volume_cumulative_usd: 703632.9274129998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-03T00:00:00Z"
bullets:
  - "Market prices a 41% chance McConnell vacates his seat before term ends, near coin-flip territory."
  - "Polymarket logs $230K in 24h, equal to 33% of all-time volume, a sharp single-session concentration."
  - "Fresh attention on a sitting senator's tenure signals traders are pricing real near-term event risk."
  - "Resolves YES if McConnell formally steps down before his Senate term expires."
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
      poly_vol_24h_usd: 229639.04661000005
sources:
  - label: "ClearMarket market record: Will Mitch McConnell step down from the Senate before h"
    url: "https://clearmarket.fyi/events/will-mitch-mcconnell-resign-from-the-senate-before-his-term-ends"
    retrieved_at: "2026-07-24T10:14:05+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-third all-time volume flush into a 41% price means desks are treating a McConnell departure as a live, near-term political risk worth active hedging today.
