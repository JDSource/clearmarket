---
signal_id: "CMSIG20260929VS00"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-41487"
headline: "Fed July 2027 hold: 76% on near-total volume return"
semantic_title: "Fed hold in July 2027 stays the heavy favorite"
telemetry: "76% · $41K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-29T07:47:54+00:00"
event_id: "CM-EVT-S64CMSWWK9"
event_slug: "kxfeddecision-27jul"
event_question: "Will the Federal Reserve make a decision in July 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-27JUL-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their July 2027 meeting?"
  current_price: 0.76
  volume_24h_usd: 41487.96
  volume_cumulative_usd: 47663.6
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-07-28T18:05:00Z"
bullets:
  - "Kalshi prices a 76% chance the Fed leaves rates unchanged at its July 2027 meeting, a strong consensus lean."
  - "24h volume of $41.5K is 87% of all-time contract volume, near the entire lifetime of liquidity deployed in one session."
  - "Surge implies fresh macro positioning, likely driven by recent Fed communication or labor/inflation data reshaping the 2027 rate path."
  - "Contract resolves after the July 2027 FOMC decision."
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
      kalshi_vol_24h_usd: 41487.96
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in July 2027?"
    url: "https://clearmarket.fyi/events/kxfeddecision-27jul"
    retrieved_at: "2026-09-29T07:47:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-total volume flush into a single session signals desks are actively repricing 2027 Fed terminal-rate assumptions, worth flagging for rates strategy.
