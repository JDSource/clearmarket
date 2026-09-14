---
signal_id: "CMSIG20260914VS01"
signal_slug: "who-will-win-the-next-swedish-general-el-vol-10500"
headline: "Swedish election winner: 97% on $10K volume burst"
semantic_title: "Sweden election odds hold near certainty on heavy trading"
telemetry: "97% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-14T14:41:37+00:00"
event_id: "CM-EVT-G35MQ80T62"
event_slug: "kxswedenparli-26"
event_question: "Will the Swedish Social Democrats win the most seats in the next Swedish general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSWEDENPARLI-26-SDP"
  question_raw: "Who will win the next Swedish general election?"
  current_price: 0.972
  volume_24h_usd: 10500.99
  volume_cumulative_usd: 32854.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-30T14:00:00Z"
bullets:
  - "Kalshi prices the leading outcome at 97%, the market is treating this as a near-resolved question, not a live contest."
  - "24h volume of $10K is 32% of the contract's all-time total, an unusually dense single-day share for a settled-looking market."
  - "High volume into a near-certain price suggests traders are either locking in late positions or testing whether any residual 3% gap can be closed."
  - "Resolves on the official result of Sweden's next general election."
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
      kalshi_vol_24h_usd: 10500.99
sources:
  - label: "ClearMarket market record: Will the Swedish Social Democrats win the most seats in"
    url: "https://clearmarket.fyi/events/kxswedenparli-26"
    retrieved_at: "2026-09-14T14:41:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy trading into a 97% contract typically flags either late yield-chasing on a near-certain payout or a small cohort hedging the tail, either way the 3% residual is drawing disproportionate capital attention.
