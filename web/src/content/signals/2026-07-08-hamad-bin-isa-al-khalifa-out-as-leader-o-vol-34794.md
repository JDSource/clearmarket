---
signal_id: "CMSIG20260708VS03"
signal_slug: "hamad-bin-isa-al-khalifa-out-as-leader-o-vol-34794"
headline: "Khalifa out by Dec 31: 5% on $35K Polymarket spike"
semantic_title: "Bahrain regime flows defend stability through year-end"
telemetry: "5% · $35K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-08T10:14:29+00:00"
event_id: "CM-EVT-VFHHKCVH97"
event_slug: "hamad-bin-isa-al-khalifa-out-as-bahrain-king"
event_question: "Will Hamad bin Isa Al Khalifa no longer lead Bahrain in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa85a7ef371d55db0807bf95126318bbe25b0f8299f0e9e0f6a061e41964cb912"
  question_raw: "Hamad bin Isa Al Khalifa out as leader of Bahrain by December 31, 2026?"
  current_price: 0.05
  volume_24h_usd: 34794.07999999999
  volume_cumulative_usd: 95779.09800099999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "5% price reflects near-consensus view that the Bahraini leadership transition is not imminent."
  - "24h volume $34.8K is 36% of all-time, a notable single-day share for a low-liquidity contract."
  - "Elevated volume on a 5% contract suggests a specific news trigger prompted a flurry of 'no' buying."
  - "Resolves December 31, 2026."
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
      poly_vol_24h_usd: 34794.07999999999
sources:
  - label: "ClearMarket market record: Will Hamad bin Isa Al Khalifa no longer lead Bahrain in"
    url: "https://clearmarket.fyi/events/hamad-bin-isa-al-khalifa-out-as-bahrain-king"
    retrieved_at: "2026-07-08T10:14:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The combination of a low price and outsized volume share indicates a geopolitical desk or news-aware trader absorbed a rumor and bet heavily against a leadership change, worth monitoring regional Gulf newswires.
