---
signal_id: "CMSIG20260921VS01"
signal_slug: "will-new-people-nl-gain-the-most-seats-vol-1484721"
headline: "New People most seats: 0% on $1.5M volume"
semantic_title: "New People winning the Duma stays a 0% long shot"
telemetry: "0% · $1.5M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T07:48:00+00:00"
event_id: "CM-EVT-XS1TS19GP7"
event_slug: "which-party-will-gain-most-seats-in-russian-parliamentary-election"
event_question: "Which party will gain the most seats in the Russian Parliamentary Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc9615bb82d6535d630ff98e8094060bc767d8b9446516e98f84d2001a35e50e7"
  question_raw: "Will New People (NL) gain the most seats in the next Russian parliamentary election?"
  current_price: 0.002
  volume_24h_usd: 1484721.4055420002
  volume_cumulative_usd: 5896828.370803001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices New People (NL) at 0% to lead the Duma, the market sees no path."
  - "25% of all-time volume traded in 24h, mirroring the United Russia flush on the same election."
  - "Coordinated volume across the Russian parliamentary suite suggests settlement or bloc positioning."
  - "Resolves on official seat count from the next Russian parliamentary election."
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
      poly_vol_24h_usd: 1484721.4055420002
sources:
  - label: "ClearMarket market record: Which party will gain the most seats in the Russian Par"
    url: "https://clearmarket.fyi/events/which-party-will-gain-most-seats-in-russian-parliamentary-election"
    retrieved_at: "2026-09-21T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired with the United Russia spike, this 0% flush confirms the market is clearing paired legs of the same election, desks should treat both as position close-out flow rather than new directional bets.
