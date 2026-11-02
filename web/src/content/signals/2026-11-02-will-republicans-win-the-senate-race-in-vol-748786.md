---
signal_id: "CMSIG20261102VS00"
signal_slug: "will-republicans-win-the-senate-race-in-vol-748786"
headline: "Michigan Senate GOP: 23% on $749K volume surge"
semantic_title: "Heavy trading tests a long-shot GOP hold in Michigan Senate"
telemetry: "23% · $749K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T17:45:32+00:00"
event_id: "CM-EVT-GBSY094P67"
event_slug: "senatemi-26"
event_question: "Michigan Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMI-26-R"
  question_raw: "Will Republicans win the Senate race in Michigan?"
  current_price: 0.23
  volume_24h_usd: 748786.64
  volume_cumulative_usd: 2890216.72
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 23%, market treats a GOP Michigan Senate win as a clear underdog outcome."
  - "24h volume of $749K is 26% of all-time flow, marking one of the contract's heaviest single-day sessions."
  - "Michigan is a key Democratic-held seat; fresh capital at this price suggests positioning around a contested battlefield map."
  - "Resolves on 2026 midterm Election Day results."
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
      kalshi_vol_24h_usd: 748786.64
sources:
  - label: "ClearMarket market record: Michigan Senate winner?"
    url: "https://clearmarket.fyi/events/senatemi-26"
    retrieved_at: "2026-11-02T17:45:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A sharp single-day surge on a 23% contract signals desks are actively hedging or speculating on tail-risk GOP pickups in the upper Midwest as midterm maps firm up.
