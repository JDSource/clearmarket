---
signal_id: "CMSIG20260607VS07"
signal_slug: "will-karen-bass-and-spencer-pratt-be-the-vol-258144"
headline: "Bass-Pratt LA mayor nominees: 79% on $258K"
semantic_title: "Bass and Pratt locked in as LA mayoral nominees at 79%"
telemetry: "79% · $258K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-07T10:26:54+00:00"
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
  - "79% implies strong but not certain market consensus that Bass and Pratt are the confirmed nominees."
  - "51% of all-time volume in 24h reflects a decisive fresh-capital surge into the nominee question."
  - "Surge likely triggered by primary results or official certification moving through canvassing process."
  - "Resolution feeds directly into the LA mayoral winner contract where Bass prices at 79%."
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
    retrieved_at: "2026-06-07T10:26:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read the 79% nominee confirmation as the structural input driving the winner market, the two contracts are tightly linked, and any residual 21% uncertainty here represents the key risk to the Bass winner-market position.
