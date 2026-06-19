---
signal_id: "CMSIG2026061706"
signal_slug: "june-u-3-unemployment-rate-seen-4-2-4-3-bls-ladder-2026-06-17"
headline: "June U-3 unemployment rate seen 4.2-4.3%: BLS ladder"
semantic_title: "June unemployment rate consensus hardens in the 4.2-4.3 percent band"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-17T14:23:29.000Z"
event_id: "CM-EVT-FJGT56DTV2"
event_slug: "kxu3-26jun"
event_question: "June 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUN-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in June?"
  current_price: 0.31
  volume_24h_usd: 0.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "The BLS unemployment ladder prices 63% above 4.2% and 31% above 4.3%, pinning the market-implied June rate in the 4.2-4.3% band."
  - "May's 172K payroll beat and 226K claims reading are consistent with a stable labor market in the 4.2-4.3% range the ladder implies."
  - "The ladder shows 99% above 3.9%, meaning the market fully rules out a return to prior low-unemployment conditions."
  - "Resolves via the Bureau of Labor Statistics Employment Situation report; the June print is the next catalyst that could reprice the distribution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US economy added 172,000 jobs in May, beating expectations, while weekly jobless claims fell to 226,000, suggesting a stable but cooling labor market."
    publisher: "Press Room"
    published_at: "2026-06-17T14:23:29.000Z"
    source_url: "https://finovoone.com/us-economy-added-172000-jobs-in-may-beating-expectations/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Press Room"
        source_url: "https://finovoone.com/us-economy-added-172000-jobs-in-may-beating-expectations/"
        retrieved_at: "2026-06-19T12:03:18+00:00"
  - type: "pm_response"
    notes: "The BLS-sourced ladder resolves on the official June Employment Situation release; current pricing is anchored by the May jobs beat and stable claims data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Press Room: US economy added 172,000 jobs in May, beating expectations | Finovoone"
    url: "https://finovoone.com/us-economy-added-172000-jobs-in-may-beating-expectations/"
    published_at: "2026-06-17T14:23:29.000Z"
    retrieved_at: "2026-06-19T12:03:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
