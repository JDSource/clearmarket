---
signal_id: "CMSIG20260925VS06"
signal_slug: "will-the-democratic-party-win-the-al-05-vol-11930"
headline: "AL-05 Dem House seat: 3% on $11K surge"
semantic_title: "AL-05 Democratic House odds stay near zero under fresh volume"
telemetry: "3% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T07:48:30+00:00"
event_id: "CM-EVT-LN7341VVS9"
event_slug: "al-05-house-election-winner"
event_question: "Will a Republican win the AL-05 House election in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x983d15d52f8780293cfb996daee22ce1327bf5349ac473b02c6ef07829ffb6f0"
  question_raw: "Will the Democratic Party win the AL-05 House seat?"
  current_price: 0.031
  volume_24h_usd: 11930.71889
  volume_cumulative_usd: 33793.611516
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democrats at just 3% in Alabama's 5th, the market rates a Democratic win as a remote tail risk."
  - "$11K in 24h equals 35% of all-time volume, a meaningful single-session spike for a near-zero price contract."
  - "Volume at near-zero odds often reflects speculative positioning on a long-shot or hedging within a broader district portfolio."
  - "Resolves on the AL-05 House election in November 2026."
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
      poly_vol_24h_usd: 11930.71889
sources:
  - label: "ClearMarket market record: Will a Republican win the AL-05 House election in 2026?"
    url: "https://clearmarket.fyi/events/al-05-house-election-winner"
    retrieved_at: "2026-09-25T07:48:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Elevated volume on a 3% Democratic contract in deep-red Alabama is more likely speculative tail-buying than informed flow, but desks tracking House control math should note any price drift from this base.
