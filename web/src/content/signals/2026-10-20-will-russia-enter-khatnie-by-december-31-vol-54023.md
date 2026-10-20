---
signal_id: "CMSIG20261020VS01"
signal_slug: "will-russia-enter-khatnie-by-december-31-vol-54023"
headline: "Russia enters Khatnie by Dec 31: 27% on $54K spike"
semantic_title: "Traders pile into Russia taking Khatnie by year-end at 27%"
telemetry: "27% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T07:48:28+00:00"
event_id: "CM-EVT-KR1P3ML5Y6"
event_slug: "will-russia-enter-khatnie-by"
event_question: "Will Russia enter Khatnie by June 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x41026240b7e9da9e447ba71d113c8e09dd0fff1bafa3a4a8ec38febe12d43f7a"
  question_raw: "Will Russia enter Khatnie by December 31, 2026?"
  current_price: 0.27
  volume_24h_usd: 54023.36740799999
  volume_cumulative_usd: 69785.29871499997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 27% odds on Russian forces entering Khatnie by December 31, a meaningful but minority probability."
  - "$54K in 24h represents 77% of all-time volume, making this one of the most concentrated single-session surges in the batch."
  - "77% of lifetime volume in one day points to a very recent tactical development or battlefield report driving fresh positioning."
  - "Resolves December 31, 2026; at 27% the market sees it as a live but non-base-case scenario."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 54023.36740799999
sources:
  - label: "ClearMarket market record: Will Russia enter Khatnie by June 2026?"
    url: "https://clearmarket.fyi/events/will-russia-enter-khatnie-by"
    retrieved_at: "2026-10-20T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly the entire lifetime liquidity of this contract printing in one session signals a specific front-line development that desks tracking Eastern European conflict exposure need to verify immediately.
