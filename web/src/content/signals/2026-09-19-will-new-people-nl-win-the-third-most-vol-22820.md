---
signal_id: "CMSIG20260919VS04"
signal_slug: "will-new-people-nl-win-the-third-most-vol-22820"
headline: "New People third in Duma: 78% on $23K"
semantic_title: "New People party finishing third in Duma vote finds buyers"
telemetry: "78% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-CJPNXB53C5"
event_slug: "russia-parliamentary-election-3rd-place"
event_question: "Will a party other than United Russia or the Communist Party of the Russian Federation finish in third place in the next Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c511719257c8e4f486fc30696ae718c250eb24eef1fd9fae0bbae774f5e876e"
  question_raw: "Will New People (NL) win the third-most seats in the next Russian parliamentary election?"
  current_price: 0.78
  volume_24h_usd: 22820.5986
  volume_cumulative_usd: 48857.727974
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices New People (NL) winning the third-most Duma seats at 78%, strong market consensus."
  - "24h volume of $23K is 47% of all-time handle, the contract's most active session by a wide margin."
  - "Elevated odds and heavy volume together suggest traders see NL's third-place finish as the path-of-least-resistance outcome."
  - "Resolves on official Russian parliamentary election seat tallies."
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
      poly_vol_24h_usd: 22820.5986
sources:
  - label: "ClearMarket market record: Will a party other than United Russia or the Communist "
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-3rd-place"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-majority of all-time volume arriving in a single session at 78% indicates desks are consolidating around NL as the clear third-party in Russian parliamentary positioning.
