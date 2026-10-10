---
signal_id: "CMSIG20261010VS04"
signal_slug: "will-the-democratic-party-win-the-attorn-vol-15644"
headline: "NY Dem AG: 91% on $16K volume spike"
semantic_title: "NY AG odds hold near certainty as fresh volume arrives"
telemetry: "91% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-2WVDLYDTS5"
event_slug: "kxattygenny-26"
event_question: "Will the New York Attorney General race be decided by January 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXATTYGENNY-26-D"
  question_raw: "Will the Democratic party win the Attorney General race in New York?"
  current_price: 0.909
  volume_24h_usd: 15644.41
  volume_cumulative_usd: 35581.89
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning New York's Attorney General race at 91%, near-certain favorite territory."
  - "44% of all-time volume, $16K, printed in one session, indicating renewed market attention at an extreme price."
  - "Fresh volume at 91% odds typically reflects either late position-taking on the favorite or thin short-side liquidity being removed."
  - "Resolves on 2026 New York Attorney General election outcome."
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
      kalshi_vol_24h_usd: 15644.41
sources:
  - label: "ClearMarket market record: Will the New York Attorney General race be decided by J"
    url: "https://clearmarket.fyi/events/kxattygenny-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should flag that volume concentration at 91% in a statewide AG race may indicate event-driven attention, such as a legal development or candidate news, worth monitoring for downstream implications.
