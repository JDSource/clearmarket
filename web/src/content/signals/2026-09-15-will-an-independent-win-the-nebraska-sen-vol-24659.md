---
signal_id: "CMSIG20260915VS02"
signal_slug: "will-an-independent-win-the-nebraska-sen-vol-24659"
headline: "Nebraska Senate indie: 33% on $25K surge"
semantic_title: "Nebraska Senate independent bid holds under 25% odds"
telemetry: "33% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-15T13:06:46+00:00"
event_id: "CM-EVT-CY3W5Z2793"
event_slug: "nebraska-senate-election-winner"
event_question: "Nebraska Senate Election Winner  "
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5554740293afa7aafd5fed10fd2de43a898e2884c1f98bd65185e703f371b9db"
  question_raw: "Will an independent win the Nebraska Senate race in 2026?"
  current_price: 0.33
  volume_24h_usd: 24659.502254999996
  volume_cumulative_usd: 68388.06902800001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket puts an independent winning the Nebraska Senate race at 33%, below the coin-flip but not a long shot."
  - "36% of all-time volume hit in 24 hours, signaling a sharp burst of fresh attention to this race."
  - "A new poll, candidate announcement, or major-party development in Nebraska likely triggered the repositioning."
  - "Resolves on 2026 Nebraska Senate election night."
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
      poly_vol_24h_usd: 24659.502254999996
sources:
  - label: "ClearMarket market record: Nebraska Senate Election Winner  "
    url: "https://clearmarket.fyi/events/nebraska-senate-election-winner"
    retrieved_at: "2026-09-15T13:06:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A one-third probability combined with a 36% all-time volume day suggests the race has moved from settled to genuinely contested, worth flagging for political-risk desks tracking Senate control scenarios.
