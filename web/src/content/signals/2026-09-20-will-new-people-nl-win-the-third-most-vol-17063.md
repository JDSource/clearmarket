---
signal_id: "CMSIG20260920VS02"
signal_slug: "will-new-people-nl-win-the-third-most-vol-17063"
headline: "New People Duma third: 65% on $17K volume"
semantic_title: "New People favored for third place in Russian Duma at 65%"
telemetry: "65% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T07:47:56+00:00"
event_id: "CM-EVT-CJPNXB53C5"
event_slug: "russia-parliamentary-election-3rd-place"
event_question: "Will a party other than United Russia or the Communist Party of the Russian Federation finish in third place in the next Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c511719257c8e4f486fc30696ae718c250eb24eef1fd9fae0bbae774f5e876e"
  question_raw: "Will New People (NL) win the third-most seats in the next Russian parliamentary election?"
  current_price: 0.65
  volume_24h_usd: 17063.341959
  volume_cumulative_usd: 54513.32641599999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "65% odds put New People (NL) as the probable third-largest party in the next Russian parliamentary election."
  - "$17K in 24h is 31% of all-time volume, a meaningful single-session concentration."
  - "Surge may reflect updated polling or a shift in the LDPR contest (see Spike 3)."
  - "Resolution tied to the next Russian parliamentary election cycle."
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
      poly_vol_24h_usd: 17063.341959
sources:
  - label: "ClearMarket market record: Will a party other than United Russia or the Communist "
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-3rd-place"
    retrieved_at: "2026-09-20T07:47:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Paired volume spikes on New People and LDPR contracts suggest traders are actively rotating between the two third-place candidates, a desk should track both legs as a spread.
