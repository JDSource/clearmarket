---
signal_id: "CMSIG20260811VS04"
signal_slug: "will-lisa-demuth-be-the-republican-nomin-vol-58182"
headline: "Demuth MN GOP governor: 73% on $58K surge"
semantic_title: "Demuth holds as MN GOP gubernatorial favorite at 73%"
telemetry: "73% · $58K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-JRLDTRKHR2"
event_slug: "kxgovmnnomr-26"
event_question: "Will the Minnesota Republican Party nominate a gubernatorial candidate by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVMNNOMR-26-LDEM"
  question_raw: "Will Lisa Demuth be the Republican nominee for Governor in Minnesota?"
  current_price: 0.73
  volume_24h_usd: 58182.23
  volume_cumulative_usd: 195154.62
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Market prices Demuth as a 73% favorite for the Minnesota Republican gubernatorial nomination."
  - "$58K in 24h volume, 30% of all-time, is the largest single-day draw on this contract."
  - "Volume surge points to fresh attention on the MN GOP field, possibly on a rival entering or exiting."
  - "Resolves YES if Demuth secures the Republican nomination for Minnesota governor in 2026."
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
      kalshi_vol_24h_usd: 58182.23
sources:
  - label: "ClearMarket market record: Will the Minnesota Republican Party nominate a gubernat"
    url: "https://clearmarket.fyi/events/kxgovmnnomr-26"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The largest 24h draw on this contract at a firm 73% suggests the MN GOP nomination race has a live catalyst, desks should check for recent field changes that may be driving traders to lock in exposure at current odds.
