---
signal_id: "CMSIG20260804VS07"
signal_slug: "will-bert-mizusawa-be-the-republican-nom-vol-10834"
headline: "Mizusawa VA Senate GOP nominee: 94% on $11K"
semantic_title: "Mizusawa locks in as Virginia GOP Senate pick at 94%"
telemetry: "94% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-04T10:33:57+00:00"
event_id: "CM-EVT-ZF0DQ0MY94"
event_slug: "kxsenatevar-26"
event_question: "Will the Virginia Republican Senate nominee be determined before the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEVAR-26-BMIZ"
  question_raw: "Will Bert Mizusawa be the Republican nominee for the Senate in Virginia?"
  current_price: 0.94
  volume_24h_usd: 10834.24
  volume_cumulative_usd: 32660.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "At 94%, Kalshi treats Mizusawa's Republican Senate nomination in Virginia as effectively decided."
  - "24h volume of $10.8K is 33% of all-time, a sharp single-session share for a near-resolved contract."
  - "Fresh volume at this price level suggests late entrants are closing out opposing positions rather than opening new ones."
  - "Resolves on the certified 2026 Virginia Republican Senate primary result."
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
      kalshi_vol_24h_usd: 10834.24
sources:
  - label: "ClearMarket market record: Will the Virginia Republican Senate nominee be determin"
    url: "https://clearmarket.fyi/events/kxsenatevar-26"
    retrieved_at: "2026-08-04T10:33:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 94% contract pulling a third of its lifetime volume in one day points to imminent resolution, a desk focused on the Virginia Senate general election should treat Mizusawa as the confirmed Republican nominee for planning purposes.
