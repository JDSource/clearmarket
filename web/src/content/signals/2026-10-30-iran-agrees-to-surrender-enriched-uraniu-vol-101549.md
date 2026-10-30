---
signal_id: "CMSIG20261030VS04"
signal_slug: "iran-agrees-to-surrender-enriched-uraniu-vol-101549"
headline: "Iran uranium deal: 0% on $102K Polymarket"
semantic_title: "Iran uranium surrender by Oct 31 stays priced at zero"
telemetry: "0% · $102K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-Z3K4DFFZY1"
event_slug: "iran-agrees-to-surrender-enriched-uranium-stockpile-by"
event_question: "Will Iran agree to surrender its enriched uranium stockpile by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaff5b702feef28fd0207583e17f8f2610d8191b5951441974e166dcdb61366e2"
  question_raw: "Iran agrees to surrender enriched uranium stockpile by October 31, 2026?"
  current_price: 0.002
  volume_24h_usd: 101549.97018
  volume_cumulative_usd: 260100.47729
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-31T00:00:00Z"
bullets:
  - "0% price means Polymarket participants assign no realistic chance Iran surrenders enriched uranium by October 31."
  - "$102K in 24h is 39% of all-time volume, significant fresh capital flowing into an effectively dead contract."
  - "Volume on a 0% contract one day before the deadline suggests profit-taking or settlement positioning."
  - "Resolves October 31, 2026, tomorrow, making this the final session of meaningful liquidity."
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
      poly_vol_24h_usd: 101549.97018
sources:
  - label: "ClearMarket market record: Will Iran agree to surrender its enriched uranium stock"
    url: "https://clearmarket.fyi/events/iran-agrees-to-surrender-enriched-uranium-stockpile-by"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Six-figure volume on a 0%-priced contract expiring tomorrow signals desks are closing long-shot positions and confirming the consensus that no Iran deal materializes before the deadline.
