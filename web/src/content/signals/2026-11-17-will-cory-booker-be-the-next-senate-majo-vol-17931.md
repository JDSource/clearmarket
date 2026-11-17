---
signal_id: "CMSIG20261117VS00"
signal_slug: "will-cory-booker-be-the-next-senate-majo-vol-17931"
headline: "Booker majority leader: 0% on $17.9K surge"
semantic_title: "Booker Senate Majority Leader odds collapse to zero"
telemetry: "0% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-17T07:48:39+00:00"
event_id: "CM-EVT-ZZZ60Y4302"
event_slug: "next-senate-majority-leader-485"
event_question: "Who will be the Senate Majority Leader in the next Congress?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x68bdc81862795e3572a2df9e0ad2e0150c9e2450c3ce78d3534bdcfd7da3ef5b"
  question_raw: "Will Cory Booker be the next Senate Majority Leader?"
  current_price: 0.002
  volume_24h_usd: 17931.120000000003
  volume_cumulative_usd: 28359.07728
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-03T00:00:00Z"
bullets:
  - "Market prices Booker at 0%, the Senate Majority Leader bid is effectively ruled out."
  - "24h volume of $17.9K is 63% of all-time handle, compressing nearly all lifetime flow into one session."
  - "Fresh attention likely triggered by a caucus vote, rival announcement, or Booker public statement closing the door."
  - "Resolves when Senate Democrats formally select a Majority Leader; market is already pricing a settled outcome."
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
      poly_vol_24h_usd: 17931.120000000003
sources:
  - label: "ClearMarket market record: Who will be the Senate Majority Leader in the next Cong"
    url: "https://clearmarket.fyi/events/next-senate-majority-leader-485"
    retrieved_at: "2026-11-17T07:48:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A single-session flush of 63% of lifetime volume into a zero-priced contract signals the desk that this race has effectively closed, monitor Senate Democratic caucus news for the confirming event.
