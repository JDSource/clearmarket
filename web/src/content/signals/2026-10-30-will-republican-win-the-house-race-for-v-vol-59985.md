---
signal_id: "CMSIG20261030VS03"
signal_slug: "will-republican-win-the-house-race-for-v-vol-59985"
headline: "VA-06 GOP House: 92% on $60K Kalshi flow"
semantic_title: "VA-06 Republican seat draws conviction bets at 92%"
telemetry: "92% · $60K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T07:48:50+00:00"
event_id: "CM-EVT-DR4SW84W87"
event_slug: "kxhouserace-va06-26"
event_question: "VA-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-VA06-26-R"
  question_raw: "Will Republican win the House race for VA-06?"
  current_price: 0.924
  volume_24h_usd: 59985.7
  volume_cumulative_usd: 82530.09
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republicans winning VA-06 at 92%, one of the firmest House reads on the board."
  - "24h volume of $60K is 73% of all-time, the contract is drawing nearly all its liquidity today."
  - "Pre-election surge on a 92% line implies terminal positioning, not discovery."
  - "Contract resolves on VA-06 House election result."
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
      kalshi_vol_24h_usd: 59985.7
sources:
  - label: "ClearMarket market record: VA-06 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-va06-26"
    retrieved_at: "2026-10-30T07:48:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy last-day volume on a near-locked 92% contract points to desks clearing Virginia House exposure before polls open rather than making new directional bets.
