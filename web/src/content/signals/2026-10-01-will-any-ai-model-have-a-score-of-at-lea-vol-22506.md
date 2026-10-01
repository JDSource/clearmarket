---
signal_id: "CMSIG20261001VS01"
signal_slug: "will-any-ai-model-have-a-score-of-at-lea-vol-22506"
headline: "AI score 1530 before Jan 2027: 97% on $22K surge"
semantic_title: "Heavy trading holds the 1530 AI benchmark at near-certainty"
telemetry: "97% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T07:48:14+00:00"
event_id: "CM-EVT-0MCTG7XWR4"
event_slug: "kxaispike-27"
event_question: "Will there be significant AI capability growth this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAISPIKE-27B-1530"
  question_raw: "Will any AI model have a score of at least 1530 before Jan 1, 2027"
  current_price: 0.97
  volume_24h_usd: 22506.11
  volume_cumulative_usd: 31265.85
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a 1530 benchmark score before Jan 1, 2027 at 97%, near-certain resolution yes."
  - "72% of all-time contract volume ($22K of $31K lifetime) cleared in a single 24h window."
  - "Surge likely reflects a published or leaked score result pushing residual doubters to close short positions."
  - "Resolves Jan 1, 2027; at 97% the remaining 3% is pure tail risk on a scoring dispute or delay."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 22506.11
sources:
  - label: "ClearMarket market record: Will there be significant AI capability growth this yea"
    url: "https://clearmarket.fyi/events/kxaispike-27"
    retrieved_at: "2026-10-01T07:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly three-quarters of lifetime volume in one day at 97% means the market is treating this as essentially resolved, a desk should check whether an official benchmark publication just dropped.
