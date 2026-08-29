---
signal_id: "CMSIG20260829VS01"
signal_slug: "will-ed-markey-be-the-democratic-nominee-vol-135850"
headline: "Markey MA Dem nominee: 98% on $136K"
semantic_title: "Markey nomination odds hold firm through a volume surge"
telemetry: "98% · $136K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-29T13:34:58+00:00"
event_id: "CM-EVT-J620PJQLH6"
event_slug: "kxsenatemad-26"
event_question: "Will the Massachusetts Democratic Senate nominee be determined by September 15, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEMAD-26-EMAR"
  question_raw: "Will Ed Markey be the Democratic nominee for the Senate in Massachusetts?"
  current_price: 0.982
  volume_24h_usd: 135850.07
  volume_cumulative_usd: 537603.74
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-15T14:00:00Z"
bullets:
  - "98% price leaves almost no probability of a credible challenger emerging in the Massachusetts Democratic primary."
  - "Kalshi sees $136K in 24h, hitting 25% of all-time volume, a notable liquidity event for a near-settled contract."
  - "Fresh volume into a 98% market suggests either late entrants locking in yes-side exposure or a small faction testing downside."
  - "Resolves on the Massachusetts Democratic Senate primary result."
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
      kalshi_vol_24h_usd: 135850.07
sources:
  - label: "ClearMarket market record: Will the Massachusetts Democratic Senate nominee be det"
    url: "https://clearmarket.fyi/events/kxsenatemad-26"
    retrieved_at: "2026-08-29T13:34:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 25% all-time volume day on a near-resolved contract suggests a desk is either hedging residual tail risk or building a position ahead of the primary close, the 2% downside is cheap optionality on a surprise.
