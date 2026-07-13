---
signal_id: "CMSIG20260713VS01"
signal_slug: "will-mohammed-bin-salman-cease-to-be-the-vol-51050"
headline: "MBS Saudi leadership: 5% on $51K, 77% of all-time vol"
semantic_title: "Heavy flows defend MBS retaining de facto Saudi leadership by December"
telemetry: "5% · $51K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-13T10:56:44+00:00"
event_id: "CM-EVT-7TQCR95JL6"
event_slug: "mohammed-bin-salman-out-as-leader-of-saudi-arabia-by"
event_question: "Will Mohammed bin Salman be out as leader of Saudi Arabia in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb75da764f8b8363d534eba91c4fb19ceb666272f6fb1aa4ef66bdf7ae3e34b30"
  question_raw: "Will Mohammed bin Salman cease to be the de facto leader of Saudi Arabia by December 31, 2026?"
  current_price: 0.046
  volume_24h_usd: 51050.380000000005
  volume_cumulative_usd: 66581.73322299999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "5% price implies market assigns slim but non-negligible odds MBS exits power by December."
  - "24h volume $51K is 77% of all-time handle, effectively a full market repricing in one session."
  - "Spike suggests fresh geopolitical attention, possibly linked to regional instability or succession rumors."
  - "Contract resolves December 2026; thin all-time liquidity means even modest flows move the needle."
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
      poly_vol_24h_usd: 51050.380000000005
sources:
  - label: "ClearMarket market record: Will Mohammed bin Salman be out as leader of Saudi Arab"
    url: "https://clearmarket.fyi/events/mohammed-bin-salman-out-as-leader-of-saudi-arabia-by"
    retrieved_at: "2026-07-13T10:56:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 77% all-time volume concentration in a single day on a thinly traded contract signals a desk or informed participant is pricing in a tail-risk scenario around Saudi leadership continuity.
