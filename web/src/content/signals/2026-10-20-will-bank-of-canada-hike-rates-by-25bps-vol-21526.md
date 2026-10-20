---
signal_id: "CMSIG20261020VS07"
signal_slug: "will-bank-of-canada-hike-rates-by-25bps-vol-21526"
headline: "BoC hikes 25bps Oct 2026: 62% on $22K Kalshi volume"
semantic_title: "Buyers back a 25bps Bank of Canada hike in October at 62%"
telemetry: "62% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-20T07:48:28+00:00"
event_id: "CM-EVT-RCX0GXDHW8"
event_slug: "kxcbdecisioncanada-26oct"
event_question: "Will the Bank of Canada make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCBDECISIONCANADA-26OCT-H25"
  question_raw: "Will Bank of Canada Hike rates by 25bps at their October 2026 meeting?"
  current_price: 0.62
  volume_24h_usd: 21526.86
  volume_cumulative_usd: 72555.96
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T13:29:00Z"
bullets:
  - "Kalshi prices 62% on the Bank of Canada raising rates 25bps at its October 2026 meeting, a majority lean but far from consensus."
  - "$22K in 24h is 30% of all-time volume, moving alongside the hold contract as the full rate-decision market reprices."
  - "62% for a hike implies traders have a base case for tightening but the hold scenario at 39% remains very much alive."
  - "Resolves on the Bank of Canada October 2026 rate announcement; any surprise inflation or labor data could compress this spread sharply."
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
      kalshi_vol_24h_usd: 21526.86
sources:
  - label: "ClearMarket market record: Will the Bank of Canada make a decision in October 2026"
    url: "https://clearmarket.fyi/events/kxcbdecisioncanada-26oct"
    retrieved_at: "2026-10-20T07:48:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 62/39 hike-to-hold split on Kalshi tells desks the market has a lean but pricing is loose enough to move materially on the next Canadian CPI or jobs print.
