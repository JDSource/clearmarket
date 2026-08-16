---
signal_id: "CMSIG2026081406"
signal_slug: "democrats-win-us-house-2026-kalshi-86-2026-08-14"
headline: "Democrats win US House 2026: Kalshi 86%"
semantic_title: "Democrats winning the House stays heavily favored at 86%"
telemetry: "Kalshi 86%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.86
  volume_24h_usd: 6199.71
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning the US House at 86%, a heavily favored outcome resolved via the Library of Congress."
  - "State-level Democratic election-security moves signal confidence in a competitive cycle, consistent with an 86% market price."
  - "The companion Kalshi contract on Republicans retaining at least one chamber sits at 47%, implying the Senate race is viewed as genuinely competitive even as the House leans strongly Democratic."
  - "Resolves via the Library of Congress following the November 2026 midterm results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "State Democratic officials are legislating election security measures ahead of November, citing Trump's casting of doubt on election integrity and increased federal involvement."
    publisher: "Kevin Hardy"
    published_at: "2026-08-14T00:00:00.000Z"
    source_url: "https://stateline.org/2026/08/14/no-more-hypothetical-situations-state-officials-work-to-protect-elections-from-the-feds/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Hardy"
        source_url: "https://stateline.org/2026/08/14/no-more-hypothetical-situations-state-officials-work-to-protect-elections-from-the-feds/"
        retrieved_at: "2026-08-16T08:23:09+00:00"
  - type: "pm_response"
    notes: "Kalshi's 86% on Democrats winning the House contrasts with the 47% on Republicans holding at least one chamber, pointing to the Senate as the true battleground in market pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Hardy: No more 'hypothetical situations': States move to fortify elections ag"
    url: "https://stateline.org/2026/08/14/no-more-hypothetical-situations-state-officials-work-to-protect-elections-from-the-feds/"
    published_at: "2026-08-14T00:00:00.000Z"
    retrieved_at: "2026-08-16T08:23:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
