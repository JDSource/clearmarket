---
signal_id: "CMSIG20261001VS03"
signal_slug: "will-any-ai-model-have-a-score-of-at-lea-vol-37514"
headline: "AI score 1520 by Jan 1: 99% on $37K surge"
semantic_title: "AI 1520 benchmark by Jan 1 priced as all but done"
telemetry: "99% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T15:04:01+00:00"
event_id: "CM-EVT-0MCTG7XWR4"
event_slug: "kxaispike-27"
event_question: "Will there be significant AI capability growth this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAISPIKE-27B-1520"
  question_raw: "Will any AI model have a score of at least 1520 before Jan 1, 2027"
  current_price: 0.99
  volume_24h_usd: 37514.54
  volume_cumulative_usd: 142017.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a 99% probability that some AI model scores at least 1520 before 2027, effectively resolved in the market."
  - "24h volume of $37K is 26% of all-time, a notable single-session print on a contract the market already treats as settled."
  - "The 1520 threshold is the softer cousin of Spike 0; fresh volume here likely reflects arbitrage or portfolio positioning."
  - "Resolves Jan 1, 2027; the 1% residual is noise, not a real signal of doubt."
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
      kalshi_vol_24h_usd: 37514.54
sources:
  - label: "ClearMarket market record: Will there be significant AI capability growth this yea"
    url: "https://clearmarket.fyi/events/kxaispike-27"
    retrieved_at: "2026-10-01T15:04:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Activity on a 99%-priced contract suggests traders are using it for collateral positioning or hedging rather than expressing genuine uncertainty, desks can treat this threshold as commercially resolved.
