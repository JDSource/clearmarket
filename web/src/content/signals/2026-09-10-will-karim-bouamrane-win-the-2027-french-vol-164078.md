---
signal_id: "CMSIG20260910VS01"
signal_slug: "will-karim-bouamrane-win-the-2027-french-vol-164078"
headline: "Bouamrane France 2027: 0% on $164K volume"
semantic_title: "Bouamrane French presidential odds stay at zero on heavy trade"
telemetry: "0% · $164K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-10T12:40:48+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x53e78cfec087a9bc8d1336c16a2da9db577cacedb5569c36e776711b264351a6"
  question_raw: "Will Karim Bouamrane win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 164078.0
  volume_cumulative_usd: 484303.39528299996
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket holds Bouamrane at 0%, reflecting near-zero market conviction in his 2027 path."
  - "$164K traded in 24 hours, 34% of all-time volume, in tandem with the Castets spike."
  - "Simultaneous spikes across multiple French left-wing candidates point to a coordinated reassessment of the left's 2027 field."
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
      poly_vol_24h_usd: 164078.0
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-09-10T12:40:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The synchronized volume across Castets and Bouamrane contracts at 0% suggests a structural left-field collapse is being priced in, worth flagging for any European political risk book.
