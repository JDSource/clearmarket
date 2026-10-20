---
signal_id: "CMSIG20261020VS06"
signal_slug: "will-likud-win-35-or-more-seats-in-the-2-vol-22390"
headline: "Likud 35+ seats 2026 election: 0% on $22K volume"
semantic_title: "A Likud supermajority at 35-plus seats is ruled out at 0%"
telemetry: "0% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T07:48:28+00:00"
event_id: "CM-EVT-49Z7YZY008"
event_slug: "israel-election-likud-of-seats"
event_question: "Will Likud win at least 30 seats in the next Israeli election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x78b3aec55f914a149fc110ffd4dcfb008ff94e2df4a451b396f7c14a572d6aa7"
  question_raw: "Will Likud win 35 or more seats in the 2026 Israeli legislative election?"
  current_price: 0.003
  volume_24h_usd: 22390.604833
  volume_cumulative_usd: 67599.293864
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices 0% on Likud winning 35 or more seats in the 2026 Israeli election, the market has effectively closed this outcome."
  - "$22K in 24h is 33% of all-time volume, suggesting traders are actively locking in the zero on this ceiling band."
  - "Zero pricing on the top band while lower bands attract real volume implies a strong polling or coalition signal has capped expectations."
  - "Resolution on official election results; 0% contracts can still attract volume as traders confirm or hedge a closed-out scenario."
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
      poly_vol_24h_usd: 22390.604833
sources:
  - label: "ClearMarket market record: Will Likud win at least 30 seats in the next Israeli el"
    url: "https://clearmarket.fyi/events/israel-election-likud-of-seats"
    retrieved_at: "2026-10-20T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a 0%-priced contract signals desks are using it to actively rule out a Likud supermajority scenario, likely reflecting a specific polling release or coalition arithmetic update.
