---
signal_id: "CMSIG20260804VS04"
signal_slug: "will-haley-stevens-be-the-democratic-nom-vol-31998"
headline: "Stevens MI Senate nominee: 2% on $32K flow"
semantic_title: "Haley Stevens Michigan Senate odds slip to near zero"
telemetry: "2% · $32K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-04T10:33:57+00:00"
event_id: "CM-EVT-ZMWFMPNXD9"
event_slug: "kxsenatemid-26"
event_question: "Will the Michigan Democratic Senate nominee be determined by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEMID-26-HSTE"
  question_raw: "Will Haley Stevens be the Democratic nominee for the Senate in Michigan?"
  current_price: 0.02
  volume_24h_usd: 31998.4
  volume_cumulative_usd: 102177.52
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "At 2%, Kalshi has effectively ruled Stevens out of the Michigan Democratic Senate nomination."
  - "24h volume of $32K represents 31% of all-time, fresh capital is arriving to confirm, not contest, the near-zero price."
  - "Volume alongside the El-Sayed and Thanedar/McKinney contracts suggests a broad Michigan primary repricing session."
  - "Resolves on the certified 2026 Michigan Democratic Senate primary result."
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
      kalshi_vol_24h_usd: 31998.4
sources:
  - label: "ClearMarket market record: Will the Michigan Democratic Senate nominee be determin"
    url: "https://clearmarket.fyi/events/kxsenatemid-26"
    retrieved_at: "2026-08-04T10:33:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-zero pricing with 31% of lifetime volume in a single day indicates the market is mopping up residual Stevens probability, a desk should treat her path as closed barring an extraordinary development.
