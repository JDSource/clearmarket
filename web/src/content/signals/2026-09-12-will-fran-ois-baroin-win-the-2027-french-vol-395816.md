---
signal_id: "CMSIG20260912VS02"
signal_slug: "will-fran-ois-baroin-win-the-2027-french-vol-395816"
headline: "Baroin French president: 0% on $396K surge"
semantic_title: "Baroin 2027 French presidency stays a long shot at 0%"
telemetry: "0% · $396K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-12T11:56:57+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc9763b782d68da2d9adfccfe232a90599edea130dd45f00f67b615a164393293"
  question_raw: "Will François Baroin win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 395816.15
  volume_cumulative_usd: 1136634.903999
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket assigns François Baroin effectively zero probability of winning the 2027 French presidency."
  - "$396K in 24h volume represents 35% of all-time contract volume, a major spike for a zero-priced outcome."
  - "Fresh attention on a 0% candidate typically precedes a news event; traders may be testing whether new information changes the read."
  - "Contract resolves on the 2027 French presidential election result."
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
      poly_vol_24h_usd: 395816.15
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-09-12T11:56:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A burst of volume into a zero-priced contract is a signal worth monitoring for imminent news, a desk covering European political risk should watch for a Baroin candidacy development or polling shift.
