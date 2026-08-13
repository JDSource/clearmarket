---
signal_id: "CMSIG20260813VS04"
signal_slug: "will-russia-capture-all-of-drobysheve-by-vol-29487"
headline: "Russia captures Drobysheve: 12% on $29K surge"
semantic_title: "Russia full Drobysheve capture by year-end stays a long shot"
telemetry: "12% · $29K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-13T09:08:38+00:00"
event_id: "CM-EVT-P49JZ61TB2"
event_slug: "will-russia-capture-all-of-drobysheve-by-march-31"
event_question: "Will Russia capture all of Drobysheve in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1531394070411c2e5f081a9406de4b009374808e3e832f1c1f5ddc37bb6d4ba0"
  question_raw: "Will Russia capture all of Drobysheve by December 31?"
  current_price: 0.12
  volume_24h_usd: 29487.739999999994
  volume_cumulative_usd: 35149.318240000015
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a full Russian capture of Drobysheve by Dec 31 at 12%, skepticism dominates."
  - "84% of all-time contract volume arrived in 24 hours, this market is effectively newly active."
  - "Near-total volume concentration in a single session suggests a ground-movement report or battlefield update triggered fresh attention."
  - "Resolves YES only if Russia controls all of Drobysheve before Jan 1, 2027."
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
      poly_vol_24h_usd: 29487.739999999994
sources:
  - label: "ClearMarket market record: Will Russia capture all of Drobysheve in 2026? (multi-d"
    url: "https://clearmarket.fyi/events/will-russia-capture-all-of-drobysheve-by-march-31"
    retrieved_at: "2026-08-13T09:08:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

84% of lifetime volume in one day on a conflict-territory contract tells a desk that a specific on-the-ground development is driving attention, worth cross-referencing against frontline mapping updates.
