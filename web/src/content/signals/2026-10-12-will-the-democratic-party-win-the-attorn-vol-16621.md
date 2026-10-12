---
signal_id: "CMSIG20261012VS04"
signal_slug: "will-the-democratic-party-win-the-attorn-vol-16621"
headline: "Dem NY Atty General: 94% on $16.6K surge"
semantic_title: "Buyers back NY Attorney General Democratic win at 94%"
telemetry: "94% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-12T17:18:20+00:00"
event_id: "CM-EVT-2WVDLYDTS5"
event_slug: "kxattygenny-26"
event_question: "Will the New York Attorney General race be decided by January 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXATTYGENNY-26-D"
  question_raw: "Will the Democratic party win the Attorney General race in New York?"
  current_price: 0.936
  volume_24h_usd: 16621.11
  volume_cumulative_usd: 65289.15
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices Democratic victory in New York's AG race at 94%, heavy favorite with active reinforcement."
  - "24h volume of $16.6K hits exactly 25% of all-time handle, a clean milestone in a deep contract."
  - "Fresh volume at 94% suggests traders are layering into the favorite rather than fading, conviction trade."
  - "Resolves on certified New York Attorney General election result."
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
      kalshi_vol_24h_usd: 16621.11
sources:
  - label: "ClearMarket market record: Will the New York Attorney General race be decided by J"
    url: "https://clearmarket.fyi/events/kxattygenny-26"
    retrieved_at: "2026-10-12T17:18:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk reads concentrated buying at 94% as a conviction signal that the market sees no credible pathway for a Republican upset in a statewide New York race heading into election cycle close.
