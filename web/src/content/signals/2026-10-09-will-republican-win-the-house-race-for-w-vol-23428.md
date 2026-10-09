---
signal_id: "CMSIG20261009VS00"
signal_slug: "will-republican-win-the-house-race-for-w-vol-23428"
headline: "WI-1 Republican win: 66% on $23K surge"
semantic_title: "Traders pile into WI-1 GOP hold at 2-to-1 odds"
telemetry: "66% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-09T14:56:08+00:00"
event_id: "CM-EVT-CM1BLLFVK3"
event_slug: "housewi1-26"
event_question: "Will the WI-01 House race winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEWI1-26-R"
  question_raw: "Will Republican win the House race for WI-1?"
  current_price: 0.66
  volume_24h_usd: 23428.26
  volume_cumulative_usd: 32187.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices GOP at 66%, a clear but not overwhelming favorite to hold WI-1."
  - "24h volume of $23K is 73% of all-time handle, signaling a near-total liquidity event on this contract."
  - "Late-cycle capital deployment this close to the race suggests poll movement or internal data is sharpening conviction."
  - "Resolves on WI-1 general election result."
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
      kalshi_vol_24h_usd: 23428.26
sources:
  - label: "ClearMarket market record: Will the WI-01 House race winner be determined by Janua"
    url: "https://clearmarket.fyi/events/housewi1-26"
    retrieved_at: "2026-10-09T14:56:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A volume burst equal to nearly three-quarters of all prior trading in one day flags WI-1 as a watched swing seat, desks should treat this as a leading indicator of fresh ground-level data entering the market.
