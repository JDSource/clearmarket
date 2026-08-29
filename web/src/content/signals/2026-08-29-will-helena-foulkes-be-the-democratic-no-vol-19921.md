---
signal_id: "CMSIG20260829VS04"
signal_slug: "will-helena-foulkes-be-the-democratic-no-vol-19921"
headline: "Foulkes RI Dem nominee: 100% on $20K"
semantic_title: "Foulkes RI governor nomination trades at 100% on heavy flow"
telemetry: "100% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-29T13:34:58+00:00"
event_id: "CM-EVT-ZVCJ160PY0"
event_slug: "kxgovrinomd-26"
event_question: "Will Rhode Island have a Democratic Governor nominee by September 8, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVRINOMD-26-HFOU"
  question_raw: "Will Helena Foulkes be the Democratic nominee for Governor in Rhode Island?"
  current_price: 0.996
  volume_24h_usd: 19921.99
  volume_cumulative_usd: 28262.81
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "100% price leaves zero market-implied probability of any other Democratic gubernatorial nominee in Rhode Island."
  - "Kalshi logs $20K in 24h, representing 70% of all-time volume, an unusually concentrated single-day surge."
  - "Volume at a ceiling price typically reflects late liquidity-taking or settlement positioning ahead of primary close."
  - "Resolves on the Rhode Island Democratic gubernatorial primary result."
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
      kalshi_vol_24h_usd: 19921.99
sources:
  - label: "ClearMarket market record: Will Rhode Island have a Democratic Governor nominee by"
    url: "https://clearmarket.fyi/events/kxgovrinomd-26"
    retrieved_at: "2026-08-29T13:34:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

70% of all-time volume in one day on a 100% contract is a settlement-flow signal, a desk should treat this as near-certain resolution and close any opposing exposure immediately.
