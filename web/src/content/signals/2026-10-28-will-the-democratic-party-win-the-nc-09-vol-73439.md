---
signal_id: "CMSIG20261028VS04"
signal_slug: "will-the-democratic-party-win-the-nc-09-vol-73439"
headline: "Dems NC-09 House seat: 31% on $73K"
semantic_title: "Democrats trail in NC-09 as buyers back the underdog side"
telemetry: "31% · $73K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-28T15:35:02+00:00"
event_id: "CM-EVT-0PM0Y1S600"
event_slug: "nc-09-house-election-winner"
event_question: "Will the winner of the NC-09 House election be determined by November 3, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdc23b5a54616abf57d7f89f57a29dbacc0d836ab6f3994f5533c8c41ba929ebb"
  question_raw: "Will the Democratic Party win the NC-09 House seat?"
  current_price: 0.31
  volume_24h_usd: 73439.095487
  volume_cumulative_usd: 166570.937015
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats winning NC-09 at 31%, a clear underdog stance with the seat leaning Republican."
  - "24h volume of $73K is 44% of all-time, a notable single-session concentration in a district-level race."
  - "Activity likely driven by late polling, candidate news, or early-vote data shifting attention to this competitive district."
  - "Resolves on the certified winner of the NC-09 House general election."
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
      poly_vol_24h_usd: 73439.095487
sources:
  - label: "ClearMarket market record: Will the winner of the NC-09 House election be determin"
    url: "https://clearmarket.fyi/events/nc-09-house-election-winner"
    retrieved_at: "2026-10-28T15:35:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh capital on the underdog Democratic side at 31% in a house race drawing nearly half its lifetime volume in one session warrants attention as a potential signal of shifting ground-level data in NC-09.
