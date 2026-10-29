---
signal_id: "CMSIG20261029VS00"
signal_slug: "will-any-ai-model-have-a-score-of-at-lea-vol-91073"
headline: "AI 1540 score by Jan 2027: 99% on $91K surge"
semantic_title: "AI hitting 1540 before year-end stays a near-certainty"
telemetry: "99% · $91K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T07:48:41+00:00"
event_id: "CM-EVT-0MCTG7XWR4"
event_slug: "kxaispike-27"
event_question: "Will there be significant AI capability growth this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAISPIKE-27B-1540"
  question_raw: "Will any AI model have a score of at least 1540 before Jan 1, 2027"
  current_price: 0.99
  volume_24h_usd: 91073.9
  volume_cumulative_usd: 110766.61
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a 1540 AI benchmark score by Jan 1, 2027 at 99%, market treats it as done."
  - "$91K traded in 24h, equal to 82% of all-time volume, almost the entire lifetime book repriced today."
  - "Late-cycle rush near resolution suggests traders locking in near-certain 'yes' before contract closes."
  - "Resolves Jan 1, 2027; near-zero residual doubt leaves little room for price movement."
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
      kalshi_vol_24h_usd: 91073.9
sources:
  - label: "ClearMarket market record: Will there be significant AI capability growth this yea"
    url: "https://clearmarket.fyi/events/kxaispike-27"
    retrieved_at: "2026-10-29T07:48:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 82%-of-all-time volume print at 99% odds signals the desk this contract is effectively resolved in the market's eyes, monitor for the benchmark announcement that triggers formal settlement.
