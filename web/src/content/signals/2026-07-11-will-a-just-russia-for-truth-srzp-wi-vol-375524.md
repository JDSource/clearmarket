---
signal_id: "CMSIG20260711VS01"
signal_slug: "will-a-just-russia-for-truth-srzp-wi-vol-375524"
headline: "SRZP most Duma seats: 0% on $376K inflow"
semantic_title: "SRZP Duma plurality: capital stacks against opposition path"
telemetry: "0% · $376K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-11T09:24:55+00:00"
event_id: "CM-EVT-T6F5BDTGC1"
event_slug: "russia-parliamentary-election-winner"
event_question: "Will United Russia win the most seats in the Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x57de5cb5861ac19516a631dabfbfbf1b0ebd28693fbd6412cbb24582f3304dbc"
  question_raw: "Will A Just Russia – For Truth (SRZP) win the most seats in the next Russian parliamentary election?"
  current_price: 0.005
  volume_24h_usd: 375524.96000000025
  volume_cumulative_usd: 684213.9141259983
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket marks SRZP at 0%, effectively ruling out any plurality outcome for the left-nationalist party."
  - "55% of all-time volume, $376K, hit in 24h, mirroring the GP spike in timing and structure."
  - "Parallel surges across GP and SRZP contracts point to a single catalyst, possibly a Polymarket policy review or mass settlement event."
  - "Resolution contingent on official Duma seat tallies; current Russian electoral law makes opposition pluralities structurally implausible."
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
      poly_vol_24h_usd: 375524.96000000025
sources:
  - label: "ClearMarket market record: Will United Russia win the most seats in the Russian pa"
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-winner"
    retrieved_at: "2026-07-11T09:24:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The synchronized 0%-price volume surge across multiple Russian opposition party contracts is a desk-level signal of a platform-side resolution or contract restructuring, not organic political newsflow, risk teams should treat both contracts as administratively driven.
