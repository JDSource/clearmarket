---
signal_id: "CMSIG20260916VS02"
signal_slug: "will-trump-publicly-criticize-kevin-wars-vol-37675"
headline: "Trump criticizes Warsh by Jan '27: 55% on $38K"
semantic_title: "Odds split nearly even on Trump criticizing Warsh before Jan 2027"
telemetry: "55% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-P95C3C1H51"
event_slug: "kxdjtattackwarsh-27"
event_question: "Will Trump publicly criticize Kevin Warsh?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDJTATTACKWARSH-27-JAN"
  question_raw: "Will Trump publicly criticize Kevin Warsh before Jan 2027?"
  current_price: 0.55
  volume_24h_usd: 37675.37
  volume_cumulative_usd: 52557.29
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices a public Trump-Warsh clash at 55%, essentially a coin-flip with a slight lean toward it happening."
  - "72% of all-time volume hit in 24h, $37.7K, the sharpest single-day share of any spike in this batch."
  - "Warsh is a leading Fed chair candidate; any policy friction or nomination-process news could trigger Trump commentary."
  - "Contract resolves Jan 1, 2027, leaving roughly 15 weeks for the event to materialize or expire."
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
      kalshi_vol_24h_usd: 37675.37
sources:
  - label: "ClearMarket market record: Will Trump publicly criticize Kevin Warsh?"
    url: "https://clearmarket.fyi/events/kxdjtattackwarsh-27"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With 72% of lifetime volume appearing in a single session on a near-50/50 contract, traders are actively disputing the probability of a Trump-Warsh public rift, a desk following Fed succession risk should track this as a sentiment gauge.
