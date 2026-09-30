---
signal_id: "CMSIG20260930VS03"
signal_slug: "will-the-republican-party-win-the-ca-36-vol-35460"
headline: "CA-36 GOP House: 4% on $35K, 45% of all-time"
semantic_title: "CA-36 GOP odds stay near zero as heavy volume tests the 4% floor"
telemetry: "4% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T07:48:11+00:00"
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
  - "Polymarket prices Republicans at just 4% to win California's 36th House seat, a near-certain Democratic hold."
  - "$35K in 24h volume is 45% of all-time contract volume, the single largest activity day by a wide margin."
  - "A near-zero price with surging volume often precedes a news catalyst; attention here may front-run a candidate development."
  - "Contract resolves on the November 2026 CA-36 House general election result."
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
    retrieved_at: "2026-09-30T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When nearly half of all-time volume hits a contract priced at 4%, it warrants scrutiny, either a speculative long-shot bet or early positioning ahead of a candidate or redistricting development in CA-36.
