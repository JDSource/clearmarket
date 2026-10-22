---
signal_id: "CMSIG20261022VS05"
signal_slug: "iaea-visits-isfahan-fordow-or-natanz-n-vol-41882"
headline: "IAEA Iran visit by Dec 31: 14% on $42K"
semantic_title: "IAEA Iran site visit by year-end stays a long shot at 14%"
telemetry: "14% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T13:25:36+00:00"
event_id: "CM-EVT-2M6LXFRJ38"
event_slug: "iaea-visits-isfahan-fordow-or-natanz-nuclear-site-by-july-31-20260624040209014"
event_question: "Will the IAEA visit the Isfahan, Fordow, or Natanz nuclear site by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6c783a56758368cb7ebdd383a368ab39728d3475d36a561626176657faaeb564"
  question_raw: "IAEA visits Isfahan, Fordow, or Natanz nuclear site by December 31?"
  current_price: 0.14
  volume_24h_usd: 41882.971953
  volume_cumulative_usd: 148218.87940399998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T23:59:00Z"
bullets:
  - "Polymarket prices an IAEA visit to Isfahan, Fordow, or Natanz by December 31 at just 14%, reflecting deep skepticism."
  - "$42K in 24h is 28% of all-time volume, notable fresh flow into a geopolitical tail-risk contract."
  - "Volume surge likely tied to diplomatic headlines or IAEA board meeting chatter, even as the price stays anchored near lows."
  - "Hard December 31 resolution makes this a clean binary on near-term Iran nuclear diplomacy."
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
      poly_vol_24h_usd: 41882.971953
sources:
  - label: "ClearMarket market record: Will the IAEA visit the Isfahan, Fordow, or Natanz nucl"
    url: "https://clearmarket.fyi/events/iaea-visits-isfahan-fordow-or-natanz-nuclear-site-by-july-31-20260624040209014"
    retrieved_at: "2026-10-22T13:25:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital entering a 14% contract on IAEA access to Iranian sites signals a desk buying cheap optionality on a diplomatic breakthrough, the price staying low means consensus remains deeply pessimistic on Iran compliance.
