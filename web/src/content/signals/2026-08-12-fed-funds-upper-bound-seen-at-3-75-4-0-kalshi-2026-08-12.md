---
signal_id: "CMSIG2026081201"
signal_slug: "fed-funds-upper-bound-seen-at-3-75-4-0-kalshi-2026-08-12"
headline: "Fed funds upper bound seen at 3.75-4.0%: Kalshi"
semantic_title: "Fed rate cut odds climb after jobs miss and CPI drop"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (next decision cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.3
  volume_24h_usd: 10.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.75-4.0% range, with 80% above 3.50% but only 30% above 4.0%."
  - "Jobs miss and CPI decline are consistent with the market pricing in meaningful cuts; the implied range sits well below current policy levels."
  - "Compare the near-term ladder (CM-EVT-4ZQLQPNH91) implying 3.50-3.75%, suggesting the market sees a multi-step cut path unfolding over successive meetings."
  - "Resolves via the Fed's official post-meeting rate announcement; any surprise hold or hawkish tone would sharply reprice the upper rungs."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A weak July jobs report showing 23,000 positions lost and falling CPI data have shifted market expectations toward earlier and deeper Fed rate cuts."
    publisher: "stockwirex.com"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://stockwirex.com/analysis/acf-group-fed-rate-expectations-august-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "stockwirex.com"
        source_url: "https://stockwirex.com/analysis/acf-group-fed-rate-expectations-august-2026/"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data is the only priced source here; the distribution shows a clear dovish lean with the 4.0% rung at just 30%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "stockwirex.com: Jobs Miss & Falling CPI Shift Fed Rate Bets"
    url: "https://stockwirex.com/analysis/acf-group-fed-rate-expectations-august-2026/"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
