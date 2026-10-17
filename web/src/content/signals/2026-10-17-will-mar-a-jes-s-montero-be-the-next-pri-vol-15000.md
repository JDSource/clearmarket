---
signal_id: "CMSIG20261017VS05"
signal_slug: "will-mar-a-jes-s-montero-be-the-next-pri-vol-15000"
headline: "Montero Spain PM: 0% on $15K Polymarket flow"
semantic_title: "Montero as Spain PM priced at zero; volume tests the floor"
telemetry: "0% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T11:58:01+00:00"
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
  - "Polymarket prices María Jesús Montero's path to Prime Minister at 0%, a hard rejection of the scenario."
  - "24h volume of $15K is 43% of all-time, substantial flow arriving to confirm or probe the zero-price floor."
  - "Flow into a zero-priced contract typically reflects new entrants confirming consensus or seeking edge on a tail scenario."
  - "Resolves contingent on Spanish government formation or leadership transition events."
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
    retrieved_at: "2026-10-17T11:58:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Significant volume into a zero-priced political contract is a geopolitical signal worth flagging, desks covering European sovereign risk should verify whether any Spanish coalition dynamics have shifted.
