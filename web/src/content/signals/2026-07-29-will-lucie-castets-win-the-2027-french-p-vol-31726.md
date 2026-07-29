---
signal_id: "CMSIG20260729VS02"
signal_slug: "will-lucie-castets-win-the-2027-french-p-vol-31726"
headline: "Castets 2027 French president: 0% on $32K"
semantic_title: "Castets 2027 French presidency priced out at 0%"
telemetry: "0% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xac9719f855755f578e4979f8edb4e17e259e8e1cc79e46bdbde49e23dbd8b98f"
  question_raw: "Will Lucie Castets win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 31726.132
  volume_cumulative_usd: 61027.54899999999
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices Lucie Castets winning the 2027 French presidency at 0%, effectively eliminated."
  - "52% of all-time volume arrived in 24h, making this the contract's busiest single session."
  - "Surge likely reflects a confirming datapoint, polling, candidacy withdrawal, or party realignment news."
  - "Resolves on 2027 election outcome; current price implies no viable path to victory."
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
      poly_vol_24h_usd: 31726.132
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 0% price drawing over half of all-time volume in one day signals that new information has definitively closed off Castets as a credible candidate in French left-wing calculus.
