---
signal_id: "CMSIG20260804VS02"
signal_slug: "will-donavan-mckinney-be-the-democratic-vol-110168"
headline: "McKinney MI-13 nominee: 87% on $110K volume"
semantic_title: "Buyers back McKinney as the MI-13 Democratic pick at 87%"
telemetry: "87% · $110K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-04T10:33:57+00:00"
event_id: "CM-EVT-KJP3106M36"
event_slug: "mi-13-democratic-primary-winner"
event_question: "Will the Democratic primary winner be determined for Michigan's 13th congressional district by August 4, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2cfbd8aabc3519021dc16ab0c7e0f42b0fdac191e64bcc3c42c2319c4c0117f3"
  question_raw: "Will Donavan McKinney be the Democratic Nominee for MI-13?"
  current_price: 0.87
  volume_24h_usd: 110168.360489
  volume_cumulative_usd: 344316.2094299998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-04T00:00:00Z"
bullets:
  - "At 87%, Polymarket treats McKinney as the strong frontrunner for the MI-13 Democratic nomination."
  - "24h volume of $110K is 32% of all-time, substantial single-session conviction behind the leading position."
  - "Simultaneous volume on Thanedar (13%) confirms the field is collapsing around McKinney as primary day nears."
  - "Resolves on the certified MI-13 Democratic primary nominee."
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
      poly_vol_24h_usd: 110168.360489
sources:
  - label: "ClearMarket market record: Will the Democratic primary winner be determined for Mi"
    url: "https://clearmarket.fyi/events/mi-13-democratic-primary-winner"
    retrieved_at: "2026-08-04T10:33:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Coordinated volume across both the McKinney and Thanedar contracts in one session signals the market has reached near-terminal certainty, a desk can treat the 13% residual as tail risk, not genuine contest.
