---
signal_id: "CMSIG20261029VS02"
signal_slug: "will-the-democratic-party-win-the-nc-09-vol-87892"
headline: "Dems NC-09 House seat: 32% on $88K inflow"
semantic_title: "Democrats trail in NC-09 as fresh volume tests the underdog price"
telemetry: "32% · $88K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-29T07:48:41+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdc23b5a54616abf57d7f89f57a29dbacc0d836ab6f3994f5533c8c41ba929ebb"
  question_raw: "Will the Democratic Party win the NC-09 House seat?"
  current_price: 0.32
  volume_24h_usd: 87892.27211499999
  volume_cumulative_usd: 181073.90808500003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats winning NC-09 at 32%, the market assigns Republicans a clear edge."
  - "$87.9K in 24h volume is 49% of all-time, nearly half the contract's lifetime book flowed today."
  - "NC-09 is an active midterm battleground; fresh attention often precedes a poll, filing, or candidate news."
  - "Resolves after the 2026 midterm election results for NC's 9th congressional district."
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
      poly_vol_24h_usd: 87892.27211499999
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-29T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time volume arriving in one session at a 32% Democratic price signals the desk this race is drawing serious handicapping attention, watch for a new poll or candidate development in NC-09.
