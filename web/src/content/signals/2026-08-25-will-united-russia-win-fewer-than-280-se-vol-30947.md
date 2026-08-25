---
signal_id: "CMSIG20260825VS03"
signal_slug: "will-united-russia-win-fewer-than-280-se-vol-30947"
headline: "United Russia sub-280 seats: 3% on $31K spike"
semantic_title: "Odds hold near zero that United Russia loses seats below 280"
telemetry: "3% · $31K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-25T08:37:37+00:00"
event_id: "CM-EVT-MCHQSDBHW5"
event_slug: "how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
event_question: "How many seats will United Russia win in the next Russian legislative election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x430751274480232547064a75eb29ceead00b95cf3e21709911a147cfada04e16"
  question_raw: "Will United Russia win fewer than 280 seats in the next Russian State Duma election?"
  current_price: 0.034
  volume_24h_usd: 30947.170000000006
  volume_cumulative_usd: 66999.183146
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices United Russia winning fewer than 280 Duma seats at just 3%, near-impossible per market consensus."
  - "24h volume of $31K is 46% of all-time, nearly half the contract's lifetime volume traded in one session."
  - "A 46% all-time share at 3% odds suggests a contested positioning event: either a sharp view on Russian electoral mechanics or a new information catalyst."
  - "Duma elections not yet scheduled; resolution depends on next election announcement."
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
      poly_vol_24h_usd: 30947.170000000006
sources:
  - label: "ClearMarket market record: How many seats will United Russia win in the next Russi"
    url: "https://clearmarket.fyi/events/how-many-seats-will-united-russia-win-in-the-next-russian-legislative-election"
    retrieved_at: "2026-08-25T08:37:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume arriving at a 3% price is a strong signal that a desk or informed participant is either defending the existing consensus or expressing a geopolitical tail risk, worth monitoring for associated Russia-related news flow.
