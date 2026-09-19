---
signal_id: "CMSIG20260919VS00"
signal_slug: "trump-x-greenland-deal-signed-by-decembe-vol-104928"
headline: "Trump-Greenland deal by Dec 31: 92% on $105K surge"
semantic_title: "Traders back a Trump-Greenland deal closing by year-end"
telemetry: "92% · $105K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T07:47:59+00:00"
event_id: "CM-EVT-M8SXSN1YS7"
event_slug: "trump-x-greenland-deal-signed-by-december-31"
event_question: "Will a Trump-Greenland deal be signed by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a7aed00fae37de19e0b789a6b50a7475ff1afa898c50b9da11ca733a23199fa"
  question_raw: "Trump x Greenland deal signed by December 31?"
  current_price: 0.92
  volume_24h_usd: 104928.48512199998
  volume_cumulative_usd: 205556.40646899998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices 92% odds, near-certainty that a formal deal gets signed before January."
  - "24h volume of $105K is 51% of all-time handle, signaling a concentrated late-stage conviction push."
  - "Fresh attention at this price level suggests participants expect an imminent announcement or framework leak."
  - "Resolves December 31, 2026; any diplomatic delay or congressional complication is the key tail risk."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 104928.48512199998
sources:
  - label: "ClearMarket market record: Will a Trump-Greenland deal be signed by December 31?"
    url: "https://clearmarket.fyi/events/trump-x-greenland-deal-signed-by-december-31"
    retrieved_at: "2026-09-19T07:47:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half the contract's lifetime volume arriving in a single session at 92% means desks are treating this as near-done and position-squaring is driving the surge, watch for an official signing announcement within days.
