---
signal_id: "CMSIG2026061703"
signal_slug: "june-u-3-unemployment-implied-4-2-4-3-kalshi-ladder-2026-06-17"
headline: "June U-3 unemployment implied 4.2-4.3%: Kalshi ladder"
semantic_title: "June unemployment seen near 4.2-4.3 percent in Kalshi distribution"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
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
  - "Kalshi's ladder implies June unemployment near 4.2-4.3%: 63% above 4.2% but only 31% above 4.3%, with 99% above 3.9%."
  - "May's 172,000 payroll beat is consistent with the ladder's central estimate; the market is not pricing a sharp deterioration from May's level."
  - "Elevated jobless claims this week add modest upside risk to the 4.3% strike, though economists attribute the rise to seasonal distortions rather than structural weakness."
  - "Resolves via the Bureau of Labor Statistics Employment Situation report for June; the U-3 headline rate is the settlement data point."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US economy added 172,000 jobs in May, beating expectations, while weekly jobless claims remain elevated amid seasonal volatility."
    publisher: "Press Room"
    published_at: "2026-06-17T14:23:29.000Z"
    source_url: "https://finovoone.com/us-economy-added-172000-jobs-in-may-beating-expectations/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Press Room"
        source_url: "https://finovoone.com/us-economy-added-172000-jobs-in-may-beating-expectations/"
        retrieved_at: "2026-06-20T10:30:38+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution is tightly centered on 4.2-4.3%, consistent with a labor market that is softening gradually rather than breaking."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Press Room: US economy added 172,000 jobs in May, beating expectations | Finovoone"
    url: "https://finovoone.com/us-economy-added-172000-jobs-in-may-beating-expectations/"
    published_at: "2026-06-17T14:23:29.000Z"
    retrieved_at: "2026-06-20T10:30:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
