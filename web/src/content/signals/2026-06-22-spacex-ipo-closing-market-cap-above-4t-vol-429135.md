---
signal_id: "CMSIG20260622VS06"
signal_slug: "spacex-ipo-closing-market-cap-above-4t-vol-429135"
headline: "SpaceX IPO above $4T: 0% on $429K surge"
semantic_title: "SpaceX $4T IPO valuation written off by Polymarket capital"
telemetry: "0% · $429K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-22T13:33:01+00:00"
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
  - "Polymarket prices SpaceX closing above $4T at 0%, market has fully dismissed this scenario."
  - "24h volume of $429K is 48% of all-time, unusually high for a contract priced at zero."
  - "Volume at 0% typically reflects either final settlement liquidation or speculative lottery buying at negligible cost."
  - "Resolves at IPO close; $4T would require a near-doubling of the consensus $2T, $2.2T band."
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
    retrieved_at: "2026-06-22T13:33:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge at 0% on the $4T contract is a late-stage liquidity event, a desk should monitor for any residual speculative positioning rather than treat this as directional signal.
