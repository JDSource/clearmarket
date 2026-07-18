---
signal_id: "CMSIG20260718VS00"
signal_slug: "will-saeed-jalili-be-head-of-state-in-ir-vol-189307"
headline: "Jalili Iran head of state: 0% on $189K surge"
semantic_title: "Capital writes off Jalili's hold on Iranian leadership"
telemetry: "0% · $189K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-18T09:20:34+00:00"
event_id: "CM-EVT-RHBS1Y2385"
event_slug: "iran-leader-end-of-2026"
event_question: "Will Iran's leader change by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6ab0ce92e138eec9776d055e052140ff284f885fb8a54c74a944316e4a2e4d80"
  question_raw: "Will Saeed Jalili be head of state in Iran end of 2026?"
  current_price: 0.001
  volume_24h_usd: 189307.97999999998
  volume_cumulative_usd: 362926.216655
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Price at 0%, Polymarket traders assign zero probability Jalili leads Iran through end-2026."
  - "24h volume of $189K represents 52% of all-time contract liquidity, a decisive conviction flush."
  - "Fresh attention likely trails post-Khamenei succession signals or regime consolidation news sidelining Jalili."
  - "Contract resolves end-2026; zero pricing now forecloses meaningful recovery without a structural shock."
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
      poly_vol_24h_usd: 189307.97999999998
sources:
  - label: "ClearMarket market record: Will Iran's leader change by the end of 2026?"
    url: "https://clearmarket.fyi/events/iran-leader-end-of-2026"
    retrieved_at: "2026-07-18T09:20:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-total collapse to zero on half the contract's lifetime volume in a single session signals a desk-level consensus that Jalili is effectively eliminated from Iran's near-term power structure.
