---
signal_id: "CMSIG2026070201"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-02"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound consensus anchors at 3.50-3.75%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T13:28:56.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound (next cut cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.11
  volume_24h_usd: 612.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-07-29T18:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50% but only 11% above 3.75%, implying a floor near 3.50%."
  - "The weak June payroll print of 57,000 jobs is consistent with this dovish pricing, reinforcing expectations for meaningful Fed cuts ahead."
  - "Trading volume on this Kalshi ladder surged 12,921% day over day, signaling a sharp influx of fresh positioning after the jobs report."
  - "A companion Kalshi ladder (CM-EVT-MR57HVWJT3) implies a higher range of 3.75-4.0%, with only 57% above 3.75%, the spread between the two ladders reflects uncertainty over the pace of cuts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US economy added only 57,000 jobs in June, well below expectations, muddying the Fed's rate outlook."
    publisher: "americanbanker.com"
    published_at: "2026-07-02T13:28:56.000Z"
    source_url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "americanbanker.com"
        source_url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; extraordinary volume spike confirms the June NFP miss drove heavy fresh activity into rate-cut pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "americanbanker.com: US added 57,000 jobs in June; Fed outlook muddied | American Banker"
    url: "https://www.americanbanker.com/news/u-s-added-57-000-jobs-in-june-fed-outlook-muddied"
    published_at: "2026-07-02T13:28:56.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
