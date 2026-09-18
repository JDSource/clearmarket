---
signal_id: "CMSIG20260918VS01"
signal_slug: "will-spd-win-the-most-seats-in-the-2026-vol-186070"
headline: "SPD MV plurality: 50% on $186K inflow"
semantic_title: "SPD plurality odds hold at 50% through a volume surge"
telemetry: "50% · $186K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-18T12:39:43+00:00"
event_id: "CM-EVT-N815VR9GY5"
event_slug: "mecklenburg-vorpommern-parliamentary-election-winner"
event_question: "Will the SPD win the most seats in the Mecklenburg-Vorpommern state parliament election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7742a04b33fb5a5b15474a7c70f3c073922c1f471bddc66ceb01c1ffd1841829"
  question_raw: "Will SPD win the most seats in the 2026 Mecklenburg-Vorpommern parliamentary elections?"
  current_price: 0.5
  volume_24h_usd: 186070.64316500002
  volume_cumulative_usd: 579813.251804
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "50% price is the market's version of a coin-flip, SPD and AfD are priced as dead-level rivals."
  - "32% of all-time volume in 24 hours underscores how rapidly conviction is being tested pre-vote."
  - "Paired with Spike 0, the two contracts together imply no dominant favorite heading into election day."
  - "Resolves on certified seat totals from the Mecklenburg-Vorpommern state parliament."
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
      poly_vol_24h_usd: 186070.64316500002
sources:
  - label: "ClearMarket market record: Will the SPD win the most seats in the Mecklenburg-Vorp"
    url: "https://clearmarket.fyi/events/mecklenburg-vorpommern-parliamentary-election-winner"
    retrieved_at: "2026-09-18T12:39:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With both AfD and SPD contracts trading near 50% on simultaneous volume spikes, a desk should treat the Mecklenburg-Vorpommern result as a binary risk event with no priced edge.
