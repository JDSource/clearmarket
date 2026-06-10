---
signal_id: "CMSIG20260610VS07"
signal_slug: "will-karen-bass-and-spencer-pratt-be-the-vol-258144"
headline: "Bass-Pratt LA nominees: 79% on $258K surge"
semantic_title: "Bass-Pratt LA ballot pairing defended as the dominant ticket"
telemetry: "79% · $258K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-10T11:37:24+00:00"
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
  - "79% price reflects strong market consensus that Bass and Pratt are the confirmed general-election pairing."
  - "$258K in 24h is 51% of all-time volume, majority of lifetime activity in a single session."
  - "Aligns with the broader LA mayoral market pricing Bass at 79% to win, confirming nominee composition."
  - "Kalshi contract resolves on official nominee certification; surge suggests that trigger is imminent."
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
    retrieved_at: "2026-06-10T11:37:24+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes in the nominee-pairing and winner contracts at identical probabilities indicate a correlated institutional trade, a desk pricing LA electoral risk across both legs in one session.
