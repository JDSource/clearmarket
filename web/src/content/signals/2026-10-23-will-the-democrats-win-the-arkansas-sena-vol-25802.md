---
signal_id: "CMSIG20261023VS05"
signal_slug: "will-the-democrats-win-the-arkansas-sena-vol-25802"
headline: "Arkansas Senate Dem: 4% on $26K, 59% of all-time"
semantic_title: "Democrats in Arkansas stay a long shot at 4% odds"
telemetry: "4% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T07:49:03+00:00"
event_id: "CM-EVT-GC5J8DX6R3"
event_slug: "arkansas-senate-election-winner"
event_question: "Will a Republican win the Arkansas Senate election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfd583ce731a731f6500cf5427090f1e708ec102140146200306b56c489ed4364"
  question_raw: "Will the Democrats win the Arkansas Senate race in 2026?"
  current_price: 0.042
  volume_24h_usd: 25802.174279999996
  volume_cumulative_usd: 43722.96300799999
  arbitration_model: "uma_oracle"
bullets:
  - "4% price on polymarket leaves the Arkansas Senate seat firmly in Republican hands by market consensus."
  - "$25,802 in 24h is 59% of all-time volume, more than half the contract's lifetime traded in a single session."
  - "A spike of this size into a 4% contract may reflect a political event or filing development drawing speculative attention."
  - "Resolves on 2026 Arkansas Senate general election."
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
      poly_vol_24h_usd: 25802.174279999996
sources:
  - label: "ClearMarket market record: Will a Republican win the Arkansas Senate election?"
    url: "https://clearmarket.fyi/events/arkansas-senate-election-winner"
    retrieved_at: "2026-10-23T07:49:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When 59% of a contract's lifetime volume trades in one day against a 4% price, a desk should investigate whether a specific candidate filing or news event in Arkansas triggered speculative positioning, or whether this is a pure liquidity-driven flush.
