---
signal_id: "CMSIG2026061806"
signal_slug: "june-u-3-unemployment-rate-seen-4-2-4-3-kalshi-2026-06-18"
headline: "June U-3 unemployment rate seen 4.2-4.3%: Kalshi"
semantic_title: "June unemployment rate consensus clusters between 4.2 and 4.3 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-18T12:43:30.000Z"
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
  - "The Kalshi ladder implies a June 2026 unemployment rate in the 4.2-4.3% range, with 63% above 4.2% and only 31% above 4.3%."
  - "Low jobless claims data is consistent with the market's sub-4.3% central estimate, no sudden deterioration is being priced into the distribution."
  - "The ladder shows 99% above 3.9%, confirming the market sees no scenario in which June unemployment falls back to 2024 lows."
  - "Resolves via FRED official Bureau of Labor Statistics release; the June Employment Situation report is the settlement data point."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US initial jobless claims fell to 226,000 for the week ending June 14, extending a streak of historically low layoff filings."
    publisher: "ABC News"
    published_at: "2026-06-18T12:43:30.000Z"
    source_url: "https://ingest.abcnews.com/Business/wireStory/us-filings-unemployment-benefits-fall-226000-week-layoffs-133995874"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://ingest.abcnews.com/Business/wireStory/us-filings-unemployment-benefits-fall-226000-week-layoffs-133995874"
        retrieved_at: "2026-06-21T11:13:58+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder clusters tightly at 4.2-4.3%, consistent with a stable but softening labor market reading from current claims data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: US filings for unemployment benefits fall to 226,000 as layoffs remain"
    url: "https://ingest.abcnews.com/Business/wireStory/us-filings-unemployment-benefits-fall-226000-week-layoffs-133995874"
    published_at: "2026-06-18T12:43:30.000Z"
    retrieved_at: "2026-06-21T11:13:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
