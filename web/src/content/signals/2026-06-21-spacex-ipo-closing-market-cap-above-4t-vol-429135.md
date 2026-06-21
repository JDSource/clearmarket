---
signal_id: "CMSIG20260621VS06"
signal_slug: "spacex-ipo-closing-market-cap-above-4t-vol-429135"
headline: "SpaceX IPO above $4T: 0% on $429K inflow"
semantic_title: "Capital dismisses SpaceX crossing $4T at IPO close"
telemetry: "0% · $429K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-21T11:14:34+00:00"
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
  - "Polymarket at 0%, no credible probability assigned to a $4T closing market cap."
  - "24h volume $429K equals 48% of all-time; residual buyers fully absorbed and rejected."
  - "$4T would imply roughly double the $2T consensus floor, market treats it as fantasy."
  - "Zero price with near-half lifetime volume suggests terminal no-resolution flush."
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
    retrieved_at: "2026-06-21T11:14:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $4T strike is being zeroed out in real time, a desk can use this as a hard ceiling reference and close any book exposure above that level without meaningful counter-party risk.
