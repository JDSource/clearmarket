---
signal_id: "CMSIG20260907VS00"
signal_slug: "will-maura-sullivan-be-the-democratic-no-vol-22304"
headline: "Sullivan NH-1 Dem nominee: 83% on $22K surge"
semantic_title: "Traders back Sullivan as NH-1 Dem nominee"
telemetry: "83% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-07T13:54:42+00:00"
event_id: "CM-EVT-6N9YKDY7Z9"
event_slug: "kxnh1d-26"
event_question: "Will the Democratic nominee for New Hampshire's 1st Congressional District be determined by January 1, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNH1D-26-MSUL"
  question_raw: "Will Maura Sullivan be the Democratic nominee for NH-1?"
  current_price: 0.83
  volume_24h_usd: 22304.39
  volume_cumulative_usd: 67469.28
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices Sullivan at 83%, strong favorite to claim the NH-1 Democratic nomination."
  - "24h volume of $22K equals 33% of all-time handle, a decisive single-session commitment."
  - "Concentrated fresh activity suggests a near-term filing deadline or primary date is approaching."
  - "Contract resolves on Democratic nominee certification for New Hampshire's 1st Congressional District."
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
      kalshi_vol_24h_usd: 22304.39
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for New Hampshire's 1st Con"
    url: "https://clearmarket.fyi/events/kxnh1d-26"
    retrieved_at: "2026-09-07T13:54:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A third of lifetime volume landing in one session signals the market is treating Sullivan's nomination as effectively settled, with residual odds pricing minimal but live upset risk.
