---
signal_id: "CMSIG20260831VS03"
signal_slug: "will-the-republican-party-win-the-md-01-vol-12323"
headline: "MD-01 GOP House seat: 92% on $12K volume"
semantic_title: "Heavy trading backs the GOP hold in Maryland's 1st District"
telemetry: "92% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-31T15:48:06+00:00"
event_id: "CM-EVT-XY0NDB9QD2"
event_slug: "md-01-house-election-winner"
event_question: "Will the MD-01 House seat be won by a Democrat or Republican in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf4ad902ef8628285f6f1e5b2a993a0d426363a93d45c2084b328cd0a371d4f27"
  question_raw: "Will the Republican Party win the MD-01 House seat?"
  current_price: 0.92
  volume_24h_usd: 12323.473332
  volume_cumulative_usd: 33313.95183400001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans winning MD-01 at 92%, a near-lock in a historically red district."
  - "24h volume of $12.3K is 37% of all-time, showing renewed positioning on this race."
  - "Surge may reflect a candidate announcement, primary result, or updated Cook/Sabato rating."
  - "Resolves on November 2026 general election results."
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
      poly_vol_24h_usd: 12323.473332
sources:
  - label: "ClearMarket market record: Will the MD-01 House seat be won by a Democrat or Repub"
    url: "https://clearmarket.fyi/events/md-01-house-election-winner"
    retrieved_at: "2026-08-31T15:48:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High-confidence, rising volume on a House seat usually means a catalyst, primary outcome or opponent quality news, is prompting traders to close out any remaining doubt before the general.
