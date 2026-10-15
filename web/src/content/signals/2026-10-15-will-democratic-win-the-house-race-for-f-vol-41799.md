---
signal_id: "CMSIG20261015VS03"
signal_slug: "will-democratic-win-the-house-race-for-f-vol-41799"
headline: "FL-25 (D): 79% on $42K, 27% of all-time vol"
semantic_title: "FL-25 Democratic odds hold above 75% through a volume wave"
telemetry: "79% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T07:48:38+00:00"
event_id: "CM-EVT-Q8F4815M66"
event_slug: "kxhouserace-fl25-26"
event_question: "Will the Florida 25th House seat be won in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL25-26-D"
  question_raw: "Will Democratic win the House race for FL-25?"
  current_price: 0.79
  volume_24h_usd: 41799.83
  volume_cumulative_usd: 155835.98
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "At 79%, Kalshi traders favor Democrats to take FL-25, a contested Florida district drawing real capital."
  - "$42K in 24h is 27% of all-time volume, meaningful for a down-ballot House race."
  - "Florida congressional seats rarely see this liquidity; fresh attention may precede a poll, fundraising filing, or candidate event."
  - "Contract resolves on FL-25 House election result."
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
      kalshi_vol_24h_usd: 41799.83
sources:
  - label: "ClearMarket market record: Will the Florida 25th House seat be won in the next ele"
    url: "https://clearmarket.fyi/events/kxhouserace-fl25-26"
    retrieved_at: "2026-10-15T07:48:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained odds above 75% with a fresh volume wave flags FL-25 as a credible Democratic pickup on desk scorecards, worth monitoring alongside broader Florida swing signals.
