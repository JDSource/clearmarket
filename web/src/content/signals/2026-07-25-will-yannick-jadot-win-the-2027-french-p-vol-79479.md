---
signal_id: "CMSIG20260725VS02"
signal_slug: "will-yannick-jadot-win-the-2027-french-p-vol-79479"
headline: "Jadot 2027 French presidency: 0% on $79K surge"
semantic_title: "Jadot 2027 French presidential bid priced out at 0%"
telemetry: "0% · $79K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xae0bce0eab50dc2961c6426b8b4096ff238cbb59408235b629bfbfef3a2c1a12"
  question_raw: "Will Yannick Jadot win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 79479.72700000001
  volume_cumulative_usd: 241382.59158599997
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices Yannick Jadot at 0%, the market has effectively ruled out his path to the Élysée."
  - "$79K in 24h is 33% of all-time volume, a meaningful re-engagement with a contract already near zero."
  - "Volume at a floor price typically reflects either closing of residual positions or traders locking in the near-zero outcome."
  - "French presidential election is scheduled for spring 2027; contract resolves on first or second round winner."
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
      poly_vol_24h_usd: 79479.72700000001
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume on a 0%-priced contract signals position cleanup or arbitrage closing, not a re-evaluation of the candidate, a desk can treat this as confirmation of consensus, not a reappraisal.
