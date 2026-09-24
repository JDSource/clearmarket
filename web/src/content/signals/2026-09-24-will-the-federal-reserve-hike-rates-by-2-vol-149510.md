---
signal_id: "CMSIG20260924VS00"
signal_slug: "will-the-federal-reserve-hike-rates-by-2-vol-149510"
headline: "Fed Oct hike: 66% on $150K surge"
semantic_title: "Heavy trading backs a Fed October hike at 2-in-3 odds"
telemetry: "66% · $150K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T07:48:17+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H25"
  question_raw: "Will the Federal Reserve Hike rates by 25bps at their October 2026 meeting?"
  current_price: 0.66
  volume_24h_usd: 149510.72
  volume_cumulative_usd: 530404.89
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "Kalshi prices a 25bps October hike at 66%, market treats a move as the base case."
  - "$149.5K traded in 24h, equal to 28% of the contract's entire all-time volume."
  - "Fresh capital arriving weeks before the October meeting signals rate-path repricing is live."
  - "Resolves on the FOMC decision; any intervening CPI or jobs data will move this sharply."
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
      kalshi_vol_24h_usd: 149510.72
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-24T07:48:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A two-thirds probability on a near-term Fed hike drawing $150K in a single session tells rates desks the market is treating October as a live meeting, worth tracking alongside Fed funds futures for basis.
