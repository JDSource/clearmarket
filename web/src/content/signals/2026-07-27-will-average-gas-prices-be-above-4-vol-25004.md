---
signal_id: "CMSIG20260727VS04"
signal_slug: "will-average-gas-prices-be-above-4-vol-25004"
headline: "US gas above $4.04: 99% on $25K volume"
semantic_title: "Fresh volume backs gas prices holding above $4.04"
telemetry: "99% · $25K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-27T11:16:33+00:00"
event_id: "CM-EVT-9BFFMNBK34"
event_slug: "kxaaagasm-26jul31"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASM-26JUL31-4.04"
  question_raw: "Will average **gas prices** be above $4.04?"
  current_price: 0.99
  volume_24h_usd: 25004.22
  volume_cumulative_usd: 43418.27
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-30T14:00:00Z"
bullets:
  - "Kalshi prices average US gas above $4.04 at 99%, same near-certainty as adjacent strikes."
  - "24h volume $25K is 58% of all-time; slightly less concentrated than $4.02 and $4.00 contracts."
  - "The $4.04 strike still comfortably inside current national average, driving the 99% read."
  - "Part of a ladder of Kalshi gas contracts all clearing 99% simultaneously."
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
      kalshi_vol_24h_usd: 25004.22
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasm-26jul31"
    retrieved_at: "2026-07-27T11:16:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The $4.04 contract at 99% alongside its ladder peers confirms the market has no meaningful doubt about near-term gas prices, the relevant signal for desks is where on the ladder conviction begins to slip.
