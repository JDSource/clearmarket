---
signal_id: "CMSIG20261106VS03"
signal_slug: "will-chuck-schumer-be-the-next-senate-ma-vol-37392"
headline: "Schumer Senate majority leader: 83% on $37K"
semantic_title: "Schumer majority leader odds hold at 83% through fresh buying"
telemetry: "83% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T15:37:54+00:00"
event_id: "CM-EVT-ZZZ60Y4302"
event_slug: "next-senate-majority-leader-485"
event_question: "Who will be the Senate Majority Leader in the next Congress?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x99dcf0abf02cdbd62e6a17a95c68f7864be5f5779d25d44cf7ea134f5d7979a9"
  question_raw: "Will Chuck Schumer be the next Senate Majority Leader?"
  current_price: 0.83
  volume_24h_usd: 37392.481849
  volume_cumulative_usd: 69116.35456200001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-03T00:00:00Z"
bullets:
  - "At 83%, Polymarket assigns Schumer a strong but not certain grip on the majority leader role."
  - "$37K in 24h covers 54% of all-time volume, the majority of price discovery is happening today."
  - "Volume spike may reflect Senate procedural news or a leadership challenge drawing fresh attention."
  - "Resolution tied to formal Senate Democratic caucus leadership selection."
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
      poly_vol_24h_usd: 37392.481849
sources:
  - label: "ClearMarket market record: Who will be the Senate Majority Leader in the next Cong"
    url: "https://clearmarket.fyi/events/next-senate-majority-leader-485"
    retrieved_at: "2026-11-06T15:37:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half of all-time volume arriving in one session on a high-probability contract suggests a specific Senate leadership development is in play, desks tracking legislative risk on budget or regulatory items should watch for caucus signaling.
