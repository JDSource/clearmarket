---
signal_id: "CMSIG20261017VS05"
signal_slug: "will-republican-win-the-house-race-for-n-vol-18552"
headline: "NC-1 GOP House: 36% on $19K Kalshi surge"
semantic_title: "NC-1 Republican odds slip below 50% with volume picking up"
telemetry: "36% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T07:48:43+00:00"
event_id: "CM-EVT-22K74MYTV1"
event_slug: "housenc1-26"
event_question: "Will the winner of the North Carolina 1st Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSENC1-26-R"
  question_raw: "Will Republican win the House race for NC-1?"
  current_price: 0.36
  volume_24h_usd: 18552.54
  volume_cumulative_usd: 36119.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi marks the Republican below 50% at 36%, making the Democratic candidate the implied favorite."
  - "$18.6K in 24h accounts for 51% of all-time volume, the majority of the contract's history in one session."
  - "NC-1 was previously a swing target; a below-50% Republican read on surging volume flags a potential rating shift."
  - "Resolves on 2026 North Carolina general election night."
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
      kalshi_vol_24h_usd: 18552.54
sources:
  - label: "ClearMarket market record: Will the winner of the North Carolina 1st Congressional"
    url: "https://clearmarket.fyi/events/housenc1-26"
    retrieved_at: "2026-10-17T07:48:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A majority of lifetime volume trading in a single day with the Republican priced as the underdog signals NC-1 may have moved meaningfully on new polling, candidate news, or campaign finance disclosures.
