---
signal_id: "CMSIG20260808VS00"
signal_slug: "will-the-fed-increase-interest-rates-by-vol-723198"
headline: "Fed 50bps Sept hike: 0% on $723K surge"
semantic_title: "A 50+ bps Fed hike in September stays a near-zero bet"
telemetry: "0% · $723K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-08T08:36:03+00:00"
event_id: "CM-EVT-LZ9Q8BDFL0"
event_slug: "fed-decision-in-september-762"
event_question: "Will the Federal Reserve make a decision in September?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2e4b58fc18dbffd74d5275d89fb076943f21992763c45dcadd81391b83bde13c"
  question_raw: "Will the Fed increase interest rates by 50+ bps after the September 2026 meeting?"
  current_price: 0.005
  volume_24h_usd: 723198.97096
  volume_cumulative_usd: 2600501.9645910007
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-16T00:00:00Z"
bullets:
  - "Kalshi prices a 50+ bps September hike at 0%, the market sees it as essentially impossible."
  - "24h volume of $723K is 28% of all-time, marking the largest single-day activity on this contract."
  - "Surge likely driven by macro traders closing or testing the floor ahead of September FOMC positioning."
  - "Resolves after the September 2026 Fed meeting decision."
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
      poly_vol_24h_usd: 723198.97096
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September?"
    url: "https://clearmarket.fyi/events/fed-decision-in-september-762"
    retrieved_at: "2026-08-08T08:36:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-zero price holding through a $723K volume surge tells a rates desk there is no credible scenario being priced for aggressive Fed tightening in September.
