---
signal_id: "CMSIG20261029VS05"
signal_slug: "will-democratic-win-the-house-race-for-v-vol-47292"
headline: "Dems VA-05 House race: 42% on $47K volume"
semantic_title: "VA-05 Democratic odds stay contested as heavy trading tests 42%"
telemetry: "42% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T07:48:41+00:00"
event_id: "CM-EVT-J5Q1GQ0MF2"
event_slug: "kxhouserace-va05-26"
event_question: "Will a winner be determined in the Virginia 5th Congressional District House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA05-26-D"
  question_raw: "Will Democratic win the House race for VA-05?"
  current_price: 0.42
  volume_24h_usd: 47292.91
  volume_cumulative_usd: 149491.17
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Democratic win in VA-05 at 42%, a near-even race with a slight Republican lean."
  - "$47.3K in 24h is 32% of all-time volume, a solid single-session share for a competitive House contract."
  - "VA-05 is a genuine toss-up zone; this volume level reflects active market-making on a genuinely uncertain outcome."
  - "Resolves on 2026 midterm election results for Virginia's 5th congressional district."
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
      kalshi_vol_24h_usd: 47292.91
sources:
  - label: "ClearMarket market record: Will a winner be determined in the Virginia 5th Congres"
    url: "https://clearmarket.fyi/events/kxhouserace-va05-26"
    retrieved_at: "2026-10-29T07:48:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 42% price with 32% of lifetime volume in one day tells the desk VA-05 is being treated as a live competitive race, pair with the Republican-side contract for a full picture of where odds are settling.
