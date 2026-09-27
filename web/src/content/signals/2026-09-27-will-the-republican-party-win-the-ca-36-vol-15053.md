---
signal_id: "CMSIG20260927VS02"
signal_slug: "will-the-republican-party-win-the-ca-36-vol-15053"
headline: "GOP CA-36 House seat: 4% on $15K volume"
semantic_title: "Republicans face steep odds in CA-36, priced at 4%"
telemetry: "4% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-27T13:31:15+00:00"
event_id: "CM-EVT-T5L606P9D2"
event_slug: "ca-36-house-election-winner"
event_question: "Will the winner of the California's 36th congressional district House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x20e049d4e1df60bbb782882618d5808bfc485eb283d61027f04755f5e6ba7592"
  question_raw: "Will the Republican Party win the CA-36 House seat?"
  current_price: 0.04
  volume_24h_usd: 15053.09
  volume_cumulative_usd: 44099.344238
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Republican win in CA-36 at 4%, effectively ruling out a GOP pickup in this deep-blue district."
  - "24h volume of $15K is 34% of the contract's entire all-time volume, the largest single-day share in this batch."
  - "Heavy trading into a near-zero price suggests either disciplined fading of an outlier scenario or fresh attention ahead of a candidate filing or redistricting development."
  - "Contract resolves on the 2026 CA-36 House general election outcome."
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
      poly_vol_24h_usd: 15053.09
sources:
  - label: "ClearMarket market record: Will the winner of the California's 36th congressional "
    url: "https://clearmarket.fyi/events/ca-36-house-election-winner"
    retrieved_at: "2026-09-27T13:31:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Thirty-four percent of all-time volume in one session on a 4% contract is a notable positioning signal, desks should check for any CA-36 redistricting, candidate, or legal news driving the renewed interest.
