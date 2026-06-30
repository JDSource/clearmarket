---
signal_id: "CMSIG20260630VS07"
signal_slug: "will-melat-kiros-be-the-democratic-nomin-vol-70210"
headline: "Kiros CO-01 Dem nominee: 78% on $70K Kalshi surge"
semantic_title: "Kiros commands strong capital backing for the CO-01 Democratic nod"
telemetry: "78% · $70K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-30T10:55:12+00:00"
event_id: "CM-EVT-Q1BHRBLKP7"
event_slug: "kxcoprimary-01d26"
event_question: "Will the Democratic nominee be from Colorado by the 2024 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCOPRIMARY-01D26-MKIR"
  question_raw: "Will Melat Kiros be the Democratic nominee for CO-01?"
  current_price: 0.78
  volume_24h_usd: 70210.3
  volume_cumulative_usd: 279161.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi at 78%, strong front-runner status with meaningful doubt still priced."
  - "24h volume $70K is 25% of all-time, a healthy mid-cycle positioning surge."
  - "Colorado's 1st District primary is approaching; fresh flows suggest sharpening consensus."
  - "22% residual uncertainty leaves room for a challenger scenario or late news."
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
      kalshi_vol_24h_usd: 70210.3
sources:
  - label: "ClearMarket market record: Will the Democratic nominee be from Colorado by the 202"
    url: "https://clearmarket.fyi/events/kxcoprimary-01d26"
    retrieved_at: "2026-06-30T10:55:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 78% price with 25% of all-time volume flowing in a single session tells a political desk that Kiros is becoming a near-consensus pick while a meaningful minority is still hedging against an upset.
