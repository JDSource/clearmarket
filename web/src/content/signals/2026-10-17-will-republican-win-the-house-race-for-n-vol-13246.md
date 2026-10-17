---
signal_id: "CMSIG20261017VS07"
signal_slug: "will-republican-win-the-house-race-for-n-vol-13246"
headline: "NC-1 Republican: 36% on $13K Kalshi volume pop"
semantic_title: "NC-1 Republican odds slip to 36%; fresh volume tests the favorite"
telemetry: "36% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
event_id: "CM-EVT-22K74MYTV1"
event_slug: "housenc1-26"
event_question: "Will the winner of the North Carolina 1st Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENC1-26-R"
  question_raw: "Will Republican win the House race for NC-1?"
  current_price: 0.36
  volume_24h_usd: 13246.07
  volume_cumulative_usd: 36119.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican at just 36% in NC-1, making Democrats the clear market favorite at 64% implied odds."
  - "24h volume of $13K is 37% of all-time, a substantial one-day share into a competitively priced race."
  - "NC-1 pricing below 50% for the Republican is a notable signal in a state with several competitive 2026 contests."
  - "Resolves on November 2026 election night."
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
      kalshi_vol_24h_usd: 13246.07
sources:
  - label: "ClearMarket market record: Will the winner of the North Carolina 1st Congressional"
    url: "https://clearmarket.fyi/events/housenc1-26"
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A Republican priced below 50% drawing over a third of all-time volume in one session marks NC-1 as a genuine toss-up that desks modeling House majority math should treat as a live swing seat.
