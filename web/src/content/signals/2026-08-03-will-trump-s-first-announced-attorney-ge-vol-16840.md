---
signal_id: "CMSIG20260803VS02"
signal_slug: "will-trump-s-first-announced-attorney-ge-vol-16840"
headline: "Trump AG confirmation: 76% on $17K volume spike"
semantic_title: "Buyers back Trump AG confirmation at 76%"
telemetry: "76% · $17K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-03T11:19:10+00:00"
event_id: "CM-EVT-NY76DC3G68"
event_slug: "kxagconf-26"
event_question: "Will Todd Blanche be confirmed?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAGCONF-26JUN05-SEP01"
  question_raw: "Will Trump's first announced Attorney General pick be confirmed as Attorney General before Sep 1, 2026?"
  current_price: 0.76
  volume_24h_usd: 16840.63
  volume_cumulative_usd: 63526.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "At 76%, the market gives the nominee a clear but not certain path to Senate confirmation."
  - "$16.8K in 24h equals 27% of all-time volume, a meaningful single-session concentration."
  - "Senate Judiciary Committee activity or a scheduled confirmation vote likely triggered fresh positioning."
  - "Resolves on Senate confirmation of Trump's first announced Attorney General pick."
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
      kalshi_vol_24h_usd: 16840.63
sources:
  - label: "ClearMarket market record: Will Todd Blanche be confirmed?"
    url: "https://clearmarket.fyi/events/kxagconf-26"
    retrieved_at: "2026-08-03T11:19:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 27% all-time volume share in one day at 76% odds indicates desks are actively repricing confirmation risk, likely tied to a committee vote or new floor schedule announcement.
