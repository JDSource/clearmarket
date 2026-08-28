---
signal_id: "CMSIG20260828VS04"
signal_slug: "will-karishma-manzur-be-the-democratic-n-vol-13841"
headline: "Manzur NH Dem Senate: 7% on $14K volume"
semantic_title: "Manzur NH Senate bid holds at 7% as Pappas dominates"
telemetry: "7% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-28T19:52:39+00:00"
event_id: "CM-EVT-HY8R70V952"
event_slug: "new-hampshire-democratic-senate-primary-winner"
event_question: "Will the Democratic Party winner of the New Hampshire Senate primary be determined by the 2026 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1cf96ff28b0fa76e23f12a0cf299fc3bced8b26e0addfc1ef11fb58347c0216e"
  question_raw: "Will Karishma Manzur be the Democratic nominee for Senate in New Hampshire?"
  current_price: 0.074
  volume_24h_usd: 13841.773855
  volume_cumulative_usd: 39445.141711
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "7% leaves a slim tail for Manzur to overtake Pappas as the New Hampshire Democratic Senate nominee."
  - "35% of all-time volume today, relative to contract size, the most concentrated daily share in the NH cluster."
  - "Likely driven by traders hedging or closing positions as the Pappas narrative tightens across venues."
  - "Resolves on New Hampshire Democratic primary certification."
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
      poly_vol_24h_usd: 13841.773855
sources:
  - label: "ClearMarket market record: Will the Democratic Party winner of the New Hampshire S"
    url: "https://clearmarket.fyi/events/new-hampshire-democratic-senate-primary-winner"
    retrieved_at: "2026-08-28T19:52:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 7% residual with a third of lifetime volume printing today points to tail-risk positioning or washout selling, desks should read this as the market offering one final exit on a Manzur upset scenario.
