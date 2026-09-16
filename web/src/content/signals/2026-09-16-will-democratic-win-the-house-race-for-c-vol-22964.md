---
signal_id: "CMSIG20260916VS04"
signal_slug: "will-democratic-win-the-house-race-for-c-vol-22964"
headline: "Dem wins CA-22 House: 92% on $23K volume spike"
semantic_title: "Democrats near-certain to hold CA-22 House seat"
telemetry: "92% · $23K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-BGY2J6YL26"
event_slug: "houseca22-26"
event_question: "CA-22 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSECA22-26-D"
  question_raw: "Will Democratic win the House race for CA-22?"
  current_price: 0.918
  volume_24h_usd: 22964.91
  volume_cumulative_usd: 49557.14
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic hold in CA-22 at 92%, leaving only an 8% path for a Republican flip."
  - "46% of all-time volume, $23K, arrived in 24h, a significant concentration for a single House race."
  - "CA-22 is a competitive Central Valley district; the high price suggests recent data strongly favors the Democratic candidate."
  - "Resolves on 2026 midterm election night; the 8% Republican tail remains the active trading opportunity."
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
      kalshi_vol_24h_usd: 22964.91
sources:
  - label: "ClearMarket market record: CA-22 House winner?"
    url: "https://clearmarket.fyi/events/houseca22-26"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sharp one-session volume at a 92% Democratic price on a historically competitive district suggests a meaningful informational update, desks tracking House majority scenarios should note the reduced flip probability here.
