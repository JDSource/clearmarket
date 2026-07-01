---
signal_id: "CMSIG20260701VS06"
signal_slug: "will-samuel-alito-retires-the-supreme-co-vol-47435"
headline: "Alito exits Supreme Court before 2027: 34% on $47K"
semantic_title: "Flows test Alito retirement odds ahead of recess"
telemetry: "34% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-01T11:21:48+00:00"
event_id: "CM-EVT-D6V79HLL45"
event_slug: "kxalitoout"
event_question: "Will Justice Alito retire from the Supreme Court?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXALITOOUT-27JAN01"
  question_raw: "Will Samuel Alito retires the Supreme Court in before 2027?"
  current_price: 0.34
  volume_24h_usd: 47435.12
  volume_cumulative_usd: 64615.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a 34% probability that Justice Alito retires before end of 2026, meaningful tail."
  - "$47K in 24h equals 73% of all-time volume; contract is drawing concentrated fresh attention."
  - "SCOTUS summer recess is the natural window for retirement announcements, driving near-term focus."
  - "A 34% price reflects genuine uncertainty; desks should monitor for health or political disclosures."
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
      kalshi_vol_24h_usd: 47435.12
sources:
  - label: "ClearMarket market record: Will Justice Alito retire from the Supreme Court?"
    url: "https://clearmarket.fyi/events/kxalitoout"
    retrieved_at: "2026-07-01T11:21:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Alito retirement odds at 34% with 73% of all-time volume printing in one session indicate the SCOTUS composition trade is live and heating into the summer recess window, relevant for any rates/regulatory long-horizon book.
