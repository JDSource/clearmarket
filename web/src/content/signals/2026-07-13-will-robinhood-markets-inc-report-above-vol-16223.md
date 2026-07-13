---
signal_id: "CMSIG20260713VS02"
signal_slug: "will-robinhood-markets-inc-report-above-vol-16223"
headline: "Robinhood Q2 funded customers >27.7M: 98% on $16K"
semantic_title: "Robinhood funded-customer beat sits near certainty ahead of Q2 print"
telemetry: "98% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-13T10:56:44+00:00"
event_id: "CM-EVT-QHYZG7JK22"
event_slug: "kxhood-26julfunded"
event_question: "Robinhood funded customers, July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOOD-26JULFUNDED-P27700000.0"
  question_raw: "Will Robinhood Markets Inc. report above 27.7 million funded customers in Q2 2026?"
  current_price: 0.98
  volume_24h_usd: 16223.99
  volume_cumulative_usd: 33403.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-28T20:00:00Z"
bullets:
  - "98% price reflects near-consensus that Robinhood clears 27.7M funded customers in Q2 2026."
  - "24h volume $16K is 49% of all-time, renewed positioning ahead of Q2 earnings disclosure."
  - "Surge likely reflects Q2 report imminent or already scheduled, drawing last-minute directional flow."
  - "Resolves on official Q2 customer count report; residual 2% discount reflects execution or reporting risk."
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
      kalshi_vol_24h_usd: 16223.99
sources:
  - label: "ClearMarket market record: Robinhood funded customers, July 2026"
    url: "https://clearmarket.fyi/events/kxhood-26julfunded"
    retrieved_at: "2026-07-13T10:56:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing with fresh volume near the report date suggests the desk community views the 27.7M threshold as a formality, but is actively closing out hedges or adding late confirmation exposure.
