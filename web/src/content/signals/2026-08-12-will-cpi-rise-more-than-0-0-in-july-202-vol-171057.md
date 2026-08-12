---
signal_id: "CMSIG20260812VS03"
signal_slug: "will-cpi-rise-more-than-0-0-in-july-202-vol-171057"
headline: "July CPI above 0.0%: 63% on $171K inflow"
semantic_title: "Odds favor a positive July CPI print on fresh volume"
telemetry: "63% · $171K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-HVKDYMRT39"
event_slug: "kxcpi-26jul"
event_question: "CPI month-over-month change, July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUL-T0.0"
  question_raw: "Will CPI rise more than 0.0% in July 2026?"
  current_price: 0.63
  volume_24h_usd: 171057.4
  volume_cumulative_usd: 299313.59
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-11T13:56:00Z"
bullets:
  - "Kalshi prices a positive July CPI monthly change at 63%, modest inflation lean, not a strong conviction."
  - "$171K in 24h is 57% of all-time volume, suggesting this market is relatively new and drawing first-time positioning."
  - "Trading ahead of the August CPI release date implies desks are laying risk before the data drop."
  - "Resolves on the BLS July 2026 CPI monthly change figure."
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
      kalshi_vol_24h_usd: 171057.4
sources:
  - label: "ClearMarket market record: CPI month-over-month change, July 2026"
    url: "https://clearmarket.fyi/events/kxcpi-26jul"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume at a 63% price signals pre-release positioning rather than post-data certainty, a desk running rates or inflation trades should note the market is not yet strongly committed to a direction.
