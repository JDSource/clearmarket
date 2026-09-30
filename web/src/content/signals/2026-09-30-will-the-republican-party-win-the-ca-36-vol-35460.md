---
signal_id: "CMSIG20260930VS04"
signal_slug: "will-the-republican-party-win-the-ca-36-vol-35460"
headline: "GOP CA-36: 4% on $35K volume spike"
semantic_title: "CA-36 Republican win stays a long shot at 4%"
telemetry: "4% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T14:33:50+00:00"
event_id: "CM-EVT-T5L606P9D2"
event_slug: "ca-36-house-election-winner"
event_question: "Will the winner of the California's 36th congressional district House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x20e049d4e1df60bbb782882618d5808bfc485eb283d61027f04755f5e6ba7592"
  question_raw: "Will the Republican Party win the CA-36 House seat?"
  current_price: 0.04
  volume_24h_usd: 35460.0
  volume_cumulative_usd: 79559.344238
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Republican win in CA-36 at just 4%, the Democratic incumbent is overwhelming favorite."
  - "24h volume of $35K is 45% of all-time, the largest single-day turnover yet on this contract."
  - "A surge into a near-zero contract often precedes a known catalyst; fresh attention warrants monitoring."
  - "Resolves on the 2026 CA-36 House general election result."
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
      poly_vol_24h_usd: 35460.0
sources:
  - label: "ClearMarket market record: Will the winner of the California's 36th congressional "
    url: "https://clearmarket.fyi/events/ca-36-house-election-winner"
    retrieved_at: "2026-09-30T14:33:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High volume share into a 4% contract is a flag for desks, either opportunistic fade trading or an early signal that a development is circulating before it hits headlines.
