---
signal_id: "CMSIG20260907VS01"
signal_slug: "will-carleigh-beriont-be-the-democratic-vol-12250"
headline: "Beriont NH-01 Dem nominee: 2% on $12K inflow"
semantic_title: "Beriont NH-01 Dem nominee odds stay near zero"
telemetry: "2% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-07T13:54:42+00:00"
event_id: "CM-EVT-BHSCBSRT91"
event_slug: "nh-01-democratic-primary-winner"
event_question: "Will a Democrat win the NH-01 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7d145bcc5ba69711989e88df77d3b91858bd020277becfe903583f538a01e265"
  question_raw: "Will Carleigh Beriont be the Democratic nominee for NH-01?"
  current_price: 0.024
  volume_24h_usd: 12250.795099999998
  volume_cumulative_usd: 36815.18512800001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "Polymarket prices Beriont at 2%, the market reads her nomination as a remote outcome."
  - "24h volume of $12K is 33% of all-time, mirroring the Sullivan spike and suggesting linked activity."
  - "Paired surge across both NH-01 contracts points to the same catalytic event, likely a primary deadline or poll drop, driving traders to reprice the full field simultaneously."
  - "Contract resolves on Democratic nominee certification for New Hampshire's 1st Congressional District."
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
      poly_vol_24h_usd: 12250.795099999998
sources:
  - label: "ClearMarket market record: Will a Democrat win the NH-01 primary election?"
    url: "https://clearmarket.fyi/events/nh-01-democratic-primary-winner"
    retrieved_at: "2026-09-07T13:54:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes on the Sullivan and Beriont contracts, each consuming a third of their all-time liquidity in one day, indicate a single informational catalyst is forcing a full field re-rating, with capital piling into Sullivan and off Beriont.
