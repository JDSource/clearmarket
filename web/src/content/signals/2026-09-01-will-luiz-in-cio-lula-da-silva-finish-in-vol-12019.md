---
signal_id: "CMSIG20260901VS02"
signal_slug: "will-luiz-in-cio-lula-da-silva-finish-in-vol-12019"
headline: "Lula third in Brazil round 1: 0% on $12K"
semantic_title: "Lula finishing third in Brazil's first round priced out"
telemetry: "0% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-01T13:00:43+00:00"
event_id: "CM-EVT-MQHJWNSWH5"
event_slug: "brazil-presidential-election-first-round-3rd-place"
event_question: "Will the third-place finisher in the first round of the Brazil presidential election receive more than 10% of the vote?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd24e8798122cba5bb43a77e9a78f2e26bd65c47f281f4b66582718fa215b9f6e"
  question_raw: "Will Luiz Inácio Lula da Silva finish in third place in the first round of the 2026 Brazilian presidential election?"
  current_price: 0.001
  volume_24h_usd: 12019.696033000017
  volume_cumulative_usd: 47952.730036
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "0% price means the market assigns effectively zero probability to Lula finishing third or worse in the first round."
  - "24h volume of $12K equals 25% of all-time, marking a notable one-day attention spike on a contract already near-resolved."
  - "Volume at zero likely reflects traders closing short positions or arbitrageurs clearing residual liquidity as the outcome is treated as settled."
  - "Resolves on official Brazilian electoral first-round results; Lula is a dominant frontrunner in all current polling."
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
      poly_vol_24h_usd: 12019.696033000017
sources:
  - label: "ClearMarket market record: Will the third-place finisher in the first round of the"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-3rd-place"
    retrieved_at: "2026-09-01T13:00:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 25% all-time volume day on a 0% contract signals position cleanup and arbitrage closing, not a genuine directional view, desks can treat this as administrative flow rather than an informational signal.
