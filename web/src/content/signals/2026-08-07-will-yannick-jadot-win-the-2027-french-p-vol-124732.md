---
signal_id: "CMSIG20260807VS02"
signal_slug: "will-yannick-jadot-win-the-2027-french-p-vol-124732"
headline: "Jadot French president: 0% on $124K inflow"
semantic_title: "Jadot 2027 French presidency draws volume but odds stay at zero"
telemetry: "0% · $125K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-07T08:54:29+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xae0bce0eab50dc2961c6426b8b4096ff238cbb59408235b629bfbfef3a2c1a12"
  question_raw: "Will Yannick Jadot win the 2027 French presidential election?"
  current_price: 0.002
  volume_24h_usd: 124732.386
  volume_cumulative_usd: 439755.96858600015
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket holds Jadot at 0%, market sees no viable path to the Élysée."
  - "$124K over 24h is 28% of all-time volume; two French long-shots spiking together is notable."
  - "Parallel Baroin spike suggests a broad French presidential field re-evaluation is underway."
  - "Resolves on the 2027 French presidential election outcome."
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
      poly_vol_24h_usd: 124732.386
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-08-07T08:54:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two simultaneous French presidential long-shot spikes point to a desk catalyst, likely a polling release or party announcement, worth monitoring for spillover into front-runner contracts.
