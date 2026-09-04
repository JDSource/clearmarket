---
signal_id: "CMSIG20260904VS03"
signal_slug: "will-democratic-win-the-house-race-for-v-vol-16650"
headline: "Democrat VA-2 House: 83% on $16K volume test"
semantic_title: "VA-2 Democratic odds hold at 83% through a volume test"
telemetry: "83% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-04T12:29:08+00:00"
event_id: "CM-EVT-29P41DBY75"
event_slug: "houseva2-26"
event_question: "Who will win the Virginia 2nd District House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEVA2-26-D"
  question_raw: "Will Democratic win the House race for VA-2?"
  current_price: 0.83
  volume_24h_usd: 16650.43
  volume_cumulative_usd: 32362.41
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices the Democratic candidate at 83%, market leans Democratic but leaves meaningful tail risk."
  - "$16K in 24h equals 51% of all-time volume, a majority of all trading compressed into one session."
  - "VA-2 is a competitive coastal Virginia district; renewed volume may track a late-filing or fundraising disclosure."
  - "Contract resolves on the certified winner of the VA-2 U.S. House general election."
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
      kalshi_vol_24h_usd: 16650.43
sources:
  - label: "ClearMarket market record: Who will win the Virginia 2nd District House election?"
    url: "https://clearmarket.fyi/events/houseva2-26"
    retrieved_at: "2026-09-04T12:29:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time volume printing in a single day at 83% tells a desk the market is actively re-evaluating tail risk in a district that remains genuinely competitive, worth monitoring alongside VA campaign finance filings.
