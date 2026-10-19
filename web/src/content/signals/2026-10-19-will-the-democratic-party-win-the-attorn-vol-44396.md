---
signal_id: "CMSIG20261019VS00"
signal_slug: "will-the-democratic-party-win-the-attorn-vol-44396"
headline: "NY AG Dem win: 89% on $44K volume surge"
semantic_title: "Buyers back the NY AG Democratic hold at 89%"
telemetry: "89% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-19T07:48:06+00:00"
event_id: "CM-EVT-2WVDLYDTS5"
event_slug: "kxattygenny-26"
event_question: "Will the New York Attorney General race be decided by January 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXATTYGENNY-26-D"
  question_raw: "Will the Democratic party win the Attorney General race in New York?"
  current_price: 0.89
  volume_24h_usd: 44396.94
  volume_cumulative_usd: 166260.29
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Market prices a near-certain Democratic hold of the New York Attorney General seat at 89%."
  - "Kalshi logs $44K in 24h volume, 27% of the contract's entire all-time traded value in one session."
  - "Late-cycle attention at this confidence level suggests traders are stress-testing the lead, not doubting it."
  - "Resolves on New York AG election results; any Republican upset would be a significant repricing event."
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
      kalshi_vol_24h_usd: 44396.94
sources:
  - label: "ClearMarket market record: Will the New York Attorney General race be decided by J"
    url: "https://clearmarket.fyi/events/kxattygenny-26"
    retrieved_at: "2026-10-19T07:48:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A fresh capital deployment at an 89% consensus signals the desk is watching for any last-minute shock that could reprice a race the market considers effectively settled.
