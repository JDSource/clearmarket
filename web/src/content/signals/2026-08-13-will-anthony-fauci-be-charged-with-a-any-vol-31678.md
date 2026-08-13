---
signal_id: "CMSIG20260813VS06"
signal_slug: "will-anthony-fauci-be-charged-with-a-any-vol-31678"
headline: "Fauci charged by Jan 2027: 49% on $32K surge"
semantic_title: "Fauci criminal charge odds sit at the line on fresh volume"
telemetry: "49% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-13T09:08:38+00:00"
event_id: "CM-EVT-69K59CM028"
event_slug: "kxfederalcharge-27jan01"
event_question: "Will someone be charged with a federal crime in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDERALCHARGE-27JAN01-AFAU"
  question_raw: "Will Anthony Fauci be charged with a any crime before Jan 1, 2027?"
  current_price: 0.49
  volume_24h_usd: 31678.69
  volume_cumulative_usd: 103981.35
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a Fauci criminal charge before Jan 1, 2027 at 49%, effectively no market consensus."
  - "30% of all-time volume hit in 24 hours, suggesting renewed attention tied to DOJ or congressional activity."
  - "A dead-even price means the market is genuinely split, unresolved political and legal signals are driving uncertainty."
  - "Resolves YES if any criminal charge is filed against Fauci before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 31678.69
sources:
  - label: "ClearMarket market record: Will someone be charged with a federal crime in 2026?"
    url: "https://clearmarket.fyi/events/kxfederalcharge-27jan01"
    retrieved_at: "2026-08-13T09:08:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 49% price on a high-profile political-legal contract absorbing 30% of its lifetime volume in one day signals a desk that a prosecutorial or congressional development may be imminent or recently reported.
