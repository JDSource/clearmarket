---
signal_id: "CMSIG20260730VS02"
signal_slug: "will-the-fed-increase-interest-rates-by-vol-422177"
headline: "Fed +25 bps Sep: 57% on $422K volume"
semantic_title: "A 25 bps Fed hike in September leads the rate book"
telemetry: "57% · $422K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-30T10:21:41+00:00"
event_id: "CM-EVT-LZ9Q8BDFL0"
event_slug: "fed-decision-in-september-762"
event_question: "Will the Federal Reserve make a decision in September?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x876506d8b2bd7a0d3fa4fe18c024eee6e1dd81ee24c26795dadd6cfe4a7b5d0d"
  question_raw: "Will the Fed increase interest rates by 25 bps after the September 2026 meeting?"
  current_price: 0.57
  volume_24h_usd: 422177.19761699997
  volume_cumulative_usd: 1528961.125628
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-16T00:00:00Z"
bullets:
  - "57% pricing makes a 25 bps hike the single most likely Fed outcome priced across the September contract suite."
  - "$422K in 24h volume represents 28% of all-time, a notable but not dominant session, consistent with incremental conviction."
  - "Read alongside the hold contract at 39%, the market is pricing a hiking bias with a meaningful pause tail."
  - "Resolves on the September 2026 FOMC announcement; the 57% level sets the current consensus benchmark."
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
      poly_vol_24h_usd: 422177.19761699997
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September?"
    url: "https://clearmarket.fyi/events/fed-decision-in-september-762"
    retrieved_at: "2026-07-30T10:21:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 25 bps hike contract leading at 57% while the hold contract sits at 39% tells a desk the market has a hiking lean but retains real uncertainty, duration and rates vol positioning should reflect a bimodal, not base-case, distribution.
