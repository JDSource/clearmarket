---
signal_id: "CMSIG20260605VS07"
signal_slug: "will-karen-bass-and-spencer-pratt-be-the-vol-258144"
headline: "Bass & Pratt LA nominees: 79% on $258K surge"
semantic_title: "Bass-Pratt LA mayoral ticket locked in at market consensus"
telemetry: "79% · $258K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-05T12:03:57+00:00"
event_id: "CM-EVT-5D13MHJ4R8"
event_slug: "kxlamayormatchup-26jun"
event_question: "Will there be a Los Angeles mayoral election by the specified date?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLAMAYORMATCHUP-26JUN-KBASSPRA"
  question_raw: "Will Karen Bass and Spencer Pratt be the nominees in the 2026 Los Angeles mayoral primary?"
  current_price: 0.79
  volume_24h_usd: 258144.78
  volume_cumulative_usd: 510429.59
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-06-02T14:00:00Z"
bullets:
  - "Market prices 79% odds Bass and Pratt are the confirmed major-party nominees in the LA mayoral race."
  - "$258K in 24h volume is 51% of all-time handle, majority of the contract's history compressed into one session."
  - "Aligns with the standalone LA mayoral winner market also at 79%, suggesting a coherent, consistent book."
  - "Nomination confirmation or ballot certification event likely triggered the surge in settling activity."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 258144.78
sources:
  - label: "ClearMarket market record: Will there be a Los Angeles mayoral election by the spe"
    url: "https://clearmarket.fyi/events/kxlamayormatchup-26jun"
    retrieved_at: "2026-06-05T12:03:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 79% nominee-pairing price matching the winner market's frontrunner probability indicates the Kalshi book is internally consistent, desks can treat the Bass-Pratt general election matchup as the consensus scenario for LA 2026.
