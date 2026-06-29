---
signal_id: "CMSIG20260629VS01"
signal_slug: "will-lebanon-recognize-israel-by-june-30-vol-349485"
headline: "Lebanon recognizes Israel: 18% on $349K inflow"
semantic_title: "Heavy flows fade Lebanon-Israel recognition by June 30"
telemetry: "18% · $349K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-29T12:29:31+00:00"
event_id: "CM-EVT-C44TBGCDK8"
event_slug: "which-countries-will-recognize-israel-by-june-30"
event_question: "Will additional countries recognize Israel by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x274cec202608757e62a0cf64ec63a3a814a6cc23a1bff1819b437362c5c16732"
  question_raw: "Will Lebanon recognize Israel by June 30?"
  current_price: 0.176
  volume_24h_usd: 349485.5637720003
  volume_cumulative_usd: 646170.2598100009
  arbitration_model: "uma_oracle"
bullets:
  - "18% prices the outcome as a long shot, markets assign roughly 4-in-5 odds against recognition this month."
  - "$349K in 24h represents 54% of all-time volume, suggesting a sharp catalyst or influential position shift."
  - "Spike this close to the June 30 deadline implies either a rumor triggering buyers or large holders liquidating longs."
  - "Contract expires tomorrow; unresolved diplomatic status makes the 18% print a residual risk premium."
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
      poly_vol_24h_usd: 349485.5637720003
sources:
  - label: "ClearMarket market record: Will additional countries recognize Israel by June 30?"
    url: "https://clearmarket.fyi/events/which-countries-will-recognize-israel-by-june-30"
    retrieved_at: "2026-06-29T12:29:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

For a geopolitical desk, the sudden volume concentration one day before expiry on an 18% contract warrants checking whether back-channel normalization talks produced a leak or whether this is simply late short-side covering.
