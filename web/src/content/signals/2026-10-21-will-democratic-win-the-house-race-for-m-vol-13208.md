---
signal_id: "CMSIG20261021VS07"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-13208"
headline: "Dem wins ME-2 House: 41% on $13K volume"
semantic_title: "ME-2 House race sits near a coin-flip with buyers returning"
telemetry: "41% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T13:25:08+00:00"
event_id: "CM-EVT-JWBGQF2D62"
event_slug: "houseme2-26"
event_question: "Will a new representative be elected in Maine's 2nd congressional district?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEME2-26-D"
  question_raw: "Will Democratic win the House race for ME-2?"
  current_price: 0.41
  volume_24h_usd: 13208.19
  volume_cumulative_usd: 43388.45
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices the Democratic candidate in Maine's 2nd at 41%, effectively a competitive toss-up leaning slight Republican."
  - "30% of all-time volume, $13K, arrived in 24 hours, refreshing a contract that had been thinly traded."
  - "ME-2 has been a perennial battleground; renewed volume near 50% signals a polling release or candidate development."
  - "Resolves on certified 2026 midterm results for Maine's 2nd congressional district."
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
      kalshi_vol_24h_usd: 13208.19
sources:
  - label: "ClearMarket market record: Will a new representative be elected in Maine's 2nd con"
    url: "https://clearmarket.fyi/events/houseme2-26"
    retrieved_at: "2026-10-21T13:25:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-50% pricing with a 30% all-time volume day tells a desk this competitive House seat is back in active price discovery, any polling or fundraising catalyst here could swing the contract sharply given thin historical liquidity.
