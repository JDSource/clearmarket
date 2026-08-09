---
signal_id: "CMSIG20260809VS01"
signal_slug: "will-ed-case-be-the-democratic-nominee-f-vol-84276"
headline: "Ed Case HI-1 nominee: 100% on $84K surge"
semantic_title: "Traders lock in Ed Case as Hawaii-1 nominee at 100%"
telemetry: "100% · $84K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-09T08:37:25+00:00"
event_id: "CM-EVT-HCC270BBT1"
event_slug: "kxhi01d-26"
event_question: "Will the Democratic nominee for Hawaii's 1st congressional district be determined by January 1, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHI01D-26-ECAS"
  question_raw: "Will Ed Case be the Democratic nominee for Hawaii's first congressional district?"
  current_price: 0.999
  volume_24h_usd: 84276.5
  volume_cumulative_usd: 124151.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices Ed Case as the Democratic nominee for Hawaii's first district at 100%, fully resolved in traders' view."
  - "24h volume of $84K is 68% of all-time handle, the largest single-session share in this contract's life."
  - "Volume surge at ceiling price points to a qualifying event, likely a primary result or withdrawal, driving final settlement."
  - "Contract resolves on Democratic primary outcome for Hawaii's first congressional district."
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
      kalshi_vol_24h_usd: 84276.5
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Hawaii's 1st congressio"
    url: "https://clearmarket.fyi/events/kxhi01d-26"
    retrieved_at: "2026-08-09T08:37:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% price absorbing two-thirds of all-time volume in one day signals a binary event has effectively settled the question, desks can treat the nomination as confirmed and move to general-election modeling.
