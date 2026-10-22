---
signal_id: "CMSIG20261022VS01"
signal_slug: "iaea-visits-isfahan-fordow-or-natanz-n-vol-83830"
headline: "IAEA Iran site visit: 14% on $84K surge"
semantic_title: "IAEA access to Iran nuclear sites stays a long shot at 14%"
telemetry: "14% · $84K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-22T07:48:28+00:00"
event_id: "CM-EVT-2M6LXFRJ38"
event_slug: "iaea-visits-isfahan-fordow-or-natanz-nuclear-site-by-july-31-20260624040209014"
event_question: "Will the IAEA visit the Isfahan, Fordow, or Natanz nuclear site by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6c783a56758368cb7ebdd383a368ab39728d3475d36a561626176657faaeb564"
  question_raw: "IAEA visits Isfahan, Fordow, or Natanz nuclear site by December 31?"
  current_price: 0.14
  volume_24h_usd: 83830.97195299999
  volume_cumulative_usd: 148218.87940399998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T23:59:00Z"
bullets:
  - "Polymarket prices an IAEA visit to Isfahan, Fordow, or Natanz by Dec 31 at just 14%, market reads access as unlikely."
  - "57% of all-time volume arrived in the last 24h, the single largest daily session yet on this contract."
  - "Surge likely tied to fresh diplomatic signals or nuclear-talks noise; attention at this scale typically precedes a catalyst."
  - "Resolves December 31, 2026 based on confirmed IAEA inspection of named sites."
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
      poly_vol_24h_usd: 83830.97195299999
sources:
  - label: "ClearMarket market record: Will the IAEA visit the Isfahan, Fordow, or Natanz nucl"
    url: "https://clearmarket.fyi/events/iaea-visits-isfahan-fordow-or-natanz-nuclear-site-by-july-31-20260624040209014"
    retrieved_at: "2026-10-22T07:48:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half the contract's lifetime liquidity landing in one session tells a desk that nuclear-diplomacy risk is being actively repriced, even as the odds remain deeply skeptical of access materializing.
