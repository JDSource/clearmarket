---
signal_id: "CMSIG20260920VS01"
signal_slug: "will-the-democrats-win-the-kansas-senate-vol-18773"
headline: "Democrats KS Senate 2026: 28% on $19K spike"
semantic_title: "Democrats' Kansas Senate odds hold under 30% on fresh volume"
telemetry: "28% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T12:50:42+00:00"
event_id: "CM-EVT-V8Y5SZ7SK0"
event_slug: "kansas-senate-election-winner"
event_question: "Kansas Senate Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x460d3942d385cdeda20519c0c5ad804ae48dc18efc9a82e1f1be87a29e69adb3"
  question_raw: "Will the Democrats win the Kansas Senate race in 2026?"
  current_price: 0.28
  volume_24h_usd: 18773.847091
  volume_cumulative_usd: 64821.55181700001
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices a Democratic Kansas Senate win at 28%, a long shot, but not dismissed."
  - "24h volume of $19K represents 29% of all-time handle, one of the contract's heaviest single sessions."
  - "Fresh attention may precede a candidate announcement, polling update, or national party resource decision on the race."
  - "Resolves YES if the Democratic candidate wins the 2026 Kansas U.S. Senate general election."
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
      poly_vol_24h_usd: 18773.847091
sources:
  - label: "ClearMarket market record: Kansas Senate Election Winner"
    url: "https://clearmarket.fyi/events/kansas-senate-election-winner"
    retrieved_at: "2026-09-20T12:50:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag that 29% of all-time volume printing in one day on a deep-red state Senate race implies traders are actively reassessing the competitive landscape, possibly ahead of a catalyst.
