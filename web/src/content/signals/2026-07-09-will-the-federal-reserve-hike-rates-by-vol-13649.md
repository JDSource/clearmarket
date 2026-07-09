---
signal_id: "CMSIG20260709VS05"
signal_slug: "will-the-federal-reserve-hike-rates-by-vol-13649"
headline: "Fed hike >25bps at July meeting: 1% on $13K"
semantic_title: "Market fades any >25bps Fed move at July 2026 meeting"
telemetry: "1% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-09T10:57:00+00:00"
event_id: "CM-EVT-BHTHYWRLH7"
event_slug: "kxfeddecision-26jul"
event_question: "Will the Federal Reserve make a decision in July 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26JUL-H26"
  question_raw: "Will the Federal Reserve Hike rates by >25bps at their July 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 13649.39
  volume_cumulative_usd: 16866.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "1% price, an outsized July hike is treated as a near-impossibility by the market."
  - "$13K in 24h is 81% of all-time; tiny absolute size but extreme session concentration signals a resolution chase."
  - "With the July FOMC meeting imminent, traders are settling this tail-risk contract ahead of the decision."
  - "Kalshi contract resolves on the July 2026 meeting outcome; flow is cleanup, not new conviction."
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
      kalshi_vol_24h_usd: 13649.39
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in July 2026?"
    url: "https://clearmarket.fyi/events/kxfeddecision-26jul"
    retrieved_at: "2026-07-09T10:57:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 81% all-time volume concentration at 1% with a meeting days away is a pure resolution-driven flush, desks can confirm the market prices a super-sized July hike as essentially off the table.
