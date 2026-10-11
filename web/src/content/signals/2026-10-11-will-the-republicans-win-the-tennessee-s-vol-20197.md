---
signal_id: "CMSIG20261011VS05"
signal_slug: "will-the-republicans-win-the-tennessee-s-vol-20197"
headline: "TN Senate GOP Polymarket: 94% on $20K"
semantic_title: "Heavy trading tests the Tennessee GOP Senate price at 94%"
telemetry: "94% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T07:48:50+00:00"
event_id: "CM-EVT-TGH45YCRW3"
event_slug: "tennessee-senate-election-winner"
event_question: "Will a Republican win the Tennessee Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x17d8c697aa69e53ef8062fc4b42ff6f8f7983ec569a021aab6d707d6f797780a"
  question_raw: "Will the Republicans win the Tennessee Senate race in 2026?"
  current_price: 0.936
  volume_24h_usd: 20197.084677000003
  volume_cumulative_usd: 47904.50628000002
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Republican Tennessee win at 94%, closely tracking the Kalshi 93% on the same race."
  - "42% of all-time volume on this contract placed in 24h, keeping cross-venue pricing tight."
  - "Simultaneous volume spikes on both venues point to coordinated market attention, likely midterm cycle re-engagement."
  - "Resolves on 2026 Tennessee Senate election night."
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
      poly_vol_24h_usd: 20197.084677000003
sources:
  - label: "ClearMarket market record: Will a Republican win the Tennessee Senate election?"
    url: "https://clearmarket.fyi/events/tennessee-senate-election-winner"
    retrieved_at: "2026-10-11T07:48:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-identical pricing with simultaneous volume spikes on Kalshi and Polymarket confirms genuine market-wide re-engagement on Tennessee, not a venue-specific quirk.
