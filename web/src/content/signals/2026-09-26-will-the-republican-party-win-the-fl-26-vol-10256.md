---
signal_id: "CMSIG20260926VS05"
signal_slug: "will-the-republican-party-win-the-fl-26-vol-10256"
headline: "GOP FL-26 House hold: 85% on $10K volume"
semantic_title: "Republican FL-26 hold at 85% draws a volume surge near 25%"
telemetry: "85% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T07:47:58+00:00"
event_id: "CM-EVT-683BTN68V2"
event_slug: "fl-26-house-election-winner"
event_question: "Will the Republican candidate win Florida's 26th Congressional District House election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2d0d0159d0edd3511bf1aeef4ef53a74b0ef2dadcfc6b1019aa31ce74b664861"
  question_raw: "Will the Republican Party win the FL-26 House seat?"
  current_price: 0.85
  volume_24h_usd: 10256.786667
  volume_cumulative_usd: 40645.567847
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "85% on Polymarket prices FL-26 as a strong but not foregone Republican retention."
  - "24h volume of $10K is 25% of all-time, a full quarter of lifetime activity arriving in a single session."
  - "Positioning into an 85% contract at this stage suggests traders are seeking yield on a near-certain outcome or reacting to candidate news."
  - "Resolves on the certified 2026 FL-26 House election result."
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
      poly_vol_24h_usd: 10256.786667
sources:
  - label: "ClearMarket market record: Will the Republican candidate win Florida's 26th Congre"
    url: "https://clearmarket.fyi/events/fl-26-house-election-winner"
    retrieved_at: "2026-09-26T07:47:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A quarter of lifetime volume hitting FL-26 at 85% indicates fresh directional conviction, a desk should check whether a Democratic challenger withdrawal, new poll, or fundraising report triggered the session.
