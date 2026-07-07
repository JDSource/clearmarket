---
signal_id: "CMSIG20260707VS03"
signal_slug: "will-democratics-win-the-senate-race-in-vol-273644"
headline: "Democrats win Maine Senate: 57% on $274K spike"
semantic_title: "Maine Senate Democratic hold sits at narrow majority odds"
telemetry: "57% · $274K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-07T10:52:51+00:00"
event_id: "CM-EVT-QVFGZVBLK6"
event_slug: "senateme-26"
event_question: "Will the Maine Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEME-26-D"
  question_raw: "Will Democratics win the Senate race in Maine?"
  current_price: 0.57
  volume_24h_usd: 273644.33
  volume_cumulative_usd: 824934.52
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "57% reflects a lean-Democrat outlook, consistent with a contested but structurally favorable race."
  - "Kalshi records $274K in 24h, 33% of all-time, suggesting Platner dropout news is reshaping the field."
  - "Volume spike directly linked to Spike 0: Platner exit materially alters the Republican primary and general map."
  - "Contract resolves on Democrats winning Maine's 2026 U.S. Senate general election."
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
      kalshi_vol_24h_usd: 273644.33
sources:
  - label: "ClearMarket market record: Will the Maine Senate race be decided by January 4, 202"
    url: "https://clearmarket.fyi/events/senateme-26"
    retrieved_at: "2026-07-07T10:52:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This flow is a downstream consequence of the Platner dropout contract; desks tracking Senate control probabilities should model the Maine seat as moving toward Democrats given Republican field disruption.
