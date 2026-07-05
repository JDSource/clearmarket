---
signal_id: "CMSIG2026070202"
signal_slug: "fed-cut-over-25bp-in-single-meeting-kalshi-9-2026-07-02"
headline: "Fed cut over 25bp in single meeting: Kalshi 9%"
semantic_title: "Fed jumbo cut consensus remains fractured near historic lows"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.089
  volume_24h_usd: 48.86
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 9% on the Federal Reserve cutting by more than 25 basis points in a single meeting, resolved via Federal Reserve data."
  - "Despite a sharply weak June payroll print, the market prices out an emergency-scale cut, consistent with the concurrent inflation concern flagged in the stagflation narrative."
  - "The 9% probability reflects the market pricing the Fed as constrained by inflation even as labor weakens, a paralysis signal, not a pivot signal."
  - "The companion Kalshi ladder (CM-EVT-PHWX2H6DM5) implies cuts will come gradually, with the upper bound seen settling in the 3.50-3.75% range rather than dropping abruptly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Stagflationary conditions, weak June jobs alongside sticky inflation, described as the Fed's nightmare scenario."
    publisher: "investing.com"
    published_at: "2026-07-02T00:00:00.000Z"
    source_url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Kalshi binary contract resolving via Federal Reserve; low probability is the market's verdict on Fed capacity to act aggressively in a stagflationary environment."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Fed’s Nightmare Scenario Has Arrived: Weak Jobs, High Inflation | Inve"
    url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
    published_at: "2026-07-02T00:00:00.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
