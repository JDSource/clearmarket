---
signal_id: "CMSIG20260604VS06"
signal_slug: "will-bitcoin-dip-to-55-000-in-june-vol-226297"
headline: "BTC dip to $55K in June: 14% on $226K"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-04T11:15:28+00:00"
event_id: "CM-EVT-3PF6P6GGK5"
event_slug: "what-price-will-bitcoin-hit-in-june-2026"
event_question: "Will Bitcoin's price reach a specific level in June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xadebd6bbf401c9509dd2e78b65a16b567f1f386dccd8cac86cd389bb53ec3a58"
  question_raw: "Will Bitcoin dip to $55,000 in June?"
  current_price: 0.138
  volume_24h_usd: 226297.9937449999
  volume_cumulative_usd: 300883.1541469998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-01T04:00:00Z"
bullets:
  - "Polymarket prices 14% chance Bitcoin touches $55K during June 2026."
  - "Polymarket: $226K 24h, 75% of $300K all-time; concentrated speculative flow on deep-downside tail."
  - "14% on a further ~15% leg down from $65K range reflects meaningful but minority tail-risk pricing."
  - "Resolves end of June; paired with $65K contract, implies market sees $65K likely but $55K as low-probability extension."
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
      poly_vol_24h_usd: 226297.9937449999
sources:
  - label: "ClearMarket market record: Will Bitcoin's price reach a specific level in June?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-in-june-2026"
    retrieved_at: "2026-06-04T11:15:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

14% at $55K alongside 87% at $65K gives desks a clean implied distribution, BTC downside consensus anchors around $65K with a 1-in-7 chance of a deeper capitulation to $55K this month.
