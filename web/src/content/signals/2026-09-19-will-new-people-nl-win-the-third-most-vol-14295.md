---
signal_id: "CMSIG20260919VS05"
signal_slug: "will-new-people-nl-win-the-third-most-vol-14295"
headline: "New People third-most Duma seats: 61% on $14K"
semantic_title: "New People party stays favored for third-place Duma finish"
telemetry: "61% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T07:47:59+00:00"
event_id: "CM-EVT-CJPNXB53C5"
event_slug: "russia-parliamentary-election-3rd-place"
event_question: "Will a party other than United Russia or the Communist Party of the Russian Federation finish in third place in the next Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c511719257c8e4f486fc30696ae718c250eb24eef1fd9fae0bbae774f5e876e"
  question_raw: "Will New People (NL) win the third-most seats in the next Russian parliamentary election?"
  current_price: 0.61
  volume_24h_usd: 14295.602908
  volume_cumulative_usd: 37449.984457000006
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices New People (NL) at 61% to finish third in seat count, a moderate conviction lead."
  - "38% of all-time volume in one session suggests active comparison-trading against other Duma party outcome contracts."
  - "61% implies traders see NL ahead of LDPR and A Just Russia in the final tally but the race is not closed."
  - "Resolves on official Duma seat certification after the next Russian parliamentary election."
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
      poly_vol_24h_usd: 14295.602908
sources:
  - label: "ClearMarket market record: Will a party other than United Russia or the Communist "
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-3rd-place"
    retrieved_at: "2026-09-19T07:47:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

This contract is most useful as a relative-value read against companion Duma contracts; the 38% single-day volume share suggests arbitrage activity across the Russian parliamentary outcome suite rather than standalone directional conviction.
