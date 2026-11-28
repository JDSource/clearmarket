---
signal_id: "CMSIG20261128VS00"
signal_slug: "will-miguel-tellado-be-the-next-prime-mi-vol-92277"
headline: "Tellado Spain PM: 0% on $92K surge"
semantic_title: "Tellado PM bid stays dead as fresh volume tests the floor"
telemetry: "0% · $92K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-28T07:48:37+00:00"
event_id: "CM-EVT-D9KHM803Y2"
event_slug: "next-prime-minister-of-spain-20260625005215443"
event_question: "Who will be the next Prime Minister of Spain?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd3b68cd44f465f6c4090950f247368148292a6cedea926032c846f952015a4b9"
  question_raw: "Will Miguel Tellado be the next Prime Minister of Spain?"
  current_price: 0.001
  volume_24h_usd: 92277.53
  volume_cumulative_usd: 266877.256
  arbitration_model: "uma_oracle"
  resolves_at: "2028-03-31T23:59:00Z"
bullets:
  - "Polymarket prices Tellado at 0%, the market sees no credible path to the premiership."
  - "24h volume of $92K is 35% of all-time, a sharp burst of fresh attention on a dormant contract."
  - "Surge likely reflects renewed Spanish political speculation, possibly coalition or no-confidence chatter driving traders to confirm the floor."
  - "Contract resolves on whether Tellado is named next PM; current odds leave no room for doubt."
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
      poly_vol_24h_usd: 92277.53
sources:
  - label: "ClearMarket market record: Who will be the next Prime Minister of Spain?"
    url: "https://clearmarket.fyi/events/next-prime-minister-of-spain-20260625005215443"
    retrieved_at: "2026-11-28T07:48:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 35% all-time volume spike settling at 0% signals the market is being stress-tested by political noise around Spanish coalition dynamics, desks should watch for a no-confidence motion or early-election headline as the likely catalyst.
