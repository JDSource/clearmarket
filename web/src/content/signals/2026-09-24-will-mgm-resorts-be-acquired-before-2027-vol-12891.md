---
signal_id: "CMSIG20260924VS07"
signal_slug: "will-mgm-resorts-be-acquired-before-2027-vol-12891"
headline: "MGM Resorts acquired by 2027: 4% on $13K"
semantic_title: "MGM Resorts acquisition odds stay at 4% despite fresh bets"
telemetry: "4% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-24T13:08:49+00:00"
event_id: "CM-EVT-QQ0N50YK83"
event_slug: "which-companies-will-be-acquired-before-2027"
event_question: "Which companies will be acquired before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb957a0c805d53d96f666fd5c0ea0f70535ca092bfd55fc07ba9b782e3d3d249"
  question_raw: "Will MGM Resorts be acquired before 2027?"
  current_price: 0.04
  volume_24h_usd: 12891.129957999998
  volume_cumulative_usd: 38673.882357999995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "4% odds on Polymarket reflect deep market skepticism that MGM Resorts closes an acquisition before 2027."
  - "$13K in 24h covers 33% of all-time volume, notable engagement for a near-zero-priced contract."
  - "Fresh volume on a 4% contract typically signals speculative positioning on a low-probability corporate event."
  - "Resolves if MGM Resorts announces a completed acquisition before January 1, 2027."
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
      poly_vol_24h_usd: 12891.129957999998
sources:
  - label: "ClearMarket market record: Which companies will be acquired before 2027?"
    url: "https://clearmarket.fyi/events/which-companies-will-be-acquired-before-2027"
    retrieved_at: "2026-09-24T13:08:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

One-third of all-time volume on a 4% contract in a single session is a flag for event-driven desks, either informed speculation on an unconfirmed approach or a liquidity-seeking lottery trade worth monitoring for follow-through.
