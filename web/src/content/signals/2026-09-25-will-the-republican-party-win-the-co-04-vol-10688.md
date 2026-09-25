---
signal_id: "CMSIG20260925VS05"
signal_slug: "will-the-republican-party-win-the-co-04-vol-10688"
headline: "CO-04 GOP House seat: 70% on $10K volume"
semantic_title: "Traders pile into CO-04 Republican House odds at 70%"
telemetry: "70% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T07:48:30+00:00"
event_id: "CM-EVT-7T2BJXLWQ5"
event_slug: "co-04-house-election-winner"
event_question: "CO-04 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x13d25ac2d08197538635b4879303c2e01e1e6f2250eaeca4cd2a81fbf864fb9d"
  question_raw: "Will the Republican Party win the CO-04 House seat?"
  current_price: 0.7
  volume_24h_usd: 10688.090304999998
  volume_cumulative_usd: 25137.969317
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans at 70% in Colorado's 4th, competitive but leaning GOP."
  - "$10K in 24h represents 43% of all-time volume, a notable concentration of activity."
  - "CO-04 has been a swing-district flashpoint; fresh volume suggests bettors see a near-term catalyst or news development."
  - "Resolves on the CO-04 House general election in November 2026."
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
      poly_vol_24h_usd: 10688.090304999998
sources:
  - label: "ClearMarket market record: CO-04 House Election Winner"
    url: "https://clearmarket.fyi/events/co-04-house-election-winner"
    retrieved_at: "2026-09-25T07:48:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 43% lifetime-volume day on a 70% Republican price in a genuine swing district warrants desk attention as a potential leading indicator ahead of candidate or polling news.
