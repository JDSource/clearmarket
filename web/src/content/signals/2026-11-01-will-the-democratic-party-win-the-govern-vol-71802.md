---
signal_id: "CMSIG20261101VS01"
signal_slug: "will-the-democratic-party-win-the-govern-vol-71802"
headline: "Maryland Dem governor: 99% on $72K surge"
semantic_title: "Maryland governor odds stay near certain with a volume surge"
telemetry: "99% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T14:43:30+00:00"
event_id: "CM-EVT-RYZ7GGP8S0"
event_slug: "govpartymd-26"
event_question: "Maryland Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYMD-26-D"
  question_raw: "Will the Democratic party win the governorship in Maryland"
  current_price: 0.99
  volume_24h_usd: 71802.53
  volume_cumulative_usd: 102945.55
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-18T15:00:00Z"
bullets:
  - "At 99% on Kalshi, the market treats a Democratic Maryland governorship as near-certain."
  - "$72K in 24h is 70% of all-time volume, an extraordinary concentration implying late one-sided flow to lock in the edge."
  - "Maryland is a reliably blue state; surge likely reflects traders closing positions or arbitraging residual risk at the limit."
  - "Resolves on certified 2026 Maryland gubernatorial result."
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
      kalshi_vol_24h_usd: 71802.53
sources:
  - label: "ClearMarket market record: Maryland Governor winner?"
    url: "https://clearmarket.fyi/events/govpartymd-26"
    retrieved_at: "2026-11-01T14:43:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Seventy percent of all-time volume printing in a single day on a 99% contract suggests late-stage position squaring, a desk signal that the Maryland race is effectively closed.
