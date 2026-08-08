---
signal_id: "CMSIG20260808VS03"
signal_slug: "will-trump-s-first-announced-attorney-ge-vol-67470"
headline: "Trump AG pick confirmed: 99% on $67K surge"
semantic_title: "Odds hold firm on Trump's AG pick getting confirmed"
telemetry: "99% · $67K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:36:03+00:00"
event_id: "CM-EVT-NY76DC3G68"
event_slug: "kxagconf-26"
event_question: "Will Todd Blanche be confirmed?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAGCONF-26JUN05-SEP01"
  question_raw: "Will Trump's first announced Attorney General pick be confirmed as Attorney General before Sep 1, 2026?"
  current_price: 0.99
  volume_24h_usd: 67470.82
  volume_cumulative_usd: 210227.98
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "Kalshi prices confirmation of Trump's first AG pick at 99%, near-certain in the market's view."
  - "24h volume of $67K is 32% of all-time, reflecting fresh conviction rather than residual noise."
  - "Surge suggests traders see little remaining uncertainty as the Senate vote approaches."
  - "Resolves upon Senate confirmation vote completion."
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
      kalshi_vol_24h_usd: 67470.82
sources:
  - label: "ClearMarket market record: Will Todd Blanche be confirmed?"
    url: "https://clearmarket.fyi/events/kxagconf-26"
    retrieved_at: "2026-08-08T08:36:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 99% price absorbing 32% of all-time volume in one day signals the confirmation is effectively treated as done by the market, with minimal capital positioned against it.
