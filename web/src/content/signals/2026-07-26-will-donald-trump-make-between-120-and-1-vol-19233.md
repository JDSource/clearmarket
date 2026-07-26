---
signal_id: "CMSIG20260726VS04"
signal_slug: "will-donald-trump-make-between-120-and-1-vol-19233"
headline: "Trump Truth Social 120-139 posts: 99% on $19K"
semantic_title: "Trump Truth Social post count near certainty at 99%"
telemetry: "99% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-26T09:56:30+00:00"
event_id: "CM-EVT-XPZP0MG799"
event_slug: "kxtruthsocial-26jul25"
event_question: "Will Trump post on Truth Social between July 19-25?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUTHSOCIAL-26JUL25-B129"
  question_raw: "Will Donald Trump make between 120 and 139 Truth Social posts the week of Jul 19, 2026?"
  current_price: 0.99
  volume_24h_usd: 19233.85
  volume_cumulative_usd: 59374.6
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-26T14:00:00Z"
bullets:
  - "Kalshi prices Trump posting 120, 139 Truth Social posts in the week of Jul 19 at 99%, effectively resolved."
  - "32% of all-time volume transacted in 24h as the contract approaches settlement."
  - "Actual post counts for the week are likely observable, driving one-sided liquidity to lock in the outcome."
  - "Contract resolves on weekly post tally; 99% leaves virtually no residual uncertainty."
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
      kalshi_vol_24h_usd: 19233.85
sources:
  - label: "ClearMarket market record: Will Trump post on Truth Social between July 19-25?"
    url: "https://clearmarket.fyi/events/kxtruthsocial-26jul25"
    retrieved_at: "2026-07-26T09:56:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing with fresh volume is consistent with late-stage arbitrage activity as traders clean up remaining basis ahead of settlement, not a signal of new information.
