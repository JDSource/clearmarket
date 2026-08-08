---
signal_id: "CMSIG20260808VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-376464"
headline: "Fed Sept hold: 64% on $376K inflow"
semantic_title: "Traders back the Fed holding rates flat in September"
telemetry: "64% · $376K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:36:03+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their September 2026 meeting?"
  current_price: 0.64
  volume_24h_usd: 376464.49
  volume_cumulative_usd: 1000936.63
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi prices a 0bps September hike at 64%, a clear majority bet on no rate change."
  - "24h volume of $376K is 38% of all-time, the deepest single-day engagement on this contract."
  - "Fresh capital is reinforcing the hold scenario as the dominant base case ahead of FOMC."
  - "Resolves at the September 2026 Federal Reserve meeting announcement."
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
      kalshi_vol_24h_usd: 376464.49
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-08-08T08:36:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy conviction at 64% with 38% of all-time volume printing in one day signals the rates market has largely settled on a September pause as its working assumption.
