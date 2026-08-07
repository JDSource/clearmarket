---
signal_id: "CMSIG20260807VS01"
signal_slug: "will-fran-ois-baroin-win-the-2027-french-vol-131124"
headline: "Baroin French president: 0% on $131K surge"
semantic_title: "Baroin 2027 French presidency stays a long shot on fresh volume"
telemetry: "0% · $131K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-07T08:54:29+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc9763b782d68da2d9adfccfe232a90599edea130dd45f00f67b615a164393293"
  question_raw: "Will François Baroin win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 131124.437
  volume_cumulative_usd: 395952.437999
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Market prices Baroin at effectively zero, contract treats his path as closed."
  - "$131K in 24h represents 33% of all-time volume, a sudden burst of attention."
  - "Fresh flow into a 0% contract likely reflects arbitrage, curiosity, or field reshuffling news."
  - "Resolves on the 2027 French presidential election result."
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
      poly_vol_24h_usd: 131124.437
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-08-07T08:54:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume against a 0% price suggests a desk should watch for a structural field development, someone is spending real dollars confirming or probing this candidate's elimination.
