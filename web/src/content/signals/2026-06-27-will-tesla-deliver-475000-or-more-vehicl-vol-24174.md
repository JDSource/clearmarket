---
signal_id: "CMSIG20260627VS02"
signal_slug: "will-tesla-deliver-475000-or-more-vehicl-vol-24174"
headline: "Tesla Q2 ≥475K deliveries: 26% on $24K surge"
semantic_title: "Capital stacks on Tesla falling short of 475K Q2 deliveries"
telemetry: "26% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-27T10:03:08+00:00"
event_id: "CM-EVT-TKB6WQH0P3"
event_slug: "how-many-tesla-deliveries-in-q2-2026"
event_question: "Will Tesla deliver between 350000 and 375000 vehicles in Q2 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4926438a8bcd51e07989a94a7efafff86a0c66101a5f0f51dc0a252425c41b4b"
  question_raw: "Will Tesla deliver 475000 or more vehicles in Q2 2026"
  current_price: 0.255
  volume_24h_usd: 24174.326288000007
  volume_cumulative_usd: 41610.83813800001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket at 26%, majority of capital prices a miss against the 475K threshold."
  - "$24K in 24h is 58% of all-time contract volume, the sharpest single-session commitment yet."
  - "Q2 ends June 30; delivery data imminent, driving last-window positioning across both sides."
  - "Sister contract (400K, 425K band at 29%) absorbs overlapping flow, see Spike 5."
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
      poly_vol_24h_usd: 24174.326288000007
sources:
  - label: "ClearMarket market record: Will Tesla deliver between 350000 and 375000 vehicles i"
    url: "https://clearmarket.fyi/events/how-many-tesla-deliveries-in-q2-2026"
    retrieved_at: "2026-06-27T10:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 58% of all-time volume printing in one session at deadline, desks are making concentrated directional bets on Tesla's delivery miss, worth cross-referencing with the band contract for implied distribution.
