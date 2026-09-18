---
signal_id: "CMSIG20260918VS04"
signal_slug: "will-united-russia-win-between-325-and-3-vol-30023"
headline: "United Russia 325-339 seats: 41% on $30K surge"
semantic_title: "United Russia 325-339 seat band stays in play at 41%"
telemetry: "41% · $30K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-18T12:39:43+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe62ab836381dd820968f6b58ab546958aaa63de184c48bc6e0522d551807e1b1"
  question_raw: "Will United Russia win between 325 and 339 seats in the next Russian State Duma election?"
  current_price: 0.41
  volume_24h_usd: 30023.161486
  volume_cumulative_usd: 106953.42173400002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "41% price means this specific seat-count band is the single most-likely outcome bracket in the market."
  - "28% of all-time volume in 24 hours suggests renewed attention to Duma election positioning or polling."
  - "The 325-339 range implies a strong United Russia majority but below a constitutional-supermajority threshold."
  - "Resolves on the official certified seat count from the next Russian State Duma election."
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
      poly_vol_24h_usd: 30023.161486
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-09-18T12:39:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume on the modal seat-count bracket signals desks are repricing the Duma outcome distribution, likely in response to new polling or electoral-law developments.
