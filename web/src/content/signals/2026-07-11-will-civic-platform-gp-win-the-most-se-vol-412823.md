---
signal_id: "CMSIG20260711VS00"
signal_slug: "will-civic-platform-gp-win-the-most-se-vol-412823"
headline: "GP most Duma seats: 0% on $413K surge"
semantic_title: "Traders write off Civic Platform's Duma plurality bid"
telemetry: "0% · $413K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-11T09:24:55+00:00"
event_id: "CM-EVT-T6F5BDTGC1"
event_slug: "russia-parliamentary-election-winner"
event_question: "Will United Russia win the most seats in the Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48337ab13ef050f08a95d9bd39d1ece42923bd4c315bf82d8c2b86cd97af73d9"
  question_raw: "Will Civic Platform (GP) win the most seats in the next Russian parliamentary election?"
  current_price: 0.003
  volume_24h_usd: 412823.69000000047
  volume_cumulative_usd: 568876.6443280011
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices GP at 0%, implying zero credible path to a Duma plurality."
  - "24h volume of $413K is 73% of all-time handle, near-total lifetime activity in one session."
  - "Coordinated volume across Russian opposition party contracts suggests systematic position-closing or arbitrage sweep."
  - "Resolves on next Russian State Duma election result; United Russia dominance is the implicit baseline."
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
      poly_vol_24h_usd: 412823.69000000047
sources:
  - label: "ClearMarket market record: Will United Russia win the most seats in the Russian pa"
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-winner"
    retrieved_at: "2026-07-11T09:24:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The concentration of lifetime volume in a single session across multiple Russian party contracts signals a coordinated book-clearing event, likely triggered by a rule clarification or contract restructuring, worth monitoring for associated SRZP and LDPR contract flows.
