---
signal_id: "CMSIG20260830VS00"
signal_slug: "will-trump-make-0-trips-to-mar-a-lago-as-vol-18979"
headline: "Trump zero Mar-a-Lago trips Aug: 99% on $18.9K surge"
semantic_title: "Trump's August Mar-a-Lago absence holds near certainty"
telemetry: "99% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-30T13:31:03+00:00"
event_id: "CM-EVT-BD8VLVHC95"
event_slug: "kxlagodays-26aug"
event_question: "Will Trump make 0 trips to Mar-a-Lago as President in Aug 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLAGODAYS-26AUG-0"
  question_raw: "Will Trump make 0 trips to Mar-a-Lago as President in Aug 2026?"
  current_price: 0.99
  volume_24h_usd: 18979.7
  volume_cumulative_usd: 49096.34
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-01T14:00:00Z"
bullets:
  - "Market prices 99%, near-certain Trump made no Mar-a-Lago visits in August 2026."
  - "24h volume of $18.9K is 39% of all-time handle, a sharp late-month settlement rush."
  - "August ends Aug 31; traders locking in positions one day before resolution explains the spike."
  - "Contract resolves imminently, volume reflects closing arbitrage, not a view shift."
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
      kalshi_vol_24h_usd: 18979.7
sources:
  - label: "ClearMarket market record: Will Trump make 0 trips to Mar-a-Lago as President in A"
    url: "https://clearmarket.fyi/events/kxlagodays-26aug"
    retrieved_at: "2026-08-30T13:31:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The surge is classic pre-resolution convergence on Kalshi: with one day left and the price at 99%, desks are collecting the last basis points before the contract settles.
