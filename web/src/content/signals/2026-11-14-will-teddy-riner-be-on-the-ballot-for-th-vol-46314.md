---
signal_id: "CMSIG20261114VS02"
signal_slug: "will-teddy-riner-be-on-the-ballot-for-th-vol-46314"
headline: "Riner 2027 ballot: 32% on $46K volume"
semantic_title: "Riner on the 2027 French ballot picks up at 32%"
telemetry: "32% · $46K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-14T07:48:40+00:00"
event_id: "CM-EVT-6Q8LZ5QQW0"
event_slug: "2027-french-presidential-election-who-will-be-on-the-ballot"
event_question: "Will Marine Le Pen be on the ballot for the 2027 French presidential election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4a467cd0e45358dfc86a1be7e9a7ecf1c0a563e3535f8cf6690bfa358a1cbf6f"
  question_raw: "Will Teddy Riner be on the ballot for the 2027 French presidential election?"
  current_price: 0.324
  volume_24h_usd: 46314.640138
  volume_cumulative_usd: 92994.93384400001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-17T00:00:00Z"
bullets:
  - "Polymarket prices Olympic champion Teddy Riner appearing on the 2027 French presidential ballot at 32%, a live but minority probability."
  - "24h volume of $46K is 50% of all-time, half of all trading on this contract arrived today."
  - "Spike likely triggered by French political commentary or Riner public statements drawing fresh speculative interest."
  - "Resolves ahead of the official 2027 candidate declaration window."
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
      poly_vol_24h_usd: 46314.640138
sources:
  - label: "ClearMarket market record: Will Marine Le Pen be on the ballot for the 2027 French"
    url: "https://clearmarket.fyi/events/2027-french-presidential-election-who-will-be-on-the-ballot"
    retrieved_at: "2026-11-14T07:48:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time volume arriving in a single session on a non-establishment candidacy signals that desks tracking French political tail risk are beginning to price a credible, if unlikely, outsider entry into the 2027 race.
