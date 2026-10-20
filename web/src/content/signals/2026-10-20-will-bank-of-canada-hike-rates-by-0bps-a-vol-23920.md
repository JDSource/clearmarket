---
signal_id: "CMSIG20261020VS05"
signal_slug: "will-bank-of-canada-hike-rates-by-0bps-a-vol-23920"
headline: "BoC holds rates Oct 2026: 39% on $24K Kalshi volume"
semantic_title: "Bank of Canada October hold bets run neck-and-neck at 39%"
telemetry: "39% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T07:48:28+00:00"
event_id: "CM-EVT-RCX0GXDHW8"
event_slug: "kxcbdecisioncanada-26oct"
event_question: "Will the Bank of Canada make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCBDECISIONCANADA-26OCT-H0"
  question_raw: "Will Bank of Canada Hike rates by 0bps at their October 2026 meeting?"
  current_price: 0.39
  volume_24h_usd: 23920.47
  volume_cumulative_usd: 75274.31
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T13:29:00Z"
bullets:
  - "Kalshi prices 39% on the Bank of Canada holding rates unchanged at its October 2026 meeting, slightly trailing the hike scenario."
  - "$24K in 24h is 32% of all-time volume, moving in tandem with the 25bps hike contract for a clear two-sided rate debate."
  - "39% hold vs. 62% hike on the companion contract implies the market has a lean but not conviction toward a 25bps move."
  - "Resolves on the Bank of Canada October 2026 rate decision; spread is narrow enough that one data print could flip positioning."
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
      kalshi_vol_24h_usd: 23920.47
sources:
  - label: "ClearMarket market record: Will the Bank of Canada make a decision in October 2026"
    url: "https://clearmarket.fyi/events/kxcbdecisioncanada-26oct"
    retrieved_at: "2026-10-20T07:48:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The tight 39%/62% split across hold and hike contracts signals genuine uncertainty into the October BoC meeting, macro desks with Canadian rate exposure should treat this as a live two-outcome event.
