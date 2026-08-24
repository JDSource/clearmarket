---
signal_id: "CMSIG2026082102"
signal_slug: "aug-u-3-rate-seen-4-1-4-2-kalshi-ladder-2026-08-21"
headline: "Aug U-3 rate seen 4.1-4.2%: Kalshi ladder"
semantic_title: "August unemployment rate holds near 4.1 to 4.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-21T00:00:00.000Z"
event_id: "CM-EVT-CN1M891289"
event_slug: "kxu3-26aug"
event_question: "August 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26AUG-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in August?"
  current_price: 0.23
  volume_24h_usd: 2157.66
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-04T14:00:00Z"
bullets:
  - "Kalshi ladder implies August U-3 unemployment in the 4.1-4.2% range: 54% above 4.1%, only 23% above 4.2%."
  - "Claims falling to 206,000 is consistent with the ladder's tight clustering just above 4.1%, signaling no labor-market deterioration."
  - "The four-week average rising despite the weekly dip is a mechanical artifact; the distribution shows little tail risk above 4.5%."
  - "Companion Kalshi ladder for September (CM-EVT-720DZC17Y9) implies 4.2-4.3%, suggesting the market sees a gradual drift, not a spike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Initial jobless claims fell 6,000 to 206,000 for the week ending August 15, though the four-week average rose due to rolling-window effects."
    publisher: "Tomas Ferreira"
    published_at: "2026-08-21T00:00:00.000Z"
    source_url: "https://usmarketcurrent.com/claims-fell-6000-and-the-four-week-average-still-rose-4250-august-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tomas Ferreira"
        source_url: "https://usmarketcurrent.com/claims-fell-6000-and-the-four-week-average-still-rose-4250-august-2026/"
        retrieved_at: "2026-08-24T08:42:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves on the Bureau of Labor Statistics U-3 unemployment rate for August 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tomas Ferreira: Initial claims fell 6,000 to 206,000. The four-week average rose anywa"
    url: "https://usmarketcurrent.com/claims-fell-6000-and-the-four-week-average-still-rose-4250-august-2026/"
    published_at: "2026-08-21T00:00:00.000Z"
    retrieved_at: "2026-08-24T08:42:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
