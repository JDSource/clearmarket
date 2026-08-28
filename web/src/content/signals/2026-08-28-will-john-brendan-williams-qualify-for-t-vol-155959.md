---
signal_id: "CMSIG20260828VS00"
signal_slug: "will-john-brendan-williams-qualify-for-t-vol-155959"
headline: "Williams AK runoff: 89% on $156K surge"
semantic_title: "Traders back Williams into Alaska's top-four runoff"
telemetry: "89% · $156K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-28T19:52:39+00:00"
event_id: "CM-EVT-FD44Z12859"
event_slug: "kxakprimary-26may19"
event_question: "Will the AK-AL primary advance by the next general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAKPRIMARY-26MAY19-JWIL"
  question_raw: "Will John Brendan Williams qualify for the runoff in the 2026 Alaska top-four primary?"
  current_price: 0.89
  volume_24h_usd: 155959.13
  volume_cumulative_usd: 188755.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "89% implies near-certainty Williams clears the top-four threshold in Alaska's ranked-choice primary."
  - "24h volume of $156K is 83% of all-time handle, the bulk of lifetime activity landed today."
  - "Late-primary attention spike suggests fresh information or filing deadline clarification driving conviction."
  - "Resolves on official Alaska Division of Elections certification of top-four qualifiers."
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
      kalshi_vol_24h_usd: 155959.13
sources:
  - label: "ClearMarket market record: Will the AK-AL primary advance by the next general elec"
    url: "https://clearmarket.fyi/events/kxakprimary-26may19"
    retrieved_at: "2026-08-28T19:52:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 83% all-time volume concentration at 89% odds signals the market has effectively called this race, any desk pricing Alaskan downballot scenarios should treat Williams's runoff spot as near-settled.
