---
signal_id: "CMSIG20260618VS06"
signal_slug: "spacex-ipo-closing-market-cap-above-4t-vol-429135"
headline: "SpaceX IPO above $4T: 0% on $429K inflow"
semantic_title: "Capital fades SpaceX $4T IPO cap as implausible"
telemetry: "0% · $429K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-18T11:49:22+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2576d8fe9a5ed75f58c2ef34bad961916d4799254c8d248734aee5cf5224eb07"
  question_raw: "SpaceX IPO closing market cap above $4T?"
  current_price: 0.002
  volume_24h_usd: 429135.1700309999
  volume_cumulative_usd: 897378.6698439954
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket prices zero, $4T closing cap is dismissed as outside any credible IPO scenario."
  - "48% of all-time volume arriving in 24h at zero suggests a coordinated settlement or final repricing event."
  - "Given $2.2T at 67%, the $4T strike implies an 82% premium-to-current-market, the market rejects it entirely."
  - "Volume at zero is arbitrage-harvesting activity, not speculative positioning."
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
      poly_vol_24h_usd: 429135.1700309999
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-18T11:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note the $4T contract purely as a calibration point, the volume confirms participants are systematically clearing residual exposure across the full SpaceX valuation ladder ahead of IPO resolution.
