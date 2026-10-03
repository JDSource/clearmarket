---
signal_id: "CMSIG20261003VS00"
signal_slug: "will-the-nasdaq-100-be-above-30999-99-at-vol-15140"
headline: "Nasdaq-100 Dec close: 99% on $15K surge"
semantic_title: "Nasdaq-100 above 30K by year-end stays a near-lock"
telemetry: "99% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T07:48:19+00:00"
event_id: "CM-EVT-HYFSJ2CNW7"
event_slug: "kxnasdaq100maxy-26dec31h1600"
event_question: "What will be the highest price reached by the Nasdaq-100 in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNASDAQ100MAXY-26DEC31H1600-T30999.99"
  question_raw: "Will the Nasdaq-100 be above 30999.99 at the end of Dec 31, 2026 at 4pm EST?"
  current_price: 0.99
  volume_24h_usd: 15140.89
  volume_cumulative_usd: 20429.79
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T00:00:00Z"
bullets:
  - "Kalshi contract at 99%, market treats Nasdaq-100 finishing above 31K on Dec 31 as essentially certain."
  - "24h volume of $15K is 74% of all-time contract volume, signaling concentrated late-cycle positioning."
  - "Fresh activity at this extreme price likely reflects hedgers locking in or arb traders compressing residual tail risk."
  - "Resolves at 4 pm EST Dec 31, 2026 based on Nasdaq-100 official close."
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
      kalshi_vol_24h_usd: 15140.89
sources:
  - label: "ClearMarket market record: What will be the highest price reached by the Nasdaq-10"
    url: "https://clearmarket.fyi/events/kxnasdaq100maxy-26dec31h1600"
    retrieved_at: "2026-10-03T07:48:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that near-unity pricing drawing 74% of all-time volume in one session suggests active residual-risk management, not speculative inflow, watch for correlated equity tail hedges.
