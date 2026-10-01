---
signal_id: "CMSIG20261001VS02"
signal_slug: "will-above-70000-jobs-be-added-in-septem-vol-14768"
headline: "Sept jobs above 70K: 66% on $15K Kalshi surge"
semantic_title: "Fresh volume backs September payrolls clearing 70K jobs"
telemetry: "66% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-01T07:48:14+00:00"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "Will the September 2026 jobs report show positive job growth?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T70000"
  question_raw: "Will above 70000 jobs be added in September 2026?"
  current_price: 0.66
  volume_24h_usd: 14768.23
  volume_cumulative_usd: 21824.48
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi prices September 2026 nonfarm payrolls above 70K at 66%, a clear lean toward a solid print."
  - "68% of all-time contract volume ($15K of $22K lifetime) arrived in 24h ahead of the data release."
  - "Pre-release positioning surge is classic, ADP, jobless claims, or ISM data likely moved the needle."
  - "Resolves on the official BLS September 2026 employment report, due imminently."
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
      kalshi_vol_24h_usd: 14768.23
sources:
  - label: "ClearMarket market record: Will the September 2026 jobs report show positive job g"
    url: "https://clearmarket.fyi/events/kxpayrolls-26sep"
    retrieved_at: "2026-10-01T07:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 68% lifetime-volume flush the day before or day-of the jobs report tells a desk that positioning is lopsided to the upside, skew in rates or equity vol around the print should be monitored.
