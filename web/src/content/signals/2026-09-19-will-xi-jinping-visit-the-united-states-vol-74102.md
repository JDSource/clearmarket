---
signal_id: "CMSIG20260919VS01"
signal_slug: "will-xi-jinping-visit-the-united-states-vol-74102"
headline: "Xi US visit by Oct 1: 92% on $74K volume"
semantic_title: "Xi US visit before Oct 1 draws heavy late-stage trading"
telemetry: "92% · $74K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-VD0FYJK2D7"
event_slug: "kxxiusa-26jul07"
event_question: "Will Xi Jinping visit the United States?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXXIUSA-26JUL07-OCT01"
  question_raw: "Will Xi Jinping visit the United States of America before Oct 1, 2026?"
  current_price: 0.92
  volume_24h_usd: 74102.78
  volume_cumulative_usd: 284817.47
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-08T14:00:00Z"
bullets:
  - "Kalshi prices a Xi Jinping US visit before Oct 1, 2026 at 92%, strongly consensus."
  - "24h volume of $74K represents 26% of all-time, a notable single-session share this close to resolution."
  - "With under two weeks to deadline, volume likely reflects position squaring or last-minute directional conviction."
  - "Resolves Oct 1, 2026; any cancellation or postponement announcement is the primary repricing risk."
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
      kalshi_vol_24h_usd: 74102.78
sources:
  - label: "ClearMarket market record: Will Xi Jinping visit the United States?"
    url: "https://clearmarket.fyi/events/kxxiusa-26jul07"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy late-window trading at 92% tells desks that participants are either locking in gains or adding at the top of conviction, the tight deadline amplifies any headline sensitivity.
