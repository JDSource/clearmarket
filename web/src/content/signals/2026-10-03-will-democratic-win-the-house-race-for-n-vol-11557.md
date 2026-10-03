---
signal_id: "CMSIG20261003VS05"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-11557"
headline: "Democrat NC-11 House: 68% on $12K surge"
semantic_title: "Traders pile into Democrat at 68% in NC-11 House race"
telemetry: "68% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T07:48:19+00:00"
event_id: "CM-EVT-0N8GC3M3K5"
event_slug: "kxhousenc11-26"
event_question: "Who will win the North Carolina 11th congressional district House election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSENC11-26-DEM"
  question_raw: "Will Democratic win the House race for NC-11?"
  current_price: 0.68
  volume_24h_usd: 11557.74
  volume_cumulative_usd: 37529.93
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi contract prices Democratic win in North Carolina's 11th District at 68%, a meaningful lean in a traditionally Republican-leaning mountain district."
  - "24h volume of $12K is 31% of all-time contract activity, indicating a sharp one-day focus on this race."
  - "NC-11 has been reliably Republican; pricing at 68% Democratic with a volume surge points to a significant local development, candidate, scandal, or polling shift, warranting immediate monitoring."
  - "Resolves on 2026 general election certified result for NC-11."
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
      kalshi_vol_24h_usd: 11557.74
sources:
  - label: "ClearMarket market record: Who will win the North Carolina 11th congressional dist"
    url: "https://clearmarket.fyi/events/kxhousenc11-26"
    retrieved_at: "2026-10-03T07:48:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat NC-11 at 68% Democratic as a high-signal anomaly, this district's historical lean makes a 68% Democratic price noteworthy, and the volume surge suggests informed flow ahead of a public catalyst.
