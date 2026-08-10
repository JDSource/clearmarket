---
signal_id: "CMSIG2026080702"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-08-07"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound stays near 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.35
  volume_24h_usd: 2417.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 3.50-3.75% range: 98% above 3.50%, but only 35% above 3.75%."
  - "The CBS News report that September hike bets have collapsed is consistent with the ladder: above 4.00% sits at just 1%, suggesting markets have fully abandoned hike pricing."
  - "The sharp cliff between 3.75% (35%) and 4.00% (1%) is the market's clearest signal that a hold is the dominant scenario, not a cut."
  - "Resolution via the Federal Reserve's official rate announcement; the named source in the contract is unspecified, but Fed policy decisions are public record."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Economists say the unexpected July job losses have sharply reduced the probability of a Federal Reserve rate hike in September."
    publisher: "cbsnews.com"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/federal-reserve-september-rate-decision-jobs-report-kevin-warsh/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/federal-reserve-september-rate-decision-jobs-report-kevin-warsh/"
        retrieved_at: "2026-08-10T09:14:34+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution aligns tightly with economist commentary post-July payrolls, showing no residual hike premium above 4 percent."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: The Fed was expected to hike interest rates in September. Don't bet on"
    url: "https://www.cbsnews.com/news/federal-reserve-september-rate-decision-jobs-report-kevin-warsh/"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-10T09:14:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
