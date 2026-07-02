---
signal_id: "CMSIG20260702VS06"
signal_slug: "will-above-20000-jobs-be-added-in-june-2-vol-19630"
headline: "June jobs above 20K: 94% on $19.6K Kalshi spike"
semantic_title: "Macro desks stack conviction on a 20K-plus June jobs print"
telemetry: "94% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-02T10:35:06+00:00"
event_id: "CM-EVT-NHWMG744L8"
event_slug: "kxpayrolls-26jun"
event_question: "Nonfarm payroll employment change, June 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26JUN-T20000"
  question_raw: "Will above 20000 jobs be added in June 2026?"
  current_price: 0.94
  volume_24h_usd: 19630.08
  volume_cumulative_usd: 28229.96
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "94% price reflects strong consensus that June 2026 nonfarm payrolls will clear the 20,000 threshold."
  - "$19.6K in 24h, 70% of all-time volume, is the dominant single-session flow in this contract's history."
  - "Surge likely precedes Friday's NFP release; 70% all-time share confirms this is a pre-report positioning rush."
  - "Resolution on the official BLS June 2026 payrolls release; low bar of 20K adds to high-confidence pricing."
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
      kalshi_vol_24h_usd: 19630.08
sources:
  - label: "ClearMarket market record: Nonfarm payroll employment change, June 2026"
    url: "https://clearmarket.fyi/events/kxpayrolls-26jun"
    retrieved_at: "2026-07-02T10:35:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 70% all-time volume concentration in a single pre-report session signals desks are using this low-bar contract as a cheap macro hedge or directional expression ahead of Friday's NFP, watch for correlated moves in rates and USD contracts.
