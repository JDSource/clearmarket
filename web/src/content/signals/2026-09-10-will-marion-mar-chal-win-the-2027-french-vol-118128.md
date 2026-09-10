---
signal_id: "CMSIG20260910VS03"
signal_slug: "will-marion-mar-chal-win-the-2027-french-vol-118128"
headline: "Maréchal France 2027: 0% on $118K inflow"
semantic_title: "Maréchal 2027 French presidency draws volume but stays at 0%"
telemetry: "0% · $118K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-10T12:40:48+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf9f40504425133cce159883ca3eaf376a815ab1ae763086ae8e4a3f5eacea479"
  question_raw: "Will Marion Maréchal win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 118128.0
  volume_cumulative_usd: 439489.353
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices Marion Maréchal at 0%, despite $118K in fresh 24-hour activity."
  - "27% of all-time volume arrived in one session, alongside parallel spikes in Castets and Bouamrane markets."
  - "The cross-market French presidential surge, left and right, points to a broad re-pricing of non-incumbent candidates ahead of a likely 2027 field announcement cycle."
  - "Resolves on the 2027 French presidential election."
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
      poly_vol_24h_usd: 118128.0
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-09-10T12:40:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume hitting Maréchal at 0% alongside left-wing candidates suggests traders are actively flushing alternative candidates off the board, useful signal for anyone modeling the French political risk landscape.
