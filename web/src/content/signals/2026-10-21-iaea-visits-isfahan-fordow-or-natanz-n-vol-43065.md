---
signal_id: "CMSIG20261021VS00"
signal_slug: "iaea-visits-isfahan-fordow-or-natanz-n-vol-43065"
headline: "IAEA Iran site visit: 17% on $43K surge"
semantic_title: "IAEA access to Iran sites by Dec 31 stays a long shot"
telemetry: "17% · $43K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-21T13:25:08+00:00"
event_id: "CM-EVT-2M6LXFRJ38"
event_slug: "iaea-visits-isfahan-fordow-or-natanz-nuclear-site-by-july-31-20260624040209014"
event_question: "Will the IAEA visit the Isfahan, Fordow, or Natanz nuclear site by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6c783a56758368cb7ebdd383a368ab39728d3475d36a561626176657faaeb564"
  question_raw: "IAEA visits Isfahan, Fordow, or Natanz nuclear site by December 31?"
  current_price: 0.17
  volume_24h_usd: 43065.21
  volume_cumulative_usd: 106335.90745100002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T23:59:00Z"
bullets:
  - "Polymarket prices only 17% odds, inspectors are not expected back at Isfahan, Fordow, or Natanz this year."
  - "24h volume of $43K equals 40% of all-time handle, signaling a sharp burst of fresh attention on this contract."
  - "Renewed diplomatic signals or back-channel talks likely driving traders to take a position ahead of year-end."
  - "Resolves YES if IAEA physically visits any named site before December 31, 2026."
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
      poly_vol_24h_usd: 43065.21
sources:
  - label: "ClearMarket market record: Will the IAEA visit the Isfahan, Fordow, or Natanz nucl"
    url: "https://clearmarket.fyi/events/iaea-visits-isfahan-fordow-or-natanz-nuclear-site-by-july-31-20260624040209014"
    retrieved_at: "2026-10-21T13:25:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 40% all-time volume share in one session tells a desk that geopolitical desks are pricing a near-term Iran nuclear catalyst, the 17% price means the base case is still no access, but the surge warrants watching diplomatic wires closely.
