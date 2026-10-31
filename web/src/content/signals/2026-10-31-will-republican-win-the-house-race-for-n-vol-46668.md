---
signal_id: "CMSIG20261031VS06"
signal_slug: "will-republican-win-the-house-race-for-n-vol-46668"
headline: "NY-02 GOP House: 81% on $47K Kalshi spike"
semantic_title: "NY-02 Republican House odds hold at 81% as trading surges"
telemetry: "81% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T14:16:49+00:00"
event_id: "CM-EVT-M23Y1W2P93"
event_slug: "kxhouserace-ny02-26"
event_question: "Will the winner of the New York's 2nd Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-NY02-26-R"
  question_raw: "Will Republican win the House race for NY-02?"
  current_price: 0.81
  volume_24h_usd: 46668.02
  volume_cumulative_usd: 57718.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican NY-02 House win at 81%, a strong favorite read."
  - "$47K traded in 24h is 81% of the contract's entire all-time volume, the most concentrated spike in this batch."
  - "Near-total all-time volume in one day on a House race suggests the market is newly liquid, not seasoned."
  - "Resolves on NY-02 2026 House election; thin prior volume means the price is sensitive to any new flow."
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
      kalshi_vol_24h_usd: 46668.02
sources:
  - label: "ClearMarket market record: Will the winner of the New York's 2nd Congressional Dis"
    url: "https://clearmarket.fyi/events/kxhouserace-ny02-26"
    retrieved_at: "2026-10-31T14:16:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Eighty-one percent of all-time volume arriving in one session on a House race tells a desk this contract was essentially dormant until now, treat the 81% price with caution given limited prior price discovery.
