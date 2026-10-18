---
signal_id: "CMSIG20261018VS03"
signal_slug: "will-the-republican-party-win-the-tn-07-vol-11320"
headline: "TN-07 GOP seat: 97% on $11K volume rise"
semantic_title: "TN-07 Republican hold draws fresh trading at 97%"
telemetry: "97% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-18T12:26:25+00:00"
event_id: "CM-EVT-N1Q1LN0697"
event_slug: "tn-07-house-election-winner"
event_question: "Will the winner of the TN-07 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x25bb72b2889af65cebf573aaba1d824b13c0663d2a87ead3f1ffc1d09a4455d1"
  question_raw: "Will the Republican Party win the TN-07 House seat?"
  current_price: 0.968
  volume_24h_usd: 11320.900761
  volume_cumulative_usd: 37620.789094
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republican TN-07 win at 97%, leaving minimal probability for any other outcome."
  - "24h volume of $11K represents 30% of all-time handle, meaningful but below the NC-11 intensity, suggesting routine late-cycle flow."
  - "Fresh activity in a near-locked contract typically reflects resolution-proximity positioning rather than competitive uncertainty."
  - "Contract resolves on Nov 3 general election results for TN-07."
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
      poly_vol_24h_usd: 11320.900761
sources:
  - label: "ClearMarket market record: Will the winner of the TN-07 House election be determin"
    url: "https://clearmarket.fyi/events/tn-07-house-election-winner"
    retrieved_at: "2026-10-18T12:26:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 97% with 30% of lifetime volume in one day, TN-07 is attracting resolution arb traffic ahead of election night, a desk can treat this as a liquidity footnote rather than a signal of competitive risk.
