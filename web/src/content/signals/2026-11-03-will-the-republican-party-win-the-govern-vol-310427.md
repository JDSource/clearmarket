---
signal_id: "CMSIG20261103VS05"
signal_slug: "will-the-republican-party-win-the-govern-vol-310427"
headline: "Ohio GOP governor: 18% on $310K volume"
semantic_title: "Ohio Republican governor bid trades as an underdog at 18%"
telemetry: "18% · $310K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T07:49:22+00:00"
event_id: "CM-EVT-ZJYN286LR2"
event_slug: "govpartyoh-26"
event_question: "Ohio Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYOH-26-R"
  question_raw: "Will the Republican party win the governorship in Ohio"
  current_price: 0.18
  volume_24h_usd: 310427.72
  volume_cumulative_usd: 1239184.71
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Ohio governorship win at only 18%, making the Democrat a strong favorite."
  - "25% of all-time volume, a quarter-milestone surge, hits on Election Day as positions are finalized."
  - "Ohio's governor race has shifted toward Democrats; 18% GOP pricing reflects the market's current read of the structural lean."
  - "Resolves on certified Ohio gubernatorial results."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 310427.72
sources:
  - label: "ClearMarket market record: Ohio Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyoh-26"
    retrieved_at: "2026-11-03T07:49:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $310K Election Day surge into an 18% Republican contract tells a desk the Ohio governor race has been all but called for Democrats in prediction-market pricing.
