---
signal_id: "CMSIG20260807VS00"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-177241"
headline: "Fed Sep hold: 50% on $177K inflow"
semantic_title: "Fed September hold sits at 50% through a volume surge"
telemetry: "50% · $177K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-07T08:54:29+00:00"
event_id: "CM-EVT-18Z2VTMCX0"
event_slug: "kxfeddecision-26sep"
event_question: "Will the Federal Reserve make a decision in September 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26SEP-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their September 2026 meeting?"
  current_price: 0.5
  volume_24h_usd: 177241.88
  volume_cumulative_usd: 487879.89
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Even-split odds signal maximum uncertainty on whether the Fed stands pat in September."
  - "$177K traded in 24h, 36% of all-time volume, marks a sharp acceleration of attention."
  - "August macro data window opens now; traders positioning ahead of jobs and CPI prints."
  - "Resolves at the September 2026 FOMC meeting decision."
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
      kalshi_vol_24h_usd: 177241.88
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in September 2"
    url: "https://clearmarket.fyi/events/kxfeddecision-26sep"
    retrieved_at: "2026-08-07T08:54:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 50/50 read with one-third of lifetime volume printing in a single day tells a rates desk that the September meeting is genuinely live and consensus has not formed.
