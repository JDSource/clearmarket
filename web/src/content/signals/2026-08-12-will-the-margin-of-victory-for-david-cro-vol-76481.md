---
signal_id: "CMSIG20260812VS04"
signal_slug: "will-the-margin-of-victory-for-david-cro-vol-76481"
headline: "Crowley WI margin target: 99% on $76K surge"
semantic_title: "Crowley margin contract trades near certainty after primary"
telemetry: "99% · $76K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-KZPXP2LDK6"
event_slug: "kxprimarymov-govwinomd26"
event_question: "Will the Wisconsin Democratic Governor primary margin of victory be at least 5 percentage points?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYMOV-GOVWINOMD26-DCRO-P1"
  question_raw: "Will the margin of victory for David Crowley in the 2026 Wisconsin Democratic gubernatorial primary be between 0% and 3%?"
  current_price: 0.99
  volume_24h_usd: 76481.34
  volume_cumulative_usd: 91993.6
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-11T14:00:00Z"
bullets:
  - "Kalshi prices Crowley hitting his victory-margin threshold at 99%, effectively a resolved line."
  - "$76K in 24h is 83% of all-time volume, consistent with a settlement-driven flush."
  - "Companion to the nomination contract; both moving to 99-100% in the same session confirms primary outcome."
  - "Resolves on the certified margin of victory in the Wisconsin Democratic gubernatorial primary."
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
      kalshi_vol_24h_usd: 76481.34
sources:
  - label: "ClearMarket market record: Will the Wisconsin Democratic Governor primary margin o"
    url: "https://clearmarket.fyi/events/kxprimarymov-govwinomd26"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Like the nomination contract, this is a settlement event, desks can treat both Wisconsin Democratic primary lines as closed and focus capital on the November general.
