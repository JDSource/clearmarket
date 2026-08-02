---
signal_id: "CMSIG20260802VS03"
signal_slug: "will-donavan-mckinney-be-the-democratic-vol-49153"
headline: "McKinney MI-13 Dem nominee: 86% on $49K"
semantic_title: "McKinney leads MI-13 Democratic primary betting at 86%"
telemetry: "86% · $49K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-02T09:53:38+00:00"
event_id: "CM-EVT-KJP3106M36"
event_slug: "mi-13-democratic-primary-winner"
event_question: "Will the Democratic primary winner be determined for Michigan's 13th congressional district by August 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2cfbd8aabc3519021dc16ab0c7e0f42b0fdac191e64bcc3c42c2319c4c0117f3"
  question_raw: "Will Donavan McKinney be the Democratic Nominee for MI-13?"
  current_price: 0.86
  volume_24h_usd: 49153.31053900003
  volume_cumulative_usd: 195461.59066400002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "Polymarket puts McKinney as the MI-13 Democratic nominee at 86%, strong consensus pricing with little uncertainty left."
  - "25% of all-time volume cleared in 24h, crossing the all-time quarter threshold and confirming active market interest."
  - "Coordinated with Thanedar contract activity; aggregate flow suggests traders are locking in the McKinney-wins narrative."
  - "Resolves on MI-13 primary outcome; high-confidence pricing may compress further if no late polling surprises emerge."
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
      poly_vol_24h_usd: 49153.31053900003
sources:
  - label: "ClearMarket market record: Will the Democratic primary winner be determined for Mi"
    url: "https://clearmarket.fyi/events/mi-13-democratic-primary-winner"
    retrieved_at: "2026-08-02T09:53:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into an 86% contract reflects conviction-locking ahead of primary resolution, desks are pricing out the tail of a Thanedar upset rather than expressing new bullish view.
