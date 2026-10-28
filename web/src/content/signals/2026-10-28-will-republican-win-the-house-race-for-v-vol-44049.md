---
signal_id: "CMSIG20261028VS07"
signal_slug: "will-republican-win-the-house-race-for-v-vol-44049"
headline: "GOP VA-05 House win: 56% on $44K surge"
semantic_title: "Virginia VA-05 GOP odds sit near 50% on fresh volume"
telemetry: "56% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T15:35:02+00:00"
event_id: "CM-EVT-J5Q1GQ0MF2"
event_slug: "kxhouserace-va05-26"
event_question: "Will a winner be determined in the Virginia 5th Congressional District House race?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA05-26-R"
  question_raw: "Will Republican win the House race for VA-05?"
  current_price: 0.56
  volume_24h_usd: 44049.46
  volume_cumulative_usd: 157841.54
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican winning VA-05 at 56%, a slim margin signaling a genuinely contested race."
  - "28% of all-time volume arrived in 24h, a meaningful but less concentrated spike than other House races today."
  - "Near-even pricing with fresh capital suggests VA-05 has moved into competitive territory, possibly on new polling or campaign developments."
  - "Resolves on the certified winner of the VA-05 House race."
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
      kalshi_vol_24h_usd: 44049.46
sources:
  - label: "ClearMarket market record: Will a winner be determined in the Virginia 5th Congres"
    url: "https://clearmarket.fyi/events/kxhouserace-va05-26"
    retrieved_at: "2026-10-28T15:35:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 56% GOP price on fresh volume in VA-05 flags this as a real toss-up worth tracking for House majority scenarios, slim enough that additional information could shift the contract materially.
