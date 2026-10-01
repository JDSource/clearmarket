---
signal_id: "CMSIG20261001VS00"
signal_slug: "will-any-ai-model-have-a-score-of-at-lea-vol-55500"
headline: "AI score 1530 by Jan 1: 99% on $55K surge"
semantic_title: "AI 1530 benchmark by Jan 1 stays near certain"
telemetry: "99% · $56K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T15:04:01+00:00"
event_id: "CM-EVT-0MCTG7XWR4"
event_slug: "kxaispike-27"
event_question: "Will there be significant AI capability growth this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAISPIKE-27B-1530"
  question_raw: "Will any AI model have a score of at least 1530 before Jan 1, 2027"
  current_price: 0.99
  volume_24h_usd: 55500.73
  volume_cumulative_usd: 64441.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a 99% chance some AI model clears the 1530 benchmark before 2027, near-certain consensus."
  - "24h volume of $55K is 86% of all-time traded, signaling a concentrated, late-cycle flush of remaining doubt."
  - "Fresh attention likely driven by a recent model release or benchmark result bringing the threshold into immediate reach."
  - "Resolves Jan 1, 2027, three months out; residual 1% represents pure tail risk on a surprise freeze."
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
      kalshi_vol_24h_usd: 55500.73
sources:
  - label: "ClearMarket market record: Will there be significant AI capability growth this yea"
    url: "https://clearmarket.fyi/events/kxaispike-27"
    retrieved_at: "2026-10-01T15:04:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume spike effectively closes the book on this contract, desks should treat the 1530 threshold as already priced in and look to the next benchmark level for tradeable uncertainty.
