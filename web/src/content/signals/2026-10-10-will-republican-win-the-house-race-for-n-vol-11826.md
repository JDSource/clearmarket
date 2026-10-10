---
signal_id: "CMSIG20261010VS05"
signal_slug: "will-republican-win-the-house-race-for-n-vol-11826"
headline: "NC-11 GOP House: 23% on $12K volume push"
semantic_title: "NC-11 Republican odds slip to 23% under fresh pressure"
telemetry: "23% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T14:12:44+00:00"
event_id: "CM-EVT-0N8GC3M3K5"
event_slug: "kxhousenc11-26"
event_question: "Who will win the North Carolina 11th congressional district House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSENC11-26-GOP"
  question_raw: "Will Republican win the House race for NC-11?"
  current_price: 0.23
  volume_24h_usd: 11826.53
  volume_cumulative_usd: 29077.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republican at just 23%, the market treats NC-11 as leaning strongly Democratic."
  - "$12K in 24h equals 41% of all-time contract volume, a meaningful acceleration for a lower-dollar race."
  - "Attention on a 23% contract often precedes a news event testing whether the longshot is truly priced correctly."
  - "Resolves on NC-11 general election outcome."
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
      kalshi_vol_24h_usd: 11826.53
sources:
  - label: "ClearMarket market record: Who will win the North Carolina 11th congressional dist"
    url: "https://clearmarket.fyi/events/kxhousenc11-26"
    retrieved_at: "2026-10-10T14:12:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that nearly half of a contract's lifetime volume hitting on a 23% price is a signal that someone is actively stress-testing an assumed outcome, worth monitoring for candidate or district news.
