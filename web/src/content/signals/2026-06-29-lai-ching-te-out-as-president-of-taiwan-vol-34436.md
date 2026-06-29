---
signal_id: "CMSIG20260629VS03"
signal_slug: "lai-ching-te-out-as-president-of-taiwan-vol-34436"
headline: "Lai out by Dec 31, 2026: 4% on $34K inflow"
semantic_title: "Traders write off Lai Ching-te removal through year-end"
telemetry: "4% · $34K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T01:47:13+00:00"
event_id: "CM-EVT-MH9KTJJZ41"
event_slug: "lai-ching-te-out-as-president-of-taiwan-in-2026"
event_question: "Will Lai Ching-te no longer be President of Taiwan by December 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x68e47e45601b8e7fff925490f419191126c0f87cdf978717881fd2efa18cfb5b"
  question_raw: "Lai Ching-te out as President of Taiwan by December 31, 2026?"
  current_price: 0.04
  volume_24h_usd: 34436.75875
  volume_cumulative_usd: 103898.47551900003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 4%, market firmly discounts presidential removal or departure as a 2026 scenario."
  - "$34K in 24h is 33% of all-time volume; fresh attention on a tail-risk contract with six months remaining."
  - "Cross-strait tension headlines likely driving curiosity inflows; 4% reflects institutional consensus on Taiwan political stability."
  - "Resolves December 31, 2026, long runway for catalyst-driven repricing if PRC pressure escalates."
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
      poly_vol_24h_usd: 34436.75875
sources:
  - label: "ClearMarket market record: Will Lai Ching-te no longer be President of Taiwan by D"
    url: "https://clearmarket.fyi/events/lai-ching-te-out-as-president-of-taiwan-in-2026"
    retrieved_at: "2026-06-29T01:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A geopolitical desk should note the volume as attention-driven rather than conviction-driven, at 4%, the surge more likely reflects news-scanning hedgers than traders with directional edge on Taiwan political risk.
