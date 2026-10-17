---
signal_id: "CMSIG20261017VS06"
signal_slug: "will-mar-a-jes-s-montero-be-the-next-pri-vol-15000"
headline: "Montero Spain PM: 0% on $15K Polymarket surge"
semantic_title: "Montero as Spain's next PM trades at zero on fresh volume"
telemetry: "0% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T07:48:43+00:00"
event_id: "CM-EVT-D9KHM803Y2"
event_slug: "next-prime-minister-of-spain-20260625005215443"
event_question: "Who will be the next Prime Minister of Spain?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48e2b67721830dd1a9e187827b6ec4dc8d3f41732f12ce9f44717b187001bb3a"
  question_raw: "Will María Jesús Montero be the next Prime Minister of Spain?"
  current_price: 0.001
  volume_24h_usd: 15000.0
  volume_cumulative_usd: 34981.28699999999
  arbitration_model: "uma_oracle"
  resolves_at: "2028-03-31T23:59:00Z"
bullets:
  - "Polymarket prices María Jesús Montero becoming Spain's next Prime Minister at effectively 0%."
  - "$15K in 24h is 43% of all-time volume, significant activity for a market priced at zero."
  - "Volume at 0% likely reflects position cleanup, final arbitrage, or traders closing residual longs after a political development ruled out her path."
  - "Resolves upon Spain's next Prime Minister taking office."
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
      poly_vol_24h_usd: 15000.0
sources:
  - label: "ClearMarket market record: Who will be the next Prime Minister of Spain?"
    url: "https://clearmarket.fyi/events/next-prime-minister-of-spain-20260625005215443"
    retrieved_at: "2026-10-17T07:48:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume into a zero-priced contract signals the market has reached consensus closure, desks can treat this as a resolved directional call and focus on who the remaining PM candidates are.
