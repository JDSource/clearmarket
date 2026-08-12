---
signal_id: "CMSIG2026081002"
signal_slug: "fed-funds-upper-bound-seen-at-3-50-3-75-kalshi-2026-08-10"
headline: "Fed funds upper bound seen at 3.50-3.75%: Kalshi"
semantic_title: "Near-term Fed cut odds stay heavily favored below 3.75%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-10T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound (near-term meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.42
  volume_24h_usd: 16509.41
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the near-term Fed funds upper bound in the 3.50-3.75% range, with 98% above 3.50% but only 42% above 3.75%."
  - "The 23,000 July payroll loss is consistent with the market's strong pricing for cuts; the 3.75% rung at 42% shows real uncertainty about how far and fast cuts go."
  - "The longer-horizon ladder (CM-EVT-MR57HVWJT3) implies the upper bound drifts higher to the 3.75-4.0% zone over subsequent meetings, suggesting a step-down cut path."
  - "Resolves via the Fed's official post-meeting announcement for the relevant decision date; a surprise hold would collapse the above-3.75% pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "July payrolls fell 23,000, a sharp deterioration that complicates the Federal Reserve's rate path and fuels rate-cut speculation."
    publisher: "111things.com"
    published_at: "2026-08-10T00:00:00.000Z"
    source_url: "https://111things.com/national/weak-july-jobs-report-complicates-the-federal-reserves-path-on-interest-rates/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "111things.com"
        source_url: "https://111things.com/national/weak-july-jobs-report-complicates-the-federal-reserves-path-on-interest-rates/"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "Kalshi is the sole priced venue on this ladder; the near-term distribution shows sharply tighter consensus than the longer-dated equivalent."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "111things.com: Weak July Jobs Report Complicates the Federal Reserve’s Path on Intere"
    url: "https://111things.com/national/weak-july-jobs-report-complicates-the-federal-reserves-path-on-interest-rates/"
    published_at: "2026-08-10T00:00:00.000Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
