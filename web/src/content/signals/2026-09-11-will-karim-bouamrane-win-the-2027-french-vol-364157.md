---
signal_id: "CMSIG20260911VS00"
signal_slug: "will-karim-bouamrane-win-the-2027-french-vol-364157"
headline: "Bouamrane 2027: 0% on $364K surge"
semantic_title: "Bouamrane 2027 presidency bet collapses to zero"
telemetry: "0% · $364K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-11T12:33:13+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x53e78cfec087a9bc8d1336c16a2da9db577cacedb5569c36e776711b264351a6"
  question_raw: "Will Karim Bouamrane win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 364157.4
  volume_cumulative_usd: 848460.795283
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices Bouamrane at 0%, the market sees no viable path to the Élysée."
  - "43% of all-time volume landed in 24h, the sharpest single-day conviction reset on record for this contract."
  - "Fresh attention likely follows a political development, a withdrawal signal, poll collapse, or coalition news, that traders treated as definitive."
  - "Contract resolves on 2027 French presidential election result; at 0% it is effectively closed."
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
      poly_vol_24h_usd: 364157.4
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-09-11T12:33:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-total volume flush to zero in one session signals a hard information event, desks should check for a formal Bouamrane withdrawal or disqualifying political development before 2027 campaign filing deadlines.
