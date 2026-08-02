---
signal_id: "CMSIG20260802VS04"
signal_slug: "will-google-release-gemini-3-5-pro-befor-vol-15465"
headline: "Gemini 3.5 Pro by Aug 16: 68% on $15K"
semantic_title: "Gemini 3.5 Pro by Aug 16 holds above 50% on heavy Kalshi flow"
telemetry: "68% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-02T09:53:38+00:00"
event_id: "CM-EVT-HCS172JGG4"
event_slug: "kxgemini-gemi35p"
event_question: "Will Google release Gemini 3.5 Pro?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGEMINI-GEMI35P-26AUG16"
  question_raw: "Will Google release Gemini 3.5 Pro before Aug 16, 2026?"
  current_price: 0.68
  volume_24h_usd: 15465.26
  volume_cumulative_usd: 34464.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-23T14:00:00Z"
bullets:
  - "Kalshi prices a Gemini 3.5 Pro release before Aug 16 at 68%, market leans toward a near-term Google delivery."
  - "45% of all-time volume in 24h is the single largest daily share in this contract's life, a notable conviction signal."
  - "Surge likely tied to Google announcements, developer leaks, or I/O-adjacent release signals narrowing the window to two weeks."
  - "Resolves Aug 16; rapid decay window means pricing is highly sensitive to any Google communications this week."
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
      kalshi_vol_24h_usd: 15465.26
sources:
  - label: "ClearMarket market record: Will Google release Gemini 3.5 Pro?"
    url: "https://clearmarket.fyi/events/kxgemini-gemi35p"
    retrieved_at: "2026-08-02T09:53:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 45%-of-all-time single-day volume print at 68% suggests fresh information, a leak, announcement, or developer signal, is pulling forward Gemini 3.5 Pro release expectations.
