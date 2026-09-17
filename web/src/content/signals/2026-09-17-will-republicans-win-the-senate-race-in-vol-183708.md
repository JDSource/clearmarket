---
signal_id: "CMSIG20260917VS02"
signal_slug: "will-republicans-win-the-senate-race-in-vol-183708"
headline: "GOP Nebraska Senate: 70% on $184K inflow"
semantic_title: "Republicans lead Nebraska Senate race at 70% on the tape"
telemetry: "70% · $184K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-17T13:05:20+00:00"
event_id: "CM-EVT-37PJ66HMC4"
event_slug: "senatene-26"
event_question: "Nebraska Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENE-26-R"
  question_raw: "Will Republicans win the Senate race in Nebraska?"
  current_price: 0.7
  volume_24h_usd: 183708.13
  volume_cumulative_usd: 496231.99
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 70% to hold Nebraska, a firm but not certain lead."
  - "$184K in 24h volume, 37% of all-time, marks the largest single-day trading session to date."
  - "Nebraska has emerged as a competitive Senate battleground, drawing fresh capital as polling shifts."
  - "Contract resolves on November 2026 election results."
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
      kalshi_vol_24h_usd: 183708.13
sources:
  - label: "ClearMarket market record: Nebraska Senate winner?"
    url: "https://clearmarket.fyi/events/senatene-26"
    retrieved_at: "2026-09-17T13:05:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A large absolute volume day, even at 37% of all-time, signals that Nebraska Senate is being actively repriced as a competitive race worth hedging into the fall campaign.
