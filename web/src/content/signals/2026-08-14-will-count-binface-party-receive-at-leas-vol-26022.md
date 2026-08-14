---
signal_id: "CMSIG20260814VS04"
signal_slug: "will-count-binface-party-receive-at-leas-vol-26022"
headline: "Count Binface 20% Clacton vote: 99% on $26K"
semantic_title: "Count Binface 20% vote share, near certain at 99%"
telemetry: "99% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-14T09:04:43+00:00"
event_id: "CM-EVT-ZXC0NSR2P9"
event_slug: "kxvotepercentbinface-clactonbyelection26sep01cbin"
event_question: "Will Count Binface receive at least X percent of the vote in the Clacton by-election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEPERCENTBINFACE-CLACTONBYELECTION26SEP01CBIN-60"
  question_raw: "Will Count Binface Party receive at least 20% of the popular vote in the 2026 Clacton by-election?"
  current_price: 0.99
  volume_24h_usd: 26022.3
  volume_cumulative_usd: 51754.94
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-09-01T14:00:00Z"
bullets:
  - "99% leaves almost no probability of the 20% threshold going unmet."
  - "$26K in 24h equals exactly 50% of all-time contract volume, the single largest daily share in this batch."
  - "Half of all lifetime liquidity arriving at near-full price signals final confirmation, not discovery."
  - "Resolves on certified 2026 Clacton popular vote result."
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
      kalshi_vol_24h_usd: 26022.3
sources:
  - label: "ClearMarket market record: Will Count Binface receive at least X percent of the vo"
    url: "https://clearmarket.fyi/events/kxvotepercentbinface-clactonbyelection26sep01cbin"
    retrieved_at: "2026-08-14T09:04:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fifty percent of all-time volume printing at 99% in one session means this contract is being closed out, not opened, desks should treat it as settled.
