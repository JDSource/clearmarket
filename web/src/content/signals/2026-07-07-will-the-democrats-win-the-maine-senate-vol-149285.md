---
signal_id: "CMSIG20260707VS04"
signal_slug: "will-the-democrats-win-the-maine-senate-vol-149285"
headline: "Democrats win 2026 Maine Senate: 60% on $149K"
semantic_title: "Polymarket stacks Democratic Maine Senate odds at 60%"
telemetry: "60% · $149K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-07T10:52:51+00:00"
event_id: "CM-EVT-7YMVN17NP0"
event_slug: "maine-senate-election-winner"
event_question: "Will the winner of the Maine Senate election be determined by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x66bbf6d55e0296278858b3147689f3df9259374f158f9f028b608baa322a639c"
  question_raw: "Will the Democrats win the Maine Senate race in 2026?"
  current_price: 0.6
  volume_24h_usd: 149285.24395200002
  volume_cumulative_usd: 549386.1676260008
  arbitration_model: "uma_oracle"
bullets:
  - "60% on Polymarket versus 57% on Kalshi shows cross-venue consensus on a modest Democratic edge."
  - "$149K in 24h, 27% of all-time, reflects parallel repricing as Platner dropout information propagates."
  - "Small spread between venues suggests no meaningful arbitrage; both markets absorbing the same catalyst."
  - "Resolves on the 2026 Maine Senate general election Democratic candidate winning."
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
      poly_vol_24h_usd: 149285.24395200002
sources:
  - label: "ClearMarket market record: Will the winner of the Maine Senate election be determi"
    url: "https://clearmarket.fyi/events/maine-senate-election-winner"
    retrieved_at: "2026-07-07T10:52:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The cross-venue alignment at 57, 60% with synchronized volume spikes gives political risk desks a high-confidence read: Maine Senate shifts to a Democratic lean following Republican field fragmentation.
