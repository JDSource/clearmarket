---
signal_id: "CMSIG20261016VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-14447"
headline: "Fed Jan 2027 hike: 25% on $14K Kalshi surge"
semantic_title: "Odds of a January Fed hike hold at 25%"
telemetry: "25% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-16T12:59:44+00:00"
event_id: "CM-EVT-NPLFGMTJW3"
event_slug: "kxfeddecision-27jan"
event_question: "Will the Federal Reserve make a decision in January 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-27JAN-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their January 2027 meeting?"
  current_price: 0.25
  volume_24h_usd: 14447.89
  volume_cumulative_usd: 31416.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-27T19:05:00Z"
bullets:
  - "Kalshi prices a 25bps January 2027 Fed hike at exactly 25%, a live tail risk, not consensus."
  - "24h volume of $14K represents 46% of all-time activity, a sharp single-day acceleration."
  - "Fresh positioning likely triggered by inflation data or Fed communication shifting rate-path expectations."
  - "Contract resolves on the January 2027 FOMC decision."
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
      kalshi_vol_24h_usd: 14447.89
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in January 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-27jan"
    retrieved_at: "2026-10-16T12:59:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-half of all-time volume printing in one day at the 25% level tells a macro desk that rate-hike tail risk is being actively repriced and warrants updating January 2027 curve exposure.
