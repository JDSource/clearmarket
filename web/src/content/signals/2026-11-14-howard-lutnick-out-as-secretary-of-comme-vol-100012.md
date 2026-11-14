---
signal_id: "CMSIG20261114VS00"
signal_slug: "howard-lutnick-out-as-secretary-of-comme-vol-100012"
headline: "Lutnick out by Dec 31: 49% on $100K surge"
semantic_title: "Lutnick exit odds sit at a coin flip into year-end"
telemetry: "49% · $100K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-14T07:48:40+00:00"
event_id: "CM-EVT-H31QLM4JT3"
event_slug: "howard-lutnick-out-as-secretary-of-commerce-by-december-31"
event_question: "Will Howard Lutnick be out as Secretary of Commerce by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7978663d03b5c053dcea87b39e06fad5bcdd036b0c7febfa4309502c02f70c2c"
  question_raw: "Howard Lutnick out as Secretary of Commerce by December 31?"
  current_price: 0.49
  volume_24h_usd: 100012.461437
  volume_cumulative_usd: 194163.083696
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Lutnick Commerce exit at 49%, effectively no lean either way."
  - "24h volume of $100K is 52% of all-time, fresh capital nearly matching total prior activity."
  - "Mid-November deadline focus sharpens; fresh attention here typically precedes a news catalyst."
  - "Resolves Dec 31, 2026, any Cabinet reshuffle signal in coming weeks is the trigger."
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
      poly_vol_24h_usd: 100012.461437
sources:
  - label: "ClearMarket market record: Will Howard Lutnick be out as Secretary of Commerce by "
    url: "https://clearmarket.fyi/events/howard-lutnick-out-as-secretary-of-commerce-by-december-31"
    retrieved_at: "2026-11-14T07:48:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-even split on a sitting Cabinet secretary's tenure, with more than half of all-time volume arriving in one session, signals desks are actively hedging administration stability risk into year-end.
