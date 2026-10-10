---
signal_id: "CMSIG20261010VS07"
signal_slug: "will-democratic-win-the-house-race-for-t-vol-13016"
headline: "TX-35 Dem House: 60% on $13K surge"
semantic_title: "Betting picks up on Democrats leading TX-35 at 60%"
telemetry: "60% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-30RGTM2V02"
event_slug: "kxhousetx35-26"
event_question: "Will there be a winner determined in the TX-35 House race by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSETX35-26-D"
  question_raw: "Will Democratic win the House race for TX-35?"
  current_price: 0.6
  volume_24h_usd: 13016.95
  volume_cumulative_usd: 50246.95
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning TX-35 at 60%, a modest favorite in what the market treats as a competitive seat."
  - "26% of all-time volume, $13K, printed in 24 hours, the market's busiest single session for this contract."
  - "Democratic lean in TX-35 at 60% is notable given Texas's statewide Republican tilt; fresh volume may reflect demographic or turnout modeling."
  - "Resolves on 2026 TX-35 House election result."
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
      kalshi_vol_24h_usd: 13016.95
sources:
  - label: "ClearMarket market record: Will there be a winner determined in the TX-35 House ra"
    url: "https://clearmarket.fyi/events/kxhousetx35-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that a 60% Democratic price in a Texas House seat drawing its heaviest single-day volume suggests active disagreement about district competitiveness, making TX-35 worth tracking for polling and campaign spending data.
