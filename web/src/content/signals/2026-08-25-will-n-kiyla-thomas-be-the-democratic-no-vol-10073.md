---
signal_id: "CMSIG20260825VS05"
signal_slug: "will-n-kiyla-thomas-be-the-democratic-no-vol-10073"
headline: "Thomas OK Dem Senate nom: 92% on $10K surge"
semantic_title: "N'Kiyla Thomas backed as Oklahoma Dem Senate pick at 92%"
telemetry: "92% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-25T08:37:37+00:00"
event_id: "CM-EVT-CZVRJYSHK1"
event_slug: "kxsenateokd-26"
event_question: "Will the Oklahoma Democratic Senate nominee be determined before the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEOKD-26-NTHO"
  question_raw: "Will N’Kiyla Thomas be the Democratic nominee for the Senate in Oklahoma?"
  current_price: 0.916
  volume_24h_usd: 10073.2
  volume_cumulative_usd: 33163.86
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices N'Kiyla Thomas as the Oklahoma Democratic Senate nominee at 92%, near-settled by market consensus."
  - "24h volume of $10K is 30% of all-time, a notable single-day share for a state-level primary contract."
  - "Oklahoma Senate primary activity at this price suggests a filing or ballot qualification update may have resolved remaining uncertainty."
  - "Resolves upon official Democratic primary result; high odds leave little room for a reversal."
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
      kalshi_vol_24h_usd: 10073.2
sources:
  - label: "ClearMarket market record: Will the Oklahoma Democratic Senate nominee be determin"
    url: "https://clearmarket.fyi/events/kxsenateokd-26"
    retrieved_at: "2026-08-25T08:37:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 30% all-time volume surge into a 92% nominee contract points to a recent procedural development, filing confirmation or a competitor withdrawal, that desks are pricing as essentially conclusive.
