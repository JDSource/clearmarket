---
signal_id: "CMSIG20261025VS03"
signal_slug: "will-the-democratic-party-win-the-nc-09-vol-42378"
headline: "Dem wins NC-09: 36% on $42K surge"
semantic_title: "Democrats back in play for NC-09 with odds at 36%"
telemetry: "36% · $42K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T12:57:02+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdc23b5a54616abf57d7f89f57a29dbacc0d836ab6f3994f5533c8c41ba929ebb"
  question_raw: "Will the Democratic Party win the NC-09 House seat?"
  current_price: 0.36
  volume_24h_usd: 42378.244147
  volume_cumulative_usd: 85029.12521500001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "36% prices Democrats as underdogs but live, not written off, closer to a coin-flip than a long shot."
  - "Polymarket's $42K 24h handle equals 50% of all-time volume, suggesting a sharp new-information catalyst."
  - "NC-09 is a competitive swing district; fresh attention at the midterm stretch often precedes polling or candidate news."
  - "Resolves on 2026 midterm NC-09 House race certification."
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
      poly_vol_24h_usd: 42378.244147
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-25T12:57:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of lifetime volume printing in one session on a competitive House district contract is a strong signal that new district-level data or campaign developments are moving informed money into NC-09.
