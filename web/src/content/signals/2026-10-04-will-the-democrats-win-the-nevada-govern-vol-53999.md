---
signal_id: "CMSIG20261004VS03"
signal_slug: "will-the-democrats-win-the-nevada-govern-vol-53999"
headline: "Nevada governor Dem: 54% on $54K spike"
semantic_title: "Nevada governor race sits at a 54% toss-up"
telemetry: "54% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T07:48:35+00:00"
event_id: "CM-EVT-Q7DX7L87P0"
event_slug: "nevada-governor-winner-2026"
event_question: "Will the Nevada governor election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x707eb5c6df23e32e0b770dd0ccd1245abb7fac0dcfd24d8b68dd99e5ca737180"
  question_raw: "Will the Democrats win the Nevada governor race in 2026?"
  current_price: 0.54
  volume_24h_usd: 53999.873435
  volume_cumulative_usd: 116799.60262499998
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket prices Democrats at 54% in Nevada's 2026 governor race, effectively a coin flip."
  - "46% of all-time volume cleared in one session, making this one of the contract's most active days."
  - "A near-even market this early signals genuine uncertainty about both party nominees."
  - "Resolves on Nevada 2026 general election night."
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
      poly_vol_24h_usd: 53999.873435
sources:
  - label: "ClearMarket market record: Will the Nevada governor election be won by the Republi"
    url: "https://clearmarket.fyi/events/nevada-governor-winner-2026"
    retrieved_at: "2026-10-04T07:48:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume at the 54% mark tells a desk the Nevada governor contract is attracting serious two-way flow, any candidate clarity or economic data from the state could break this open.
