---
signal_id: "CMSIG20261018VS01"
signal_slug: "will-the-republican-party-win-the-nc-11-vol-16982"
headline: "NC-11 GOP win: 17% on $17K volume pop"
semantic_title: "NC-11 Republican odds slip to long-shot territory"
telemetry: "17% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-18T12:26:25+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe64ec54460a1f1b250c9785968e6ebecfb0fd542a34300a161f64460c7a811df"
  question_raw: "Will the Republican Party win the NC-11 House seat?"
  current_price: 0.17
  volume_24h_usd: 16982.062131
  volume_cumulative_usd: 30464.597665
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Polymarket prices Republican NC-11 win at just 17%, flagging the seat as strongly Democratic-leaning."
  - "24h volume of $17K is a striking 56% of the contract's entire all-time handle, signaling a sharp attention spike."
  - "Over half of lifetime volume arriving in one session points to a recent polling release or ballot development driving reassessment."
  - "NC-11 and its Democratic counterpart (Spike 2) are trading simultaneously, the paired flow confirms a directional repricing event."
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
      poly_vol_24h_usd: 16982.062131
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-18T12:26:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The paired surge across both NC-11 contracts in a single session is the clearest tell that new information, likely a poll or candidate development, is forcing a rapid rerating of this district.
