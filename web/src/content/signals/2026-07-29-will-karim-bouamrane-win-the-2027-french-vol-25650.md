---
signal_id: "CMSIG20260729VS07"
signal_slug: "will-karim-bouamrane-win-the-2027-french-vol-25650"
headline: "Bouamrane 2027 French president: 0% on $26K"
semantic_title: "Bouamrane 2027 French presidency priced out at 0%"
telemetry: "0% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x53e78cfec087a9bc8d1336c16a2da9db577cacedb5569c36e776711b264351a6"
  question_raw: "Will Karim Bouamrane win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 25650.12
  volume_cumulative_usd: 80102.095283
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices Karim Bouamrane winning the 2027 French presidency at 0%, market has ruled him out."
  - "32% of all-time volume hit in 24h on a contract with $80K lifetime handle, meaningful single-day flow."
  - "Volume arrives alongside the Castets 0% spike, suggesting a broad reassessment of French left-field candidates."
  - "Resolves on the 2027 French presidential result; both PS-adjacent candidates now priced at zero."
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
      poly_vol_24h_usd: 25650.12
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous 0%-pricing volume spikes on Bouamrane and Castets indicate the market is actively closing out the French left-wing long-shot book, likely in response to the same political development.
