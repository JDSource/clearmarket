---
signal_id: "CMSIG20261011VS06"
signal_slug: "will-afghanistan-recognize-israel-by-dec-vol-18788"
headline: "Afghanistan-Israel recognition: 3% on $19K"
semantic_title: "Afghanistan recognizing Israel by December 31 trades at 3%"
telemetry: "3% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-11T14:36:40+00:00"
event_id: "CM-EVT-2KCBS1KX88"
event_slug: "which-countries-will-recognize-israel-by-december-31"
event_question: "Which countries will recognize Israel by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7ba4447c532f6c634be6657261acb7e47ab916658f358ec13b1bcc99fdfda929"
  question_raw: "Will Afghanistan recognize Israel by December 31?"
  current_price: 0.031
  volume_24h_usd: 18788.722375999998
  volume_cumulative_usd: 40202.534220999994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T17:00:00Z"
bullets:
  - "Polymarket prices Afghanistan recognizing Israel by year-end at 3%, effectively zero probability."
  - "47% of all-time volume hit in 24 hours, a notable surge into a geopolitically implausible contract."
  - "Likely linked to the same diplomatic news cycle driving the Pakistan-Israel spike, traders testing related claims."
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
      poly_vol_24h_usd: 18788.722375999998
sources:
  - label: "ClearMarket market record: Which countries will recognize Israel by December 31?"
    url: "https://clearmarket.fyi/events/which-countries-will-recognize-israel-by-december-31"
    retrieved_at: "2026-10-11T14:36:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Parallel spikes in Afghanistan and Pakistan recognition contracts suggest a common news trigger; a desk should watch regional diplomatic headlines for the underlying catalyst.
