---
signal_id: "CMSIG20261029VS07"
signal_slug: "will-republican-win-the-house-race-for-v-vol-48018"
headline: "GOP VA-05 House race: 59% on $48K volume"
semantic_title: "Republican odds in VA-05 lead at 59% amid a fresh volume push"
telemetry: "59% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T07:48:41+00:00"
event_id: "CM-EVT-J5Q1GQ0MF2"
event_slug: "kxhouserace-va05-26"
event_question: "Will a winner be determined in the Virginia 5th Congressional District House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA05-26-R"
  question_raw: "Will Republican win the House race for VA-05?"
  current_price: 0.59
  volume_24h_usd: 48018.6
  volume_cumulative_usd: 168081.83
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in VA-05 at 59%, modest but clear edge, complementing the Democratic contract at 42%."
  - "$48K in 24h is 29% of all-time, near-identical volume to the Democratic side, confirming two-sided flow."
  - "Matched volume across both VA-05 contracts today points to active arbitrage or competing directional bets on the same race."
  - "Resolves on 2026 midterm election night for Virginia's 5th district."
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
      kalshi_vol_24h_usd: 48018.6
sources:
  - label: "ClearMarket market record: Will a winner be determined in the Virginia 5th Congres"
    url: "https://clearmarket.fyi/events/kxhouserace-va05-26"
    retrieved_at: "2026-10-29T07:48:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Mirrored volume on both sides of VA-05 in one session tells the desk this race is being actively repriced from multiple angles, the 59%/42% split implies slight but not decisive Republican advantage heading into the midterm.
